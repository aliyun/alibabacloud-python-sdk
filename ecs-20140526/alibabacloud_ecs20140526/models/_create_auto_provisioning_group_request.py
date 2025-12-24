# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class CreateAutoProvisioningGroupRequest(DaraModel):
    def __init__(
        self,
        launch_configuration: main_models.CreateAutoProvisioningGroupRequestLaunchConfiguration = None,
        auto_provisioning_group_name: str = None,
        auto_provisioning_group_type: str = None,
        client_token: str = None,
        data_disk_config: List[main_models.CreateAutoProvisioningGroupRequestDataDiskConfig] = None,
        default_target_capacity_type: str = None,
        description: str = None,
        excess_capacity_termination_policy: str = None,
        execution_mode: str = None,
        hibernation_options_configured: bool = None,
        launch_template_config: List[main_models.CreateAutoProvisioningGroupRequestLaunchTemplateConfig] = None,
        launch_template_id: str = None,
        launch_template_version: str = None,
        max_spot_price: float = None,
        min_target_capacity: str = None,
        owner_account: str = None,
        owner_id: int = None,
        pay_as_you_go_allocation_strategy: str = None,
        pay_as_you_go_target_capacity: str = None,
        pre_paid_options: main_models.CreateAutoProvisioningGroupRequestPrePaidOptions = None,
        region_id: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        resource_pool_options: main_models.CreateAutoProvisioningGroupRequestResourcePoolOptions = None,
        spot_allocation_strategy: str = None,
        spot_instance_interruption_behavior: str = None,
        spot_instance_pools_to_use_count: int = None,
        spot_target_capacity: str = None,
        system_disk_config: List[main_models.CreateAutoProvisioningGroupRequestSystemDiskConfig] = None,
        tag: List[main_models.CreateAutoProvisioningGroupRequestTag] = None,
        terminate_instances: bool = None,
        terminate_instances_with_expiration: bool = None,
        total_target_capacity: str = None,
        valid_from: str = None,
        valid_until: str = None,
    ):
        self.launch_configuration = launch_configuration
        # The name of the auto provisioning group. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.auto_provisioning_group_name = auto_provisioning_group_name
        # The delivery type of the auto provisioning group. Valid values:
        # 
        # *   request: one-time asynchronous delivery. When the auto provisioning group is started, it attempts to asynchronously deliver an instance cluster that meets the target capacity only once. The group does not retry the operation regardless of whether all the instances are delivered.
        # *   instant: one-time synchronous delivery. When the auto provisioning group is started, it attempts to synchronously deliver an instance cluster that meets the target capacity only once. The list of delivered instances and the causes of delivery failures are returned in the response.
        # *   maintain: continuous delivery. When the auto provisioning group is started, it attempts to deliver an instance cluster that meets the target capacity, and monitors the real-time capacity. If the target capacity of the auto provisioning group is not reached, the auto provisioning group continues to create instances until the target capacity is reached.
        # 
        # Default value: maintain.
        self.auto_provisioning_group_type = auto_provisioning_group_type
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The information of data disks on the instance.
        self.data_disk_config = data_disk_config
        # The type of supplemental instances. When the sum of the `PayAsYouGoTargetCapacity` and `SpotTargetCapacity` values is smaller than the `TotalTargetCapacity` value, the auto provisioning group creates instances of the specified type to meet the total target capacity. Valid values:
        # 
        # *   PayAsYouGo: pay-as-you-go
        # *   Spot: spot instance
        # 
        # Default value: Spot.
        self.default_target_capacity_type = default_target_capacity_type
        # The description of the auto provisioning group.
        self.description = description
        # Specifies whether to release scaled-in instances when the real-time capacity of the auto provisioning group exceeds the target capacity and the group is triggered to scale in. Valid values:
        # 
        # *   termination: releases the scaled-in instances in the auto provisioning group.
        # *   no-termination: removes the scaled-in instances from the auto provisioning group but does not release the instances.
        # 
        # Default value: no-termination.
        self.excess_capacity_termination_policy = excess_capacity_termination_policy
        self.execution_mode = execution_mode
        # >This parameter is in invitational preview and is not publicly available.
        self.hibernation_options_configured = hibernation_options_configured
        # The extended configurations of the launch template.
        self.launch_template_config = launch_template_config
        # The ID of the launch template associated with the auto provisioning group. You can call the [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html) operation to query available launch templates. When both LaunchTemplateId and `LaunchConfiguration.*` parameters are specified, LaunchTemplateId takes precedence.
        self.launch_template_id = launch_template_id
        # The version of the launch template associated with the auto provisioning group. You can call the [DescribeLaunchTemplateVersions](https://help.aliyun.com/document_detail/73761.html) operation to query the versions of available launch templates.
        # 
        # Default value: the default version of the launch template.
        self.launch_template_version = launch_template_version
        # The maximum price of spot instances in the auto provisioning group.
        # 
        # >  When both `MaxSpotPrice` and `LaunchTemplateConfig.N.MaxPrice` are specified, the smaller one of the two parameter values is used.
        self.max_spot_price = max_spot_price
        # The minimum target capacity of the auto provisioning group. The value must be a positive integer. When you specify this parameter, take note of the following items:
        # 
        # - This parameter takes effect only when `AutoProvisioningGroupType` is set to instant. 
        # - If the number of instances that can be created in the current region is smaller than the value of this parameter, the operation cannot be called and no instances are created. 
        # - If the number of instances that can be created in the current region is greater than the value of this parameter, instances can be created based on the specified parameters.
        self.min_target_capacity = min_target_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The policy for creating pay-as-you-go instances. Valid values:
        # 
        # *   lowest-price: cost optimization policy. The auto provisioning group selects the lowest-priced instance type to create instances.
        # *   prioritized: priority-based policy. The auto provisioning group creates instances based on the priority specified by `LaunchTemplateConfig.N.Priority`.
        # 
        # Default value: lowest-price.
        self.pay_as_you_go_allocation_strategy = pay_as_you_go_allocation_strategy
        # The target capacity of pay-as-you-go instances in the auto provisioning group. The value must be less than or equal to the `TotalTargetCapacity` value.
        self.pay_as_you_go_target_capacity = pay_as_you_go_target_capacity
        # The capacity details of the subscription instance.
        self.pre_paid_options = pre_paid_options
        # The ID of the region in which to create the auto provisioning group. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the resource group to which to assign the auto provisioning group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource pool options to use to create instances. When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the auto provisioning group creates pay-as-you-go instances.
        # *   This parameter takes effect only if you set `AutoProvisioningGroupType` to instant.
        self.resource_pool_options = resource_pool_options
        # The policy for creating spot instances. Valid values:
        # 
        # *   lowest-price: cost optimization policy. The auto provisioning group selects the lowest-priced instance type to create instances.
        # *   diversified: balanced distribution policy. The auto provisioning group creates instances in zones that are specified in extended configurations and then evenly distributes the instances across the zones.
        # *   capacity-optimized: capacity-optimized distribution policy. The auto provisioning group creates instances of the optimal instance types across the optimal zones based on resource availability.
        # 
        # Default value: lowest-price.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The operation to be performed on the spot instance when it is interrupted. Valid values:
        # 
        # *   stop: stops the spot instance.
        # *   terminate: releases the spot instance.
        # 
        # Default value: terminate.
        self.spot_instance_interruption_behavior = spot_instance_interruption_behavior
        # The number of spot instances of the lowest-priced instance type to be created by the auto provisioning group. This parameter takes effect when `SpotAllocationStrategy` is set to `lowest-price`.
        # 
        # The value must be smaller than the N value specified in `LaunchTemplateConfig.N`.
        self.spot_instance_pools_to_use_count = spot_instance_pools_to_use_count
        # The target capacity of spot instances in the auto provisioning group. The value must be less than or equal to the `TotalTargetCapacity` value.
        self.spot_target_capacity = spot_target_capacity
        # The information of system disks on the instance.
        self.system_disk_config = system_disk_config
        # The tags to add to the auto provisioning group.
        self.tag = tag
        # Specifies whether to release instances in the auto provisioning group when the auto provisioning group is deleted. Valid values:
        # 
        # *   true: releases the instances.
        # *   false: retains the instances.
        # 
        # Default value: false.
        self.terminate_instances = terminate_instances
        # Specifies whether to release instances in the auto provisioning group when the group expires. Valid values:
        # 
        # *   true: releases the instances.
        # *   false: only removes the instances from the auto provisioning group but does not release them.
        # 
        # Default value: false.
        self.terminate_instances_with_expiration = terminate_instances_with_expiration
        # The total target capacity of the auto provisioning group. The value must be a positive integer.
        # 
        # The total target capacity of the auto provisioning group must be greater than or equal to the sum of the target capacity of pay-as-you-go instances specified by `PayAsYouGoTargetCapacity` and the target capacity of spot instances specified by `SpotTargetCapacity`.
        # 
        # This parameter is required.
        self.total_target_capacity = total_target_capacity
        # The time at which to start the auto provisioning group. The period of time between this point in time and the point in time specified by `ValidUntil` is the validity period of the auto provisioning group.
        # 
        # Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # By default, an auto provisioning group is started immediately after it is created.
        self.valid_from = valid_from
        # The time at which the auto provisioning group expires. The period of time between this point in time and the point in time specified by `ValidFrom` is the validity period of the auto provisioning group.
        # 
        # Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # Default value: 2099-12-31T23:59:59Z.
        self.valid_until = valid_until

    def validate(self):
        if self.launch_configuration:
            self.launch_configuration.validate()
        if self.data_disk_config:
            for v1 in self.data_disk_config:
                 if v1:
                    v1.validate()
        if self.launch_template_config:
            for v1 in self.launch_template_config:
                 if v1:
                    v1.validate()
        if self.pre_paid_options:
            self.pre_paid_options.validate()
        if self.resource_pool_options:
            self.resource_pool_options.validate()
        if self.system_disk_config:
            for v1 in self.system_disk_config:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.launch_configuration is not None:
            result['LaunchConfiguration'] = self.launch_configuration.to_map()

        if self.auto_provisioning_group_name is not None:
            result['AutoProvisioningGroupName'] = self.auto_provisioning_group_name

        if self.auto_provisioning_group_type is not None:
            result['AutoProvisioningGroupType'] = self.auto_provisioning_group_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        result['DataDiskConfig'] = []
        if self.data_disk_config is not None:
            for k1 in self.data_disk_config:
                result['DataDiskConfig'].append(k1.to_map() if k1 else None)

        if self.default_target_capacity_type is not None:
            result['DefaultTargetCapacityType'] = self.default_target_capacity_type

        if self.description is not None:
            result['Description'] = self.description

        if self.excess_capacity_termination_policy is not None:
            result['ExcessCapacityTerminationPolicy'] = self.excess_capacity_termination_policy

        if self.execution_mode is not None:
            result['ExecutionMode'] = self.execution_mode

        if self.hibernation_options_configured is not None:
            result['HibernationOptionsConfigured'] = self.hibernation_options_configured

        result['LaunchTemplateConfig'] = []
        if self.launch_template_config is not None:
            for k1 in self.launch_template_config:
                result['LaunchTemplateConfig'].append(k1.to_map() if k1 else None)

        if self.launch_template_id is not None:
            result['LaunchTemplateId'] = self.launch_template_id

        if self.launch_template_version is not None:
            result['LaunchTemplateVersion'] = self.launch_template_version

        if self.max_spot_price is not None:
            result['MaxSpotPrice'] = self.max_spot_price

        if self.min_target_capacity is not None:
            result['MinTargetCapacity'] = self.min_target_capacity

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.pay_as_you_go_allocation_strategy is not None:
            result['PayAsYouGoAllocationStrategy'] = self.pay_as_you_go_allocation_strategy

        if self.pay_as_you_go_target_capacity is not None:
            result['PayAsYouGoTargetCapacity'] = self.pay_as_you_go_target_capacity

        if self.pre_paid_options is not None:
            result['PrePaidOptions'] = self.pre_paid_options.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.resource_pool_options is not None:
            result['ResourcePoolOptions'] = self.resource_pool_options.to_map()

        if self.spot_allocation_strategy is not None:
            result['SpotAllocationStrategy'] = self.spot_allocation_strategy

        if self.spot_instance_interruption_behavior is not None:
            result['SpotInstanceInterruptionBehavior'] = self.spot_instance_interruption_behavior

        if self.spot_instance_pools_to_use_count is not None:
            result['SpotInstancePoolsToUseCount'] = self.spot_instance_pools_to_use_count

        if self.spot_target_capacity is not None:
            result['SpotTargetCapacity'] = self.spot_target_capacity

        result['SystemDiskConfig'] = []
        if self.system_disk_config is not None:
            for k1 in self.system_disk_config:
                result['SystemDiskConfig'].append(k1.to_map() if k1 else None)

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.terminate_instances is not None:
            result['TerminateInstances'] = self.terminate_instances

        if self.terminate_instances_with_expiration is not None:
            result['TerminateInstancesWithExpiration'] = self.terminate_instances_with_expiration

        if self.total_target_capacity is not None:
            result['TotalTargetCapacity'] = self.total_target_capacity

        if self.valid_from is not None:
            result['ValidFrom'] = self.valid_from

        if self.valid_until is not None:
            result['ValidUntil'] = self.valid_until

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LaunchConfiguration') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfiguration()
            self.launch_configuration = temp_model.from_map(m.get('LaunchConfiguration'))

        if m.get('AutoProvisioningGroupName') is not None:
            self.auto_provisioning_group_name = m.get('AutoProvisioningGroupName')

        if m.get('AutoProvisioningGroupType') is not None:
            self.auto_provisioning_group_type = m.get('AutoProvisioningGroupType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        self.data_disk_config = []
        if m.get('DataDiskConfig') is not None:
            for k1 in m.get('DataDiskConfig'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestDataDiskConfig()
                self.data_disk_config.append(temp_model.from_map(k1))

        if m.get('DefaultTargetCapacityType') is not None:
            self.default_target_capacity_type = m.get('DefaultTargetCapacityType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExcessCapacityTerminationPolicy') is not None:
            self.excess_capacity_termination_policy = m.get('ExcessCapacityTerminationPolicy')

        if m.get('ExecutionMode') is not None:
            self.execution_mode = m.get('ExecutionMode')

        if m.get('HibernationOptionsConfigured') is not None:
            self.hibernation_options_configured = m.get('HibernationOptionsConfigured')

        self.launch_template_config = []
        if m.get('LaunchTemplateConfig') is not None:
            for k1 in m.get('LaunchTemplateConfig'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchTemplateConfig()
                self.launch_template_config.append(temp_model.from_map(k1))

        if m.get('LaunchTemplateId') is not None:
            self.launch_template_id = m.get('LaunchTemplateId')

        if m.get('LaunchTemplateVersion') is not None:
            self.launch_template_version = m.get('LaunchTemplateVersion')

        if m.get('MaxSpotPrice') is not None:
            self.max_spot_price = m.get('MaxSpotPrice')

        if m.get('MinTargetCapacity') is not None:
            self.min_target_capacity = m.get('MinTargetCapacity')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PayAsYouGoAllocationStrategy') is not None:
            self.pay_as_you_go_allocation_strategy = m.get('PayAsYouGoAllocationStrategy')

        if m.get('PayAsYouGoTargetCapacity') is not None:
            self.pay_as_you_go_target_capacity = m.get('PayAsYouGoTargetCapacity')

        if m.get('PrePaidOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestPrePaidOptions()
            self.pre_paid_options = temp_model.from_map(m.get('PrePaidOptions'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('ResourcePoolOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('ResourcePoolOptions'))

        if m.get('SpotAllocationStrategy') is not None:
            self.spot_allocation_strategy = m.get('SpotAllocationStrategy')

        if m.get('SpotInstanceInterruptionBehavior') is not None:
            self.spot_instance_interruption_behavior = m.get('SpotInstanceInterruptionBehavior')

        if m.get('SpotInstancePoolsToUseCount') is not None:
            self.spot_instance_pools_to_use_count = m.get('SpotInstancePoolsToUseCount')

        if m.get('SpotTargetCapacity') is not None:
            self.spot_target_capacity = m.get('SpotTargetCapacity')

        self.system_disk_config = []
        if m.get('SystemDiskConfig') is not None:
            for k1 in m.get('SystemDiskConfig'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestSystemDiskConfig()
                self.system_disk_config.append(temp_model.from_map(k1))

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TerminateInstances') is not None:
            self.terminate_instances = m.get('TerminateInstances')

        if m.get('TerminateInstancesWithExpiration') is not None:
            self.terminate_instances_with_expiration = m.get('TerminateInstancesWithExpiration')

        if m.get('TotalTargetCapacity') is not None:
            self.total_target_capacity = m.get('TotalTargetCapacity')

        if m.get('ValidFrom') is not None:
            self.valid_from = m.get('ValidFrom')

        if m.get('ValidUntil') is not None:
            self.valid_until = m.get('ValidUntil')

        return self

class CreateAutoProvisioningGroupRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of tag N to add to the auto provisioning group.
        # 
        # Valid values of N: 1 to 20. The tag key cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain http:// or https://.
        self.key = key
        # The value of tag N to add to the auto provisioning group.
        # 
        # Valid values of N: 1 to 20. The tag value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateAutoProvisioningGroupRequestSystemDiskConfig(DaraModel):
    def __init__(
        self,
        disk_category: str = None,
    ):
        # The category of the system disk. You can specify multiple disk categories, and the disk categories are prioritized in the order in which they are specified. If a specified disk category is unavailable, the system uses the next available disk category. Valid values:
        # 
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD
        # - cloud: basic disk.
        self.disk_category = disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        return self

class CreateAutoProvisioningGroupRequestResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # The IDs of private pools. The ID of a private pool is the same as the ID of the elasticity assurance or capacity reservation that is associated with the private pool. You can specify the IDs of only targeted private pools for this parameter.
        self.private_pool_ids = private_pool_ids
        # Specifies which resource pools to use to create instances. Resource pools include the public pool and the private pools that are associated with elasticity assurance and capacity reservations in the Active state. Valid values:
        # 
        # *   PrivatePoolFirst: uses private pools first. If you set this parameter to PrivatePoolFirst, you can specify ResourcePoolOptions.PrivatePoolIds or leave ResourcePoolOptions.PrivatePoolIds empty. If you specify ResourcePoolOptions.PrivatePoolIds, the specified private pools are used first. If you leave ResourcePoolOptions.PrivatePoolIds empty or the private pools that you specify in ResourcePoolOptions.PrivatePoolIds have insufficient capacity, matching open private pools are used. If no matching open private pools exist, the public pool is used.
        # *   PrivatePoolOnly: uses only private pools. If you set this parameter to PrivatePoolOnly, you must specify ResourcePoolOptions.PrivatePoolIds. If the private pools that you specify in ResourcePoolOptions.PrivatePoolIds have insufficient capacity, instances cannot be created.
        # *   PublicPoolOnly: uses the public pool.
        # 
        # Default value: PublicPoolOnly.
        self.strategy = strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_ids is not None:
            result['PrivatePoolIds'] = self.private_pool_ids

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolIds') is not None:
            self.private_pool_ids = m.get('PrivatePoolIds')

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateAutoProvisioningGroupRequestPrePaidOptions(DaraModel):
    def __init__(
        self,
        specify_capacity_distribution: List[main_models.CreateAutoProvisioningGroupRequestPrePaidOptionsSpecifyCapacityDistribution] = None,
    ):
        # The minimum capacity set for different instance types. This parameter is valid only when `AutoProvisioningGroupType` is set to request.
        self.specify_capacity_distribution = specify_capacity_distribution

    def validate(self):
        if self.specify_capacity_distribution:
            for v1 in self.specify_capacity_distribution:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SpecifyCapacityDistribution'] = []
        if self.specify_capacity_distribution is not None:
            for k1 in self.specify_capacity_distribution:
                result['SpecifyCapacityDistribution'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.specify_capacity_distribution = []
        if m.get('SpecifyCapacityDistribution') is not None:
            for k1 in m.get('SpecifyCapacityDistribution'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestPrePaidOptionsSpecifyCapacityDistribution()
                self.specify_capacity_distribution.append(temp_model.from_map(k1))

        return self

class CreateAutoProvisioningGroupRequestPrePaidOptionsSpecifyCapacityDistribution(DaraModel):
    def __init__(
        self,
        instance_types: List[str] = None,
        min_target_capacity: int = None,
    ):
        # Details about the instance types. Duplicate instance types are not allowed and the instance types are within the LaunchTemplateConfig.InstanceType range.
        self.instance_types = instance_types
        # The minimum number of instances to be delivered within the `InstanceTypes` range.
        # 
        # >  `sum(MinTargetCapacity)<= TotalTargetCapacity` indicates that the sum of MinTargetCapacity values of all instance types cannot exceed the TotalTargetCapacity value. If any instance type set cannot meet the MinTargetCapacity requirement due to insufficient inventory or other reasons, the entire request fails.
        self.min_target_capacity = min_target_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.min_target_capacity is not None:
            result['MinTargetCapacity'] = self.min_target_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('MinTargetCapacity') is not None:
            self.min_target_capacity = m.get('MinTargetCapacity')

        return self

class CreateAutoProvisioningGroupRequestLaunchTemplateConfig(DaraModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: List[int] = None,
        excluded_instance_types: List[str] = None,
        image_id: str = None,
        instance_family_level: str = None,
        instance_type: str = None,
        max_price: float = None,
        max_quantity: int = None,
        memories: List[float] = None,
        priority: int = None,
        v_switch_id: str = None,
        weighted_capacity: float = None,
    ):
        # The architectures of the instance types.
        self.architectures = architectures
        # Specifies whether to include burstable instance types. Valid values:
        # 
        # *   Exclude: excludes burstable instance types.
        # *   Include: includes burstable instance types.
        # *   Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The numbers of vCPUs of instance types.
        self.cores = cores
        # The instance types that you want to exclude.
        self.excluded_instance_types = excluded_instance_types
        # The ID of the image. You can use this parameter to specify the image that is used by the current resource pool. If you do not specify this parameter, the image that is configured in `LaunchConfiguration.ImageId` or the launch template is used by default. You can call the [DescribeImages](https://help.aliyun.com/document_detail/25534.html) operation to query the available images. Note: This parameter is supported only when `AutoProvisioningGroupType` is set to instant.
        self.image_id = image_id
        # The instance family level of the instance type in extended configuration N. This parameter is used to filter instance types. Valid values of Nextended configuration N, Valid values:
        # 
        # *   EntryLevel: entry level (shared instance types). Instance types of this level are the most cost-effective but may not ensure stable computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # *   EnterpriseLevel: enterprise level. Instance types of this level provide stable performance and dedicated resources and are suitable for business scenarios that require high stability. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # *   CreditEntryLevel: credit entry level. This value is valid only for burstable instances. CPU credits are used to ensure computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low but may fluctuate in specific cases. For information about burstable instances, see [Overview](https://help.aliyun.com/document_detail/59977.html).
        # 
        # Valid values of N: 1 to 10.
        self.instance_family_level = instance_family_level
        # The instance type in extended configuration N. Valid values of N: 1 to 20. For information about the valid values of this parameter, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type = instance_type
        # The maximum price of spot instances in extended configuration N.
        # 
        # >  If you specify one or more `LaunchTemplateConfig.N.*` parameters, you must also specify `LaunchTemplateConfig.N.MaxPrice`.
        self.max_price = max_price
        # >  This parameter is in invitational preview and is not publicly available.
        self.max_quantity = max_quantity
        # The memory sizes of instance types.
        self.memories = memories
        # The priority of extended configuration N. A value of 0 indicates the highest priority. Valid values: 0 to ∞.
        self.priority = priority
        # The ID of the vSwitch in extended configuration N. The zone of the ECS instances created from the extended configuration is determined by the vSwitch.
        # 
        # >  If you specify one or more `LaunchTemplateConfig.N.*` parameters, you must also specify `LaunchTemplateConfig.N.VSwitchId`.
        self.v_switch_id = v_switch_id
        # The weight of the instance type in extended configuration N. A greater weight indicates that a single instance has more computing power and fewer instances are required. The value must be greater than 0.
        # 
        # The weight is calculated based on the computing power of the specified instance type and the minimum computing power of a single instance in the cluster to be created by the auto provisioning group. For example, assume that the minimum computing power of a single instance is 8 vCPUs and 60 GiB of memory.
        # 
        # *   For an instance type with 8 vCPUs and 60 GiB of memory, you can set the weight to 1.
        # *   For an instance type with 16 vCPUs and 120 GiB of memory, you can set the weight to 2.
        self.weighted_capacity = weighted_capacity

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architectures is not None:
            result['Architectures'] = self.architectures

        if self.burstable_performance is not None:
            result['BurstablePerformance'] = self.burstable_performance

        if self.cores is not None:
            result['Cores'] = self.cores

        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.max_quantity is not None:
            result['MaxQuantity'] = self.max_quantity

        if self.memories is not None:
            result['Memories'] = self.memories

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')

        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('MaxQuantity') is not None:
            self.max_quantity = m.get('MaxQuantity')

        if m.get('Memories') is not None:
            self.memories = m.get('Memories')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        return self

class CreateAutoProvisioningGroupRequestDataDiskConfig(DaraModel):
    def __init__(
        self,
        disk_category: str = None,
    ):
        # The category of data disk N. You can use this parameter to specify multiple disk categories, and the disk categories are prioritized in the order in which they are specified. If a specified disk category is unavailable, the system uses the next available disk category. Valid values:
        # 
        # - cloud_efficiency: ultra disk
        # - cloud_ssd: standard SSD
        # - cloud_essd: ESSD
        # - cloud: basic disk
        self.disk_category = disk_category

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_category is not None:
            result['DiskCategory'] = self.disk_category

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskCategory') is not None:
            self.disk_category = m.get('DiskCategory')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfiguration(DaraModel):
    def __init__(
        self,
        arn: List[main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationArn] = None,
        auto_release_time: str = None,
        credit_specification: str = None,
        data_disk: List[main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationDataDisk] = None,
        deployment_set_id: str = None,
        host_name: str = None,
        host_names: List[str] = None,
        image_family: str = None,
        image_id: str = None,
        instance_description: str = None,
        instance_name: str = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        key_pair_name: str = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        system_disk: main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSystemDisk = None,
        system_disk_category: str = None,
        system_disk_description: str = None,
        system_disk_name: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        tag: List[main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationTag] = None,
        user_data: str = None,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cpu_options: main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationCpuOptions = None,
        image_options: main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationImageOptions = None,
        period: int = None,
        period_unit: str = None,
        scheduler_options: main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSchedulerOptions = None,
        security_options: main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSecurityOptions = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.arn = arn
        # The automatic release time of the pay-as-you-go instance. Specify the time in the [ISO 8601](https://help.aliyun.com/document_detail/25696.html) standard in the `yyyy-MM-ddTHH:mm:ssZ` format. The time must be in Coordinated Universal Time (UTC).
        # 
        # *   If the value of `ss` is not `00`, the start time is automatically rounded down to the nearest minute based on the value of `mm`.
        # *   The specified time must be at least 30 minutes later than the current time.
        # *   The specified time can be at most three years later than the current time.
        self.auto_release_time = auto_release_time
        # The performance mode of the burstable instance. Valid values:
        # 
        # *   Standard: the standard mode. For more information, see the "Standard mode" section in the [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html) topic.
        # *   Unlimited: the unlimited mode. For more information, see the "Unlimited mode" section in the [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html) topic.
        # 
        # This parameter is empty by default.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.credit_specification = credit_specification
        # The cloud disks in the extended configurations of the launch template.
        self.data_disk = data_disk
        # The ID of the deployment set.
        self.deployment_set_id = deployment_set_id
        # The instance hostname. Take note of the following items:
        # 
        # *   The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-).
        # *   For Windows instances, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. It can contain letters, digits, and hyphens (-).
        # *   For instances that run other operating systems such as Linux, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate a hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
        # *   You cannot specify both `LaunchConfiguration.HostName` and `LaunchConfiguration.HostNames.N`. Otherwise, an error is returned.
        # *   When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.host_name = host_name
        # The hostname of instance N. You can use this parameter to specify different hostnames for multiple instances. Take note of the following items:
        # 
        # - This parameter takes effect only when `AutoProvisioningGroupType` is set to instant. 
        # - The value of N indicates the number of instances. Valid values of N: 1 to 1000. The value of N must be the same as the TotalTargetCapacity value. 
        # - The hostname cannot start or end with a period (.) or hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). 
        # - For Windows instances, the hostname must be 2 to 15 characters in length and cannot contain periods (.) or contain only digits. The hostname can contain letters, digits, and hyphens (-). 
        # - For instances that run other operating systems such as Linux, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-). 
        # - You cannot specify both `LaunchConfiguration.HostName` and `LaunchConfiguration.HostNames.N`. Otherwise, an error is returned. 
        # - When both LaunchTemplateId and LaunchConfiguration.* parameters are specified, LaunchTemplateId takes precedence.
        self.host_names = host_names
        # The name of the image family. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `aliyun` or `acs:`. The name cannot contain `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), and hyphens (-).
        self.image_family = image_family
        # The ID of the image to be used to create the instance. You can call the [DescribeImages](https://help.aliyun.com/document_detail/25534.html) operation to query available image resources. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.image_id = image_id
        # The instance description. The description must be 2 to 256 characters in length. The description can contain letters and cannot start with `http://` or `https://`. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.instance_description = instance_description
        # The instance name. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-).
        # 
        # The default value of this parameter is the `InstanceId` value.
        # 
        # When you batch create instances, you can batch configure sequential names for the instances. For more information, see [Batch configure sequential names or hostnames for multiple instances](https://help.aliyun.com/document_detail/196048.html).
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.instance_name = instance_name
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth
        # *   PayByTraffic: pay-by-traffic
        # 
        # >  When the pay-by-traffic billing method for network usage is used, the maximum inbound and outbound bandwidth values are used as the upper limits of bandwidth instead of guaranteed performance specifications. When demands outstrip resource supplies, the maximum bandwidths may be limited. If you want guaranteed bandwidth for your instance, use the pay-by-bandwidth billing method.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # *   When the maximum outbound public bandwidth is less than or equal to 10 Mbit/s, the valid values of this parameter are 1 to 10 and the default value is 10.
        # *   When the maximum outbound public bandwidth is greater than 10 Mbit/s, the valid values of this parameter are 1 to the value of `LaunchConfiguration.InternetMaxBandwidthOut`, and the default value is the value of `LaunchConfiguration.InternetMaxBandwidthOut`.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # *   none: The instance is not I/O optimized.
        # *   optimized: The instance is I/O optimized.
        # 
        # For instances of retired instance types, the default value is none. For instances of other instance types, the default value is optimized.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.io_optimized = io_optimized
        # The key pair name.
        # 
        # *   For Windows instances, this parameter is ignored. This parameter is empty by default.
        # *   By default, password-based logon is disabled for Linux instances.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.key_pair_name = key_pair_name
        # The instance password. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The password can contain the following special characters:
        # 
        # ``( ) ` ~ ! @ # $ % ^ & * - _ + = | { }  ``: ; \\" < > , . ? /``  For Windows instances, the password cannot start with a forward slash (/). When both LaunchTemplateId and LaunchConfiguration.* parameters are specified, LaunchTemplateId takes precedence. `
        self.password = password
        # Specifies whether to use the password preset in the image. Valid values:
        # 
        # *   true: uses the password preset in the image.
        # *   false: does not use the password preset in the image.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.password_inherit = password_inherit
        # The name of the instance Resource Access Management (RAM) role. You can call the [ListRoles](https://help.aliyun.com/document_detail/28713.html) operation provided by RAM to query the instance RAM roles that you created. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which to assign the instance. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.resource_group_id = resource_group_id
        # Specifies whether to enable security hardening. Valid values:
        # 
        # *   Active: enables security hardening. This value is applicable only to public images.
        # *   Deactive: disables security hardening. This value is applicable to all image types.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which to assign the instance. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the new ECS instances belong.
        self.security_group_ids = security_group_ids
        # The system disk information of instances. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk = system_disk
        # The category of the system disk. Valid values:
        # 
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: enhanced SSD (ESSD)
        # *   cloud: basic disk
        # 
        # For non-I/O optimized instances of retired instance types, the default value is cloud. For other instances, the default value is cloud_efficiency.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk_category = system_disk_category
        # The description of the system disk. The description must be 2 to 256 characters in length. The description can contain letters and cannot start with `http://` or `https://`.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk_description = system_disk_description
        # The name of the system disk. The name must be 2 to 128 characters in length. The name must start with a letter and cannot start with `http://` or `https://`. The name can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is empty by default.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk_name = system_disk_name
        # The performance level of the ESSD to be used as the system disk. Valid values:
        # 
        # *   PL0 (default): A single ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # For more information about ESSD performance levels, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Valid values: 20 to 500. Unit: GiB. The value must be at least 20 and greater than or equal to the size of the image specified by LaunchConfiguration.ImageId.
        # 
        # Default value: 40 or the size of the image specified by LaunchConfiguration.ImageId, whichever is greater.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.system_disk_size = system_disk_size
        # The tag in the extended configurations of the launch template.
        self.tag = tag
        # The instance user data. The user data must be encoded in Base64. The raw data can be up to 32 KB in size. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.user_data = user_data
        # Specifies whether to enable auto-renewal for the reserved instance. This parameter is required only when the instance uses the subscription billing method. Valid values:
        # 
        # *   true
        # *   false (default)
        self.auto_renew = auto_renew
        # The auto-renewal period of the instance. Valid values:
        # 
        # Valid values when PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        self.cpu_options = cpu_options
        # The image options.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the AutoProvisioningGroupType parameter is set to instant.
        self.image_options = image_options
        # The subscription period of the instance. The unit is specified by `PeriodUnit`. This parameter takes effect and is required only if the subscription billing method is selected. Valid values:
        # 
        # Valid values if PeriodUnit is set to Month: 1, 2, 3, 6, and 12.
        self.period = period
        # The unit of the subscription period. Default value: Month. Valid values:
        # 
        # Month
        self.period_unit = period_unit
        self.scheduler_options = scheduler_options
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours. Default value: 1. Valid values: Valid values:
        # 
        # *   1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # *   0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # Alibaba Cloud sends an ECS system event to notify you 5 minutes before the instance is released. The spot instance is billed by second. We recommend that you specify an appropriate protection period based on your business requirements.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the AutoProvisioningGroupType parameter is set to instant.
        self.spot_duration = spot_duration
        # The interruption event of the spot instances. Valid values:
        # 
        # *   Terminate: The instance is released.
        # *   Stop: The instance is stopped in economical mode.
        # 
        # For information about the economical mode, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        # 
        # Default value: Terminate.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the AutoProvisioningGroupType parameter is set to instant.
        self.spot_interruption_behavior = spot_interruption_behavior

    def validate(self):
        if self.arn:
            for v1 in self.arn:
                 if v1:
                    v1.validate()
        if self.data_disk:
            for v1 in self.data_disk:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()
        if self.cpu_options:
            self.cpu_options.validate()
        if self.image_options:
            self.image_options.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.security_options:
            self.security_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Arn'] = []
        if self.arn is not None:
            for k1 in self.arn:
                result['Arn'].append(k1.to_map() if k1 else None)

        if self.auto_release_time is not None:
            result['AutoReleaseTime'] = self.auto_release_time

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        result['DataDisk'] = []
        if self.data_disk is not None:
            for k1 in self.data_disk:
                result['DataDisk'].append(k1.to_map() if k1 else None)

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.host_names is not None:
            result['HostNames'] = self.host_names

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_description is not None:
            result['SystemDiskDescription'] = self.system_disk_description

        if self.system_disk_name is not None:
            result['SystemDiskName'] = self.system_disk_name

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['AutoRenewPeriod'] = self.auto_renew_period

        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()

        if self.security_options is not None:
            result['SecurityOptions'] = self.security_options.to_map()

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.arn = []
        if m.get('Arn') is not None:
            for k1 in m.get('Arn'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationArn()
                self.arn.append(temp_model.from_map(k1))

        if m.get('AutoReleaseTime') is not None:
            self.auto_release_time = m.get('AutoReleaseTime')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.data_disk = []
        if m.get('DataDisk') is not None:
            for k1 in m.get('DataDisk'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationDataDisk()
                self.data_disk.append(temp_model.from_map(k1))

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HostNames') is not None:
            self.host_names = m.get('HostNames')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskDescription') is not None:
            self.system_disk_description = m.get('SystemDiskDescription')

        if m.get('SystemDiskName') is not None:
            self.system_disk_name = m.get('SystemDiskName')

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('AutoRenewPeriod') is not None:
            self.auto_renew_period = m.get('AutoRenewPeriod')

        if m.get('CpuOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('ImageOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('SchedulerOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m.get('SchedulerOptions'))

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestLaunchConfigurationSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationSecurityOptions(DaraModel):
    def __init__(
        self,
        trusted_system_mode: str = None,
    ):
        self.trusted_system_mode = trusted_system_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.trusted_system_mode is not None:
            result['TrustedSystemMode'] = self.trusted_system_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TrustedSystemMode') is not None:
            self.trusted_system_mode = m.get('TrustedSystemMode')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationSchedulerOptions(DaraModel):
    def __init__(
        self,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
    ):
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        self.dedicated_host_id = dedicated_host_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether the instance that uses the image supports logons of the ecs-user user. Valid value:
        # 
        # *   true: The instance that uses the image supports logons of the ecs-user user.
        # *   false: The instance that uses the image does not support logons of the ecs-user user.
        self.login_as_non_root = login_as_non_root

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_as_non_root is not None:
            result['LoginAsNonRoot'] = self.login_as_non_root

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginAsNonRoot') is not None:
            self.login_as_non_root = m.get('LoginAsNonRoot')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationCpuOptions(DaraModel):
    def __init__(
        self,
        core: int = None,
        threads_per_core: int = None,
    ):
        self.core = core
        self.threads_per_core = threads_per_core

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core is not None:
            result['Core'] = self.core

        if self.threads_per_core is not None:
            result['ThreadsPerCore'] = self.threads_per_core

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Core') is not None:
            self.core = m.get('Core')

        if m.get('ThreadsPerCore') is not None:
            self.threads_per_core = m.get('ThreadsPerCore')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag. Valid values of N: 1 to 20. The tag key cannot be an empty string. It can be up to 128 characters in length and cannot start with acs: or aliyun. It cannot contain `http://` or `https://`. If both the LaunchTemplateId and LaunchConfiguration.* parameters are specified, the LaunchTemplateId parameter takes precedence.
        self.key = key
        # The value of the tag. Valid values of N: 1 to 20. The tag value can be an empty string. It can be up to 128 characters in length. It cannot start with acs: or contain `http://` or `https://`. If both the LaunchTemplateId and LaunchConfiguration.* parameters are specified, the LaunchTemplateId parameter takes precedence.
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

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationSystemDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        encrypt_algorithm: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        provisioned_iops: int = None,
    ):
        # The ID of the automatic snapshot policy to apply to the system disk.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the AutoProvisioningGroupType parameter is set to instant.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature for the system disk. Valid values:
        # 
        # *   true: force attaches the disk to the instance.
        # *   false: disables the performance burst feature for the system disk.
        # 
        # >  This parameter is available only if you set `LaunchConfiguration.SystemDisk.Category` to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The algorithm to use to encrypt the system disk. Valid values:
        # 
        # *   aes-256
        # *   sm4-128
        # 
        # Default value: aes-256.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        # 
        # >  This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # *   true: encrypts system disk N.
        # *   false: does not encrypt system disk N.
        # 
        # Default value: false. Valid values:
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.encrypted = encrypted
        # The ID of the KMS key to use for system disk N.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.kmskey_id = kmskey_id
        # The provisioned read/write IOPS of the ESSD AutoPL disk to use as the system disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >  This parameter is available only if you set LaunchConfiguration.SystemDisk.Category to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationDataDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kms_key_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The ID of the automatic snapshot policy to apply to data disk N.
        # 
        # When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when the AutoProvisioningGroupType parameter is set to instant.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature for the system disk. Valid values:
        # 
        # *   true: force attaches the disk to the instance.
        # *   false: disables the performance burst feature for the system disk.
        # 
        # >  This parameter is available only if you set LaunchConfiguration.DataDisk.N.Category to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. Valid values of N: 1 to 16. Valid values:
        # 
        # *   cloud_efficiency: utra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: ESSD.
        # *   cloud: basic disk.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency. For non-I/O optimized instances, the default value is cloud.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.category = category
        # Specifies whether to release data disk N when the instance to which the data disk is attached is released. Valid values:
        # 
        # *   true: releases data disk N when the associated instance is released.
        # *   false: does not release data disk N when the associated instance is released.
        # 
        # Default value: true.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.delete_with_instance = delete_with_instance
        # The description of data disk N. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.description = description
        # The mount point of data disk N. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.device = device
        # The name of data disk N. The name must be 2 to 128 characters in length. The name must start with a letter but cannot start with `http://` or `https://`. The name can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-).
        # 
        # This parameter is left empty by default.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.disk_name = disk_name
        # >  This parameter is not publicly available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N. Valid values:
        # 
        # *   true: encrypts system disk N.
        # *   false: does not encrypt system disk N.
        # 
        # Default value: false. Valid values:
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key to use for data disk N. When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.kms_key_id = kms_key_id
        # The performance level of the Enterprise SSD (ESSD) to use as data disk N. The value of N in this parameter must be the same as the value of N in `LaunchConfiguration.DataDisk.N.Category`. Valid values:
        # 
        # *   PL0: A single ESSD can deliver up to 10000 random read/write IOPS.
        # *   PL1 (default): A single ESSD can deliver up to 50000 random read/write IOPS.
        # *   PL2: A single ESSD can deliver up to 100000 random read/write IOPS.
        # *   PL3: A single ESSD can deliver up to 1000000 random read/write IOPS.
        # 
        # For information about ESSD performance levels, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.performance_level = performance_level
        # The provisioned read/write IOPS of the ESSD AutoPL disk to use as the system disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}.
        # 
        # Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # >  This parameter is available only if you set LaunchConfiguration.DataDisk.N.Category to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The size of data disk N. Valid values of N: 1 to 16. Unit: GiB. Valid values:
        # 
        # *   Valid values if you set LaunchConfiguration.DataDisk.N.Category to cloud_efficiency: 20 to 32768.
        # 
        # *   Valid values if you set LaunchConfiguration.DataDisk.N.Category to cloud_ssd: 20 to 32768.
        # 
        # *   Valid values if you set LaunchConfiguration.DataDisk.N.Category to cloud_essd: vary based on the `LaunchConfiguration.DataDisk.N.PerformanceLevel` value.
        # 
        #     *   Valid values if you set LaunchConfiguration.DataDisk.N.PerformanceLevel to PL0: 40 to 32768.
        #     *   Valid values if you set LaunchConfiguration.DataDisk.N.PerformanceLevel to PL1: 20 to 32768.
        #     *   Valid values if you set LaunchConfiguration.DataDisk.N.PerformanceLevel to PL2: 461 to 32768.
        #     *   Valid values if you set LaunchConfiguration.DataDisk.N.PerformanceLevel to PL3: 1261 to 32768.
        # 
        # *   Valid values if you set LaunchConfiguration.DataDisk.N.Category to cloud: 5 to 2000.
        # 
        # >  The value of this parameter must be greater than or equal to the size of the snapshot specified by `LaunchConfiguration.DataDisk.N.SnapshotId`.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.size = size
        # The ID of the snapshot to use to create data disk N. Valid values of N: 1 to 16.
        # 
        # If you specify this parameter, `LaunchConfiguration.DataDisk.N.Size` is ignored. The size of data disk N is the same as that of the snapshot specified by this parameter. Use snapshots created after July 15, 2013. Otherwise, an error is returned and your request is rejected.
        # 
        # When both LaunchTemplateId and LaunchConfiguration.\\* parameters are specified, LaunchTemplateId takes precedence.
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_snapshot_policy_id is not None:
            result['AutoSnapshotPolicyId'] = self.auto_snapshot_policy_id

        if self.bursting_enabled is not None:
            result['BurstingEnabled'] = self.bursting_enabled

        if self.category is not None:
            result['Category'] = self.category

        if self.delete_with_instance is not None:
            result['DeleteWithInstance'] = self.delete_with_instance

        if self.description is not None:
            result['Description'] = self.description

        if self.device is not None:
            result['Device'] = self.device

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kms_key_id is not None:
            result['KmsKeyId'] = self.kms_key_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DeleteWithInstance') is not None:
            self.delete_with_instance = m.get('DeleteWithInstance')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Device') is not None:
            self.device = m.get('Device')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KmsKeyId') is not None:
            self.kms_key_id = m.get('KmsKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

class CreateAutoProvisioningGroupRequestLaunchConfigurationArn(DaraModel):
    def __init__(
        self,
        assume_role_for: int = None,
        role_type: str = None,
        rolearn: str = None,
    ):
        # >  This parameter is in invitational preview and is not publicly available.
        self.assume_role_for = assume_role_for
        # >  This parameter is in invitational preview and is not publicly available.
        self.role_type = role_type
        # >  This parameter is in invitational preview and is not publicly available.
        self.rolearn = rolearn

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        if self.rolearn is not None:
            result['Rolearn'] = self.rolearn

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        if m.get('Rolearn') is not None:
            self.rolearn = m.get('Rolearn')

        return self

