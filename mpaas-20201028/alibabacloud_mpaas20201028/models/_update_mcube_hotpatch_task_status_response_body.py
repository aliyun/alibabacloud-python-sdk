# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class UpdateMcubeHotpatchTaskStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
        update_hotpatch_task_status_result: main_models.UpdateMcubeHotpatchTaskStatusResponseBodyUpdateHotpatchTaskStatusResult = None,
    ):
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message
        self.update_hotpatch_task_status_result = update_hotpatch_task_status_result

    def validate(self):
        if self.update_hotpatch_task_status_result:
            self.update_hotpatch_task_status_result.validate()

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

        if self.update_hotpatch_task_status_result is not None:
            result['UpdateHotpatchTaskStatusResult'] = self.update_hotpatch_task_status_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        if m.get('UpdateHotpatchTaskStatusResult') is not None:
            temp_model = main_models.UpdateMcubeHotpatchTaskStatusResponseBodyUpdateHotpatchTaskStatusResult()
            self.update_hotpatch_task_status_result = temp_model.from_map(m.get('UpdateHotpatchTaskStatusResult'))

        return self

class UpdateMcubeHotpatchTaskStatusResponseBodyUpdateHotpatchTaskStatusResult(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        request_id: str = None,
        result: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.error_code = error_code
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result is not None:
            result['Result'] = self.result

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

