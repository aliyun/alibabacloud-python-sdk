# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDocumentDownloadUrlRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        document_id: str = None,
        knowledge_base_name: str = None,
        namespace: str = None,
        network_type: str = None,
    ):
        # The data catalog to which the knowledge base belongs. This parameter, together with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListCatalogs to obtain the value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The ID of the document.
        # 
        # This parameter is required.
        self.document_id = document_id
        # The name of the knowledge base. The name must be unique within the namespace. It is specified upon creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. This parameter, together with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListNamespaces to obtain the value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The network type of the presigned URL. Valid values:
        # - PUBLIC: Accessible over the Internet. This is the default value.
        # - INTERNAL: Accessible only over the internal network within the same Alibaba Cloud region. No Internet traffic fees are incurred.
        self.network_type = network_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.document_id is not None:
            result['DocumentId'] = self.document_id

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('DocumentId') is not None:
            self.document_id = m.get('DocumentId')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        return self

