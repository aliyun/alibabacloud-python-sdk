# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_agentcore20260804 import models as main_models
from darabonba.model import DaraModel

class UpdateMemoryRuleRequest(DaraModel):
    def __init__(
        self,
        body: main_models.UpdateMemoryRuleRequestBody = None,
    ):
        # The JSON request body.
        # 
        # This parameter is required.
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            temp_model = main_models.UpdateMemoryRuleRequestBody()
            self.body = temp_model.from_map(m.get('body'))

        return self

class UpdateMemoryRuleRequestBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        enabled: bool = None,
        name: str = None,
        strategy: main_models.UpdateMemoryRuleRequestBodyStrategy = None,
    ):
        # description
        self.description = description
        # enabled
        self.enabled = enabled
        # name
        self.name = name
        # The extraction strategy. Uses partial merging, where omitted fields retain their original values.
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.name is not None:
            result['name'] = self.name

        if self.strategy is not None:
            result['strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('strategy') is not None:
            temp_model = main_models.UpdateMemoryRuleRequestBodyStrategy()
            self.strategy = temp_model.from_map(m.get('strategy'))

        return self

class UpdateMemoryRuleRequestBodyStrategy(DaraModel):
    def __init__(
        self,
        instruction: str = None,
        type: str = None,
    ):
        # The custom extraction instruction. If omitted, the original value is retained. An empty string clears the value.
        self.instruction = instruction
        # type
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

