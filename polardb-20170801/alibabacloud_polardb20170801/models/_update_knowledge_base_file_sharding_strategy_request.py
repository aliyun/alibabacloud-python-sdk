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
        # The unique ID of the knowledge base file.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to restore inheritance of the chunking strategy from the knowledge space. When this parameter is set to true, ShardingStrategyConfig cannot be specified at the same time.
        self.inherit_space_strategy = inherit_space_strategy
        # The unique ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The ID of the region where the knowledge base resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The file-level chunking strategy configuration. This parameter is required when InheritSpaceStrategy is not set to true.
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
        # The default chunking strategy. This strategy is used when no rule is matched.
        # 
        # This parameter is required.
        self.default_strategy = default_strategy
        # The list of override rules that are matched in order. Currently, a maximum of one exact-match rule with ContentType set to table is supported.
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
        # The rule match condition. Currently, only exact matching by content type for table content is supported.
        # 
        # This parameter is required.
        self.match = match
        # The chunking strategy to use when the rule is matched.
        # 
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
        # The chunking strategy parameters of the override rule. MaxTokens takes effect only when Type is set to hybrid. MarkdownTables supports auto, on, or off.
        self.parameters = parameters
        # The chunking strategy type of the override rule. Valid values:
        # - hybrid
        # - hierarchical
        # 
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
        # The Markdown table processing mode. Valid values:
        # - auto: Automatically determines the processing mode.
        # - on: Forcefully enables Markdown table processing.
        # - off: Disables Markdown table processing.
        self.markdown_tables = markdown_tables
        # The maximum number of tokens per chunk for matched content. The value must be a positive integer. This parameter takes effect only when Type is set to hybrid.
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
        # The content type. Currently, only table is supported, which matches content that is parsed as tables.
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
        # The parameters of the default chunking strategy. MaxTokens and MergePeers are supported only when Type is set to hybrid.
        self.parameters = parameters
        # The type of the default chunking strategy. Valid values:
        # - hybrid: Splits by document structure and limits the token count.
        # - hierarchical: Splits only by document structure.
        # 
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
        # The maximum number of tokens per chunk. The value must be a positive integer. This parameter takes effect only when Type is set to hybrid.
        self.max_tokens = max_tokens
        # Specifies whether to merge adjacent small chunks under the same heading. This parameter takes effect only when Type is set to hybrid.
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

