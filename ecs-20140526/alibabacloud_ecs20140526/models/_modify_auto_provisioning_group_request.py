# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class ModifyAutoProvisioningGroupRequest(DaraModel):
    def __init__(
        self,
        auto_provisioning_group_id: str = None,
        auto_provisioning_group_name: str = None,
        default_target_capacity_type: str = None,
        excess_capacity_termination_policy: str = None,
        launch_template_config: List[main_models.ModifyAutoProvisioningGroupRequestLaunchTemplateConfig] = None,
        max_spot_price: float = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_as_you_go_target_capacity: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        spot_target_capacity: str = None,
        terminate_instances_with_expiration: bool = None,
        total_target_capacity: str = None,
    ):
        # The ID of the auto provisioning group.
        self.auto_provisioning_group_id = auto_provisioning_group_id
        # The name of the auto provisioning group. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with http:// or https://. The name can contain digits, colons (:), underscores (_), or hyphens (-).
        self.auto_provisioning_group_name = auto_provisioning_group_name
        # The billing method of the capacity difference when the sum of PayAsYouGoTargetCapacity and SpotTargetCapacity is less than TotalTargetCapacity. Valid values:
        # 
        # - PayAsYouGo: pay-as-you-go instance.
        # - Spot: spot instance.
        self.default_target_capacity_type = default_target_capacity_type
        # Specifies whether to release instances when the real-time capacity of the auto provisioning group exceeds the target capacity and a scale-in event is triggered. Valid values:
        # 
        # - termination: Releases the scaled-in instances.
        # - no-termination: Only removes the scaled-in instances from the auto provisioning group.
        self.excess_capacity_termination_policy = excess_capacity_termination_policy
        # The extended launch template list.
        self.launch_template_config = launch_template_config
        # The maximum price of spot instances in the auto provisioning group.
        # 
        # > If both MaxSpotPrice and LaunchTemplateConfig.N.MaxPrice are specified, the lower value is used. LaunchTemplateConfig.N.MaxPrice is specified in Settings when the auto provisioning group is created and cannot be modified.
        self.max_spot_price = max_spot_price
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The target capacity of pay-as-you-go instances in the auto provisioning group. Valid values: less than the parameter value of TotalTargetCapacity.
        self.pay_as_you_go_target_capacity = pay_as_you_go_target_capacity
        # The region ID of the auto provisioning group. You can invoke [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The target capacity of spot instances in the auto provisioning group. Valid values: less than the parameter value of TotalTargetCapacity.
        self.spot_target_capacity = spot_target_capacity
        # Specifies whether to release instances in the auto provisioning group when the group expires. Valid values:
        # 
        # - true: Releases the instances in the group.
        # - false: Only removes the instances from the auto provisioning group.
        self.terminate_instances_with_expiration = terminate_instances_with_expiration
        # The total target capacity of the auto provisioning group. Valid values: positive integers.
        # 
        # The total capacity must be greater than or equal to the sum of PayAsYouGoTargetCapacity (the target capacity of pay-as-you-go instances) and SpotTargetCapacity (the target capacity of spot instances).
        self.total_target_capacity = total_target_capacity

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
        if self.auto_provisioning_group_id is not None:
            result['AutoProvisioningGroupId'] = self.auto_provisioning_group_id

        if self.auto_provisioning_group_name is not None:
            result['AutoProvisioningGroupName'] = self.auto_provisioning_group_name

        if self.default_target_capacity_type is not None:
            result['DefaultTargetCapacityType'] = self.default_target_capacity_type

        if self.excess_capacity_termination_policy is not None:
            result['ExcessCapacityTerminationPolicy'] = self.excess_capacity_termination_policy

        result['LaunchTemplateConfig'] = []
        if self.launch_template_config is not None:
            for k1 in self.launch_template_config:
                result['LaunchTemplateConfig'].append(k1.to_map() if k1 else None)

        if self.max_spot_price is not None:
            result['MaxSpotPrice'] = self.max_spot_price

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_as_you_go_target_capacity is not None:
            result['PayAsYouGoTargetCapacity'] = self.pay_as_you_go_target_capacity

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.spot_target_capacity is not None:
            result['SpotTargetCapacity'] = self.spot_target_capacity

        if self.terminate_instances_with_expiration is not None:
            result['TerminateInstancesWithExpiration'] = self.terminate_instances_with_expiration

        if self.total_target_capacity is not None:
            result['TotalTargetCapacity'] = self.total_target_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoProvisioningGroupId') is not None:
            self.auto_provisioning_group_id = m.get('AutoProvisioningGroupId')

        if m.get('AutoProvisioningGroupName') is not None:
            self.auto_provisioning_group_name = m.get('AutoProvisioningGroupName')

        if m.get('DefaultTargetCapacityType') is not None:
            self.default_target_capacity_type = m.get('DefaultTargetCapacityType')

        if m.get('ExcessCapacityTerminationPolicy') is not None:
            self.excess_capacity_termination_policy = m.get('ExcessCapacityTerminationPolicy')

        self.launch_template_config = []
        if m.get('LaunchTemplateConfig') is not None:
            for k1 in m.get('LaunchTemplateConfig'):
                temp_model = main_models.ModifyAutoProvisioningGroupRequestLaunchTemplateConfig()
                self.launch_template_config.append(temp_model.from_map(k1))

        if m.get('MaxSpotPrice') is not None:
            self.max_spot_price = m.get('MaxSpotPrice')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayAsYouGoTargetCapacity') is not None:
            self.pay_as_you_go_target_capacity = m.get('PayAsYouGoTargetCapacity')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SpotTargetCapacity') is not None:
            self.spot_target_capacity = m.get('SpotTargetCapacity')

        if m.get('TerminateInstancesWithExpiration') is not None:
            self.terminate_instances_with_expiration = m.get('TerminateInstancesWithExpiration')

        if m.get('TotalTargetCapacity') is not None:
            self.total_target_capacity = m.get('TotalTargetCapacity')

        return self

class ModifyAutoProvisioningGroupRequestLaunchTemplateConfig(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        max_price: float = None,
        priority: int = None,
        v_switch_id: str = None,
        weighted_capacity: float = None,
    ):
        # The instance type specified in the extension launch template. Valid values of N: 1 to 20. For more information, see [Instance family](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type = instance_type
        # The maximum price of the spot instance in the extended launch template.
        self.max_price = max_price
        # The priority of the extended launch template. A value of 0 indicates the highest priority. Valid values: greater than 0.
        self.priority = priority
        # The ID of the vSwitch to which the ECS instance belongs in the extended launch template. The zone of the ECS instance launched from the extended template is determined by the vSwitch.
        self.v_switch_id = v_switch_id
        # The weight of the instance type specified in the extended launch template. A higher value indicates that a single instance can meet more computing requirements, which means fewer instances are required. Valid values: greater than 0.
        # 
        # You can calculate the weight based on the computing power of the specified instance type and the minimum computing power of a single node in the cluster. For example, if the minimum computing power of a single node is 8 vCPUs and 60 GiB:
        # 
        # - The weight of an instance type with 8 vCPUs and 60 GiB can be set to 1.
        # - The weight of an instance type with 16 vCPUs and 120 GiB can be set to 2.
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

