# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class CreateMcubeMiniTaskResponseBody(DaraModel):
    def __init__(
        self,
        create_mini_task_result: main_models.CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_mini_task_result = create_mini_task_result
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_mini_task_result:
            self.create_mini_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_mini_task_result is not None:
            result['CreateMiniTaskResult'] = self.create_mini_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateMiniTaskResult') is not None:
            temp_model = main_models.CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult()
            self.create_mini_task_result = temp_model.from_map(m.get('CreateMiniTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class CreateMcubeMiniTaskResponseBodyCreateMiniTaskResult(DaraModel):
    def __init__(
        self,
        mini_task_id: str = None,
        result_msg: str = None,
        success: bool = None,
    ):
        self.mini_task_id = mini_task_id
        self.result_msg = result_msg
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mini_task_id is not None:
            result['MiniTaskId'] = self.mini_task_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniTaskId') is not None:
            self.mini_task_id = m.get('MiniTaskId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

