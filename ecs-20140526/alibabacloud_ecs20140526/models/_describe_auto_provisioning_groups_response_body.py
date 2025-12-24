# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeAutoProvisioningGroupsResponseBody(DaraModel):
    def __init__(
        self,
        auto_provisioning_groups: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroups = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # Details about the auto provisioning groups.
        self.auto_provisioning_groups = auto_provisioning_groups
        # The number of the page returned.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The number of queried auto provisioning groups.
        self.total_count = total_count

    def validate(self):
        if self.auto_provisioning_groups:
            self.auto_provisioning_groups.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_groups is not None:
            result['AutoProvisioningGroups'] = self.auto_provisioning_groups.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroups') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroups()
            self.auto_provisioning_groups = temp_model.from_map(m.get('AutoProvisioningGroups'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroups(DaraModel):
    def __init__(
        self,
        auto_provisioning_group: List[main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroup] = None,
    ):
        self.auto_provisioning_group = auto_provisioning_group

    def validate(self):
        if self.auto_provisioning_group:
            for v1 in self.auto_provisioning_group:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AutoProvisioningGroup'] = []
        if self.auto_provisioning_group is not None:
            for k1 in self.auto_provisioning_group:
                result['AutoProvisioningGroup'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.auto_provisioning_group = []
        if m.get('AutoProvisioningGroup') is not None:
            for k1 in m.get('AutoProvisioningGroup'):
                temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroup()
                self.auto_provisioning_group.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroup(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_id: str = None,
        auto_provisioning_group_name: str = None,
        auto_provisioning_group_type: str = None,
        creation_time: str = None,
        excess_capacity_termination_policy: str = None,
        launch_template_configs: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigs = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        max_spot_price: float = None,
        pay_as_you_go_options: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupPayAsYouGoOptions = None,
        region_id: str = None,
        resource_group_id: str = None,
        spot_options: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupSpotOptions = None,
        state: str = None,
        status: str = None,
        tags: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTags = None,
        target_capacity_specification: main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTargetCapacitySpecification = None,
        terminate_instances: bool = None,
        terminate_instances_with_expiration: bool = None,
        valid_from: str = None,
        valid_until: str = None,
    ):
        # The ID of the auto provisioning group.
        self.auto_provisioning_group_id = auto_provisioning_group_id
        # The name of the auto provisioning group.
        self.auto_provisioning_group_name = auto_provisioning_group_name
        # The delivery type of the auto provisioning group. Valid values:
        # 
        # *   request: one-time delivery. When the auto provisioning group is started, it delivers instances only once. If the instances fail to be delivered, the auto provisioning group does not retry the delivery.
        # *   maintain: continuous delivery. When the auto provisioning group is started, it attempts to deliver instances that meet the target capacity and monitors the real-time capacity. If the target capacity of the auto provisioning group is not reached, the auto provisioning group continues to create instances until the target capacity is reached.
        self.auto_provisioning_group_type = auto_provisioning_group_type
        # The time when the auto provisioning group was created.
        self.creation_time = creation_time
        # Indicates whether to release the scaled-in instances when the real-time capacity of the auto provisioning group exceeds the target capacity and the group is triggered to scale in. Valid values:
        # 
        # *   termination: releases the scaled-in instances.
        # *   no-termination: only removes the scaled-in instances from the auto provisioning group but does not release the instances.
        self.excess_capacity_termination_policy = excess_capacity_termination_policy
        # Details about the extended configurations.
        self.launch_template_configs = launch_template_configs
        # The ID of the launch template associated with the auto provisioning group.
        self.launch_template_id = launch_template_id
        # The version of the launch template associated with the auto provisioning group.
        self.launch_template_version = launch_template_version
        # The maximum price of spot  instances in the auto provisioning group.
        # 
        # >  When both the MaxSpotPrice and LaunchTemplateConfig.N.MaxPrice parameters are specified, the smaller one of the two parameter values is used.
        # 
        # The LaunchTemplateConfig.N.Priority parameter is set when the auto provisioning group is created, and cannot be modified.
        self.max_spot_price = max_spot_price
        # The policies related to pay-as-you-go instances.
        self.pay_as_you_go_options = pay_as_you_go_options
        # The region ID of the auto provisioning group.
        self.region_id = region_id
        # The ID of the resource group to which the auto provisioning group belongs.
        self.resource_group_id = resource_group_id
        # The policy related to spot instances.
        self.spot_options = spot_options
        # The overall status of instance scheduling in the auto provisioning group. Valid values:
        # 
        # *   fulfilled: Scheduling was complete and the instances were delivered.
        # *   pending-fulfillment: The instances were being created.
        # *   pending-termination: The instances were being removed.
        # *   error: An exception occurred during scheduling and the instances were not delivered.
        self.state = state
        # The status of the auto provisioning group. Valid values:
        # 
        # *   submitted: The auto provisioning group was created but did not execute scheduling tasks.
        # *   active: The auto provisioning group was executing scheduling tasks.
        # *   deleted: The auto provisioning group was deleted.
        # *   delete-running: The auto provisioning group was being deleted.
        # *   modifying: The auto provisioning group was being modified.
        self.status = status
        # The tags that are added to the auto provisioning group.
        self.tags = tags
        # The settings of the target capacity of the auto provisioning group.
        self.target_capacity_specification = target_capacity_specification
        # Indicates whether to release instances in the auto provisioning group when the auto provisioning group is deleted. Valid values:
        # 
        # *   true: releases the instances.
        # *   false: only removes the instances from the auto provisioning group but does not release the instances.
        self.terminate_instances = terminate_instances
        # Indicates whether to release instances in the auto provisioning group when the group expires. Valid values:
        # 
        # *   true: releases the instances.
        # *   false: only removes the instances from the auto provisioning group but does not release the instances.
        self.terminate_instances_with_expiration = terminate_instances_with_expiration
        # The time at which the auto provisioning group is started. The provisioning group is effective until the point in time specified by `ValidUntil`.
        self.valid_from = valid_from
        # The time at which the auto provisioning group expires. The period of time between this point in time and the point in time specified by the `ValidFrom` parameter is the validity period of the auto provisioning group.
        self.valid_until = valid_until

    def validate(self):
        if self.launch_template_configs:
            self.launch_template_configs.validate()
        if self.pay_as_you_go_options:
            self.pay_as_you_go_options.validate()
        if self.spot_options:
            self.spot_options.validate()
        if self.tags:
            self.tags.validate()
        if self.target_capacity_specification:
            self.target_capacity_specification.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id

        if self.auto_provisioning_group_name is not None:
            result['AutoProvisioningGroupName'] = self.auto_provisioning_group_name

        if self.auto_provisioning_group_type is not None:
            result['AutoProvisioningGroupType'] = self.auto_provisioning_group_type

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.excess_capacity_termination_policy is not None:
            result['ExcessCapacityTerminationPolicy'] = self.excess_capacity_termination_policy

        if self.launch_template_configs is not None:
            result['LaunchTemplateConfigs'] = self.launch_template_configs.to_map()

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.max_spot_price is not None:
            result['MaxSpotPrice'] = self.max_spot_price

        if self.pay_as_you_go_options is not None:
            result['PayAsYouGoOptions'] = self.pay_as_you_go_options.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.spot_options is not None:
            result['SpotOptions'] = self.spot_options.to_map()

        if self.state is not None:
            result['State'] = self.state

        if self.status is not None:
            result['Status'] = self.status

        if self.tags is not None:
            result['Tags'] = self.tags.to_map()

        if self.target_capacity_specification is not None:
            result['TargetCapacitySpecification'] = self.target_capacity_specification.to_map()

        if self.terminate_instances is not None:
            result['TerminateInstances'] = self.terminate_instances

        if self.terminate_instances_with_expiration is not None:
            result['TerminateInstancesWithExpiration'] = self.terminate_instances_with_expiration

        if self.valid_from is not None:
            result['ValidFrom'] = self.valid_from

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')

        if m.get('AutoProvisioningGroupName') is not None:
            self.auto_provisioning_group_name = m.get('AutoProvisioningGroupName')

        if m.get('AutoProvisioningGroupType') is not None:
            self.auto_provisioning_group_type = m.get('AutoProvisioningGroupType')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('ExcessCapacityTerminationPolicy') is not None:
            self.excess_capacity_termination_policy = m.get('ExcessCapacityTerminationPolicy')

        if m.get('LaunchTemplateConfigs') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigs()
            self.launch_template_configs = temp_model.from_map(m.get('LaunchTemplateConfigs'))

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('MaxSpotPrice') is not None:
            self.max_spot_price = m.get('MaxSpotPrice')

        if m.get('PayAsYouGoOptions') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupPayAsYouGoOptions()
            self.pay_as_you_go_options = temp_model.from_map(m.get('PayAsYouGoOptions'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SpotOptions') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupSpotOptions()
            self.spot_options = temp_model.from_map(m.get('SpotOptions'))

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Tags') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTags()
            self.tags = temp_model.from_map(m.get('Tags'))

        if m.get('TargetCapacitySpecification') is not None:
            temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTargetCapacitySpecification()
            self.target_capacity_specification = temp_model.from_map(m.get('TargetCapacitySpecification'))

        if m.get('TerminateInstances') is not None:
            self.terminate_instances = m.get('TerminateInstances')

        if m.get('TerminateInstancesWithExpiration') is not None:
            self.terminate_instances_with_expiration = m.get('TerminateInstancesWithExpiration')

        if m.get('ValidFrom') is not None:
            self.valid_from = m.get('ValidFrom')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTargetCapacitySpecification(DaraModel):
    def __init__(
        self,
        default_target_capacity_type: str = None,
        pay_as_you_go_target_capacity: float = None,
        spot_target_capacity: float = None,
        total_target_capacity: float = None,
    ):
        # The type of supplemental instances. When the sum of the `PayAsYouGoTargetCapacity` and `SpotTargetCapacity` values is less than the `TotalTargetCapacity` value, the auto provisioning group creates instances of the specified billing method to meet the target capacity. Valid values:
        # 
        # *   PayAsYouGo: pay-as-you-go instances.
        # *   Spot: spot instances.
        self.default_target_capacity_type = default_target_capacity_type
        # The target capacity of pay-as-you-go instances that the auto provisioning group provisions.
        self.pay_as_you_go_target_capacity = pay_as_you_go_target_capacity
        # The target capacity of spot instances that the auto provisioning group provisions.
        self.spot_target_capacity = spot_target_capacity
        # The target capacity of the auto provisioning group. The capacity consists of the following parts:
        # 
        # *   PayAsYouGoTargetCapacity
        # *   SpotTargetCapacity
        # *   The supplemental capacity besides instance capacities specified by PayAsYouGoTargetCapacity and SpotTargetCapacity.
        self.total_target_capacity = total_target_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_target_capacity_type is not None:
            result['DefaultTargetCapacityType'] = self.default_target_capacity_type

        if self.pay_as_you_go_target_capacity is not None:
            result['PayAsYouGoTargetCapacity'] = self.pay_as_you_go_target_capacity

        if self.spot_target_capacity is not None:
            result['SpotTargetCapacity'] = self.spot_target_capacity

        if self.total_target_capacity is not None:
            result['TotalTargetCapacity'] = self.total_target_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultTargetCapacityType') is not None:
            self.default_target_capacity_type = m.get('DefaultTargetCapacityType')

        if m.get('PayAsYouGoTargetCapacity') is not None:
            self.pay_as_you_go_target_capacity = m.get('PayAsYouGoTargetCapacity')

        if m.get('SpotTargetCapacity') is not None:
            self.spot_target_capacity = m.get('SpotTargetCapacity')

        if m.get('TotalTargetCapacity') is not None:
            self.total_target_capacity = m.get('TotalTargetCapacity')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTags(DaraModel):
    def __init__(
        self,
        tag: List[main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTagsTag] = None,
    ):
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTagsTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupTagsTag(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of tag N that is added to the auto provisioning group.
        # 
        # Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length and cannot contain http:// or https://. The tag key cannot start with acs: or aliyun.
        self.tag_key = tag_key
        # The value of tag N that is added to the auto provisioning group.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupSpotOptions(DaraModel):
    def __init__(
        self,
        allocation_strategy: str = None,
        instance_interruption_behavior: str = None,
        instance_pools_to_use_count: int = None,
    ):
        # The policy for creating spot instances. Valid values:
        # 
        # *   lowest-price: cost optimization policy. This policy indicates that the lowest-priced instance type is used to create instances.
        # *   diversified: balanced distribution policy. This policy indicates that instances are created evenly across multiple zones specified in the extended configuration.
        self.allocation_strategy = allocation_strategy
        # The action to be performed after the excess spot instances are stopped. Valid values:
        # 
        # *   stop: retains the excess spot instances in the stopped state.
        # *   terminate: releases the excess spot instances.
        self.instance_interruption_behavior = instance_interruption_behavior
        # The number of instances that the auto provisioning group creates by selecting the instance type of the lowest price.
        # 
        # >  This parameter is set when the auto provisioning group is created, and cannot be modified.
        self.instance_pools_to_use_count = instance_pools_to_use_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy

        if self.instance_interruption_behavior is not None:
            result['InstanceInterruptionBehavior'] = self.instance_interruption_behavior

        if self.instance_pools_to_use_count is not None:
            result['InstancePoolsToUseCount'] = self.instance_pools_to_use_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        if m.get('InstanceInterruptionBehavior') is not None:
            self.instance_interruption_behavior = m.get('InstanceInterruptionBehavior')

        if m.get('InstancePoolsToUseCount') is not None:
            self.instance_pools_to_use_count = m.get('InstancePoolsToUseCount')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupPayAsYouGoOptions(DaraModel):
    def __init__(
        self,
        allocation_strategy: str = None,
    ):
        # The policy for creating pay-as-you-go instances. Valid values:
        # 
        # *   lowest-price: cost optimization policy. This policy indicates that lowest-cost instance types are used to create instances.
        # *   prioritized: priority-based policy. This policy indicates that instances are created based on the priority specified by the LaunchTemplateConfig.N.Priority parameter.
        # 
        # >  The LaunchTemplateConfig.N.Priority parameter is set when the auto provisioning group is created, and cannot be modified.
        self.allocation_strategy = allocation_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_strategy is not None:
            result['AllocationStrategy'] = self.allocation_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationStrategy') is not None:
            self.allocation_strategy = m.get('AllocationStrategy')

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigs(DaraModel):
    def __init__(
        self,
        launch_template_config: List[main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigsLaunchTemplateConfig] = None,
    ):
        self.launch_template_config = launch_template_config

    def validate(self):
        if self.launch_template_config:
            for v1 in self.launch_template_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LaunchTemplateConfig'] = []
        if self.launch_template_config is not None:
            for k1 in self.launch_template_config:
                result['LaunchTemplateConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.launch_template_config = []
        if m.get('LaunchTemplateConfig') is not None:
            for k1 in m.get('LaunchTemplateConfig'):
                temp_model = main_models.DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigsLaunchTemplateConfig()
                self.launch_template_config.append(temp_model.from_map(k1))

        return self

class DescribeAutoProvisioningGroupsResponseBodyAutoProvisioningGroupsAutoProvisioningGroupLaunchTemplateConfigsLaunchTemplateConfig(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        max_price: float = None,
        priority: float = None,
        v_switch_id: str = None,
        weighted_capacity: float = None,
    ):
        # The instance type that is specified in the extended configuration.
        self.instance_type = instance_type
        # The maximum price of the instance type specified in the extended configuration.
        self.max_price = max_price
        # The priority of the instance type specified in the extended configuration. A value of 0 indicates the highest priority.
        self.priority = priority
        # The ID of the vSwitch specified in the extended configuration.
        self.v_switch_id = v_switch_id
        # The weight of the instance type specified in the extended configuration.
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

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        return self

