# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachLoadBalancersRequest(DaraModel):
    def __init__(
        self,
        async_: bool = None,
        client_token: str = None,
        force_detach: bool = None,
        load_balancers: List[str] = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        scaling_group_id: str = None,
    ):
        # Specifies whether to detach the CLB instance from the scaling group in an asynchronous manner. If you detach the CLB instance from the scaling group in an asynchronous manner, the call is successful only after all operations are successful. If a specific operation fails, the call fails. We recommend that you set this parameter to true.
        # 
        # Valid values:
        # 
        # *   true: detaches the CLB instance from the scaling group in an asynchronous manner. In this case, the ID of the scaling activity is returned.
        # *   false: does not detach the CLB instance from the scaling group in an asynchronous manner.
        # 
        # Default value: false.
        self.async_ = async_
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that the value is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to remove Elastic Compute Service (ECS) instances in the scaling group from the backend server groups of the load balancer. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.force_detach = force_detach
        # The IDs of the CLB instances. You can specify up to five instance IDs.
        # 
        # This parameter is required.
        self.load_balancers = load_balancers
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        # The ID of the scaling group.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.async_ is not None:
            result['Async'] = self.async_

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.force_detach is not None:
            result['ForceDetach'] = self.force_detach

        if self.load_balancers is not None:
            result['LoadBalancers'] = self.load_balancers

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Async') is not None:
            self.async_ = m.get('Async')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ForceDetach') is not None:
            self.force_detach = m.get('ForceDetach')

        if m.get('LoadBalancers') is not None:
            self.load_balancers = m.get('LoadBalancers')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

