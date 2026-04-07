# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDagTestRequest(DaraModel):
    def __init__(
        self,
        bizdate: str = None,
        name: str = None,
        node_id: int = None,
        node_params: str = None,
        project_env: str = None,
    ):
        # This parameter is required.
        self.bizdate = bizdate
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.node_id = node_id
        self.node_params = node_params
        # This parameter is required.
        self.project_env = project_env

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.name is not None:
            result['Name'] = self.name

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_params is not None:
            result['NodeParams'] = self.node_params

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeParams') is not None:
            self.node_params = m.get('NodeParams')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        return self

