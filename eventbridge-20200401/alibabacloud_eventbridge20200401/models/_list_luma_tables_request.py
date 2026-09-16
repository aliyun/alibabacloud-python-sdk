# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLumaTablesRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        limit: int = None,
        namespace: str = None,
        next_token: str = None,
    ):
        # The name of the agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the agent. You can call ListLumaCatalogs to obtain the catalog name.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The maximum number of entries to return per page. Valid values: 1 to 100. Default value: 100. Each entry requires a back-to-origin metadata query, so this value also limits the number of back-to-origin queries per call.
        self.limit = limit
        # The name of the namespace bound to the agent. You can call ListLumaNamespaces to obtain the namespace name.
        # 
        # This parameter is required.
        self.namespace = namespace
        # The starting token for a paging query. Leave this parameter empty or set it to "0" for the first query. For subsequent pages, use the NextToken value returned in the previous response.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_name is not None:
            result['AgentName'] = self.agent_name

        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self

