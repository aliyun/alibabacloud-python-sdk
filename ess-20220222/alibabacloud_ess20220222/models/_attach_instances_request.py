# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AttachInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        entrusted: bool = None,
        ignore_invalid_instance: bool = None,
        instance_ids: List[str] = None,
        lifecycle_hook: bool = None,
        load_balancer_weights: List[int] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to use the scaling group to manage the lifecycles of manually added instances. Valid values:
        # 
        # *   true: The scaling group manages the lifecycles of manually added instances and automatically created instances in the same manner. In this case, Auto Scaling releases the instances when they are removed from the scaling group. This rule does not apply to instances that are removed by calling the DetachInstances operation.
        # *   false: The scaling group does not manage the lifecycles of manually added instances. In this case, Auto Scaling does not release the instances when they are removed from the scaling group.
        # 
        # >  You cannot specify this parameter for subscription instances, non-Alibaba Cloud instances, and instances in Economical Mode.
        # 
        # Default value: false.
        self.entrusted = entrusted
        # Specifies whether to ignore invalid instances when a batch of instances is added to the scaling group. Valid values:
        # 
        # *   true: ignores invalid instances. If invalid instances exist and valid instances are added, the corresponding scaling activity enters the Warning state. You can check the scaling activity details to view the invalid instances that are ignored.
        # *   false: does not ignore invalid instances. If invalid instances exist in the batch of instances that you want to add to the scaling group, an error is reported.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances, elastic container instances, non-Alibaba Cloud instances, or instances in Economical Mode.
        self.instance_ids = instance_ids
        # Specifies whether to trigger the lifecycle hook for scale-outs when you call this operation. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  You cannot specify this parameter for subscription instances and instances in Economical Mode.
        # 
        # Default value: false.
        self.lifecycle_hook = lifecycle_hook
        # The weight of an ECS instance or elastic container instance as a backend server. You can use this parameter to specify weights for multiple instances at the same time.
        self.load_balancer_weights = load_balancer_weights
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
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
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted

        if self.ignore_invalid_instance is not None:
            result['IgnoreInvalidInstance'] = self.ignore_invalid_instance

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lifecycle_hook is not None:
            result['LifecycleHook'] = self.lifecycle_hook

        if self.load_balancer_weights is not None:
            result['LoadBalancerWeights'] = self.load_balancer_weights

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

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')

        if m.get('IgnoreInvalidInstance') is not None:
            self.ignore_invalid_instance = m.get('IgnoreInvalidInstance')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LifecycleHook') is not None:
            self.lifecycle_hook = m.get('LifecycleHook')

        if m.get('LoadBalancerWeights') is not None:
            self.load_balancer_weights = m.get('LoadBalancerWeights')

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

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

