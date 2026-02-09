# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class UpdateMcubeWhitelistResponseBody(DaraModel):
    def __init__(
        self,
        add_whitelist_result: main_models.UpdateMcubeWhitelistResponseBodyAddWhitelistResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.add_whitelist_result = add_whitelist_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.add_whitelist_result:
            self.add_whitelist_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_whitelist_result is not None:
            result['AddWhitelistResult'] = self.add_whitelist_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWhitelistResult') is not None:
            temp_model = main_models.UpdateMcubeWhitelistResponseBodyAddWhitelistResult()
            self.add_whitelist_result = temp_model.from_map(m.get('AddWhitelistResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class UpdateMcubeWhitelistResponseBodyAddWhitelistResult(DaraModel):
    def __init__(
        self,
        add_whitelist_info: main_models.UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.add_whitelist_info = add_whitelist_info
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        if self.add_whitelist_info:
            self.add_whitelist_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_whitelist_info is not None:
            result['AddWhitelistInfo'] = self.add_whitelist_info.to_map()

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddWhitelistInfo') is not None:
            temp_model = main_models.UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo()
            self.add_whitelist_info = temp_model.from_map(m.get('AddWhitelistInfo'))

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateMcubeWhitelistResponseBodyAddWhitelistResultAddWhitelistInfo(DaraModel):
    def __init__(
        self,
        fail_num: int = None,
        fail_user_ids: str = None,
        success_num: int = None,
    ):
        self.fail_num = fail_num
        self.fail_user_ids = fail_user_ids
        self.success_num = success_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_num is not None:
            result['FailNum'] = self.fail_num

        if self.fail_user_ids is not None:
            result['FailUserIds'] = self.fail_user_ids

        if self.success_num is not None:
            result['SuccessNum'] = self.success_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailNum') is not None:
            self.fail_num = m.get('FailNum')

        if m.get('FailUserIds') is not None:
            self.fail_user_ids = m.get('FailUserIds')

        if m.get('SuccessNum') is not None:
            self.success_num = m.get('SuccessNum')

        return self

