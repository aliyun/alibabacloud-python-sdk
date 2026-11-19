# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListMemoryTasksResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListMemoryTasksResponseBodyItems] = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # items
        self.items = items
        # maxResults
        self.max_results = max_results
        # message
        self.message = message
        # nextToken
        self.next_token = next_token
        # requestId
        self.request_id = request_id
        # success
        self.success = success
        # totalCount
        self.total_count = total_count

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        result['items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['items'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.message is not None:
            result['message'] = self.message

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        self.items = []
        if m.get('items') is not None:
            for k1 in m.get('items'):
                temp_model = main_models.ListMemoryTasksResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListMemoryTasksResponseBodyItems(DaraModel):
    def __init__(
        self,
        changes: List[main_models.ListMemoryTasksResponseBodyItemsChanges] = None,
        created_at: str = None,
        error: main_models.ListMemoryTasksResponseBodyItemsError = None,
        finished_at: str = None,
        input_message_count: int = None,
        input_token_count: int = None,
        memories: List[main_models.ListMemoryTasksResponseBodyItemsMemories] = None,
        started_at: str = None,
        status: str = None,
        strategy_config: main_models.ListMemoryTasksResponseBodyItemsStrategyConfig = None,
        task_id: str = None,
        trigger_type: str = None,
    ):
        # changes
        self.changes = changes
        # createdAt
        # 
        # This parameter is required.
        self.created_at = created_at
        # error
        self.error = error
        # finishedAt
        self.finished_at = finished_at
        # inputMessageCount
        # 
        # This parameter is required.
        self.input_message_count = input_message_count
        # inputTokenCount
        # 
        # This parameter is required.
        self.input_token_count = input_token_count
        # memories
        # 
        # This parameter is required.
        self.memories = memories
        # startedAt
        self.started_at = started_at
        # status
        # 
        # This parameter is required.
        self.status = status
        # strategyConfig
        # 
        # This parameter is required.
        self.strategy_config = strategy_config
        # taskId
        # 
        # This parameter is required.
        self.task_id = task_id
        # triggerType
        # 
        # This parameter is required.
        self.trigger_type = trigger_type

    def validate(self):
        if self.changes:
            for v1 in self.changes:
                 if v1:
                    v1.validate()
        if self.error:
            self.error.validate()
        if self.memories:
            for v1 in self.memories:
                 if v1:
                    v1.validate()
        if self.strategy_config:
            self.strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['changes'] = []
        if self.changes is not None:
            for k1 in self.changes:
                result['changes'].append(k1.to_map() if k1 else None)

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.error is not None:
            result['error'] = self.error.to_map()

        if self.finished_at is not None:
            result['finishedAt'] = self.finished_at

        if self.input_message_count is not None:
            result['inputMessageCount'] = self.input_message_count

        if self.input_token_count is not None:
            result['inputTokenCount'] = self.input_token_count

        result['memories'] = []
        if self.memories is not None:
            for k1 in self.memories:
                result['memories'].append(k1.to_map() if k1 else None)

        if self.started_at is not None:
            result['startedAt'] = self.started_at

        if self.status is not None:
            result['status'] = self.status

        if self.strategy_config is not None:
            result['strategyConfig'] = self.strategy_config.to_map()

        if self.task_id is not None:
            result['taskId'] = self.task_id

        if self.trigger_type is not None:
            result['triggerType'] = self.trigger_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.changes = []
        if m.get('changes') is not None:
            for k1 in m.get('changes'):
                temp_model = main_models.ListMemoryTasksResponseBodyItemsChanges()
                self.changes.append(temp_model.from_map(k1))

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('error') is not None:
            temp_model = main_models.ListMemoryTasksResponseBodyItemsError()
            self.error = temp_model.from_map(m.get('error'))

        if m.get('finishedAt') is not None:
            self.finished_at = m.get('finishedAt')

        if m.get('inputMessageCount') is not None:
            self.input_message_count = m.get('inputMessageCount')

        if m.get('inputTokenCount') is not None:
            self.input_token_count = m.get('inputTokenCount')

        self.memories = []
        if m.get('memories') is not None:
            for k1 in m.get('memories'):
                temp_model = main_models.ListMemoryTasksResponseBodyItemsMemories()
                self.memories.append(temp_model.from_map(k1))

        if m.get('startedAt') is not None:
            self.started_at = m.get('startedAt')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('strategyConfig') is not None:
            temp_model = main_models.ListMemoryTasksResponseBodyItemsStrategyConfig()
            self.strategy_config = temp_model.from_map(m.get('strategyConfig'))

        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')

        if m.get('triggerType') is not None:
            self.trigger_type = m.get('triggerType')

        return self

class ListMemoryTasksResponseBodyItemsStrategyConfig(DaraModel):
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

class ListMemoryTasksResponseBodyItemsMemories(DaraModel):
    def __init__(
        self,
        memory_id: str = None,
    ):
        # memoryId
        # 
        # This parameter is required.
        self.memory_id = memory_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        return self

class ListMemoryTasksResponseBodyItemsError(DaraModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # code
        # 
        # This parameter is required.
        self.code = code
        # message
        # 
        # This parameter is required.
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        return self

class ListMemoryTasksResponseBodyItemsChanges(DaraModel):
    def __init__(
        self,
        memory_id: str = None,
        operation: str = None,
    ):
        # memoryId
        # 
        # This parameter is required.
        self.memory_id = memory_id
        # operation
        # 
        # This parameter is required.
        self.operation = operation

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_id is not None:
            result['memoryId'] = self.memory_id

        if self.operation is not None:
            result['operation'] = self.operation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryId') is not None:
            self.memory_id = m.get('memoryId')

        if m.get('operation') is not None:
            self.operation = m.get('operation')

        return self

