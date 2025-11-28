# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ChatWithKnowledgeBaseShrinkRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        include_knowledge_base_results: bool = None,
        knowledge_params_shrink: str = None,
        model_params_shrink: str = None,
        owner_id: int = None,
        prompt_params: str = None,
        region_id: str = None,
    ):
        # The cluster ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/196830.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # Whether to return the retrieved result. Default value: false.
        self.include_knowledge_base_results = include_knowledge_base_results
        # The knowledge retrieval parameter object. If you do not specify this parameter, only chat mode is enabled.
        self.knowledge_params_shrink = knowledge_params_shrink
        # The Large Language Model (LLM) invocation parameter object.
        # 
        # This parameter is required.
        self.model_params_shrink = model_params_shrink
        self.owner_id = owner_id
        # The system prompt template, which should include {{ text_chunks }},{{ user_system_prompt }},{{ graph_entities },{{ graph_relations }}. If any of these placeholders are not specified, the corresponding section should have no effect.
        self.prompt_params = prompt_params
        # 实例所在的地域ID
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.include_knowledge_base_results is not None:
            result['IncludeKnowledgeBaseResults'] = self.include_knowledge_base_results

        if self.knowledge_params_shrink is not None:
            result['KnowledgeParams'] = self.knowledge_params_shrink

        if self.model_params_shrink is not None:
            result['ModelParams'] = self.model_params_shrink

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.prompt_params is not None:
            result['PromptParams'] = self.prompt_params

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('IncludeKnowledgeBaseResults') is not None:
            self.include_knowledge_base_results = m.get('IncludeKnowledgeBaseResults')

        if m.get('KnowledgeParams') is not None:
            self.knowledge_params_shrink = m.get('KnowledgeParams')

        if m.get('ModelParams') is not None:
            self.model_params_shrink = m.get('ModelParams')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PromptParams') is not None:
            self.prompt_params = m.get('PromptParams')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

