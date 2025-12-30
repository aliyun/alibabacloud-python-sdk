# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetLibraryListResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetLibraryListResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        self.cost = cost
        self.data = data
        self.data_type = data_type
        self.err_code = err_code
        self.message = message
        self.request_id = request_id
        self.success = success
        self.time = time

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cost is not None:
            result['cost'] = self.cost

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.data_type is not None:
            result['dataType'] = self.data_type

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        if self.time is not None:
            result['time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cost') is not None:
            self.cost = m.get('cost')

        if m.get('data') is not None:
            temp_model = main_models.GetLibraryListResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('dataType') is not None:
            self.data_type = m.get('dataType')

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        if m.get('time') is not None:
            self.time = m.get('time')

        return self

class GetLibraryListResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        records: List[main_models.GetLibraryListResponseBodyDataRecords] = None,
        total_pages: int = None,
        total_records: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.records = records
        self.total_pages = total_pages
        self.total_records = total_records

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.total_pages is not None:
            result['totalPages'] = self.total_pages

        if self.total_records is not None:
            result['totalRecords'] = self.total_records

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.GetLibraryListResponseBodyDataRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('totalPages') is not None:
            self.total_pages = m.get('totalPages')

        if m.get('totalRecords') is not None:
            self.total_records = m.get('totalRecords')

        return self

class GetLibraryListResponseBodyDataRecords(DaraModel):
    def __init__(
        self,
        description: str = None,
        document_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        index_setting: main_models.GetLibraryListResponseBodyDataRecordsIndexSetting = None,
        library_name: str = None,
    ):
        self.description = description
        self.document_count = document_count
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.id = id
        self.index_setting = index_setting
        self.library_name = library_name

    def validate(self):
        if self.index_setting:
            self.index_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.document_count is not None:
            result['documentCount'] = self.document_count

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['gmtModified'] = self.gmt_modified

        if self.id is not None:
            result['id'] = self.id

        if self.index_setting is not None:
            result['indexSetting'] = self.index_setting.to_map()

        if self.library_name is not None:
            result['libraryName'] = self.library_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('documentCount') is not None:
            self.document_count = m.get('documentCount')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('gmtModified') is not None:
            self.gmt_modified = m.get('gmtModified')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('indexSetting') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSetting()
            self.index_setting = temp_model.from_map(m.get('indexSetting'))

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSetting(DaraModel):
    def __init__(
        self,
        chunk_strategy: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy = None,
        model_config: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer = None,
        recall_strategy: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy = None,
        text_index_setting: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting = None,
        vector_index_setting: main_models.GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting = None,
    ):
        self.chunk_strategy = chunk_strategy
        self.model_config = model_config
        self.prompt_role_style = prompt_role_style
        self.query_enhancer = query_enhancer
        self.recall_strategy = recall_strategy
        self.text_index_setting = text_index_setting
        self.vector_index_setting = vector_index_setting

    def validate(self):
        if self.chunk_strategy:
            self.chunk_strategy.validate()
        if self.model_config:
            self.model_config.validate()
        if self.query_enhancer:
            self.query_enhancer.validate()
        if self.recall_strategy:
            self.recall_strategy.validate()
        if self.text_index_setting:
            self.text_index_setting.validate()
        if self.vector_index_setting:
            self.vector_index_setting.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_strategy is not None:
            result['chunkStrategy'] = self.chunk_strategy.to_map()

        if self.model_config is not None:
            result['modelConfig'] = self.model_config.to_map()

        if self.prompt_role_style is not None:
            result['promptRoleStyle'] = self.prompt_role_style

        if self.query_enhancer is not None:
            result['queryEnhancer'] = self.query_enhancer.to_map()

        if self.recall_strategy is not None:
            result['recallStrategy'] = self.recall_strategy.to_map()

        if self.text_index_setting is not None:
            result['textIndexSetting'] = self.text_index_setting.to_map()

        if self.vector_index_setting is not None:
            result['vectorIndexSetting'] = self.vector_index_setting.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chunkStrategy') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m.get('chunkStrategy'))

        if m.get('modelConfig') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m.get('modelConfig'))

        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')

        if m.get('queryEnhancer') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m.get('queryEnhancer'))

        if m.get('recallStrategy') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m.get('recallStrategy'))

        if m.get('textIndexSetting') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m.get('textIndexSetting'))

        if m.get('vectorIndexSetting') is not None:
            temp_model = main_models.GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m.get('vectorIndexSetting'))

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingVectorIndexSetting(DaraModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        self.category = category
        self.embedding_type = embedding_type
        self.enable = enable
        self.rank_threshold = rank_threshold
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.embedding_type is not None:
            result['embeddingType'] = self.embedding_type

        if self.enable is not None:
            result['enable'] = self.enable

        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('embeddingType') is not None:
            self.embedding_type = m.get('embeddingType')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingTextIndexSetting(DaraModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        self.category = category
        self.enable = enable
        self.index_analyzer = index_analyzer
        self.rank_threshold = rank_threshold
        self.search_analyzer = search_analyzer
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.enable is not None:
            result['enable'] = self.enable

        if self.index_analyzer is not None:
            result['indexAnalyzer'] = self.index_analyzer

        if self.rank_threshold is not None:
            result['rankThreshold'] = self.rank_threshold

        if self.search_analyzer is not None:
            result['searchAnalyzer'] = self.search_analyzer

        if self.top_k is not None:
            result['topK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('indexAnalyzer') is not None:
            self.index_analyzer = m.get('indexAnalyzer')

        if m.get('rankThreshold') is not None:
            self.rank_threshold = m.get('rankThreshold')

        if m.get('searchAnalyzer') is not None:
            self.search_analyzer = m.get('searchAnalyzer')

        if m.get('topK') is not None:
            self.top_k = m.get('topK')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingRecallStrategy(DaraModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        self.document_rank_type = document_rank_type
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.document_rank_type is not None:
            result['documentRankType'] = self.document_rank_type

        if self.limit is not None:
            result['limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('documentRankType') is not None:
            self.document_rank_type = m.get('documentRankType')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingQueryEnhancer(DaraModel):
    def __init__(
        self,
        enable_follow_up: bool = None,
        enable_multi_query: bool = None,
        enable_open_qa: bool = None,
        enable_query_rewrite: bool = None,
        enable_session: bool = None,
        local_knowledge_id: str = None,
        with_document_reference: bool = None,
    ):
        self.enable_follow_up = enable_follow_up
        self.enable_multi_query = enable_multi_query
        self.enable_open_qa = enable_open_qa
        self.enable_query_rewrite = enable_query_rewrite
        self.enable_session = enable_session
        self.local_knowledge_id = local_knowledge_id
        self.with_document_reference = with_document_reference

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_follow_up is not None:
            result['enableFollowUp'] = self.enable_follow_up

        if self.enable_multi_query is not None:
            result['enableMultiQuery'] = self.enable_multi_query

        if self.enable_open_qa is not None:
            result['enableOpenQa'] = self.enable_open_qa

        if self.enable_query_rewrite is not None:
            result['enableQueryRewrite'] = self.enable_query_rewrite

        if self.enable_session is not None:
            result['enableSession'] = self.enable_session

        if self.local_knowledge_id is not None:
            result['localKnowledgeId'] = self.local_knowledge_id

        if self.with_document_reference is not None:
            result['withDocumentReference'] = self.with_document_reference

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableFollowUp') is not None:
            self.enable_follow_up = m.get('enableFollowUp')

        if m.get('enableMultiQuery') is not None:
            self.enable_multi_query = m.get('enableMultiQuery')

        if m.get('enableOpenQa') is not None:
            self.enable_open_qa = m.get('enableOpenQa')

        if m.get('enableQueryRewrite') is not None:
            self.enable_query_rewrite = m.get('enableQueryRewrite')

        if m.get('enableSession') is not None:
            self.enable_session = m.get('enableSession')

        if m.get('localKnowledgeId') is not None:
            self.local_knowledge_id = m.get('localKnowledgeId')

        if m.get('withDocumentReference') is not None:
            self.with_document_reference = m.get('withDocumentReference')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingModelConfig(DaraModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        self.temperature = temperature
        # topP
        self.top_p = top_p

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.temperature is not None:
            result['temperature'] = self.temperature

        if self.top_p is not None:
            result['topP'] = self.top_p

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('temperature') is not None:
            self.temperature = m.get('temperature')

        if m.get('topP') is not None:
            self.top_p = m.get('topP')

        return self

class GetLibraryListResponseBodyDataRecordsIndexSettingChunkStrategy(DaraModel):
    def __init__(
        self,
        doc_tree_split: bool = None,
        doc_tree_split_size: int = None,
        enhance_graph: bool = None,
        enhance_table: bool = None,
        overlap: int = None,
        sentence_split: bool = None,
        sentence_split_size: int = None,
        size: int = None,
        split: bool = None,
    ):
        self.doc_tree_split = doc_tree_split
        self.doc_tree_split_size = doc_tree_split_size
        self.enhance_graph = enhance_graph
        self.enhance_table = enhance_table
        self.overlap = overlap
        self.sentence_split = sentence_split
        self.sentence_split_size = sentence_split_size
        self.size = size
        self.split = split

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_tree_split is not None:
            result['docTreeSplit'] = self.doc_tree_split

        if self.doc_tree_split_size is not None:
            result['docTreeSplitSize'] = self.doc_tree_split_size

        if self.enhance_graph is not None:
            result['enhanceGraph'] = self.enhance_graph

        if self.enhance_table is not None:
            result['enhanceTable'] = self.enhance_table

        if self.overlap is not None:
            result['overlap'] = self.overlap

        if self.sentence_split is not None:
            result['sentenceSplit'] = self.sentence_split

        if self.sentence_split_size is not None:
            result['sentenceSplitSize'] = self.sentence_split_size

        if self.size is not None:
            result['size'] = self.size

        if self.split is not None:
            result['split'] = self.split

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('docTreeSplit') is not None:
            self.doc_tree_split = m.get('docTreeSplit')

        if m.get('docTreeSplitSize') is not None:
            self.doc_tree_split_size = m.get('docTreeSplitSize')

        if m.get('enhanceGraph') is not None:
            self.enhance_graph = m.get('enhanceGraph')

        if m.get('enhanceTable') is not None:
            self.enhance_table = m.get('enhanceTable')

        if m.get('overlap') is not None:
            self.overlap = m.get('overlap')

        if m.get('sentenceSplit') is not None:
            self.sentence_split = m.get('sentenceSplit')

        if m.get('sentenceSplitSize') is not None:
            self.sentence_split_size = m.get('sentenceSplitSize')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('split') is not None:
            self.split = m.get('split')

        return self

