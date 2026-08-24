# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_milvusknowledgebase20260604 import models as main_models
from darabonba.model import DaraModel

class SearchKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        document_ids: List[str] = None,
        enable_knowledge_graph: bool = None,
        image: main_models.SearchKnowledgeBaseRequestImage = None,
        page_number: int = None,
        page_size: int = None,
        query: str = None,
        rerank_model_id: int = None,
        rerank_model_name: str = None,
        retrieval_config: main_models.SearchKnowledgeBaseRequestRetrievalConfig = None,
        tag_filter: main_models.SearchKnowledgeBaseRequestTagFilter = None,
        version: str = None,
    ):
        # The list of document IDs.
        self.document_ids = document_ids
        # Specifies whether to enable the knowledge graph.
        self.enable_knowledge_graph = enable_knowledge_graph
        # The image retrieval input.
        self.image = image
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The query for retrieval.
        self.query = query
        # The rerank model ID.
        self.rerank_model_id = rerank_model_id
        # The name of the rerank model that the tenant has activated. If both rerankModelName and rerankModelId are specified, this parameter takes precedence.
        self.rerank_model_name = rerank_model_name
        # The retrieval configuration.
        self.retrieval_config = retrieval_config
        # The tag filter.
        self.tag_filter = tag_filter
        # The knowledge base version.
        self.version = version

    def validate(self):
        if self.image:
            self.image.validate()
        if self.retrieval_config:
            self.retrieval_config.validate()
        if self.tag_filter:
            self.tag_filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_ids is not None:
            result['documentIds'] = self.document_ids

        if self.enable_knowledge_graph is not None:
            result['enableKnowledgeGraph'] = self.enable_knowledge_graph

        if self.image is not None:
            result['image'] = self.image.to_map()

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.query is not None:
            result['query'] = self.query

        if self.rerank_model_id is not None:
            result['rerankModelId'] = self.rerank_model_id

        if self.rerank_model_name is not None:
            result['rerankModelName'] = self.rerank_model_name

        if self.retrieval_config is not None:
            result['retrievalConfig'] = self.retrieval_config.to_map()

        if self.tag_filter is not None:
            result['tagFilter'] = self.tag_filter.to_map()

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentIds') is not None:
            self.document_ids = m.get('documentIds')

        if m.get('enableKnowledgeGraph') is not None:
            self.enable_knowledge_graph = m.get('enableKnowledgeGraph')

        if m.get('image') is not None:
            temp_model = main_models.SearchKnowledgeBaseRequestImage()
            self.image = temp_model.from_map(m.get('image'))

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('rerankModelId') is not None:
            self.rerank_model_id = m.get('rerankModelId')

        if m.get('rerankModelName') is not None:
            self.rerank_model_name = m.get('rerankModelName')

        if m.get('retrievalConfig') is not None:
            temp_model = main_models.SearchKnowledgeBaseRequestRetrievalConfig()
            self.retrieval_config = temp_model.from_map(m.get('retrievalConfig'))

        if m.get('tagFilter') is not None:
            temp_model = main_models.SearchKnowledgeBaseRequestTagFilter()
            self.tag_filter = temp_model.from_map(m.get('tagFilter'))

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class SearchKnowledgeBaseRequestTagFilter(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.SearchKnowledgeBaseRequestTagFilterConditions] = None,
        relation: str = None,
    ):
        # The list of tag conditions.
        self.conditions = conditions
        # The logical relation between conditions.
        self.relation = relation

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

        if self.relation is not None:
            result['relation'] = self.relation

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.SearchKnowledgeBaseRequestTagFilterConditions()
                self.conditions.append(temp_model.from_map(k1))

        if m.get('relation') is not None:
            self.relation = m.get('relation')

        return self

class SearchKnowledgeBaseRequestTagFilterConditions(DaraModel):
    def __init__(
        self,
        field: str = None,
        op: str = None,
        value: Any = None,
    ):
        # The tag field.
        self.field = field
        # The operator.
        self.op = op
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field is not None:
            result['field'] = self.field

        if self.op is not None:
            result['op'] = self.op

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')

        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class SearchKnowledgeBaseRequestRetrievalConfig(DaraModel):
    def __init__(
        self,
        candidate_count: int = None,
        enable_query_expansion: bool = None,
        min_score: float = None,
        semantic_weight: float = None,
        translation_languages: List[str] = None,
    ):
        # The number of candidate results to recall.
        self.candidate_count = candidate_count
        # Specifies whether to enable query expansion.
        self.enable_query_expansion = enable_query_expansion
        # The minimum relevance score.
        self.min_score = min_score
        # The weight of semantic relevance.
        self.semantic_weight = semantic_weight
        # The list of translation languages.
        self.translation_languages = translation_languages

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.candidate_count is not None:
            result['candidateCount'] = self.candidate_count

        if self.enable_query_expansion is not None:
            result['enableQueryExpansion'] = self.enable_query_expansion

        if self.min_score is not None:
            result['minScore'] = self.min_score

        if self.semantic_weight is not None:
            result['semanticWeight'] = self.semantic_weight

        if self.translation_languages is not None:
            result['translationLanguages'] = self.translation_languages

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('candidateCount') is not None:
            self.candidate_count = m.get('candidateCount')

        if m.get('enableQueryExpansion') is not None:
            self.enable_query_expansion = m.get('enableQueryExpansion')

        if m.get('minScore') is not None:
            self.min_score = m.get('minScore')

        if m.get('semanticWeight') is not None:
            self.semantic_weight = m.get('semanticWeight')

        if m.get('translationLanguages') is not None:
            self.translation_languages = m.get('translationLanguages')

        return self

class SearchKnowledgeBaseRequestImage(DaraModel):
    def __init__(
        self,
        base_64: str = None,
        object_key: str = None,
        url: str = None,
    ):
        # The Base64-encoded image.
        self.base_64 = base_64
        # The object key of the image.
        self.object_key = object_key
        # The image URL.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.base_64 is not None:
            result['base64'] = self.base_64

        if self.object_key is not None:
            result['objectKey'] = self.object_key

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('base64') is not None:
            self.base_64 = m.get('base64')

        if m.get('objectKey') is not None:
            self.object_key = m.get('objectKey')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self

