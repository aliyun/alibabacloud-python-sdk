# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        hybrid_search: str = None,
        hybrid_search_args: str = None,
        include_metadata_fields: str = None,
        include_vector: bool = None,
        kb_uuid: str = None,
        metrics: str = None,
        offset: int = None,
        order_by: str = None,
        query: str = None,
        recall_window: str = None,
        rerank_factor: float = None,
        top_k: int = None,
    ):
        self.filter = filter
        self.hybrid_search = hybrid_search
        self.hybrid_search_args = hybrid_search_args
        self.include_metadata_fields = include_metadata_fields
        self.include_vector = include_vector
        # This parameter is required.
        self.kb_uuid = kb_uuid
        self.metrics = metrics
        self.offset = offset
        self.order_by = order_by
        # This parameter is required.
        self.query = query
        self.recall_window = recall_window
        self.rerank_factor = rerank_factor
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.hybrid_search is not None:
            result['HybridSearch'] = self.hybrid_search

        if self.hybrid_search_args is not None:
            result['HybridSearchArgs'] = self.hybrid_search_args

        if self.include_metadata_fields is not None:
            result['IncludeMetadataFields'] = self.include_metadata_fields

        if self.include_vector is not None:
            result['IncludeVector'] = self.include_vector

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.query is not None:
            result['Query'] = self.query

        if self.recall_window is not None:
            result['RecallWindow'] = self.recall_window

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args = m.get('HybridSearchArgs')

        if m.get('IncludeMetadataFields') is not None:
            self.include_metadata_fields = m.get('IncludeMetadataFields')

        if m.get('IncludeVector') is not None:
            self.include_vector = m.get('IncludeVector')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RecallWindow') is not None:
            self.recall_window = m.get('RecallWindow')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

