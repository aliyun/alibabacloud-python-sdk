# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDocumentCollectionShrinkRequest(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        collection: str = None,
        dbinstance_id: str = None,
        dimension: int = None,
        embedding_model: str = None,
        enable_graph: bool = None,
        entity_types_shrink: str = None,
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
        relationship_types_shrink: str = None,
        sparse_retrieval_fields: str = None,
        sparse_vector_index_config_shrink: str = None,
        support_sparse: bool = None,
        vector_index_config_shrink: str = None,
    ):
        # The vector index algorithm.
        # 
        # Valid values:
        # 
        # - `hnswflat`: An HNSW index without quantization compression. This is the default value.
        # 
        # - `novam`: A graph index without quantization compression. This algorithm is suitable for high-performance scenarios such as real-time recommendation.
        # 
        # - `novad`: A partitioned index with rabitq quantization. This algorithm is suitable for large-scale, low-cost retrieval scenarios.
        self.algorithm = algorithm
        # The name of the document collection to create.
        # 
        # > The name must comply with PostgreSQL object naming conventions.
        # 
        # This parameter is required.
        self.collection = collection
        # The ID of the instance.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in the target region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The vector dimension. If you omit this parameter, the system uses a default dimension for the selected `EmbeddingModel`.
        self.dimension = dimension
        # The embedding model. The default value is `text-embedding-v3`.
        # 
        # > Supported models:
        # >
        # > - `text-embedding-v3` (Recommended, Default): 1,024, 768, or 512 dimensions
        # >
        # > - `multimodal-embedding-v1` (Recommended): 1,024 dimensions, a multimodal embedding model
        # >
        # > - `text-embedding-v1`: 1,536 dimensions
        # >
        # > - `text-embedding-v2`: 1,536 dimensions
        # >
        # > - `text2vec` (Not recommended): 1,024 dimensions
        # >
        # > - `m3e-base` (Not recommended): 768 dimensions
        # >
        # > - `m3e-small` (Not recommended): 512 dimensions
        # >
        # > - `clip-vit-b-32` (Not recommended): CLIP ViT-B/32 model, 512 dimensions, an image embedding model
        # >
        # > - `clip-vit-b-16` (Not recommended): CLIP ViT-B/16 model, 512 dimensions, an image embedding model
        # >
        # > - `clip-vit-l-14` (Not recommended): CLIP ViT-L/14 model, 768 dimensions, an image embedding model
        # >
        # > - `clip-vit-l-14-336px` (Not recommended): CLIP ViT-L/14\\@336px model, 768 dimensions, an image embedding model
        # >
        # > - `clip-rn50` (Not recommended): CLIP RN50 model, 1,024 dimensions, an image embedding model
        # >
        # > - `clip-rn101` (Not recommended): CLIP RN101 model, 512 dimensions, an image embedding model
        # >
        # > - `clip-rn50x4` (Not recommended): CLIP RN50x4 model, 640 dimensions, an image embedding model
        # >
        # > - `clip-rn50x16` (Not recommended): CLIP RN50x16 model, 768 dimensions, an image embedding model
        # >
        # > - `clip-rn50x64` (Not recommended): CLIP RN50x64 model, 1,024 dimensions, an image embedding model
        self.embedding_model = embedding_model
        # Specifies whether to build a knowledge graph. The default value is `false`.
        # 
        # > To use this parameter, you must first upgrade your instance to a version that supports the graph engine. During the public preview period, submit a ticket to request an upgrade.
        self.enable_graph = enable_graph
        # A list of entity types.
        # 
        # > This parameter is required when `EnableGraph` is set to `true`.
        self.entity_types_shrink = entity_types_shrink
        # Specifies whether to use memory-mapped files (mmap) to build the HNSW index. The default value is 0. Setting this to `1` is recommended if you do not need to delete data and require high upload performance.
        # 
        # Valid values:
        # 
        # - `0`: Builds the index by using segmented page storage. This mode supports delete and update operations and can use the `shared_buffer` in PostgreSQL for caching. This is the default value.
        # 
        # - `1`: Builds the index by using mmap. This mode does not support delete or update operations.
        # 
        # >Notice: 
        # 
        # The `ExternalStorage` parameter is supported only by AnalyticDB for PostgreSQL V6.0 instances. It is not supported by V7.0 instances.
        self.external_storage = external_storage
        # The metadata fields to use for full-text search. These fields must be keys defined in `Metadata`. Separate multiple fields with a comma (,).
        self.full_text_retrieval_fields = full_text_retrieval_fields
        # The size of the candidate set (`ef_construction`) for HNSW index construction. The value must be greater than or equal to `2 * HnswM`.
        # 
        # > Value range:
        # >
        # > - For AnalyticDB for PostgreSQL V6.0 instances: 40 to 4,000.
        # >
        # > - For AnalyticDB for PostgreSQL V7.0 instances: 4 to 1,000. The default value is 64.
        self.hnsw_ef_construction = hnsw_ef_construction
        # The maximum number of neighbors (M) for the HNSW algorithm. You do not typically need to set this parameter, as the system automatically sets it based on the vector dimension.
        # 
        # > Value range:
        # >
        # > - For AnalyticDB for PostgreSQL V6.0 instances: 1 to 1,000.
        # >
        # > - For AnalyticDB for PostgreSQL V7.0 instances: 2 to 100. The default value is 16.
        # 
        # > We recommend that you set this parameter based on the vector dimension:
        # >
        # > - If the dimension is 384 or less: 16
        # >
        # > - If the dimension is greater than 384 and less than or equal to 768: 32
        # >
        # > - If the dimension is greater than 768 and less than or equal to 1,024: 64
        # >
        # > - If the dimension is greater than 1,024: 128
        self.hnsw_m = hnsw_m
        # The name of the LLM model. Valid values:
        # 
        # - `knowledge-extract-standard`: The default value.
        # 
        # - `knowledge-extract-mini`
        # 
        # > This parameter takes effect only when `EnableGraph` is set to `true`.
        self.llmmodel = llmmodel
        # The language used to build the knowledge graph. Valid values:
        # 
        # - `Simplified Chinese`: The default value.
        # 
        # - `English`
        # 
        # > This parameter takes effect only when `EnableGraph` is set to `true`.
        self.language = language
        # The name of the manager account that has `rds_superuser` permissions.
        # 
        # > You can create an account in the console on the \\*\\*Account Management\\*\\* page or by calling the [CreateAccount](https://help.aliyun.com/document_detail/2361789.html) operation.
        # 
        # This parameter is required.
        self.manager_account = manager_account
        # The password for the manager account.
        # 
        # This parameter is required.
        self.manager_account_password = manager_account_password
        # The metadata schema for the vector data, specified as a JSON map where keys are field names and values are data types.
        # 
        # > Supported data types
        # >
        # > - For a list of supported data types, see [Data types](https://help.aliyun.com/document_detail/424383.html).
        # >
        # > - The `money` data type is not supported.
        # 
        # >Warning: 
        # 
        # The following fields are reserved and cannot be used: `id`, `vector`, `doc_name`, `content`, `loader_metadata`, `source`, and `to_tsvector`.
        self.metadata = metadata
        # The metadata fields on which to create scalar indexes. These fields must be keys defined in `Metadata`. Separate multiple fields with a comma (,).
        self.metadata_indices = metadata_indices
        # The distance metric for the vector index.
        # 
        # Valid values:
        # 
        # - **`l2`**: Euclidean distance.
        # 
        # - **`ip`**: dot product (inner product) distance.
        # 
        # - **`cosine`** (Default): cosine similarity.
        self.metrics = metrics
        # The namespace. The default value is `public`.
        # 
        # > You can call the [CreateNamespace](https://help.aliyun.com/document_detail/2401495.html) operation to create a namespace and the [ListNamespaces](https://help.aliyun.com/document_detail/2401502.html) operation to list namespaces.
        self.namespace = namespace
        self.owner_id = owner_id
        # The tokenizer for full-text search. The default value is `zh_cn`.
        self.parser = parser
        # Specifies whether to enable the PQ (product quantization) algorithm to accelerate indexing. This is recommended for datasets with over 500,000 entries. Valid values:
        # 
        # - `0`: Disables the feature.
        # 
        # - `1`: Enables the feature. This is the default value.
        self.pq_enable = pq_enable
        # The region ID of the instance.
        # 
        # This parameter is required.
        self.region_id = region_id
        # A list of relationship types.
        # 
        # > This parameter is required when `EnableGraph` is set to `true`.
        self.relationship_types_shrink = relationship_types_shrink
        # The metadata fields used to build the sparse vector. These fields must be keys defined in `Metadata`. Separate multiple fields with a comma (,).
        self.sparse_retrieval_fields = sparse_retrieval_fields
        # Configuration for the sparse vector index. Specifying this parameter creates the index.
        self.sparse_vector_index_config_shrink = sparse_vector_index_config_shrink
        # Specifies whether to support sparse vectors. The default value is `false`.
        self.support_sparse = support_sparse
        # Configuration for the dense vector index.
        self.vector_index_config_shrink = vector_index_config_shrink

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

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.enable_graph is not None:
            result['EnableGraph'] = self.enable_graph

        if self.entity_types_shrink is not None:
            result['EntityTypes'] = self.entity_types_shrink

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

        if self.relationship_types_shrink is not None:
            result['RelationshipTypes'] = self.relationship_types_shrink

        if self.sparse_retrieval_fields is not None:
            result['SparseRetrievalFields'] = self.sparse_retrieval_fields

        if self.sparse_vector_index_config_shrink is not None:
            result['SparseVectorIndexConfig'] = self.sparse_vector_index_config_shrink

        if self.support_sparse is not None:
            result['SupportSparse'] = self.support_sparse

        if self.vector_index_config_shrink is not None:
            result['VectorIndexConfig'] = self.vector_index_config_shrink

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
            self.entity_types_shrink = m.get('EntityTypes')

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
            self.relationship_types_shrink = m.get('RelationshipTypes')

        if m.get('SparseRetrievalFields') is not None:
            self.sparse_retrieval_fields = m.get('SparseRetrievalFields')

        if m.get('SparseVectorIndexConfig') is not None:
            self.sparse_vector_index_config_shrink = m.get('SparseVectorIndexConfig')

        if m.get('SupportSparse') is not None:
            self.support_sparse = m.get('SupportSparse')

        if m.get('VectorIndexConfig') is not None:
            self.vector_index_config_shrink = m.get('VectorIndexConfig')

        return self

