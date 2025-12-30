# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class RunLibraryChatGenerationRequest(DaraModel):
    def __init__(
        self,
        doc_id_list: List[str] = None,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        follow_up_llm: str = None,
        library_id: str = None,
        llm_type: str = None,
        multi_query_llm: str = None,
        query: str = None,
        query_criteria: main_models.RunLibraryChatGenerationRequestQueryCriteria = None,
        rerank_type: str = None,
        session_id: str = None,
        stream: bool = None,
        sub_query_list: List[str] = None,
        text_search_parameter: main_models.RunLibraryChatGenerationRequestTextSearchParameter = None,
        top_k: int = None,
        vector_search_parameter: main_models.RunLibraryChatGenerationRequestVectorSearchParameter = None,
        with_document_reference: bool = None,
    ):
        self.doc_id_list = doc_id_list
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.follow_up_llm = follow_up_llm
        # This parameter is required.
        self.library_id = library_id
        # This parameter is required.
        self.llm_type = llm_type
        self.multi_query_llm = multi_query_llm
        # This parameter is required.
        self.query = query
        self.query_criteria = query_criteria
        self.rerank_type = rerank_type
        # sessionId
        self.session_id = session_id
        self.stream = stream
        self.sub_query_list = sub_query_list
        self.text_search_parameter = text_search_parameter
        self.top_k = top_k
        self.vector_search_parameter = vector_search_parameter
        self.with_document_reference = with_document_reference

    def validate(self):
        if self.query_criteria:
            self.query_criteria.validate()
        if self.text_search_parameter:
            self.text_search_parameter.validate()
        if self.vector_search_parameter:
            self.vector_search_parameter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id_list is not None:
            result['docIdList'] = self.doc_id_list

        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up

        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query

        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa

        if self.follow_up_llm is not None:
            result['followUpLlm'] = self.follow_up_llm

        if self.library_id is not None:
            result['libraryId'] = self.library_id

        if self.llm_type is not None:
            result['llmType'] = self.llm_type

        if self.multi_query_llm is not None:
            result['multiQueryLlm'] = self.multi_query_llm

        if self.query is not None:
            result['query'] = self.query

        if self.query_criteria is not None:
            result['queryCriteria'] = self.query_criteria.to_map()

        if self.rerank_type is not None:
            result['rerankType'] = self.rerank_type

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.stream is not None:
            result['stream'] = self.stream

        if self.sub_query_list is not None:
            result['subQueryList'] = self.sub_query_list

        if self.text_search_parameter is not None:
            result['textSearchParameter'] = self.text_search_parameter.to_map()

        if self.top_k is not None:
            result['topK'] = self.top_k

        if self.vector_search_parameter is not None:
            result['vectorSearchParameter'] = self.vector_search_parameter.to_map()

        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docIdList') is not None:
            self.doc_id_list = m.get('docIdList')

        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')

        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')

        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')

        if m.get('followUpLlm') is not None:
            self.follow_up_llm = m.get('followUpLlm')

        if m.get('libraryId') is not None:
            self.library_id = m.get('libraryId')

        if m.get('llmType') is not None:
            self.llm_type = m.get('llmType')

        if m.get('multiQueryLlm') is not None:
            self.multi_query_llm = m.get('multiQueryLlm')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryCriteria') is not None:
            temp_model = main_models.RunLibraryChatGenerationRequestQueryCriteria()
            self.query_criteria = temp_model.from_map(m.get('queryCriteria'))

        if m.get('rerankType') is not None:
            self.rerank_type = m.get('rerankType')

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('subQueryList') is not None:
            self.sub_query_list = m.get('subQueryList')

        if m.get('textSearchParameter') is not None:
            temp_model = main_models.RunLibraryChatGenerationRequestTextSearchParameter()
            self.text_search_parameter = temp_model.from_map(m.get('textSearchParameter'))

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        if m.get('vectorSearchParameter') is not None:
            temp_model = main_models.RunLibraryChatGenerationRequestVectorSearchParameter()
            self.vector_search_parameter = temp_model.from_map(m.get('vectorSearchParameter'))

        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')

        return self

class RunLibraryChatGenerationRequestVectorSearchParameter(DaraModel):
    def __init__(
        self,
        limit: int = None,
    ):
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        return self

class RunLibraryChatGenerationRequestTextSearchParameter(DaraModel):
    def __init__(
        self,
        limit: int = None,
        search_analyzer_type: str = None,
    ):
        self.limit = limit
        self.search_analyzer_type = search_analyzer_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.search_analyzer_type is not None:
            result['searchAnalyzerType'] = self.search_analyzer_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('searchAnalyzerType') is not None:
            self.search_analyzer_type = m.get('searchAnalyzerType')

        return self

class RunLibraryChatGenerationRequestQueryCriteria(DaraModel):
    def __init__(
        self,
        and_: List[main_models.RunLibraryChatGenerationRequestQueryCriteriaAnd] = None,
        or_: List[main_models.RunLibraryChatGenerationRequestQueryCriteriaOr] = None,
    ):
        self.and_ = and_
        self.or_ = or_

    def validate(self):
        if self.and_:
            for v1 in self.and_:
                 if v1:
                    v1.validate()
        if self.or_:
            for v1 in self.or_:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['and'] = []
        if self.and_ is not None:
            for k1 in self.and_:
                result['and'].append(k1.to_map() if k1 else None)

        result['or'] = []
        if self.or_ is not None:
            for k1 in self.or_:
                result['or'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.and_ = []
        if m.get('and') is not None:
            for k1 in m.get('and'):
                temp_model = main_models.RunLibraryChatGenerationRequestQueryCriteriaAnd()
                self.and_.append(temp_model.from_map(k1))

        self.or_ = []
        if m.get('or') is not None:
            for k1 in m.get('or'):
                temp_model = main_models.RunLibraryChatGenerationRequestQueryCriteriaOr()
                self.or_.append(temp_model.from_map(k1))

        return self

class RunLibraryChatGenerationRequestQueryCriteriaOr(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boost is not None:
            result['boost'] = self.boost

        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class RunLibraryChatGenerationRequestQueryCriteriaAnd(DaraModel):
    def __init__(
        self,
        boost: float = None,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        self.boost = boost
        self.key = key
        self.operator = operator
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.boost is not None:
            result['boost'] = self.boost

        if self.key is not None:
            result['key'] = self.key

        if self.operator is not None:
            result['operator'] = self.operator

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('boost') is not None:
            self.boost = m.get('boost')

        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('operator') is not None:
            self.operator = m.get('operator')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

