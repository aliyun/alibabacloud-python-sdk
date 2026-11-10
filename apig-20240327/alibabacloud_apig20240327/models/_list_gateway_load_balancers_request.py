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
        # Specifies whether to return all instances in the optional list mode. This parameter affects the pagination and filtering strategies.
        self.all = all
        # The exact load balancer instance ID used to query details by ID in the optional list mode.
        self.load_balancer_id = load_balancer_id
        # The network type filter.
        self.network = network
        # Specifies whether to return the list of load balancers associated with the gateway. If set to true, the associated load balancers are returned based on database relationships. We recommend setting this parameter to true to retrieve the associated load balancers. If set to false or left empty, the optional list mode is used to call the SLB or NLB API and filter bindable instances. In the default mode where related is false, calling the SLB or NLB API may return a 500 error due to backend data issues in common scenarios.
        self.related = related
        # The load balancer type filter.
        self.type = type
        # The VPC filter used to filter instances within the specified VPC in the optional list mode. This parameter is required when type is set to NLB and related is not set to true. Otherwise, the API returns a 500 error.
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

