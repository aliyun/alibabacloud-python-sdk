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
        top_k: int = None,
        url_expiration: str = None,
        use_full_text_retrieval: bool = None,
    ):
        # Document collection name.
        # 
        # > Created by the [CreateDocumentCollection](https://help.aliyun.com/document_detail/2618448.html) API. You can use the [ListDocumentCollections](https://help.aliyun.com/document_detail/2618452.html) API to view the list of created document collections.
        # 
        # This parameter is required.
        self.collection = collection
        self.content = content
        # Instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB for PostgreSQL instances in the target region, including the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # In image search scenarios, the source file name of the image to be searched.
        # 
        # > The image file must have a file extension. Currently supported image extensions: bmp, jpg, jpeg, png, tiff.
        self.file_name = file_name
        # In image search scenarios, the publicly accessible URL of the image file.
        # 
        # > The image file must have a file extension. Currently supported image extensions: bmp, jpg, jpeg, png, tiff.
        self.file_url = file_url
        # Filter condition for the data to be queried, in SQL WHERE format. It is an expression that returns a boolean value (true or false). The conditions can be simple comparison operators such as equal (=), not equal (<> or !=), greater than (>), less than (<), greater than or equal to (>=), less than or equal to (<=), or more complex expressions combined with logical operators (AND, OR, NOT), and conditions using keywords like IN, BETWEEN, LIKE, etc.
        # 
        # > 
        # > - For detailed syntax, refer to: https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/
        self.filter = filter
        # Whether to enable knowledge graph enhancement. Default value: false.
        self.graph_enhance = graph_enhance
        # The search parameters of the knowledge graph.
        self.graph_search_args = graph_search_args
        # Dual recall algorithm, default is empty (i.e., directly compare and sort the scores of vectors and full text).
        # 
        # Available values:
        # 
        # - RRF: Reciprocal rank fusion, with a parameter k controlling the fusion effect. See HybridSearchArgs configuration for details;
        # - Weight: Weighted ranking, using a parameter alpha to control the weight of vector and full-text scores, then sorting. See HybridSearchArgs configuration for details;
        # - Cascaded: Perform full-text retrieval first, then vector retrieval on top of it;
        self.hybrid_search = hybrid_search
        # The parameters of the two-way retrieval algorithm. The following parameters are supported:
        # 
        # *   When HybridSearch is set to RRF, the scores are calculated by using the `1/(k+rank_i)` formula. The constant k is a positive integer that is greater than 1.
        # 
        # <!---->
        # 
        #     { 
        #        "RRF": {
        #         "k": 60
        #        }
        #     }
        # 
        # *   When HybridSearch is set to Weight, the scores are calculated by using the `alpha * vector_score + (1-alpha) * text_score` formula. The alpha parameter specifies the proportion of the vector search score and the full-text search score and ranges from 0 to 1. A value of 0 specifies full-text search and a value of 1 specifies vector search.
        # 
        # <!---->
        # 
        #     { 
        #        "Weight": {
        #         "alpha": 0.5
        #        }
        #     }
        self.hybrid_search_args = hybrid_search_args
        # Specifies whether to return the URL of the document. Default value: false.
        self.include_file_url = include_file_url
        # The metadata fields to be returned. Separate multiple fields with commas (,). This parameter is empty by default.
        self.include_metadata_fields = include_metadata_fields
        # Whether to return vectors. Default is false.
        # > - **false**: Do not return vectors.
        # > - **true**: Return vectors.
        self.include_vector = include_vector
        # Similarity algorithm used during retrieval. If this value is empty, the algorithm specified at the time of knowledge base creation is used. It is recommended not to set this unless there is a specific need.
        # 
        # > Value description:
        # > - **l2**: Euclidean distance.
        # > - **ip**: Inner product (dot product) distance.
        # > - **cosine**: Cosine similarity.
        self.metrics = metrics
        # Namespace, default is public.
        # 
        # > You can create a namespace using the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) API and view the list of namespaces using the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) API.
        self.namespace = namespace
        # Password for the namespace.
        # 
        # > This value is specified in the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) API.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # Offset, used for paginated queries.
        self.offset = offset
        # The fields by which to sort the results. This parameter is empty by default.
        # 
        # The field must be either a metadata field or a default field in the table (e.g., id). Supported formats include:
        # 
        # Single field, such as chunk_id. Multiple fields that are separated by commas (,), such as block_id,chunk_id. Descending order is supported, e.g., block_id DESC, chunk_id DESC.
        self.order_by = order_by
        self.owner_id = owner_id
        # Recall window. When this value is not empty, it adds context to the returned search results. The format is an array of 2 elements: List<A, B>, where -10 <= A <= 0 and 0 <= B <= 10.
        # > - Recommended when documents are fragmented and retrieval may lose contextual information.
        # > - Re-ranking takes precedence over windowing, i.e., re-rank first, then apply windowing.
        self.recall_window = recall_window
        # The region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Re-ranking factor. When this value is not empty, it will re-rank the vector search results. The value range is 1 < RerankFactor <= 5.
        # > - Re-ranking is slower when documents are sparsely split.
        # > - It is recommended that the re-ranked count (TopK * Factor, rounded up) does not exceed 50.
        self.rerank_factor = rerank_factor
        # The number of the returned top results.
        self.top_k = top_k
        # The validity period of the returned image URL.
        # 
        # >  Value Description
        # 
        # *   Supported units are seconds (s) and days (d). For example, 300s specifies that the URL is valid for 300 seconds, and 60d specifies that the URL is valid for 60 days.
        # 
        # *   Valid values: 60s to 365d.
        # 
        # *   Default value: 7200s, that is, 2 hours.
        self.url_expiration = url_expiration
        # Whether to use full-text retrieval (dual recall). Default is false, which means only vector retrieval is used.
        self.use_full_text_retrieval = use_full_text_retrieval

    def validate(self):
        if self.graph_search_args:
            self.graph_search_args.validate()

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

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('UrlExpiration') is not None:
            self.url_expiration = m.get('UrlExpiration')

        if m.get('UseFullTextRetrieval') is not None:
            self.use_full_text_retrieval = m.get('UseFullTextRetrieval')

        return self

class QueryContentRequestGraphSearchArgs(DaraModel):
    def __init__(
        self,
        graph_top_k: int = None,
    ):
        # The number of top entities and relationship edges. Default value: 60.
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

