# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateKnowledgeBaseShrinkRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        chunk_configuration_shrink: str = None,
        description: str = None,
        knowledge_base_name: str = None,
        namespace: str = None,
        search_configuration_shrink: str = None,
    ):
        # The data catalog to which the knowledge base belongs. It is used together with Namespace and KnowledgeBaseName to locate the knowledge base. You can call ListCatalogs to obtain the value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. Updates the default chunking strategy of the knowledge base. This update takes effect only for newly uploaded documents and does not re-chunk existing documents. If this parameter is not specified, the strategy is not modified.
        self.chunk_configuration_shrink = chunk_configuration_shrink
        # Updates the description of the knowledge base. If this parameter is not specified, the description is not modified.
        self.description = description
        # The name of the knowledge base. The name must be unique within the namespace. It is specified during creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. It is used together with Catalog and KnowledgeBaseName to locate the knowledge base. You can call ListNamespaces to obtain the value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # Optional. Updates the default search configuration at the knowledge base level. The update takes effect immediately for subsequent search requests. If this parameter is not specified, the configuration is not modified.
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

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

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

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('SearchConfiguration') is not None:
            self.search_configuration_shrink = m.get('SearchConfiguration')

        return self

