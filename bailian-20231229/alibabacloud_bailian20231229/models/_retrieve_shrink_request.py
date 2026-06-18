# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveShrinkRequest(DaraModel):
    def __init__(
        self,
        dense_similarity_top_k: int = None,
        enable_reranking: bool = None,
        enable_rewrite: bool = None,
        extra_shrink: str = None,
        images_shrink: str = None,
        index_id: str = None,
        query: str = None,
        query_history_shrink: str = None,
        rerank_shrink: str = None,
        rerank_min_score: float = None,
        rerank_top_n: int = None,
        rewrite_shrink: str = None,
        save_retriever_history: bool = None,
        search_filters_shrink: str = None,
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
        self.extra_shrink = extra_shrink
        # The URLs of images to include in the query.
        self.images_shrink = images_shrink
        # The ID of the knowledge base. This is the `Data.Id` value returned by the `CreateIndex` operation.
        # 
        # > - Ensure the specified knowledge base exists and has not been deleted.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The query, which is the original user prompt. There are no limits on the length of the query.
        self.query = query
        # The conversation history, used for <props="china">[conversational query rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[conversational query rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji). This parameter is effective only when `EnableRewrite` is set to `true`.
        self.query_history_shrink = query_history_shrink
        # The reranking configurations.
        self.rerank_shrink = rerank_shrink
        # The similarity threshold for reranking. Only text chunks with a similarity score greater than this value are returned. The value must be between 0.01 and 1.00, inclusive. This parameter overrides the similarity threshold setting of the knowledge base.
        # 
        # If not specified, the threshold configured for the knowledge base is used.
        self.rerank_min_score = rerank_min_score
        # The number of top-ranked text chunks to return after reranking. The value must be an integer from 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # Configuration for conversational query rewriting.
        self.rewrite_shrink = rewrite_shrink
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
        self.search_filters_shrink = search_filters_shrink
        # The number of top-K text chunks to retrieve using keyword retrieval. This feature finds text chunks in the knowledge base that exactly match the keywords in the query. It helps filter out irrelevant text chunks and provide more accurate results.
        # The value must be an integer from 0 to 100.
        # The sum of `DenseSimilarityTopK` and `SparseSimilarityTopK` must not exceed 200.
        # 
        # Default value: 100.
        self.sparse_similarity_top_k = sparse_similarity_top_k

    def validate(self):
        pass

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

        if self.extra_shrink is not None:
            result['Extra'] = self.extra_shrink

        if self.images_shrink is not None:
            result['Images'] = self.images_shrink

        if self.index_id is not None:
            result['IndexId'] = self.index_id

        if self.query is not None:
            result['Query'] = self.query

        if self.query_history_shrink is not None:
            result['QueryHistory'] = self.query_history_shrink

        if self.rerank_shrink is not None:
            result['Rerank'] = self.rerank_shrink

        if self.rerank_min_score is not None:
            result['RerankMinScore'] = self.rerank_min_score

        if self.rerank_top_n is not None:
            result['RerankTopN'] = self.rerank_top_n

        if self.rewrite_shrink is not None:
            result['Rewrite'] = self.rewrite_shrink

        if self.save_retriever_history is not None:
            result['SaveRetrieverHistory'] = self.save_retriever_history

        if self.search_filters_shrink is not None:
            result['SearchFilters'] = self.search_filters_shrink

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
            self.extra_shrink = m.get('Extra')

        if m.get('Images') is not None:
            self.images_shrink = m.get('Images')

        if m.get('IndexId') is not None:
            self.index_id = m.get('IndexId')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('QueryHistory') is not None:
            self.query_history_shrink = m.get('QueryHistory')

        if m.get('Rerank') is not None:
            self.rerank_shrink = m.get('Rerank')

        if m.get('RerankMinScore') is not None:
            self.rerank_min_score = m.get('RerankMinScore')

        if m.get('RerankTopN') is not None:
            self.rerank_top_n = m.get('RerankTopN')

        if m.get('Rewrite') is not None:
            self.rewrite_shrink = m.get('Rewrite')

        if m.get('SaveRetrieverHistory') is not None:
            self.save_retriever_history = m.get('SaveRetrieverHistory')

        if m.get('SearchFilters') is not None:
            self.search_filters_shrink = m.get('SearchFilters')

        if m.get('SparseSimilarityTopK') is not None:
            self.sparse_similarity_top_k = m.get('SparseSimilarityTopK')

        return self

