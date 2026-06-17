# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryContentRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        content: str = None,
        dbinstance_id: str = None,
        file_name: str = None,
        file_url: str = None,
        filter: str = None,
        graph_enhance: bool = None,
        graph_search_args: main_models.QueryContentRequestGraphSearchArgs = None,
        hybrid_search: str = None,
        hybrid_search_args: Dict[str, dict] = None,
        include_file_url: bool = None,
        include_metadata_fields: str = None,
        include_vector: bool = None,
        metrics: str = None,
        namespace: str = None,
        namespace_password: str = None,
        offset: int = None,
        order_by: str = None,
        owner_id: int = None,
        recall_window: List[int] = None,
        region_id: str = None,
        rerank_factor: float = None,
        rerank_model: main_models.QueryContentRequestRerankModel = None,
        top_k: int = None,
        url_expiration: str = None,
        use_full_text_retrieval: bool = None,
    ):
        # The name of the document collection.
        # 
        # > A document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. Call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to list your document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The text to use for retrieval.
        self.content = content
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to find the IDs of all AnalyticDB for PostgreSQL instances in a region.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The filename of the source image for a search-by-image query.
        # 
        # > The image file must have a file extension. The supported extensions are bmp, jpg, jpeg, png, and tiff.
        self.file_name = file_name
        # The publicly accessible URL of the image file for a search-by-image query.
        # 
        # > The image file must have a file extension. The supported extensions are bmp, jpg, jpeg, png, and tiff.
        self.file_url = file_url
        # A filter condition for the query, specified as a SQL `WHERE` clause that returns a boolean value. The clause can use comparison operators (such as `=`, `<>`, `!=`, `>`, `<`, `>=`, and `<=`), logical operators (`AND`, `OR`, and `NOT`), and keywords such as `IN`, `BETWEEN`, and `LIKE`.
        # 
        # > - For details about the syntax, see https\\://www\\.postgresqltutorial.com/postgresql-tutorial/postgresql-where/.
        self.filter = filter
        # Specifies whether to enable knowledge graph enhancement. The default value is `false`.
        self.graph_enhance = graph_enhance
        # The parameters for knowledge graph retrieval.
        self.graph_search_args = graph_search_args
        # Specifies the hybrid search algorithm. If this parameter is not specified, the system directly compares and sorts the scores from dense vector retrieval and full-text search.
        # 
        # Valid values:
        # 
        # - RRF: reciprocal rank fusion. This method uses a `k` parameter to control the fusion effect. For more information, see the `HybridSearchArgs` parameter.
        # 
        # - Weight: A weighted sorting method. This method uses parameters to control the score weights of vector retrieval and full-text search before sorting. For more information, see the `HybridSearchArgs` parameter.
        # 
        # - Cascaded: Performs full-text search first, and then performs vector retrieval on the results.
        self.hybrid_search = hybrid_search
        # Parameters for the multi-channel recall algorithm. Currently, `RRF` and `Weight` are supported. `HybridPathsSetting` can be used to specify the recall paths, including dense vector search (`dense`), sparse vector search (`sparse`), and full-text search (`fulltext`). If this parameter is not specified, the system recalls dense vectors and full-text search results by default.
        # 
        # - RRF: Specifies the constant `k` in the scoring formula `1/(k+rank_i)`. The value must be an integer greater than 1. Example:
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
        # - Weight:
        # 
        #   - For dual-channel recall (if `HybridPathsSetting` is not specified, only `alpha` is configured):
        # 
        #     - The score is calculated using the formula: `alpha * dense_score + (1-alpha) * fulltext_score`. The `alpha` parameter represents the score weight of dense vector retrieval relative to full-text search. The value must be in the range of 0 to 1. A value of 0 indicates that only full-text search is used, and a value of 1 indicates that only dense vector retrieval is used.
        # 
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        # 
        # - For three-channel recall:
        # 
        #   - The score is calculated using the formula: `normalized_dense * dense_score + normalized_sparse * sparse_score + normalized_fulltext * fulltext_score`. The `dense`, `sparse`, and `fulltext` parameters represent the weights for the dense vector, sparse vector, and full-text search results, respectively. Their values must be greater than or equal to 0. The system automatically normalizes the weights to a sum of 1 (for example, `normalized_x = x / (dense + sparse + fulltext)`).
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
        # Specifies whether to return the URL of the document. The default value is `false`.
        self.include_file_url = include_file_url
        # The metadata fields to include in the response. If left empty, no metadata is returned. To specify multiple fields, use a comma-separated list.
        self.include_metadata_fields = include_metadata_fields
        # Specifies whether to include the vector in the results. The default value is `false`.
        # 
        # > - **false**: The vector is not returned.
        # >
        # > - **true**: The vector is returned.
        self.include_vector = include_vector
        # The similarity algorithm used for retrieval. If this parameter is not specified, the algorithm that was specified when the document collection was created is used. We recommend that you do not set this parameter unless you have specific requirements.
        # 
        # > Valid values:
        # >
        # > - **l2**: Euclidean distance.
        # >
        # > - **ip**: dot product (inner product) distance.
        # >
        # > - **cosine**: cosine similarity.
        self.metrics = metrics
        # The namespace. The default value is `public`.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to list existing namespaces.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # > This password is set when you call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The offset for paginated queries.
        self.offset = offset
        # The field to sort the results by. By default, this parameter is empty.
        # 
        # The field must be a metadata field or a default field from the table, such as `id`. Supported formats include single fields (e.g., `chunk_id`), multiple comma-separated fields (e.g., `block_id, chunk_id`), and fields with a sort direction (e.g., `block_id DESC, chunk_id DESC`).
        self.order_by = order_by
        self.owner_id = owner_id
        # The recall window. If this parameter is specified, additional context is returned with the retrieval results. The value must be a two-element array, `[A, B]`, where `-10 <= A <= 0` and `0 <= B <= 10`.
        # 
        # > - Use this parameter when documents are finely chunked and retrieval might otherwise lose contextual information.
        # >
        # > - Reranking is prioritized over windowing. The system first applies reranking and then processes the window.
        self.recall_window = recall_window
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The factor for reranking vector retrieval results. The value must be greater than 1 and less than or equal to 5.
        # 
        # > - Reranking may be slower if document chunks are sparse.
        # >
        # > - For best performance, the number of items to be reranked (`TopK` \\* `RerankFactor`, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The parameters for the reranking model.
        self.rerank_model = rerank_model
        # The number of top results to return.
        self.top_k = top_k
        # The validity period of the returned image URL.
        # 
        # > - The value can be specified in seconds (s) or days (d). For example, `300s` indicates that the link is valid for 300 seconds, and `60d` indicates that the link is valid for 60 days.
        # >
        # > - The value must be in the range of `60s` to `365d`.
        # >
        # > - Default value: `7200s` (2 hours).
        self.url_expiration = url_expiration
        # (Deprecated) Specifies whether to use full-text search (dual-channel recall). The default value is `false`, which means only vector retrieval is used.
        self.use_full_text_retrieval = use_full_text_retrieval

    def validate(self):
        if self.graph_search_args:
            self.graph_search_args.validate()
        if self.rerank_model:
            self.rerank_model.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection is not None:
            result['Collection'] = self.collection

        if self.content is not None:
            result['Content'] = self.content

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.graph_enhance is not None:
            result['GraphEnhance'] = self.graph_enhance

        if self.graph_search_args is not None:
            result['GraphSearchArgs'] = self.graph_search_args.to_map()

        if self.hybrid_search is not None:
            result['HybridSearch'] = self.hybrid_search

        if self.hybrid_search_args is not None:
            result['HybridSearchArgs'] = self.hybrid_search_args

        if self.include_file_url is not None:
            result['IncludeFileUrl'] = self.include_file_url

        if self.include_metadata_fields is not None:
            result['IncludeMetadataFields'] = self.include_metadata_fields

        if self.include_vector is not None:
            result['IncludeVector'] = self.include_vector

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.offset is not None:
            result['Offset'] = self.offset

        if self.order_by is not None:
            result['OrderBy'] = self.order_by

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.recall_window is not None:
            result['RecallWindow'] = self.recall_window

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rerank_factor is not None:
            result['RerankFactor'] = self.rerank_factor

        if self.rerank_model is not None:
            result['RerankModel'] = self.rerank_model.to_map()

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.url_expiration is not None:
            result['UrlExpiration'] = self.url_expiration

        if self.use_full_text_retrieval is not None:
            result['UseFullTextRetrieval'] = self.use_full_text_retrieval

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('GraphEnhance') is not None:
            self.graph_enhance = m.get('GraphEnhance')

        if m.get('GraphSearchArgs') is not None:
            temp_model = main_models.QueryContentRequestGraphSearchArgs()
            self.graph_search_args = temp_model.from_map(m.get('GraphSearchArgs'))

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args = m.get('HybridSearchArgs')

        if m.get('IncludeFileUrl') is not None:
            self.include_file_url = m.get('IncludeFileUrl')

        if m.get('IncludeMetadataFields') is not None:
            self.include_metadata_fields = m.get('IncludeMetadataFields')

        if m.get('IncludeVector') is not None:
            self.include_vector = m.get('IncludeVector')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('Offset') is not None:
            self.offset = m.get('Offset')

        if m.get('OrderBy') is not None:
            self.order_by = m.get('OrderBy')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RecallWindow') is not None:
            self.recall_window = m.get('RecallWindow')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RerankFactor') is not None:
            self.rerank_factor = m.get('RerankFactor')

        if m.get('RerankModel') is not None:
            temp_model = main_models.QueryContentRequestRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UrlExpiration') is not None:
            self.url_expiration = m.get('UrlExpiration')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class QueryContentRequestRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
    ):
        # This parameter is available only when `RerankModel.Name` is set to `qwen3-rerank`.
        # You can add a custom task description to guide the model\\"s sorting strategy.
        self.instruct = instruct
        # The name of the reranking model. Valid values: `qwen3-rerank`, `gte-rerank-v2`.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instruct is not None:
            result['Instruct'] = self.instruct

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class QueryContentRequestGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # The number of top entities and relationship edges to return. The default value is `60`.
        self.graph_top_k = graph_top_k

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.graph_top_k is not None:
            result['GraphTopK'] = self.graph_top_k

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GraphTopK') is not None:
            self.graph_top_k = m.get('GraphTopK')

        return self

