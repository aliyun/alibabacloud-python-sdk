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
        # Ensures the idempotence of the request.
        # 
        # You can generate a parameter value from your client to ensure that the value is unique among different requests. The value can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to entrust the lifecycle of an existing instance to the scaling group when the instance is manually added to the scaling group. Valid values:
        # 
        # - true: Entrusted. The lifecycle of the instance is managed by Auto Scaling, which is the same as that of instances automatically created by the scaling group. The instance is automatically released when it is removed from the scaling group (excluding instances removed when you invoke the DetachInstances operation).
        # - false: Not entrusted. The instance is not released when it is removed from the scaling group.
        # 
        # > This parameter is not supported for subscription instances, managed instances, and instances in the Economical Mode in the scaling group.
        # 
        # Default value: false.
        self.entrusted = entrusted
        # Specifies whether to ignore invalid instances when a batch of instances is added to the scaling group. Valid values:
        # 
        # - true: Invalid instances are ignored when a batch of instances is added to the scaling group. If invalid instances exist and valid instances are successfully added, the execution status of the scaling activity is displayed as Warning. You can view the invalid instances in the scaling activity details.
        # 
        # - false: Invalid instances are not ignored when a batch of instances is added to the scaling group. If invalid instances exist in the batch, an error is reported.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances, ECI instances, managed instances, or instances in the Economical Mode in the scaling group to be added.
        self.instance_ids = instance_ids
        # Specifies whether to trigger the scale-out lifecycle hook when instances are added to the scaling group. Valid values:
        # 
        # - true: Triggered.
        # - false: Not triggered.
        # > This parameter is not supported for managed instances and instances in the Economical Mode in the scaling group.
        # 
        # Default value: false.
        self.lifecycle_hook = lifecycle_hook
        # The weight of the ECS instance or ECI instance as a backend server of the load balancing instance.
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

