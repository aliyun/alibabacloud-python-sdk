# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeSpaceShrinkRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        knowledge_space_id: str = None,
        llmmodel: str = None,
        name: str = None,
        region_id: str = None,
        rerank_model: str = None,
        sharding_strategy_config_shrink: str = None,
    ):
        # The description of the knowledge space. The description can be up to 512 characters in length.
        self.description = description
        # The unique identifier of the knowledge space.
        # 
        # This parameter is required.
        self.knowledge_space_id = knowledge_space_id
        # The name of the large language model.
        self.llmmodel = llmmodel
        # The name of the knowledge space. The name must be 1 to 128 characters in length.
        self.name = name
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The name of the reranking model.
        self.rerank_model = rerank_model
        # The default chunking strategy configuration for the knowledge space. Both simple strategies and composite strategies that match by content type are supported.
        self.sharding_strategy_config_shrink = sharding_strategy_config_shrink

    def validate(self):
        pass

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

        if self.sharding_strategy_config_shrink is not None:
            result['ShardingStrategyConfig'] = self.sharding_strategy_config_shrink

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
            self.sharding_strategy_config_shrink = m.get('ShardingStrategyConfig')

        return self

