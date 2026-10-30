# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerStatusRequest(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_status: str = None,
    ):
        # The instance ID of the load balancing instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The updated instance status. Valid values:
        # - **Active**: Runs the load balancing instance. Listeners in the instance can forward accepted traffic based on rules.
        # - **InActive**: Stops the load balancing instance. Listeners in the instance no longer forward accepted traffic.
        # 
        # This parameter is required.
        self.load_balancer_status = load_balancer_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        return self

