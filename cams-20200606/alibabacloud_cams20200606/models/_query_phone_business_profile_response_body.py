# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class QueryPhoneBusinessProfileResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.QueryPhoneBusinessProfileResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The HTTP status code returned.
        # 
        # *   A value of OK indicates that the call is successful.
        # *   Other values indicate that the call fails. For more information, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail

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
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryPhoneBusinessProfileResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryPhoneBusinessProfileResponseBodyData(DaraModel):
    def __init__(
        self,
        about: str = None,
        address: str = None,
        description: str = None,
        email: str = None,
        profile_picture_url: str = None,
        vertical: str = None,
        websites: List[str] = None,
    ):
        # Regarding.
        self.about = about
        # The address.
        self.address = address
        # The description.
        self.description = description
        # The email address.
        self.email = email
        # The profile picture.
        self.profile_picture_url = profile_picture_url
        # The industry.
        self.vertical = vertical
        # The website.
        self.websites = websites

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.about is not None:
            result['About'] = self.about

        if self.address is not None:
            result['Address'] = self.address

        if self.description is not None:
            result['Description'] = self.description

        if self.email is not None:
            result['Email'] = self.email

        if self.profile_picture_url is not None:
            result['ProfilePictureUrl'] = self.profile_picture_url

        if self.vertical is not None:
            result['Vertical'] = self.vertical

        if self.websites is not None:
            result['Websites'] = self.websites

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('About') is not None:
            self.about = m.get('About')

        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('ProfilePictureUrl') is not None:
            self.profile_picture_url = m.get('ProfilePictureUrl')

        if m.get('Vertical') is not None:
            self.vertical = m.get('Vertical')

        if m.get('Websites') is not None:
            self.websites = m.get('Websites')

        return self

