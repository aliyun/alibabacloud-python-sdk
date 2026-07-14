# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class CreateDocumentCollectionRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        embedding_model: str = None,
        enable_graph: bool = None,
        entity_types: List[str] = None,
        external_storage: int = None,
        full_text_retrieval_fields: str = None,
        hnsw_ef_construction: str = None,
        hnsw_m: int = None,
        llmmodel: str = None,
        language: str = None,
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
        relationship_types: List[str] = None,
        sparse_retrieval_fields: str = None,
        sparse_vector_index_config: main_models.CreateDocumentCollectionRequestSparseVectorIndexConfig = None,
        support_sparse: bool = None,
        vector_index_config: main_models.CreateDocumentCollectionRequestVectorIndexConfig = None,
    ):
        # The vector index algorithm.
        # 
        # Valid values:
        # - hnswflat: HNSW index without quantization compression (default).
        # - novam: graph index without quantization compression, suitable for high-performance scenarios such as real-time recommendations.
        # - novad: partitioned index with RaBitQ quantization, suitable for large-scale low-cost retrieval scenarios.
        self.algorithm = algorithm
        # The name of the knowledge base to create.
        # 
        # > The name must comply with PostgreSQL object naming conventions.
        # 
        # This parameter is required.
        self.collection = collection
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The vector dimensions. The default value is the dimension supported by the embedding model.
        self.dimension = dimension
        # The embedding model. Default value: text-embedding-v3.
        # 
        # > Supported models:
        # > - text-embedding-v3 (recommended, default): 1024, 768, or 512 dimensions
        # > - multimodal-embedding-v1 (recommended): 1024 dimensions, multimodal embedding model
        # > - text-embedding-v1: 1536 dimensions
        # > - text-embedding-v2: 1536 dimensions
        # > - text2vec (not recommended): 1024 dimensions
        # > - m3e-base (not recommended): 768 dimensions
        # > - m3e-small (not recommended): 512 dimensions
        # > - clip-vit-b-32 (not recommended): CLIP ViT-B/32 model, 512 dimensions, image embedding model
        # > - clip-vit-b-16 (not recommended): CLIP ViT-B/16 model, 512 dimensions, image embedding model
        # > - clip-vit-l-14 (not recommended): CLIP ViT-L/14 model, 768 dimensions, image embedding model
        # > - clip-vit-l-14-336px (not recommended): CLIP ViT-L/14@336px model, 768 dimensions, image embedding model
        # > - clip-rn50 (not recommended): CLIP RN50 model, 1024 dimensions, image embedding model
        # > - clip-rn101 (not recommended): CLIP RN101 model, 512 dimensions, image embedding model
        # > - clip-rn50x4 (not recommended): CLIP RN50x4 model, 640 dimensions, image embedding model
        # > - clip-rn50x16 (not recommended): CLIP RN50x16 model, 768 dimensions, image embedding model
        # > - clip-rn50x64 (not recommended): CLIP RN50x64 model, 1024 dimensions, image embedding model
        self.embedding_model = embedding_model
        # Specifies whether to enable knowledge graph construction. Default value: false.
        # 
        # > Before using this parameter, upgrade the instance to a version that supports the graph engine. (During the public preview, submit a ticket to upgrade the version.)
        self.enable_graph = enable_graph
        # The list of entity types.
        # 
        # > This parameter is required when knowledge graph construction is enabled.
        self.entity_types = entity_types
        # Specifies whether to use mmap to build the HNSW index. Default value: 0. If data does not need to be deleted and you require high upload performance, set this parameter to 1.
        # 
        # Valid values:
        # - 0: uses segment-page storage to build the index. This mode uses shared_buffer in PostgreSQL as cache and supports delete and update operations.
        # - 1: uses mmap to build the index. This mode does not support delete or update operations.
        # 
        # >Notice: Only version 6.0 supports the ExternalStorage parameter. Version 7.0 does not support this parameter.
        self.external_storage = external_storage
        # The fields used for full-text retrieval. Separate multiple fields with commas (,). The fields must be keys defined in Metadata.
        self.full_text_retrieval_fields = full_text_retrieval_fields
        # The candidate set size when building an index with the HNSW algorithm. The value must be >= 2*HNSW_M.
        # 
        # > Valid values:
        # >- AnalyticDB for PostgreSQL 6.0 instances: 40 to 4000.
        # >- AnalyticDB for PostgreSQL 7.0 instances: 4 to 1000. Default value: 64.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors in the HNSW algorithm. This value is automatically set based on the vector dimensions. Manual configuration is generally not required.
        # 
        # > Valid values:
        # >- AnalyticDB for PostgreSQL 6.0 instances: 1 to 1000.
        # >- AnalyticDB for PostgreSQL 7.0 instances: 2 to 100. Default value: 16.
        # 
        # > Recommended values based on vector dimensions:
        # >- 384 or fewer: 16
        # >- Greater than 384 and up to 768: 32
        # >- Greater than 768 and up to 1024: 64
        # >- Greater than 1024: 128
        self.hnsw_m = hnsw_m
        # The LLM model name. Valid values:
        # - knowledge-extract-standard: default value.
        # - knowledge-extract-mini
        # > This parameter takes effect only when knowledge graph construction is enabled.
        self.llmmodel = llmmodel
        # The language used for knowledge graph construction. Valid values:
        # - Simplified Chinese: Simplified Chinese. Default value.
        # - English: English.
        # > This parameter takes effect only when knowledge graph construction is enabled.
        self.language = language
        # The name of the management account that has the rds_superuser permission.
        # 
        # > You can create an account in the console by navigating to Account Management, or by calling the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password of the management account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The metadata of vector data, in the format of a JSON string representing a MAP. The key represents the field name, and the value represents the data type.
        # 
        # > Supported data types:
        # > - For the list of data types, see [Data types](https://help.aliyun.com/document_detail/424383.html).
        # > - The money type is not supported.
        # 
        # >Warning: The following fields are reserved and cannot be used: id, vector, doc_name, content, loader_metadata, source, and to_tsvector.
        self.metadata = metadata
        # The scalar index fields. Separate multiple fields with commas (,). The fields must be keys defined in Metadata.
        self.metadata_indices = metadata_indices
        # The distance metric used for building vector indexes.
        # 
        # Valid values:
        # - **l2**: Euclidean distance.
        # - **ip**: inner product distance.
        # - **cosine** (default): cosine similarity.
        self.metrics = metrics
        # The namespace. Default value: public.
        # 
        # > You can create a namespace by calling the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation and query the list of namespaces by calling the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation.
        self.namespace = namespace
        self.owner_id = owner_id
        # The tokenizer used for full-text retrieval. Default value: zh_cn.
        self.parser = parser
        # Specifies whether to enable Product Quantization (PQ) algorithm acceleration for the index. We recommend enabling this feature when the data volume exceeds 500,000. Valid values:
        # - 0: disabled.
        # - 1: enabled (default).
        self.pq_enable = pq_enable
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of relationship edge types.
        # 
        # > This parameter is required when knowledge graph construction is enabled.
        self.relationship_types = relationship_types
        # The metadata fields used for building sparse vectors. Separate multiple fields with commas (,). The fields must be keys defined in Metadata.
        self.sparse_retrieval_fields = sparse_retrieval_fields
        # The sparse vector index configuration. If specified, a sparse vector index is created.
        self.sparse_vector_index_config = sparse_vector_index_config
        # Specifies whether to support sparse vectors. Default value: false.
        self.support_sparse = support_sparse
        # The dense vector index configuration.
        self.vector_index_config = vector_index_config

    def validate(self):
        if self.sparse_vector_index_config:
            self.sparse_vector_index_config.validate()
        if self.vector_index_config:
            self.vector_index_config.validate()

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

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.enable_graph is not None:
            result['EnableGraph'] = self.enable_graph

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.external_storage is not None:
            result['ExternalStorage'] = self.external_storage

        if self.full_text_retrieval_fields is not None:
            result['FullTextRetrievalFields'] = self.full_text_retrieval_fields

        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        if self.llmmodel is not None:
            result['LLMModel'] = self.llmmodel

        if self.language is not None:
            result['Language'] = self.language

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

        if self.relationship_types is not None:
            result['RelationshipTypes'] = self.relationship_types

        if self.sparse_retrieval_fields is not None:
            result['SparseRetrievalFields'] = self.sparse_retrieval_fields

        if self.sparse_vector_index_config is not None:
            result['SparseVectorIndexConfig'] = self.sparse_vector_index_config.to_map()

        if self.support_sparse is not None:
            result['SupportSparse'] = self.support_sparse

        if self.vector_index_config is not None:
            result['VectorIndexConfig'] = self.vector_index_config.to_map()

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

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('EnableGraph') is not None:
            self.enable_graph = m.get('EnableGraph')

        if m.get('EntityTypes') is not None:
            self.entity_types = m.get('EntityTypes')

        if m.get('ExternalStorage') is not None:
            self.external_storage = m.get('ExternalStorage')

        if m.get('FullTextRetrievalFields') is not None:
            self.full_text_retrieval_fields = m.get('FullTextRetrievalFields')

        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        if m.get('LLMModel') is not None:
            self.llmmodel = m.get('LLMModel')

        if m.get('Language') is not None:
            self.language = m.get('Language')

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

        if m.get('RelationshipTypes') is not None:
            self.relationship_types = m.get('RelationshipTypes')

        if m.get('SparseRetrievalFields') is not None:
            self.sparse_retrieval_fields = m.get('SparseRetrievalFields')

        if m.get('SparseVectorIndexConfig') is not None:
            temp_model = main_models.CreateDocumentCollectionRequestSparseVectorIndexConfig()
            self.sparse_vector_index_config = temp_model.from_map(m.get('SparseVectorIndexConfig'))

        if m.get('SupportSparse') is not None:
            self.support_sparse = m.get('SupportSparse')

        if m.get('VectorIndexConfig') is not None:
            temp_model = main_models.CreateDocumentCollectionRequestVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class CreateDocumentCollectionRequestVectorIndexConfig(DaraModel):
    def __init__(
        self,
        nlist: int = None,
        rabitq_bits: int = None,
    ):
        # The Novad list count (number of partitions). Valid values: 2 to 1073741824. Default value: 256.
        self.nlist = nlist
        # The number of RaBitQ compression bits. Valid values: 1 to 8. Default value: 3.
        self.rabitq_bits = rabitq_bits

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nlist is not None:
            result['Nlist'] = self.nlist

        if self.rabitq_bits is not None:
            result['RabitqBits'] = self.rabitq_bits

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nlist') is not None:
            self.nlist = m.get('Nlist')

        if m.get('RabitqBits') is not None:
            self.rabitq_bits = m.get('RabitqBits')

        return self

class CreateDocumentCollectionRequestSparseVectorIndexConfig(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        hnsw_ef_construction: int = None,
        hnsw_m: int = None,
    ):
        # The vector index algorithm.
        # 
        # Valid values:
        # - hnswflat: HNSW index without quantization compression (default).
        # - novam: graph index without quantization compression, suitable for high-performance scenarios such as real-time recommendations.
        self.algorithm = algorithm
        # The candidate set size when building an index with the HNSW algorithm. Valid values: 4 to 1000. Default value: 64.
        # 
        # > This parameter is required only for AnalyticDB for PostgreSQL 7.0 instances, and the value must be >= 2*HNSW_M.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors in the HNSW algorithm. This value is automatically set based on the vector dimensions. Manual configuration is generally not required.
        # 
        # > Valid values:
        # >- AnalyticDB for PostgreSQL 6.0 instances: 1 to 1000.
        # >- AnalyticDB for PostgreSQL 7.0 instances: 2 to 100. Default value: 16.
        # 
        # > Recommended values based on vector dimensions:
        # >- 384 or fewer: 16
        # >- Greater than 384 and up to 768: 32
        # >- Greater than 768 and up to 1024: 64
        # >- Greater than 1024: 128
        self.hnsw_m = hnsw_m

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['Algorithm'] = self.algorithm

        if self.hnsw_ef_construction is not None:
            result['HnswEfConstruction'] = self.hnsw_ef_construction

        if self.hnsw_m is not None:
            result['HnswM'] = self.hnsw_m

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Algorithm') is not None:
            self.algorithm = m.get('Algorithm')

        if m.get('HnswEfConstruction') is not None:
            self.hnsw_ef_construction = m.get('HnswEfConstruction')

        if m.get('HnswM') is not None:
            self.hnsw_m = m.get('HnswM')

        return self

