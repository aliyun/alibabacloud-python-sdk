# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SendEmailVerificationForMessageContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: str = None,
        email_address: str = None,
    ):
        # The ID of the contact.
        self.contact_id = contact_id
        # The email address of the contact.
        # 
        # The specified email address must be the one you specify when you call [AddMessageContact](~~AddMessageContact~~).
        self.email_address = email_address

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.email_address is not None:
            result['EmailAddress'] = self.email_address

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('EmailAddress') is not None:
            self.email_address = m.get('EmailAddress')

        return self

