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
        # Vector retrieval top K. After generating vectors based on input text, the top K chunks in the knowledge base that are most similar to the vector representation of the input text are retrieved. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.dense_similarity_top_k = dense_similarity_top_k
        # Specifies whether to enable reranking. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.enable_reranking = enable_reranking
        # Specifies whether to enable multi-round conversation rewriting. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.enable_rewrite = enable_rewrite
        self.images = images
        # The primary key ID of the knowledge base, which is the `Data.Id` parameter returned by the [CreateIndex](https://www.alibabacloud.com/help/en/model-studio/developer-reference/api-bailian-2023-12-29-createindex) operation.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The input query prompt. The length and characters of the query are not limited.
        self.query = query
        self.query_history = query_history
        # Ranking configurations.
        self.rerank = rerank
        # Similarity Threshold The lowest similarity score of chunks that can be returned. This parameter is used to filter text chunks returned by the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values: [0.01-1.00]. The priority of this parameter is greater than the similarity threshold configured for the knowledge base.
        # 
        # By default, this parameter is left empty. In this case, the similarity threshold of the knowledge base is used.
        self.rerank_min_score = rerank_min_score
        # The top N return data after reranking. Valid values: 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # Conversation rewriting configurations.
        self.rewrite = rewrite
        # Specifies whether to save the retrieve test history. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.save_retriever_history = save_retriever_history
        # Specifies complex filter conditions. For more information about the syntax of SearchFilters, see the SearchFilter syntax section of this topic.
        self.search_filters = search_filters
        # The top K of keyword retrieval. Chunks that exactly match the keywords of the input text are retrieved from the knowledge base. This filters out irrelevant chunks and boosts accuracy. Valid values: 0 to 100. The sum of the `DenseSimilarityTopK` and `SparseSimilarityTopK` parameters must be less than or equal to 200.
        # 
        # Default value: 100.
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
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
        # Conversation rewriting model name. The query rewriting model automatically adjusts the original prompt based on the context to improve retrieval performance. Valid value:
        # 
        # *   conv-rewrite-qwen-1.8b
        # 
        # By default, this parameter is left empty, which means conv-rewrite-qwen-1.8b is used.
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
    ):
        # The name of the rank model. For more information, see [Create a knowledge base](https://www.alibabacloud.com/help/en/model-studio/user-guide/rag-knowledge-base). Valid values:
        # 
        # *   gte-rerank-hybrid: Recommended official model.
        # *   gte-rerank
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

class RetrieveRequestQueryHistory(DaraModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        self.content = content
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

