# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_umeng_finplus20220913 import models as main_models
from darabonba.model import DaraModel

class EncryptInvokeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.EncryptInvokeResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
        self.request_id = request_id
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

        if self.msg is not None:
            result['Msg'] = self.msg

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
            temp_model = main_models.EncryptInvokeResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class EncryptInvokeResponseBodyData(DaraModel):
    def __init__(
        self,
        encrypt_data: str = None,
        encrypt_key: str = None,
        sign: str = None,
    ):
        self.encrypt_data = encrypt_data
        self.encrypt_key = encrypt_key
        self.sign = sign

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.encrypt_data is not None:
            result['encryptData'] = self.encrypt_data

        if self.encrypt_key is not None:
            result['encryptKey'] = self.encrypt_key

        if self.sign is not None:
            result['sign'] = self.sign

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('encryptData') is not None:
            self.encrypt_data = m.get('encryptData')

        if m.get('encryptKey') is not None:
            self.encrypt_key = m.get('encryptKey')

        if m.get('sign') is not None:
            self.sign = m.get('sign')

        return self

