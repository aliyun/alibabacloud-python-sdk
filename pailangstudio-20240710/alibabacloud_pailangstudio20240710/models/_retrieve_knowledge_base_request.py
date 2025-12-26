# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        hybrid_strategy_config: str = None,
        meta_data_filter_conditions: str = None,
        query: str = None,
        query_mode: str = None,
        rerank_config: str = None,
        rewrite_config: str = None,
        score_threshold: float = None,
        top_k: int = None,
        version_name: str = None,
        workspace_id: str = None,
    ):
        self.hybrid_strategy_config = hybrid_strategy_config
        self.meta_data_filter_conditions = meta_data_filter_conditions
        # This parameter is required.
        self.query = query
        self.query_mode = query_mode
        self.rerank_config = rerank_config
        self.rewrite_config = rewrite_config
        self.score_threshold = score_threshold
        self.top_k = top_k
        self.version_name = version_name
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hybrid_strategy_config is not None:
            result['HybridStrategyConfig'] = self.hybrid_strategy_config

        if self.meta_data_filter_conditions is not None:
            result['MetaDataFilterConditions'] = self.meta_data_filter_conditions

        if self.query is not None:
            result['Query'] = self.query

        if self.query_mode is not None:
            result['QueryMode'] = self.query_mode

        if self.rerank_config is not None:
            result['RerankConfig'] = self.rerank_config

        if self.rewrite_config is not None:
            result['RewriteConfig'] = self.rewrite_config

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HybridStrategyConfig') is not None:
            self.hybrid_strategy_config = m.get('HybridStrategyConfig')

        if m.get('MetaDataFilterConditions') is not None:
            self.meta_data_filter_conditions = m.get('MetaDataFilterConditions')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryMode') is not None:
            self.query_mode = m.get('QueryMode')

        if m.get('RerankConfig') is not None:
            self.rerank_config = m.get('RerankConfig')

        if m.get('RewriteConfig') is not None:
            self.rewrite_config = m.get('RewriteConfig')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

