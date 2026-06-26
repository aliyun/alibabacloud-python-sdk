# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import BinaryIO, Dict, List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class QueryContentAdvanceRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        content: str = None,
        dbinstance_id: str = None,
        file_name: str = None,
        file_url_object: BinaryIO = None,
        filter: str = None,
        graph_enhance: bool = None,
        graph_search_args: main_models.QueryContentAdvanceRequestGraphSearchArgs = None,
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
        rerank_model: main_models.QueryContentAdvanceRequestRerankModel = None,
        top_k: int = None,
        url_expiration: str = None,
        use_full_text_retrieval: bool = None,
    ):
        # The name of the document collection.
        # 
        # > The document collection is created by calling the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) operation. You can call the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) operation to query existing document collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The text content used for retrieval.
        self.content = content
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the source image file to search in image-to-image search scenarios.
        # 
        # > The image file must have a file extension. Supported image extensions: bmp, jpg, jpeg, png, and tiff.
        self.file_name = file_name
        # The publicly accessible URL of the image file in image-to-image search scenarios.
        # 
        # > The image file must have a file extension. Supported image extensions: bmp, jpg, jpeg, png, and tiff.
        self.file_url_object = file_url_object
        # The filter condition for the data to query, in SQL WHERE clause format. The filter is an expression that returns a Boolean value (true or false). Conditions can be simple comparison operators such as equal to (=), not equal to (<> or !=), greater than (>), less than (<), greater than or equal to (>=), and less than or equal to (<=). Conditions can also be more complex expressions combined with logical operators (AND, OR, NOT), as well as conditions using the IN, BETWEEN, and LIKE keywords.
        # 
        # > 
        # > - For detailed syntax, refer to: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/.
        self.filter = filter
        # Specifies whether to enable knowledge graph enhancement. Default value: false.
        self.graph_enhance = graph_enhance
        # The knowledge graph retrieval parameters.
        self.graph_search_args = graph_search_args
        # The multi-channel recall algorithm. Default value: empty, which indicates that the dense vector and full-text index scores are directly compared and sorted.
        # 
        # Valid values:
        # 
        # - RRF: Reciprocal Rank Fusion. A parameter k controls the fusion effect. For more information, see the HybridSearchArgs configuration.
        # - Weight: Weighted sorting. Parameters control the score weights of AISearch retrieve and full-text index results before sorting. For more information, see the HybridSearchArgs configuration.
        # - Cascaded: Full-text index retrieve is performed first, followed by AISearch retrieve based on the full-text index results.
        self.hybrid_search = hybrid_search
        # The algorithm parameters for multi-channel recall. RRF and Weight are supported. HybridPathsSetting specifies the recall paths: dense vectors (dense), sparse vectors (sparse), and full-text index (fulltext). If this value is empty, dense vectors (dense) and full-text index (fulltext) are used by default.
        # 
        # - RRF: Specifies the constant k in the score calculation formula `1/(k+rank_i)`. The value must be a positive integer greater than 1. Format:
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
        #    - Dual-path recall (without specifying HybridPathsSetting, only specifying alpha):
        #       - Formula: alpha * dense_score + (1-alpha) * fulltext_score. The alpha parameter specifies the score weight between dense vectors and full-text index retrieve. Valid values: 0 to 1, where 0 indicates full-text index only and 1 indicates dense vector only:
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        #   - Three-path recall pattern:
        #      - Formula: normalized_dense * dense_score + normalized_sparse * sparse_score + normalized_fulltext * fulltext_score. The dense, sparse, and fulltext values represent the weights for dense vectors, sparse vectors, and full-text index retrieve respectively. Valid values: greater than or equal to 0. The system automatically performs normalization of the weights to 0 to 1 (normalized_x = x / (dense + sparse + fulltext)).
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
        # Specifies whether to synchronously return the URL of the document. By default, the URL is not returned.
        self.include_file_url = include_file_url
        # The metadata fields to return. Default value: empty. Separate multiple fields with commas.
        self.include_metadata_fields = include_metadata_fields
        # Specifies whether to return vectors. Default value: false.
        # > - **false**: Does not return vectors.
        # > - **true**: Returns vectors.
        self.include_vector = include_vector
        # The similarity algorithm used for retrieval. If this value is empty, the algorithm specified when the knowledge base was created is used. Leave this parameter empty unless you have specific requirements.
        # 
        # > Valid values:
        # > - **l2**: Euclidean distance.
        # > - **ip**: inner product distance.
        # > - **cosine**: cosine similarity.
        self.metrics = metrics
        # The namespace. Default value: public.
        # 
        # > You can create a namespace by calling the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation and query namespaces by calling the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation.
        self.namespace = namespace
        # The password of the namespace.
        # 
        # > This value is specified by the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The offset for paged query. Used for paging through results.
        self.offset = offset
        # The field used for sorting. Default value: empty.
        # 
        # The field must belong to metadata or a default field in the table, such as id. Supported formats:
        # 
        # A single field, such as chunk_id.
        # Multiple fields separated by commas, such as block_id, chunk_id.
        # Descending order, such as block_id DESC, chunk_id DESC.
        self.order_by = order_by
        self.owner_id = owner_id
        # The recall window. When this value is not empty, additional context around the retrieval results is returned. The format is a two-element array: List<A, B>, where -10<=A<=0 and 0<=B<=10.
        # > - Use this parameter when documents are split into overly small chunks and retrieval may lose contextual information.
        # > - Reranking takes priority over windowing. Reranking is performed first, followed by windowing.
        self.recall_window = recall_window
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The reranking factor. When this value is not empty, the AISearch retrieve results are reranked. Valid values: 1 < RerankFactor <= 5.
        # > - Reranking is slow when documents are sparsely chunked.
        # > - The total number of reranked results (TopK × Factor, rounded up) should not exceed 50.
        self.rerank_factor = rerank_factor
        # The rerank model parameters.
        self.rerank_model = rerank_model
        # The number of top results to return.
        self.top_k = top_k
        # The validity period of the returned image URL.
        # 
        # > Valid values:
        # > - Supports seconds (s) and days (d) as units. For example, 300s indicates a validity period of 300 seconds, and 60d indicates a validity period of 60 days.
        # > - Valid values: 60s to 365d.
        # > - Default value: 7200s (2 hours).
        self.url_expiration = url_expiration
        # (Deprecated) Specifies whether to use full-text retrieval (dual-path recall). Default value: false, which indicates that only vector retrieval is used.
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

        if self.file_url_object is not None:
            result['FileUrl'] = self.file_url_object

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
            self.file_url_object = m.get('FileUrl')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('GraphEnhance') is not None:
            self.graph_enhance = m.get('GraphEnhance')

        if m.get('GraphSearchArgs') is not None:
            temp_model = main_models.QueryContentAdvanceRequestGraphSearchArgs()
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
            temp_model = main_models.QueryContentAdvanceRequestRerankModel()
            self.rerank_model = temp_model.from_map(m.get('RerankModel'))

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UrlExpiration') is not None:
            self.url_expiration = m.get('UrlExpiration')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class QueryContentAdvanceRequestRerankModel(DaraModel):
    def __init__(
        self,
        instruct: str = None,
        name: str = None,
        rerank_metadata_fields: str = None,
    ):
        # This parameter can be set when RerankModel.Name is qwen3-rerank.
        # Adds a custom sorting task type description. This parameter guides the model to adopt different sorting strategies.
        self.instruct = instruct
        # The name of the rerank model. Valid values: qwen3-rerank, gte-rerank-v2.
        self.name = name
        self.rerank_metadata_fields = rerank_metadata_fields

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

        if self.rerank_metadata_fields is not None:
            result['RerankMetadataFields'] = self.rerank_metadata_fields

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Instruct') is not None:
            self.instruct = m.get('Instruct')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RerankMetadataFields') is not None:
            self.rerank_metadata_fields = m.get('RerankMetadataFields')

        return self

class QueryContentAdvanceRequestGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # The number of top entities and relationship edges to return. Default value: 60.
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

