# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class CreateChatappMigrationInitiateResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.CreateChatappMigrationInitiateResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # Details about the access denial.
        self.access_denied_detail = access_denied_detail
        # The status code of the request.
        # 
        # - A value of OK indicates that the request was successful.
        # 
        # - For other error codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # The error message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            self.access_denied_detail = m.get('AccessDeniedDetail')

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.CreateChatappMigrationInitiateResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateChatappMigrationInitiateResponseBodyData(DaraModel):
    def __init__(
        self,
        id: str = None,
        phone_number: str = None,
        status: str = None,
    ):
        # The ID of the phone number.
        self.id = id
        # The phone number.
        self.phone_number = phone_number
        # The status of the phone number.
        # Valid value: MIGRATING: The phone number is being migrated.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

