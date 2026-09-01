# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AnswerKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        max_context_chars: int = None,
        query_text: str = None,
        region_id: str = None,
        rerank_enabled: bool = None,
        return_sources: bool = None,
        score_threshold: float = None,
        search_mode: str = None,
        system_prompt: str = None,
        top_k: int = None,
        user_instructions: str = None,
    ):
        # The unique ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The maximum number of context characters. Valid values: 1000 to 32000.
        self.max_context_chars = max_context_chars
        # The user query text.
        # 
        # This parameter is required.
        self.query_text = query_text
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable reranking. Default value: false.
        self.rerank_enabled = rerank_enabled
        # Specifies whether to return citation sources. Default value: true.
        self.return_sources = return_sources
        # The similarity score threshold.
        self.score_threshold = score_threshold
        # The search mode. Valid values: knn, rrf, precise, semantic, and balanced.
        self.search_mode = search_mode
        # The system prompt.
        self.system_prompt = system_prompt
        # The number of results to recall during retrieval.
        self.top_k = top_k
        # The supplementary user instructions.
        self.user_instructions = user_instructions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.max_context_chars is not None:
            result['MaxContextChars'] = self.max_context_chars

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_enabled is not None:
            result['RerankEnabled'] = self.rerank_enabled

        if self.return_sources is not None:
            result['ReturnSources'] = self.return_sources

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.search_mode is not None:
            result['SearchMode'] = self.search_mode

        if self.system_prompt is not None:
            result['SystemPrompt'] = self.system_prompt

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.user_instructions is not None:
            result['UserInstructions'] = self.user_instructions

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('MaxContextChars') is not None:
            self.max_context_chars = m.get('MaxContextChars')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankEnabled') is not None:
            self.rerank_enabled = m.get('RerankEnabled')

        if m.get('ReturnSources') is not None:
            self.return_sources = m.get('ReturnSources')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('SearchMode') is not None:
            self.search_mode = m.get('SearchMode')

        if m.get('SystemPrompt') is not None:
            self.system_prompt = m.get('SystemPrompt')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UserInstructions') is not None:
            self.user_instructions = m.get('UserInstructions')

        return self

