# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeWarmPoolInstancesResponseBody(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        scaling_group_id: str = None,
        warm_pool_instances: List[main_models.DescribeWarmPoolInstancesResponseBodyWarmPoolInstances] = None,
    ):
        # The token for the next query. An empty NextToken value indicates that no more results are available.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The list of ECS instances in the warm pool.
        self.warm_pool_instances = warm_pool_instances

    def validate(self):
        if self.warm_pool_instances:
            for v1 in self.warm_pool_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        result['WarmPoolInstances'] = []
        if self.warm_pool_instances is not None:
            for k1 in self.warm_pool_instances:
                result['WarmPoolInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        self.warm_pool_instances = []
        if m.get('WarmPoolInstances') is not None:
            for k1 in m.get('WarmPoolInstances'):
                temp_model = main_models.DescribeWarmPoolInstancesResponseBodyWarmPoolInstances()
                self.warm_pool_instances.append(temp_model.from_map(k1))

        return self

class DescribeWarmPoolInstancesResponseBodyWarmPoolInstances(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        instance_id: str = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        lifecycle_state: str = None,
        private_ip_address: str = None,
        scaling_activity_id: str = None,
        scaling_configuration_id: str = None,
        scaling_group_id: str = None,
        scaling_instance_id: str = None,
        zone_id: str = None,
    ):
        # The time when the ECS instance was added to the warm pool, accurate to the second. The time is in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mm:ssZ format.
        self.created_time = created_time
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # The ID of the instance launch template.
        self.launch_template_id = launch_template_id
        # The version of the instance launch template.
        self.launch_template_version = launch_template_version
        # The lifecycle state of the ECS instance in the warm pool. Valid values:
        # 
        # - Pending: The ECS instance is being added to the warm pool.
        # 
        # - Pending:Wait: The addition of the ECS instance is suspended. If a lifecycle hook that applies to scale-out activities for the warm pool is created in the scaling group, the ECS instance is suspended when it is added to the warm pool and waits for the lifecycle hook to time out.
        # 
        # - Removing: The ECS instance is being removed from the warm pool.
        # 
        # - Removing:Wait: The removal of the ECS instance is suspended. If a lifecycle hook that applies to scale-in activities for the warm pool is created in the scaling group, the ECS instance is suspended when it is removed from the warm pool and waits for the lifecycle hook to time out.
        # 
        # - Running: The ECS instance is successfully added to the warm pool and is in the running state.
        # 
        # - Stopped: The ECS instance is successfully added to the warm pool and is in the economical mode.
        self.lifecycle_state = lifecycle_state
        # The private IP address of the instance.
        self.private_ip_address = private_ip_address
        # The ID of the scaling activity when the ECS instance was added to the warm pool.
        self.scaling_activity_id = scaling_activity_id
        # The ID of the associated scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The instance identity in the scaling group, which corresponds one-to-one with the ID of the ECS instance.
        self.scaling_instance_id = scaling_instance_id
        # The zone ID of the ECS instance.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

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

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

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

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

