# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DetachInstancesRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        decrease_desired_capacity: bool = None,
        detach_option: str = None,
        ignore_invalid_instance: bool = None,
        instance_ids: List[str] = None,
        lifecycle_hook: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to adjust the expected number of instances in the scaling group. Valid values:
        # 
        # *   true: After a specific number of instances are removed from the scaling group, the expected number of instances in the scaling group decreases.
        # *   false: After a specific number of instances are removed from the scaling group, the expected number of instances in the scaling group remains unchanged.
        # 
        # Default value: true.
        self.decrease_desired_capacity = decrease_desired_capacity
        # Specifies whether to detach the ECS instances or elastic container instances that are marked for removal from the associated load balancers, and whether to remove the private IP addresses of these instances from the IP address whitelists of the associated ApsaraDB RDS instances.
        # 
        # Both: detaches the ECS instances or elastic container instances that are marked for removal from the associated load balancers and removes the private IP addresses of these instances from the IP address whitelists of the associated ApsaraDB RDS instances.
        # 
        # >  This parameter is not supported if you want to remove Alibaba Cloud-hosted third-party instances from a scaling group.
        self.detach_option = detach_option
        # Specifies whether to ignore invalid instances when you remove a batch of instances from the scaling group. Valid values:
        # 
        # *   true: ignores invalid instances. If invalid instances exist and valid instances are removed from the scaling group, the corresponding scaling activity enters the Warning state. You can check the scaling activity details to view the invalid instances that are ignored.
        # *   false: does not ignore invalid instances. If invalid instances exist in the batch of instances that you want to remove from the scaling group, an error is reported.
        # 
        # Default value: false.
        self.ignore_invalid_instance = ignore_invalid_instance
        # The IDs of the ECS instances, elastic container instances, or Aliababa Cloud-managed third-party instances that you want to remove from a scaling group.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # Specifies whether to trigger a lifecycle hook for scale-in purposes when ECS instances or elastic container instances are removed from the scaling group. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is not supported if you want to remove Alibaba Cloud-hosted third-party instances from a scaling group.
        # 
        # Default value: false.
        self.lifecycle_hook = lifecycle_hook
        self.owner_account = owner_account
        self.owner_id = owner_id
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

        if self.decrease_desired_capacity is not None:
            result['DecreaseDesiredCapacity'] = self.decrease_desired_capacity

        if self.detach_option is not None:
            result['DetachOption'] = self.detach_option

        if self.ignore_invalid_instance is not None:
            result['IgnoreInvalidInstance'] = self.ignore_invalid_instance

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lifecycle_hook is not None:
            result['LifecycleHook'] = self.lifecycle_hook

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

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

        if m.get('DecreaseDesiredCapacity') is not None:
            self.decrease_desired_capacity = m.get('DecreaseDesiredCapacity')

        if m.get('DetachOption') is not None:
            self.detach_option = m.get('DetachOption')

        if m.get('IgnoreInvalidInstance') is not None:
            self.ignore_invalid_instance = m.get('IgnoreInvalidInstance')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LifecycleHook') is not None:
            self.lifecycle_hook = m.get('LifecycleHook')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

