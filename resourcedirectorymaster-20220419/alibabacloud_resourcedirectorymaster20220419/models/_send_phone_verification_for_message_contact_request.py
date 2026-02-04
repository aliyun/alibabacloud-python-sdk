# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendPhoneVerificationForMessageContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        phone_number: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The mobile phone number of the contact.
        # 
        # The value must be in the `<Country code>-<Mobile phone number>` format.
        # 
        # The specified mobile phone number must be the one you specify when you call the [AddMessageContact](~~AddMessageContact~~) operation.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        return self

