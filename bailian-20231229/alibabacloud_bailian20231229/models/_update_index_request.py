# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateIndexRequest(DaraModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        description: str = None,
        id: str = None,
        name: str = None,
        pipeline_commercial_cu: int = None,
        pipeline_commercial_type: str = None,
        rerank_min_score: str = None,
        sparse_similarity_top_k: int = None,
    ):
        self.dense_similarity_top_k = dense_similarity_top_k
        self.description = description
        # This parameter is required.
        self.id = id
        self.name = name
        self.pipeline_commercial_cu = pipeline_commercial_cu
        self.pipeline_commercial_type = pipeline_commercial_type
        self.rerank_min_score = rerank_min_score
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k

        if self.description is not None:
            result['Description'] = self.description

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.pipeline_commercial_cu is not None:
            result['PipelineCommercialCu'] = self.pipeline_commercial_cu

        if self.pipeline_commercial_type is not None:
            result['PipelineCommercialType'] = self.pipeline_commercial_type

        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score

        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PipelineCommercialCu') is not None:
            self.pipeline_commercial_cu = m.get('PipelineCommercialCu')

        if m.get('PipelineCommercialType') is not None:
            self.pipeline_commercial_type = m.get('PipelineCommercialType')

        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')

        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')

        return self

