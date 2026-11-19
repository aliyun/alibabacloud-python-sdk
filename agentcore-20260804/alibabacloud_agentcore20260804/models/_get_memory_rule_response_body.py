# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class GetMemoryRuleResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.GetMemoryRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # data
        self.data = data
        # httpStatusCode
        self.http_status_code = http_status_code
        # message
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.GetMemoryRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class GetMemoryRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        enabled: bool = None,
        failed_task_count: int = None,
        last_executed_at: str = None,
        last_task_id: str = None,
        last_task_status: str = None,
        memory_store_id: str = None,
        name: str = None,
        rule_id: str = None,
        strategy: main_models.GetMemoryRuleResponseBodyDataStrategy = None,
        succeeded_task_count: int = None,
        task_count: int = None,
        updated_at: str = None,
    ):
        # createdAt
        # 
        # This parameter is required.
        self.created_at = created_at
        # description
        self.description = description
        # enabled
        # 
        # This parameter is required.
        self.enabled = enabled
        # failedTaskCount
        # 
        # This parameter is required.
        self.failed_task_count = failed_task_count
        # The time when the last execution started, in RFC 3339 format.
        self.last_executed_at = last_executed_at
        # lastTaskId
        self.last_task_id = last_task_id
        # lastTaskStatus
        self.last_task_status = last_task_status
        # memoryStoreId
        # 
        # This parameter is required.
        self.memory_store_id = memory_store_id
        # name
        # 
        # This parameter is required.
        self.name = name
        # ruleId
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # strategy
        # 
        # This parameter is required.
        self.strategy = strategy
        # succeededTaskCount
        # 
        # This parameter is required.
        self.succeeded_task_count = succeeded_task_count
        # The total number of distinct task IDs that have started execution. Retries are not counted separately.
        # 
        # This parameter is required.
        self.task_count = task_count
        # updatedAt
        # 
        # This parameter is required.
        self.updated_at = updated_at

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.failed_task_count is not None:
            result['failedTaskCount'] = self.failed_task_count

        if self.last_executed_at is not None:
            result['lastExecutedAt'] = self.last_executed_at

        if self.last_task_id is not None:
            result['lastTaskId'] = self.last_task_id

        if self.last_task_status is not None:
            result['lastTaskStatus'] = self.last_task_status

        if self.memory_store_id is not None:
            result['memoryStoreId'] = self.memory_store_id

        if self.name is not None:
            result['name'] = self.name

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        if self.succeeded_task_count is not None:
            result['succeededTaskCount'] = self.succeeded_task_count

        if self.task_count is not None:
            result['taskCount'] = self.task_count

        if self.updated_at is not None:
            result['updatedAt'] = self.updated_at

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('failedTaskCount') is not None:
            self.failed_task_count = m.get('failedTaskCount')

        if m.get('lastExecutedAt') is not None:
            self.last_executed_at = m.get('lastExecutedAt')

        if m.get('lastTaskId') is not None:
            self.last_task_id = m.get('lastTaskId')

        if m.get('lastTaskStatus') is not None:
            self.last_task_status = m.get('lastTaskStatus')

        if m.get('memoryStoreId') is not None:
            self.memory_store_id = m.get('memoryStoreId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('strategy') is not None:
            temp_model = main_models.GetMemoryRuleResponseBodyDataStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        if m.get('succeededTaskCount') is not None:
            self.succeeded_task_count = m.get('succeededTaskCount')

        if m.get('taskCount') is not None:
            self.task_count = m.get('taskCount')

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class GetMemoryRuleResponseBodyDataStrategy(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        type: str = None,
    ):
        # The strategy-level instruction. It takes effect together with the store-level instruction. If a conflict occurs, this field takes precedence.
        self.instruction = instruction
        # type
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruction is not None:
            result['instruction'] = self.instruction

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instruction') is not None:
            self.instruction = m.get('instruction')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

