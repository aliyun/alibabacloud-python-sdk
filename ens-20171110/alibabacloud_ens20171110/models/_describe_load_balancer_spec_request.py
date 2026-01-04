# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLoadBalancerSpecRequest(DaraModel):
    def __init__(
        self,
        load_balancer_spec: str = None,
    ):
        # The specifications of the ELB instance.
        self.load_balancer_spec = load_balancer_spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_spec is not None:
            result['LoadBalancerSpec'] = self.load_balancer_spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerSpec') is not None:
            self.load_balancer_spec = m.get('LoadBalancerSpec')

        return self

