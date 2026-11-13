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
        # The creation type of the instances in the scaling group. Valid values: 
        # 
        # - AutoCreated: The ECS instance is created by Auto Scaling through automatic creation based on the instance configuration source. 
        # - Attached: The ECS instance is not created by Auto Scaling, but is manually added to the scaling group.
        # - Managed: The managed instance is not created by Auto Scaling, but is manually added to the scaling group.
        self.creation_type = creation_type
        # The creation types of the instances in the scaling group. You can specify only one of the CreationTypes and CreationType parameters at a time.
        self.creation_types = creation_types
        # The health status of the ECS instances in the scaling group. ECS instances that are not in the Running state are considered unhealthy. Valid values: 
        # 
        # - Healthy: The ECS instance is healthy. 
        # - Unhealthy: The ECS instance is unhealthy. 
        # 
        # Auto Scaling automatically removes unhealthy ECS instances from the scaling group and releases ECS instances created through automatic creation.
        # 
        # Whether to release manually added ECS instances depends on their managed state. If the instance lifecycle is not managed by the scaling group, the instance is only removed but not released. If the instance lifecycle is managed by the scaling group, the instance is removed and released.
        # 
        # > Make sure that your account has sufficient active balance. If your account has overdue payments, all pay-as-you-go ECS instances, including pay-as-you-go instances and spot instances, are stopped or even released. For more information about the instance status changes of ECS instances in a scaling group after overdue payments, see [Overdue payments](https://help.aliyun.com/document_detail/170589.html).
        self.health_status = health_status
        # The IDs of the ECS instances.
        # 
        # Invalid InstanceIds are ignored in the returned query results, and no error is reported.
        self.instance_ids = instance_ids
        # The lifecycle state of the ECS instances in the scaling group. Valid values:
        #  
        # - InService: The ECS instance is added to the scaling group and provides services normally. 
        # - Pending: The ECS instance is being added to the scaling group. The procedure of adding an ECS instance to a scaling group includes adding the instance to the backend server group of a load balancing instance and adding the IP address of the instance to the access whitelist of an ApsaraDB RDS instance.
        # - Pending:Wait: The addition of the ECS instance to the scaling group is suspended. If a lifecycle hook applicable to scale-out activities is created in the scaling group, the ECS instance is suspended when it is added to the scaling group and waits for the hook timeout to end.
        # - Protected: The ECS instance provides services normally, but Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Standby: The ECS instance does not provide services, the weight of SLB backend server is set to zero, and Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Stopped: The ECS instance is stopped and does not provide services.
        # - Removing: The ECS instance is being removed from the scaling group. The procedure of removing an ECS instance from a scaling group includes removing the instance from the backend server group of a load balancing instance and removing the IP address of the instance from the access whitelist of an ApsaraDB RDS instance. 
        # - Removing:Wait: The removal of the ECS instance from the scaling group is suspended. If a lifecycle hook applicable to scale-down activities is created in the scaling group, the ECS instance is suspended when it is removed from the scaling group and waits for the hook timeout to end.
        self.lifecycle_state = lifecycle_state
        # The lifecycle statuses of the ECS instances in the scaling group. You can specify only one of the LifecycleStates and LifecycleState parameters at a time. We recommend that you use this parameter.
        self.lifecycle_states = lifecycle_states
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the ECS instance list. Pages start from page 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page in a paging query. Maximum value: 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The ID of the region to which the scaling group belongs.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling activity.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the associated scaling configuration.
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

