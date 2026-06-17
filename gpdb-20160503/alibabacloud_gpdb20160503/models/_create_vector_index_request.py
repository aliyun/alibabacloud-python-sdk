# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateVectorIndexRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        external_storage: int = None,
        hnsw_ef_construction: int = None,
        hnsw_m: int = None,
        manager_account: str = None,
        manager_account_password: str = None,
        metrics: str = None,
        namespace: str = None,
        nlist: int = None,
        owner_id: int = None,
        pq_enable: int = None,
        rabitq_bits: int = None,
        region_id: str = None,
        type: str = None,
    ):
        # The vector indexing algorithm.
        # 
        # Valid values:
        # 
        # - `hnswflat`: (Default) An HNSW index that does not use quantization compression.
        # 
        # - `novam`: A graph-based index that does not use quantization compression. This algorithm is suitable for high-performance scenarios, such as real-time recommendations.
        # 
        # - `novad`: A partitioned index that uses rabitq quantization. This algorithm is suitable for large-scale, cost-effective retrieval scenarios.
        self.algorithm = algorithm
        # The collection name.
        # 
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to list all collections.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to view the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The vector dimension.
        # 
        # > - This parameter is required for dense vectors.
        # >
        # > - This value must match the length of the `Rows.Vector` data provided when calling the [UpsertCollectionData](https://help.aliyun.com/document_detail/2401493.html) operation.
        self.dimension = dimension
        # Specifies whether to use `mmap` to build the HNSW index. The default value is 0. Set this to 1 for high-performance data uploads in scenarios where data deletion is not required.
        # 
        # Valid values:
        # 
        # - `0`: (Default) Builds the index by using segmented page storage. This mode uses the `shared_buffer` in PostgreSQL for caching and supports delete and update operations.
        # 
        # - `1`: Builds the index by using `mmap`. This mode does not support delete and update operations.
        # 
        # >Notice: 
        # 
        # The `ExternalStorage` parameter is supported only by AnalyticDB for PostgreSQL V6.0.
        self.external_storage = external_storage
        # The size of the candidate set for the HNSW algorithm during index construction. The value must be in the range of 4 to 1,000. The default value is 64.
        # 
        # > This parameter applies only to AnalyticDB for PostgreSQL V7.0 instances, and its value must be greater than or equal to `2 * HnswM`.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors for the Hierarchical Navigable Small World (HNSW) algorithm. The system automatically sets this value based on the vector dimension. You do not typically need to configure this parameter manually.
        # 
        # > Valid values:
        # >
        # > - For AnalyticDB for PostgreSQL V6.0 instances: 1 to 1,000.
        # >
        # > - For AnalyticDB for PostgreSQL V7.0 instances: 2 to 100. The default value is 16.
        # 
        # > We recommend the following values based on the vector dimension:
        # >
        # > - For dimensions of 384 or less: 16
        # >
        # > - For dimensions from 385 to 768: 32
        # >
        # > - For dimensions from 769 to 1,024: 64
        # >
        # > - For dimensions greater than 1,024: 128
        self.hnsw_m = hnsw_m
        # The name of the management account that has `rds_superuser` permissions.
        # 
        # > You can create an account on the \\*\\*account management\\*\\* page in the console or by calling the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the management account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The distance metric used to build the vector index. Valid values:
        # 
        # - `l2`: euclidean distance
        # 
        # - `ip`: dot product (inner product)
        # 
        # - `cosine`: cosine similarity
        # 
        # > Sparse vectors support only `ip`.
        self.metrics = metrics
        # The namespace. The default value is `public`.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to list all namespaces.
        self.namespace = namespace
        # The number of lists (partitions) for the Novad algorithm. The value must be in the range of 2 to 1,073,741,824. The default value is 256.
        self.nlist = nlist
        self.owner_id = owner_id
        # Specifies whether to enable Product Quantization (PQ) to accelerate indexing. Recommended for collections with over 500,000 vectors. Valid values:
        # 
        # - `0`: Disabled.
        # 
        # - `1`: Enabled. (Default)
        self.pq_enable = pq_enable
        # The number of bits for rabitq compression. The valid range is 1 to 8. The default value is 3.
        self.rabitq_bits = rabitq_bits
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The vector type. Valid values:
        # 
        # - `Dense`: (Default) a dense vector
        # 
        # - `Sparse`: a sparse vector
        self.type = type

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

        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        if self.manager_account is not None:
            result['ManagerAccount'] = self.manager_account

        if self.manager_account_password is not None:
            result['ManagerAccountPassword'] = self.manager_account_password

        if self.metrics is not None:
            result['Metrics'] = self.metrics

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.nlist is not None:
            result['Nlist'] = self.nlist

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pq_enable is not None:
            result['PqEnable'] = self.pq_enable

        if self.rabitq_bits is not None:
            result['RabitqBits'] = self.rabitq_bits

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        if m.get('ManagerAccount') is not None:
            self.manager_account = m.get('ManagerAccount')

        if m.get('ManagerAccountPassword') is not None:
            self.manager_account_password = m.get('ManagerAccountPassword')

        if m.get('Metrics') is not None:
            self.metrics = m.get('Metrics')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Nlist') is not None:
            self.nlist = m.get('Nlist')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PqEnable') is not None:
            self.pq_enable = m.get('PqEnable')

        if m.get('RabitqBits') is not None:
            self.rabitq_bits = m.get('RabitqBits')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

