# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLoadBalancerStatusRequest(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        load_balancer_status: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the CLB instance.
        # 
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        # The state of the CLB instance. Valid values: **active** and **inactive**.
        # 
        # *   **active** (default)
        # 
        #     If a CLB instance is in the **active** state, listeners of the CLB instance can forward traffic based on forwarding rules.
        # 
        #     By default, newly created CLB instances are in the **active** state.
        # 
        # *   **inactive**
        # 
        #     If a CLB instance is in the **inactive** state, listeners of the CLB instance do not forward traffic.
        # 
        # >  If all listeners of a CLB instance are deleted, the CLB instance automatically switches to the **inactive** state.
        # 
        # This parameter is required.
        self.load_balancer_status = load_balancer_status
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the CLB instance is deployed.
        # 
        # You can query region IDs from the [Regions and zones](https://help.aliyun.com/document_detail/40654.html) list or by calling the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

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

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('LoadBalancerStatus') is not None:
            self.load_balancer_status = m.get('LoadBalancerStatus')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

