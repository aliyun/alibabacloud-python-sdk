# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class EnableScalingGroupRequest(DaraModel):
    def __init__(
        self,
        active_scaling_configuration_id: str = None,
        instance_ids: List[str] = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.EnableScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        load_balancer_weights: List[int] = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
    ):
        # The ID of the scaling configuration that you want to enable in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The IDs of the ECS instances that you want to add to the scaling group after the scaling group is enabled.
        # 
        # Before you add ECS instances to the scaling group, make sure that the instances meet the following requirements:
        # 
        # *   The instances must reside in the same region as the scaling group.
        # *   The instances must be in the Running state.
        # *   The instances do not belong to another scaling group.
        # *   The instances are billed on a subscription or pay-as-you-go basis, or the instances are preemptible instances.
        # *   If you specify VswitchID for the scaling group, the instances must share the same VPC as the scaling group.
        # *   If you do not specify VswitchID for the scaling group, the instances must use the classic network.
        self.instance_ids = instance_ids
        # The ID of the launch template that is used by Auto Scaling to create ECS instances.
        self.launch_template_id = launch_template_id
        # The information about the instance types that you want to extend in the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version number of the launch template. Valid values:
        # 
        # *   A fixed template version number.
        # *   Default: The default template version is always used.
        # *   Latest: The latest template version is always used.
        self.launch_template_version = launch_template_version
        # The weights of ECS instances or elastic container instances as backend servers.
        # 
        # Default value: 50.
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
        if self.launch_template_overrides:
            for v1 in self.launch_template_overrides:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

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
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.EnableScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

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

class EnableScalingGroupRequestLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        # The instance type. If you want to scale instances based on instance type weights in the scaling group, you must specify `LaunchTemplateOverrides.WeightedCapacity` after you specify this parameter.
        # 
        # The instance type specified by using this parameter overwrites the instance type of the launch template.
        # 
        # >  This parameter takes effect only if you specify LaunchTemplateId.
        # 
        # You can use this parameter to specify any instance types that are available for purchase.
        self.instance_type = instance_type
        # The weight of the instance type. If you want to scale instances based on instance type weights in the scaling group, you must specify this parameter after you specify `LaunchTemplateOverrides.InstanceType`.
        # 
        # The weight specifies the capacity of an instance of the specified instance type in the scaling group. A higher weight specifies that a smaller number of instances of the specified instance type are required to meet the expected capacity requirement.
        # 
        # Performance metrics such as the number of vCPUs and the memory size of each instance type may vary. You can specify different weights for different instance types based on your business requirements.
        # 
        # Example:
        # 
        # *   Current capacity: 0
        # *   Expected capacity: 6
        # *   Capacity of ecs.c5.xlarge: 4
        # 
        # To reach the expected capacity, Auto Scaling must scale out two instances of ecs.c5.xlarge.
        # 
        # >  The total capacity of the scaling group is constrained and cannot surpass the combined total of the maximum group size defined by MaxSize and the highest weight assigned to any instance type.
        # 
        # Valid values of WeightedCapacity: 1 to 500.
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        return self

