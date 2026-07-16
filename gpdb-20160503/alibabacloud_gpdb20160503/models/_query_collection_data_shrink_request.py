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
        # The name of the collection.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to list available collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The content for full-text search. If this parameter is omitted, only vector search is performed. If this parameter is specified, the system performs a hybrid search of vector search and full-text search.
        # 
        # > You must specify one of the Content and Vector parameters.
        self.content = content
        # The ID of the instance.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query details for all AnalyticDB for PostgreSQL instances in a region, including their instance IDs.
        self.dbinstance_id = dbinstance_id
        # The filter conditions for data retrieval. It is in the format of a WHERE clause in SQL. This expression returns a boolean value, which can be a simple comparison operator, such as `=`, `<>`, `!=`, `>`, `<`, `>=`, and `<=`, or a more complex expression combined with logical operators, such as `AND`, `OR`, and `NOT`, and keywords such as `IN`, `BETWEEN`, and `LIKE`.
        # 
        # > - For more information about the syntax, see [PostgreSQL WHERE](https://www.postgresqltutorial.com/postgresql-tutorial/postgresql-where/).
        self.filter = filter
        # The hybrid search algorithm. If this parameter is empty, the system ranks results by directly comparing the scores from the vector search and the full-text search.
        # 
        # Valid values:
        # 
        # - `RRF`: Reciprocal Rank Fusion. This algorithm has a parameter k to control the fusion effect. For more information, see the description of the `HybridSearchArgs` parameter.
        # 
        # - `Weight`: weighted sort. This algorithm uses a parameter alpha to control the score ratio of vector search and full-text search, and then sorts the results. For more information about the parameter, see the `HybridSearchArgs` parameter.
        # 
        # - `Cascaded`: performs a full-text search, and then performs a vector search on the search results.
        self.hybrid_search = hybrid_search
        # The parameters for the hybrid search algorithm. The following algorithms are supported: RRF and Weight.
        # 
        # - For RRF, specify the constant k in the scoring algorithm `1/(k+rank_i)`. The value must be a positive integer greater than 1. The format is as follows:
        # 
        # ```
        # { 
        #    "RRF": {
        #     "k": 60
        #    }
        # }
        # ```
        # 
        # - For Weight, in the formula `alpha * vector_score + (1-alpha) * text_score`, the alpha parameter indicates the score ratio of the vector search to the full-text search. The value ranges from 0 to 1. 0 indicates that only the full-text search is used, and 1 indicates that only the vector search is used.
        # 
        # ```
        # { 
        #    "Weight": {
        #     "alpha": 0.5
        #    }
        # }
        # ```
        self.hybrid_search_args_shrink = hybrid_search_args_shrink
        # This parameter is left empty by default. It specifies the metadata fields to be returned. You can specify multiple fields and separate them with commas (,).
        self.include_metadata_fields = include_metadata_fields
        # Specifies whether to return sparse vector data. Valid values:
        # 
        # - **true**: returns sparse vector data.
        # 
        # - **false**: does not return sparse vector data.
        self.include_sparse_values = include_sparse_values
        # Specifies whether to return dense vector data. Valid values:
        # 
        # - **true**: returns dense vector data.
        # 
        # - **false**: does not return dense vector data.
        self.include_values = include_values
        # The similarity algorithm for search. Valid values:
        # 
        # - **l2**: the Euclidean distance.
        # 
        # - **ip**: the dot product distance.
        # 
        # - **cosine**: the cosine similarity.
        # 
        # > If this parameter is not specified, the algorithm specified when the index is created is used.
        self.metrics = metrics
        # The name of the namespace.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to list available namespaces.
        self.namespace = namespace
        # The password for the namespace.
        # 
        # This parameter is required.
        self.namespace_password = namespace_password
        # This parameter is left empty by default. It specifies the start position of a paged query. This parameter is not supported in hybrid search.
        # 
        # The value must be greater than or equal to 0. When this parameter is not empty, Total in the response indicates the total number of hits. This parameter is used with TopK. For example, if you want to retrieve chunks 0 to 44 with a page size of 20, you must send three requests:
        # 
        # - `Offset=0, TopK=20` returns chunks 0 to 19.
        # 
        # - `Offset=20, TopK=20` returns chunks 20 to 39.
        # 
        # - `Offset=40, TopK=20` returns chunks 40 to 44.
        self.offset = offset
        # This parameter is left empty by default. It specifies the field based on which to sort the results. This parameter is not supported in hybrid search.
        # 
        # The field must be a metadata field or a default field in the table, such as `id`. The following formats are supported:
        # 
        # - A single field, such as `chunk_id`.
        # 
        # - Multiple fields separated by commas (,), such as `block_id, chunk_id`.
        # 
        # - Descending order, such as `block_id DESC, chunk_id DESC`.
        self.order_by = order_by
        self.owner_id = owner_id
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Uses another relational table to filter vector data, which is similar to the JOIN operation.
        # 
        # > The data of the relational table can be returned by setting the IncludeMetadataFields parameter. For example, `rds_table_name.id` indicates that the id field of the relational table is returned.
        self.relational_table_filter_shrink = relational_table_filter_shrink
        # The sparse vector data.
        self.sparse_vector_shrink = sparse_vector_shrink
        # Specifies the number of top results to return.
        # 
        # This parameter is required.
        self.top_k = top_k
        # The vector data. The length of the vector data must be the same as that specified in the [CreateCollection](https://help.aliyun.com/document_detail/2401497.html) operation.
        # 
        # > - If `SparseVector` is empty, only the dense vector search results are returned.
        # >
        # > - If both `Vector` and `SparseVector` are empty, only the full-text search results are returned.
        self.vector_shrink = vector_shrink
        # The ID of the workspace that consists of multiple database instances. You must specify this parameter or the DBInstanceId parameter. If both this parameter and DBInstanceId are specified, this parameter is used.
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

