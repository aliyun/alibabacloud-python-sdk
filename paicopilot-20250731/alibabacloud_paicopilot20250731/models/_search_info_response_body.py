# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class SearchInfoResponseBody(DaraModel):
    def __init__(
        self,
        knowledge_base_search_results: List[main_models.SearchInfoResponseBodyKnowledgeBaseSearchResults] = None,
        request_id: str = None,
        web_search_results: List[main_models.SearchInfoResponseBodyWebSearchResults] = None,
    ):
        self.knowledge_base_search_results = knowledge_base_search_results
        self.request_id = request_id
        self.web_search_results = web_search_results

    def validate(self):
        if self.knowledge_base_search_results:
            for v1 in self.knowledge_base_search_results:
                 if v1:
                    v1.validate()
        if self.web_search_results:
            for v1 in self.web_search_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseSearchResults'] = []
        if self.knowledge_base_search_results is not None:
            for k1 in self.knowledge_base_search_results:
                result['KnowledgeBaseSearchResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WebSearchResults'] = []
        if self.web_search_results is not None:
            for k1 in self.web_search_results:
                result['WebSearchResults'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_search_results = []
        if m.get('KnowledgeBaseSearchResults') is not None:
            for k1 in m.get('KnowledgeBaseSearchResults'):
                temp_model = main_models.SearchInfoResponseBodyKnowledgeBaseSearchResults()
                self.knowledge_base_search_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.web_search_results = []
        if m.get('WebSearchResults') is not None:
            for k1 in m.get('WebSearchResults'):
                temp_model = main_models.SearchInfoResponseBodyWebSearchResults()
                self.web_search_results.append(temp_model.from_map(k1))

        return self

class SearchInfoResponseBodyWebSearchResults(DaraModel):
    def __init__(
        self,
        index: str = None,
        result_content: str = None,
        score: float = None,
        source_link: str = None,
    ):
        self.index = index
        self.result_content = result_content
        self.score = score
        self.source_link = source_link

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.result_content is not None:
            result['ResultContent'] = self.result_content

        if self.score is not None:
            result['Score'] = self.score

        if self.source_link is not None:
            result['SourceLink'] = self.source_link

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SourceLink') is not None:
            self.source_link = m.get('SourceLink')

        return self

class SearchInfoResponseBodyKnowledgeBaseSearchResults(DaraModel):
    def __init__(
        self,
        index: str = None,
        result_content: str = None,
        score: float = None,
    ):
        self.index = index
        self.result_content = result_content
        self.score = score

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index is not None:
            result['Index'] = self.index

        if self.result_content is not None:
            result['ResultContent'] = self.result_content

        if self.score is not None:
            result['Score'] = self.score

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ResultContent') is not None:
            self.result_content = m.get('ResultContent')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        return self

