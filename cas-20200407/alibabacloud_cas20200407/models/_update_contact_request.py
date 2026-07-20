# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContactRequest(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        email: str = None,
        idcard: str = None,
        mobile: str = None,
        name: str = None,
        webhooks: str = None,
    ):
        # The contact ID.
        # 
        # This parameter is required.
        self.contact_id = contact_id
        # The email address of the contact.
        self.email = email
        # The ID card number of the contact. This parameter is required for the CFCA certificate brand and is not required for other brands.
        self.idcard = idcard
        # The phone number of the contact.
        self.mobile = mobile
        # The name of the certificate contact.
        self.name = name
        # The webhook URLs of DingTalk, WeCom, or Lark chatbots. The value is a string in list format.
        self.webhooks = webhooks

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.email is not None:
            result['Email'] = self.email

        if self.idcard is not None:
            result['Idcard'] = self.idcard

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.name is not None:
            result['Name'] = self.name

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('Idcard') is not None:
            self.idcard = m.get('Idcard')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

