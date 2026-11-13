# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyScalingGroupRequest(DaraModel):
    def __init__(
        self,
        active_scaling_configuration_id: str = None,
        allocation_strategy: str = None,
        auto_rebalance: bool = None,
        az_balance: bool = None,
        balance_mode: str = None,
        capacity_options: main_models.ModifyScalingGroupRequestCapacityOptions = None,
        compensate_with_on_demand: bool = None,
        custom_policy_arn: str = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        disable_desired_capacity: bool = None,
        group_deletion_protection: bool = None,
        health_check_type: str = None,
        health_check_types: List[str] = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.ModifyScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        owner_account: str = None,
        owner_id: int = None,
        removal_policies: List[str] = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
        scaling_policy: str = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        stop_instance_timeout: int = None,
        v_switch_ids: List[str] = None,
        zone_shift_policy: main_models.ModifyScalingGroupRequestZoneShiftPolicy = None,
    ):
        # The ID of the active scaling configuration in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The capacity allocation policy, which determines how the scaling group selects available instance types to meet the capacity requirements. The capacity distribution policy applies to both pay-as-you-go and spot capacities. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:                              
        # 
        # - priority: creates instances in the order of the configured instance types.
        # 
        # - lowestPrice: creates instances in ascending order of the vCPU unit price of the instance types.
        # 
        # Default value: priority.
        self.allocation_strategy = allocation_strategy
        # Specifies whether to enable automatic balancing for the scaling group. This parameter takes effect only when BalancedOnly is enabled for a zone-balanced scaling group. Valid values:
        # - false: disables automatic balancing for the scaling group.
        # - true: enables automatic balancing for the scaling group. The scaling group automatically detects the capacity across zones. If the capacity is unbalanced across zones, the scaling group proactively scales across zones to rebalance the capacity.
        # 
        # Default value: false.
        self.auto_rebalance = auto_rebalance
        # Specifies whether the capacity of the scaling group is evenly distributed across multiple zones. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:
        # - true: The capacity of the scaling group is evenly distributed across multiple zones.
        # - false: The capacity of the scaling group is not evenly distributed across multiple zones.
        # 
        # Default value: false.
        self.az_balance = az_balance
        # The zone balancing mode. This parameter takes effect only when the zone balancing mode is enabled. Valid values:
        #  
        # - BalancedBestEffort: If resource creation fails in a zone, the system degrades to other zones to ensure best-effort delivery of resources.
        # 
        # - BalancedOnly: If resource creation fails in a zone, the system does not degrade to other zones. The scale-out activity partially succeeds to avoid excessive imbalance of resources across different zones.
        # 
        # Default value: BalancedBestEffort.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # Specifies whether to automatically attempt to create pay-as-you-go instances to meet the required number of ECS instances if sufficient spot instances cannot be created due to price or inventory reasons when the MultiAZPolicy parameter of the CreateScalingGroup operation is set to COST_OPTIMIZED. Valid values:
        # 
        # - true: allows the creation of pay-as-you-go instances.
        # 
        # - false: does not allow the creation of pay-as-you-go instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The Alibaba Cloud Resource Name (ARN) of the Function Compute function for the custom scale-in policy. This parameter takes effect only when the first removal policy configured in RemovalPolicies is CustomPolicy.
        self.custom_policy_arn = custom_policy_arn
        # The default cooldown time of the scaling group. This parameter applies only to simple scaling rules. Valid values: 0 to 86400. Unit: seconds.
        # 
        # During the cooldown time, the scaling group does not execute any other scaling activities. This applies only to scaling activities triggered by CloudMonitor event-triggered tasks.
        self.default_cooldown = default_cooldown
        # The expected number of ECS instances or elastic container instances in the scaling group. The scaling group automatically maintains the number of ECS instances or elastic container instances at the expected number. Valid values: MinSize to MaxSize.
        # 
        # > If the expected number of instances feature is disabled and then re-enabled, you must reset the DesiredCapacity value.
        self.desired_capacity = desired_capacity
        # Specifies whether to disable the expected number of instances feature for the scaling group. Valid values:
        # 
        # - false: enables the expected number of instances feature.
        # - true: disables the expected number of instances feature.
        # 
        # > You can change the Settings of this parameter to true (that is, shutdown the expected number of instances feature) only when no scaling activity is in progress in the scaling group. When you shutdown the expected number of instances feature, the current DesiredCapacity property of the scaling group is cleared, but the current number of instances in the scaling group remains unchanged.
        self.disable_desired_capacity = disable_desired_capacity
        # Specifies whether to enable deletion protection for the scaling group. Valid values:
        # 
        # - true: enables deletion protection for the scaling group. In this case, the scaling group cannot be deleted.
        # - false: disables deletion protection for the scaling group.
        self.group_deletion_protection = group_deletion_protection
        # The health check mode of the scaling group. Valid values:
        # 
        # - NONE: disables health checks.
        # - ECS: performs health checks on instances in the scaling group. This value applies to both ECS and elastic container instance scaling groups.
        # - LOAD_BALANCER: determines the health status of instances based on the health check results of load balancing. Classic Load Balancer (CLB) is not supported.
        # Default value: ECS.
        # 
        # > To enable both instance health checks and load balancer health checks, use the HealthCheckTypes parameter.
        self.health_check_type = health_check_type
        # The health check modes of the scaling group.
        # 
        # > You can use this parameter to specify multiple values to enable multiple health check options. If the HealthCheckType parameter is configured, this parameter is ignored.
        self.health_check_types = health_check_types
        # The ID of the instance launch template, which is used to specify that the scaling group obtains launch configuration information from the instance launch template.
        self.launch_template_id = launch_template_id
        # The extended instance type information of the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the instance launch template. Valid values:
        #          
        # - A specific template version number.
        # - Default: always uses the default version of the template.
        # - Latest: always uses the latest version of the template.
        self.launch_template_version = launch_template_version
        # The maximum lifetime of an instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 0 or [86400, Integer.maxValue]. A value of 0 indicates that the configured value of MaxInstanceLifetime is cleared (that is, MaxInstanceLifetime is not configured).
        # 
        # Default value: null.
        # 
        # > This parameter cannot be configured for scaling groups of the elastic container instance type or scaling groups that have the no fees for stopped instances feature enabled.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of ECS instances or elastic container instances in the scaling group. If the number of ECS instances or elastic container instances in the scaling group exceeds the value of MaxSize, Auto Scaling automatically removes ECS instances or elastic container instances.
        # 
        # <props="china">The value range of MaxSize varies based on the usage of Auto Scaling. Go to the [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota value for the **maximum number of instances in a single scaling group**.
        # 
        # <props="intl">The value range of MaxSize varies based on the usage of Auto Scaling. Go to the [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota value for the **maximum number of instances in a single scaling group**.
        # 
        # <props="partner">The value range of MaxSize varies based on the usage of Auto Scaling. Go to the Quota Center to view the quota value for the **maximum number of instances in a single scaling group**.
        # 
        # For example, if the quota value for the **maximum number of instances in a single scaling group** is 2000, the value range of MaxSize is 0 to 2000.
        self.max_size = max_size
        # The minimum number of ECS instances or elastic container instances in the scaling group. If the number of ECS instances or elastic container instances in the scaling group is less than the value of MinSize, Auto Scaling initiates the automatic creation of ECS instances or elastic container instances.
        # 
        # > The value of MinSize must be less than or equal to the value of MaxSize.
        self.min_size = min_size
        # The scaling policy for ECS instances in a multi-zone scaling group. Valid values:
        # 
        # - PRIORITY: scales the scaling group based on the priorities of vSwitches (VSwitchIds.N). Auto Scaling preferentially attempts to scale the scaling group in the zone where the vSwitch with the highest priority resides. If the scaling fails, Auto Scaling automatically attempts to scale the scaling group in the zone where the vSwitch with the next highest priority resides.
        # 
        # - COST_OPTIMIZED: during scale-out, Auto Scaling attempts to create ECS instances in ascending order of vCPU unit price. During scale-in, Auto Scaling attempts to remove ECS instances in descending order of vCPU unit price. If the scaling configuration specifies multiple instance types that use the spot billing method, spot instances are preferentially created. You can use the CompensateWithOnDemand parameter to specify whether Auto Scaling automatically attempts to create pay-as-you-go instances when spot instances cannot be created.
        # 
        # > COST_OPTIMIZED takes effect only when the scaling configuration specifies multiple instance types or uses spot instances.
        # 
        # - BALANCE: evenly allocate ECS instances across the active zones specified for the scaling group. If the instances are unevenly distributed across zones due to insufficient inventory, you can call the RebalanceInstance operation to balance the resources.
        # 
        # - COMPOSABLE: a composite policy that allows you to combine the preceding scaling policies for ECS instances in a multi-zone scaling group based on your needs.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than this value, pay-as-you-go instances are preferentially created.
        # 
        # Default value: 0 when the MultiAZPolicy parameter is set to COMPOSABLE.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the minimum number of pay-as-you-go instances specified by OnDemandBaseCapacity. Valid values: 0 to 100.
        # 
        # Default value: 100 when the MultiAZPolicy parameter is set to COMPOSABLE.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The scale-in policy of the scaling group, which specifies the ECS instances to be removed. Valid values:
        # 
        # - OldestInstance: removes the ECS instances that were added to the scaling group at the earliest point in time.
        # 
        # - NewestInstance: removes the ECS instances that were added to the scaling group at the latest point in time.
        # 
        # - OldestScalingConfiguration: removes the ECS instances that were created by using the earliest scaling configuration.
        self.removal_policies = removal_policies
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group to be modified.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling group. The name must be unique within a region. The name must be 2 to 64 characters in length and start with a letter, digit, or Chinese character. It can contain digits, underscores (_), hyphens (-), and periods (.).
        self.scaling_group_name = scaling_group_name
        # The revoke pattern of the scaling group. Valid values: 
        # 
        # - recycle: The revoke pattern of the scaling group is shutdown and revoke pattern.  
        # - release: The revoke pattern of the scaling group is release pattern.
        # - forcerelease: The revoke pattern of the scaling group is forcible release pattern.
        # 
        #     > If you select forcerelease, the system forcibly releases instances in the Running state during scale-down activities. Forcibly releasing an instance is equivalent to a power-off operation, which erases temporary data in the memory and storage of the instance. The data cannot be recovered. Proceed with caution.
        # 
        # - forcerecycle: The revoke pattern of the scaling group is forcible shutdown and revoke pattern.
        # 
        #     > If you select forcerecycle, the system forcibly shuts down instances in the Running state during scale-down activities. Forcible shutdown is equivalent to a power-off operation, which erases temporary data in the memory and storage of the instance. The data cannot be recovered. Proceed with caution.
        # 
        # The ScalingPolicy parameter specifies the revoke pattern of the scaling group. However, the specific action when an instance is removed from the scaling group is determined by the RemovePolicy parameter of the RemoveInstances operation. For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The spot capacity distribution policy. You can use this parameter to separately specify the distribution policy for spot capacity. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:
        # 
        # - priority: creates instances in the order of the configured instance types.
        # - lowestPrice: creates instances in ascending order of the vCPU unit price of the instance types.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of available instance types. The scaling group evenly creates spot instances across multiple instance types with the lowest cost. Valid values: 0 to 10.
        # 
        # Default value: 2 when the MultiAZPolicy parameter is set to COMPOSABLE.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable the spot instance replenishment feature. After this feature is enabled, when the scaling group receives a system message indicating that a spot instance will be reclaimed, the scaling group attempts to create a new instance to replace the spot instance to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The timeout period for waiting for an ECS instance to be successfully stopped during the scale-in flow. Unit: seconds.
        # Valid values: 30 to 240.
        # 
        # > - This parameter takes effect only in the scale-in flow when ScalingPolicy is set to the release pattern.  
        # > - If the Settings of this parameter are configured, the system waits for a maximum of the StopInstanceTimeout period for the instance to be successfully stopped. After the timeout period elapses, the scale-in flow continues regardless of whether the instance is successfully stopped.  
        # > - If the Settings of this parameter are not configured, the system waits for a long time for the instance to be successfully stopped. The scale-in flow continues only after the instance is successfully stopped. If the instance stop has failed, the scale-in flow will rollback and the scale-in has failed.
        # > - A value of 0 indicates that the parameter settings of this parameter are canceled.
        self.stop_instance_timeout = stop_instance_timeout
        # The IDs of one or more vSwitches.
        # 
        # This parameter takes effect only when the network type of the scaling group is VPC. The VPC to which the specified vSwitches belong must be the same as the VPC to which the scaling group belongs.
        # 
        # The vSwitches can reside in different zones. The priorities of vSwitches are sorted in ascending order of numbers. 1 indicates the highest priority. If ECS instances cannot be created in the zone where the vSwitch with a higher priority resides, the vSwitch with the next highest priority is automatically selected to create ECS instances.
        self.v_switch_ids = v_switch_ids
        # The behavior policy of the scaling group during zone shift.
        self.zone_shift_policy = zone_shift_policy

    def validate(self):
        if self.capacity_options:
            self.capacity_options.validate()
        if self.launch_template_overrides:
            for v1 in self.launch_template_overrides:
                 if v1:
                    v1.validate()
        if self.zone_shift_policy:
            self.zone_shift_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id

        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy

        if self.auto_rebalance is not None:
            result['AutoRebalance'] = self.auto_rebalance

        if self.az_balance is not None:
            result['AzBalance'] = self.az_balance

        if self.balance_mode is not None:
            result['BalanceMode'] = self.balance_mode

        if self.capacity_options is not None:
            result['CapacityOptions'] = self.capacity_options.to_map()

        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

        if self.custom_policy_arn is not None:
            result['CustomPolicyARN'] = self.custom_policy_arn

        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown

        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity

        if self.disable_desired_capacity is not None:
            result['DisableDesiredCapacity'] = self.disable_desired_capacity

        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_types is not None:
            result['HealthCheckTypes'] = self.health_check_types

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.max_instance_lifetime is not None:
            result['MaxInstanceLifetime'] = self.max_instance_lifetime

        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy

        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity

        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name

        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy

        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy

        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.stop_instance_timeout is not None:
            result['StopInstanceTimeout'] = self.stop_instance_timeout

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_shift_policy is not None:
            result['ZoneShiftPolicy'] = self.zone_shift_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')

        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        if m.get('AutoRebalance') is not None:
            self.auto_rebalance = m.get('AutoRebalance')

        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')

        if m.get('BalanceMode') is not None:
            self.balance_mode = m.get('BalanceMode')

        if m.get('CapacityOptions') is not None:
            temp_model = main_models.ModifyScalingGroupRequestCapacityOptions()
            self.capacity_options = temp_model.from_map(m.get('CapacityOptions'))

        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

        if m.get('CustomPolicyARN') is not None:
            self.custom_policy_arn = m.get('CustomPolicyARN')

        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('DisableDesiredCapacity') is not None:
            self.disable_desired_capacity = m.get('DisableDesiredCapacity')

        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckTypes') is not None:
            self.health_check_types = m.get('HealthCheckTypes')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.ModifyScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('MaxInstanceLifetime') is not None:
            self.max_instance_lifetime = m.get('MaxInstanceLifetime')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')

        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')

        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')

        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')

        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')

        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('StopInstanceTimeout') is not None:
            self.stop_instance_timeout = m.get('StopInstanceTimeout')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneShiftPolicy') is not None:
            temp_model = main_models.ModifyScalingGroupRequestZoneShiftPolicy()
            self.zone_shift_policy = temp_model.from_map(m.get('ZoneShiftPolicy'))

        return self

class ModifyScalingGroupRequestZoneShiftPolicy(DaraModel):
    def __init__(
        self,
        impaired_zone_health_check_behavior: str = None,
        scale_in_blocked_rule_types: List[str] = None,
        scale_out_in_healthy_zones_only: bool = None,
    ):
        # The health check behavior in impaired zones. Valid values: 
        # 
        # - ReplaceUnhealthy: normally replaces unhealthy instances in all zones. 
        # - IgnoreUnhealthy: does not replace unhealthy instances in impaired zones. Healthy zones are not affected.
        self.impaired_zone_health_check_behavior = impaired_zone_health_check_behavior
        # Blocks scale-in activities triggered by specified types of scaling rules. The blocking scope covers all zones under the scaling group, not just the impaired zones. This prevents false scale-in activities caused by fake improvements in monitoring metrics due to unreachable instances in impaired zones. Valid values: 
        # 
        # - StepScalingRule: blocks scale-in activities triggered by step scaling rules. 
        # - TargetTrackingScalingRule: blocks scale-in activities triggered by target tracking scaling rules. 
        # - None: does not block any scale-in activities.
        self.scale_in_blocked_rule_types = scale_in_blocked_rule_types
        # Specifies whether scale-out creates instances only in healthy zones during zone shift. Valid values: 
        # 
        # - true: creates instances only in healthy zones during scale-out and skips impaired zones. 
        # - false: does not restrict zones, and scale-out can create instances in any zone under the scaling group.
        self.scale_out_in_healthy_zones_only = scale_out_in_healthy_zones_only

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.impaired_zone_health_check_behavior is not None:
            result['ImpairedZoneHealthCheckBehavior'] = self.impaired_zone_health_check_behavior

        if self.scale_in_blocked_rule_types is not None:
            result['ScaleInBlockedRuleTypes'] = self.scale_in_blocked_rule_types

        if self.scale_out_in_healthy_zones_only is not None:
            result['ScaleOutInHealthyZonesOnly'] = self.scale_out_in_healthy_zones_only

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImpairedZoneHealthCheckBehavior') is not None:
            self.impaired_zone_health_check_behavior = m.get('ImpairedZoneHealthCheckBehavior')

        if m.get('ScaleInBlockedRuleTypes') is not None:
            self.scale_in_blocked_rule_types = m.get('ScaleInBlockedRuleTypes')

        if m.get('ScaleOutInHealthyZonesOnly') is not None:
            self.scale_out_in_healthy_zones_only = m.get('ScaleOutInHealthyZonesOnly')

        return self

class ModifyScalingGroupRequestLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        weighted_capacity: int = None,
    ):
        # When you need the scaling group to scale based on the instance type capacity, specify both this parameter and LaunchTemplateOverrides.WeightedCapacity.
        # 
        # This parameter is used to specify the instance type and overrides the instance type in the launch template.
        # 
        # > This parameter takes effect only when the LaunchTemplateId parameter is specified.
        # 
        # Valid values of InstanceType: available ECS instance types.
        self.instance_type = instance_type
        # This parameter is used to specify the maximum hourly price for the instance type that overrides the launch template (that is, LaunchTemplateOverride.N.InstanceType). You can specify N values for this parameter to extend the launch template to support N instance types. Valid values of N: 1 to 20.
        # > This parameter takes effect only when the LaunchTemplateId parameter is specified.
        self.spot_price_limit = spot_price_limit
        # When you need the scaling group to scale based on the instance type capacity, specify this parameter after you specify LaunchTemplateOverrides.InstanceType. The two parameters correspond to each other.
        # 
        # This parameter is used to specify the weight of the instance type, which indicates the capacity that a single instance of the instance type represents in the scaling group.
        # 
        # A greater weight indicates that fewer instances of this instance type are required to meet the expected capacity.
        # 
        # Because performance metrics such as the number of vCPUs and memory size vary with instance types, you can configure different weights for different instance types based on your needs.
        # 
        # Example:
        # 
        # - Current capacity: 0.
        # 
        # - Expected capacity: 6.
        # 
        # - Capacity of the ecs.c5.xlarge instance type: 4.
        # 
        # To meet the expected capacity, the scaling group scales out two ecs.c5.xlarge instances.
        # 
        # > During scale-out, the capacity of the scaling group cannot exceed the sum of the maximum capacity (MaxSize) and the maximum weight of the instance type.
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

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        return self

class ModifyScalingGroupRequestCapacityOptions(DaraModel):
    def __init__(
        self,
        compensate_with_on_demand: bool = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        price_comparison_mode: str = None,
        spot_auto_replace_on_demand: bool = None,
    ):
        # Specifies whether to automatically attempt to create pay-as-you-go instances to meet the required number of ECS instances if sufficient spot instances cannot be created due to price or inventory reasons when the MultiAZPolicy parameter of the CreateScalingGroup operation is set to COST_OPTIMIZED. Valid values:
        # 
        # - true: allows the creation of pay-as-you-go instances.
        # - false: does not allow the creation of pay-as-you-go instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. If the number of pay-as-you-go instances in the scaling group is less than this value, the system preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        # 
        # Default value: 0 when the MultiAZPolicy parameter is set to COMPOSABLE.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the minimum number of pay-as-you-go instances specified by OnDemandBaseCapacity. Valid values: 0 to 100.
        # 
        # Default value: 100 when the MultiAZPolicy parameter is set to COMPOSABLE.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The price comparison mode for the cost optimization policy of the scaling group. Valid values:
        # - PricePerUnit: compares prices based on the price per unit of capacity.
        # 
        #   The capacity of an instance in the scaling group equals the weight configured for the instance type. The default weight is 1, which means one ECS instance occupies a capacity of 1.
        # 
        # - PricePerVCpu: compares prices based on the price per vCPU.
        # 
        # Default value: PricePerUnit.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to attempt to use spot instances to replace pay-as-you-go capacity when the percentage of pay-as-you-go instances exceeds the OnDemandPercentageAboveBaseCapacity value after CompensateWithOnDemand is enabled. In common scenarios where CompensateWithOnDemand downgrades spot instances to pay-as-you-go instances due to spot inventory or price reasons, this feature attempts to use spot instances to replace the excess pay-as-you-go capacity to avoid long-term retention of pay-as-you-go instances. Valid values:
        # 
        # - true: allows the replacement.
        # - false: does not allow the replacement.
        # 
        # Default value: false.
        self.spot_auto_replace_on_demand = spot_auto_replace_on_demand

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity

        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity

        if self.price_comparison_mode is not None:
            result['PriceComparisonMode'] = self.price_comparison_mode

        if self.spot_auto_replace_on_demand is not None:
            result['SpotAutoReplaceOnDemand'] = self.spot_auto_replace_on_demand

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')

        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')

        if m.get('PriceComparisonMode') is not None:
            self.price_comparison_mode = m.get('PriceComparisonMode')

        if m.get('SpotAutoReplaceOnDemand') is not None:
            self.spot_auto_replace_on_demand = m.get('SpotAutoReplaceOnDemand')

        return self

