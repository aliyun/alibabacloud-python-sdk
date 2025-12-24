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
    ):
        # The ID of the active scaling configuration in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The allocation policy. Auto Scaling selects instance types based on the allocation policy to create the required number of instances. The policy can be applied to pay-as-you-go instances and preemptible instances at the same time. This parameter takes effect only when you set the MultiAZPolicy parameter to COMPOSABLE. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order to create the required number of instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the lowest unit price of vCPUs to create the required number of instances.
        # 
        # Default value: priority.
        self.allocation_strategy = allocation_strategy
        # Whether to enable automatic rebalancing for the scaling group. This takes effect only when BalancedOnly is enabled for the scaling group. Valid values:
        # 
        # *   false: Auto rebalancing is disabled for the scaling group.
        # *   true: If Auto rebalancing is enabled, the scaling group automatically detects the capacity of the zone. If the capacity of the zone is unbalanced, the scaling group actively scales out the zone and re-balances the capacity of the zone.
        # 
        # Default value: false.
        self.auto_rebalance = auto_rebalance
        # Specifies whether to evenly distribute instances in the scaling group across zones. This parameter takes effect only when you set the `MultiAZPolicy` parameter to `COMPOSABLE`. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.az_balance = az_balance
        # The zone balancing mode. This mode takes effect only when the zone balancing mode is enabled. Valid values:
        # 
        # *   BalancedBestEffort: If a resource fails to be created in a zone, the resource is downgraded to another zone. This ensures best-effort delivery of the resource.
        # *   BalancedOnly: If a resource fails to be created in a zone, the resource is not downgraded to another zone. The scale-out activity is partially successful to avoid excessive imbalance of resources in different zones.
        # 
        # Default value: BalancedBestEffort.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # Specifies whether to automatically create pay-as-you-go instances to meet the requirements on the number of ECS instances in the scaling group when the number of preemptible instances cannot be reached due to reasons such as cost-related issues and insufficient resources. This parameter takes effect only if you set `MultiAZPolicy` in the `CreateScalingGroup` operation to `COST_OPTIMIZED`. Valid values:
        # 
        # *   true
        # *   false
        self.compensate_with_on_demand = compensate_with_on_demand
        # The ARN of the custom scaling policy (Function). This parameter takes effect only when you specify CustomPolicy as the first step of the instance removal policy.
        self.custom_policy_arn = custom_policy_arn
        # The cooldown period of the scaling group. This parameter is available only if you set ScalingRuleType to SimpleScalingRule. Valid values: 0 to 86400. Unit: seconds.
        # 
        # During the cooldown period, Auto Scaling does not execute scaling activities that are triggered by CloudMonitor event-triggered tasks.
        self.default_cooldown = default_cooldown
        # The expected number of ECS instances or elastic container instances in the scaling group. Auto Scaling maintains the expected number of ECS instances or elastic container instances in the scaling group. Make sure that you adhere to the following rule when specifying this parameter: Value of MaxSize ≥ Value of DesiredCapacity ≥ Value of MinSize
        # 
        # >  If you re-enable the Expected Number of Instances feature, you must specify a value for `DesiredCapacity` again.
        self.desired_capacity = desired_capacity
        self.disable_desired_capacity = disable_desired_capacity
        # Specifies whether to enable deletion protection for the scaling group. Valid values:
        # 
        # *   true: enables deletion protection for the scaling group. This way, the scaling group cannot be deleted.
        # *   false: disables deletion protection for the scaling group.
        self.group_deletion_protection = group_deletion_protection
        # The health check mode of the scaling group. Valid values:
        # 
        # *   NONE: Auto Scaling does not check the health status of instances.
        # *   ECS: Auto Scaling checks the health status of instances in the scaling group. If you want to enable instance health check, you can set the value to ECS, regardless of whether the scaling group is of ECS type or Elastic Container Instance type.
        # *   LOAD_BALANCER: Auto Scaling checks the health status of instances in the scaling group based on the health check results of load balancers. The health check results of Classic Load Balancer (CLB) instances are not supported as the health check basis for instances in the scaling group. Default value: ECS.
        # 
        # >  If you want to enable instance health check and load balancer health check at the same time, we recommend that you specify `HealthCheckTypes`.
        self.health_check_type = health_check_type
        # The health check mode of the scaling group.
        # 
        # >  You can specify multiple values for this parameter to enable multiple health check options at the same time. If you specify HealthCheckType, this parameter is ignored.
        self.health_check_types = health_check_types
        # The ID of the launch template that is used by Auto Scaling to create instances.
        self.launch_template_id = launch_template_id
        # Details of the instance types that are specified in the extended configurations of the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version number of the launch template. Valid values:
        # 
        # *   A fixed template version number.
        # *   Default: The default template version is always used.
        # *   Latest: The latest template version is always used.
        self.launch_template_version = launch_template_version
        # The maximum life span of the instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 86400 to Integer.maxValue. ``You can also set this parameter to 0. A value of 0 indicates that the instance has an unlimited life span in the scaling group.
        # 
        # Default value: null.
        # 
        # > You cannot specify this parameter for scaling groups that manage elastic container instances or scaling groups whose ScalingPolicy is set to recycle.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of ECS instances or elastic container instances that can be contained in the scaling group. If the total number of instances in the scaling group is greater than the value of MaxSize, Auto Scaling proactively removes the surplus instances from the scaling group to restore the total number to match the maximum limit.
        # 
        # The value range of MaxSize is directly correlated with the degree of dependency your business has on Auto Scaling. You can go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check **the maximum number of instances that a single scaling group can contain.**
        # 
        # For example, if a scaling group can contain up to **2,000** instances, the value range of MaxSize is 0 to 2000.
        self.max_size = max_size
        # The minimum number of ECS instances or elastic container instances that must be contained in the scaling group. If the total number of instances in the scaling group is less than the value of MinSize, Auto Scaling proactively adds instances to the scaling group to ensure that the total number aligns with the minimum threshold.
        # 
        # >  The value of MinSize must be less than or equal to the value of MaxSize.
        self.min_size = min_size
        # The scaling policy for the multi-zone scaling group that contains ECS instances. Valid values:
        # 
        # *   PRIORITY: ECS instances are scaled based on the vSwitch priority. The first vSwitch specified by using the VSwitchIds parameter has the highest priority. Auto Scaling preferentially scales instances in the zone where the vSwitch that has the highest priority resides. If the scaling fails, Auto Scaling scales instances in the zone where the vSwitch that has the next highest priority resides.
        # *   COST_OPTIMIZED: During a scale-out activity, Auto Scaling preferentially creates ECS instances of the instance type that has the lowest unit price of vCPU. During a scale-in activity, Auto Scaling preferentially removes ECS instances of the instance types that have the highest unit price of vCPU. Auto Scaling preferentially creates preemptible instances when preemptible instance types are specified in the scaling configuration. You can use the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when Auto Scaling fails to create preemptible instances.
        # 
        # > The `COST_OPTIMIZED` setting takes effect only when multiple instance types are specified or at least one instance type is specified for preemptible instances.
        # 
        # *   BALANCE: ECS instances are evenly distributed across zones that are specified in the scaling group. If ECS instances are unevenly distributed among zones due to insufficient resources, you can call the RebalanceInstance operation to evenly distribute the instances among the zones.
        # *   COMPOSABLE: You can flexibly combine the preceding policies based on your business requirements.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances that must be included in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances.
        # 
        # If you set the `MultiAZPolicy` parameter to `COMPOSABLE` Policy, the default value is 0.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The expected percentage of pay-as-you-go instances in the excess instances when the minimum number of pay-as-you-go instances reaches the requirement. Valid values: 0 to 100.
        # 
        # If you set the `MultiAZPolicy` parameter to `COMPOSABLE` Policy, the default value is 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy that is used to remove ECS instances from the scaling group. Valid values:
        # 
        # *   OldestInstance: removes ECS instances that are added at the earliest point in time to the scaling group.
        # *   NewestInstance: removes ECS instances that are most recently added to the scaling group.
        # *   OldestScalingConfiguration: removes ECS instances that are created based on the earliest scaling configuration.
        self.removal_policies = removal_policies
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the scaling group that you want to modify.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling group. The name of each scaling group must be unique in a region. The name must be 2 to 64 characters in length and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit.
        self.scaling_group_name = scaling_group_name
        # The reclaim mode of the scaling group. Valid values:
        # 
        # *   recycle: economical mode
        # 
        # *   release: release mode
        # 
        # *   forcerelease: forced release mode
        # 
        #     **
        # 
        #     **Note** If you set the value to `forcerelease`, Auto Scaling forcibly releases instances that are in the `Running` state during scale-ins. Forced release is equivalent to power outage. If an instance is forcibly released, ephemeral data on the instance will be cleared and cannot be recovered. Exercise caution when you select this option.
        # 
        # *   forcerecycle: forced recycle mode
        # 
        #     **
        # 
        #     **Note** If you set the value to `forcerecycle`, Auto Scaling forcibly shuts down instances that are in the `Running` state during scale-ins. Forced shutdown is equivalent to power outage. If an instance is forcibly shut down, ephemeral data on the instance will be cleared and cannot be recovered. Exercise caution when you select this option.
        # 
        # ScalingPolicy specifies only the reclaim mode of the scaling group. RemovePolicy of the RemoveInstances operation specifies the manner how instances are removed from the scaling group. For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The allocation policy of preemptible instances. You can use this parameter to individually specify the allocation policy of preemptible instances. This parameter takes effect only when you set the `MultiAZPolicy` parameter to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order to create the required number of preemptible instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the lowest unit price of vCPUs to create the required number of preemptible instances.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of instance types that you specify. Auto Scaling creates preemptible instances of multiple instance types that are provided at the lowest price. Valid values: 0 to 10.
        # 
        # If you set the `MultiAZPolicy` parameter to `COMPOSABLE` Policy, the default value is 2.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to supplement preemptible instances. If this parameter is set to true, Auto Scaling creates an instance to replace a preemptible instance when Auto Scaling receives the system message that the preemptible instance is to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The period of time that is required by the Elastic Compute Service (ECS) instance to enter the Stopped state during the scale-in process. Unit: seconds. Valid values: 30 to 240.
        # 
        # > 
        # 
        # *   This parameter takes effect only if you set ScalingPolicy to release.\\
        #     If you specify this parameter, the system proceeds with the scale-in process only after the period of time specified by StopInstanceTimeout ends. In this case, the scale-in operation continues regardless of whether the ECS instance enters the Stopped state or not.\\
        #     If you do not specify this parameter, the system proceeds with the scale-in process only after the ECS instance enters the Stopped state. If the ECS instance fails to enter the Stopped state, the scale-in process rolls back, and the scale-in operation is considered as failed.
        # 
        # *   When you call the ModifyScalingGroup operation, you can set the value to 0. In this case, the system ignores this parameter.
        self.stop_instance_timeout = stop_instance_timeout
        # The IDs of vSwitches.
        # 
        # This parameter takes effect only when the network type of the scaling group is virtual private cloud (VPC). The specified vSwitches and the scaling group must reside in the same VPC.
        # 
        # The vSwitches can reside in different zones. The vSwitches are sorted in ascending order. The first vSwitch specified by using the VSwitchIds parameter has the highest priority. If Auto Scaling fails to create ECS instances in the zone where the vSwitch that has the highest priority resides, Auto Scaling creates ECS instances in the zone where the vSwitch that has the next highest priority resides.
        self.v_switch_ids = v_switch_ids

    def validate(self):
        if self.capacity_options:
            self.capacity_options.validate()
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

        return self

class ModifyScalingGroupRequestLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        weighted_capacity: int = None,
    ):
        # The instance type. The instance type that you specify by using the InstanceType parameter overwrites the instance type that is specified in the launch template.
        # 
        # If you want Auto Scaling to scale instances in the scaling group based on the instance type weight, you must specify both the InstanceType and WeightedCapacity parameters.
        # 
        # > This parameter takes effect only after you specify the LaunchTemplateId parameter.
        # 
        # You can use the InstanceType parameter to specify only instance types that are available for purchase.
        self.instance_type = instance_type
        self.spot_price_limit = spot_price_limit
        # The weight of the instance type. The weight specifies the capacity of a single instance of the specified instance type in the scaling group. If you want Auto Scaling to scale instances in the scaling group based on the weighted capacity of instances, you must specify the WeightedCapacity parameter after you specify the InstanceType parameter.
        # 
        # A higher weight specifies that a smaller number of instances of the specified instance type are required to meet the expected capacity.
        # 
        # Performance metrics, such as the number of vCPUs and the memory size of each instance type, may vary. You can specify different weights for different instance types based on your business requirements.
        # 
        # Example:
        # 
        # *   Current capacity: 0
        # *   Expected capacity: 6
        # *   Capacity of ecs.c5.xlarge: 4
        # 
        # To meet the expected capacity requirement, Auto Scaling must create and add two ecs.c5.xlarge instances.
        # 
        # > The capacity of the scaling group cannot exceed the sum of the maximum number of instances that is specified by the MaxSize parameter and the maximum weight of the instance type.
        # 
        # Valid values of the WeightedCapacity parameter: 1 to 500.
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
        # Specifies whether to automatically create pay-as-you-go ECS instances to reach the required number of ECS instances when preemptible ECS instances cannot be created due to high prices or insufficient inventory of resources. This parameter takes effect only if you set `MultiAZPolicy` in the `CreateScalingGroup` operation to `COST_OPTIMIZED`. Valid values:
        # 
        # *   true
        # *   false
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. When the number of pay-as-you-go instances drops below the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        # 
        # If you set `MultiAZPolicy` to `COMPOSABLE`, the default value is 0.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of additional pay-as-you-go instances beyond the minimum required by `OnDemandBaseCapacity` in the scaling group. Valid values: 0 to 100
        # 
        # If you set `MultiAZPolicy` to `COMPOSABLE`, the default value is 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The price comparison mode. Valid values:
        # 
        # *   PricePerUnit: compares prices based on capacity.
        # 
        #     The capacity of instances in a scaling group is determined by the weights of the instance types used. If no weight is specified, the default weight is 1, which specifies that each instance in the scaling group has a capacity of 1.
        # 
        # *   PricePerVCpu: compares prices based on the price per vCPU.
        # 
        # Default value: PricePerUnit.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to replace pay-as-you-go instances with preemptible instances. If you specify `CompensateWithOnDemand`, it may result in a higher percentage of pay-as-you-go instances compared to the value of `OnDemandPercentageAboveBaseCapacity`. In this case, Auto Scaling will try to deploy preemptible instances to replace the surplus pay-as-you-go instances. When `CompensateWithOnDemand` is specified, Auto Scaling creates pay-as-you-go instances if there are not enough preemptible instance types. To avoid keeping these pay-as-you-go ECS instances for long periods, Auto Scaling tries to replace them with preemptible instances as soon as enough of preemptible instance types become available. Valid values:
        # 
        # *   true
        # *   false
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

