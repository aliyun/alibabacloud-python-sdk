# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class InvalidPhoneNumberFilterResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.InvalidPhoneNumberFilterResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
    ):
        # The response code. Valid values:
        # 
        # *   **OK**: The request is successful.
        # *   **MobileNumberIllegal**: The phone number is invalid.
        # *   **EncyrptTypeIllegal**: The encryption type is invalid.
        # *   **MobileNumberTypeNotMatch**: The phone number does not match the encryption type.
        # *   **CarrierIllegal**: The carrier type is invalid.
        # *   **AuthCodeNotExist**: The authorization code does not exist.
        # *   **PortabilityNumberNotSupported**: Mobile number portability is not supported.
        # *   **Unknown**: An unknown exception occurred.
        # *   **AuthCodeAndApiNotMatch**: A system exception occurred.
        # *   **AuthCodeAndApiNotMatch**: The authorization code does not match the API operation.
        # *   **RequestFrequencyLimit**: Repeated queries for the same phone number at a high frequency within a short period of time are prohibited due to restrictions that are set by carriers. If this error code is returned, please try again later.
        self.code = code
        # Details about the returned entries.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.InvalidPhoneNumberFilterResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class InvalidPhoneNumberFilterResponseBodyData(DaraModel):
    def __init__(
        self,
        code: str = None,
        encrypted_number: str = None,
        expire_time: str = None,
        original_number: str = None,
    ):
        # The returned filter results.
        # 
        # *   **YES**: the valid phone number. The mappings are returned.
        # *   **NO**: the invalid phone number. No mappings are returned.
        self.code = code
        # The encrypted phone number.
        self.encrypted_number = encrypted_number
        # The time when the phone number expires.
        self.expire_time = expire_time
        # The original phone number.
        self.original_number = original_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.encrypted_number is not None:
            result['EncryptedNumber'] = self.encrypted_number

        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time

        if self.original_number is not None:
            result['OriginalNumber'] = self.original_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EncryptedNumber') is not None:
            self.encrypted_number = m.get('EncryptedNumber')

        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')

        if m.get('OriginalNumber') is not None:
            self.original_number = m.get('OriginalNumber')

        return self

