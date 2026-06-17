# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateCollectionShrinkRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        external_storage: int = None,
        full_text_retrieval_fields: str = None,
        hnsw_ef_construction: str = None,
        hnsw_m: int = None,
        manager_account: str = None,
        manager_account_password: str = None,
        metadata: str = None,
        metadata_indices: str = None,
        metrics: str = None,
        namespace: str = None,
        owner_id: int = None,
        parser: str = None,
        pq_enable: int = None,
        region_id: str = None,
        sparse_vector_index_config_shrink: str = None,
        support_sparse: bool = None,
        vector_index_config_shrink: str = None,
        workspace_id: str = None,
    ):
        # The vector index algorithm.
        # 
        # Valid values:
        # 
        # - `hnswflat`: (Default) An HNSW index without quantization compression.
        # 
        # - `novam`: A graph index without quantization compression. This algorithm is suitable for high-performance scenarios, such as real-time recommendations.
        # 
        # - `novad`: A partitioned index with `rabitq` quantization. This algorithm is suitable for large-scale, low-cost retrieval scenarios.
        self.algorithm = algorithm
        # The name of the collection to create.
        # 
        # > The name must comply with PostgreSQL object naming conventions.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The vector dimension.
        # 
        # > If you specify this parameter, a vector index is created. In subsequent calls to the [UpsertCollectionData](https://help.aliyun.com/document_detail/2401493.html) operation, the length of `Rows.Vector` must match this dimension. If you do not specify this parameter, you must call the [CreateVectorIndex](https://help.aliyun.com/document_detail/2401499.html) operation to create an index later.
        self.dimension = dimension
        # Specifies whether to use `mmap` to build the HNSW index. The default value is 0. We recommend setting this to 1 if your data does not require deletion and you need high-performance data ingestion.
        # 
        # Valid values:
        # 
        # - `0`: (Default) Builds the index by using segmented page storage. This mode can use the `shared_buffer` in PostgreSQL for caching and supports `DELETE` and `UPDATE` operations.
        # 
        # - `1`: Builds the index by using `mmap`. This mode does not support `DELETE` or `UPDATE` operations.
        # 
        # >Notice: 
        # 
        # The `ExternalStorage` parameter is available only for AnalyticDB for PostgreSQL v6.0 instances and is not supported in v7.0.
        self.external_storage = external_storage
        # The fields to use for full-text search. Use commas (`,`) to separate multiple field names. These fields must be keys defined in the `Metadata` parameter.
        self.full_text_retrieval_fields = full_text_retrieval_fields
        # The size of the candidate set for HNSW index construction. The value must be greater than or equal to `2 * HnswM`.
        # 
        # > Value range:
        # >
        # > - For AnalyticDB for PostgreSQL V6.0 instances: 40 to 4000.
        # >
        # > - For AnalyticDB for PostgreSQL V7.0 instances: 4 to 1000. The default value is 64.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors for the HNSW algorithm. You do not typically need to set this parameter, as the system automatically determines a value based on the vector dimension.
        # 
        # > Value range:
        # >
        # > - For AnalyticDB for PostgreSQL V6.0 instances: 1 to 1000.
        # >
        # > - For AnalyticDB for PostgreSQL V7.0 instances: 2 to 100. The default value is 16.
        # 
        # > We recommend that you set this parameter based on the vector dimension:
        # >
        # > - 16 for dimensions less than or equal to 384.
        # >
        # > - 32 for dimensions greater than 384 and less than or equal to 768.
        # >
        # > - 64 for dimensions greater than 768 and less than or equal to 1024.
        # >
        # > - 128 for dimensions greater than 1024.
        self.hnsw_m = hnsw_m
        # The name of the management account that has the `rds_superuser` privilege.
        # 
        # > You can call the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation to create an account.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the management account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # A JSON string that defines the metadata schema as a map. The keys are field names, and the values are their corresponding data types.
        # 
        # > Supported data types
        # >
        # > - For a list of supported data types, see [Data types](https://help.aliyun.com/document_detail/424383.html).
        # >
        # > - The `money` data type is not supported.
        # 
        # >Warning: 
        # 
        # The field names `id`, `vector`, `to_tsvector`, and `source` are reserved and cannot be used.
        # 
        # This parameter is required.
        self.metadata = metadata
        # The scalar index fields. Separate multiple fields with commas (`,`). The fields must be keys that are defined in `Metadata`.
        self.metadata_indices = metadata_indices
        # The distance metric used to build the vector index. Valid values:
        # 
        # - `l2`: Euclidean distance.
        # 
        # - `ip`: dot product.
        # 
        # - `cosine`: cosine similarity.
        self.metrics = metrics
        # The namespace.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace or the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to list existing namespaces.
        self.namespace = namespace
        self.owner_id = owner_id
        # The parser for full-text search. The default is `zh_cn`.
        self.parser = parser
        # Specifies whether to enable Product Quantization (PQ) for index acceleration. This is recommended for datasets with more than 500,000 entries. Valid values:
        # 
        # - `0`: Disabled.
        # 
        # - `1`: (Default) Enabled.
        self.pq_enable = pq_enable
        # The ID of the region where the instance is located.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The configuration for the sparse vector index. If specified, a sparse vector index is created.
        self.sparse_vector_index_config_shrink = sparse_vector_index_config_shrink
        # Specifies whether to enable support for sparse vectors. The default value is `false`.
        self.support_sparse = support_sparse
        # The configuration for the dense vector index.
        self.vector_index_config_shrink = vector_index_config_shrink
        # The ID of the workspace, which contains multiple database instances. You must specify either `WorkspaceId` or `DBInstanceId`. If both are specified, `WorkspaceId` takes precedence.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.external_storage is not None:
            result['ExternalStorage'] = self.external_storage

        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields

        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account

        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password

        if self.metadata is not None:
            result['Metadata'] = self.metadata

        if self.metadata_indices is not None:
            result['MetadataIndices'] = self.metadata_indices

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.parser is not None:
            result['Parser'] = self.parser

        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sparse_vector_index_config_shrink is not None:
            result['SparseVectorIndexConfig'] = self.sparse_vector_index_config_shrink

        if self.support_sparse is not None:
            result['SupportSparse'] = self.support_sparse

        if self.vector_index_config_shrink is not None:
            result['VectorIndexConfig'] = self.vector_index_config_shrink

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('ExternalStorage') is not None:
            self.external_storage = m.get('ExternalStorage')

        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')

        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')

        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')

        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        if m.get('MetadataIndices') is not None:
            self.metadata_indices = m.get('MetadataIndices')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Parser') is not None:
            self.parser = m.get('Parser')

        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SparseVectorIndexConfig') is not None:
            self.sparse_vector_index_config_shrink = m.get('SparseVectorIndexConfig')

        if m.get('SupportSparse') is not None:
            self.support_sparse = m.get('SupportSparse')

        if m.get('VectorIndexConfig') is not None:
            self.vector_index_config_shrink = m.get('VectorIndexConfig')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

