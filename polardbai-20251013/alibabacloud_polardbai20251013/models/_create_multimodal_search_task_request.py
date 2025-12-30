# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateMultimodalSearchTaskRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        dataset_ids: List[str] = None,
        embedding_model: str = None,
        query: str = None,
        search_model: str = None,
        top_k: int = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.dataset_ids = dataset_ids
        self.embedding_model = embedding_model
        self.query = query
        self.search_model = search_model
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.dataset_ids is not None:
            result['DatasetIds'] = self.dataset_ids

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.query is not None:
            result['Query'] = self.query

        if self.search_model is not None:
            result['SearchModel'] = self.search_model

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatasetIds') is not None:
            self.dataset_ids = m.get('DatasetIds')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('SearchModel') is not None:
            self.search_model = m.get('SearchModel')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

