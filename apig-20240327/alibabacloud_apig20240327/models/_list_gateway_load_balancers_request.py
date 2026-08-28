# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGatewayLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        load_balancer_id: str = None,
        network: str = None,
        related: bool = None,
        type: str = None,
        vpc_id: str = None,
    ):
        self.all = all
        self.load_balancer_id = load_balancer_id
        self.network = network
        self.related = related
        self.type = type
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.load_balancer_id is not None:
            result['loadBalancerId'] = self.load_balancer_id

        if self.network is not None:
            result['network'] = self.network

        if self.related is not None:
            result['related'] = self.related

        if self.type is not None:
            result['type'] = self.type

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('loadBalancerId') is not None:
            self.load_balancer_id = m.get('loadBalancerId')

        if m.get('network') is not None:
            self.network = m.get('network')

        if m.get('related') is not None:
            self.related = m.get('related')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

