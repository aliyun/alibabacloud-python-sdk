# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_winnexo20260512 import models as main_models
from darabonba.model import DaraModel

class ExecuteScheduledTaskResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        execution_id: str = None,
        message: str = None,
        request_id: str = None,
        task_execution: main_models.ExecuteScheduledTaskResponseBodyTaskExecution = None,
    ):
        # 业务状态码：成功为 200，失败为后端错误码
        self.code = code
        # 执行记录 ID
        self.execution_id = execution_id
        # 错误描述，成功时为空
        self.message = message
        # 请求追踪 ID
        self.request_id = request_id
        self.task_execution = task_execution

    def validate(self):
        if self.task_execution:
            self.task_execution.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.task_execution is not None:
            result['taskExecution'] = self.task_execution.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('taskExecution') is not None:
            temp_model = main_models.ExecuteScheduledTaskResponseBodyTaskExecution()
            self.task_execution = temp_model.from_map(m.get('taskExecution'))

        return self

class ExecuteScheduledTaskResponseBodyTaskExecution(DaraModel):
    def __init__(
        self,
        auto_preference: str = None,
        billing_id: str = None,
        collaboration_group_id: str = None,
        enable_web_search: bool = None,
        execution_id: str = None,
        model: str = None,
        operating_object_name: List[str] = None,
        skill_codes: List[str] = None,
        task_id: str = None,
        task_name: str = None,
        task_understand: str = None,
        tenant_id: str = None,
        user_id: str = None,
    ):
        # 任务 AUTO 偏好：none=默认、performance=效果优先、credit=成本优先
        self.auto_preference = auto_preference
        self.billing_id = billing_id
        self.collaboration_group_id = collaboration_group_id
        self.enable_web_search = enable_web_search
        self.execution_id = execution_id
        # 执行模型档位
        self.model = model
        self.operating_object_name = operating_object_name
        self.skill_codes = skill_codes
        self.task_id = task_id
        self.task_name = task_name
        self.task_understand = task_understand
        self.tenant_id = tenant_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_preference is not None:
            result['autoPreference'] = self.auto_preference

        if self.billing_id is not None:
            result['billingId'] = self.billing_id

        if self.collaboration_group_id is not None:
            result['collaborationGroupId'] = self.collaboration_group_id

        if self.enable_web_search is not None:
            result['enableWebSearch'] = self.enable_web_search

        if self.execution_id is not None:
            result['executionId'] = self.execution_id

        if self.model is not None:
            result['model'] = self.model

        if self.operating_object_name is not None:
            result['operatingObjectName'] = self.operating_object_name

        if self.skill_codes is not None:
            result['skillCodes'] = self.skill_codes

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.task_name is not None:
            result['taskName'] = self.task_name

        if self.task_understand is not None:
            result['taskUnderstand'] = self.task_understand

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoPreference') is not None:
            self.auto_preference = m.get('autoPreference')

        if m.get('billingId') is not None:
            self.billing_id = m.get('billingId')

        if m.get('collaborationGroupId') is not None:
            self.collaboration_group_id = m.get('collaborationGroupId')

        if m.get('enableWebSearch') is not None:
            self.enable_web_search = m.get('enableWebSearch')

        if m.get('executionId') is not None:
            self.execution_id = m.get('executionId')

        if m.get('model') is not None:
            self.model = m.get('model')

        if m.get('operatingObjectName') is not None:
            self.operating_object_name = m.get('operatingObjectName')

        if m.get('skillCodes') is not None:
            self.skill_codes = m.get('skillCodes')

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('taskName') is not None:
            self.task_name = m.get('taskName')

        if m.get('taskUnderstand') is not None:
            self.task_understand = m.get('taskUnderstand')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

