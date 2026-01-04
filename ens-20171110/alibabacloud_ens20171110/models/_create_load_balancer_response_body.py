# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerResponseBody(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        network_id: str = None,
        request_id: str = None,
        v_switch_id: str = None,
    ):
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the ELB instance.
        self.load_balancer_name = load_balancer_name
        # The ID of the network.
        self.network_id = network_id
        # The ID of the request.
        self.request_id = request_id
        # The ID of the vSwitch to which the ELB instance belongs.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

