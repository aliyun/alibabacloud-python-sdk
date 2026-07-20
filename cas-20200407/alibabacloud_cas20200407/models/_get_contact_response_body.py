# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContactResponseBody(DaraModel):
    def __init__(
        self,
        contact_id: int = None,
        email: str = None,
        email_status: int = None,
        id_card: str = None,
        mobile: str = None,
        mobile_status: int = None,
        name: str = None,
        request_id: str = None,
        webhooks: str = None,
    ):
        # The contact ID.
        self.contact_id = contact_id
        # The email address of the contact.
        self.email = email
        # Indicates whether the email address is verified.
        self.email_status = email_status
        # The ID card number of the contact. This parameter is required for the CFCA certificate brand and is not required for other brands.
        self.id_card = id_card
        # The phone number of the contact.
        self.mobile = mobile
        # Indicates whether the phone number is verified.
        self.mobile_status = mobile_status
        # The name of the certificate contact.
        self.name = name
        # The request ID.
        self.request_id = request_id
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

        if self.email_status is not None:
            result['EmailStatus'] = self.email_status

        if self.id_card is not None:
            result['IdCard'] = self.id_card

        if self.mobile is not None:
            result['Mobile'] = self.mobile

        if self.mobile_status is not None:
            result['MobileStatus'] = self.mobile_status

        if self.name is not None:
            result['Name'] = self.name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.webhooks is not None:
            result['Webhooks'] = self.webhooks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EmailStatus') is not None:
            self.email_status = m.get('EmailStatus')

        if m.get('IdCard') is not None:
            self.id_card = m.get('IdCard')

        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')

        if m.get('MobileStatus') is not None:
            self.mobile_status = m.get('MobileStatus')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Webhooks') is not None:
            self.webhooks = m.get('Webhooks')

        return self

