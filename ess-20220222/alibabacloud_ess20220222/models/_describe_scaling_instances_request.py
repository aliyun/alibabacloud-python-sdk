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
        # The method used to create the instance in the scaling group. Valid values: 
        # 
        # - AutoCreated: The ECS instance is created by automatic creation based on the instance configuration source in Auto Scaling. 
        # - Attached: The ECS instance is not created by Auto Scaling but manually added to the scaling group.
        # - Managed: The managed instance is not created by Auto Scaling but manually added to the scaling group.
        self.creation_type = creation_type
        # The methods used to create instances in the scaling group. You can specify only one of this parameter and CreationType.
        self.creation_types = creation_types
        # The health check status of the ECS instance in the scaling group. ECS instances that are not in the Running state are considered unhealthy. Valid values: 
        # 
        # - Healthy: The ECS instance is healthy. 
        # - Unhealthy: The ECS instance is unhealthy. 
        # 
        # Auto Scaling automatically removes unhealthy ECS instances from the scaling group and releases the ECS instances created by automatic creation.
        # 
        # Whether a manually added ECS instance is released depends on its managed state. If the instance lifecycle is not managed by the scaling group, the instance is only removed but not released. If the instance lifecycle is managed by the scaling group, the instance is removed and released.
        # 
        # > Make sure that your account has a sufficient available quota. If your account has an overdue payment, all pay-as-you-go ECS instances (including pay-as-you-go instances and spot instances) are stopped or even released. For information about how the status of ECS instances in a scaling group changes after an overdue payment occurs, see [Overdue payments](https://help.aliyun.com/document_detail/170589.html).
        self.health_status = health_status
        # The IDs of the ECS instances.
        # 
        # Invalid InstanceId values are ignored in the query results, and no error is returned.
        self.instance_ids = instance_ids
        # The lifecycle state of the ECS instance in the scaling group. Valid values:
        #  
        # - InService: The ECS instance is added to the scaling group and provides services in the Normal state. 
        # - Pending: The ECS instance is being added to the scaling group. During this procedure, the ECS instance is added to the backend server group of the associated load balancing instance and to the access whitelist of the associated ApsaraDB RDS instance.
        # - Pending:Wait: The ECS instance is waiting to be added to the scaling group. If a lifecycle hook that applies to scale-out activities is created for the scaling group, the ECS instance is suspended and waits for the lifecycle hook timeout to end.
        # - Protected: The ECS instance is protected. The ECS instance provides services as expected, but Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Standby: The ECS instance is in the standby state. The ECS instance does not provide services, the weight of SLB backend server is set to zero, and Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Stopped: The ECS instance is stopped and does not provide services.
        # - Removing: The ECS instance is being removed from the scaling group. During this procedure, the ECS instance is removed from the backend server group of the associated load balancing instance and from the access whitelist of the associated ApsaraDB RDS instance. 
        # - Removing:Wait: The ECS instance is waiting to be removed from the scaling group. If a lifecycle hook that applies to scale-down activities is created for the scaling group, the ECS instance is suspended and waits for the lifecycle hook timeout to end.
        self.lifecycle_state = lifecycle_state
        # The lifecycle states of ECS instances in the scaling group. You can specify only one of this parameter and LifecycleState. We recommend that you use this parameter.
        self.lifecycle_states = lifecycle_states
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The page number of the ECS instance list. Minimum value: 1.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page in a paged query. Settings: Maximum value: 100.
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

