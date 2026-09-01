# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdateKnowledgeSpaceRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        knowledge_space_id: str = None,
        llmmodel: str = None,
        name: str = None,
        region_id: str = None,
        rerank_model: str = None,
        sharding_strategy_config: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfig = None,
    ):
        self.description = description
        # This parameter is required.
        self.knowledge_space_id = knowledge_space_id
        self.llmmodel = llmmodel
        self.name = name
        # This parameter is required.
        self.region_id = region_id
        self.rerank_model = rerank_model
        self.sharding_strategy_config = sharding_strategy_config

    def validate(self):
        if self.sharding_strategy_config:
            self.sharding_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.knowledge_space_id is not None:
            result['KnowledgeSpaceId'] = self.knowledge_space_id

        if self.llmmodel is not None:
            result['LLMModel'] = self.llmmodel

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model

        if self.sharding_strategy_config is not None:
            result['ShardingStrategyConfig'] = self.sharding_strategy_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KnowledgeSpaceId') is not None:
            self.knowledge_space_id = m.get('KnowledgeSpaceId')

        if m.get('LLMModel') is not None:
            self.llmmodel = m.get('LLMModel')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankModel') is not None:
            self.rerank_model = m.get('RerankModel')

        if m.get('ShardingStrategyConfig') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfig()
            self.sharding_strategy_config = temp_model.from_map(m.get('ShardingStrategyConfig'))

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfig(DaraModel):
    def __init__(
        self,
        default_strategy: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategy = None,
        rules: List[main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRules] = None,
    ):
        self.default_strategy = default_strategy
        self.rules = rules

    def validate(self):
        if self.default_strategy:
            self.default_strategy.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_strategy is not None:
            result['DefaultStrategy'] = self.default_strategy.to_map()

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultStrategy') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategy()
            self.default_strategy = temp_model.from_map(m.get('DefaultStrategy'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigRules(DaraModel):
    def __init__(
        self,
        match: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesMatch = None,
        strategy: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategy = None,
    ):
        self.match = match
        self.strategy = strategy

    def validate(self):
        if self.match:
            self.match.validate()
        if self.strategy:
            self.strategy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.match is not None:
            result['Match'] = self.match.to_map()

        if self.strategy is not None:
            result['Strategy'] = self.strategy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Match') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesMatch()
            self.match = temp_model.from_map(m.get('Match'))

        if m.get('Strategy') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesStrategyParameters(DaraModel):
    def __init__(
        self,
        markdown_tables: str = None,
        max_tokens: int = None,
    ):
        self.markdown_tables = markdown_tables
        self.max_tokens = max_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.markdown_tables is not None:
            result['MarkdownTables'] = self.markdown_tables

        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkdownTables') is not None:
            self.markdown_tables = m.get('MarkdownTables')

        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigRulesMatch(DaraModel):
    def __init__(
        self,
        content_type: str = None,
    ):
        self.content_type = content_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        self.type = type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            temp_model = main_models.UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateKnowledgeSpaceRequestShardingStrategyConfigDefaultStrategyParameters(DaraModel):
    def __init__(
        self,
        max_tokens: int = None,
        merge_peers: bool = None,
    ):
        self.max_tokens = max_tokens
        self.merge_peers = merge_peers

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_tokens is not None:
            result['MaxTokens'] = self.max_tokens

        if self.merge_peers is not None:
            result['MergePeers'] = self.merge_peers

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxTokens') is not None:
            self.max_tokens = m.get('MaxTokens')

        if m.get('MergePeers') is not None:
            self.merge_peers = m.get('MergePeers')

        return self

