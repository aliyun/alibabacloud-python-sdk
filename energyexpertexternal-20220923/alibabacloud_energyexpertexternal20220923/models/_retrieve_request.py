# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RetrieveRequest(DaraModel):
    def __init__(
        self,
        document_ids: List[int] = None,
        folder_ids: List[str] = None,
        pre_retrieve_top_k: int = None,
        query: str = None,
        reranker_threshold: float = None,
        top_k: int = None,
        use_reranker: bool = None,
    ):
        self.document_ids = document_ids
        self.folder_ids = folder_ids
        self.pre_retrieve_top_k = pre_retrieve_top_k
        # This parameter is required.
        self.query = query
        self.reranker_threshold = reranker_threshold
        self.top_k = top_k
        self.use_reranker = use_reranker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_ids is not None:
            result['documentIds'] = self.document_ids

        if self.folder_ids is not None:
            result['folderIds'] = self.folder_ids

        if self.pre_retrieve_top_k is not None:
            result['preRetrieveTopK'] = self.pre_retrieve_top_k

        if self.query is not None:
            result['query'] = self.query

        if self.reranker_threshold is not None:
            result['rerankerThreshold'] = self.reranker_threshold

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.use_reranker is not None:
            result['useReranker'] = self.use_reranker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentIds') is not None:
            self.document_ids = m.get('documentIds')

        if m.get('folderIds') is not None:
            self.folder_ids = m.get('folderIds')

        if m.get('preRetrieveTopK') is not None:
            self.pre_retrieve_top_k = m.get('preRetrieveTopK')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rerankerThreshold') is not None:
            self.reranker_threshold = m.get('rerankerThreshold')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('useReranker') is not None:
            self.use_reranker = m.get('useReranker')

        return self

