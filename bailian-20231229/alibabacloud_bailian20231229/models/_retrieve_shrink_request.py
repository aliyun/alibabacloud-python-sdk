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
        self.extra_shrink = extra_shrink
        # The URLs of the images passed in the query.
        self.images_shrink = images_shrink
        # The ID of the knowledge base, which is the Data.Id returned by the CreateIndex operation.
        # 
        # > - Make sure that the corresponding knowledge base is created and not deleted.
        # 
        # This parameter is required.
        self.index_id = index_id
        # The input text, which is the original input prompt. The length and characters of Query are not limited.
        self.query = query
        # <props="china">[Multi-turn conversation rewriting](https://help.aliyun.com/model-studio/use-cases/rag-optimization#b7031e2ad6cji)<props="intl">[Multi-turn conversation rewriting](https://www.alibabacloud.com/help/model-studio/use-cases/rag-optimization#b7031e2ad6cji) allows you to pass in your own managed conversation history. This parameter takes effect only when EnableRewrite is set to **true**. Otherwise, it does not take effect even if you specify it.
        self.query_history_shrink = query_history_shrink
        # The reranking configuration.
        self.rerank_shrink = rerank_shrink
        # The similarity threshold. This threshold specifies the minimum similarity score allowed for recalled text chunks and is used to filter the text chunks returned by the ranking model. Only text chunks with a score greater than this value are recalled. Valid values: 0.01 to 1.00. This parameter has a higher priority than the similarity threshold configured for the knowledge base.
        # 
        # If no specific value is specified, the similarity threshold configured for the knowledge base is used by default.
        self.rerank_min_score = rerank_min_score
        # The top N text chunks to return after reranking. Valid values: 1 to 20. Default value: 5.
        self.rerank_top_n = rerank_top_n
        # The multi-turn conversation rewriting configuration.
        self.rewrite_shrink = rewrite_shrink
        # Specifies whether to save the historical text chunk recall test data. Valid values:
        # - true: Save.
        # - false: Do not save.
        # 
        # Default value: false.
        self.save_retriever_history = save_retriever_history
        # The personalized retrieval conditions, such as tags, configured by using SearchFilter to filter semantic retrieval results and exclude information irrelevant to the query.
        # The filtering logic takes effect when the is_displayed_chunk_content parameter is set to true. For more information, see [Knowledge base SearchFilters](https://help.aliyun.com/document_detail/2869641.html).
        self.search_filters_shrink = search_filters_shrink
        # The top K value for keyword retrieval. The system retrieves chunks from the knowledge base that are an exact match for the keywords in the input text. This helps you filter out irrelevant text chunks and provides more accurate results.
        # Valid values: 0 to 100.
        # The sum of DenseSimilarityTopK and SparseSimilarityTopK must be less than or equal to 200.
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

