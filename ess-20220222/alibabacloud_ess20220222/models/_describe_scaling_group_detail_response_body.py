# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingGroupDetailResponseBody(DaraModel):
    def __init__(
        self,
        output: str = None,
        request_id: str = None,
        scaling_group: main_models.DescribeScalingGroupDetailResponseBodyScalingGroup = None,
    ):
        # The output details of the scaling group of the Elastic Container Instance type. Currently, the output is displayed in a Kubernetes Deployment YAML file.
        self.output = output
        # The request ID.
        self.request_id = request_id
        # The scaling group.
        self.scaling_group = scaling_group

    def validate(self):
        if self.scaling_group:
            self.scaling_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_group is not None:
            result['ScalingGroup'] = self.scaling_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingGroup') is not None:
            temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('ScalingGroup'))

        return self

class DescribeScalingGroupDetailResponseBodyScalingGroup(DaraModel):
    def __init__(
        self,
        active_capacity: int = None,
        active_scaling_configuration_id: str = None,
        alb_server_groups: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupAlbServerGroups] = None,
        allocation_strategy: str = None,
        az_balance: bool = None,
        compensate_with_on_demand: bool = None,
        creation_time: str = None,
        current_host_name: str = None,
        custom_policy_arn: str = None,
        dbinstance_ids: List[str] = None,
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
        launch_template_overrides: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupLaunchTemplateOverrides] = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        load_balancer_configs: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupLoadBalancerConfigs] = None,
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
        server_groups: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupServerGroups] = None,
        spot_allocation_strategy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        standby_capacity: int = None,
        stopped_capacity: int = None,
        suspended_processes: List[str] = None,
        system_suspended: bool = None,
        tags: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupTags] = None,
        total_capacity: int = None,
        total_instance_count: int = None,
        vserver_groups: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroups] = None,
        v_switch_id: str = None,
        v_switch_ids: List[str] = None,
        vpc_id: str = None,
    ):
        # The number of ECS instances that are in the In Service state in the scaling group.
        self.active_capacity = active_capacity
        # The ID of the active scaling configuration in the scaling group.
        self.active_scaling_configuration_id = active_scaling_configuration_id
        # The information about the Application Load Balancer (ALB) server groups.
        self.alb_server_groups = alb_server_groups
        # The allocation policy of instances. Auto Scaling selects instance types based on the allocation policy to create the required number of instances. You can apply the policy to pay-as-you-go instances and preemptible instances. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order to create the required number of instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the lowest unit price of vCPUs to create the required number of instances.
        self.allocation_strategy = allocation_strategy
        # Indicates whether instances in the scaling group are evenly distributed across zones. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   true
        # *   false
        self.az_balance = az_balance
        # Indicates whether pay-as-you-go ECS instances can be automatically created to reach the required number of ECS instances when preemptible ECS instances cannot be created due to high prices or insufficient inventory of resources. This parameter takes effect when you set `MultiAZPolicy` to `COST_OPTIMIZED`. Valid values:
        # 
        # *   true
        # *   false
        self.compensate_with_on_demand = compensate_with_on_demand
        # The time when the scaling group was created.
        self.creation_time = creation_time
        # >  This parameter is not available for use.
        self.current_host_name = current_host_name
        # The Alibaba Cloud Resource Name (ARN) of the function that is specified in the custom scale-in policy. This parameter takes effect only if you set the first value of RemovalPolicies to CustomPolicy.
        self.custom_policy_arn = custom_policy_arn
        # The IDs of the ApsaraDB RDS instances that are associated with the scaling group.
        self.dbinstance_ids = dbinstance_ids
        # The cooldown period of the scaling group. Unit: seconds.
        self.default_cooldown = default_cooldown
        # The expected number of ECS instances in the scaling group. Auto Scaling automatically maintains the expected number of ECS instances.
        self.desired_capacity = desired_capacity
        # Indicates whether the Expected Number of Instances feature is enabled. Valid values:
        # 
        # *   true
        # *   false
        self.enable_desired_capacity = enable_desired_capacity
        # Indicates whether Deletion Protection is enabled for the scaling group. Valid values:
        # 
        # *   true: Deletion Protection is enabled for the scaling group. This way, the scaling group cannot be deleted.
        # *   false: Deletion Protection is disabled for the scaling group.
        self.group_deletion_protection = group_deletion_protection
        # The type of the instances that are managed by the scaling group. Valid values:
        # 
        # *   ECS: ECS instances
        # *   ECI: elastic container instances
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
        # The number of instances that are in the Initialized state and not added to the scaling group.
        self.init_capacity = init_capacity
        # >  This parameter is not available for use.
        self.is_elastic_strength_in_alarm = is_elastic_strength_in_alarm
        # The ID of the launch template that is used by the scaling group.
        self.launch_template_id = launch_template_id
        # The information about the instance types that are extended in the launch template.
        self.launch_template_overrides = launch_template_overrides
        # The version number of the launch template.
        self.launch_template_version = launch_template_version
        # The status of the scaling group. Valid values:
        # 
        # *   Active: The scaling group is in the Enabled state. Enabled scaling groups can receive requests to execute scaling rules and trigger scaling activities.
        # *   Inactive: The scaling group is in the Disabled state. Disabled scaling groups cannot receive requests to execute scaling rules.
        # *   Deleting: The scaling group is being deleted. Scaling groups that are being deleted cannot receive requests to execute scaling rules, and the parameter settings of the scaling groups cannot be modified.
        self.lifecycle_state = lifecycle_state
        # The CLB configurations.
        self.load_balancer_configs = load_balancer_configs
        # The IDs of the SLB instances that are associated with the scaling group.
        self.load_balancer_ids = load_balancer_ids
        # The maximum life span of an instance in the scaling group. Unit: seconds.
        # 
        # Valid values: 0 or from 86400 to `Integer.maxValue`. A value of 0 for MaxInstanceLifetime indicates that any previously set limit has been removed, which effectively disables the maximum instance lifetime constraint.
        # 
        # Default value: null.
        # 
        # >  This parameter is not supported by scaling groups of the Elastic Container Instance type and scaling groups whose ScalingPolicy is set to Recycle.
        self.max_instance_lifetime = max_instance_lifetime
        # The maximum number of ECS instances that can be contained in the scaling group.
        self.max_size = max_size
        # The minimum number of ECS instances that must be contained in the scaling group.
        self.min_size = min_size
        # The time when the scaling group was modified.
        self.modification_time = modification_time
        # The ID of the CloudMonitor application group that is associated with the scaling group.
        self.monitor_group_id = monitor_group_id
        # The scaling policy of the ECS instances in the multi-zone scaling group. Valid values:
        # 
        # *   PRIORITY: ECS instances are created based on the value of VSwitchIds. If Auto Scaling cannot create ECS instances in the zone where the vSwitch of the highest priority resides, Auto Scaling creates ECS instances in the zone where the vSwitch of the next highest priority resides.
        # 
        # *   COST_OPTIMIZED: ECS instances are created based on the unit prices of their vCPUs. Auto Scaling preferentially creates ECS instances that use the lowest-priced vCPUs. If preemptible instance types are specified in the scaling configuration, Auto Scaling preferentially creates preemptible instances. You can also specify CompensateWithOnDemand to allow Auto Scaling to create pay-as-you-go instances in the case that preemptible instances cannot be created due to insufficient inventory of preemptible instance types.
        # 
        #     **
        # 
        #     **Note** The COST_OPTIMIZED setting takes effect only if you specified multiple instance types or preemptible instance types in your scaling configuration.
        # 
        # *   BALANCE: ECS instances are evenly distributed across the zones of the scaling group. If ECS instance are unevenly distributed across the specified zones due to insufficient inventory of instance types, you can call the RebalanceInstance operation to rebalance the distribution of the ECS instances.
        self.multi_azpolicy = multi_azpolicy
        # The minimum number of pay-as-you-go instances that must be contained in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances in the scaling group is less than the value of this parameter, Auto Scaling preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the excess instances when the minimum number of pay-as-you-go instances reaches the requirement. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The number of ECS instances that are being added to the scaling group and configured.
        self.pending_capacity = pending_capacity
        # The number of ECS instances that are in the Pending Add state in the scaling group.
        self.pending_wait_capacity = pending_wait_capacity
        # The number of ECS instances that are in the Protected state in the scaling group.
        self.protected_capacity = protected_capacity
        # The region ID of the scaling group.
        self.region_id = region_id
        # The instance removal policies.
        self.removal_policies = removal_policies
        # The number of ECS instances that are being removed from the scaling group.
        self.removing_capacity = removing_capacity
        # The number of ECS instances that are in the Pending Remove state in the scaling group.
        self.removing_wait_capacity = removing_wait_capacity
        # The ID of the resource group to which the scaling group belongs.
        # 
        # >  If you specify this parameter, new scaling groups are added to the specified resource group. If you do not specify this parameter, new scaling groups are added to the default resource group.
        self.resource_group_id = resource_group_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The name of the scaling group. The name of each scaling group must be unique in a region.
        # 
        # The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter or digit.
        self.scaling_group_name = scaling_group_name
        # The reclaim mode of the scaling group. Valid values:
        # 
        # *   recycle: economical mode
        # *   release: release mode
        # *   forcerelease: forced release mode
        # *   forcerecycle: forced recycle mode
        # 
        # For more information, see [RemoveInstances](https://help.aliyun.com/document_detail/25955.html).
        self.scaling_policy = scaling_policy
        # The information about the server groups.
        # 
        # >  You can use this parameter to obtain information about ALB server groups and Network Load Balancer (NLB) server groups attached to your scaling group.
        self.server_groups = server_groups
        # The allocation policy of preemptible instances. Auto Scaling selects instance types based on the allocation policy to create the required number of preemptible instances. You can apply the policy to pay-as-you-go instances and preemptible instances. This parameter takes effect only if you set `MultiAZPolicy` to `COMPOSABLE`. Valid values:
        # 
        # *   priority: Auto Scaling selects instance types based on the specified order to create the required number of preemptible instances.
        # *   lowestPrice: Auto Scaling selects instance types that have the lowest unit price of vCPUs to create the required number of preemptible instances.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The number of instance types that are specified. Preemptible instances of multiple lowest-priced instance types are evenly distributed across the zones of the scaling group. Valid values: 0 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether preemptible instances can be supplemented. If this parameter is set to true, Auto Scaling creates an instance to replace a preemptible instance when Auto Scaling receives the system message which indicates that the preemptible instance is to be reclaimed.
        self.spot_instance_remedy = spot_instance_remedy
        # The number of ECS instances that are in the Standby state in the scaling group.
        self.standby_capacity = standby_capacity
        # The number of instances that are stopped in Economical Mode in the scaling group.
        self.stopped_capacity = stopped_capacity
        # The processes that are suspended. If no process is suspended, null is returned. Valid values:
        # 
        # *   ScaleIn: scale-in
        # *   ScaleOut: scale-out
        # *   HealthCheck: health check
        # *   AlarmNotification: event-triggered task
        # *   ScheduledAction: scheduled task
        self.suspended_processes = suspended_processes
        # Indicates whether Auto Scaling stops executing scaling activities in the scaling group. Valid values:
        # 
        # *   true: Auto Scaling stops executing scaling activities in the scaling group if the scaling activities failed for more than seven consecutive days in the scaling group. You must modify the scaling group or scaling configuration to resume the execution of the scaling activities.
        # *   false: Auto Scaling does not stop executing scaling activities in the scaling group.
        self.system_suspended = system_suspended
        # The tags of the scaling group.
        self.tags = tags
        # The total weighted capacity of all ECS instances in the scaling group if Weighted is specified. In other cases, the value of this parameter indicates the total number of ECS instances in the scaling group.
        self.total_capacity = total_capacity
        # The total number of Elastic Compute Service (ECS) instances in the scaling group.
        self.total_instance_count = total_instance_count
        # The backend vServer groups.
        self.vserver_groups = vserver_groups
        # The vSwitch ID of the scaling group.
        self.v_switch_id = v_switch_id
        # The IDs of the vSwitches that are associated with the scaling group. If you specify VSwitchIds, VSwitchId is ignored.
        self.v_switch_ids = v_switch_ids
        # The virtual private cloud (VPC) ID of the scaling group.
        self.vpc_id = vpc_id

    def validate(self):
        if self.alb_server_groups:
            for v1 in self.alb_server_groups:
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

        if self.az_balance is not None:
            result['AzBalance'] = self.az_balance

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

        if self.spot_instance_pools is not None:
            result['SpotInstancePools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['SpotInstanceRemedy'] = self.spot_instance_remedy

        if self.standby_capacity is not None:
            result['StandbyCapacity'] = self.standby_capacity

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
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupAlbServerGroups()
                self.alb_server_groups.append(temp_model.from_map(k1))

        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        if m.get('AzBalance') is not None:
            self.az_balance = m.get('AzBalance')

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
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupLaunchTemplateOverrides()
                self.launch_template_overrides.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        self.load_balancer_configs = []
        if m.get('LoadBalancerConfigs') is not None:
            for k1 in m.get('LoadBalancerConfigs'):
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupLoadBalancerConfigs()
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
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupServerGroups()
                self.server_groups.append(temp_model.from_map(k1))

        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')

        if m.get('SpotInstancePools') is not None:
            self.spot_instance_pools = m.get('SpotInstancePools')

        if m.get('SpotInstanceRemedy') is not None:
            self.spot_instance_remedy = m.get('SpotInstanceRemedy')

        if m.get('StandbyCapacity') is not None:
            self.standby_capacity = m.get('StandbyCapacity')

        if m.get('StoppedCapacity') is not None:
            self.stopped_capacity = m.get('StoppedCapacity')

        if m.get('SuspendedProcesses') is not None:
            self.suspended_processes = m.get('SuspendedProcesses')

        if m.get('SystemSuspended') is not None:
            self.system_suspended = m.get('SystemSuspended')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('TotalInstanceCount') is not None:
            self.total_instance_count = m.get('TotalInstanceCount')

        self.vserver_groups = []
        if m.get('VServerGroups') is not None:
            for k1 in m.get('VServerGroups'):
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroups()
                self.vserver_groups.append(temp_model.from_map(k1))

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroups(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        vserver_group_attributes: List[main_models.DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroupsVServerGroupAttributes] = None,
    ):
        # The ID of the Classic Load Balancer (CLB, formerly known as Server Load Balancer or SLB) instance to which the backend vServer group belongs.
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
                temp_model = main_models.DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroupsVServerGroupAttributes()
                self.vserver_group_attributes.append(temp_model.from_map(k1))

        return self

class DescribeScalingGroupDetailResponseBodyScalingGroupVServerGroupsVServerGroupAttributes(DaraModel):
    def __init__(
        self,
        port: int = None,
        vserver_group_id: str = None,
        weight: int = None,
    ):
        # The port number of a backend vServer.
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

class DescribeScalingGroupDetailResponseBodyScalingGroupTags(DaraModel):
    def __init__(
        self,
        propagate: bool = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # Indicates whether the tags of the scaling group can be propagated to instances. Valid values:
        # 
        # *   true: The tags of the scaling group can be propagated to only instances that are newly created.
        # *   false: The tags of the scaling group cannot be propagated to any instances.
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

class DescribeScalingGroupDetailResponseBodyScalingGroupServerGroups(DaraModel):
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

class DescribeScalingGroupDetailResponseBodyScalingGroupLoadBalancerConfigs(DaraModel):
    def __init__(
        self,
        load_balancer_id: str = None,
        weight: int = None,
    ):
        # The ID of the CLB instance.
        self.load_balancer_id = load_balancer_id
        # The weight of a backend server.
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

class DescribeScalingGroupDetailResponseBodyScalingGroupLaunchTemplateOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        spot_price_limit: float = None,
        weighted_capacity: int = None,
    ):
        # The instance type. The instance type that is specified by using this parameter overwrites the instance type of the launch template.
        self.instance_type = instance_type
        # The maximum bid price of the instance type that is specified by `LaunchTemplateOverride.InstanceType`.
        # 
        # >  This parameter takes effect only if you specify `LaunchTemplateId`.
        self.spot_price_limit = spot_price_limit
        # The weight of the instance type. The value of this parameter indicates the capacity of an instance of the specified instance type in the scaling group. A higher weight indicates that a smaller number of instances of the specified instance type are required to meet the expected capacity requirement.
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

class DescribeScalingGroupDetailResponseBodyScalingGroupAlbServerGroups(DaraModel):
    def __init__(
        self,
        alb_server_group_id: str = None,
        port: int = None,
        weight: int = None,
    ):
        # The ID of the Application Load Balancer (ALB) server group.
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

