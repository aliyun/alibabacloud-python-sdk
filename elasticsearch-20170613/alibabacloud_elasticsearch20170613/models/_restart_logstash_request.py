# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RestartLogstashRequest(DaraModel):
    def __init__(
        self,
        batch_count: float = None,
        blue_green_dep: bool = None,
        node_types: List[str] = None,
        nodes: List[str] = None,
        restart_type: str = None,
        client_token: str = None,
        force: bool = None,
    ):
        self.batch_count = batch_count
        self.blue_green_dep = blue_green_dep
        self.node_types = node_types
        self.nodes = nodes
        self.restart_type = restart_type
        self.client_token = client_token
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_count is not None:
            result['batchCount'] = self.batch_count

        if self.blue_green_dep is not None:
            result['blueGreenDep'] = self.blue_green_dep

        if self.node_types is not None:
            result['nodeTypes'] = self.node_types

        if self.nodes is not None:
            result['nodes'] = self.nodes

        if self.restart_type is not None:
            result['restartType'] = self.restart_type

        if self.client_token is not None:
            result['clientToken'] = self.client_token

        if self.force is not None:
            result['force'] = self.force

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchCount') is not None:
            self.batch_count = m.get('batchCount')

        if m.get('blueGreenDep') is not None:
            self.blue_green_dep = m.get('blueGreenDep')

        if m.get('nodeTypes') is not None:
            self.node_types = m.get('nodeTypes')

        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')

        if m.get('restartType') is not None:
            self.restart_type = m.get('restartType')

        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')

        if m.get('force') is not None:
            self.force = m.get('force')

        return self

