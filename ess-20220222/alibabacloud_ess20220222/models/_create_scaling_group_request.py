# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class CreateScalingGroupRequest(DaraModel):
    def __init__(
        self,
        alb_server_groups: List[main_models.CreateScalingGroupRequestAlbServerGroups] = None,
        allocation_strategy: str = None,
        auto_rebalance: bool = None,
        az_balance: bool = None,
        balance_mode: str = None,
        capacity_options: main_models.CreateScalingGroupRequestCapacityOptions = None,
        client_token: str = None,
        compensate_with_on_demand: bool = None,
        container_group_id: str = None,
        custom_policy_arn: str = None,
        dbinstance_ids: str = None,
        dbinstances: List[main_models.CreateScalingGroupRequestDBInstances] = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        group_deletion_protection: bool = None,
        group_type: str = None,
        health_check_type: str = None,
        health_check_types: List[str] = None,
        instance_id: str = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.CreateScalingGroupRequestLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        lifecycle_hooks: List[main_models.CreateScalingGroupRequestLifecycleHooks] = None,
        load_balancer_configs: List[main_models.CreateScalingGroupRequestLoadBalancerConfigs] = None,
        load_balancer_ids: str = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        removal_policies: List[str] = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        scaling_group_name: str = None,
        scaling_policy: str = None,
        server_groups: List[main_models.CreateScalingGroupRequestServerGroups] = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        stop_instance_timeout: int = None,
        sync_alarm_rule_to_cms: bool = None,
        tags: List[main_models.CreateScalingGroupRequestTags] = None,
        vserver_groups: List[main_models.CreateScalingGroupRequestVServerGroups] = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        zone_shift_policy: main_models.CreateScalingGroupRequestZoneShiftPolicy = None,
    ):
        # The collection of information about the ALB server groups.
        self.alb_server_groups = alb_server_groups
        # The capacity allocation policy, which determines how the scaling group selects available instance types to meet the capacity requirements. The capacity distribution policy applies to both pay-as-you-go and spot capacities. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:
        # 
        # - priority: Creates instances based on the order of the configured instance types.
        # - lowestPrice: Creates instances based on the unit price per vCPU of the instance types in ascending order.
        # 
        # Default value: priority.
        self.allocation_strategy = allocation_strategy
        # Specifies whether to enable automatic balancing for the scaling group. This parameter takes effect only when BalancedOnly is enabled for the zone-balanced scaling group. Valid values:
        # - false: Does not enable automatic balancing for the scaling group.
        # - true: Enables automatic balancing for the scaling group. The scaling group automatically detects the capacity across zones. When the capacity is unbalanced across zones, the scaling group proactively scales out or in to rebalance the capacity across zones.
        # 
        # Default value: false.
        self.auto_rebalance = auto_rebalance
        # Specifies whether the capacity of the scaling group is evenly distributed across multiple zones. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:
        # 
        # - true: The capacity of the scaling group is evenly distributed across multiple zones.
        # - false: The capacity of the scaling group is not evenly distributed across multiple zones.
        # 
        # > If the MultiAZPolicy parameter is set to COMPOSABLE and the AzBalance parameter is set to true, the effect is the same as when the MultiAZPolicy parameter is set to BALANCE.
        # 
        # Default value: false.
        self.az_balance = az_balance
        # The zone balancing mode. This parameter takes effect only when the zone balancing mode is enabled. Valid values:
        #  
        # - BalancedBestEffort: When resource creation fails in a zone, the system falls back to other zones to ensure best-effort delivery of resources.
        # 
        # - BalancedOnly: When resource creation fails in a zone, the system does not fall back to other zones. The scale-out activity partially succeeds to avoid excessive imbalance of resources across different zones.
        # 
        # Default value: BalancedBestEffort.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can only contain ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to automatically attempt to create pay-as-you-go instances to meet the required number of ECS instances when the MultiAZPolicy parameter is set to COST_OPTIMIZED and sufficient spot instances cannot be created due to price or inventory reasons. Valid values:
        # 
        # - true: allows the creation.
        # - false: does not allow the creation.
        # 
        # Default value: true.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The ECI instance ID, which is the container group ID.
        self.container_group_id = container_group_id
        # The ARN of the Function Compute function for the custom scale-in policy. This parameter takes effect only when the first removal policy configured in RemovalPolicies is CustomPolicy.
        self.custom_policy_arn = custom_policy_arn
        # The IDs of the ApsaraDB RDS instances. The value can be a JSON array that contains multiple ApsaraDB RDS instance IDs. Separate multiple IDs with commas (,). 
        # 
        # <props="china">The maximum number of ApsaraDB RDS instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of ApsaraDB RDS instances that can be associated with a scaling group**.
        # 
        # <props="intl">The maximum number of ApsaraDB RDS instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of ApsaraDB RDS instances that can be associated with a scaling group**.
        # 
        # <props="partner">The maximum number of ApsaraDB RDS instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to Quota Center to check the quota for the **maximum number of ApsaraDB RDS instances that can be associated with a scaling group**.
        self.dbinstance_ids = dbinstance_ids
        # The list of databases associated with the scaling group.
        self.dbinstances = dbinstances
        # The cooldown time after a scaling activity (adding or removing instances) is completed. Valid values: 0 to 86400. Unit: seconds.
        # 
        # During the cooldown time, the scaling group does not execute other scaling activities. This parameter takes effect only for scaling activities triggered by CloudMonitor event-triggered tasks.  
        # 
        # Default value: 300.
        self.default_cooldown = default_cooldown
        # The expected number of instances in the scaling group. The scaling group automatically maintains the number of instances at the expected number. The value cannot be greater than MaxSize or less than MinSize.
        self.desired_capacity = desired_capacity
        # Specifies whether to enable deletion protection for the scaling group. Valid values:
        # 
        # - true: enables deletion protection for the scaling group. In this case, the scaling group cannot be deleted.
        # - false: disables deletion protection for the scaling group.
        # 
        # Default value: false.
        self.group_deletion_protection = group_deletion_protection
        # The type of instances managed by the scaling group. Valid values:
        # 
        # - ECS: the scaling group manages ECS instances.
        # 
        # - ECI: the scaling group manages ECI instances.
        # 
        # Default value: ECS.
        self.group_type = group_type
        # The health check type of the scaling group. Valid values:
        # 
        # - NONE: disables health checks.
        # - ECS: performs health checks on instances in the scaling group. This value is used to enable instance health checks for both ECS and ECI scaling groups.
        # - LOAD_BALANCER: determines the health status of instances based on the health check results of the load balancer. CLB is not supported.
        # 
        # 
        # Default value: ECS.
        # 
        # > If you want to enable both instance health checks and load balancer health checks, use the `HealthCheckTypes` parameter.
        self.health_check_type = health_check_type
        # The health check modes of the scaling group.
        # > You can set multiple values for this parameter to enable multiple health check options. If the HealthCheckType parameter is specified, this parameter is ignored.
        self.health_check_types = health_check_types
        # The ID of the instance. When you create a scaling group, Auto Scaling obtains the required configuration information from the specified instance and automatically creates a scaling configuration.
        self.instance_id = instance_id
        # The ID of the launch template. This parameter is used to specify the launch template from which the scaling group obtains launch configurations.
        self.launch_template_id = launch_template_id
        # The extended instance type information of the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the launch template. Valid values:
        # 
        # - A specific version number.
        # 
        # - Default: always uses the default version of the launch template.
        # 
        # - Latest: always uses the latest version of the launch template.
        self.launch_template_version = launch_template_version
        # The list of lifecycle hook information.
        self.lifecycle_hooks = lifecycle_hooks
        # The list of load balancing configurations.
        self.load_balancer_configs = load_balancer_configs
        # The IDs of the Classic Load Balancer (CLB) instances. The value can be a JSON array that contains multiple CLB instance IDs. Separate multiple IDs with commas (,).
        # 
        # <props="china">The maximum number of CLB instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of load balancing instances that can be associated with a scaling group**.
        # 
        # <props="intl">The maximum number of CLB instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of load balancing instances that can be associated with a scaling group**.
        # 
        # <props="partner">The maximum number of CLB instances that can be associated with a scaling group depends on your Auto Scaling usage. Go to Quota Center to check the quota for the **maximum number of load balancing instances that can be associated with a scaling group**.
        self.load_balancer_ids = load_balancer_ids
        # The maximum lifetime of an instance in the scaling group. Unit: seconds.
        # 
        # Valid values: [86400, Integer.maxValue].
        # 
        # Default value: null.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of instances in the scaling group. If the number of instances in the scaling group is greater than the value of MaxSize, Auto Scaling automatically removes instances. 
        # 
        # <props="china">The value range of MaxSize depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of instances in a scaling group**.
        # 
        # <props="intl">The value range of MaxSize depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the quota for the **maximum number of instances in a scaling group**.
        # 
        # <props="partner">The value range of MaxSize depends on your Auto Scaling usage. Go to Quota Center to check the quota for the **maximum number of instances in a scaling group**.
        # 
        # If the quota for the **maximum number of instances in a scaling group** is 2000, the value range of MaxSize is 0 to 2000.
        # 
        # This parameter is required.
        self.max_size = max_size
        # The minimum number of instances in the scaling group. If the number of instances in the scaling group is less than the value of MinSize, Auto Scaling automatically creates instances. 
        # 
        # > The value of MinSize must be less than or equal to the value of MaxSize.
        # 
        # This parameter is required.
        self.min_size = min_size
        # The multi-zone scaling policy for ECS instances in the scaling group. Valid values: 
        #          
        # - PRIORITY: the vSwitches specified by VSwitchIds are prioritized. Auto Scaling preferentially attempts to scale ECS instances in the zone where the highest-priority vSwitch resides. If the scaling fails, Auto Scaling automatically attempts to scale instances in the zone of the next highest-priority vSwitch.  
        # - COST_OPTIMIZED: during scale-out, Auto Scaling attempts to create ECS instances in ascending order of vCPU unit price. During scale-in, Auto Scaling attempts to remove ECS instances in descending order of vCPU unit price. If the scaling configuration settings specify multiple instance types that use the preemptible billing method, spot instances are preferentially created. You can use the CompensateWithOnDemand parameter to specify whether to automatically attempt to create pay-as-you-go instances when spot instances cannot be created due to insufficient inventory or other reasons. 
        # 
        #     > COST_OPTIMIZED takes effect only when the scaling configuration settings specify multiple instance types or use spot instances. 
        # - BALANCE: evenly distributes ECS instances across the zones specified for the scaling group. If the instances are unevenly allocated across zones due to insufficient inventory or other reasons, you can invoke the [RebalanceInstance](https://help.aliyun.com/document_detail/71516.html) operation to balance the resources.
        # 
        #     > If the `MultiAZPolicy` parameter is set to `BALANCE`, the effect is the same as when the `MultiAZPolicy` parameter is set to `COMPOSABLE` and the `AzBalance` parameter is set to `true`. 
        # - COMPOSABLE: a combined policy that allows you to combine the preceding multi-zone scaling policies for ECS instances based on your needs. You can also specify additional parameters to control the capacity of the scaling group in a more fine-grained manner.
        # 
        # Default value: PRIORITY.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than this value, pay-as-you-go instances are preferentially created.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances after the scaling group meets the minimum number of pay-as-you-go instances (OnDemandBaseCapacity). Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The filtering policy for the instance removal policy. Valid values:
        # 
        # - OldestInstance: removes the ECS instances that were added to the scaling group at the earliest point in time.
        # - NewestInstance: removes the ECS instances that were added to the scaling group at the latest point in time.
        # - OldestScalingConfiguration: removes the ECS instances that were created based on the earliest scaling configuration.
        # - CustomPolicy: removes ECS instances based on a custom scale-in policy function.
        # 
        # The scaling configuration mentioned in OldestScalingConfiguration refers to the instance configuration source in the scaling group, including scaling configurations and launch templates. CustomPolicy can only be set as the first removal policy. If you specify CustomPolicy, you must also specify the CustomPolicyARN parameter.
        # 
        # > The removal of ECS instances from a scaling group is also affected by the multi-zone scaling policy (MultiAZPolicy) of the scaling group. For more information, see [Configure a combined policy for removing instances](https://help.aliyun.com/document_detail/254822.html).
        self.removal_policies = removal_policies
        # The ID of the resource group to which the newly created scaling group belongs.
        # > Assigns the newly created scaling group to the specified resource group. If you do not specify this parameter, the scaling group belongs to the default resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The name of the scaling group. The name must be unique within a region.
        # 
        # It must be 2 to 64 characters in length. It must start with a digit, a letter, or a Chinese character, and can contain digits, underscores (_), hyphens (-), and periods (.).
        # 
        # Default value: the value of ScalingGroupId.
        self.scaling_group_name = scaling_group_name
        # The reclaim mode of the scaling group. Valid values: 
        #          
        # - recycle: sets the reclaim mode of the scaling group to shutdown and reclaim mode.  
        # - release: sets the reclaim mode of the scaling group to release mode.
        # - forcerelease: sets the reclaim mode of the scaling group to force release mode.
        #     > If you select forcerelease, the system forcibly releases instances in the `Running` state during scale-down activities. Forcibly releasing an instance is equivalent to a power-off operation, which erases temporary data in the memory and storage of the instance. The data cannot be recovered. Proceed with caution.
        # - forcerecycle: sets the reclaim mode of the scaling group to force shutdown and reclaim mode.
        #     > If you select forcerecycle, the system forcibly shuts down instances in the `Running` state during scale-down activities. Forcibly shutting down an instance is equivalent to a power-off operation, which erases temporary data in the memory and storage of the instance. The data cannot be recovered. Proceed with caution.
        # 
        # 
        # The ScalingPolicy parameter specifies the reclaim mode of the scaling group, but the specific action taken when an instance is removed from the scaling group is determined by the RemovePolicy parameter of RemoveInstances. For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The collection of information about the server groups.
        # > You cannot configure the same server group settings in both AlbServerGroups and ServerGroups at the same time.
        self.server_groups = server_groups
        # The spot capacity distribution policy. You can use this parameter to separately specify the distribution policy for spot capacity. This parameter takes effect only when the MultiAZPolicy parameter is set to COMPOSABLE. Valid values:
        # 
        # - priority: Creates instances based on the order of the configured instance types.
        # - lowestPrice: Creates instances based on the unit price per vCPU of the instance types in ascending order.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of available instance types. The scaling group evenly creates spot instances across multiple instance types with the lowest cost. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable the Auto Scaling policy to supplement spot instances. After this feature is enabled, when a system message indicating that a spot instance is to be reclaimed is received, the scaling group attempts to create a new instance to replace the spot instance to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The timeout period for waiting for an ECS instance to be stopped during the scale-in process. Unit: seconds.
        # Valid values: 30 to 240.
        # 
        # > - This parameter takes effect only in the scale-in process when ScalingPolicy is set to release.  
        # > - If this parameter is specified, the system waits for a maximum of the StopInstanceTimeout period for the instance to be stopped. After the timeout period elapses, the scale-in process continues regardless of whether the instance is stopped.  
        # > - If this parameter is not specified, the system waits for a long time for the instance to be stopped. The scale-in process continues only after the instance is stopped. If the instance fails to be stopped, the scale-in process is rolled back and the scale-in fails.
        self.stop_instance_timeout = stop_instance_timeout
        # > This parameter is not available.
        self.sync_alarm_rule_to_cms = sync_alarm_rule_to_cms
        # The collection of tag information for the scaling group.
        self.tags = tags
        # The collection of information about the virtual server groups associated with the scaling group.
        self.vserver_groups = vserver_groups
        # The ID of the vSwitch. After this parameter is specified, the network type of the scaling group is VPC.
        # 
        # > If neither VSwitchId nor VSwitchIds is specified for the scaling group, the network type of the scaling group is classic network by default.
        self.v_switch_id = v_switch_id
        # The IDs of one or more vSwitches. If you use the VSwitchIds parameter, the VSwitchId parameter is ignored. After this parameter is specified, the network type of the scaling group is VPC.
        # 
        # When you specify multiple vSwitches:
        # 
        # - The vSwitches must belong to the same VPC.
        # 
        # - The vSwitches can belong to different zones.
        # 
        # - The vSwitches are prioritized in ascending order of numbers. 1 indicates the highest priority. If instances cannot be created in the zone of a higher-priority vSwitch, the system automatically selects the next highest-priority vSwitch to create instances.
        # 
        # > If neither VSwitchId nor VSwitchIds is specified for the scaling group, the network type of the scaling group is classic network by default.
        self.v_switch_ids = v_switch_ids
        # The behavior policy of the scaling group during zone shift.
        self.zone_shift_policy = zone_shift_policy

    def validate(self):
        if self.alb_server_groups:
            for v1 in self.alb_server_groups:
                 if v1:
                    v1.validate()
        if self.capacity_options:
            self.capacity_options.validate()
        if self.dbinstances:
            for v1 in self.dbinstances:
                 if v1:
                    v1.validate()
        if self.launch_template_overrides:
            for v1 in self.launch_template_overrides:
                 if v1:
                    v1.validate()
        if self.lifecycle_hooks:
            for v1 in self.lifecycle_hooks:
                 if v1:
                    v1.validate()
        if self.load_balancer_configs:
            for v1 in self.load_balancer_configs:
                 if v1:
                    v1.validate()
        if self.server_groups:
            for v1 in self.server_groups:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.vserver_groups:
            for v1 in self.vserver_groups:
                 if v1:
                    v1.validate()
        if self.zone_shift_policy:
            self.zone_shift_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AlbServerGroups'] = []
        if self.alb_server_groups is not None:
            for k1 in self.alb_server_groups:
                result['AlbServerGroups'].append(k1.to_map() if k1 else None)

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

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

        if self.container_group_id is not None:
            result['ContainerGroupId'] = self.container_group_id

        if self.custom_policy_arn is not None:
            result['CustomPolicyARN'] = self.custom_policy_arn

        if self.dbinstance_ids is not None:
            result['DBInstanceIds'] = self.dbinstance_ids

        result['DBInstances'] = []
        if self.dbinstances is not None:
            for k1 in self.dbinstances:
                result['DBInstances'].append(k1.to_map() if k1 else None)

        if self.default_cooldown is not None:
            result['DefaultCooldown'] = self.default_cooldown

        if self.desired_capacity is not None:
            result['DesiredCapacity'] = self.desired_capacity

        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_types is not None:
            result['HealthCheckTypes'] = self.health_check_types

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        result['LifecycleHooks'] = []
        if self.lifecycle_hooks is not None:
            for k1 in self.lifecycle_hooks:
                result['LifecycleHooks'].append(k1.to_map() if k1 else None)

        result['LoadBalancerConfigs'] = []
        if self.load_balancer_configs is not None:
            for k1 in self.load_balancer_configs:
                result['LoadBalancerConfigs'].append(k1.to_map() if k1 else None)

        if self.load_balancer_ids is not None:
            result['LoadBalancerIds'] = self.load_balancer_ids

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

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.scaling_group_name is not None:
            result['ScalingGroupName'] = self.scaling_group_name

        if self.scaling_policy is not None:
            result['ScalingPolicy'] = self.scaling_policy

        result['ServerGroups'] = []
        if self.server_groups is not None:
            for k1 in self.server_groups:
                result['ServerGroups'].append(k1.to_map() if k1 else None)

        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy

        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.stop_instance_timeout is not None:
            result['StopInstanceTimeout'] = self.stop_instance_timeout

        if self.sync_alarm_rule_to_cms is not None:
            result['SyncAlarmRuleToCms'] = self.sync_alarm_rule_to_cms

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k1 in self.vserver_groups:
                result['VServerGroups'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.zone_shift_policy is not None:
            result['ZoneShiftPolicy'] = self.zone_shift_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k1 in m.get('AlbServerGroups'):
                temp_model = main_models.CreateScalingGroupRequestAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k1))

        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        if m.get('AutoRebalance') is not None:
            self.auto_rebalance = m.get('AutoRebalance')

        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')

        if m.get('BalanceMode') is not None:
            self.balance_mode = m.get('BalanceMode')

        if m.get('CapacityOptions') is not None:
            temp_model = main_models.CreateScalingGroupRequestCapacityOptions()
            self.capacity_options = temp_model.from_map(m.get('CapacityOptions'))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

        if m.get('ContainerGroupId') is not None:
            self.container_group_id = m.get('ContainerGroupId')

        if m.get('CustomPolicyARN') is not None:
            self.custom_policy_arn = m.get('CustomPolicyARN')

        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')

        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k1 in m.get('DBInstances'):
                temp_model = main_models.CreateScalingGroupRequestDBInstances()
                self.dbinstances.append(temp_model.from_map(k1))

        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckTypes') is not None:
            self.health_check_types = m.get('HealthCheckTypes')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.CreateScalingGroupRequestLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        self.lifecycle_hooks = []
        if m.get('LifecycleHooks') is not None:
            for k1 in m.get('LifecycleHooks'):
                temp_model = main_models.CreateScalingGroupRequestLifecycleHooks()
                self.lifecycle_hooks.append(temp_model.from_map(k1))

        self.load_balancer_configs = []
        if m.get('LoadBalancerConfigs') is not None:
            for k1 in m.get('LoadBalancerConfigs'):
                temp_model = main_models.CreateScalingGroupRequestLoadBalancerConfigs()
                self.load_balancer_configs.append(temp_model.from_map(k1))

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')

        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')

        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k1 in m.get('ServerGroups'):
                temp_model = main_models.CreateScalingGroupRequestServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')

        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('StopInstanceTimeout') is not None:
            self.stop_instance_timeout = m.get('StopInstanceTimeout')

        if m.get('SyncAlarmRuleToCms') is not None:
            self.sync_alarm_rule_to_cms = m.get('SyncAlarmRuleToCms')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateScalingGroupRequestTags()
                self.tags.append(temp_model.from_map(k1))

        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k1 in m.get('VServerGroups'):
                temp_model = main_models.CreateScalingGroupRequestVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('ZoneShiftPolicy') is not None:
            temp_model = main_models.CreateScalingGroupRequestZoneShiftPolicy()
            self.zone_shift_policy = temp_model.from_map(m.get('ZoneShiftPolicy'))

        return self

class CreateScalingGroupRequestZoneShiftPolicy(DaraModel):
    def __init__(
        self,
        impaired_zone_health_check_behavior: str = None,
        scale_in_blocked_rule_types: List[str] = None,
        scale_out_in_healthy_zones_only: bool = None,
    ):
        # The health check behavior in impaired zones. Valid values: 
        # 
        # - ReplaceUnhealthy: Replaces unhealthy instances in all zones normally. 
        # - IgnoreUnhealthy: Does not replace unhealthy instances in impaired zones. Healthy zones are not affected. 
        # 
        # Default value: ReplaceUnhealthy.
        self.impaired_zone_health_check_behavior = impaired_zone_health_check_behavior
        # Blocks scale-in triggered by specified types of scaling rules. The blocking scope applies to all zones under the scaling group, not just the impaired zones. This prevents false scale-in caused by fake improvements in monitoring metrics due to unreachable instances in impaired zones. Valid values: 
        # 
        # - StepScalingRule: Blocks scale-in triggered by step scaling rules. 
        # - TargetTrackingScalingRule: Blocks scale-in triggered by target tracking scaling rules. 
        # - None: Does not block. 
        # 
        # Default value: None.
        self.scale_in_blocked_rule_types = scale_in_blocked_rule_types
        # Specifies whether scale-out creates instances only in healthy zones during zone shift. Valid values: 
        # 
        # - true: Scale-out creates instances only in healthy zones and skips impaired zones. 
        # - false: Scale-out is not restricted by zone and can create instances in any zone of the scaling group. 
        # 
        # Default value: false.
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

class CreateScalingGroupRequestVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.CreateScalingGroupRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the Classic Load Balancer (CLB) instance to which the virtual server group belongs.
        self.load_balancer_id = load_balancer_id
        # The attributes of the backend server group.
        self.vserver_group_attributes = vserver_group_attributes

    def validate(self):
        if self.vserver_group_attributes:
            for v1 in self.vserver_group_attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        result['VServerGroupAttributes'] = []
        if self.vserver_group_attributes is not None:
            for k1 in self.vserver_group_attributes:
                result['VServerGroupAttributes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        self.vserver_group_attributes = []
        if m.get('VServerGroupAttributes') is not None:
            for k1 in m.get('VServerGroupAttributes'):
                temp_model = main_models.CreateScalingGroupRequestVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k1))

        return self

class CreateScalingGroupRequestVServerGroupsVServerGroupAttributes(DaraModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        # The port number used by the instance after Auto Scaling adds the instance to the virtual server group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the virtual server group.
        self.vserver_group_id = vserver_group_id
        # The weight of the instance as a backend server after Auto Scaling adds the instance to the virtual server group. A higher weight indicates that more access requests are allocated to the instance. If the weight is 0, the instance does not receive access requests. Valid values: 0 to 100.
        # 
        # Default value: 50.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.vserver_group_id is not None:
            result['VServerGroupId'] = self.vserver_group_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('VServerGroupId') is not None:
            self.vserver_group_id = m.get('VServerGroupId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateScalingGroupRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        propagate: bool = None,
        value: str = None,
    ):
        # The tag key of the scaling group.
        self.key = key
        # Specifies whether the tag is a propagatable tag. Valid values:
        # - true: tags on the scaling group are propagated only to newly created instances, not to existing instances in the scaling group.
        # - false: tags on the scaling group are not propagated to instances.
        # 
        # Default value: false.
        self.propagate = propagate
        # The tag value of the scaling group.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.propagate is not None:
            result['Propagate'] = self.propagate

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Propagate') is not None:
            self.propagate = m.get('Propagate')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateScalingGroupRequestServerGroups(DaraModel):
    def __init__(
        self,
        port: int = None,
        server_group_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The port number used by the instance after Auto Scaling adds the instance to the server group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # - ALB: Application Load Balancer (ALB).
        # - NLB: Network Load Balancer (NLB).
        # - GWLB: Gateway Load Balancer (GWLB).
        self.type = type
        # The weight of the instance as a backend server after Auto Scaling adds the instance to the server group. Valid values: 0 to 100.
        # 
        # A higher weight specifies that more access requests are allocated to the instance. If the weight is 0, the instance does not receive access requests.
        # 
        # > This parameter is required for ALB and NLB. You cannot configure this parameter for GWLB.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.server_group_id is not None:
            result['ServerGroupId'] = self.server_group_id

        if self.type is not None:
            result['Type'] = self.type

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('ServerGroupId') is not None:
            self.server_group_id = m.get('ServerGroupId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateScalingGroupRequestLoadBalancerConfigs(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        weight: int = None,
    ):
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The weight of the instance as a backend server after Auto Scaling adds the instance to the CLB server group. A higher weight specifies that more requests are distributed to the instance. If the weight is 0, the instance does not receive requests. Valid values: 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

class CreateScalingGroupRequestLifecycleHooks(DaraModel):
    def __init__(
        self,
        default_result: str = None,
        heartbeat_timeout: int = None,
        lifecycle_hook_name: str = None,
        lifecycle_transition: str = None,
        notification_arn: str = None,
        notification_metadata: str = None,
    ):
        # The action to be performed after the wait state ends. Valid values:
        # 
        # - CONTINUE: continues the response to the scale-out activity or continues the response to the scale-down activity.
        # 
        # - ABANDON: directly releases the instances created by the scale-out activity or directly removes the instances in the scale-down activity from the scaling group.
        # 
        # When a scale-down activity (SCALE_IN) occurs in the scaling group and triggers multiple lifecycle hooks, if the wait state triggered by a lifecycle hook whose DefaultResult is ABANDON ends, the other corresponding wait states end in advance. In other cases, the next action is subject to the next action of the last wait state that ends.
        # 
        # Default value: CONTINUE.
        self.default_result = default_result
        # The wait time set by the lifecycle hook for the scaling group activity. After the wait state times out, the next action is performed. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call RecordLifecycleActionHeartbeat to extend the wait time of the instance, or call CompleteLifecycleAction to end the wait state of the scaling activity in advance.
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The name of the lifecycle hook. The name cannot be modified after it is specified. If you do not specify this parameter, the default value is the same as the lifecycle hook ID.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The type of scaling activity to which the lifecycle hook applies. Valid values:
        # 
        # - SCALE_OUT: scale-out activities of the scaling group.
        # 
        # - SCALE_IN: scale-down activities of the scaling group.
        # 
        # > If you specify a lifecycle hook for the scaling group, this parameter is required, and other related parameters are optional.
        self.lifecycle_transition = lifecycle_transition
        # The identifier of the notification recipient for the lifecycle hook. Simple Message Queue (formerly MNS) queues or topics are supported. The parameter value format is acs:ess:{region}:{account-id}:{resource-relative-id}.
        # 
        # - region: the region where the scaling group resides.
        # 
        # - account-id: the Alibaba Cloud account ID.
        # 
        # Examples:
        # 
        # - Simple Message Queue (formerly MNS) queue: acs:ess:{region}:{account-id}:queue/{queuename}.
        # 
        # - Simple Message Queue (formerly MNS) topic: acs:ess:{region}:{account-id}:topic/{topicname}.
        self.notification_arn = notification_arn
        # The fixed string information for the wait state of the scaling activity. The value cannot exceed 4,096 characters in length. Each time Auto Scaling pushes a message to the notification recipient, it also sends the predefined value of the NotificationMetadata parameter to help you manage and mark different types of notification information. The NotificationMetadata parameter takes effect only when you also specify the NotificationArn parameter.
        self.notification_metadata = notification_metadata

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_result is not None:
            result['DefaultResult'] = self.default_result

        if self.heartbeat_timeout is not None:
            result['HeartbeatTimeout'] = self.heartbeat_timeout

        if self.lifecycle_hook_name is not None:
            result['LifecycleHookName'] = self.lifecycle_hook_name

        if self.lifecycle_transition is not None:
            result['LifecycleTransition'] = self.lifecycle_transition

        if self.notification_arn is not None:
            result['NotificationArn'] = self.notification_arn

        if self.notification_metadata is not None:
            result['NotificationMetadata'] = self.notification_metadata

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultResult') is not None:
            self.default_result = m.get('DefaultResult')

        if m.get('HeartbeatTimeout') is not None:
            self.heartbeat_timeout = m.get('HeartbeatTimeout')

        if m.get('LifecycleHookName') is not None:
            self.lifecycle_hook_name = m.get('LifecycleHookName')

        if m.get('LifecycleTransition') is not None:
            self.lifecycle_transition = m.get('LifecycleTransition')

        if m.get('NotificationArn') is not None:
            self.notification_arn = m.get('NotificationArn')

        if m.get('NotificationMetadata') is not None:
            self.notification_metadata = m.get('NotificationMetadata')

        return self

class CreateScalingGroupRequestLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        weighted_capacity: int = None,
    ):
        # If you want the scaling group to scale based on the capacity of the instance type, specify both this parameter and LaunchTemplateOverrides.WeightedCapacity.
        # 
        # This parameter is used to specify the instance type and overrides the instance type in the launch template.
        # 
        # > This parameter takes effect only when the LaunchTemplateId parameter is specified.
        # 
        # Valid values of InstanceType: available ECS instance types.
        self.instance_type = instance_type
        # This parameter is used to specify the maximum price for the overridden instance type (namely, `LaunchTemplateOverride.InstanceType`) in the launch template.
        # > This parameter takes effect only when the `LaunchTemplateId` parameter is specified.
        self.spot_price_limit = spot_price_limit
        # If you want the scaling group to scale based on the capacity of the instance type, specify this parameter after you specify LaunchTemplateOverrides.InstanceType.
        # 
        # This parameter is used to specify the weight of the instance type, which indicates the capacity represented by a single instance of the instance type in the scaling group. A larger weight indicates that fewer instances of this instance type are required to meet the expected capacity.
        # 
        # Because performance metrics such as the number of vCPUs and memory size vary among instance types, you can configure different weights for different instance types based on your needs.
        # 
        # Example:
        # 
        # - Current capacity: 0.
        # 
        # - Expected capacity: 6.
        # 
        # - Capacity of the ecs.c5.xlarge instance type: 4.
        # 
        # To meet the expected capacity, the scaling group scales out two ecs.c5.xlarge instances for you.
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

class CreateScalingGroupRequestDBInstances(DaraModel):
    def __init__(
        self,
        attach_mode: str = None,
        dbinstance_id: str = None,
        type: str = None,
    ):
        # The association mode between the scaling group and the database. Valid values:
        # - SecurityIp: Modifies the IP whitelist mode by automatically adding scaled-out instances to the IP whitelist of the database. Only ApsaraDB RDS databases are supported.
        # - SecurityGroup: Uses the security group mode by adding the security group of the scaling configuration to the security group whitelist of the database to allow instances in the security group to access the database.
        self.attach_mode = attach_mode
        # The database instance ID.
        self.dbinstance_id = dbinstance_id
        # The type of the database. Valid values:
        # - RDS
        # - Redis
        # - MongoDB
        # 
        # Default value: RDS.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attach_mode is not None:
            result['AttachMode'] = self.attach_mode

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachMode') is not None:
            self.attach_mode = m.get('AttachMode')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateScalingGroupRequestCapacityOptions(DaraModel):
    def __init__(
        self,
        compensate_with_on_demand: bool = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        price_comparison_mode: str = None,
        spot_auto_replace_on_demand: bool = None,
    ):
        # Specifies whether to allow the system to automatically attempt to create pay-as-you-go instances to meet the required number of ECS instances when the MultiAZPolicy parameter is set to COST_OPTIMIZED and sufficient spot instances cannot be created due to price or inventory reasons. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed.
        # 
        # Default value: true.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. When the number of pay-as-you-go instances in the scaling group is less than this value, the system preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        # 
        # When the MultiAZPolicy parameter is set to COMPOSABLE, the default value is 0.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances after the scaling group meets the minimum number of pay-as-you-go instances specified by OnDemandBaseCapacity. Valid values: 0 to 100.
        # 
        # When the MultiAZPolicy parameter is set to COMPOSABLE, the default value is 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The price comparison mode for the cost optimization policy of the scaling group. Valid values:
        # - PricePerUnit: Compares prices based on the price per unit of capacity.
        # 
        #   The capacity of an instance in the scaling group is equal to the weight set for the instance type. The default weight is 1, which means one ECS instance occupies a capacity of 1.
        # 
        # - PricePerVCpu: Compares prices based on the price per vCPU.
        # 
        # Default value: PricePerUnit.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to attempt to use spot instances to replace pay-as-you-go capacity when CompensateWithOnDemand is enabled and the proportion of pay-as-you-go instances exceeds the OnDemandPercentageAboveBaseCapacity value. In common scenarios where CompensateWithOnDemand downgrades spot instances to pay-as-you-go instances due to spot inventory or price reasons, this parameter attempts to use spot instances to replace the excess pay-as-you-go capacity to avoid long-term existence of pay-as-you-go instances. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed.
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

class CreateScalingGroupRequestAlbServerGroups(DaraModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        # The ID of the ALB server group.
        # 
        # A scaling group supports a limited number of associated ALB server groups. To view or manually apply for a quota increase, go to the [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.alb_server_group_id = alb_server_group_id
        # The port number used by the instance after Auto Scaling adds the instance to the ALB server group. Valid values: 1 to 65535.
        self.port = port
        # The weight of the instance as a backend server after Auto Scaling adds the instance to the ALB server group. A higher weight specifies that more requests are distributed to the instance. If the weight is 0, the instance does not receive requests. Valid values: 0 to 100.
        self.weight = weight

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alb_server_group_id is not None:
            result['AlbServerGroupId'] = self.alb_server_group_id

        if self.port is not None:
            result['Port'] = self.port

        if self.weight is not None:
            result['Weight'] = self.weight

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbServerGroupId') is not None:
            self.alb_server_group_id = m.get('AlbServerGroupId')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Weight') is not None:
            self.weight = m.get('Weight')

        return self

