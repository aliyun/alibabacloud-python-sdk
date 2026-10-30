# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateKnowledgeBaseShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        chunk_configuration_shrink: str = None,
        description: str = None,
        embedding_dimension: int = None,
        embedding_model: str = None,
        knowledge_base_name: str = None,
        metadata_schema_shrink: str = None,
        namespace: str = None,
        search_configuration_shrink: str = None,
    ):
        # The EventHouse catalog to which the knowledge base belongs. This parameter, together with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. This parameter cannot be modified after the knowledge base is created. You cannot bind a system catalog.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. The default chunking strategy for the knowledge base. This strategy applies only to documents uploaded after the configuration. If this parameter is not specified, the system default chunking strategy is used.
        self.chunk_configuration_shrink = chunk_configuration_shrink
        # The description of the knowledge base.
        self.description = description
        # Optional. The vector dimensions. This parameter is attached to the embedding model for validation. Valid values for text-embedding-v3: 64, 128, 256, 512, 768, and 1024. Valid values for text-embedding-v4: 64, 128, 256, 512, 768, 1024, 1536, and 2048. Valid values for qwen3.7-text-embedding: 256, 512, 768, 1024, 1536, 2048, and 2560. Valid values for qwen3.7-text-embedding-flash: 256, 512, 768, and 1024. If this parameter is not specified, the default dimension of the model, 1024, is used. This parameter cannot be modified after the knowledge base is created. To change the model, you must rebuild the knowledge base, even if the dimensions remain the same.
        self.embedding_dimension = embedding_dimension
        # Optional. The embedding model. This parameter cannot be modified after the knowledge base is created. Valid values: text-embedding-v3, text-embedding-v4, qwen3.7-text-embedding, and qwen3.7-text-embedding-flash. Only Qwen models provided by Model Studio are supported. Third-party models are not supported. Default value: text-embedding-v4.
        self.embedding_model = embedding_model
        # The name of the knowledge base. The name must be unique within the same namespace.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # Declares the metadata fields for the knowledge base. When you upload documents, the metadata can only contain the fields declared here. This parameter cannot be modified after the knowledge base is created.
        self.metadata_schema_shrink = metadata_schema_shrink
        # The EventHouse namespace to which the knowledge base belongs. The namespace must belong to the specified catalog. This parameter, together with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. This parameter cannot be modified after the knowledge base is created.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Optional. The default search configuration at the knowledge base level. This configuration takes effect when the corresponding parameters are not specified in a search request. You can modify this configuration by calling UpdateKnowledgeBase after the knowledge base is created.
        self.search_configuration_shrink = search_configuration_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.chunk_configuration_shrink is not None:
            result['ChunkConfiguration'] = self.chunk_configuration_shrink

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_dimension is not None:
            result['EmbeddingDimension'] = self.embedding_dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.metadata_schema_shrink is not None:
            result['MetadataSchema'] = self.metadata_schema_shrink

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.search_configuration_shrink is not None:
            result['SearchConfiguration'] = self.search_configuration_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('ChunkConfiguration') is not None:
            self.chunk_configuration_shrink = m.get('ChunkConfiguration')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingDimension') is not None:
            self.embedding_dimension = m.get('EmbeddingDimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MetadataSchema') is not None:
            self.metadata_schema_shrink = m.get('MetadataSchema')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchConfiguration') is not None:
            self.search_configuration_shrink = m.get('SearchConfiguration')

        return self

