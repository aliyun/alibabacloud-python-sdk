# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dianjin20240628 import models as main_models
from darabonba.model import DaraModel

class GetLibraryResponseBody(DaraModel):
    def __init__(
        self,
        cost: int = None,
        data: main_models.GetLibraryResponseBodyData = None,
        data_type: str = None,
        err_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        time: str = None,
    ):
        # Response time in milliseconds.
        self.cost = cost
        # The response data object.
        self.data = data
        # The data type.
        self.data_type = data_type
        # The error code.
        self.err_code = err_code
        # Fault type
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request succeeded.
        self.success = success
        # UNIX timestamp
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
            temp_model = main_models.GetLibraryResponseBodyData()
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

class GetLibraryResponseBodyData(DaraModel):
    def __init__(
        self,
        description: str = None,
        document_count: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: str = None,
        index_setting: main_models.GetLibraryResponseBodyDataIndexSetting = None,
        library_name: str = None,
    ):
        # The document library description.
        self.description = description
        # The number of documents in the library.
        self.document_count = document_count
        # Creation time
        self.gmt_create = gmt_create
        # The last modification time in YYYY-MM-DD HH:MM:SS format.
        self.gmt_modified = gmt_modified
        # The document library ID.
        self.id = id
        # The document library index settings.
        self.index_setting = index_setting
        # The document library name.
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
            temp_model = main_models.GetLibraryResponseBodyDataIndexSetting()
            self.index_setting = temp_model.from_map(m.get('indexSetting'))

        if m.get('libraryName') is not None:
            self.library_name = m.get('libraryName')

        return self

class GetLibraryResponseBodyDataIndexSetting(DaraModel):
    def __init__(
        self,
        chunk_strategy: main_models.GetLibraryResponseBodyDataIndexSettingChunkStrategy = None,
        model_config: main_models.GetLibraryResponseBodyDataIndexSettingModelConfig = None,
        prompt_role_style: str = None,
        query_enhancer: main_models.GetLibraryResponseBodyDataIndexSettingQueryEnhancer = None,
        recall_strategy: main_models.GetLibraryResponseBodyDataIndexSettingRecallStrategy = None,
        text_index_setting: main_models.GetLibraryResponseBodyDataIndexSettingTextIndexSetting = None,
        vector_index_setting: main_models.GetLibraryResponseBodyDataIndexSettingVectorIndexSetting = None,
    ):
        # The chunking strategy.
        self.chunk_strategy = chunk_strategy
        # Model configuration.
        self.model_config = model_config
        # The prompt role style.
        self.prompt_role_style = prompt_role_style
        # Query enhancement settings.
        self.query_enhancer = query_enhancer
        # The recall strategy.
        self.recall_strategy = recall_strategy
        # Text index settings.
        self.text_index_setting = text_index_setting
        # Vector index settings.
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
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingChunkStrategy()
            self.chunk_strategy = temp_model.from_map(m.get('chunkStrategy'))

        if m.get('modelConfig') is not None:
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingModelConfig()
            self.model_config = temp_model.from_map(m.get('modelConfig'))

        if m.get('promptRoleStyle') is not None:
            self.prompt_role_style = m.get('promptRoleStyle')

        if m.get('queryEnhancer') is not None:
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingQueryEnhancer()
            self.query_enhancer = temp_model.from_map(m.get('queryEnhancer'))

        if m.get('recallStrategy') is not None:
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingRecallStrategy()
            self.recall_strategy = temp_model.from_map(m.get('recallStrategy'))

        if m.get('textIndexSetting') is not None:
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingTextIndexSetting()
            self.text_index_setting = temp_model.from_map(m.get('textIndexSetting'))

        if m.get('vectorIndexSetting') is not None:
            temp_model = main_models.GetLibraryResponseBodyDataIndexSettingVectorIndexSetting()
            self.vector_index_setting = temp_model.from_map(m.get('vectorIndexSetting'))

        return self

class GetLibraryResponseBodyDataIndexSettingVectorIndexSetting(DaraModel):
    def __init__(
        self,
        category: str = None,
        embedding_type: str = None,
        enable: bool = None,
        rank_threshold: float = None,
        top_k: int = None,
    ):
        # The vector index source. We recommend ADB.
        self.category = category
        # The text embedding model for the vector index.
        self.embedding_type = embedding_type
        # Enable vector indexing.
        self.enable = enable
        # The ranking threshold for vector indexing.
        self.rank_threshold = rank_threshold
        # Number of final results returned by the vector index.
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

class GetLibraryResponseBodyDataIndexSettingTextIndexSetting(DaraModel):
    def __init__(
        self,
        category: str = None,
        enable: bool = None,
        index_analyzer: str = None,
        rank_threshold: float = None,
        search_analyzer: str = None,
        top_k: int = None,
    ):
        # The text index type.
        self.category = category
        # Enable text indexing.
        self.enable = enable
        # The text index analyzer: Standard, IkMaxWord, or IkSmart.
        self.index_analyzer = index_analyzer
        # The ranking threshold for text indexing.
        self.rank_threshold = rank_threshold
        # The text index search analyzer: Standard, IkMaxWord, or IkSmart.
        self.search_analyzer = search_analyzer
        # The number of final summary results from text indexing.
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

class GetLibraryResponseBodyDataIndexSettingRecallStrategy(DaraModel):
    def __init__(
        self,
        document_rank_type: str = None,
        limit: int = None,
    ):
        # The merge and sort policy.
        self.document_rank_type = document_rank_type
        # The number of results returned after merging two recall paths.
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

class GetLibraryResponseBodyDataIndexSettingQueryEnhancer(DaraModel):
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
        # Enable multi-turn query enhancement.
        self.enable_follow_up = enable_follow_up
        # Use Large Language Model (LLM) knowledge to decompose queries.
        self.enable_multi_query = enable_multi_query
        # Use Large Language Model (LLM) knowledge to answer questions.
        self.enable_open_qa = enable_open_qa
        # Rewrite queries using domain-specific knowledge.
        self.enable_query_rewrite = enable_query_rewrite
        # Record session history.
        self.enable_session = enable_session
        # The document library ID used for knowledge rewriting.
        self.local_knowledge_id = local_knowledge_id
        # Include document references in responses.
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

class GetLibraryResponseBodyDataIndexSettingModelConfig(DaraModel):
    def __init__(
        self,
        temperature: float = None,
        top_p: float = None,
    ):
        # temperature
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

class GetLibraryResponseBodyDataIndexSettingChunkStrategy(DaraModel):
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
        # Enable layout-based splitting.
        self.doc_tree_split = doc_tree_split
        # The layout-based splitting size.
        self.doc_tree_split_size = doc_tree_split_size
        # Enhance images.
        self.enhance_graph = enhance_graph
        # Enhance tables.
        self.enhance_table = enhance_table
        # The overlap length between chunks.
        self.overlap = overlap
        # Split by sentence.
        self.sentence_split = sentence_split
        # The sentence-based splitting size.
        self.sentence_split_size = sentence_split_size
        # The chunk size.
        self.size = size
        # Enable chunking.
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

