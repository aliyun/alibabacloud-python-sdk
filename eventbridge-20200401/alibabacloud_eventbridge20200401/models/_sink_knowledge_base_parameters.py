# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SinkKnowledgeBaseParameters(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        knowledge_base_name: str = None,
        namespace: str = None,
    ):
        # The data catalog to which the target knowledge base belongs. This parameter, together with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListCatalogs to obtain this value.
        self.catalog = catalog
        # The name of the target knowledge base, which is unique within the namespace. You can call ListKnowledgeBases to obtain this value.
        self.knowledge_base_name = knowledge_base_name
        # The namespace to which the target knowledge base belongs. The namespace must belong to the specified data catalog. You can call ListNamespaces to obtain this value.
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

