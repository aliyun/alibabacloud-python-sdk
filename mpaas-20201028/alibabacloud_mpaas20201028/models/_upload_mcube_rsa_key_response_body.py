# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class UploadMcubeRsaKeyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        upload_rsa_result: main_models.UploadMcubeRsaKeyResponseBodyUploadRsaResult = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.upload_rsa_result = upload_rsa_result

    def validate(self):
        if self.upload_rsa_result:
            self.upload_rsa_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        if self.upload_rsa_result is not None:
            result['UploadRsaResult'] = self.upload_rsa_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('UploadRsaResult') is not None:
            temp_model = main_models.UploadMcubeRsaKeyResponseBodyUploadRsaResult()
            self.upload_rsa_result = temp_model.from_map(m.get('UploadRsaResult'))

        return self

class UploadMcubeRsaKeyResponseBodyUploadRsaResult(DaraModel):
    def __init__(
        self,
        data: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.data = data
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

