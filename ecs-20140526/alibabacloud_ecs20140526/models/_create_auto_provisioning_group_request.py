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
        candidate_options: main_models.CreateAutoProvisioningGroupRequestCandidateOptions = None,
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
        # The name of the auto provisioning group. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.auto_provisioning_group_name = auto_provisioning_group_name
        # The delivery type of the auto provisioning group. Valid values:
        # 
        # - request: One-time asynchronous delivery. The group delivers the instance cluster only at startup. If scheduling fails, no retry occurs.
        # 
        # - instant: One-time synchronous delivery. The group creates instances synchronously at startup and returns the list of successfully created instances and reasons for failures in the response.
        # 
        # - maintain: Continuous provisioning. The group attempts to deliver the instance cluster at startup and monitors real-time capacity. If the target capacity is not met, it continues creating ECS instances.
        # 
        # Default value: maintain.
        self.auto_provisioning_group_type = auto_provisioning_group_type
        self.candidate_options = candidate_options
        # Ensures request idempotence. Generate a unique value from your client for this parameter to ensure uniqueness across different requests. ClientToken supports only ASCII characters and cannot exceed 64 characters. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The list of data disk configurations for instances.
        self.data_disk_config = data_disk_config
        # Specifies the billing method for the capacity difference when the sum of `PayAsYouGoTargetCapacity` and `SpotTargetCapacity` is less than `TotalTargetCapacity`. Valid values:
        # 
        # - PayAsYouGo: Pay-as-you-go instances.
        # 
        # - Spot: Spot instances.
        # 
        # Default value: Spot.
        self.default_target_capacity_type = default_target_capacity_type
        # The description of the auto provisioning group.
        self.description = description
        # Specifies whether to release instances when the real-time capacity of the auto provisioning group exceeds the target capacity and scale-in is triggered. Valid values:
        # 
        # - termination: Releases scaled-in instances.
        # 
        # - no-termination: Only removes scaled-in instances from the auto provisioning group.
        # 
        # Default value: no-termination.
        self.excess_capacity_termination_policy = excess_capacity_termination_policy
        self.execution_mode = execution_mode
        # > This parameter is in invitational preview and is not yet available.
        self.hibernation_options_configured = hibernation_options_configured
        # The list of extended launch template configurations.
        self.launch_template_config = launch_template_config
        # The ID of the launch template associated with the auto provisioning group. Call [DescribeLaunchTemplates](https://help.aliyun.com/document_detail/73759.html) to query available launch templates. When both a launch template and launch configuration parameters (`LaunchConfiguration.*`) are specified, the launch template takes precedence.
        self.launch_template_id = launch_template_id
        # The version of the launch template associated with the auto provisioning group. Call [DescribeLaunchTemplateVersions](https://help.aliyun.com/document_detail/73761.html) to query available launch template versions.
        # 
        # Default value: The default version of the launch template.
        self.launch_template_version = launch_template_version
        # The maximum price for spot instances in the auto provisioning group.
        # 
        # > If both `MaxSpotPrice` and `LaunchTemplateConfig.N.MaxPrice` are set, the lower value takes effect.
        self.max_spot_price = max_spot_price
        # The minimum target capacity of the auto provisioning group. Valid values: Positive integers.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with `AutoProvisioningGroupType=instant`.
        # 
        # - If the instance inventory in the region is less than this value, the API call fails and no instances are created.
        # 
        # - If the instance inventory in the region is greater than this value, instances are created based on other configured parameters.
        self.min_target_capacity = min_target_capacity
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The strategy for creating pay-as-you-go instances. Valid values:
        # 
        # - lowest-price: Cost optimization strategy. Selects the instance type with the lowest price.
        # 
        # - prioritized: Priority-based strategy. Creates instances based on the priority specified in `LaunchTemplateConfig.N.Priority`.
        # 
        # Default value: lowest-price.
        self.pay_as_you_go_allocation_strategy = pay_as_you_go_allocation_strategy
        # The target capacity for pay-as-you-go instances in the auto provisioning group. Valid values: Integers less than or equal to the value of `TotalTargetCapacity`.
        self.pay_as_you_go_target_capacity = pay_as_you_go_target_capacity
        # Detailed capacity configuration for subscription instances.
        self.pre_paid_options = pre_paid_options
        # The region ID of the auto provisioning group. Call [DescribeRegions](https://help.aliyun.com/document_detail/25609.html) to view the latest Alibaba Cloud region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource group ID of the auto provisioning group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The resource pool strategy used when creating instances. Note:
        # 
        # - This parameter takes effect only when creating pay-as-you-go instances.
        # 
        # - This parameter takes effect only when creating an auto provisioning group with `AutoProvisioningGroupType=instant`.
        self.resource_pool_options = resource_pool_options
        # The strategy for creating spot instances. Valid values:
        # 
        # - lowest-price: Cost optimization strategy. Selects the instance type with the lowest price.
        # 
        # - diversified: Balanced zone distribution strategy. Creates instances across the zones specified in the launch template configurations and distributes them evenly.
        # 
        # - capacity-optimized: Capacity optimization strategy. Selects the optimal instance type and zone based on inventory availability.
        # 
        # Default value: lowest-price.
        self.spot_allocation_strategy = spot_allocation_strategy
        # The behavior when a spot instance is interrupted. Valid values:
        # 
        # - stop: Stops the instance.
        # 
        # - terminate: Releases the instance.
        # 
        # Default value: terminate.
        self.spot_instance_interruption_behavior = spot_instance_interruption_behavior
        # Takes effect only when `SpotAllocationStrategy` is set to `lowest-price`. Specifies the number of lowest-priced instance types from which the auto provisioning group creates instances.
        # 
        # Valid values: Less than the value of N in `LaunchTemplateConfig.N`.
        self.spot_instance_pools_to_use_count = spot_instance_pools_to_use_count
        # The target capacity for spot instances in the auto provisioning group. Valid values: Integers less than or equal to the value of `TotalTargetCapacity`.
        self.spot_target_capacity = spot_target_capacity
        # The list of system disk configurations for instances.
        self.system_disk_config = system_disk_config
        # The list of tags bound to the auto provisioning group.
        self.tag = tag
        # Specifies whether to release instances in the group when you delete the auto provisioning group. Valid values:
        # 
        # - true: Releases instances in the group.
        # 
        # - false: Retains instances in the group.
        # 
        # Default value: false.
        self.terminate_instances = terminate_instances
        # Specifies whether to release instances in the group when the auto provisioning group expires. Valid values:
        # 
        # - true: Releases instances in the group.
        # 
        # - false: Only removes instances from the auto provisioning group.
        # 
        # Default value: false.
        self.terminate_instances_with_expiration = terminate_instances_with_expiration
        # The total target capacity of the auto provisioning group. Valid values: Positive integers.
        # 
        # The total capacity must be greater than or equal to the sum of `PayAsYouGoTargetCapacity` (target capacity for pay-as-you-go instances) and `SpotTargetCapacity` (target capacity for spot instances).
        # 
        # This parameter is required.
        self.total_target_capacity = total_target_capacity
        # The start time of the auto provisioning group. Used together with `ValidUntil` to define the validity period.
        # 
        # Specify the time in [ISO 8601](https://help.aliyun.com/document_detail/25696.html) format using UTC+0 time. Format: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # Default value: The timestamp when the API call takes effect immediately.
        self.valid_from = valid_from
        # The expiration time of the auto provisioning group. Used together with `ValidFrom` to define the validity period.
        # 
        # Specify the time in [ISO 8601](https://help.aliyun.com/document_detail/25696.html) format using UTC+0 time. Format: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # Default value: 2099-12-31T23:59:59Z.
        self.valid_until = valid_until

    def validate(self):
        if self.launch_configuration:
            self.launch_configuration.validate()
        if self.candidate_options:
            self.candidate_options.validate()
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

        if self.candidate_options is not None:
            result['CandidateOptions'] = self.candidate_options.to_map()

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

        if m.get('CandidateOptions') is not None:
            temp_model = main_models.CreateAutoProvisioningGroupRequestCandidateOptions()
            self.candidate_options = temp_model.from_map(m.get('CandidateOptions'))

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
        # The tag key of the auto provisioning group.
        # 
        # N ranges from 1 to 20. If specified, the value cannot be an empty string. The key can be up to 128 characters in length and cannot start with aliyun or acs:. It also cannot contain http\\:// or https\\://.
        self.key = key
        # The tag value of the auto provisioning group.
        # 
        # N ranges from 1 to 20. If specified, the value can be an empty string. The value can be up to 128 characters in length and cannot contain http\\:// or https\\://.
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
        # The system disk type. You can specify multiple candidate disk types. The order specifies their priority. If one disk type is unavailable, the system automatically switches to the next type. Valid values:
        # 
        # - cloud_efficiency: Ultra disk.
        # 
        # - cloud_ssd: Standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud: Basic disk.
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
        # The list of private pool IDs. Valid values: 1 to 20.
        self.private_pool_ids = private_pool_ids
        # Resource pools include private pools generated by Elastic Guaranteed or Capacity Reservation services, and public pools. Instances select from these pools at startup. Valid values:
        # 
        # - PrivatePoolFirst: Private pools first. With this strategy,
        #   if ResourcePoolOptions.PrivatePoolIds is specified, the specified private pools are prioritized. If no private pool is specified or the specified private pools lack capacity, open private pools are automatically matched. If no eligible private pools exist, instances are created from the public pool.
        # 
        # - PrivatePoolOnly: Private pools only. With this strategy, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pools lack capacity, instance startup fails.
        # 
        # - PublicPoolOnly: Use the public pool to create instances.
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
        # The minimum capacity set for different instance types. This parameter is supported only when `AutoProvisioningGroupType = request`.
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
        # The set of instance types. Duplicates are not allowed, and the types must be within the range of LaunchTemplateConfig.InstanceType.
        self.instance_types = instance_types
        # The minimum number of instances to deliver within the `InstanceTypes` range.
        # 
        # > `sum(MinTargetCapacity)<= TotalTargetCapacity`. The sum of MinTargetCapacity across all instance type sets cannot exceed TotalTargetCapacity. If any instance type set fails to meet its MinTargetCapacity due to inventory issues, the entire request fails.
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
        # The list of architecture types for instance types.
        self.architectures = architectures
        # Specifies whether the instance type supports performance bursts. Valid values:
        # 
        # - Exclude: Excludes burstable instance types.
        # 
        # - Include: Includes burstable instance types.
        # 
        # - Required: Includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The list of vCPU counts for instance types.
        self.cores = cores
        # The list of instance types to exclude.
        self.excluded_instance_types = excluded_instance_types
        # The image ID. Use this parameter to specify the image for the current resource pool. If not set, the image specified in `LaunchConfiguration.ImageId` or the launch template is used by default. Call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available images.
        # Note: This parameter is supported only when `AutoProvisioningGroupType = instant`.
        self.image_id = image_id
        # The instance family level, used to filter eligible instance types. Valid values:
        # 
        # - EntryLevel: Entry-level, or shared-resource instances. Lower cost but no guaranteed stable computing performance. Suitable for workloads with low average CPU usage. For more information, see [Shared-resource instances](https://help.aliyun.com/document_detail/108489.html).
        # 
        # - EnterpriseLevel: Enterprise-level. Stable performance with dedicated resources. Suitable for workloads requiring high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # - CreditEntryLevel: Credit entry-level, or burstable instances. Uses CPU credits to guarantee computing performance. Suitable for workloads with low average CPU usage and occasional bursts. For more information, see [Burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # 
        # N ranges from 1 to 10.
        self.instance_family_level = instance_family_level
        # The instance type corresponding to the extended launch template. N ranges from 1 to 20. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.instance_type = instance_type
        # The maximum hourly price for spot instances in the extended launch template.
        # 
        # > After `LaunchTemplateConfig` is set, `LaunchTemplateConfig.N.MaxPrice` is required.
        self.max_price = max_price
        # > This parameter is in invitational preview and is not supported.
        self.max_quantity = max_quantity
        # The list of memory sizes for instance types.
        self.memories = memories
        # The priority of the extended launch template. A value of 0 indicates the highest priority. Valid values: 0 to +∞.
        self.priority = priority
        # The ID of the virtual switch to which the ECS instance belongs in the extended launch template. The zone of the ECS instance launched from this template is determined by the virtual switch.
        # 
        # > After `LaunchTemplateConfig` is set, `LaunchTemplateConfig.N.VSwitchId` is required.
        self.v_switch_id = v_switch_id
        # The weight of the instance type in the extended launch template. A higher value indicates greater computing power per instance and fewer instances needed. Valid values: Greater than 0.
        # 
        # You can calculate the weight based on the computing power of the specified instance type and the minimum computing power required per node in the cluster. For example, if the minimum computing power per node is 8 vCPUs and 60 GiB memory:
        # 
        # - An instance type with 8 vCPUs and 60 GiB memory can have a weight of 1.
        # 
        # - An instance type with 16 vCPUs and 120 GiB memory can have a weight of 2.
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
        # The data disk type. You can specify multiple candidate disk types. The order specifies their priority. If one disk type is unavailable, the system automatically switches to the next type. Valid values:
        # 
        # - cloud_efficiency: Ultra disk.
        # 
        # - cloud_ssd: Standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud: Basic disk.
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

class CreateAutoProvisioningGroupRequestCandidateOptions(DaraModel):
    def __init__(
        self,
        evaluate: bool = None,
        timeout_minutes: int = None,
    ):
        self.evaluate = evaluate
        self.timeout_minutes = timeout_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.evaluate is not None:
            result['Evaluate'] = self.evaluate

        if self.timeout_minutes is not None:
            result['TimeoutMinutes'] = self.timeout_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Evaluate') is not None:
            self.evaluate = m.get('Evaluate')

        if m.get('TimeoutMinutes') is not None:
            self.timeout_minutes = m.get('TimeoutMinutes')

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
        # > This parameter is in invitational preview and is not supported.
        self.arn = arn
        # The automatic release time for pay-as-you-go instances. Specify the time in [ISO 8601](https://help.aliyun.com/document_detail/25696.html) format using UTC+0 time. Format: `yyyy-MM-ddTHH:mm:ssZ`.
        # 
        # - If seconds (`ss`) are not `00`, the time is rounded down to the start of the current minute (`mm`).
        # 
        # - The earliest release time is 30 minutes after the current time.
        # 
        # - The latest release time cannot exceed three years from the current time.
        self.auto_release_time = auto_release_time
        # The running mode of burstable instances. Valid values:
        # 
        # - Standard: Standard mode. For more information, see the "Performance-constrained mode" section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html)
        # 
        # - Unlimited: Unlimited mode. For more information, see the "Unlimited mode" section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html)
        # 
        # Default value: None.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.credit_specification = credit_specification
        # The list of data disk configurations for the extended launch template.
        self.data_disk = data_disk
        # The deployment set ID.
        self.deployment_set_id = deployment_set_id
        # The hostname of the instance. Requirements:
        # 
        # - Periods (.) and hyphens (-) cannot be the first or last character and cannot appear consecutively.
        # 
        # - Windows instances: 2–15 characters. Periods (.) are not supported. Cannot consist of only digits. Can contain letters, digits, and hyphens (-).
        # 
        # - Other instances (such as Linux): 2–64 characters. Multiple periods (.) are supported. Each segment between periods can contain letters, digits, and hyphens (-).
        # 
        # - Do not set both `LaunchConfiguration.HostName` and `LaunchConfiguration.HostNames.N`. Otherwise, an error is returned.
        # 
        # - When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.host_name = host_name
        # The list of hostnames for one or more instances. Requirements:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with `AutoProvisioningGroupType=instant`.
        # 
        # - N indicates the number of instances. Valid values: 1 to 1000. The value must match TotalTargetCapacity.
        # 
        # - Periods (.) and hyphens (-) cannot be the first or last character and cannot appear consecutively.
        # 
        # - When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.host_names = host_names
        # The image family name. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `aliyun` or `acs:`. It also cannot contain `http://` or `https://`.
        self.image_family = image_family
        # The image ID. This is the image used when launching instances. Call [DescribeImages](https://help.aliyun.com/document_detail/25534.html) to query available images. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.image_id = image_id
        # The instance description. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.instance_description = instance_description
        # The instance name. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), periods (.), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        # 
        # Default value: The instance `InstanceId`.
        # 
        # To create multiple ECS instances, you can batch configure sequential instance names. For more information, see [Batch configure sequential instance names or hostnames](https://help.aliyun.com/document_detail/196048.html).
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.instance_name = instance_name
        # The network billing type. Valid values:
        # 
        # - PayByBandwidth: Pay-by-bandwidth.
        # 
        # - PayByTraffic: Pay-by-traffic.
        # 
        # > For pay-by-traffic, inbound and outbound bandwidth peaks represent upper limits and are not service-level commitments. Bandwidth may be throttled during resource contention. Use pay-by-bandwidth if your workload requires guaranteed bandwidth.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth, in Mbit/s. Valid values:
        # 
        # - When outbound public bandwidth is ≤ 10 Mbit/s: 1–10. Default: 10.
        # 
        # - When outbound public bandwidth is > 10 Mbit/s: 1–`LaunchConfiguration.InternetMaxBandwidthOut`. Default: `LaunchConfiguration.InternetMaxBandwidthOut`.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth, in Mbit/s. Valid values: 0–100.
        # 
        # Default value: 0.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # - none: Not I/O optimized.
        # 
        # - optimized: I/O optimized.
        # 
        # For retired instance types, the default value is none. For other instance types, the default value is optimized.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.io_optimized = io_optimized
        # The key pair name.
        # 
        # - For Windows instances, this parameter is ignored. Default value: empty.
        # 
        # - For Linux instances, password logon is disabled after initialization.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.key_pair_name = key_pair_name
        # The instance password. The password must be 8 to 30 characters in length and include at least three of the following: uppercase letters, lowercase letters, digits, and special characters. Valid special characters:
        # 
        # ``()`~!@#$%^&*-_+=|{}`[]`:;\\"<>,.?/``
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.password = password
        # Specifies whether to use the password preset in the image. Valid values:
        # 
        # - true: Uses the preset password.
        # 
        # - false: Does not use the preset password.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.password_inherit = password_inherit
        # The RAM role name of the instance. Use the RAM API [ListRoles](https://help.aliyun.com/document_detail/28713.html) to query your created RAM roles. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.ram_role_name = ram_role_name
        # The resource group ID of the instance. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.resource_group_id = resource_group_id
        # Specifies whether to enable security hardening. Valid values:
        # 
        # - Active: Enables security hardening. Applies only to public images.
        # 
        # - Deactive: Disables security hardening. Applies to all image types.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The security group ID of the instance. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.security_group_id = security_group_id
        # The list of security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        # System disk information for the instance. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk = system_disk
        # The category of the system disk. Valid values:
        # 
        # - cloud_efficiency: Ultra disk.
        # 
        # - cloud_ssd: Standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud: Basic disk.
        # 
        # For retired instance types that are not I/O optimized, the default value is cloud. Otherwise, the default value is cloud_efficiency.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk_category = system_disk_category
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk_description = system_disk_description
        # The name of the system disk. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk_name = system_disk_name
        # The performance level of the ESSD used as the system disk. Valid values:
        # 
        # - PL0 (default): Up to 10,000 random read/write IOPS per disk.
        # 
        # - PL1: Up to 50,000 random read/write IOPS per disk.
        # 
        # - PL2: Up to 100,000 random read/write IOPS per disk.
        # 
        # - PL3: Up to 1,000,000 random read/write IOPS per disk.
        # 
        # For more information about selecting ESSD performance levels, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk, in GiB. Valid values: 20–500. The value must be greater than or equal to max{20, size of the image specified by LaunchConfiguration.ImageId}.
        # 
        # Default value: max{40, size of the image specified by LaunchConfiguration.ImageId}.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.system_disk_size = system_disk_size
        # The list of tags for the extended launch template.
        self.tag = tag
        # The instance user data. Encode the data in Base64. The raw data cannot exceed 32 KB. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.user_data = user_data
        # Specifies whether to enable auto-renewal. Takes effect when creating subscription instances. Valid values:
        # 
        # - true: Enables auto-renewal.
        # 
        # - false (default): Disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration per cycle. Valid values:
        # 
        # <props="china">
        # 
        # - When PeriodUnit=Week: 1, 2, 3.
        # 
        # - When PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, 60.
        # 
        # 
        # 
        # <props="intl">
        # 
        # When PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, 60.
        # 
        # 
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # CPU configuration.
        self.cpu_options = cpu_options
        # Image-related properties.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with AutoProvisioningGroupType=instant.
        self.image_options = image_options
        # The subscription duration. The unit is specified by `PeriodUnit`. Required when creating subscription instances. Valid values:
        # 
        # <props="china">
        # 
        # - When PeriodUnit=Week, Period values: 1, 2, 3, 4.
        # 
        # - When PeriodUnit=Month, Period values: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 60.
        # 
        # 
        # 
        # <props="intl">
        # 
        # When PeriodUnit=Month, Period values: 1, 2, 3, 6, 12.
        # 
        # 
        # 
        # <props="partner">
        # 
        # When PeriodUnit=Month, Period values: 1, 2, 3, 6, 12.
        self.period = period
        # The time unit for subscription billing. Valid values:
        # 
        # <props="china">
        # 
        # - Week.
        # 
        # - Month (default).
        # 
        # 
        # 
        # <props="intl">
        # 
        # Month (default).
        self.period_unit = period_unit
        self.scheduler_options = scheduler_options
        self.security_options = security_options
        # The reserved duration for spot instances, in hours. Default value: 1. Valid values:
        # 
        # - 1: Alibaba Cloud guarantees that the instance runs for 1 hour without being automatically released. After 1 hour, the system compares your bid price with the market price and checks inventory to decide whether to retain or reclaim the instance.
        # 
        # - 0: Alibaba Cloud does not guarantee that the instance runs for 1 hour. The system immediately compares your bid price with the market price and checks inventory to decide whether to retain or reclaim the instance.
        # 
        # Alibaba Cloud sends an ECS system event notification 5 minutes before reclaiming a spot instance. Spot instances are billed per second. Choose the reserved duration based on your task execution time.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with AutoProvisioningGroupType=instant.
        self.spot_duration = spot_duration
        # The interruption behavior for spot instances. Valid values:
        # 
        # - Terminate: Releases the instance immediately.
        # 
        # - Stop: Puts the instance into economical mode.
        # 
        # For more information about economical mode, see [Economical mode](https://help.aliyun.com/document_detail/63353.html).
        # 
        # Default value: Terminate.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with AutoProvisioningGroupType=instant.
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
        # Specifies whether instances using this image support logging on as the ecs-user. Valid values:
        # 
        # - true: Supported.
        # 
        # - false: Not supported.
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
        # The number of CPU cores.
        # 
        # Default value: See [Customize CPU options](https://help.aliyun.com/zh/ecs/user-guide/specify-and-view-cpu-options?spm=a2c4g.11186623.0.0.734f769asTEobd).
        self.core = core
        # The number of CPU threads. The vCPU count of an ECS instance equals CpuOptions.Core × CpuOptions.ThreadsPerCore.
        # 
        # CpuOptions.ThreadsPerCore=1 disables CPU hyper-threading.
        # 
        # Only specific instance types support setting the number of CPU threads.
        # 
        # Valid values and default values: See [Customize CPU options](https://help.aliyun.com/zh/ecs/user-guide/specify-and-view-cpu-options?spm=a2c4g.11186623.0.0.734f769aeIFsoj).
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
        # The tag key of the instance. N ranges from 1 to 20. If specified, the value cannot be an empty string. The key can be up to 128 characters in length and cannot start with aliyun or acs:. It also cannot contain `http://` or `https://`. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.key = key
        # The tag value of the instance. N ranges from 1 to 20. If specified, the value can be an empty string. The value can be up to 128 characters in length and cannot start with acs:. It also cannot contain `http://` or `https://`. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
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
        # The automatic snapshot policy ID applied to the system disk.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with AutoProvisioningGroupType=instant.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable performance burst. Valid values:
        # 
        # - true: Enables performance burst.
        # 
        # - false: Disables performance burst.
        # 
        # > This parameter is supported only when `SystemDisk.Category` is set to `cloud_auto`. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The encryption algorithm for the system disk. Valid values:
        # 
        # - aes-256.
        # 
        # - sm4-128.
        # 
        # Default value: aes-256.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        # 
        # > This parameter is not yet available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt system disk N. Valid values:
        # 
        # - true: Encrypts the disk.
        # 
        # - false: Does not encrypt the disk.
        # 
        # Default value: false.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.encrypted = encrypted
        # The KMS key ID for the system disk.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.kmskey_id = kmskey_id
        # The provisioned read/write IOPS for ESSD AutoPL disks. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × capacity, 50,000}.
        # 
        # > This parameter is supported only when SystemDisk.Category is set to cloud_auto. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
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
        # The automatic snapshot policy ID applied to the data disk.
        # 
        # Note:
        # 
        # - This parameter takes effect only when creating an auto provisioning group with AutoProvisioningGroupType=instant.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable performance burst. Valid values:
        # 
        # - true: Enables performance burst.
        # 
        # - false: Disables performance burst.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of data disk N. N ranges from 1 to 16. Valid values:
        # 
        # - cloud_efficiency: Ultra disk.
        # 
        # - cloud_ssd: Standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud: Basic disk.
        # 
        # For I/O optimized instances, the default value is cloud_efficiency. For non-I/O optimized instances, the default value is cloud.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        # 
        # - true: Releases the data disk with the instance.
        # 
        # - false: Does not release the data disk with the instance.
        # 
        # Default value: true.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.description = description
        # The mount point of the data disk. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length and can contain letters, digits, periods (.), colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        # 
        # Default value: empty.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.disk_name = disk_name
        # > This parameter is not yet available.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt data disk N. Valid values:
        # 
        # - true: Encrypts the disk.
        # 
        # - false: Does not encrypt the disk.
        # 
        # Default value: false.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.encrypted = encrypted
        # The KMS key ID for the data disk. When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.kms_key_id = kms_key_id
        # The performance level of the ESSD used as a data disk. The value of N must match the N in `LaunchConfiguration.DataDisk.N.Category`. Valid values:
        # 
        # - PL0: Up to 10,000 random read/write IOPS per disk.
        # 
        # - PL1 (default): Up to 50,000 random read/write IOPS per disk.
        # 
        # - PL2: Up to 100,000 random read/write IOPS per disk.
        # 
        # - PL3: Up to 1,000,000 random read/write IOPS per disk.
        # 
        # For more information about selecting ESSD performance levels, see [ESSD](https://help.aliyun.com/document_detail/122389.html).
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.performance_level = performance_level
        # The provisioned read/write IOPS for ESSD AutoPL disks. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}.
        # 
        # Baseline performance = min{1,800 + 50 × capacity, 50,000}.
        # 
        # > This parameter is supported only when DiskCategory is set to cloud_auto. For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.provisioned_iops = provisioned_iops
        # The size of data disk N, in GiB. N ranges from 1 to 16. Valid values:
        # 
        # - cloud_efficiency: 20–32768.
        # 
        # - cloud_ssd: 20–32768.
        # 
        # - cloud_essd: The valid range depends on the value of `LaunchConfiguration.DataDisk.N.PerformanceLevel`.
        # 
        #   - PL0: 40–32768.
        # 
        #   - PL1: 20–32768.
        # 
        #   - PL2: 461–32768.
        # 
        #   - PL3: 1261–32768
        # 
        # - cloud: 5–2000.
        # 
        # > The value must be greater than or equal to the size of the snapshot specified by `LaunchConfiguration.DataDisk.N.SnapshotId`.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
        self.size = size
        # The snapshot used to create data disk N. N ranges from 1 to 16.
        # 
        # After this parameter is specified, `LaunchConfiguration.DataDisk.N.Size` is ignored. The actual disk size equals the size of the specified snapshot. Snapshots created on or before July 15, 2013 are not supported and will cause the request to fail.
        # 
        # When both a launch template and launch configuration parameters are specified, the launch template takes precedence.
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
        # > This parameter is in invitational preview and is not supported.
        self.assume_role_for = assume_role_for
        # > This parameter is in invitational preview and is not supported.
        self.role_type = role_type
        # > This parameter is in invitational preview and is not supported.
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

