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
        # The request ID.
        self.request_id = request_id
        # Details about the topology.
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
    ):
        # The ID of the host where the ECS instance resides. This parameter is encrypted and cannot match the ID of the ECS instance. However, if the values of this parameter for different ECS instances are the same, the ECS instances reside on the same host.
        self.host_id = host_id
        # The instance ID.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.host_id is not None:
            result['HostId'] = self.host_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self

