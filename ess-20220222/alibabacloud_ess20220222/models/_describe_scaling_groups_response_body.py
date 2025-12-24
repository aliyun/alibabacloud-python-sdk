# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingGroupsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_groups: List[main_models.DescribeScalingGroupsResponseBodyScalingGroups] = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The scaling groups.
        self.scaling_groups = scaling_groups
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scaling_groups:
            for v1 in self.scaling_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['ScalingGroups'] = []
        if self.scaling_groups is not None:
            for k1 in self.scaling_groups:
                result['ScalingGroups'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scaling_groups = []
        if m.get('ScalingGroups') is not None:
            for k1 in m.get('ScalingGroups'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroups()
                self.scaling_groups.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScalingGroupsResponseBodyScalingGroups(DaraModel):
    def __init__(
        self,
        active_capacity: int = None,
        active_scaling_configuration_id: str = None,
        alb_server_groups: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups] = None,
        allocation_strategy: str = None,
        auto_rebalance: bool = None,
        az_balance: bool = None,
        balance_mode: str = None,
        capacity_options: main_models.DescribeScalingGroupsResponseBodyScalingGroupsCapacityOptions = None,
        compensate_with_on_demand: bool = None,
        creation_time: str = None,
        current_host_name: str = None,
        custom_policy_arn: str = None,
        dbinstance_ids: List[str] = None,
        dbinstances: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsDBInstances] = None,
        default_cooldown: int = None,
        desired_capacity: int = None,
        enable_desired_capacity: bool = None,
        group_deletion_protection: bool = None,
        group_type: str = None,
        health_check_type: str = None,
        health_check_types: List[str] = None,
        init_capacity: int = None,
        is_elastic_strength_in_alarm: bool = None,
        launch_template_id: str = None,
        launch_template_overrides: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        load_balancer_configs: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsLoadBalancerConfigs] = None,
        load_balancer_ids: List[str] = None,
        max_instance_lifetime: int = None,
        max_size: int = None,
        min_size: int = None,
        modification_time: str = None,
        monitor_group_id: str = None,
        multi_azpolicy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        pending_capacity: int = None,
        pending_wait_capacity: int = None,
        protected_capacity: int = None,
        region_id: str = None,
        removal_policies: List[str] = None,
        removing_capacity: int = None,
        removing_wait_capacity: int = None,
        resource_group_id: str = None,
        scaling_group_id: str = None,
        scaling_group_name: str = None,
        scaling_policy: str = None,
        server_groups: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsServerGroups] = None,
        spot_allocation_strategy: str = None,
        spot_capacity: int = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        standby_capacity: int = None,
        stop_instance_timeout: int = None,
        stopped_capacity: int = None,
        suspended_processes: List[str] = None,
        system_suspended: bool = None,
        tags: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsTags] = None,
        total_capacity: int = None,
        total_instance_count: int = None,
        vserver_groups: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups] = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The number of ECS instances that are in the In Service state in the scaling group.
        self.active_capacity = active_capacity
        # The ID of the active scaling configuration in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The Application Load Balancer (ALB) server groups.
        self.alb_server_groups = alb_server_groups
        # The instance allocation policy. Auto Scaling selects instance types based on the allocation policy to create the required number of preemptible instances. The policy is suitable for pay-as-you-go instances and preemptible instances. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling adopts the predefined instance type sequence to create the required number of preemptible instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the most economical vCPU pricing to create the required number of instances.
        self.allocation_strategy = allocation_strategy
        # Whether to enable automatic rebalancing for the scaling group. This takes effect only when BalancedOnly is enabled for the scaling group. Valid value:
        # 
        # *   false: Auto rebalancing is disabled for the scaling group.
        # *   true: If Auto rebalancing is enabled, the scaling group automatically detects the capacity of the zone. If the capacity of the zone is unbalanced, the scaling group actively scales out the zone and re-balances the capacity of the zone.
        self.auto_rebalance = auto_rebalance
        # Indicates whether instances in the scaling group are evenly distributed across the specified zones. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   true
        # *   false
        self.az_balance = az_balance
        # The zone balancing mode. This mode takes effect only when the zone balancing mode is enabled. Valid value:
        # 
        # *   Default value: BalancedBestEffort. If a resource fails to be created in a zone, the resource is downgraded to another zone. This ensures best-effort delivery of the resource.
        # *   BalancedOnly: If a resource fails to be created in a zone, the resource is not downgraded to another zone. The scale-out activity is partially successful to avoid excessive imbalance of resources in different zones.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # Indicates whether Auto Scaling can create pay-as-you-go instances to supplement preemptible instances if preemptible instances cannot be created due to price-related factors or insufficient inventory when MultiAZPolicy is set to COST_OPTIMIZED. Valid values:
        # 
        # *   true
        # *   false
        self.compensate_with_on_demand = compensate_with_on_demand
        # The time when the scaling group was created.
        self.creation_time = creation_time
        # >  This parameter is unavailable.
        self.current_host_name = current_host_name
        # The Alibaba Cloud Resource Name (ARN) of the function that is specified in the custom scale-in policy. This parameter takes effect only if you set the first value of RemovalPolicies to CustomPolicy.
        self.custom_policy_arn = custom_policy_arn
        # The IDs of the ApsaraDB RDS instances that are attached to the scaling group.
        self.dbinstance_ids = dbinstance_ids
        # The databases that are attached to the scaling group.
        self.dbinstances = dbinstances
        # The cooldown period of the scaling group. During the cooldown period, Auto Scaling does not execute the scaling activities that are triggered by [CloudMonitor](https://help.aliyun.com/document_detail/35170.html) event-triggered tasks.
        self.default_cooldown = default_cooldown
        # The expected number of ECS instances in the scaling group. Auto Scaling automatically maintains the expected number of ECS instances.
        self.desired_capacity = desired_capacity
        # Indicates whether the Expected Number of Instances feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_desired_capacity = enable_desired_capacity
        # Indicates whether the Deletion Protection feature is enabled for the scaling group. Valid values:
        # 
        # *   true: The Deletion Protection feature is enabled for the scaling group. The scaling group cannot be deleted.
        # *   false: The Deletion Protection feature is disabled for the scaling group.
        self.group_deletion_protection = group_deletion_protection
        # The type of instances that are managed by the scaling group.
        self.group_type = group_type
        # The health check mode of the scaling group. Valid values:
        # 
        # *   NONE: Auto Scaling does not perform health checks.
        # *   ECS: Auto Scaling checks the health status of instances in the scaling group. If you want to enable instance health check, you can set the value to ECS, regardless of whether the scaling group is of ECS type or Elastic Container Instance type.
        # *   LOAD_BALANCER: Auto Scaling checks the health status of instances in the scaling group based on the health check results of load balancers. The health check results of Classic Load Balancer (CLB) instances are not supported as the health check basis for instances in the scaling group.
        self.health_check_type = health_check_type
        # The health check mode of the scaling group. Valid values:
        # 
        # *   NONE: Auto Scaling does not perform health checks.
        # *   ECS: Auto Scaling checks the health status of instances in the scaling group. If you want to enable instance health check, you can set the value to ECS, regardless of whether the scaling group is of ECS type or Elastic Container Instance type.
        # *   LOAD_BALANCER: Auto Scaling checks the health status of instances in the scaling group based on the health check results of load balancers. The health check results of CLB instances are not supported as the health check basis for instances in the scaling group.
        self.health_check_types = health_check_types
        # The number of instances that are initialized before they are added into the scaling group.
        self.init_capacity = init_capacity
        # >  This parameter is not available for use.
        self.is_elastic_strength_in_alarm = is_elastic_strength_in_alarm
        # The ID of the launch template that is used by the scaling group.
        self.launch_template_id = launch_template_id
        # The instance types that are extended in the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the launch template that is used by the scaling group.
        self.launch_template_version = launch_template_version
        # The status of the scaling group. Valid values:
        # 
        # *   Active: The scaling group is active. Active scaling groups can receive requests to execute scaling rules and trigger scaling activities.
        # *   Inactive: The scaling group is in the Disabled state. Disabled scaling groups cannot receive requests to execute scaling rules.
        # *   Deleting: The scaling group is being deleted. Scaling groups that are being deleted cannot receive requests to execute scaling rules, and the parameter settings of the scaling groups cannot be modified.
        self.lifecycle_state = lifecycle_state
        # The load balancer configurations.
        self.load_balancer_configs = load_balancer_configs
        # The IDs of the load balancers that are attached to the scaling group.
        self.load_balancer_ids = load_balancer_ids
        # The maximum life span of each ECS instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 0 or `[86400, Integer.maxValue]`. A value of 0 for MaxInstanceLifetime indicates that a previously set limit has been removed. This effectively disables the maximum instance lifetime constraint.
        # 
        # Default value: null.
        # 
        # >  This parameter is not supported by scaling groups of the Elastic Container Instance type and scaling groups whose ScalingPolicy is set to Recycle.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of ECS instances that can be contained in the scaling group.
        self.max_size = max_size
        # The minimum number of ECS instances that must be contained in the scaling group.
        self.min_size = min_size
        # The time when the scaling group was last modified.
        self.modification_time = modification_time
        # The ID of the CloudMonitor application group that is associated with the scaling group.
        self.monitor_group_id = monitor_group_id
        # The scaling policy of the ECS instances in the multi-zone scaling group. Valid values:
        # 
        # *   PRIORITY: ECS instances are created based on the value of VSwitchIds. If Auto Scaling cannot create ECS instances in the zone where the vSwitch of the highest priority resides, Auto Scaling creates ECS instances in the zone where the vSwitch of the next highest priority resides.
        # 
        # *   COST_OPTIMIZED: ECS instances are created based on the unit prices of their vCPUs. Auto Scaling preferentially creates ECS instances whose vCPUs are provided at the lowest price. If preemptible instance types are specified in the scaling configuration, Auto Scaling preferentially creates preemptible instances. You can also specify CompensateWithOnDemand to allow Auto Scaling to create pay-as-you-go instances if preemptible instances cannot be created due to limited stock.
        # 
        #     **
        # 
        #     **Note** The COST_OPTIMIZED setting takes effect only if your scaling configuration contains multiple instance types or contains preemptible instance types.
        # 
        # *   BALANCE: ECS instances are evenly distributed across the zones that are specified for the scaling group. If ECS instances become unevenly distributed across the specified zones due to limited instance type availability, you can call the RebalanceInstance operation to balance the distribution of the ECS instances.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances that must be contained in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in excess when the minimum number of pay-as-you-go instances reaches the threshold. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The number of ECS instances that are being added to the scaling group and configured.
        self.pending_capacity = pending_capacity
        # The number of ECS instances that are in the Pending Add state in the scaling group.
        self.pending_wait_capacity = pending_wait_capacity
        # The number of ECS instances that are in the Protected state in the scaling group.
        self.protected_capacity = protected_capacity
        # The region ID of the scaling group.
        self.region_id = region_id
        # The instance removal policies. Valid values:
        # 
        # *   OldestInstance: Auto Scaling removes ECS instances that are added at the earliest point in time to the scaling group.
        # *   NewestInstance: Auto Scaling removes ECS instances that are most recently added to the scaling group.
        # *   OldestScalingConfiguration: Auto Scaling removes ECS instances that are created from the earliest scaling configuration.
        self.removal_policies = removal_policies
        # The number of ECS instances that are being removed from the scaling group.
        self.removing_capacity = removing_capacity
        # The number of ECS instances that are in the Pending Remove state in the scaling group.
        self.removing_wait_capacity = removing_wait_capacity
        # The ID of the resource group to which the scaling group belongs.
        self.resource_group_id = resource_group_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling group.
        self.scaling_group_name = scaling_group_name
        # The instance reclaim mode of the scaling group. Valid values:
        # 
        # *   recycle: economical mode.
        # *   release: release mode.
        # *   forcerelease: forced release mode.
        # 
        # For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The server groups.
        # 
        # >  You can use this parameter to obtain information about ALB server groups and Network Load Balancer (NLB) server groups attached to the scaling group.
        self.server_groups = server_groups
        # The allocation policy of preemptible instances. This parameter indicates the manner in which Auto Scaling selects instance types to create the required number of preemptible instances. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling adopts the predefined instance type sequence to create the required number of preemptible instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the most economical vCPU pricing to create the required number of preemptible instances.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of preemptible instances in the scaling group.
        self.spot_capacity = spot_capacity
        # The number of instance types in the scaling group. Auto Scaling evenly creates preemptible instances of multiple instance types that are provided at the lowest price across the zones of the scaling group. Valid values: 0 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether preemptible instances can be supplemented. If this parameter is set to true, Auto Scaling proactively creates instances to replace the preemptible instances for reclamation when Auto Scaling receives a system notification.
        self.spot_instance_remedy = spot_instance_remedy
        # The number of ECS instances that are in the Standby state in the scaling group.
        self.standby_capacity = standby_capacity
        # The period of time that is required by the Elastic Compute Service (ECS) instance to enter the Stopped state during the scale-in process. Unit: seconds.
        self.stop_instance_timeout = stop_instance_timeout
        # The number of instances that was stopped in Economical Mode in the scaling group.
        self.stopped_capacity = stopped_capacity
        # The processes that are suspended. If no process is suspended, null is returned. Valid values:
        # 
        # *   ScaleIn: scale-in processes.
        # *   ScaleOut: scale-out processes.
        # *   HealthCheck: health check processes.
        # *   AlarmNotification: event-triggered task processes.
        # *   ScheduledAction: scheduled task processes.
        self.suspended_processes = suspended_processes
        # Indicates whether Auto Scaling stops executing scaling activities in the scaling group. Valid values:
        # 
        # *   true: Auto Scaling stops executing scaling activities in the scaling group if the scaling activities failed for more than seven consecutive days in the scaling group. In this case, you must modify the scaling group or scaling configuration to resume the scaling activities.
        # *   false: Auto Scaling does not stop executing scaling activities in the scaling group.
        self.system_suspended = system_suspended
        # The tags of the scaling group.
        self.tags = tags
        # The total weighted capacity of all ECS instances in the scaling group if Weighted is specified. In other cases, this parameter specifies the total number of ECS instances in the scaling group.
        self.total_capacity = total_capacity
        # The total number of ECS instances in the scaling group.
        self.total_instance_count = total_instance_count
        # The backend vServer groups.
        self.vserver_groups = vserver_groups
        # The vSwitch ID of the scaling group.
        self.v_switch_id = v_switch_id
        # The IDs of the vSwitches that are associated with the scaling group. If you specify VSwitchIds, VSwitchId is ignored.
        self.v_switch_ids = v_switch_ids
        # The ID of the virtual private cloud (VPC) in which the scaling group resides.
        self.vpc_id = vpc_id

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
        if self.active_capacity is not None:
            result['ActiveCapacity'] = self.active_capacity

        if self.active_scaling_configuration_id is not None:
            result['ActiveScalingConfigurationId'] = self.active_scaling_configuration_id

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

        if self.compensate_with_on_demand is not None:
            result['CompensateWithOnDemand'] = self.compensate_with_on_demand

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.current_host_name is not None:
            result['CurrentHostName'] = self.current_host_name

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

        if self.enable_desired_capacity is not None:
            result['EnableDesiredCapacity'] = self.enable_desired_capacity

        if self.group_deletion_protection is not None:
            result['GroupDeletionProtection'] = self.group_deletion_protection

        if self.group_type is not None:
            result['GroupType'] = self.group_type

        if self.health_check_type is not None:
            result['HealthCheckType'] = self.health_check_type

        if self.health_check_types is not None:
            result['HealthCheckTypes'] = self.health_check_types

        if self.init_capacity is not None:
            result['InitCapacity'] = self.init_capacity

        if self.is_elastic_strength_in_alarm is not None:
            result['IsElasticStrengthInAlarm'] = self.is_elastic_strength_in_alarm

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        result['LaunchTemplateOverrides'] = []
        if self.launch_template_overrides is not None:
            for k1 in self.launch_template_overrides:
                result['LaunchTemplateOverrides'].append(k1.to_map() if k1 else None)

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

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

        if self.modification_time is not None:
            result['ModificationTime'] = self.modification_time

        if self.monitor_group_id is not None:
            result['MonitorGroupId'] = self.monitor_group_id

        if self.multi_azpolicy is not None:
            result['MultiAZPolicy'] = self.multi_azpolicy

        if self.on_demand_base_capacity is not None:
            result['OnDemandBaseCapacity'] = self.on_demand_base_capacity

        if self.on_demand_percentage_above_base_capacity is not None:
            result['OnDemandPercentageAboveBaseCapacity'] = self.on_demand_percentage_above_base_capacity

        if self.pending_capacity is not None:
            result['PendingCapacity'] = self.pending_capacity

        if self.pending_wait_capacity is not None:
            result['PendingWaitCapacity'] = self.pending_wait_capacity

        if self.protected_capacity is not None:
            result['ProtectedCapacity'] = self.protected_capacity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.removal_policies is not None:
            result['RemovalPolicies'] = self.removal_policies

        if self.removing_capacity is not None:
            result['RemovingCapacity'] = self.removing_capacity

        if self.removing_wait_capacity is not None:
            result['RemovingWaitCapacity'] = self.removing_wait_capacity

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

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

        if self.spot_capacity is not None:
            result['SpotCapacity'] = self.spot_capacity

        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.standby_capacity is not None:
            result['StandbyCapacity'] = self.standby_capacity

        if self.stop_instance_timeout is not None:
            result['StopInstanceTimeout'] = self.stop_instance_timeout

        if self.stopped_capacity is not None:
            result['StoppedCapacity'] = self.stopped_capacity

        if self.suspended_processes is not None:
            result['SuspendedProcesses'] = self.suspended_processes

        if self.system_suspended is not None:
            result['SystemSuspended'] = self.system_suspended

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.total_instance_count is not None:
            result['TotalInstanceCount'] = self.total_instance_count

        result['VServerGroups'] = []
        if self.vserver_groups is not None:
            for k1 in self.vserver_groups:
                result['VServerGroups'].append(k1.to_map() if k1 else None)

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveCapacity') is not None:
            self.active_capacity = m.get('ActiveCapacity')

        if m.get('ActiveScalingConfigurationId') is not None:
            self.active_scaling_configuration_id = m.get('ActiveScalingConfigurationId')

        self.alb_server_groups = []
        if m.get('AlbServerGroups') is not None:
            for k1 in m.get('AlbServerGroups'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups()
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
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsCapacityOptions()
            self.capacity_options = temp_model.from_map(m.get('CapacityOptions'))

        if m.get('CompensateWithOnDemand') is not None:
            self.compensate_with_on_demand = m.get('CompensateWithOnDemand')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CurrentHostName') is not None:
            self.current_host_name = m.get('CurrentHostName')

        if m.get('CustomPolicyARN') is not None:
            self.custom_policy_arn = m.get('CustomPolicyARN')

        if m.get('DBInstanceIds') is not None:
            self.dbinstance_ids = m.get('DBInstanceIds')

        self.dbinstances = []
        if m.get('DBInstances') is not None:
            for k1 in m.get('DBInstances'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsDBInstances()
                self.dbinstances.append(temp_model.from_map(k1))

        if m.get('DefaultCooldown') is not None:
            self.default_cooldown = m.get('DefaultCooldown')

        if m.get('DesiredCapacity') is not None:
            self.desired_capacity = m.get('DesiredCapacity')

        if m.get('EnableDesiredCapacity') is not None:
            self.enable_desired_capacity = m.get('EnableDesiredCapacity')

        if m.get('GroupDeletionProtection') is not None:
            self.group_deletion_protection = m.get('GroupDeletionProtection')

        if m.get('GroupType') is not None:
            self.group_type = m.get('GroupType')

        if m.get('HealthCheckType') is not None:
            self.health_check_type = m.get('HealthCheckType')

        if m.get('HealthCheckTypes') is not None:
            self.health_check_types = m.get('HealthCheckTypes')

        if m.get('InitCapacity') is not None:
            self.init_capacity = m.get('InitCapacity')

        if m.get('IsElasticStrengthInAlarm') is not None:
            self.is_elastic_strength_in_alarm = m.get('IsElasticStrengthInAlarm')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        self.launch_template_overrides = []
        if m.get('LaunchTemplateOverrides') is not None:
            for k1 in m.get('LaunchTemplateOverrides'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        self.load_balancer_configs = []
        if m.get('LoadBalancerConfigs') is not None:
            for k1 in m.get('LoadBalancerConfigs'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsLoadBalancerConfigs()
                self.load_balancer_configs.append(temp_model.from_map(k1))

        if m.get('LoadBalancerIds') is not None:
            self.load_balancer_ids = m.get('LoadBalancerIds')

        if m.get('MaxInstanceLifetime') is not None:
            self.max_instance_lifetime = m.get('MaxInstanceLifetime')

        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        if m.get('ModificationTime') is not None:
            self.modification_time = m.get('ModificationTime')

        if m.get('MonitorGroupId') is not None:
            self.monitor_group_id = m.get('MonitorGroupId')

        if m.get('MultiAZPolicy') is not None:
            self.multi_azpolicy = m.get('MultiAZPolicy')

        if m.get('OnDemandBaseCapacity') is not None:
            self.on_demand_base_capacity = m.get('OnDemandBaseCapacity')

        if m.get('OnDemandPercentageAboveBaseCapacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('OnDemandPercentageAboveBaseCapacity')

        if m.get('PendingCapacity') is not None:
            self.pending_capacity = m.get('PendingCapacity')

        if m.get('PendingWaitCapacity') is not None:
            self.pending_wait_capacity = m.get('PendingWaitCapacity')

        if m.get('ProtectedCapacity') is not None:
            self.protected_capacity = m.get('ProtectedCapacity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RemovalPolicies') is not None:
            self.removal_policies = m.get('RemovalPolicies')

        if m.get('RemovingCapacity') is not None:
            self.removing_capacity = m.get('RemovingCapacity')

        if m.get('RemovingWaitCapacity') is not None:
            self.removing_wait_capacity = m.get('RemovingWaitCapacity')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingGroupName') is not None:
            self.scaling_group_name = m.get('ScalingGroupName')

        if m.get('ScalingPolicy') is not None:
            self.scaling_policy = m.get('ScalingPolicy')

        self.server_groups = []
        if m.get('ServerGroups') is not None:
            for k1 in m.get('ServerGroups'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')

        if m.get('SpotCapacity') is not None:
            self.spot_capacity = m.get('SpotCapacity')

        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('StandbyCapacity') is not None:
            self.standby_capacity = m.get('StandbyCapacity')

        if m.get('StopInstanceTimeout') is not None:
            self.stop_instance_timeout = m.get('StopInstanceTimeout')

        if m.get('StoppedCapacity') is not None:
            self.stopped_capacity = m.get('StoppedCapacity')

        if m.get('SuspendedProcesses') is not None:
            self.suspended_processes = m.get('SuspendedProcesses')

        if m.get('SystemSuspended') is not None:
            self.system_suspended = m.get('SystemSuspended')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')

        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k1 in m.get('VServerGroups'):
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the load balancer to which the backend vServer group belongs.
        self.load_balancer_id = load_balancer_id
        # The attributes of the backend vServer groups.
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
                temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k1))

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes(DaraModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        # The port number that is used by the load balancer to provide external services.
        self.port = port
        # The ID of the backend vServer group.
        self.vserver_group_id = vserver_group_id
        # The weight of the backend vServer group.
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

class DescribeScalingGroupsResponseBodyScalingGroupsTags(DaraModel):
    def __init__(
        self,
        propagate: bool = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # Indicates whether the tags of the scaling group can be propagated to instances. Valid values:
        # 
        # *   true: The tags of the scaling group can be propagated only to new instances.
        # *   false: The tags of the scaling group cannot be propagated to instances.
        # 
        # Default value: false.
        self.propagate = propagate
        # The tag key of the scaling group.
        self.tag_key = tag_key
        # The tag value of the scaling group.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.propagate is not None:
            result['Propagate'] = self.propagate

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Propagate') is not None:
            self.propagate = m.get('Propagate')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsServerGroups(DaraModel):
    def __init__(
        self,
        port: int = None,
        server_group_id: str = None,
        type: str = None,
        weight: int = None,
    ):
        # The port number used by an ECS instance as a backend server in the server group.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # *   ALB
        # *   NLB
        self.type = type
        # The weight of an ECS instance as a backend server in the server group.
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

class DescribeScalingGroupsResponseBodyScalingGroupsLoadBalancerConfigs(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        weight: int = None,
    ):
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The weight of an ECS instance as a backend server in the CLB server group. An increase in the weight of an ECS instance indicates an increase in the number of access requests that are forwarded to the ECS instance. If you set the weight of an ECS instance to 0, no access requests are forwarded to the ECS instance. Valid values: 0 to 100.
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

class DescribeScalingGroupsResponseBodyScalingGroupsLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        weighted_capacity: int = None,
    ):
        # The instance type. The instance type that is specified by this parameter overrides the instance type that is specified in the launch template.
        self.instance_type = instance_type
        # The maximum bid price of the instance type that is specified by `LaunchTemplateOverride.InstanceType`.
        # 
        # >  This parameter takes effect only if you use `LaunchTemplateId` to specify a launch template.
        self.spot_price_limit = spot_price_limit
        # The weight of the instance type. The value of this parameter indicates the capacity of a single instance of the specified instance type in the scaling group. A higher weight indicates that a smaller number of instances of the specified instance type are required to meet the expected capacity.
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

class DescribeScalingGroupsResponseBodyScalingGroupsDBInstances(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        security_group_ids: List[str] = None,
        type: str = None,
    ):
        # The ID of the database.
        self.dbinstance_id = dbinstance_id
        # The IDs of the security groups that are added to the security group whitelist of the attached database.
        self.security_group_ids = security_group_ids
        # The type of the database. Valid values:
        # 
        # *   RDS.
        # *   Redis.
        # *   MongoDB.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsCapacityOptions(DaraModel):
    def __init__(
        self,
        compensate_with_on_demand: bool = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        price_comparison_mode: str = None,
        spot_auto_replace_on_demand: bool = None,
    ):
        # Indicates whether pay-as-you-go ECS instances can be automatically created to reach the required number of ECS instances when preemptible ECS instances cannot be created due to high prices or insufficient inventory of resources. This parameter takes effect when you set `MultiAZPolicy` to `COST_OPTIMIZED`. Valid values:
        # 
        # *   true
        # *   false
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. When the actual number of pay-as-you-go instances drops below the minimum threshold, Auto Scaling preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances when the minimum number of pay-as-you-go instances is reached. `OnDemandBaseCapacity` specifies the minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # Indicates how prices are compared. Valid values:
        # 
        # *   PricePerUnit: Prices are compared based on the price per instance capacity.
        # 
        #     Capacity is determined by the weights assigned to instance types in the scaling group. If no weight is specified, a default weight of 1 is used, meaning each instance is assigned a capacity of 1.
        # 
        # *   PricePerVCpu: Prices are compared based on the price per vCPU.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to replace pay-as-you-go ECS instances with preemptible ECS instances. If you specify `CompensateWithOnDemand`, it may result in a higher percentage of pay-as-you-go instances compared to the value of `OnDemandPercentageAboveBaseCapacity`. In this scenario, Auto Scaling will try to deploy preemptible ECS instances to replace the surplus pay-as-you-go ECS instances. When `CompensateWithOnDemand` is specified, Auto Scaling creates pay-as-you-go ECS instances if there are not enough preemptible instance types available. To avoid keeping these pay-as-you-go ECS instances for long periods, Auto Scaling tries to replace them with preemptible instances as soon as enough of preemptible instance types become available. Valid values:
        # 
        # *   true
        # *   false
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

class DescribeScalingGroupsResponseBodyScalingGroupsAlbServerGroups(DaraModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        # The ID of the ALB server group.
        self.alb_server_group_id = alb_server_group_id
        # The port number used by an ECS instance as a backend server in the ALB server group.
        self.port = port
        # The weight of an ECS instance as a backend server in the ALB server group.
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

