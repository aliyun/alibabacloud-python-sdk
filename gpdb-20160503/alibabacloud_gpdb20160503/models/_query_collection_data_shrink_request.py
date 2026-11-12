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
        # The collection name.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to view the list.
        # 
        # This parameter is required.
        self.collection = collection
        # The content used for full-text retrieval. If this parameter is left empty, only vector retrieval is used. If this parameter is specified, both vector and full-text retrieval are used.
        # 
        # > This parameter and the Vector parameter cannot be left empty at the same time.
        self.content = content
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance IDs.
        self.dbinstance_id = dbinstance_id
        # The filter condition for the data to query, in the SQL WHERE clause format. It is an expression that returns a Boolean value (true or false). The condition can be a simple comparison operator, such as equal to (=), not equal to (<> or !=), greater than (>), less than (<), greater than or equal to (>=), or less than or equal to (<=). It can also be a more complex expression combined with logical operators (AND, OR, NOT), or a condition that uses keywords such as IN, BETWEEN, and LIKE.
        # 
        # > 
        # > - For detailed syntax, refer to https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/
        self.filter = filter
        # The dual-channel recall algorithm. Default value: empty (which means the vector and full-text scores are directly compared and sorting is applied). Valid values:
        # 
        # - RRF: reciprocal rank fusion. A parameter k is used to control the fusion effect. For more information, see the HybridSearchArgs configuration.
        # - Weight: weighted sorting. A parameter alpha is used to control the weight of the vector and full-text scores before sorting. For more information, see the HybridSearchArgs configuration.
        # - Cascaded: full-text retrieval is performed first, and then vector retrieval is performed based on the results.
        self.hybrid_search = hybrid_search
        # The algorithm parameters for hybrid search. RRF and Weight are supported:
        # 
        # - RRF: specifies the constant k in the score calculation formula `1/(k+rank_i)`. The value must be a positive integer greater than 1. Format:
        # ```
        # { 
        #    "RRF": {
        #     "k": 60
        #    }
        # }
        # ```
        # 
        # - Weight: The calculation formula is `alpha * vector_score + (1-alpha) * text_score`. The parameter alpha represents the weight of the vector and full-text search scores. The value ranges from 0 to 1, where 0 indicates full-text search only and 1 indicates vector search only. Format:
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        self.hybrid_search_args_shrink = hybrid_search_args_shrink
        # The metadata fields to return. Default value: empty. Separate multiple fields with commas.
        self.include_metadata_fields = include_metadata_fields
        # Specifies whether to return sparse vector data. Valid values:
        # - **true**: returns sparse vector data.
        # - **false**: does not return sparse vector data.
        self.include_sparse_values = include_sparse_values
        # Specifies whether to return dense vector data. Valid values:
        # - **true**: returns dense vector data.
        # - **false**: does not return dense vector data.
        self.include_values = include_values
        # The similarity algorithm used during search. Valid values:
        # - **l2**: Euclidean distance.
        # - **ip**: Dot product (inner product) distance.
        # - **cosine**: Cosine similarity.
        # 
        # > If this parameter is left empty, the algorithm specified when the index is built is used.
        self.metrics = metrics
        # The namespace.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to view the list.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # The retrieval starting point during paged queries. Default value: empty. This parameter is not supported in dual-channel recall scenarios.
        # 
        # The value must be greater than or equal to 0. If this parameter is specified, the Total parameter is returned to indicate the total number of hits. This parameter is used together with TopK. For example, to retrieve chunks with chunk_id ranging from 0 to 44 with a paging size of 20, you must make three requests:
        # - Offset=0, TopK=20 returns chunks with chunk_id ranging from 0 to 19.
        # - Offset=20, TopK=20 returns chunks with chunk_id ranging from 20 to 39.
        # - Offset=30, TopK=20 returns chunks with chunk_id ranging from 40 to 44.
        self.offset = offset
        # The field based on which the results are sorted. Default value: empty. This parameter is not supported in hybrid search scenarios.
        # 
        # The field must belong to the metadata or be a default field in the table, such as id. Supported formats:
        # - A single field, such as chunk_id.
        # - Multiple fields separated by commas, such as block_id, chunk_id.
        # - Descending order, such as block_id DESC, chunk_id DESC.
        self.order_by = order_by
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Uses another relational table to filter vector data, similar to the JOIN operation.
        # 
        # > You can set the IncludeMetadataFields parameter to return data from the relational table. For example, rds_table_name.id indicates that the id field of the relational table is returned.
        self.relational_table_filter_shrink = relational_table_filter_shrink
        # The list of sparse vector data.
        self.sparse_vector_shrink = sparse_vector_shrink
        # The number of top results to return.
        # 
        # This parameter is required.
        self.top_k = top_k
        # The vector data. The length must be consistent with the dimension specified in the [CreateCollection](https://help.aliyun.com/document_detail/2401497.html) operation.
        # > 
        # > - If SparseVector is left empty, the system uses it to retrieve only dense vector results.
        # > - If both Vector and SparseVector are left empty, the system uses it to retrieve only full-text results.
        self.vector_shrink = vector_shrink
        # The ID of the workspace that consists of multiple database instances. This parameter and the DBInstanceId parameter cannot be left empty at the same time. If both parameters are specified, this parameter takes precedence.
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

