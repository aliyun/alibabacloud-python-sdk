# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class UpdateKnowledgeBaseFileShardingStrategyRequest(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        inherit_space_strategy: bool = None,
        knowledge_base_id: str = None,
        region_id: str = None,
        sharding_strategy_config: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfig = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.inherit_space_strategy = inherit_space_strategy
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # This parameter is required.
        self.region_id = region_id
        self.sharding_strategy_config = sharding_strategy_config

    def validate(self):
        if self.sharding_strategy_config:
            self.sharding_strategy_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.inherit_space_strategy is not None:
            result['InheritSpaceStrategy'] = self.inherit_space_strategy

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sharding_strategy_config is not None:
            result['ShardingStrategyConfig'] = self.sharding_strategy_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('InheritSpaceStrategy') is not None:
            self.inherit_space_strategy = m.get('InheritSpaceStrategy')

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ShardingStrategyConfig') is not None:
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfig()
            self.sharding_strategy_config = temp_model.from_map(m.get('ShardingStrategyConfig'))

        return self

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfig(DaraModel):
    def __init__(
        self,
        default_strategy: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategy = None,
        rules: List[main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRules] = None,
    ):
        # This parameter is required.
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
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategy()
            self.default_strategy = temp_model.from_map(m.get('DefaultStrategy'))

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRules()
                self.rules.append(temp_model.from_map(k1))

        return self

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRules(DaraModel):
    def __init__(
        self,
        match: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesMatch = None,
        strategy: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategy = None,
    ):
        # This parameter is required.
        self.match = match
        # This parameter is required.
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
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesMatch()
            self.match = temp_model.from_map(m.get('Match'))

        if m.get('Strategy') is not None:
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategy()
            self.strategy = temp_model.from_map(m.get('Strategy'))

        return self

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        # This parameter is required.
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
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesStrategyParameters(DaraModel):
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

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigRulesMatch(DaraModel):
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

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategy(DaraModel):
    def __init__(
        self,
        parameters: main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategyParameters = None,
        type: str = None,
    ):
        self.parameters = parameters
        # This parameter is required.
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
            temp_model = main_models.UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategyParameters()
            self.parameters = temp_model.from_map(m.get('Parameters'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpdateKnowledgeBaseFileShardingStrategyRequestShardingStrategyConfigDefaultStrategyParameters(DaraModel):
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

