# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class CreateCollectionRequest(DaraModel):
    def __init__(
        self,
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
        sparse_vector_index_config: main_models.CreateCollectionRequestSparseVectorIndexConfig = None,
        support_sparse: bool = None,
        workspace_id: str = None,
    ):
        # The name of the collection that you want to create.
        # 
        # >  The name must comply with the naming conventions of PostgreSQL objects.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # >  You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the IDs of all AnalyticDB for PostgreSQL instances in a specific region.
        self.dbinstance_id = dbinstance_id
        # The number of vector dimensions.
        # 
        # >  If you specify this parameter, an index is created. When you call the [UpsertCollectionData](https://help.aliyun.com/document_detail/2401493.html) operation, make sure that the length of the Rows.Vector parameter is the same as the value of this parameter. If you do not specify this parameter, you can call the [CreateVectorIndex](https://help.aliyun.com/document_detail/2401499.html) operation to create an index.
        self.dimension = dimension
        # Specifies whether to use the memory mapping technology to create HNSW indexes. Valid values: 0 and 1. Default value: 0. We recommend that you set the value to 1 in scenarios that require upload speed but not data deletion.
        # 
        # > 
        # 
        # *   0: uses segmented paging storage to create indexes. This method uses the shared buffer of PostgreSQL for caching and supports the delete and update operations.
        # 
        # *   1: uses the memory mapping technology to create indexes. This method does not support the delete or update operation.
        self.external_storage = external_storage
        # The fields used for full-text search. Separate multiple fields with commas (,). These fields must be keys defined in Metadata.
        self.full_text_retrieval_fields = full_text_retrieval_fields
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors for the Hierarchical Navigable Small World (HNSW) algorithm. Valid values: 1 to 1000. In most cases, this parameter is automatically configured based on the value of the Dimension parameter. You do not need to configure this parameter.
        # 
        # >  We recommend that you configure this parameter based on the value of the Dimension parameter.
        # 
        # *If you set Dimension to a value less than or equal to 384, set the value of HnswM to 16.
        # 
        # *If you set Dimension to a value greater than 384 and less than or equal to 768, set the value of HnswM to 32.
        # 
        # *If you set Dimension to a value greater than 768 and less than or equal to 1024, set the value of HnswM to 64.
        # 
        # *If you set Dimension to a value greater than 1024, set the value of HnswM to 128.
        self.hnsw_m = hnsw_m
        # Name of the management account with rds_superuser permissions.
        # 
        # > You can create an account through the console -> Account Management, or by using the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) API.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the manager account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The metadata of the vector data, which is a JSON string in the MAP format. The key specifies the field name, and the value specifies the data type.
        # 
        # >  Supported data types:
        # 
        # *   For information about the supported data types, see [Data types](https://www.alibabacloud.com/help/zh/analyticdb/analyticdb-for-postgresql/developer-reference/data-types-1/).
        # 
        # *   The money data type is not supported.
        # 
        # **
        # 
        # **Warning** Reserved fields such as id, vector, to_tsvector, and source cannot be used.
        # 
        # This parameter is required.
        self.metadata = metadata
        # The scalar index fields. Separate multiple fields with commas (,). These fields must be keys defined in Metadata.
        self.metadata_indices = metadata_indices
        # The method that is used to create vector indexes. Valid values:
        # 
        # *   l2: Euclidean distance.
        # *   ip: inner product distance.
        # *   cosine: cosine similarity.
        self.metrics = metrics
        # The name of the namespace.
        # 
        # >  You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query a list of namespaces.
        self.namespace = namespace
        self.owner_id = owner_id
        # The analyzer that is used for full-text search.
        self.parser = parser
        # Specifies whether to enable the product quantization (PQ) feature for index acceleration. We recommend that you enable this feature for more than 500,000 rows of data. Valid values:
        # 
        # *   0: no.
        # *   1 (default): yes.
        self.pq_enable = pq_enable
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.sparse_vector_index_config = sparse_vector_index_config
        self.support_sparse = support_sparse
        # The ID of the workspace that consists of multiple AnalyticDB for PostgreSQL instances. You must specify one of the WorkspaceId and DBInstanceId parameters. If you specify both parameters, the WorkspaceId parameter takes effect.
        self.workspace_id = workspace_id

    def validate(self):
        if self.sparse_vector_index_config:
            self.sparse_vector_index_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.sparse_vector_index_config is not None:
            result['SparseVectorIndexConfig'] = self.sparse_vector_index_config.to_map()

        if self.support_sparse is not None:
            result['SupportSparse'] = self.support_sparse

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
            temp_model = main_models.CreateCollectionRequestSparseVectorIndexConfig()
            self.sparse_vector_index_config = temp_model.from_map(m.get('SparseVectorIndexConfig'))

        if m.get('SupportSparse') is not None:
            self.support_sparse = m.get('SupportSparse')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateCollectionRequestSparseVectorIndexConfig(DaraModel):
    def __init__(
        self,
        hnsw_ef_construction: int = None,
        hnsw_m: int = None,
    ):
        self.hnsw_ef_construction = hnsw_ef_construction
        self.hnsw_m = hnsw_m

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        return self

