# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLumaTableRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        name: str = None,
        namespace: str = None,
    ):
        # The name of the Agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the Agent. You can call ListLumaCatalogs to obtain the catalog name.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The name of the event table bound to the Agent. You can call ListLumaTables to obtain the event table name.
        # 
        # This parameter is required.
        self.name = name
        # The name of the namespace bound to the Agent. You can call ListLumaNamespaces to obtain the namespace name.
        # 
        # This parameter is required.
        self.namespace = namespace

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

        if self.name is not None:
            result['Name'] = self.name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        return self

