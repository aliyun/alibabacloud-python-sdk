# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrievalKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_id: str = None,
        query_text: str = None,
        region_id: str = None,
        rerank_enabled: bool = None,
        score_threshold: float = None,
        top_k: int = None,
    ):
        # The unique ID of the knowledge base.
        # 
        # This parameter is required.
        self.knowledge_base_id = knowledge_base_id
        # The query text.
        # 
        # This parameter is required.
        self.query_text = query_text
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Specifies whether to enable reranking. Default value: true.
        self.rerank_enabled = rerank_enabled
        # The similarity score threshold.
        self.score_threshold = score_threshold
        # The number of results to return.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_enabled is not None:
            result['RerankEnabled'] = self.rerank_enabled

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankEnabled') is not None:
            self.rerank_enabled = m.get('RerankEnabled')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

