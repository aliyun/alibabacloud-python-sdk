# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryCollectionDataShrinkRequest(DaraModel):
    def __init__(
        self,
        collection: str = None,
        content: str = None,
        dbinstance_id: str = None,
        filter: str = None,
        hybrid_search: str = None,
        hybrid_search_args_shrink: str = None,
        include_metadata_fields: str = None,
        include_sparse_values: bool = None,
        include_values: bool = None,
        metrics: str = None,
        namespace: str = None,
        namespace_password: str = None,
        offset: int = None,
        order_by: str = None,
        owner_id: int = None,
        region_id: str = None,
        relational_table_filter_shrink: str = None,
        sparse_vector_shrink: str = None,
        top_k: int = None,
        vector_shrink: str = None,
        workspace_id: str = None,
    ):
        # Collection name.
        # 
        # > You can use the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) API to view the list.
        # 
        # This parameter is required.
        self.collection = collection
        # Content for full-text search. When this value is empty, only vector search is used; when it is not empty, both vector and full-text search are used.
        # 
        # > The Vector parameter cannot be empty at the same time.
        self.content = content
        # Instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) API to view details of all AnalyticDB PostgreSQL instances in the target region, including the instance ID.
        self.dbinstance_id = dbinstance_id
        self.filter = filter
        # Dual-path recall algorithm, default is empty (i.e., directly compare and sort the scores of vectors and full-text).
        # 
        # Available values:
        # 
        # - RRF: Reciprocal rank fusion, with a parameter k controlling the fusion effect. See HybridSearchArgs configuration for details;
        # - Weight: Weighted sorting, using a parameter alpha to control the score ratio of vectors and full-text, then sorting. See HybridSearchArgs configuration for details;
        # - Cascaded: Perform full-text search first, then vector search based on the full-text results;
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
        self.hybrid_search_args_shrink = hybrid_search_args_shrink
        # Defaults to empty, indicating the metadata fields to return. Multiple fields should be separated by commas.
        self.include_metadata_fields = include_metadata_fields
        self.include_sparse_values = include_sparse_values
        # Whether to return vector data. Value descriptions:
        # - **true**: Return vector data.
        # - **false**: Do not return vector data, used for full-text search scenarios.
        self.include_values = include_values
        # Similarity algorithm used during retrieval. Value descriptions:
        # - **l2**: Euclidean distance.
        # - **ip**: Inner product (dot product) distance.
        # - **cosine**: Cosine similarity.
        # 
        # > If this value is empty, the algorithm specified during index creation is used.
        self.metrics = metrics
        # Namespace.
        # 
        # > You can use the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) API to view the list.
        self.namespace = namespace
        # Password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # Defaults to empty, indicating the starting point for pagination queries. Does not support hybrid search scenarios.
        # 
        # The value must be >= 0. When this value is not empty, it will return `Total`, which indicates the total number of hits. This parameter works with `TopK`. For example, to paginate 20 and retrieve chunks with `chunk_id` from 0 to 44, you need to make three requests:
        # - `Offset=0, TopK=20` returns `chunk_id` 0~19
        # - `Offset=20, TopK=20` returns `chunk_id` 20~39
        # - `Offset=30, TopK=20` returns `chunk_id` 40~44
        self.offset = offset
        # Defaults to empty, indicating the field for sorting. Does not support hybrid search scenarios.
        # 
        # The field must belong to metadata or be a default field in the table, such as `id`. The supported formats are:
        # - A single field, e.g., `chunk_id`;
        # - Multiple fields, separated by commas, e.g., `block_id, chunk_id`;
        # - Supports reverse order, e.g., `block_id DESC, chunk_id DESC`;
        self.order_by = order_by
        self.owner_id = owner_id
        # Region ID where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Uses another relational table to filter vector data (similar to a Join function).
        # 
        # > Data from the relational table can be returned by setting the `IncludeMetadataFields` parameter. For example, `rds_table_name.id` indicates returning the `id` field from the relational table.
        self.relational_table_filter_shrink = relational_table_filter_shrink
        self.sparse_vector_shrink = sparse_vector_shrink
        # Set the number of top results to return.
        # 
        # This parameter is required.
        self.top_k = top_k
        # Vector data, with the same dimension as specified in the [CreateCollection](https://help.aliyun.com/document_detail/2401497.html) API.
        # > When the vector is empty, only full-text search results are returned.
        self.vector_shrink = vector_shrink
        # The ID of the Workspace composed of multiple database instances. This parameter and `DBInstanceId` cannot both be empty. If both are specified, this parameter takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

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

        if self.filter is not None:
            result['Filter'] = self.filter

        if self.hybrid_search is not None:
            result['HybridSearch'] = self.hybrid_search

        if self.hybrid_search_args_shrink is not None:
            result['HybridSearchArgs'] = self.hybrid_search_args_shrink

        if self.include_metadata_fields is not None:
            result['IncludeMetadataFields'] = self.include_metadata_fields

        if self.include_sparse_values is not None:
            result['IncludeSparseValues'] = self.include_sparse_values

        if self.include_values is not None:
            result['IncludeValues'] = self.include_values

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.relational_table_filter_shrink is not None:
            result['RelationalTableFilter'] = self.relational_table_filter_shrink

        if self.sparse_vector_shrink is not None:
            result['SparseVector'] = self.sparse_vector_shrink

        if self.top_k is not None:
            result['TopK'] = self.top_k

        if self.vector_shrink is not None:
            result['Vector'] = self.vector_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Filter') is not None:
            self.filter = m.get('Filter')

        if m.get('HybridSearch') is not None:
            self.hybrid_search = m.get('HybridSearch')

        if m.get('HybridSearchArgs') is not None:
            self.hybrid_search_args_shrink = m.get('HybridSearchArgs')

        if m.get('IncludeMetadataFields') is not None:
            self.include_metadata_fields = m.get('IncludeMetadataFields')

        if m.get('IncludeSparseValues') is not None:
            self.include_sparse_values = m.get('IncludeSparseValues')

        if m.get('IncludeValues') is not None:
            self.include_values = m.get('IncludeValues')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RelationalTableFilter') is not None:
            self.relational_table_filter_shrink = m.get('RelationalTableFilter')

        if m.get('SparseVector') is not None:
            self.sparse_vector_shrink = m.get('SparseVector')

        if m.get('TopK') is not None:
            self.top_k = m.get('TopK')

        if m.get('Vector') is not None:
            self.vector_shrink = m.get('Vector')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

