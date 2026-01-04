# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        address: str = None,
        ens_region_id: str = None,
        ens_region_ids: List[str] = None,
        load_balancer_id: str = None,
        load_balancer_name: str = None,
        load_balancer_status: str = None,
        load_balancer_type: str = None,
        network_id: str = None,
        page_number: int = None,
        page_size: int = None,
        server_id: str = None,
        v_switch_id: str = None,
    ):
        # The IP address that the ELB instance uses to provide services.
        self.address = address
        # The ID of the Edge Node Service (ENS) node.
        self.ens_region_id = ens_region_id
        # The IDs of the Edge Node Service (ENS) nodes.
        self.ens_region_ids = ens_region_ids
        # The ID of the ELB instance.
        self.load_balancer_id = load_balancer_id
        # The name of the ELB instance.
        self.load_balancer_name = load_balancer_name
        # The status of the listener for the ELB instance. Valid values:
        # 
        # *   **Active**: The listener for the instance can forward the received traffic based on forwarding rules.
        # *   **InActive**: The listener for the instance does not forward the received traffic.
        self.load_balancer_status = load_balancer_status
        self.load_balancer_type = load_balancer_type
        # The ID of the network.
        self.network_id = network_id
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page. Default value: 10. Valid values: **10** to **100**.
        self.page_size = page_size
        # The ID of the backend server.
        self.server_id = server_id
        # The ID of the vSwitch.
        self.v_switch_id = v_switch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.ens_region_ids is not None:
            result['EnsRegionIds'] = self.ens_region_ids

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.load_balancer_name is not None:
            result['LoadBalancerName'] = self.load_balancer_name

        if self.load_balancer_status is not None:
            result['LoadBalancerStatus'] = self.load_balancer_status

        if self.load_balancer_type is not None:
            result['LoadBalancerType'] = self.load_balancer_type

        if self.network_id is not None:
            result['NetworkId'] = self.network_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.server_id is not None:
            result['ServerId'] = self.server_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('EnsRegionIds') is not None:
            self.ens_region_ids = m.get('EnsRegionIds')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerName') is not None:
            self.load_balancer_name = m.get('LoadBalancerName')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('LoadBalancerType') is not None:
            self.load_balancer_type = m.get('LoadBalancerType')

        if m.get('NetworkId') is not None:
            self.network_id = m.get('NetworkId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServerId') is not None:
            self.server_id = m.get('ServerId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        return self

