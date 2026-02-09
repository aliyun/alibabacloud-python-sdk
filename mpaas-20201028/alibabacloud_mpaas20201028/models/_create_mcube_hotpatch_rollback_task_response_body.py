# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class CreateMcubeHotpatchRollbackTaskResponseBody(DaraModel):
    def __init__(
        self,
        create_hotpatch_rollback_task_result: main_models.CreateMcubeHotpatchRollbackTaskResponseBodyCreateHotpatchRollbackTaskResult = None,
        request_id: str = None,
        result_code: str = None,
        result_message: str = None,
    ):
        self.create_hotpatch_rollback_task_result = create_hotpatch_rollback_task_result
        # Id of the request
        self.request_id = request_id
        self.result_code = result_code
        self.result_message = result_message

    def validate(self):
        if self.create_hotpatch_rollback_task_result:
            self.create_hotpatch_rollback_task_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_hotpatch_rollback_task_result is not None:
            result['CreateHotpatchRollbackTaskResult'] = self.create_hotpatch_rollback_task_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_code is not None:
            result['ResultCode'] = self.result_code

        if self.result_message is not None:
            result['ResultMessage'] = self.result_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateHotpatchRollbackTaskResult') is not None:
            temp_model = main_models.CreateMcubeHotpatchRollbackTaskResponseBodyCreateHotpatchRollbackTaskResult()
            self.create_hotpatch_rollback_task_result = temp_model.from_map(m.get('CreateHotpatchRollbackTaskResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCode') is not None:
            self.result_code = m.get('ResultCode')

        if m.get('ResultMessage') is not None:
            self.result_message = m.get('ResultMessage')

        return self

class CreateMcubeHotpatchRollbackTaskResponseBodyCreateHotpatchRollbackTaskResult(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_msg: str = None,
        rollback_task_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.result_msg = result_msg
        self.rollback_task_id = rollback_task_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_msg is not None:
            result['ResultMsg'] = self.result_msg

        if self.rollback_task_id is not None:
            result['RollbackTaskId'] = self.rollback_task_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultMsg') is not None:
            self.result_msg = m.get('ResultMsg')

        if m.get('RollbackTaskId') is not None:
            self.rollback_task_id = m.get('RollbackTaskId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

