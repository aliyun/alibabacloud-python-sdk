# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeServerLoadBalancerMonitorRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        load_balancer_id: str = None,
        start_time: str = None,
    ):
        # The end time. The maximum interval between StartTime and EndTime cannot exceed 24 hours.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The load balancing instance ID.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The start time in the format of yyyy-MM-dd HH:mm:ss.
        # 
        # This parameter is required.
        self.start_time = start_time

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

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

