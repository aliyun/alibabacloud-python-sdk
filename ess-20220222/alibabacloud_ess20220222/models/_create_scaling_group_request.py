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
        # The Application Load Balancer (ALB) server groups.
        self.alb_server_groups = alb_server_groups
        # The allocation policy of instances. Auto Scaling selects instance types based on the allocation policy to create the required number of instances. The policy can be applied to pay-as-you-go instances and preemptible instances. This parameter takes effect only when you set the `MultiAZPolicy` parameter to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order of the instance types to create the required number of instances.
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
        # Specifies whether to evenly distribute instances in the scaling group across multiple zones. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you set `MultiAZPolicy` to `COMPOSABLE` and enable `AzBalance` to `true`, this setting has an equivalent effect to setting `MultiAZPolicy` to `BALANCE`.
        # 
        # Default value: false.
        self.az_balance = az_balance
        # The zone balancing mode. This mode takes effect only when the zone balancing mode is enabled. Valid values:
        # 
        # *   BalancedBestEffort: If a resource fails to be created in a zone, it is downgraded to another zone to ensure best-effort delivery of the resource.
        # *   BalancedOnly: If a resource fails to be created in a zone, it is not downgraded to another zone. The scale-out activity is partially successful to avoid excessive imbalance of resources in different zones.
        # 
        # Default value: BalancedBestEffort.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25965.html).
        self.client_token = client_token
        # Specifies whether to automatically create pay-as-you-go instances to meet the requirement on the number of ECS instances when the expected capacity of preemptible instances cannot be provided due to reasons such as cost-related issues and insufficient resources. This parameter is available only if you set the MultiAZPolicy parameter to COST_OPTIMIZED. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The ID of the elastic container instance.
        self.container_group_id = container_group_id
        # The Alibaba Cloud Resource Name (ARN) of the custom scale-in policy (Function). This parameter is available only if you specify CustomPolicy as the first step to remove instances.
        self.custom_policy_arn = custom_policy_arn
        # The IDs of the ApsaraDB RDS instances that you want to associate with the scaling group. The value can be a JSON array that contains multiple ApsaraDB RDS instance IDs. Separate multiple IDs with commas (,).
        # 
        # You can associate only a limited number of ApsaraDB RDS instances with a scaling group. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the maximum number of ApsaraDB RDS instances that you can associate with a scaling group.
        self.dbinstance_ids = dbinstance_ids
        # The databases that you want to attach to the scaling group.
        self.dbinstances = dbinstances
        # The cooldown period of the scaling group after a scaling activity is complete in the scaling group. Valid values: 0 to 86400. Unit: seconds.
        # 
        # During the cooldown period, Auto Scaling does not execute scaling activities that are triggered by CloudMonitor event-triggered tasks.
        # 
        # Default value: 300.
        self.default_cooldown = default_cooldown
        # The expected number of ECS instances in the scaling group. Auto Scaling automatically maintains the specified expected number of ECS instances. The DesiredCapacity value cannot be greater than the MaxSize value or less than the MinSize value.
        self.desired_capacity = desired_capacity
        # Specifies whether to enable deletion protection for the scaling group. Valid values:
        # 
        # *   true: enables deletion protection for the scaling group. This way, the scaling group cannot be deleted.
        # *   false: disables deletion protection for the scaling group.
        # 
        # Default value: false.
        self.group_deletion_protection = group_deletion_protection
        # The type of the instances that are managed by the scaling group. Valid values:
        # 
        # *   ECS: ECS instances.
        # *   ECI: elastic container instances.
        # 
        # Default value: ECS.
        self.group_type = group_type
        # The health check mode of the scaling group. Valid values:
        # 
        # *   NONE: Auto Scaling does not check the health status of instances.
        # *   ECS: Auto Scaling checks the health status of instances in the scaling group. If you want to enable instance health check, you can set the value to ECS, regardless of whether the scaling group is of ECS type or Elastic Container Instance type.
        # *   LOAD_BALANCER: Auto Scaling checks the health status of instances in the scaling group based on the health check results of load balancers. The health check results of Classic Load Balancer (CLB) instances are not supported as the health check basis for instances in the scaling group.
        # 
        # Default value: ECS.
        # 
        # >  If you want to enable instance health check and load balancer health check at the same time, we recommend that you specify `HealthCheckTypes`.
        self.health_check_type = health_check_type
        # The health check mode of the scaling group.
        # 
        # >  You can specify multiple values for this parameter to enable multiple health check options at the same time. If you specify `HealthCheckType`, this parameter is ignored.
        self.health_check_types = health_check_types
        # The ID of the ECS instance. When you create a scaling group, you can specify an existing ECS instance. Auto Scaling obtains the configurations of the ECS instance and automatically creates a scaling configuration from the obtained configurations.
        self.instance_id = instance_id
        # The ID of the launch template that provides instance configurations for Auto Scaling to create instances.
        self.launch_template_id = launch_template_id
        # Details of the instance types that you specify by using the Extended Configurations feature of the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version number of the launch template. Valid values:
        # 
        # *   A fixed template version number.
        # *   Default: the default template version.
        # *   Latest: the latest template version.
        self.launch_template_version = launch_template_version
        # The lifecycle hooks.
        self.lifecycle_hooks = lifecycle_hooks
        # The load balancer configurations.
        self.load_balancer_configs = load_balancer_configs
        # The IDs of the CLB instances that you want to associate with the scaling group. The value can be a JSON array that contains multiple CLB instance IDs. Separate multiple IDs with commas (,).
        # 
        # You can associate only a limited number of CLB instances with a scaling group. Go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check the maximum number of CLB instances that you can associate with a scaling group.
        self.load_balancer_ids = load_balancer_ids
        # The maximum life span of an instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 86400 to the value of the Integer.maxValue parameter.
        # 
        # Default value: null.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of instances that can be contained in the scaling group. When the total number of ECS instances in the scaling group exceeds the value of MaxSize, Auto Scaling automatically removes ECS instances from the scaling group until the total number equals the maximum number.
        # 
        # The value range of MaxSize is directly correlated with the degree of dependency your business has on Auto Scaling. You can go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas) to check **the maximum number of instances that a single scaling group can contain.**
        # 
        # If **a single scaling group can contain up to 2,000 ECS instances**, the value range of MaxSize is 0 to 2,000.
        # 
        # This parameter is required.
        self.max_size = max_size
        # The minimum number of instances that must be contained in the scaling group. When the total number of ECS instances in the scaling group is less than the value of MinSize, Auto Scaling automatically creates ECS instances in the scaling group until the total number reaches the minimum number.
        # 
        # >  The value of MinSize must be less than or equal to the value of MaxSize.
        # 
        # This parameter is required.
        self.min_size = min_size
        # The scaling policy for ECS instances in the multi-zone scaling group. Valid values:
        # 
        # *   PRIORITY: scale ECS instances based on the priority of the vSwitches specified by VSwitchIds. Auto Scaling preferentially scales instances in the zone where the vSwitch of the highest priority resides. If the scaling fails, Auto Scaling scales instances in the zone where the vSwitch of the next highest priority resides.
        # 
        # *   COST_OPTIMIZED: create ECS instances that have the lowest unit price of vCPUs during scale-out events and removes ECS instances that have the highest unit price of vCPUs during scale-in events. If you specify preemptible instance types in your scaling configuration, Auto Scaling will preferentially create preemptible instances. You can also specify CompensateWithOnDemand to allow Auto Scaling to create pay-as-you-go instances in the case that preemptible instances cannot be created due to limited stock.
        # 
        #     **
        # 
        #     **Note** The COST_OPTIMIZED setting takes effect only when your scaling configuration contains multiple instance types or specifically contains preemptible instance types.
        # 
        # *   BALANCE: evenly distribute ECS instances across the zones that are specified for the scaling group. If ECS instances are unevenly distributed across the specified zones due to insufficient inventory, you can call the [RebalanceInstance](https://help.aliyun.com/document_detail/71516.html) operation to evenly distribute the instances across the zones.
        # 
        #     **
        # 
        #     **Note** When you set `MultiAZPolicy` to `BALANCE`, this setting has an equivalent effect to setting `MultiAZPolicy` to `COMPOSABLE` and enabling `AzBalance` to `true`.
        # 
        # *   COMPOSABLE: combine the preceding policies into a custom scaling policy based on your business requirements. Alternatively, you can specify custom parameters to finely control the capacity of the scaling group.
        # 
        # Default value: PRIORITY.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances that must be contained in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances when the minimum number of pay-as-you-go instances reaches the requirement. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region ID of the scaling group.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The instance removal policies. Valid values:
        # 
        # *   OldestInstance: removes ECS instances that are added at the earliest point in time to the scaling group.
        # *   NewestInstance: removes ECS instances that are most recently added to the scaling group.
        # *   OldestScalingConfiguration: removes ECS instances that are created based on the earliest scaling configuration.
        # *   CustomPolicy: removes ECS instances based on the custom scale-in policy (Function).
        # 
        # The scaling configuration source specified by the OldestScalingConfiguration setting can be a scaling configuration or a launch template. The CustomPolicy setting takes effect only if you specify it as the first step to remove instances. If you specify CustomPolicy, you must also specify the CustomPolicyARN parameter.
        # 
        # > The removal of ECS instances from a scaling group is also affected by the value of the MultiAZPolicy parameter. For more information, see the [Configure a combination policy for removing instances](https://help.aliyun.com/document_detail/254822.html) topic.
        self.removal_policies = removal_policies
        # The ID of the resource group to which you want to add the scaling group.
        # 
        # > If you specify this parameter, new scaling groups are added to the specified resource group. If you do not specify this parameter, new scaling groups are added to the default resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The name of the scaling group. The name of each scaling group must be unique in a region.
        # 
        # The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit.
        # 
        # If you do not specify this parameter, the value of the ScalingGroupId parameter is used.
        self.scaling_group_name = scaling_group_name
        # The reclaim mode of the scaling group. Valid values:
        # 
        # *   recycle: the economical mode
        # 
        # *   release: the release mode
        # 
        # *   forcerelease: the forced release mode
        # 
        #     **
        # 
        #     **Note** If you set the value to forcerelease, Auto Scaling will forcibly release the ECS instances that are in the `Running` state during the scale-out events. Forced release equates to an immediate power-off, resulting in the irreversible deletion of all ephemeral data stored on the instance. Once executed, this action cannot be undone and the lost data cannot be recovered. Exercise caution when you select this option.
        # 
        # *   forcerecycle: the forced recycle mode
        # 
        #     **
        # 
        #     **Note** If you set the value to forcerecycle, Auto Scaling will forcibly shut down the ECS instances that are in the `Running` state during the scale-out events. Forced recycle equates to an immediate power-off, resulting in the irreversible deletion of all ephemeral data stored on the instance. Once executed, this action cannot be undone and the lost data cannot be recovered. Exercise caution when you select this option.
        # 
        # ScalingPolicy specifies the reclaim mode of the scaling group. RemovePolicy of the RemoveInstances operation specifies the specific instance removal action. For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The server groups.
        # 
        # >  You cannot use AlbServerGroups and ServerGroups to specify the same server group.
        self.server_groups = server_groups
        # The allocation policy of preemptible instances. You can use this parameter to individually specify the allocation policy of preemptible instances. This parameter takes effect only if you set the `MultiAZPolicy` parameter to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order of the instance types to create the required number of preemptible instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the lowest unit price of vCPUs to create the required number of preemptible instances.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of available instance types. Auto Scaling evenly creates preemptible instances of multiple instance types that are provided at the lowest cost in the scaling group. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to supplement preemptible instances. If you set this parameter to true, Auto Scaling creates an instance to replace a preemptible instance when Auto Scaling receives a system message which indicates that the preemptible instance is to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The period of time required by the ECS instance to enter the Stopped state. Unit: seconds. Valid values: 30 to 240.
        # 
        # > 
        # 
        # *   This parameter takes effect only if you set ScalingPolicy to release.
        # 
        # *   If you specify this parameter, the system will wait for the ECS instance to enter the Stopped state for the specified period of time before continuing with the scale-in operation, regardless of the status of the ECS instance.
        # 
        # *   If you do not specify this parameter, the system will wait for the ECS instance to stop before continuing with the scale-in operation. If the ECS instance is not successfully stopped, the scale-in process will be rolled back and considered failed.
        self.stop_instance_timeout = stop_instance_timeout
        # > This parameter is unavailable.
        self.sync_alarm_rule_to_cms = sync_alarm_rule_to_cms
        # The information about the tags of the scaling group.
        self.tags = tags
        # The backend vServer group that you want to associate with the scaling group.
        self.vserver_groups = vserver_groups
        # The ID of the vSwitch. If you specify the VSwitchId parameter, the network type of the scaling group is VPC.
        # 
        # > If you do not specify the VSwitchId or VSwitchIds parameter, the network type of the scaling group is classic network.
        self.v_switch_id = v_switch_id
        # The IDs of the vSwitches. If you specify VSwitchIds, VSwitchId is ignored. If you specify VSwitchIds, the network type of the scaling group is VPC.
        # 
        # If you specify multiple vSwitches, take note of the following items:
        # 
        # *   The vSwitches must belong to the same VPC.
        # *   The vSwitches can belong to different zones.
        # *   vSwitches are sorted in ascending order based on their priorities. The first vSwitch has the highest priority. If Auto Scaling fails to create ECS instances in the zone where the vSwitch of the highest priority resides, Auto Scaling attempts to create ECS instances in the zone where the vSwitch of the next highest priority resides.
        # 
        # >  If you do not specify VSwitchId or VSwitchIds for your scaling group, the network type of the scaling group is classic network.
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
        # The ID of the CLB instance to which the backend vServer group belongs.
        self.load_balancer_id = load_balancer_id
        # The attributes of the backend vServer group.
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
        # The port number used by each ECS instance as a backend server in the vServer group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the vServer group.
        self.vserver_group_id = vserver_group_id
        # The weight of each ECS instance as a backend server in the vServer group. If you increase the weight for an ECS instance, the number of requests that are forwarded to the ECS instance also increases. If you set the weight for an ECS instance to 0, no requests are forwarded to the ECS instance. Valid values: 0 to 100.
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
        # Identifies whether the tag is a propagatable tag. Valid values:
        # 
        # *   true: propagates the tag to only instances that are newly created.
        # *   false: does not propagate the tag to any instances.
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
        # The port number used by each ECS instance as backend server in the vServer group. Valid values: 1 to 65535.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # *   ALB
        # *   NLB
        self.type = type
        # The weight of each ECS instance as a backend server in the server group. Valid values: 0 to 100.
        # 
        # If you increase the weight for an ECS instance, the number of requests that are forwarded to the ECS instance also increases. If you set the weight for an ECS instance to 0, no requests are forwarded to the ECS instance.
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
        # The weight of each ECS instance as a backend server in the CLB backend server group. If you increase the weight for an ECS instance, the number of requests that are forwarded to the ECS instance also increases. If you set the weight for an ECS instance to 0, no requests are forwarded to the ECS instance. Valid values: 0 to 100.
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
        # The action that Auto Scaling performs when the lifecycle hook times out. Valid values:
        # 
        # *   CONTINUE: Auto Scaling continues to respond to the scaling request.
        # *   ABANDON: Auto Scaling releases ECS instances that are created during scale-out events, or removes ECS instances from the scaling group during scale-in events.
        # 
        # If multiple lifecycle hooks in the scaling group are triggered during scale-in events, and you set DefaultResult to ABANDON for one of the lifecycle hooks, Auto Scaling immediately performs the action after the lifecycle hook whose DefaultResult is set to ABANDON times out. In this case, other lifecycle hooks time out ahead of schedule. In other cases, Auto Scaling performs the action only after all lifecycle hooks time out. The action that Auto Scaling performs is determined by the value of DefaultResult that you specify for the lifecycle hook that most recently times out.
        # 
        # Default value: CONTINUE.
        self.default_result = default_result
        # The period of time before the lifecycle hook times out. When the lifecycle hook times out, Auto Scaling performs the action that is specified by DefaultResult. Valid values: 30 to 21600. Unit: seconds.
        # 
        # After you create a lifecycle hook, you can call the RecordLifecycleActionHeartbeat operation to extend the timeout period of the lifecycle hook. You can also call the CompleteLifecycleAction operation to end the timeout period of the lifecycle hook ahead of schedule.
        # 
        # Default value: 600.
        self.heartbeat_timeout = heartbeat_timeout
        # The name of the lifecycle hook. After you specify this parameter, you cannot change the name of the lifecycle hook. If you do not specify this parameter, the name of the lifecycle hook is the same as the ID of the lifecycle hook.
        self.lifecycle_hook_name = lifecycle_hook_name
        # The type of the scaling activity to which you want to apply the lifecycle hook. Valid values:
        # 
        # *   SCALE_OUT
        # *   SCALE_IN
        # 
        # >  If you specify lifecycle hooks for the scaling group, you must specify LifecycleTransition. Other parameters are optional.
        self.lifecycle_transition = lifecycle_transition
        # The Alibaba Cloud Resource Name (ARN) of the notification recipient party. You can specify a Simple Message Queue (SMQ, formerly MNS) topic or queue as the recipient party. The value is in the acs:ess:{region}:{account-id}:{resource-relative-id} format.
        # 
        # *   region: the region ID of the scaling group
        # *   account-id: the ID of your Alibaba Cloud account.
        # 
        # Examples:
        # 
        # *   SMQ queue: acs:ess:{region}:{account-id}:queue/{queuename}
        # *   SMQ topic: acs:ess:{region}:{account-id}:topic/{topicname}
        self.notification_arn = notification_arn
        # The fixed string that you want to include in notifications. When a lifecycle hook takes effect, Auto Scaling sends a notification. The fixed string can contain up to 4,096 characters in length. When Auto Scaling sends a notification to the recipient party, it includes predefined notification metadata into the notification. This helps in managing and labeling notifications of different categories. NotificationMetadata takes effect only if you specify NotificationArn.
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
        # The instance type that you want to use to override the instance type that is specified in the launch template.
        # 
        # If you want to scale instances based on the weighted capacities of the instances, you must specify both the InstanceType and WeightedCapacity parameters.
        # 
        # > This parameter is available only if you specify the LaunchTemplateId parameter.
        # 
        # You can use the InstanceType parameter to specify only instance types that are available for purchase.
        self.instance_type = instance_type
        # The maximum bid price of the instance type that is specified by the `InstanceType` parameter. You can specify 1 to 10 instance types by using the Extended Configurations feature of the launch template.
        # 
        # > This parameter is available only if you specify the `LaunchTemplateId` parameter.
        self.spot_price_limit = spot_price_limit
        # The weight of the instance type. The weight specifies the capacity of an instance of the specified instance type in the scaling group. If you want to scale instances based on the weighted capacities of the instances, you must specify the WeightedCapacity parameter after you specify the InstanceType parameter.
        # 
        # A higher weight specifies that a smaller number of instances of the specified instance type are required to meet the expected capacity requirement.
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
        # > The capacity of the scaling group cannot exceed the sum of the maximum number of instances that is specified by the MaxSize parameter and the maximum weight of the instance types.
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

class CreateScalingGroupRequestDBInstances(DaraModel):
    def __init__(
        self,
        attach_mode: str = None,
        dbinstance_id: str = None,
        type: str = None,
    ):
        # The mode in which you want to attach the database to the scaling group. Valid values:
        # 
        # *   SecurityIp: the mode in which Auto Scaling automatically adds the private IP addresses of ECS instances to the IP address whitelist of the database during scale-out events. You can set the value to SecurityIp only if you set Type to RDS.
        # *   SecurityGroup: the mode in which Auto Scaling adds the security group of the applied scaling configuration to the security group whitelist of the database. This setting allows ECS instances created from the scaling configuration to access the database.
        self.attach_mode = attach_mode
        # The database ID.
        self.dbinstance_id = dbinstance_id
        # The database type. Valid values:
        # 
        # *   RDS
        # *   Redis
        # *   MongoDB
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
        # Specifies whether to automatically create pay-as-you-go ECS instances to reach the required number of ECS instances when preemptible ECS instances cannot be created due to high prices or insufficient inventory of resources. This parameter takes effect when you set `MultiAZPolicy` to `COST_OPTIMIZED`. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: true.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. When the number of pay-as-you-go instances drops below the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        # 
        # If you set `MultiAZPolicy` to `COMPOSABLE`, the default value is 0.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances when the minimum number of pay-as-you-go instances is reached. `OnDemandBaseCapacity` specifies the minimum number of pay-as-you-go instances that must be contained in the scaling group. Valid values: 0 to 100.
        # 
        # If you set `MultiAZPolicy` to `COMPOSABLE`, the default value is 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The cost comparison method. Valid values:
        # 
        # *   PricePerUnit: Prices are compared based on the price per instance capacity.
        # 
        #     Capacity is determined by the weights assigned to instance types in the scaling group. If no weight is specified, a default weight of 1 is used, meaning each instance is assigned a capacity of 1.
        # 
        # *   PricePerVCpu: Prices are compared based on the price per vCPU.
        # 
        # Default value: PricePerUnit.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to replace pay-as-you-go instances with preemptible instances. If you specify `CompensateWithOnDemand`, it may result in a higher percentage of pay-as-you-go instances compared to the value of `OnDemandPercentageAboveBaseCapacity`. In this scenario, Auto Scaling will try to deploy preemptible instances to replace the surplus pay-as-you-go instances. When `CompensateWithOnDemand` is specified, Auto Scaling creates pay-as-you-go instances if there are not enough preemptible instance types. To avoid keeping these pay-as-you-go ECS instances for long periods, Auto Scaling tries to replace them with preemptible instances as soon as enough of preemptible instance types become available. Valid values:
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

class CreateScalingGroupRequestAlbServerGroups(DaraModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        # The ID of the ALB server group.
        # 
        # You can attach only a limited number of ALB server groups to a scaling group. To view the predefined quota limit or manually request a quota increase, go to [Quota Center](https://quotas.console.aliyun.com/products/ess/quotas).
        self.alb_server_group_id = alb_server_group_id
        # The port number used by each ECS instance as a backend server in the ALB server group. Valid values: 1 to 65535.
        self.port = port
        # The weight of an ECS instance as a backend server in the ALB server group. If you increase the weight for an ECS instance, the number of requests that are forwarded to the ECS instance also increases. If you set the weight for an ECS instance to 0, no requests are forwarded to the ECS instance. Valid values: 0 to 100.
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

