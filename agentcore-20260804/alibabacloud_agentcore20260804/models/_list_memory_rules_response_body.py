# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class ListMemoryRulesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.ListMemoryRulesResponseBodyItems] = None,
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
                temp_model = main_models.ListMemoryRulesResponseBodyItems()
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

class ListMemoryRulesResponseBodyItems(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        enabled: bool = None,
        memory_store_id: str = None,
        name: str = None,
        rule_id: str = None,
        strategy: main_models.ListMemoryRulesResponseBodyItemsStrategy = None,
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

        if self.memory_store_id is not None:
            result['memoryStoreId'] = self.memory_store_id

        if self.name is not None:
            result['name'] = self.name

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

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

        if m.get('memoryStoreId') is not None:
            self.memory_store_id = m.get('memoryStoreId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('strategy') is not None:
            temp_model = main_models.ListMemoryRulesResponseBodyItemsStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        if m.get('updatedAt') is not None:
            self.updated_at = m.get('updatedAt')

        return self

class ListMemoryRulesResponseBodyItemsStrategy(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        type: str = None,
    ):
        # The strategy-level instruction. It takes effect together with the store-level instruction. This field takes precedence in case of conflicts.
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

