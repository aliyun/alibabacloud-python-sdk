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
        # The number of top-K similar text chunks to retrieve using vector retrieval. This is achieved by generating a vector representation of the query and searching the knowledge base for the K text chunks with the most similar vectors. The value must be an integer from 0 to 100. The sum of `DenseSimilarityTopK` and `SparseSimilarityTopK` must not exceed 200.
        # 
        # Default value: 100.
        self.dense_similarity_top_k = dense_similarity_top_k
        # Specifies whether to enable reranking. For more information, see [Knowledge base](https://help.aliyun.com/document_detail/2807740.html). Valid values:
        # 
        # - `true`: Enables reranking.
        # 
        # - `false`: Disables reranking.
        # 
        # Default value: `true`.
        self.enable_reranking = enable_reranking
        # Specifies whether to enable <props="china">[conversational query rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[conversational query rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji).
        # Valid values:
        # 
        # - `true`: Enables conversational query rewriting.
        # 
        # - `false`: Disables conversational query rewriting.
        # 
        # Default value: `false`.
        self.enable_rewrite = enable_rewrite
        self.extra = extra
        # The URLs of images to include in the query.
        self.images = images
        # The ID of the knowledge base. This is the `Data.Id` value returned by the `CreateIndex` operation.
        # 
        # > - Ensure the specified knowledge base exists and has not been deleted.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The query, which is the original user prompt. There are no limits on the length of the query.
        self.query = query
        # The conversation history, used for <props="china">[conversational query rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[conversational query rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji). This parameter is effective only when `EnableRewrite` is set to `true`.
        self.query_history = query_history
        # The reranking configurations.
        self.rerank = rerank
        # The similarity threshold for reranking. Only text chunks with a similarity score greater than this value are returned. The value must be between 0.01 and 1.00, inclusive. This parameter overrides the similarity threshold setting of the knowledge base.
        # 
        # If not specified, the threshold configured for the knowledge base is used.
        self.rerank_min_score = rerank_min_score
        # The number of top-ranked text chunks to return after reranking. The value must be an integer from 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # Configuration for conversational query rewriting.
        self.rewrite = rewrite
        # Specifies whether to save the retrieval history for testing purposes. Valid values:
        # 
        # - `true`: Saves the retrieval history.
        # 
        # - `false`: Does not save the retrieval history.
        # 
        # Default value: `false`.
        self.save_retriever_history = save_retriever_history
        # Specifies custom retrieval conditions, such as tags, to filter semantic retrieval results and exclude irrelevant information.
        # The filtering logic is applied only when the `is_displayed_chunk_content` parameter is set to `true`. For more information, see [SearchFilters for a knowledge base](https://help.aliyun.com/document_detail/2869641.html).
        self.search_filters = search_filters
        # The number of top-K text chunks to retrieve using keyword retrieval. This feature finds text chunks in the knowledge base that exactly match the keywords in the query. It helps filter out irrelevant text chunks and provide more accurate results.
        # The value must be an integer from 0 to 100.
        # The sum of `DenseSimilarityTopK` and `SparseSimilarityTopK` must not exceed 200.
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
        # Specifies the model for conversational query rewriting, which automatically rewrites the original query based on the conversation context to improve retrieval results. Valid value:
        # 
        # - `conv-rewrite-qwen-1.8b`: The only model currently supported for this feature.
        # 
        # If this parameter is not specified, `conv-rewrite-qwen-1.8b` is used by default.
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
        # The reranking model to use. Specifying a model here overrides the default model selected when the knowledge base was created. Valid values:
        # 
        # <props="china">
        # 
        # - `qwen3-rerank-hybrid`: Performs reranking by using the qwen3-rerank (hybrid) model.
        # 
        # - `qwen3-rerank`: Performs reranking by using the qwen3-rerank model.
        # 
        # - `gte-rerank-hybrid`: Performs reranking by using the gte-rerank (hybrid) model.
        # 
        # - `gte-rerank`: Performs reranking by using the gte-rerank model.
        # 
        # 
        # 
        # <props="intl">
        # 
        # - `gte-rerank-hybrid`: Performs reranking by using the gte-rerank (hybrid) model.
        # 
        # - `gte-rerank`: Performs reranking by using the gte-rerank model.
        # 
        # 
        # 
        # If you do not specify this parameter, the model configured for the knowledge base is used.
        # 
        # <props="china">
        # 
        # > Use `qwen3-rerank` for semantic ranking only. We recommend `qwen3-rerank-hybrid` if you require both semantic ranking and text matching features for higher relevance.
        # 
        # 
        # 
        # <props="intl">
        # 
        # > Use `gte-rerank` for semantic ranking only. We recommend `gte-rerank-hybrid` if you require both semantic ranking and text matching features for higher relevance.
        # 
        # 
        # 
        # <props="china">
        # 
        # > The `gte-rerank-hybrid` and `gte-rerank` models are no longer updated and are not recommended for use.
        self.model_name = model_name
        # <props="intl">
        # 
        # This parameter is not yet available. Do not specify a value for it.
        # 
        # 
        # 
        # <props="china">
        # 
        # A natural language instruction to fine-tune the behavior of the reranking model.
        # 
        # >Notice: 
        # 
        # This parameter takes effect only when `RerankMode` is set to `custom`.
        self.rerank_instruct = rerank_instruct
        # <props="china">
        # 
        # Specifies the instruction intervention mode for the reranking model. This mode determines the model\\"s scoring preference.
        # 
        # **Valid values:**
        # 
        # - `qa`: (Default) Q\\&A mode. The model assigns higher scores to candidates that directly answer the query. Recommended for Q\\&A scenarios.
        # 
        # - `similar`: Similarity mode. The model assigns higher scores to candidates with high content similarity to the query. Recommended for match-based retrieval scenarios.
        # 
        # - `custom`: Custom mode. The model\\"s ranking behavior is determined by the instructions in the `RerankInstruct` parameter.
        # 
        # 
        # 
        # <props="intl">
        # 
        # This parameter is not yet available. Do not specify a value for it.
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
        # The content of the message for the specified `role`.
        self.content = content
        # The role of the entity that sent the message.
        # 
        # Valid values:
        # 
        # - `user`: Indicates that the `content` is from the end user.
        # 
        # - `assistant`: Indicates that the `content` is a response from the Model Studio application.
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

