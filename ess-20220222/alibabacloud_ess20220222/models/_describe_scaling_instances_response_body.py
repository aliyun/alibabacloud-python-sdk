# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingInstancesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_instances: List[main_models.DescribeScalingInstancesResponseBodyScalingInstances] = None,
        total_count: int = None,
        total_spot_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The ECS instances.
        self.scaling_instances = scaling_instances
        # The total number of ECS instances in the scaling group.
        self.total_count = total_count
        # The total number of preemptible instances that run as expected in the scaling group.
        self.total_spot_count = total_spot_count

    def validate(self):
        if self.scaling_instances:
            for v1 in self.scaling_instances:
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

        result['ScalingInstances'] = []
        if self.scaling_instances is not None:
            for k1 in self.scaling_instances:
                result['ScalingInstances'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_spot_count is not None:
            result['TotalSpotCount'] = self.total_spot_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scaling_instances = []
        if m.get('ScalingInstances') is not None:
            for k1 in m.get('ScalingInstances'):
                temp_model = main_models.DescribeScalingInstancesResponseBodyScalingInstances()
                self.scaling_instances.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalSpotCount') is not None:
            self.total_spot_count = m.get('TotalSpotCount')

        return self

class DescribeScalingInstancesResponseBodyScalingInstances(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        creation_time: str = None,
        creation_type: str = None,
        entrusted: bool = None,
        health_status: str = None,
        instance_id: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        private_ip_address: str = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
        scaling_instance_id: str = None,
        spot_strategy: str = None,
        warmup_state: str = None,
        weighted_capacity: int = None,
        zone_id: str = None,
    ):
        # The time when the ECS instances were added to the scaling group. The value is accurate to the second.
        self.created_time = created_time
        # The time when the ECS instances were added to the scaling group. The value is accurate to the minute.
        self.creation_time = creation_time
        # The instance creation method. Valid values:
        # 
        # *   AutoCreated: The ECS instances are created by Auto Scaling based on the instance configuration source.
        # *   Attached: The ECS instances are manually added to the scaling group.
        self.creation_type = creation_type
        # Indicates whether the scaling group is allowed to manage the instance lifecycles when ECS instances are manually added. If the scaling group is allowed to manage the instance lifecycles, Auto Scaling can release the ECS instances when the instances are automatically removed from the scaling group. Valid values:
        # 
        # *   true
        # *   false
        self.entrusted = entrusted
        # The health status of the ECS instance in the scaling group. If an ECS instance is not in the Running state, the instance is considered unhealthy. Valid values:
        # 
        # *   Healthy
        # *   Unhealthy
        # 
        # Auto Scaling automatically removes unhealthy ECS instances from the scaling group and then releases the automatically created instances among the unhealthy instances.
        # 
        # Unhealthy ECS instances that are manually added to the scaling group are released based on the management mode of the lifecycles of the instances. If the lifecycles of the ECS instances are not managed by the scaling group, Auto Scaling removes the instances from the scaling group but does not release the instances. If the lifecycles of the ECS instances are managed by the scaling group, Auto Scaling removes the instances from the scaling group and releases the instances.
        # 
        # >  Make sure that you have sufficient balance within your Alibaba Cloud account. If your Alibaba Cloud account has an overdue payment, all pay-as-you-go ECS instances, including preemptible instances, may be stopped or even released. For information about how the status of ECS instances changes when you have an overdue payment in your Alibaba Cloud account, see [Overdue payments](https://help.aliyun.com/document_detail/170589.html).
        self.health_status = health_status
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the launch template.
        self.launch_template_id = launch_template_id
        # The version number of the launch template.
        self.launch_template_version = launch_template_version
        # The lifecycle status of the ECS instance in the scaling group. Valid values:
        # 
        # *   InService: The ECS instance is added to the scaling group and provides services as expected.
        # *   Pending: The ECS instance is being added to the scaling group. When an ECS instance is being added to the scaling group, Auto Scaling also adds the instance to the backend server groups of the attached load balancers and adds the private IP address of the instance to the IP address whitelists of the attached ApsaraDB RDS instances.
        # *   Pending:Wait: The ECS instance is waiting to be added to the scaling group. If a scale-out lifecycle hook is in effect, the ECS instance remains in the Pending:Wait state until the timeout period for the lifecycle hook expires.
        # *   Protected: The ECS instance is protected. Protected ECS instances can continue to provide services as expected, but Auto Scaling does not manage the lifecycles of the ECS instances. You must manually manage the lifecycles of the ECS instances.
        # *   Standby: The ECS instance is on standby. Standby ECS instances do not provide services as expected, and the weights of the ECS instances as backend servers are reset to zero. Auto Scaling does not manage the lifecycles of the ECS instances. Therefore, you must manually manage the lifecycles of the ECS instances.
        # *   Stopped: The ECS instance is stopped. Stopped ECS instances no longer provide services.
        # *   Removing: The ECS instance is being removed from the scaling group. When an ECS instance is being removed from the scaling group, Auto Scaling also removes the instance from the backend server groups of the attached load balancers and removes the private IP address of the instance from the IP address whitelists of the attached ApsaraDB RDS instances.
        # *   Removing:Wait: The ECS instance is waiting to be removed from the scaling group. If a scale-in lifecycle hook is in effect, the ECS instance remains in the Removing:Wait state until the timeout period for the lifecycle hook expires.
        self.lifecycle_state = lifecycle_state
        # The weight of each ECS instance as a backend server.
        # 
        # >  This parameter is deprecated and is not recommended.
        self.load_balancer_weight = load_balancer_weight
        # The private IP address of the ECS instance.
        self.private_ip_address = private_ip_address
        # The ID of the scaling activity during which the ECS instances were added to the scaling group.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The ID of the ECS instance or elastic container instance.
        self.scaling_instance_id = scaling_instance_id
        # The bidding policy for the preemptible instances. Valid values:
        # 
        # *   SpotWithPriceLimit: The instances are preemptible instances that have a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are preemptible instances for which the market price at the time of purchase is automatically used as the bidding price.
        self.spot_strategy = spot_strategy
        # The warm-up status of the ECS instances. Valid values:
        # 
        # *   NoNeedWarmup: The ECS instances do not need to undergo a warm-up process.
        # *   WaitingForInstanceWarmup: The ECS instances are undergoing the warm-up process.
        # *   InstanceWarmupFinish: The warm-up process for the ECS instances is complete.
        self.warmup_state = warmup_state
        # The weight of the instance type. The weight indicates the capacity of a single instance of the specified instance type in the scaling group. A higher weight indicates that a smaller number of instances of the instance type are required to meet the expected capacity requirement.
        self.weighted_capacity = weighted_capacity
        # The zone ID of the ECS instances.
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.creation_type is not None:
            result['CreationType'] = self.creation_type

        if self.entrusted is not None:
            result['Entrusted'] = self.entrusted

        if self.health_status is not None:
            result['HealthStatus'] = self.health_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight

        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address

        if self.scaling_activity_id is not None:
            result['ScalingActivityId'] = self.scaling_activity_id

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scaling_instance_id is not None:
            result['ScalingInstanceId'] = self.scaling_instance_id

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.warmup_state is not None:
            result['WarmupState'] = self.warmup_state

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreationType') is not None:
            self.creation_type = m.get('CreationType')

        if m.get('Entrusted') is not None:
            self.entrusted = m.get('Entrusted')

        if m.get('HealthStatus') is not None:
            self.health_status = m.get('HealthStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')

        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')

        if m.get('ScalingActivityId') is not None:
            self.scaling_activity_id = m.get('ScalingActivityId')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('ScalingInstanceId') is not None:
            self.scaling_instance_id = m.get('ScalingInstanceId')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('WarmupState') is not None:
            self.warmup_state = m.get('WarmupState')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

