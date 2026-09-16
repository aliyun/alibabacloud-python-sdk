# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLumaNamespaceRequest(DaraModel):
    def __init__(
        self,
        agent_name: str = None,
        catalog: str = None,
        name: str = None,
    ):
        # The name of the Agent.
        # 
        # This parameter is required.
        self.agent_name = agent_name
        # The name of the data catalog bound to the Agent. You can call ListLumaCatalogs to obtain this value.
        # 
        # This parameter is required.
        self.catalog = catalog
        # The name of the namespace bound to the Agent. You can call ListLumaNamespaces to obtain this value.
        # 
        # This parameter is required.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentName') is not None:
            self.agent_name = m.get('AgentName')

        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

