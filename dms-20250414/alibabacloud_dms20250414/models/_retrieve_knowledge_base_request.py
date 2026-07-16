# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RetrieveKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        filter: str = None,
        hybrid_search: str = None,
        hybrid_search_args: str = None,
        include_metadata_fields: str = None,
        include_vector: bool = None,
        kb_uuid: str = None,
        metrics: str = None,
        offset: int = None,
        order_by: str = None,
        query: str = None,
        recall_window: str = None,
        rerank_factor: float = None,
        top_k: int = None,
    ):
        # A filter for the data, specified as a SQL `WHERE` clause.
        self.filter = filter
        # The hybrid search algorithm. If this parameter is not set, the system directly compares and ranks the scores from the dense vector and full-text searches.
        # 
        # Valid values:
        # 
        # - `RRF`: Reciprocal Rank Fusion. This method uses a parameter `k` to control the fusion effect. For more information, see the `HybridSearchArgs` configuration.
        # 
        # - `Weight`: Weighted ranking. This method applies weights to the vector and full-text search scores before ranking. For more information, see the `HybridSearchArgs` configuration.
        # 
        # - `Cascaded`: Performs a full-text search first, followed by a vector search on the results of the full-text search.
        self.hybrid_search = hybrid_search
        # Parameters for the specified `HybridSearch` algorithm. Both `RRF` and `Weight` are supported. You can use the `HybridPathsSetting` object to specify the retrieval paths: dense vector (`dense`), sparse vector (`sparse`), and full-text search (`fulltext`). If this object is not provided, the default retrieval paths are `dense` and `fulltext`.
        # 
        # - `RRF`: Specifies the constant `k` in the scoring formula `1/(k+rank_i)`. The value of `k` must be an integer greater than 1. The format is as follows:
        # 
        # ```
        # {
        #   "HybridPathsSetting": {
        #     "paths": "dense,fulltext"
        #   },
        #   "RRF": {
        #     "k": 60
        #   }
        # }
        # ```
        # 
        # - `Weight`:
        # 
        #   - Two-path recall (do not specify `HybridPathsSetting`; specify only `alpha`):
        # 
        #     - The score is calculated using the formula: `alpha * dense_score + (1-alpha) * fulltext_score`. The `alpha` parameter balances the scores from the dense vector and full-text searches. Its value must be in the range [0, 1], where 0 relies solely on full-text search, and 1 relies solely on dense vector search.
        # 
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        # 
        # - Three-path recall:
        # 
        #   - The score is calculated using the formula: `normalized_dense * dense_score + normalized_sparse * sparse_score + normalized_fulltext * fulltext_score`. The `dense`, `sparse`, and `fulltext` parameters are the weights for the dense vector, sparse vector, and full-text searches, respectively. Their values must be 0 or greater. The system automatically normalizes the weights to sum to 1 (for example, `normalized_x = x / (dense + sparse + fulltext)`).
        # 
        # ```
        # {
        #   "HybridPathsSetting": {
        #      "paths": "dense,sparse,fulltext"
        #    },
        #   "Weight": {
        #     "dense": 0.5,
        #     "sparse": 0.3,
        #     "fulltext": 0.2
        #   }
        # }
        # ```
        self.hybrid_search_args = hybrid_search_args
        # The metadata fields to return, separated by commas. By default, no metadata fields are returned.
        self.include_metadata_fields = include_metadata_fields
        # Specifies whether to include the vector in the results. The default value is `false`.
        # 
        # > - **false**: The vector is not returned.
        # >
        # > - **true**: The vector is returned.
        self.include_vector = include_vector
        # The ID of the knowledge base.
        # 
        # This parameter is required.
        self.kb_uuid = kb_uuid
        # The distance metric for retrieval. If unspecified, this defaults to the metric configured for the knowledge base. Only set this parameter if you have specific requirements.
        # 
        # Valid values:
        # 
        # - `l2`: Euclidean distance.
        # 
        # - `ip`: Inner product.
        # 
        # - `cosine`: Cosine similarity.
        self.metrics = metrics
        # The offset for pagination.
        self.offset = offset
        # The field to use for sorting the results. By default, this parameter is empty.
        # 
        # The field must be a metadata field or a default table field, such as `id`. Supported formats include:
        # 
        # You can specify a single field (for example, `chunk_id`), multiple comma-separated fields (for example, `block_id, chunk_id`), or fields with descending order (for example, `block_id DESC, chunk_id DESC`).
        self.order_by = order_by
        # The query text.
        # 
        # This parameter is required.
        self.query = query
        # The recall window. If specified, this parameter expands the context of the retrieved results. The format is a two-element array `[A, B]`, where `-10 <= A <= 0` and `0 <= B <= 10`.
        # 
        # > - Recommended when document chunks are highly fragmented, which might cause context loss during retrieval.
        # >
        # > - Reranking occurs before windowing is applied.
        self.recall_window = recall_window
        # The factor used to rerank vector search results. The value must be in the range (1, 5].
        # 
        # > - Reranking may be slow if document chunks are sparse.
        # >
        # > - The number of items to rerank, calculated as `ceil(TopK * RerankFactor)`, should not exceed 50.
        self.rerank_factor = rerank_factor
        # The number of top-ranked results to return.
        self.top_k = top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter is not None:
            result['Filter'] = self.filter

        if self.hybrid_search is not None:
            result['HybridSearch'] = self.hybrid_search

        if self.hybrid_search_args is not None:
            result['HybridSearchArgs'] = self.hybrid_search_args

        if self.include_metadata_fields is not None:
            result['IncludeMetadataFields'] = self.include_metadata_fields

        if self.include_vector is not None:
            result['IncludeVector'] = self.include_vector

        if self.kb_uuid is not None:
            result['KbUuid'] = self.kb_uuid

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.query is not None:
            result['Query'] = self.query

        if self.recall_window is not None:
            result['RecallWindow'] = self.recall_window

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        if self.top_k is not None:
            result['TopK'] = self.top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args = m.get('HybridSearchArgs')

        if m.get('IncludeMetadataFields') is not None:
            self.include_metadata_fields = m.get('IncludeMetadataFields')

        if m.get('IncludeVector') is not None:
            self.include_vector = m.get('IncludeVector')

        if m.get('KbUuid') is not None:
            self.kb_uuid = m.get('KbUuid')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('Query') is not None:
            self.query = m.get('Query')

        if m.get('RecallWindow') is not None:
            self.recall_window = m.get('RecallWindow')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        return self

