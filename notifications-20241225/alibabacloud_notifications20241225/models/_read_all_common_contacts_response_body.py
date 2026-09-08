# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadAllCommonContactsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ReadAllCommonContactsResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The query result.
        self.data = data
        # The result message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

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

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ReadAllCommonContactsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class ReadAllCommonContactsResponseBodyData(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        contact_email: str = None,
        contact_id: int = None,
        contact_mobile: str = None,
        contact_name: str = None,
        email_confirmed: bool = None,
        mobile_confirmed: bool = None,
        position: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The email address of the contact.
        self.contact_email = contact_email
        # The contact ID in the Account Center. A value of 0 indicates the account contact.
        self.contact_id = contact_id
        # The mobile phone number of the contact in the Account Center (masked).
        self.contact_mobile = contact_mobile
        # The contact name in the Account Center.
        self.contact_name = contact_name
        # Indicates whether the email address is verified.
        self.email_confirmed = email_confirmed
        # Indicates whether the mobile phone number of the contact in the Account Center is verified.
        self.mobile_confirmed = mobile_confirmed
        # The position of the contact in the Account Center.
        self.position = position

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.contact_email is not None:
            result['ContactEmail'] = self.contact_email

        if self.contact_id is not None:
            result['ContactId'] = self.contact_id

        if self.contact_mobile is not None:
            result['ContactMobile'] = self.contact_mobile

        if self.contact_name is not None:
            result['ContactName'] = self.contact_name

        if self.email_confirmed is not None:
            result['EmailConfirmed'] = self.email_confirmed

        if self.mobile_confirmed is not None:
            result['MobileConfirmed'] = self.mobile_confirmed

        if self.position is not None:
            result['Position'] = self.position

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ContactEmail') is not None:
            self.contact_email = m.get('ContactEmail')

        if m.get('ContactId') is not None:
            self.contact_id = m.get('ContactId')

        if m.get('ContactMobile') is not None:
            self.contact_mobile = m.get('ContactMobile')

        if m.get('ContactName') is not None:
            self.contact_name = m.get('ContactName')

        if m.get('EmailConfirmed') is not None:
            self.email_confirmed = m.get('EmailConfirmed')

        if m.get('MobileConfirmed') is not None:
            self.mobile_confirmed = m.get('MobileConfirmed')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        return self

