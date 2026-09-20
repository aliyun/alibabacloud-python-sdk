# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetNodeChildrenRequest(DaraModel):
    def __init__(
        self,
        node_id: int = None,
        project_env: str = None,
    ):
        # The node ID. You can view the node ID in the Operation Center of the DataWorks console.
        # 
        # This parameter is required.
        self.node_id = node_id
        # The environment identifier of the Operation Center. PROD indicates the production environment. DEV indicates the development environment.
        # 
        # This parameter is required.
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

