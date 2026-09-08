# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadMarketingPreferenceResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ReadMarketingPreferenceResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned by the system. For more information about error codes, see error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The message.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful. A value of true indicates success. A value of false indicates failure.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReadMarketingPreferenceResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadMarketingPreferenceResponseBodyData(DaraModel):
    def __init__(
        self,
        allow_marketing: bool = None,
        contact_email: str = None,
        contact_id: int = None,
        contact_mobile: str = None,
        contact_name: str = None,
        position: str = None,
    ):
        # Indicates whether notifications are allowed.
        self.allow_marketing = allow_marketing
        # The email address of the contact in Account Center.
        self.contact_email = contact_email
        # The contact ID in Account Center. A value of 0 indicates the account contact.
        self.contact_id = contact_id
        # The mobile phone number of the contact in Account Center (masked).
        self.contact_mobile = contact_mobile
        # The name of the contact in Account Center.
        self.contact_name = contact_name
        # The position of the contact in Account Center.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_marketing is not None:
            result['AllowMarketing'] = self.allow_marketing

        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowMarketing') is not None:
            self.allow_marketing = m.get('AllowMarketing')

        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

