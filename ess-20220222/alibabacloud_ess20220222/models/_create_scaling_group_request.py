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
    ):
        # The Application Load Balancer (ALB) server groups to associate with the scaling group.
        self.alb_server_groups = alb_server_groups
        # The capacity allocation policy determines how the scaling group selects available instance types to meet capacity requirements. The policy applies to both on-demand and preemptible capacity (effective only when the `MultiAZPolicy` parameter is set to `COMPOSABLE`). Valid values:
        # 
        # - priority: Creates instances in the order of the configured instance types.
        # 
        # - lowestPrice: Create instances based on the price per vCPU of instance types, from lowest to highest.
        # 
        # Default value: priority.
        self.allocation_strategy = allocation_strategy
        # Specifies whether to enable automatic balancing for the scaling group. This setting takes effect only when BalancedOnly is enabled for a scaling group that is balanced across availability zones. Value range:
        # 
        # - false: Does not enable automatic balancing for the scaling group.
        # 
        # - true: When automatic balancing for the scaling group is enabled, the scaling group automatically detects the capacity across availability zones. If the capacity is imbalanced, the scaling group proactively performs scaling across availability zones to rebalance the capacity.
        # 
        # Default value: false.
        self.auto_rebalance = auto_rebalance
        # Specifies whether to evenly distribute the capacity of the scaling group across multiple availability zones. This parameter is valid only when `MultiAZPolicy` is set to `COMPOSABLE`. Valid values:
        # 
        # - `true`: The capacity of the scaling group is evenly distributed across multiple availability zones.
        # 
        # - `false`: The capacity of the scaling group is not evenly distributed across multiple availability zones.
        # 
        # > If `MultiAZPolicy` is set to `COMPOSABLE` and `AzBalance` is set to `true`, the effect is the same as setting `MultiAZPolicy` to `BALANCE`.
        # 
        # Default value: `false`.
        self.az_balance = az_balance
        # The zone balancing mode is effective only when enabled. Valid values:
        # 
        # - BalancedBestEffort: If a resource fails to be created in an availability zone, the system falls back to other availability zones to ensure best-effort delivery.
        # 
        # - BalancedOnly:
        #   If resource creation fails in an availability zone, the system does not fall back to other availability zones. The scaling activity is partially successful, which prevents an excessive imbalance of resources across different availability zones.
        # 
        # Default value: BalancedBestEffort.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # A client-generated token to ensure the idempotence of the request.
        # 
        # The token must be unique across requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # This parameter is effective only when `MultiAZPolicy` is set to `COST_OPTIMIZED`. If `true`, Auto Scaling creates on-demand instances to meet capacity requirements when spot instances are unavailable due to price or inventory. Valid values:
        # 
        # - `true`: Yes.
        # 
        # - `false`: No.
        # 
        # Default value: `true`.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The ID of the ECI instance, also known as the container group ID.
        self.container_group_id = container_group_id
        # The ARN of the custom scale-in policy function. This parameter is valid only when the first removal policy in `RemovalPolicies` is `CustomPolicy`.
        self.custom_policy_arn = custom_policy_arn
        # A JSON array of RDS instance IDs.
        # 
        # <props="china">
        # 
        # The number of RDS instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of RDS instances that can be associated with a single scaling group**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The number of RDS instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of RDS instances that can be associated with a single scaling group**.
        # 
        # 
        # 
        # <props="partner">
        # 
        # The number of RDS instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to Quota Center to view the quota for **Maximum number of RDS instances that can be associated with a single scaling group**.
        self.dbinstance_ids = dbinstance_ids
        # The databases that are associated with the scaling group.
        self.dbinstances = dbinstances
        # The cooldown period, in seconds, after a scaling activity completes. Valid values: 0 to 86400.
        # 
        # During the cooldown period, the scaling group does not execute other scaling activities that are triggered by CloudMonitor alarm tasks.
        # 
        # Default value: 300.
        self.default_cooldown = default_cooldown
        # The desired number of instances in the scaling group. Auto Scaling automatically maintains this number of instances. The value must be less than or equal to `MaxSize` and greater than or equal to `MinSize`.
        self.desired_capacity = desired_capacity
        # Specifies whether to enable deletion protection for the scaling group. Valid values:
        # 
        # - `true`: Enables deletion protection. The scaling group cannot be deleted.
        # 
        # - `false`: Disables deletion protection.
        # 
        # Default value: `false`.
        self.group_deletion_protection = group_deletion_protection
        # The type of instances managed by the scaling group. Valid values:
        # 
        # - `ECS`: The scaling group manages ECS instances.
        # 
        # - `ECI`: The scaling group manages ECI instances.
        # 
        # Default value: `ECS`.
        self.group_type = group_type
        # The health check method for the scaling group. Valid values:
        # 
        # - `NONE`: No health checks are performed.
        # 
        # - `ECS`: Health checks are performed on instances in the scaling group. This value enables health checks for scaling groups of both the ECS and ECI types.
        # 
        # - `LOAD_BALANCER`: The instance health status is based on health check results from the attached load balancer. This option does not support Classic Load Balancer (CLB) instances.
        # 
        # Default value: `ECS`.
        # 
        # > To enable both instance health checks and load balancer health checks, use the `HealthCheckTypes` parameter.
        self.health_check_type = health_check_type
        # The health check methods for the scaling group.
        # 
        # > You can use this parameter to set multiple values and enable multiple health check options. If you set the `HealthCheckType` parameter, this parameter is ignored.
        self.health_check_types = health_check_types
        # The ID of an existing instance to use as a template. Auto Scaling uses this instance to create a new scaling configuration for the scaling group.
        self.instance_id = instance_id
        # The ID of the launch template that provides the configuration for the scaling group.
        self.launch_template_id = launch_template_id
        # The instance type information for extending the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the launch template. Valid values:
        # 
        # - A specific version number of the template.
        # 
        # - `Default`: Uses the default version of the template.
        # 
        # - `Latest`: Uses the latest version of the template.
        self.launch_template_version = launch_template_version
        # The list of lifecycle hooks.
        self.lifecycle_hooks = lifecycle_hooks
        # The load balancer configurations.
        self.load_balancer_configs = load_balancer_configs
        # A JSON array of Classic Load Balancer (CLB) instance IDs.
        # 
        # <props="china">
        # 
        # The number of CLB instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of load balancer instances that can be associated with a single scaling group**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The number of CLB instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of load balancer instances that can be associated with a single scaling group**.
        # 
        # 
        # 
        # <props="partner">
        # 
        # The number of CLB instances that you can associate with a single scaling group varies based on your Auto Scaling usage. Go to Quota Center to view the quota for **Maximum number of load balancer instances that can be associated with a single scaling group**.
        self.load_balancer_ids = load_balancer_ids
        # The maximum lifetime of an instance in the scaling group. Unit: seconds.
        # 
        # Value range: [86400, Integer.maxValue].
        # 
        # Default value: null.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of instances in the scaling group. If the total number of instances exceeds this value, Auto Scaling removes instances to meet this maximum.
        # 
        # <props="china">
        # 
        # The value range of `MaxSize` depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of instances per scaling group**.
        # 
        # 
        # 
        # <props="intl">
        # 
        # The value range of `MaxSize` depends on your Auto Scaling usage. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to view the quota for **Maximum number of instances per scaling group**.
        # 
        # 
        # 
        # <props="partner">
        # 
        # The value range of `MaxSize` depends on your Auto Scaling usage. Go to Quota Center to view the quota for **Maximum number of instances per scaling group**.
        # 
        # 
        # 
        # If the quota for **Maximum number of instances per scaling group** is 2,000, the value of `MaxSize` can range from 0 to 2,000.
        # 
        # This parameter is required.
        self.max_size = max_size
        # The minimum number of instances in the scaling group. If the total number of instances falls below this value, Auto Scaling adds instances to meet this minimum.
        # 
        # > The value of `MinSize` must be less than or equal to the value of `MaxSize`.
        # 
        # This parameter is required.
        self.min_size = min_size
        # The scaling policy for ECS instances in a multi-zone scaling group. Valid values:
        # 
        # - `PRIORITY`: Auto Scaling prioritizes the vSwitches specified in `VSwitchIds`. If an operation fails in a higher-priority availability zone, Auto Scaling automatically attempts it in the next-highest-priority zone.
        # 
        # - `COST_OPTIMIZED`: During scale-out, creates instances from the instance types with the lowest vCPU unit price. During scale-in, removes instances from the instance types with the highest vCPU unit price. If the scaling configuration includes multiple spot instance types, spot instances are prioritized for creation. You can use the `CompensateWithOnDemand` parameter to specify whether to automatically create on-demand instances when spot instances cannot be created due to reasons such as insufficient inventory.
        # 
        #   > The `COST_OPTIMIZED` policy takes effect only when the scaling configuration specifies multiple instance types or includes spot instances.
        # 
        # - `BALANCE`: Distributes ECS instances evenly across the specified availability zones in the scaling group. If the distribution of instances becomes uneven due to insufficient inventory, you can call the [RebalanceInstance](https://help.aliyun.com/document_detail/71516.html) API operation to rebalance the instances.
        # 
        #   > If `MultiAZPolicy` is set to `BALANCE`, the effect is the same as setting `MultiAZPolicy` to `COMPOSABLE` and `AzBalance` to `true`.
        # 
        # - `COMPOSABLE`: A composite policy that allows you to combine the preceding policies for multi-zone scaling groups as needed. You can also specify additional parameters to gain finer control over the capacity of your scaling group.
        # 
        # Default value: `PRIORITY`.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of on-demand instances required in the scaling group. Valid values: 0 to 1,000. If the number of on-demand instances is less than this value, Auto Scaling preferentially creates on-demand instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of on-demand instances among the excess instances after the minimum number of on-demand instances (`OnDemandBaseCapacity`) is met. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ID of the region where the scaling group resides.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance removal policies. Valid values:
        # 
        # - `OldestInstance`: Removes the ECS instance that was first added to the scaling group.
        # 
        # - `NewestInstance`: Removes the ECS instance that was most recently added to the scaling group.
        # 
        # - `OldestScalingConfiguration`: Removes the ECS instance that was created based on the earliest scaling configuration.
        # 
        # - `CustomPolicy`: Removes ECS instances based on a custom scale-in policy defined by a function.
        # 
        # The term `scaling configuration` in `OldestScalingConfiguration` refers to the source of instance configuration information, which includes both scaling configurations and launch templates. `CustomPolicy` can only be set as the first removal policy. If you specify `CustomPolicy`, you must also specify the `CustomPolicyARN` parameter.
        # 
        # > The removal of instances is also affected by the scaling group\\"s multi-AZ policy (`MultiAZPolicy`). For more information, see [Configure a combination of removal policies](https://help.aliyun.com/document_detail/254822.html).
        self.removal_policies = removal_policies
        # The ID of the resource group to which the new scaling group belongs.
        # 
        # > If you do not specify this parameter, the new scaling group is added to the default resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The name of the scaling group. The name must be unique within a region.
        # 
        # The name must be 2 to 64 characters in length. It must start with a letter, a digit, or a Chinese character and can contain digits, underscores (_), hyphens (-), and periods (.).
        # 
        # If you do not specify this parameter, the value of `ScalingGroupId` is used.
        self.scaling_group_name = scaling_group_name
        # The reclamation mode of the scaling group. Valid values:
        # 
        # - `recycle`: The reclamation mode is Economical Mode.
        # 
        # - `release`: The reclamation mode is Release Mode.
        # 
        # - `forcerelease`: The reclamation mode is Force Release Mode.
        # 
        #   > A forced release is equivalent to a power-off operation, which erases data in the memory and ephemeral storage of the instances. This data cannot be recovered. Use this option with caution.
        # 
        # - `forcerecycle`: The reclamation mode is Force Economical Mode.
        # 
        #   > A forced stop is equivalent to a power-off operation, which erases data in the memory and ephemeral storage of the instances. This data cannot be recovered. Use this option with caution.
        # 
        # `ScalingPolicy` specifies the reclamation mode of the scaling group. The specific action taken when an instance is removed from the scaling group is determined by the `RemovePolicy` parameter of the `RemoveInstances` operation. For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The load balancer server groups.
        # 
        # > You cannot specify the same server group in both `AlbServerGroups` and `ServerGroups`.
        self.server_groups = server_groups
        # The distribution strategy for spot capacity. You can use this parameter to specify a separate strategy for spot capacity (effective only when the `MultiAZPolicy` parameter is set to `COMPOSABLE`). Valid values:
        # 
        # - priority: Creates instances in the order of the configured instance types.
        # 
        # - lowestPrice: Creates instances in ascending order of the price per vCPU of the instance types.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of instance types to use. The scaling group creates spot instances in a balanced manner across the specified number of lowest-cost instance types. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # If set to `true`, Auto Scaling attempts to create a new instance to replace a spot instance that is about to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The timeout period for the system to wait for an ECS instance to be stopped during a scale-in event. Unit: seconds.
        # Valid values: 30 to 240.
        # 
        # > - This parameter takes effect only during scale-in events when `ScalingPolicy` is set to `release`.
        # >
        # > - If this parameter is set, the system waits for the specified `StopInstanceTimeout` period for the instance to be stopped. If the instance is not stopped after the timeout period, the scale-in process continues regardless of the instance status.
        # >
        # > - If this parameter is not set, the system waits for an extended period for the instance to be stopped. The scale-in process continues only after the instance is stopped. If the instance fails to stop, the scale-in process is rolled back, and the scale-in event fails.
        self.stop_instance_timeout = stop_instance_timeout
        # > This parameter is not yet available.
        self.sync_alarm_rule_to_cms = sync_alarm_rule_to_cms
        # The tags to apply to the scaling group.
        self.tags = tags
        # The vServer groups to associate with the scaling group.
        self.vserver_groups = vserver_groups
        # The ID of the vSwitch. If you specify this parameter, the network type of the scaling group is Virtual Private Cloud (VPC).
        # 
        # > If you do not specify the `VSwitchId` or `VSwitchIds` parameter, the network type of the scaling group defaults to classic network.
        self.v_switch_id = v_switch_id
        # The IDs of one or more vSwitches. If you specify this parameter, the `VSwitchId` parameter is ignored. If you specify this parameter, the network type of the scaling group is Virtual Private Cloud (VPC).
        # 
        # If you specify multiple vSwitches:
        # 
        # - They must belong to the same VPC.
        # 
        # - They can be in different availability zones.
        # 
        # - The vSwitches are prioritized based on their order in the list, with the first vSwitch having the highest priority. If an instance cannot be created in the availability zone of a higher-priority vSwitch, Auto Scaling automatically attempts to create the instance in the availability zone of the next-highest-priority vSwitch.
        # 
        # > If you do not specify the `VSwitchId` or `VSwitchIds` parameter, the network type of the scaling group defaults to classic network.
        self.v_switch_ids = v_switch_ids

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

        return self

class CreateScalingGroupRequestVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.CreateScalingGroupRequestVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the Classic Load Balancer (CLB) instance to which the vServer group belongs.
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
        # The port number used by an instance after it is added to the vServer group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # The weight of an instance as a backend server after the instance is added to the vServer group. The higher the weight, the more access requests are distributed to the instance. If the weight is 0, no access requests are distributed to the instance. Valid values: 0 to 100.
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
        # The key of the tag.
        self.key = key
        # Specifies whether the tag can be propagated. Valid values:
        # 
        # - `true`: The tag is propagated from the scaling group only to newly created instances, not to instances that are already running in the scaling group.
        # 
        # - `false`: The tag is not propagated from the scaling group to any instances.
        # 
        # Default value: `false`.
        self.propagate = propagate
        # The value of the tag.
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
        # The port number used by an instance after it is added to the server group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # - `ALB`: Application Load Balancer.
        # 
        # - `NLB`: Network Load Balancer.
        # 
        # - `GWLB`: Gateway Load Balancer.
        self.type = type
        # The weight of an instance as a backend server after the instance is added to the server group. Valid values: 0 to 100.
        # 
        # A higher weight indicates that more access requests are distributed to the instance. If the weight is 0, no access requests are distributed to the instance.
        # 
        # > This parameter is required for ALB and NLB server groups. You cannot set this parameter for GWLB server groups.
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
        # The weight of an instance as a backend server after the instance is added to the SLB server group. The higher the weight, the more access requests are distributed to the instance. If the weight is 0, no access requests are distributed to the instance. Valid values: 0 to 100.
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
        # The action to take after the wait state ends. Valid values:
        # 
        # - `CONTINUE`: Continues the scale-out or scale-in activity.
        # 
        # - `ABANDON`: Aborts the scale-out activity by releasing the created instances, or aborts the scale-in activity by keeping the instances in the scaling group.
        # 
        # If a scale-in (SCALE_IN) activity triggers multiple lifecycle hooks, and the `DefaultResult` of one of the lifecycle hooks is `ABANDON`, the wait state of the other lifecycle hooks ends prematurely. In other cases, the action is determined by the last lifecycle hook to complete.
        # 
        # Default value: `CONTINUE`.
        self.default_result = default_result
        # The wait time that is defined in the lifecycle hook for a scaling activity. After the wait time expires, the next action is performed. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call the `RecordLifecycleActionHeartbeat` operation to extend the wait time of an instance, or call the `CompleteLifecycleAction` operation to end the wait state of the scaling activity in advance.
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The name of the lifecycle hook. The name cannot be modified after it is specified. If you do not specify a name, the ID of the lifecycle hook is used.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The type of scaling activity to which the lifecycle hook applies. Valid values:
        # 
        # - `SCALE_OUT`: A scale-out activity.
        # 
        # - `SCALE_IN`: A scale-in activity.
        # 
        # > This parameter is required if you specify a lifecycle hook for the scaling group. Other related parameters are optional.
        self.lifecycle_transition = lifecycle_transition
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient for the lifecycle hook. Message Service (MNS) queues and topics are supported. The format is `acs:ess:{region}:{account-id}:{resource-relative-id}`.
        # 
        # - `region`: the region where the scaling group is located.
        # 
        # - `account-id`: the ID of your Alibaba Cloud account.
        # 
        # Examples:
        # 
        # - MNS queue: `acs:ess:{region}:{account-id}:queue/{queuename}`.
        # 
        # - MNS topic: `acs:ess:{region}:{account-id}:topic/{topicname}`.
        self.notification_arn = notification_arn
        # A fixed string of information for the wait state of a scaling activity. The value cannot exceed 4,096 characters in length. When Auto Scaling sends a message to the specified notification recipient, it includes the value of this parameter. This allows you to manage and categorize notifications. This parameter is valid only when you specify the `NotificationArn` parameter.
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
        # To enable the scaling group to scale based on instance type capacity, you must specify both this parameter and `LaunchTemplateOverrides.WeightedCapacity`.
        # 
        # This parameter specifies the instance type, which overrides the instance type specified in the launch template.
        # 
        # > This parameter takes effect only when the `LaunchTemplateId` parameter is specified.
        # 
        # Must be a valid ECS instance type.
        self.instance_type = instance_type
        # The maximum hourly price for the instance type specified in `LaunchTemplateOverride.InstanceType`.
        # 
        # > This parameter takes effect only when the `LaunchTemplateId` parameter is specified.
        self.spot_price_limit = spot_price_limit
        # To enable the scaling group to scale based on instance type capacity, you must specify this parameter after you specify `LaunchTemplateOverrides.InstanceType`.
        # 
        # This parameter specifies the weight of the instance type, which represents the capacity of a single instance of that type in the scaling group. A higher weight means that fewer instances of this type are needed to meet the desired capacity.
        # 
        # Because instance types have different performance metrics, such as the number of vCPUs and memory size, you can assign different weights to different instance types based on your requirements.
        # 
        # Example:
        # 
        # - Current capacity: 0.
        # 
        # - Desired capacity: 6.
        # 
        # - Capacity of ecs.c5.xlarge: 4.
        # 
        # To meet the desired capacity, the scaling group will create two ecs.c5.xlarge instances.
        # 
        # > During a scale-out activity, the capacity of the scaling group cannot exceed the sum of the maximum capacity (`MaxSize`) and the maximum weight of an instance type.
        # 
        # Valid values: 1 to 500.
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
        # The method that is used to associate the scaling group with the database. Valid values:
        # 
        # - `SecurityIp`: The IP address whitelist mode. This mode automatically adds the scaled-out instances to the IP address whitelist of the database. This mode is supported only by RDS databases.
        # 
        # - `SecurityGroup`: The security group mode. This mode adds the security group of the scaling configuration to the security group whitelist of the database. This allows instances in the security group to access the database.
        self.attach_mode = attach_mode
        # The ID of the database instance.
        self.dbinstance_id = dbinstance_id
        # The type of the database. Valid values:
        # 
        # - RDS
        # 
        # - Redis
        # 
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
        # When `MultiAZPolicy` is set to `COST_OPTIMIZED`, this parameter specifies whether to automatically create on-demand instances to meet capacity requirements when spot instances are unavailable due to price or inventory. Valid values:
        # 
        # - `true`: Yes.
        # 
        # - `false`: No.
        # 
        # Default value: `true`.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of on-demand instances required in the scaling group. When the number of on-demand instances in the scaling group is less than this value, the system preferentially creates on-demand instances. Valid values: 0 to 1,000.
        # 
        # When `MultiAZPolicy` is set to `COMPOSABLE`, the default value is 0.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of on-demand instances among the excess instances after the `OnDemandBaseCapacity` requirement is met. Valid values: 0 to 100.
        # 
        # When `MultiAZPolicy` is set to `COMPOSABLE`, the default value is 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The price comparison mode for the cost optimization strategy of the scaling group. Valid values:
        # 
        # - `PricePerUnit`: Compares prices based on per-unit capacity.
        # 
        #   The capacity of an instance in a scaling group is equal to the weight set for the instance type, with a default of 1, meaning one ECS instance equals one unit of capacity.
        # 
        # - `PricePerVCpu`: Compares prices based on per-vCPU price.
        # 
        # Default value: `PricePerUnit`.
        self.price_comparison_mode = price_comparison_mode
        # After you enable `CompensateWithOnDemand`, if the on-demand percentage exceeds the `OnDemandPercentageAboveBaseCapacity` ratio, the system attempts to replace on-demand capacity with spot capacity. A common scenario is when `CompensateWithOnDemand` leads to on-demand instances being created due to spot inventory or price issues. To avoid the prolonged existence of these on-demand instances, the system attempts to replace the excess on-demand capacity with spot instances. Valid values:
        # 
        # - `true`: Allows replacement.
        # 
        # - `false`: Does not allow replacement.
        # 
        # Default value: `false`.
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
        # A scaling group can be associated with a limited number of ALB server groups. To view or request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.alb_server_group_id = alb_server_group_id
        # The port number used by an instance after it is added to the ALB server group. Valid values: 1 to 65535.
        self.port = port
        # The weight of an instance as a backend server after the instance is added to the ALB server group. The higher the weight, the more access requests are distributed to the instance. If the weight is 0, no access requests are distributed to the instance. Valid values: 0 to 100.
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

