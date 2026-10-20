# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_bailian20231229 import models as main_models
from darabonba.model import DaraModel

class RetrieveRequest(DaraModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        extra: main_models.RetrieveRequestExtra = None,
        images: List[str] = None,
        index_id: str = None,
        query: str = None,
        query_history: List[main_models.RetrieveRequestQueryHistory] = None,
        rerank: List[main_models.RetrieveRequestRerank] = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite: List[main_models.RetrieveRequestRewrite] = None,
        save_retriever_history: bool = None,
        search_filters: List[Dict[str, str]] = None,
        sparse_similarity_top_k: int = None,
    ):
        # The top K value for AISearch. The system generates a vector for the input text and retrieves the top K text chunks in the knowledge base that are most similar to the vector representation. Valid values: 0 to 100.
        # The sum of DenseSimilarityTopK and SparseSimilarityTopK must be less than or equal to 200.
        # 
        # Default value: 100.
        self.dense_similarity_top_k = dense_similarity_top_k
        # Specifies whether to enable reranking. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: true.
        self.enable_reranking = enable_reranking
        # Specifies whether to enable <props="china">[multi-turn conversation rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[multi-turn conversation rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji).
        # Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.enable_rewrite = enable_rewrite
        self.extra = extra
        # The URLs of the images passed in the query.
        self.images = images
        # The ID of the knowledge base, which is the Data.Id returned by the CreateIndex operation.
        # 
        # > - Make sure that the corresponding knowledge base is created and not deleted.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The input text, which is the original input prompt. The length and characters of Query are not limited.
        self.query = query
        # <props="china">[Multi-turn conversation rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[Multi-turn conversation rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji) allows you to pass in your own managed conversation history. This parameter takes effect only when EnableRewrite is set to **true**. Otherwise, it does not take effect even if you specify it.
        self.query_history = query_history
        # The reranking configuration.
        self.rerank = rerank
        # The similarity threshold. This threshold specifies the minimum similarity score allowed for recalled text chunks and is used to filter the text chunks returned by the ranking model. Only text chunks with a score greater than this value are recalled. Valid values: 0.01 to 1.00. This parameter has a higher priority than the similarity threshold configured for the knowledge base.
        # 
        # If no specific value is specified, the similarity threshold configured for the knowledge base is used by default.
        self.rerank_min_score = rerank_min_score
        # The top N text chunks to return after reranking. Valid values: 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # The multi-turn conversation rewriting configuration.
        self.rewrite = rewrite
        # Specifies whether to save the historical text chunk recall test data. Valid values:
        # - true: Save.
        # - false: Do not save.
        # 
        # Default value: false.
        self.save_retriever_history = save_retriever_history
        # The personalized retrieval conditions, such as tags, configured by using SearchFilter to filter semantic retrieval results and exclude information irrelevant to the query.
        # The filtering logic takes effect when the is_displayed_chunk_content parameter is set to true. For more information, see [Knowledge base SearchFilters](https://help.aliyun.com/document_detail/2869641.html).
        self.search_filters = search_filters
        # The top K value for keyword retrieval. The system retrieves chunks from the knowledge base that are an exact match for the keywords in the input text. This helps you filter out irrelevant text chunks and provides more accurate results.
        # Valid values: 0 to 100.
        # The sum of DenseSimilarityTopK and SparseSimilarityTopK must be less than or equal to 200.
        # 
        # Default value: 100.
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        if self.extra:
            self.extra.validate()
        if self.query_history:
            for v1 in self.query_history:
                 if v1:
                    v1.validate()
        if self.rerank:
            for v1 in self.rerank:
                 if v1:
                    v1.validate()
        if self.rewrite:
            for v1 in self.rewrite:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dense_similarity_top_k is not None:
            result['DenseSimilarityTopK'] = self.dense_similarity_top_k

        if self.enable_reranking is not None:
            result['EnableReranking'] = self.enable_reranking

        if self.enable_rewrite is not None:
            result['EnableRewrite'] = self.enable_rewrite

        if self.extra is not None:
            result['Extra'] = self.extra.to_map()

        if self.images is not None:
            result['Images'] = self.images

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.query is not None:
            result['Query'] = self.query

        result['QueryHistory'] = []
        if self.query_history is not None:
            for k1 in self.query_history:
                result['QueryHistory'].append(k1.to_map() if k1 else None)

        result['Rerank'] = []
        if self.rerank is not None:
            for k1 in self.rerank:
                result['Rerank'].append(k1.to_map() if k1 else None)

        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score

        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n

        result['Rewrite'] = []
        if self.rewrite is not None:
            for k1 in self.rewrite:
                result['Rewrite'].append(k1.to_map() if k1 else None)

        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history

        if self.search_filters is not None:
            result['SearchFilters'] = self.search_filters

        if self.sparse_similarity_top_k is not None:
            result['SparseSimilarityTopK'] = self.sparse_similarity_top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenseSimilarityTopK') is not None:
            self.dense_similarity_top_k = m.get('DenseSimilarityTopK')

        if m.get('EnableReranking') is not None:
            self.enable_reranking = m.get('EnableReranking')

        if m.get('EnableRewrite') is not None:
            self.enable_rewrite = m.get('EnableRewrite')

        if m.get('Extra') is not None:
            temp_model = main_models.RetrieveRequestExtra()
            self.extra = temp_model.from_map(m.get('Extra'))

        if m.get('Images') is not None:
            self.images = m.get('Images')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        self.query_history = []
        if m.get('QueryHistory') is not None:
            for k1 in m.get('QueryHistory'):
                temp_model = main_models.RetrieveRequestQueryHistory()
                self.query_history.append(temp_model.from_map(k1))

        self.rerank = []
        if m.get('Rerank') is not None:
            for k1 in m.get('Rerank'):
                temp_model = main_models.RetrieveRequestRerank()
                self.rerank.append(temp_model.from_map(k1))

        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')

        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')

        self.rewrite = []
        if m.get('Rewrite') is not None:
            for k1 in m.get('Rewrite'):
                temp_model = main_models.RetrieveRequestRewrite()
                self.rewrite.append(temp_model.from_map(k1))

        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')

        if m.get('SearchFilters') is not None:
            self.search_filters = m.get('SearchFilters')

        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')

        return self

class RetrieveRequestRewrite(DaraModel):
    def __init__(
        self,
        model_name: str = None,
    ):
        # The name of the multi-turn conversation rewriting model. The model automatically adjusts the original input prompt (user question) based on the conversation context to improve retrieval performance. Valid values:
        # - conv-rewrite-qwen-1.8b: The conv-rewrite-qwen-1.8b model. Currently, only this model is supported.
        # 
        # Default value: null. The conv-rewrite-qwen-1.8b model is used.
        self.model_name = model_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        return self

class RetrieveRequestRerank(DaraModel):
    def __init__(
        self,
        model_name: str = None,
        rerank_instruct: str = None,
        rerank_mode: str = None,
    ):
        # The specified reranking model. The value specified here overrides the reranking model selected when the knowledge base was created. Valid values:
        # 
        # <props="china">
        # 
        # - qwen3-rerank-hybrid: qwen3-rerank (hybrid) reranking.
        # - qwen3-rerank: qwen3-rerank reranking.
        # - gte-rerank-hybrid: gte-rerank (hybrid) reranking.
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - gte-rerank-hybrid: Official reranking.
        # - gte-rerank: gte-rerank reranking.
        # 
        # 
        # 
        # 
        # 
        # 
        # Default value: null. The reranking model selected when the knowledge base was created is used.
        # 
        # 
        # <props="china">
        # 
        # > If you only need semantic reranking, use qwen3-rerank. If you need both semantic reranking and text matching features to ensure relevance, use qwen3-rerank-hybrid.
        # >
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="intl">
        # 
        # > If you only need semantic reranking, use gte-rerank. If you need both semantic reranking and text matching features to ensure relevance, use gte-rerank-hybrid.
        # >
        # 
        # 
        # 
        # 
        # 
        # 
        # <props="china">
        # 
        # > gte-rerank-hybrid and gte-rerank will no longer be updated and are not recommended.
        # >
        self.model_name = model_name
        # <props="intl">This parameter is not available. Do not specify this parameter.
        # 
        # <props="china">A natural language instruction used to fine-tune the behavior of the reranking model.
        # <notice>This parameter takes effect only when rerank_mode is set to custom.</notice>
        self.rerank_instruct = rerank_instruct
        # <props="china">
        # The instruction intervention mode of the reranking model, which determines its scoring preference.
        # 
        # **Valid values:**
        # 
        # - **qa**: (Default) Q&A mode. The model tends to assign higher scores to candidates that can directly answer the query. Recommended for Q&A scenarios.
        # 
        # - **similar**: Similarity mode. The model tends to assign higher scores to candidates that are highly consistent with the query content. Recommended for matching and retrieval scenarios.
        # 
        # - **custom**: Custom mode. The reranking behavior of the model is determined by the instruction in the rerank_instruct parameter.
        # 
        # 
        # 
        # <props="intl">This parameter is not available. Do not specify this parameter.
        self.rerank_mode = rerank_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.rerank_instruct is not None:
            result['RerankInstruct'] = self.rerank_instruct

        if self.rerank_mode is not None:
            result['RerankMode'] = self.rerank_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('RerankInstruct') is not None:
            self.rerank_instruct = m.get('RerankInstruct')

        if m.get('RerankMode') is not None:
            self.rerank_mode = m.get('RerankMode')

        return self

class RetrieveRequestQueryHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # The question or answer content of the corresponding role.
        self.content = content
        # The role.
        # 
        # Valid values:
        # 
        # - user: If this role is passed, content indicates the text that you input to the Alibaba Cloud Model Studio application.
        # - assistant: If this role is passed, content indicates the reply from the Alibaba Cloud Model Studio application.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['content'] = self.content

        if self.role is not None:
            result['role'] = self.role

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('role') is not None:
            self.role = m.get('role')

        return self

class RetrieveRequestExtra(DaraModel):
    def __init__(
        self,
        unique_id: str = None,
    ):
        self.unique_id = unique_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.unique_id is not None:
            result['uniqueId'] = self.unique_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uniqueId') is not None:
            self.unique_id = m.get('uniqueId')

        return self

