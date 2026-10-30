# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDocumentsRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        file_name_prefix: str = None,
        knowledge_base_name: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
        status: str = None,
    ):
        # The data catalog to which the knowledge base belongs. This parameter, along with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListCatalogs to obtain the value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Optional. Filters documents by file name prefix. The prefix matching semantics are the same as those of the NamePrefix parameter in ListEventStreamings. If this parameter is not specified or is left empty, no filtering is applied. The maximum length is 255 characters.
        self.file_name_prefix = file_name_prefix
        # The name of the knowledge base. The name must be unique within the namespace. It is specified upon creation and cannot be modified.
        # 
        # This parameter is required.
        self.knowledge_base_name = knowledge_base_name
        # The maximum number of results to return per page. If this parameter is not specified or is set to 0, the default value 20 is used. The maximum value is 100.
        self.max_results = max_results
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. This parameter, along with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListNamespaces to obtain the value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The token for the next page. You do not need to specify this parameter for the first query. For subsequent queries, use the NextToken value returned in the previous response. An empty value indicates that no more pages are available.
        self.next_token = next_token
        # Optional. Filters documents by exact document status. Valid values:
        # - UPLOADING: The document is being uploaded.
        # - PENDING: The document is pending processing.
        # - PROCESSING: The document is being processed.
        # - COMPLETED: The document processing is completed.
        # - FAILED: The document processing failed.
        # - DELETING: The document is being deleted.
        # If this parameter is not specified, no filtering is applied.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.file_name_prefix is not None:
            result['FileNamePrefix'] = self.file_name_prefix

        if self.knowledge_base_name is not None:
            result['KnowledgeBaseName'] = self.knowledge_base_name

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('FileNamePrefix') is not None:
            self.file_name_prefix = m.get('FileNamePrefix')

        if m.get('KnowledgeBaseName') is not None:
            self.knowledge_base_name = m.get('KnowledgeBaseName')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

