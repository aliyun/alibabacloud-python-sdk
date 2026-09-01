# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class RetrievalKnowledgeBaseResponseBody(DaraModel):
    def __init__(
        self,
        query_text: str = None,
        request_id: str = None,
        result_count: int = None,
        results: List[main_models.RetrievalKnowledgeBaseResponseBodyResults] = None,
    ):
        self.query_text = query_text
        self.request_id = request_id
        self.result_count = result_count
        self.results = results

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.query_text is not None:
            result['QueryText'] = self.query_text

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count is not None:
            result['ResultCount'] = self.result_count

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('QueryText') is not None:
            self.query_text = m.get('QueryText')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCount') is not None:
            self.result_count = m.get('ResultCount')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.RetrievalKnowledgeBaseResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        return self

class RetrievalKnowledgeBaseResponseBodyResults(DaraModel):
    def __init__(
        self,
        file_id: str = None,
        file_name: str = None,
        headings: List[str] = None,
        metadata: str = None,
        page_numbers: List[int] = None,
        shard_content: str = None,
        shard_index: int = None,
        similarity_score: float = None,
    ):
        self.file_id = file_id
        self.file_name = file_name
        self.headings = headings
        self.metadata = metadata
        self.page_numbers = page_numbers
        self.shard_content = shard_content
        self.shard_index = shard_index
        self.similarity_score = similarity_score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.headings is not None:
            result['Headings'] = self.headings

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.page_numbers is not None:
            result['PageNumbers'] = self.page_numbers

        if self.shard_content is not None:
            result['ShardContent'] = self.shard_content

        if self.shard_index is not None:
            result['ShardIndex'] = self.shard_index

        if self.similarity_score is not None:
            result['SimilarityScore'] = self.similarity_score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Headings') is not None:
            self.headings = m.get('Headings')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('PageNumbers') is not None:
            self.page_numbers = m.get('PageNumbers')

        if m.get('ShardContent') is not None:
            self.shard_content = m.get('ShardContent')

        if m.get('ShardIndex') is not None:
            self.shard_index = m.get('ShardIndex')

        if m.get('SimilarityScore') is not None:
            self.similarity_score = m.get('SimilarityScore')

        return self

