# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class CreateMcubeWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        create_whitelist_result: main_models.CreateMcubeWhitelistResponseBodyCreateWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_whitelist_result = create_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_whitelist_result:
            self.create_whitelist_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_whitelist_result is not None:
            result['CreateWhitelistResult'] = self.create_whitelist_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateWhitelistResult') is not None:
            temp_model = main_models.CreateMcubeWhitelistResponseBodyCreateWhitelistResult()
            self.create_whitelist_result = temp_model.from_map(m.get('CreateWhitelistResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class CreateMcubeWhitelistResponseBodyCreateWhitelistResult(DaraModel):
    def __init__(
        self,
        result_msg: str = None,
        success: bool = None,
        whitelist_id: str = None,
    ):
        self.result_msg = result_msg
        self.success = success
        self.whitelist_id = whitelist_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        if self.whitelist_id is not None:
            result['WhitelistId'] = self.whitelist_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('WhitelistId') is not None:
            self.whitelist_id = m.get('WhitelistId')

        return self

