# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServerLoadBalancerListenMonitorRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        load_balancer_id: str = None,
        proto: str = None,
        start_time: str = None,
        vport: str = None,
    ):
        # The end of the time range to query. The maximum range between StartTime and EndTime is 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the ELB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The request protocol, such as http, https, or tcp.
        self.proto = proto
        # The beginning of the time range to query. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The virtual IP address (VIP) port, such as 80, 8080, or 443.
        self.vport = vport

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.proto is not None:
            result['Proto'] = self.proto

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.vport is not None:
            result['VPort'] = self.vport

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Proto') is not None:
            self.proto = m.get('Proto')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('VPort') is not None:
            self.vport = m.get('VPort')

        return self

