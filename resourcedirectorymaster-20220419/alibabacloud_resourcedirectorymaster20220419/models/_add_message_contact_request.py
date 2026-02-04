# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddMessageContactRequest(DaraModel):
    def __init__(
        self,
        email_address: str = None,
        message_types: List[str] = None,
        name: str = None,
        phone_number: str = None,
        title: str = None,
    ):
        # The email address of the contact.
        # 
        # After you specify an email address, you need to call [SendEmailVerificationForMessageContact](~~SendEmailVerificationForMessageContact~~) to send verification information to the email address. After the verification is passed, the email address takes effect.
        # 
        # This parameter is required.
        self.email_address = email_address
        # The types of messages received by the contact.
        # 
        # This parameter is required.
        self.message_types = message_types
        # The name of the contact.
        # 
        # The name must be unique in your resource directory.
        # 
        # The name must be 2 to 12 characters in length and can contain only letters.
        # 
        # This parameter is required.
        self.name = name
        # The mobile phone number of the contact.
        # 
        # Specify the mobile phone number in the `<Country code>-<Mobile phone number>` format.
        # 
        # > Only mobile phone numbers in the `86-<Mobile phone number>` format in the Chinese mainland are supported.
        # 
        # After you specify a mobile phone number, you need to call [SendPhoneVerificationForMessageContact](~~SendPhoneVerificationForMessageContact~~) to send verification information to the mobile phone number. After the verification is passed, the mobile phone number takes effect.
        self.phone_number = phone_number
        # The job title of the contact.
        # 
        # Valid values:
        # 
        # *   FinanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   TechnicalDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   MaintenanceDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   CEO
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   ProjectDirector
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Other
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.email_address is not None:
            result['EmailAddress'] = self.email_address

        if self.message_types is not None:
            result['MessageTypes'] = self.message_types

        if self.name is not None:
            result['Name'] = self.name

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')

        if m.get('MessageTypes') is not None:
            self.message_types = m.get('MessageTypes')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

