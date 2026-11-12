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
        # The vector index algorithm. Valid values:
        # - hnswflat: HNSW index without quantization compression (default).
        # - novam: graph index without quantization compression, suitable for high-performance scenarios such as real-time recommendation.
        # - novad: partitioned index with RaBitQ quantization, suitable for large-scale, low-cost retrieval scenarios.
        self.algorithm = algorithm
        # The collection name.
        # > You can call the [ListCollections](https://help.aliyun.com/document_detail/2401503.html) operation to query the list.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The vector dimensions.
        # 
        # > - This parameter is required for dense vectors.
        # > - The value must be the same as the length of the vector data Rows.Vector in the [UpsertCollectionData](https://help.aliyun.com/document_detail/2401493.html) operation.
        self.dimension = dimension
        # Specifies whether to use mmap to build the HNSW index. Default value: 0. If data does not need to be deleted and you have high requirements for data upload speed, we recommend that you set this parameter to 1.
        # 
        # Valid values:
        # - 0: uses the default segment-page storage to build the index. In this mode, shared_buffer in PostgreSQL can be used for caching, and operations such as deletion and update are supported.
        # - 1: uses mmap to build the index. This mode does not support operations such as deletion and update.
        # 
        # >Notice: The ExternalStorage parameter is supported only in V6.0. It is not supported in V7.0.</notice>
        self.external_storage = external_storage
        # The size of the candidate set when the HNSW algorithm builds the index. Valid values: 4 to 1000. Default value: 64.
        # 
        # > This parameter is required only for AnalyticDB for PostgreSQL V7.0 instances, and the value must be greater than or equal to 2 × HNSW_M.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors in the HNSW algorithm. The operation automatically sets this value based on the vector dimensions. You do not need to manually set this value in most cases.
        # 
        # > Valid values:
        # >- AnalyticDB for PostgreSQL V6.0 instances: 1 to 1000.
        # >- AnalyticDB for PostgreSQL V7.0 instances: 2 to 100. Default value: 16.
        # 
        # > Recommended settings based on vector dimensions:
        # > - 384 or less: 16
        # > - Greater than 384 and less than or equal to 768: 32
        # > - Greater than 768 and less than or equal to 1024: 64
        # > - Greater than 1024: 128
        self.hnsw_m = hnsw_m
        # The name of the management account that has the rds_superuser permission.
        # 
        # > You can create an account in the console by navigating to Account Management, or call the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the management account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The distance metric used to build the vector index. Valid values:
        # - l2: Euclidean distance.
        # - ip: inner product.
        # - cosine: cosine similarity.
        # 
        # > Only ip is supported for sparse vectors.
        self.metrics = metrics
        # The namespace. Default value: public.
        # 
        # > You can call the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to query the list.
        self.namespace = namespace
        # The number of lists (partitions) for Novad. Valid values: 2 to 1073741824. Default value: 256.
        self.nlist = nlist
        self.owner_id = owner_id
        # Specifies whether to enable product quantization (PQ) algorithm acceleration for the index. We recommend that you enable this feature when the data volume exceeds 500,000. Valid values:
        # - 0: disabled.
        # - 1: enabled (default).
        self.pq_enable = pq_enable
        # The number of bits for RaBitQ compression. Valid values: 1 to 8. Default value: 3.
        self.rabitq_bits = rabitq_bits
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The vector type. Valid values:
        # - Dense: dense vector (default).
        # - Sparse: sparse vector.
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

