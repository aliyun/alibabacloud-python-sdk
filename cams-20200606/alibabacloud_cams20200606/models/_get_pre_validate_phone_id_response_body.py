# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetPreValidatePhoneIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetPreValidatePhoneIdResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://www.alibabacloud.com/help/zh/cams/latest/api-error-codes).
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.GetPreValidatePhoneIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPreValidatePhoneIdResponseBodyData(DaraModel):
    def __init__(
        self,
        phone_number: str = None,
        phone_number_id: str = None,
    ):
        # The phone number.
        self.phone_number = phone_number
        # The ID of the phone number.
        self.phone_number_id = phone_number_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        if self.phone_number_id is not None:
            result['PhoneNumberId'] = self.phone_number_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        if m.get('PhoneNumberId') is not None:
            self.phone_number_id = m.get('PhoneNumberId')

        return self

