*** Settings ***
Library     RPA.Robocorp.Vault
Library     ExtendedExchange


*** Tasks ***
Example task
    ${secret}=    Get Secret    Exchange
    Authorize    username=${secret}[account]
    ...    password=${secret}[password]
    ...    autodiscover=False
    ...    server=outlook.office365.com
    @{optionals}=    Create List
    ...    optional1@domain.com
    ...    optional2@domain.com
    Create Calendar Event
    ...    subject=Lets Gather Around
    ...    body=We need decision on the important topics
    ...    meeting_start=06-05-2022 15:00
    ...    meeting_end=06-05-2022 16:00
    ...    required_attendees=name@domain.com,another@domain.com
    ...    optional_attendees=${optionals}
    Log    Done.
