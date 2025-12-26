# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_paicopilot20250731 import models as main_models
from darabonba.model import DaraModel

class SearchInfoRequest(DaraModel):
    def __init__(
        self,
        knowledge_base_filters: List[main_models.SearchInfoRequestKnowledgeBaseFilters] = None,
        web_filters: List[main_models.SearchInfoRequestWebFilters] = None,
    ):
        self.knowledge_base_filters = knowledge_base_filters
        self.web_filters = web_filters

    def validate(self):
        if self.knowledge_base_filters:
            for v1 in self.knowledge_base_filters:
                 if v1:
                    v1.validate()
        if self.web_filters:
            for v1 in self.web_filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['KnowledgeBaseFilters'] = []
        if self.knowledge_base_filters is not None:
            for k1 in self.knowledge_base_filters:
                result['KnowledgeBaseFilters'].append(k1.to_map() if k1 else None)

        result['WebFilters'] = []
        if self.web_filters is not None:
            for k1 in self.web_filters:
                result['WebFilters'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.knowledge_base_filters = []
        if m.get('KnowledgeBaseFilters') is not None:
            for k1 in m.get('KnowledgeBaseFilters'):
                temp_model = main_models.SearchInfoRequestKnowledgeBaseFilters()
                self.knowledge_base_filters.append(temp_model.from_map(k1))

        self.web_filters = []
        if m.get('WebFilters') is not None:
            for k1 in m.get('WebFilters'):
                temp_model = main_models.SearchInfoRequestWebFilters()
                self.web_filters.append(temp_model.from_map(k1))

        return self

class SearchInfoRequestWebFilters(DaraModel):
    def __init__(
        self,
        category: str = None,
        include_sites: List[str] = None,
        query: str = None,
        result_limit: int = None,
        score_threshold: float = None,
    ):
        self.category = category
        self.include_sites = include_sites
        # This parameter is required.
        self.query = query
        self.result_limit = result_limit
        self.score_threshold = score_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.include_sites is not None:
            result['IncludeSites'] = self.include_sites

        if self.query is not None:
            result['Query'] = self.query

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('IncludeSites') is not None:
            self.include_sites = m.get('IncludeSites')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        return self

class SearchInfoRequestKnowledgeBaseFilters(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        query: str = None,
        result_limit: int = None,
        score_threshold: float = None,
    ):
        # This parameter is required.
        self.collection_name = collection_name
        # This parameter is required.
        self.query = query
        self.result_limit = result_limit
        self.score_threshold = score_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name

        if self.query is not None:
            result['Query'] = self.query

        if self.result_limit is not None:
            result['ResultLimit'] = self.result_limit

        if self.score_threshold is not None:
            result['ScoreThreshold'] = self.score_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('ResultLimit') is not None:
            self.result_limit = m.get('ResultLimit')

        if m.get('ScoreThreshold') is not None:
            self.score_threshold = m.get('ScoreThreshold')

        return self

