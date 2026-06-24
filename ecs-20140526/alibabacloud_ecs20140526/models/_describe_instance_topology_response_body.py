# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceTopologyResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        topologys: main_models.DescribeInstanceTopologyResponseBodyTopologys = None,
    ):
        self.request_id = request_id
        self.topologys = topologys

    def validate(self):
        if self.topologys:
            self.topologys.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.topologys is not None:
            result['Topologys'] = self.topologys.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Topologys') is not None:
            temp_model = main_models.DescribeInstanceTopologyResponseBodyTopologys()
            self.topologys = temp_model.from_map(m.get('Topologys'))

        return self

class DescribeInstanceTopologyResponseBodyTopologys(DaraModel):
    def __init__(
        self,
        topology: List[main_models.DescribeInstanceTopologyResponseBodyTopologysTopology] = None,
    ):
        self.topology = topology

    def validate(self):
        if self.topology:
            for v1 in self.topology:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Topology'] = []
        if self.topology is not None:
            for k1 in self.topology:
                result['Topology'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.topology = []
        if m.get('Topology') is not None:
            for k1 in m.get('Topology'):
                temp_model = main_models.DescribeInstanceTopologyResponseBodyTopologysTopology()
                self.topology.append(temp_model.from_map(k1))

        return self

class DescribeInstanceTopologyResponseBodyTopologysTopology(DaraModel):
    def __init__(
        self,
        host_id: str = None,
        instance_id: str = None,
        network_nodes: main_models.DescribeInstanceTopologyResponseBodyTopologysTopologyNetworkNodes = None,
    ):
        self.host_id = host_id
        self.instance_id = instance_id
        self.network_nodes = network_nodes

    def validate(self):
        if self.network_nodes:
            self.network_nodes.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.network_nodes is not None:
            result['NetworkNodes'] = self.network_nodes.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NetworkNodes') is not None:
            temp_model = main_models.DescribeInstanceTopologyResponseBodyTopologysTopologyNetworkNodes()
            self.network_nodes = temp_model.from_map(m.get('NetworkNodes'))

        return self

class DescribeInstanceTopologyResponseBodyTopologysTopologyNetworkNodes(DaraModel):
    def __init__(
        self,
        network_nodes: List[str] = None,
    ):
        self.network_nodes = network_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.network_nodes is not None:
            result['NetworkNodes'] = self.network_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NetworkNodes') is not None:
            self.network_nodes = m.get('NetworkNodes')

        return self

