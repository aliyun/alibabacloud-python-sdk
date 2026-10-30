# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListKnowledgeBasesRequest(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        max_results: int = None,
        namespace: str = None,
        next_token: str = None,
    ):
        # The data catalog to which the knowledge base belongs. This parameter, along with Namespace and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListCatalogs to obtain this value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The maximum number of results to return per page. If this parameter is not specified or is set to 0, the default value 20 is used. The maximum value is 100.
        self.max_results = max_results
        # The namespace to which the knowledge base belongs. The namespace must belong to the specified data catalog. This parameter, along with Catalog and KnowledgeBaseName, uniquely identifies the knowledge base. You can call ListNamespaces to obtain this value.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The pagination token for the next page. You do not need to specify this parameter for the first query. For subsequent queries, use the NextToken value returned in the previous response. An empty value indicates that no more pages are available.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

