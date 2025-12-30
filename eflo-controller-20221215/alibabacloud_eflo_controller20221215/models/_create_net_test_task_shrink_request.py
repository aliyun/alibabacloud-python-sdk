# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNetTestTaskShrinkRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        comm_test_shrink: str = None,
        delay_test_shrink: str = None,
        net_test_type: str = None,
        network_mode: str = None,
        port: str = None,
        traffic_test_shrink: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The cluster name.
        self.cluster_name = cluster_name
        # Specify when NetTestType is CommTest.
        self.comm_test_shrink = comm_test_shrink
        # Specify when NetTestType is DelayTest.
        self.delay_test_shrink = delay_test_shrink
        # The type of the network test. Valid values: DelayTest, TrafficTest, and CommTest.
        self.net_test_type = net_test_type
        # The network mode.
        self.network_mode = network_mode
        # The port number.
        self.port = port
        # If the TrafficModel is Fullmesh, leave this parameter empty.
        self.traffic_test_shrink = traffic_test_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.cluster_name is not None:
            result['ClusterName'] = self.cluster_name

        if self.comm_test_shrink is not None:
            result['CommTest'] = self.comm_test_shrink

        if self.delay_test_shrink is not None:
            result['DelayTest'] = self.delay_test_shrink

        if self.net_test_type is not None:
            result['NetTestType'] = self.net_test_type

        if self.network_mode is not None:
            result['NetworkMode'] = self.network_mode

        if self.port is not None:
            result['Port'] = self.port

        if self.traffic_test_shrink is not None:
            result['TrafficTest'] = self.traffic_test_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('ClusterName') is not None:
            self.cluster_name = m.get('ClusterName')

        if m.get('CommTest') is not None:
            self.comm_test_shrink = m.get('CommTest')

        if m.get('DelayTest') is not None:
            self.delay_test_shrink = m.get('DelayTest')

        if m.get('NetTestType') is not None:
            self.net_test_type = m.get('NetTestType')

        if m.get('NetworkMode') is not None:
            self.network_mode = m.get('NetworkMode')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('TrafficTest') is not None:
            self.traffic_test_shrink = m.get('TrafficTest')

        return self

