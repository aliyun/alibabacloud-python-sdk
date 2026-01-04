# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyLoadBalancerAttributeRequest(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
    ):
        # The ID of the ELB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The name of the ELB instance. The name must be **2** to **128** characters in length.
        # 
        # >  The value cannot start with `http://` or `https://`.
        # 
        # This parameter is required.
        self.load_balancer_name = load_balancer_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        return self

