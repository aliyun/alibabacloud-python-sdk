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
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The collection of scaling group information.
        self.scaling_groups = scaling_groups
        # The total number of scaling groups.
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
        warm_pool_capacity: int = None,
        warm_pool_configuration: main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfiguration = None,
        zone_shift_options: main_models.DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptions = None,
    ):
        # The number of ECS instances that have been added to the scaling group and are running properly.
        self.active_capacity = active_capacity
        # The ID of the active scaling configuration in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The collection of information about Application Load Balancer (ALB) server groups.
        self.alb_server_groups = alb_server_groups
        # The capacity allocation strategy, which determines how the scaling group selects available instance types to meet the capacity requirements. The capacity distribution strategy applies to both pay-as-you-go and spot capacity. This parameter takes effect only when the `MultiAZPolicy` parameter is set to `COMPOSABLE`. Valid values:
        # 
        # - priority: Creates instances based on the order of the configured instance types.
        # - lowestPrice: Creates instances based on the unit price per vCPU of the instance types in ascending order.
        self.allocation_strategy = allocation_strategy
        # Specifies whether to enable automatic balancing for the scaling group. This parameter takes effect only when BalancedOnly is enabled for zone balancing. Valid values:
        # - false: Automatic balancing for the scaling group is disabled.
        # - true: Automatic balancing for the scaling group is enabled. The scaling group automatically detects the capacity across zones. When the capacity is unbalanced, the scaling group proactively scales in or out to rebalance the capacity across zones.
        self.auto_rebalance = auto_rebalance
        # Specifies whether the capacity of the scaling group is evenly distributed across multiple zones. This parameter takes effect only when the `MultiAZPolicy` parameter is set to `COMPOSABLE`. Valid values:
        # 
        # - true: The capacity of the scaling group is evenly distributed across multiple zones.
        # - false: The capacity of the scaling group is not evenly distributed across multiple zones.
        self.az_balance = az_balance
        # The zone balancing mode. This parameter takes effect only when the zone balancing mode is enabled. Valid values:
        #  
        # - BalancedBestEffort: When resource creation fails in a zone, the system falls back to other zones to ensure best-effort delivery of resources.
        # 
        # - BalancedOnly: When resource creation fails in a zone, the system does not fall back to other zones. The scale-out activity partially succeeds to avoid excessive imbalance of resources across different zones.
        self.balance_mode = balance_mode
        # The capacity options.
        self.capacity_options = capacity_options
        # Specifies whether to automatically create pay-as-you-go instances to meet the requirement for the number of ECS instances when the MultiAZPolicy parameter is set to COST_OPTIMIZED and the required number of spot instances cannot be created due to insufficient resources or price limits. Valid values:
        # 
        # - true: yes.
        # - false: no.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The time when the scaling group was created. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # > This parameter is not available.
        self.current_host_name = current_host_name
        # The Alibaba Cloud Resource Name (ARN) of the Function Compute function for the custom scale-in policy. This parameter takes effect only when the first removal policy configured in RemovalPolicies is CustomPolicy.
        self.custom_policy_arn = custom_policy_arn
        # The IDs of the ApsaraDB RDS instances associated with the scaling group.
        self.dbinstance_ids = dbinstance_ids
        # The list of databases associated with the scaling group.
        self.dbinstances = dbinstances
        # The default cooldown time of the scaling group. During the cooldown time, the scaling group does not execute any other scaling activity. This parameter applies only to a scaling activity triggered by a CloudMonitor event-triggered task.
        self.default_cooldown = default_cooldown
        # The expected number of instances in the scaling group. The scaling group automatically maintains the number of ECS instances at the expected number of instances.
        self.desired_capacity = desired_capacity
        # Specifies whether the expected number of instances feature is enabled. Valid values:
        # - true: The expected number of instances feature is enabled.
        # - false: The expected number of instances feature is disabled.
        self.enable_desired_capacity = enable_desired_capacity
        # Indicates whether deletion protection is enabled for the scaling group. Valid values:
        # 
        # - true: Deletion protection is enabled. The scaling group cannot be deleted.
        # - false: Deletion protection is disabled.
        self.group_deletion_protection = group_deletion_protection
        # The type of instances managed by the scaling group.
        self.group_type = group_type
        # The health check mode of the scaling group. Valid values:
        # 
        # - NONE: No health check is performed.
        # - ECS: Health checks are performed on instances in the scaling group. This value applies to both ECS and ECI scaling groups.
        # - LOAD_BALANCER: The health status of instances is determined based on the health check results of load balancing (CLB load balancing type is not supported).
        self.health_check_type = health_check_type
        # The health check mode of the scaling group. Valid values:
        # 
        # - NONE: No health check is performed.
        # - ECS: Health checks are performed on instances in the scaling group. This value is used to enable instance health checks for both ECS and ECI scaling groups.
        # - LOAD_BALANCER: The health status of instances is determined based on the health check results of load balancing (the CLB load balancing type is not currently supported).
        self.health_check_types = health_check_types
        # The number of instances in the initialization state before scale-out in the scaling group.
        self.init_capacity = init_capacity
        # > This parameter is not available.
        self.is_elastic_strength_in_alarm = is_elastic_strength_in_alarm
        # The ID of the launch template used by the scaling group.
        self.launch_template_id = launch_template_id
        # The instance type overrides for the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version of the launch template used by the scaling group.
        self.launch_template_version = launch_template_version
        # The lifecycle state of the scaling group. Valid values:
        # 
        # - Active: The scaling group is active. Only active scaling groups can accept requests to execute scaling rules and trigger a scaling activity.
        # - Inactive: The scaling group is inactive. Inactive scaling groups do not accept any requests to execute scaling rules.
        # - Deleting: The scaling group is being deleted. Scaling groups in the Deleting state do not accept any requests to execute scaling rules, and their parameters cannot be modified.
        self.lifecycle_state = lifecycle_state
        # The list of load balancing configurations.
        self.load_balancer_configs = load_balancer_configs
        # The list of IDs of the load balancing instances associated with the scaling group.
        self.load_balancer_ids = load_balancer_ids
        # The maximum lifetime of an instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 0 or `[86400, Integer.maxValue]`. A value of 0 indicates that the configured value of MaxInstanceLifetime is cleared, which means MaxInstanceLifetime is not configured.
        # 
        # Default value: null.
        # 
        # >This parameter is not supported for scaling groups of the Elastic Container Instance (ECI) type or scaling groups that have the No Fees for Stopped Instances feature enabled.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of ECS instances in the scaling group.
        self.max_size = max_size
        # The minimum number of ECS instances in the scaling group.
        self.min_size = min_size
        # The time when the scaling group was modified. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time is displayed in UTC.
        self.modification_time = modification_time
        # The ID of the CloudMonitor application group associated with the scaling group.
        self.monitor_group_id = monitor_group_id
        # The scale-out and scale-in policy for ECS instances in a multi-zone scaling group. Valid values:
        #          
        # - PRIORITY: Scales instances based on the defined vSwitches (VSwitchIds). If ECS instances cannot be created in the zone of the vSwitch with the highest priority, the system automatically uses the vSwitch with the next highest priority to create ECS instances.
        # - COST_OPTIMIZED: Attempts to create instances based on the unit price of vCPUs from low to high. If the scaling configuration specifies multiple instance types that use the preemptible billing method, the system preferentially creates spot instances. You can use the CompensateWithOnDemand parameter to specify whether to automatically create pay-as-you-go instances when spot instances cannot be created due to insufficient resources.
        #     > The COST_OPTIMIZED value takes effect only when the scaling configuration specifies multiple instance types or uses spot instances.
        # - BALANCE: Evenly allocates ECS instances across the active zones specified for the scaling group. If the instances are unevenly distributed across zones due to insufficient resources, you can call the RebalanceInstance operation to balance the resources.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 1000. When the number of pay-as-you-go instances in the scaling group is less than this value, the system preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances to be created when the number of instances exceeds the value of OnDemandBaseCapacity. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The number of ECS instances that are being added to the scaling group but have not completed the relevant configurations.
        self.pending_capacity = pending_capacity
        # The number of ECS instances that are pending addition to the scaling group.
        self.pending_wait_capacity = pending_wait_capacity
        # The number of ECS instances that are in the Protected state in the scaling group.
        self.protected_capacity = protected_capacity
        # The ID of the region to which the scaling group belongs.
        self.region_id = region_id
        # The collection of policies for removing ECS instances from the scaling group. Valid values:
        # - OldestInstance: Removes the ECS instances that were created at the earliest point in time.
        # - NewestInstance: Removes the ECS instances that were created at the latest point in time.
        # - OldestScalingConfiguration: Removes the ECS instances that were created by using the earliest scaling configuration.
        self.removal_policies = removal_policies
        # The number of ECS instances that are being removed from the scaling group.
        self.removing_capacity = removing_capacity
        # The number of ECS instances that are pending removal from the scaling group.
        self.removing_wait_capacity = removing_wait_capacity
        # The ID of the resource group to which the scaling group belongs.
        self.resource_group_id = resource_group_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling group.
        self.scaling_group_name = scaling_group_name
        # The reclaim mode of the scaling group. Valid values:
        #          
        # - recycle: The scaling group uses the shutdown and reclaim mode.
        # - release: The scaling group uses the release mode.
        # - forcerelease: The scaling group uses the force release mode.
        # 
        # For more information about the actions on removed instances, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The collection of information about load balancing server groups.
        # 
        # > You can use this parameter to obtain the collection of information about ALB service groups, Network Load Balancer (NLB) server groups, and Gateway Load Balancer (GWLB) service groups associated with the scaling group.
        # >
        self.server_groups = server_groups
        # The spot capacity distribution strategy. You can use this parameter to specify the distribution strategy for spot capacity separately. This parameter takes effect only when the `MultiAZPolicy` parameter is set to `COMPOSABLE`. Valid values:
        # 
        # - priority: Creates instances based on the order of the configured instance types.
        # - lowestPrice: Creates instances based on the unit price per vCPU of the instance types in ascending order.
        # 
        # Default value: priority.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of spot instances in the scaling group.
        self.spot_capacity = spot_capacity
        # The number of available instance types specified. The scaling group creates spot instances evenly across the specified instance types with the lowest cost. Valid values: 0 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether spot instance replenishment is enabled. If this feature is enabled, when the scaling group receives a system message indicating that a preemptible instance will be reclaimed, the scaling group attempts to create a new instance to replace the preemptible instance.
        self.spot_instance_remedy = spot_instance_remedy
        # The number of instances that are in the Standby state in the scaling group.
        self.standby_capacity = standby_capacity
        # The timeout period for waiting for an ECS instance to be stopped during the scale-in process. Unit: seconds.
        self.stop_instance_timeout = stop_instance_timeout
        # The number of instances in the scaling group that are in the economical mode.
        self.stopped_capacity = stopped_capacity
        # The suspended processes. If no process is suspended, an empty value is returned. Valid values:
        # 
        # - ScaleIn: The scale-in process.
        # - ScaleOut: The scale-out process.
        # - HealthCheck: The health check process.
        # - AlarmNotification: The event-triggered task process.
        # - ScheduledAction: The scheduled task process.
        self.suspended_processes = suspended_processes
        # Indicates whether Auto Scaling stops executing any scaling activity in the scaling group. Valid values:
        # 
        # - true: Auto Scaling stops executing any scaling activity in the scaling group. This indicates that the scaling group has failed to execute scale-out or scale-in operations for more than seven consecutive days. You must modify the scaling group or scaling configuration to resume the execution of the scaling activity.
        # - false: Auto Scaling executes the scaling activity in the scaling group.
        self.system_suspended = system_suspended
        # The tags of the scaling group.
        self.tags = tags
        # The total weighted capacity of all ECS instances in the scaling group if instance type weights are configured. Otherwise, this parameter indicates the total number of ECS instances in the scaling group.
        self.total_capacity = total_capacity
        # The total number of ECS instances in the scaling group.
        self.total_instance_count = total_instance_count
        # The list of backend server groups.
        self.vserver_groups = vserver_groups
        # The ID of the vSwitch associated with the scaling group.
        self.v_switch_id = v_switch_id
        # The collection of IDs of the vSwitches associated with the scaling group. If you specify the VSwitchIds parameter, the VSwitchId parameter is ignored.
        self.v_switch_ids = v_switch_ids
        # The ID of the VPC to which the scaling group belongs.
        self.vpc_id = vpc_id
        # The number of instances in the warm pool.
        self.warm_pool_capacity = warm_pool_capacity
        # The warm pool configuration of the scaling group.
        self.warm_pool_configuration = warm_pool_configuration
        # The zone shift options.
        self.zone_shift_options = zone_shift_options

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
        if self.warm_pool_configuration:
            self.warm_pool_configuration.validate()
        if self.zone_shift_options:
            self.zone_shift_options.validate()

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

        if self.warm_pool_capacity is not None:
            result['WarmPoolCapacity'] = self.warm_pool_capacity

        if self.warm_pool_configuration is not None:
            result['WarmPoolConfiguration'] = self.warm_pool_configuration.to_map()

        if self.zone_shift_options is not None:
            result['ZoneShiftOptions'] = self.zone_shift_options.to_map()

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

        if m.get('WarmPoolCapacity') is not None:
            self.warm_pool_capacity = m.get('WarmPoolCapacity')

        if m.get('WarmPoolConfiguration') is not None:
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfiguration()
            self.warm_pool_configuration = temp_model.from_map(m.get('WarmPoolConfiguration'))

        if m.get('ZoneShiftOptions') is not None:
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptions()
            self.zone_shift_options = temp_model.from_map(m.get('ZoneShiftOptions'))

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptions(DaraModel):
    def __init__(
        self,
        expiry_time: str = None,
        impaired_zone_ids: List[str] = None,
        zone_shift_policy: main_models.DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptionsZoneShiftPolicy = None,
    ):
        # The expiration time of the zone shift. After the expiration time, the system automatically ends the shift and restores the related zones. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDThh:mmZ format.
        self.expiry_time = expiry_time
        # The list of impaired zone IDs.
        self.impaired_zone_ids = impaired_zone_ids
        # The behavior policy of the scaling group during the zone shift.
        self.zone_shift_policy = zone_shift_policy

    def validate(self):
        if self.zone_shift_policy:
            self.zone_shift_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expiry_time is not None:
            result['ExpiryTime'] = self.expiry_time

        if self.impaired_zone_ids is not None:
            result['ImpairedZoneIds'] = self.impaired_zone_ids

        if self.zone_shift_policy is not None:
            result['ZoneShiftPolicy'] = self.zone_shift_policy.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiryTime') is not None:
            self.expiry_time = m.get('ExpiryTime')

        if m.get('ImpairedZoneIds') is not None:
            self.impaired_zone_ids = m.get('ImpairedZoneIds')

        if m.get('ZoneShiftPolicy') is not None:
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptionsZoneShiftPolicy()
            self.zone_shift_policy = temp_model.from_map(m.get('ZoneShiftPolicy'))

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsZoneShiftOptionsZoneShiftPolicy(DaraModel):
    def __init__(
        self,
        impaired_zone_health_check_behavior: str = None,
        scale_in_blocked_rule_types: List[str] = None,
        scale_out_in_healthy_zones_only: bool = None,
    ):
        # The health check behavior in impaired zones. Valid values: 
        # 
        # - ReplaceUnhealthy: Unhealthy instances in all zones are replaced normally.
        # - IgnoreUnhealthy: Unhealthy instances in impaired zones are not replaced. Healthy zones are not affected.
        self.impaired_zone_health_check_behavior = impaired_zone_health_check_behavior
        # Blocks scale-in activities triggered by specified types of scaling rules. The blocking scope applies to all zones under the scaling group, not just the impaired zones. This prevents false improvements in monitoring metrics caused by unreachable instances in impaired zones, which could lead to accidental scale-in activities. Valid values: 
        # 
        # - StepScalingRule: Blocks scale-in activities triggered by step scaling rules. 
        # - TargetTrackingScalingRule: Blocks scale-in activities triggered by target tracking scaling rules. 
        # - None: No blocking.
        self.scale_in_blocked_rule_types = scale_in_blocked_rule_types
        # Specifies whether scale-out activities create instances only in healthy zones during the shift. Valid values: 
        # 
        # - true: Scale-out activities create instances only in healthy zones and skip impaired zones. 
        # - false: Scale-out activities are not restricted by zone and can create instances in any zone under the scaling group.
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

class DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfiguration(DaraModel):
    def __init__(
        self,
        capacity_options: main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationCapacityOptions = None,
        instance_reuse_policy: main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationInstanceReusePolicy = None,
        pool_state: str = None,
        status: str = None,
    ):
        # The capacity configuration of the warm pool.
        self.capacity_options = capacity_options
        # The instance reuse policy.
        self.instance_reuse_policy = instance_reuse_policy
        # The instance status in the warm pool. Valid values:
        # - Stopped: Economical mode.
        # - Running: Running.
        self.pool_state = pool_state
        # The status of the warm pool. Valid values:
        # - Active: Running.
        # - Deleting: Deleting.
        self.status = status

    def validate(self):
        if self.capacity_options:
            self.capacity_options.validate()
        if self.instance_reuse_policy:
            self.instance_reuse_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity_options is not None:
            result['CapacityOptions'] = self.capacity_options.to_map()

        if self.instance_reuse_policy is not None:
            result['InstanceReusePolicy'] = self.instance_reuse_policy.to_map()

        if self.pool_state is not None:
            result['PoolState'] = self.pool_state

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CapacityOptions') is not None:
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationCapacityOptions()
            self.capacity_options = temp_model.from_map(m.get('CapacityOptions'))

        if m.get('InstanceReusePolicy') is not None:
            temp_model = main_models.DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationInstanceReusePolicy()
            self.instance_reuse_policy = temp_model.from_map(m.get('InstanceReusePolicy'))

        if m.get('PoolState') is not None:
            self.pool_state = m.get('PoolState')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationInstanceReusePolicy(DaraModel):
    def __init__(
        self,
        reuse_on_scale_in: bool = None,
    ):
        # Specifies whether instances are added back to the warm pool when the scaling group scales in.
        self.reuse_on_scale_in = reuse_on_scale_in

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reuse_on_scale_in is not None:
            result['ReuseOnScaleIn'] = self.reuse_on_scale_in

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReuseOnScaleIn') is not None:
            self.reuse_on_scale_in = m.get('ReuseOnScaleIn')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsWarmPoolConfigurationCapacityOptions(DaraModel):
    def __init__(
        self,
        desired_group_prepared_capacity: int = None,
        min_capacity: int = None,
    ):
        # The expected number of prepared instances. The system always maintains the sum of the number of instances in the scaling group and the number of instances in the warm pool equal to the expected capacity of the warm pool.
        self.desired_group_prepared_capacity = desired_group_prepared_capacity
        # The minimum number of instances to maintain in the warm pool.
        self.min_capacity = min_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_group_prepared_capacity is not None:
            result['DesiredGroupPreparedCapacity'] = self.desired_group_prepared_capacity

        if self.min_capacity is not None:
            result['MinCapacity'] = self.min_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredGroupPreparedCapacity') is not None:
            self.desired_group_prepared_capacity = m.get('DesiredGroupPreparedCapacity')

        if m.get('MinCapacity') is not None:
            self.min_capacity = m.get('MinCapacity')

        return self

class DescribeScalingGroupsResponseBodyScalingGroupsVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.DescribeScalingGroupsResponseBodyScalingGroupsVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the load balancing instance to which the backend server group belongs.
        self.load_balancer_id = load_balancer_id
        # The property of the backend server group.
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
        # The port number used by the load balancing instance to provide services.
        self.port = port
        # The property of the backend server group.
        self.vserver_group_id = vserver_group_id
        # The weight of the backend server group.
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
        # Specifies whether the tag is propagated. Valid values:
        # - true: Tags on the scaling group are propagated only to newly created instances, but not to instances that are already running in the scaling group.
        # - false: Tags on the scaling group are not propagated to instances.
        # 
        # Default value: false.
        self.propagate = propagate
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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
        # The port number used by the ECS instance after Auto Scaling adds the ECS instance to the server group.
        self.port = port
        # The ID of the server group.
        self.server_group_id = server_group_id
        # The type of the server group. Valid values:
        # 
        # - ALB: Application Load Balancer (application load balancing).
        # - NLB: Network Load Balancer (network load balancing).
        # - GWLB: Gateway Load Balancer (gateway load balancing).
        self.type = type
        # The weight of the ECS instance as a backend server after Auto Scaling adds the ECS instance to the server group.
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
        # The ID of the load balancing CLB (formerly SLB) instance.
        self.load_balancer_id = load_balancer_id
        # The weight of the ECS instance as a backend server after Auto Scaling adds the ECS instance to the SLB server group. A higher weight specifies that more access requests are distributed to the ECS instance. If the weight is 0, the ECS instance does not receive access requests. Valid values: 0 to 100.
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
        # The specified instance type, which overrides the instance type in the launch template.
        self.instance_type = instance_type
        # The maximum hourly price for the instance type specified in the launch template override (namely, LaunchTemplateOverride.InstanceType).
        # > This parameter takes effect only when the LaunchTemplateId parameter is specified.
        self.spot_price_limit = spot_price_limit
        # The weight of the instance type, which indicates the capacity of a single instance of the specified instance type in the scaling group. A greater weight indicates that fewer instances of the specified instance type are required to meet the expected capacity.
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
        # The database instance ID.
        self.dbinstance_id = dbinstance_id
        # The list of security group whitelists added to the database by the scaling group.
        self.security_group_ids = security_group_ids
        # The type of the database. Valid values:
        # - RDS
        # - Redis
        # - MongoDB
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
        # Specifies whether to automatically create pay-as-you-go instances to meet the required number of ECS instances when the `MultiAZPolicy` parameter is set to `COST_OPTIMIZED` and sufficient spot instances cannot be created due to price or inventory reasons. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The minimum number of pay-as-you-go instances required in the scaling group. If the number of pay-as-you-go instances in the scaling group is less than this value, the system preferentially creates pay-as-you-go instances. Valid values: 0 to 1000.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances in the excess instances after the scaling group meets the minimum number of pay-as-you-go instances specified by `OnDemandBaseCapacity`. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The price comparison mode of the cost optimization strategy for the scaling group. Valid values:
        # - PricePerUnit: Compares prices based on the price per unit of capacity.
        # 
        #   The capacity of an instance in the scaling group is equal to the weight set for the instance type. The default weight is 1, which means one ECS instance occupies one unit of capacity.
        # 
        # - PricePerVCpu: Compares prices based on the price per vCPU.
        self.price_comparison_mode = price_comparison_mode
        # Specifies whether to use spot instances to replace pay-as-you-go capacity when `CompensateWithOnDemand` is enabled and the percentage of pay-as-you-go instances exceeds the value of `OnDemandPercentageAboveBaseCapacity`. In common scenarios where `CompensateWithOnDemand` downgrades spot instances to pay-as-you-go instances due to spot inventory or price reasons, this parameter attempts to use spot instances to replace the excess pay-as-you-go capacity to avoid long-term retention of pay-as-you-go instances. Valid values:
        # 
        # - true: Allowed.
        # - false: Not allowed.
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
        # The port number used by the ECS instance after Auto Scaling adds the ECS instance to the ALB server group.
        self.port = port
        # The weight of the ECS instance as a backend server after Auto Scaling adds the ECS instance to the ALB server group.
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

