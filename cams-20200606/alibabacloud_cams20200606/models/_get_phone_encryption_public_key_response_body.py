# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cams20200606 import models as main_models
from darabonba.model import DaraModel

class GetPhoneEncryptionPublicKeyResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: str = None,
        code: str = None,
        data: main_models.GetPhoneEncryptionPublicKeyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.access_denied_detail = access_denied_detail
        # The response code.
        # 
        # *   The value OK indicates that the request was successful.
        # *   For more information about other response codes, see [Error codes](https://help.aliyun.com/document_detail/196974.html).
        self.code = code
        # The returned data.
        self.data = data
        # Error description information.
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
            temp_model = main_models.GetPhoneEncryptionPublicKeyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetPhoneEncryptionPublicKeyResponseBodyData(DaraModel):
    def __init__(
        self,
        encryption_public_key: str = None,
        encryption_public_key_status: str = None,
        phone_number: str = None,
    ):
        # The public key.
        self.encryption_public_key = encryption_public_key
        # The validity state of the public key. Valid values:
        # 
        # *   MISMATCH: The public key is invalid.
        # *   VALID: The public key is valid.
        self.encryption_public_key_status = encryption_public_key_status
        # The phone number.
        self.phone_number = phone_number

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encryption_public_key is not None:
            result['EncryptionPublicKey'] = self.encryption_public_key

        if self.encryption_public_key_status is not None:
            result['EncryptionPublicKeyStatus'] = self.encryption_public_key_status

        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptionPublicKey') is not None:
            self.encryption_public_key = m.get('EncryptionPublicKey')

        if m.get('EncryptionPublicKeyStatus') is not None:
            self.encryption_public_key_status = m.get('EncryptionPublicKeyStatus')

        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')

        return self

