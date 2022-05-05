from RPA.Email.Exchange import Exchange
from exchangelib import CalendarItem
from exchangelib.items import (
    SEND_TO_ALL_AND_SAVE_COPY,
)
from typing import List, Optional, Union


class ExtendedExchange(Exchange):
    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def create_calendar_event(
        self,
        subject: str,
        body: str,
        meeting_start: str,
        meeting_end: str,
        required_attendees: Union[str, List],
        optional_attendees: Optional[Union[str, List]] = None,
    ):
        """Create calendar invite for authorized account

        Example.

        .. code:: robotframework

            @{optionals}=   Create List
            ...   optional1@domain.com
            ...   optional2@domain.com
            Create Calendar Event
            ...    subject=Lets Gather Around
            ...    body=We need decision on the important topics
            ...    meeting_start=6-5-2022 15:00
            ...    meeting_end=6-5-2022 16:00
            ...    required_attendees=name@domain.com,another@domain.com
            ...    optional_attendees=${optionals}

        :param subject: string for calendar meeting subject
        :param body: string for calendar meeting body
        :param meeting_start: '%d-%m-%Y %H:%M' or %d-%m-%Y' formatted datetime
        :param meeting_end: '%d-%m-%Y %H:%M' or %d-%m-%Y' formatted datetime
        :param required_attendees: comma separated string or list of required
         attendees (emails)
        :param optional_attendees: comma separated string or list of optional
         attendees (emails). Default `None`.
        """
        meeting_arguments = {
            "account": self.account,
            "folder": self.account.calendar,
            "start": self._parse_date_from_string(meeting_start),
            "end": self._parse_date_from_string(meeting_end),
            "subject": subject,
            "body": body,
            "required_attendees": required_attendees.split(",")
            if isinstance(required_attendees, str)
            else required_attendees,
        }
        if optional_attendees:
            meeting_arguments["optional_attendees"] = (
                optional_attendees.split(",")
                if isinstance(optional_attendees, str)
                else optional_attendees
            )
        item = CalendarItem(**meeting_arguments)
        item.save(send_meeting_invitations=SEND_TO_ALL_AND_SAVE_COPY)
