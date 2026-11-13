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
        # The current page number.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The collection of ECS instance information.
        self.scaling_instances = scaling_instances
        # The total number of ECS instances.
        self.total_count = total_count
        # The total number of running spot instances in the scaling group.
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
        replace_status: str = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
        scaling_instance_id: str = None,
        spot_strategy: str = None,
        warmup_state: str = None,
        weighted_capacity: int = None,
        zone_id: str = None,
    ):
        # The time when the ECS instance was added to the scaling group. The time is accurate to seconds and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format. The time is displayed in UTC.
        self.created_time = created_time
        # The time when the ECS instance was added to the scaling group. The time is accurate to minutes and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The creation type of the ECS instance. Valid values: 
        # 
        # - AutoCreated: The ECS instance is created by Auto Scaling through automatic creation based on the instance configuration source. 
        # - Attached: The ECS instance is not created by Auto Scaling, but is manually added to the scaling group.
        self.creation_type = creation_type
        # Specifies whether the instance is managed by the scaling group when it is manually added to the scaling group. A manually added instance in the managed state is released when it is removed from the scaling group, excluding manual removal. Valid values:
        # - true: The instance is managed by the scaling group.
        # - false: The instance is not managed by the scaling group.
        self.entrusted = entrusted
        # The health status of the ECS instance in the scaling group. ECS instances that are not in the Running state are considered unhealthy. Valid values: 
        # 
        # - Healthy: The ECS instance is healthy. 
        # - Unhealthy: The ECS instance is unhealthy. 
        # 
        # Auto Scaling automatically removes unhealthy ECS instances from the scaling group and releases ECS instances created through automatic creation.
        # 
        # Whether to release manually added ECS instances depends on their managed state. If the instance lifecycle is not managed by the scaling group, the instance is only removed but not released. If the instance lifecycle is managed by the scaling group, the instance is removed and released.
        # 
        # > Make sure that your account has sufficient active balance. If your account has overdue payments, all pay-as-you-go ECS instances, including pay-as-you-go instances and spot instances, are stopped or even released. For more information about the instance status changes of ECS instances in a scaling group after overdue payments, see [Overdue payments](https://help.aliyun.com/document_detail/170589.html).
        self.health_status = health_status
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the instance launch template.
        self.launch_template_id = launch_template_id
        # The version of the instance launch template.
        self.launch_template_version = launch_template_version
        # The lifecycle state of the ECS instance in the scaling group. Valid values:
        #  
        # - InService: The ECS instance is added to the scaling group and provides services normally. 
        # - Pending: The ECS instance is being added to the scaling group. The procedure of adding an ECS instance to a scaling group includes adding the instance to the backend server group of a load balancing instance and adding the IP address of the instance to the access whitelist of an ApsaraDB RDS instance.
        # - Pending:Wait: The addition of the ECS instance to the scaling group is suspended. If a lifecycle hook applicable to scale-out activities is created in the scaling group, the ECS instance is suspended when it is added to the scaling group and waits for the hook timeout to end.
        # - Protected: The ECS instance provides services normally, but Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Standby: The ECS instance does not provide services, the weight of SLB backend server is set to zero, and Auto Scaling does not manage the lifecycle of the ECS instance. You must manually manage the lifecycle.
        # - Stopped: The ECS instance is stopped and does not provide services.
        # - Removing: The ECS instance is being removed from the scaling group. The procedure of removing an ECS instance from a scaling group includes removing the instance from the backend server group of a load balancing instance and removing the IP address of the instance from the access whitelist of an ApsaraDB RDS instance. 
        # - Removing:Wait: The removal of the ECS instance from the scaling group is suspended. If a lifecycle hook applicable to scale-down activities is created in the scaling group, the ECS instance is suspended when it is removed from the scaling group and waits for the hook timeout to end.
        self.lifecycle_state = lifecycle_state
        # The weight of the SLB backend server.
        # > **[Deprecated]** This parameter is deprecated. Do not use it.
        self.load_balancer_weight = load_balancer_weight
        # The internal IP address of the instance in the scaling group.
        self.private_ip_address = private_ip_address
        # The instance replacement process that the instance is in. Valid values:
        # - Normal: The instance is not in any replacement process.
        # - ReBalance: The instance is in the rebalancing replacement process of the scaling group.
        # - SpotRemedy: The instance is in the spot instance remedy replacement process.
        # - MaxInstanceLifetimeExpire: The instance is in the replacement process due to the expiration of the maximum instance lifetime.
        # - InstanceRefresh: The instance is in the instance refresh replacement process.
        # - SpotReplaceOnDemand: The instance is in the process of replacing a spot instance with a pay-as-you-go instance.
        self.replace_status = replace_status
        # The ID of the scaling activity when the ECS instance was added to the scaling group.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the associated scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The ID of the scaling group to which the instance belongs.
        self.scaling_group_id = scaling_group_id
        # The instance identity in the scaling group, which corresponds one-to-one with the ID of the ECS instance or elastic container instance.
        self.scaling_instance_id = scaling_instance_id
        # The bidding policy for the spot instance. Valid values:
        # 
        # - SpotWithPriceLimit: The spot instance with a maximum price.
        # - SpotAsPriceGo: The system automatically bids based on the current market price.
        self.spot_strategy = spot_strategy
        # The warmup status of the ECS instance. Valid values: 
        #          
        # - NoNeedWarmup: No warmup is required.
        # - WaitingForInstanceWarmup: The instance is waiting for the warmup to complete.
        # - InstanceWarmupFinish: The warmup is complete.
        self.warmup_state = warmup_state
        # The weight of the instance type, which indicates the capacity of a single instance of the instance type in the scaling group. A greater weight indicates that fewer instances of the instance type are required to meet the expected capacity.
        self.weighted_capacity = weighted_capacity
        # The ID of the zone to which the ECS instance belongs.
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

        if self.replace_status is not None:
            result['ReplaceStatus'] = self.replace_status

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

        if m.get('ReplaceStatus') is not None:
            self.replace_status = m.get('ReplaceStatus')

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

