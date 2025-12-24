# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeScalingInstancesRequest(DaraModel):
    def __init__(
        self,
        creation_type: str = None,
        creation_types: List[str] = None,
        health_status: str = None,
        instance_ids: List[str] = None,
        lifecycle_state: str = None,
        lifecycle_states: List[str] = None,
        owner_account: str = None,
        owner_id: int = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
    ):
        # The instance creation method. Valid values:
        # 
        # *   AutoCreated: The ECS instances are created by Auto Scaling based on the instance configuration source.
        # *   Attached: The ECS instances are manually added to the scaling group.
        # *   Managed: The Alibaba Cloud-managed third-party instances are manually added to the scaling group.
        self.creation_type = creation_type
        # The instance creation methods. If you specify this parameter, you cannot specify CreationType.
        self.creation_types = creation_types
        # The health status of the ECS instance in the scaling group. If an ECS instance is not in the Running state, the instance is considered unhealthy. Valid values:
        # 
        # *   Healthy
        # *   Unhealthy
        # 
        # Auto Scaling automatically removes unhealthy ECS instances from the scaling group and then releases the automatically created instances among the unhealthy instances.
        # 
        # Unhealthy ECS instances that are manually added to the scaling group are released based on the management mode of the lifecycles of the instances. If the lifecycles of the ECS instances are not managed by the scaling group, Auto Scaling removes the instances from the scaling group but does not release the instances. If the lifecycles of the ECS instances are managed by the scaling group, Auto Scaling removes the instances from the scaling group and releases the instances.
        # 
        # >  Make sure that you have sufficient balance within your Alibaba Cloud account. If your Alibaba Cloud account has an overdue payment, all pay-as-you-go ECS instances, including preemptible instances, may be stopped or even released. For information about how the status of ECS instances changes when you have an overdue payment in your Alibaba Cloud account, see [Overdue payments](https://help.aliyun.com/document_detail/170589.html).
        self.health_status = health_status
        # The IDs of the ECS instances.
        # 
        # The IDs of inactive instances are not displayed in the query result, and no errors are returned.
        self.instance_ids = instance_ids
        # The lifecycle status of the ECS instance in the scaling group. Valid values:
        # 
        # *   InService: The ECS instance is added to the scaling group and provides services as expected.
        # *   Pending: The ECS instance is being added to the scaling group. When an ECS instance is being added to the scaling group, Auto Scaling also adds the instance to the backend server groups of the attached load balancers and adds the private IP address of the instance to the IP address whitelists of the attached ApsaraDB RDS instances.
        # *   Pending:Wait: The ECS instance is waiting to be added to the scaling group. If a scale-out lifecycle hook is in effect, the ECS instance remains in the Pending:Wait state until the timeout period for the lifecycle hook expires.
        # *   Protected: The ECS instance is protected. Protected ECS instances can continue to provide services as expected, but Auto Scaling does not manage the lifecycles of the ECS instances. You must manually manage the lifecycles of the ECS instances.
        # *   Standby: The ECS instance is on standby. Standby ECS instances do not provide services as expected, and the weights of the ECS instances as backend servers are reset to zero. Auto Scaling does not manage the lifecycles of the ECS instances. Therefore, you must manually manage the lifecycles of the ECS instances.
        # *   Stopped: The ECS instance is stopped. Stopped ECS instances no longer provide services.
        # *   Removing: The ECS instance is being removed from the scaling group. When an ECS instance is being removed from the scaling group, Auto Scaling also removes the instance from the backend server groups of the attached load balancers and removes the private IP address of the instance from the IP address whitelists of the attached ApsaraDB RDS instances.
        # *   Removing:Wait: The ECS instance is waiting to be removed from the scaling group. If a scale-in lifecycle hook is in effect, the ECS instance remains in the Removing:Wait state until the timeout period for the lifecycle hook expires.
        self.lifecycle_state = lifecycle_state
        # The lifecycle status of the ECS instances in the scaling group. You can specify only one of LifecycleStates and LifecycleState at a time. We recommend that you specify this parameter.
        self.lifecycle_states = lifecycle_states
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.creation_types is not None:
            result['CreationTypes'] = self.creation_types

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

        if self.lifecycle_states is not None:
            result['LifecycleStates'] = self.lifecycle_states

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('CreationTypes') is not None:
            self.creation_types = m.get('CreationTypes')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        if m.get('LifecycleStates') is not None:
            self.lifecycle_states = m.get('LifecycleStates')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        return self

