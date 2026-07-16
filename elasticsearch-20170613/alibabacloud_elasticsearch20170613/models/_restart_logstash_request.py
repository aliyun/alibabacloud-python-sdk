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
        # The concurrency for force restart. This parameter does not need to be set during a blue-green restart because force restart is not supported in that scenario.
        self.batch_count = batch_count
        # Specifies whether to perform a blue-green restart. Default value: false.
        self.blue_green_dep = blue_green_dep
        # The type of role node to restart. This parameter is not supported.
        self.node_types = node_types
        # The node information selected when restarting nodes.
        self.nodes = nodes
        # The restart type. Valid values:
        # 
        # - instance: restart the instance
        # - nodeIp: restart a node.
        self.restart_type = restart_type
        # A client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether to force restart the instance. Valid values:
        # 
        # - true: force restart
        # - false (default): do not force restart.
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

