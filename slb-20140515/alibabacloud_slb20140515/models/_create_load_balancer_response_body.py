# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLoadBalancerResponseBody(DaraModel):
    def __init__(
        self,
        address: str = None,
        address_ipversion: str = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        network_type: str = None,
        order_id: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The IP address that is allocated to the CLB instance.
        self.address = address
        # The IP version that is used by the CLB instance.
        self.address_ipversion = address_ipversion
        # The CLB instance ID.
        self.load_balancer_id = load_balancer_id
        # The CLB instance name.
        self.load_balancer_name = load_balancer_name
        # The network type of the CLB instance. Valid values:
        # 
        # *   **vpc**: VPC
        # *   **Classic**: classic network
        self.network_type = network_type
        # The order ID of the subscription CLB instance.
        self.order_id = order_id
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the CLB instance belongs.
        self.resource_group_id = resource_group_id
        # The ID of the vSwitch to which the CLB instance belongs.
        self.v_switch_id = v_switch_id
        # The ID of the VPC to which the CLB instance belongs.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.address_ipversion is not None:
            result['AddressIPVersion'] = self.address_ipversion

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.network_type is not None:
            result['NetworkType'] = self.network_type

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('AddressIPVersion') is not None:
            self.address_ipversion = m.get('AddressIPVersion')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('NetworkType') is not None:
            self.network_type = m.get('NetworkType')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

