# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class CreateScalingConfigurationRequest(DaraModel):
    def __init__(
        self,
        image_options: main_models.CreateScalingConfigurationRequestImageOptions = None,
        private_pool_options: main_models.CreateScalingConfigurationRequestPrivatePoolOptions = None,
        system_disk: main_models.CreateScalingConfigurationRequestSystemDisk = None,
        affinity: str = None,
        client_token: str = None,
        cpu: int = None,
        credit_specification: str = None,
        custom_priorities: List[main_models.CreateScalingConfigurationRequestCustomPriorities] = None,
        data_disks: List[main_models.CreateScalingConfigurationRequestDataDisks] = None,
        dedicated_host_cluster_id: str = None,
        dedicated_host_id: str = None,
        deletion_protection: bool = None,
        deployment_set_id: str = None,
        host_name: str = None,
        hpc_cluster_id: str = None,
        http_endpoint: str = None,
        http_tokens: str = None,
        image_family: str = None,
        image_id: str = None,
        image_name: str = None,
        instance_description: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[main_models.CreateScalingConfigurationRequestInstancePatternInfos] = None,
        instance_type: str = None,
        instance_type_candidate_options: main_models.CreateScalingConfigurationRequestInstanceTypeCandidateOptions = None,
        instance_type_overrides: List[main_models.CreateScalingConfigurationRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        network_interfaces: List[main_models.CreateScalingConfigurationRequestNetworkInterfaces] = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_pool_options: main_models.CreateScalingConfigurationRequestResourcePoolOptions = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options: Dict[str, Any] = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_options: main_models.CreateScalingConfigurationRequestSecurityOptions = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[main_models.CreateScalingConfigurationRequestSpotPriceLimits] = None,
        spot_strategy: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        system_disk_categories: List[str] = None,
        tags: str = None,
        tenancy: str = None,
        user_data: str = None,
        zone_id: str = None,
    ):
        self.image_options = image_options
        self.private_pool_options = private_pool_options
        self.system_disk = system_disk
        # Specifies whether to associate the instance with the dedicated host. Valid values:
        # 
        # - default: The instance is not associated with the dedicated host. When you restart an instance that was stopped in economical mode, the instance may be placed on a different dedicated host in the automatic deployment resource pool if the original dedicated host has insufficient resources.
        # 
        # - host: The instance is associated with the dedicated host. When you restart an instance that was stopped in economical mode, the instance is still placed on the original dedicated host. If the original dedicated host has insufficient resources, the instance fails to restart.
        # 
        # Default value: default.
        self.affinity = affinity
        # Ensures the idempotence of the request. You can use the client to generate a unique parameter value to make sure that the same request is not repeated. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [How to ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The number of vCPUs. Unit: cores.
        # 
        # You can specify both Cpu and Memory to define a range of instance types. For example, if you set Cpu to 2 and Memory to 16, all instance types with 2 vCPUs and 16 GiB of memory are selected. Auto Scaling determines the available instance types based on factors such as I/O optimization and zone, and then creates an instance of the instance type that has the lowest price.
        # 
        # > This configuration is effective only when the cost optimization policy is enabled for the scaling group and no instance types are specified in the scaling configuration.
        self.cpu = cpu
        # The performance mode of the burstable instance. Valid values:
        # 
        # - Standard: standard mode.
        # 
        # - Unlimited: unlimited mode.
        # 
        # For more information, see the Performance modes section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The custom priority for the combination of an ECS instance type and a vSwitch.
        # >Notice: This is effective only when the scaling policy of the scaling group is set to the priority policy.
        # 
        # If an instance cannot be created from a combination of an instance type and a vSwitch with a higher priority, Auto Scaling automatically tries the next combination in the list.
        # 
        # > If you specify custom priorities for only some combinations of instance types and vSwitches, the unspecified combinations have a lower priority than the specified ones. The unspecified combinations are still prioritized based on the order of vSwitches in the scaling group and the order of instance types in the scaling configuration.
        # >
        # > - For example, if the vSwitch order in the scaling group is vsw1, vsw2, the instance type order in the scaling configuration is type1, type2, and the custom priority order is ["vsw2+type2", "vsw1+type2"], the final priority will be: "vsw2+type2" > "vsw1+type2" > "vsw1+type1" > "vsw2+type1".
        self.custom_priorities = custom_priorities
        # A collection of data disk information.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # Specifies whether to create the ECS instance on a dedicated host. If you specify the DedicatedHostId parameter, the SpotStrategy and SpotPriceLimit settings in the request are automatically ignored. This is because dedicated hosts do not support creating preemptible instances.
        # 
        # You can call the DescribeDedicatedHosts operation to query the list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The release protection attribute of the instance. This specifies whether you can release the instance through the ECS console or by calling the DeleteInstance API. This prevents accidental release of the instance. Valid values:
        # 
        # - true: enables release protection. You cannot release the instance through the ECS console or by calling the DeleteInstance API.
        # 
        # - false: disables release protection. You can release the instance through the ECS console or by calling the DeleteInstance API.
        # 
        # Default value: false.
        # 
        # > This attribute applies only to pay-as-you-go instances to prevent accidental release of instances scaled out by Auto Scaling. It does not affect normal scale-in activities. Instances with release protection enabled can be released during scale-in activities.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the ECS instance belongs.
        self.deployment_set_id = deployment_set_id
        # The hostname of the ECS instance. A period (.) or a hyphen (-) cannot be used as the first or last character of a hostname. Consecutive periods (.) or hyphens (-) are not allowed. The naming conventions for different instance types are as follows:
        # 
        # - For Windows instances, the hostname must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot contain periods (.) or be all digits.
        # 
        # - For other instance types, such as Linux, the hostname must be 2 to 64 characters in length. You can use periods (.) to separate the hostname into multiple segments. Each segment can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the High Performance Computing (HPC) cluster to which the ECS instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # - enabled: enables the channel.
        # 
        # - disabled: disables the channel.
        # 
        # Default value: enabled.
        # 
        # > For information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # Specifies whether to enforce the security-hardened mode (IMDSv2) when accessing instance metadata. Valid values:
        # 
        # - optional: does not enforce the mode.
        # 
        # - required: enforces the mode. If you set this value, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # 
        # > For information about instance metadata access modes, see [Instance metadata access modes](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image from the specified image family to create the instance. If you have specified the `ImageId` parameter, you cannot set this parameter.
        self.image_family = image_family
        # The ID of the image file to use for creating instances.
        self.image_id = image_id
        # The name of the image file. Image names must be unique within a region. If you specify ImageId, ImageName is ignored.
        # 
        # You cannot use ImageName to specify a Marketplace image.
        self.image_name = image_name
        # The description of the ECS instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.instance_description = instance_description
        # The name of the ECS instances that are created using the scaling configuration.
        self.instance_name = instance_name
        # A collection of intelligent configuration information used to filter instance types that meet the requirements.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance type of the ECS instance. For more information, see Instance families.
        self.instance_type = instance_type
        # After you enable the candidate mode, if issues such as insufficient inventory occur, the system supplements the currently selected instance types with similar-sized alternatives or creates vSwitches in candidate zones and adds them to the scaling group.
        self.instance_type_candidate_options = instance_type_candidate_options
        # Information about the specified instance types.
        self.instance_type_overrides = instance_type_overrides
        # Multiple instance types. If you use InstanceTypes, InstanceType is ignored.
        # 
        # If an instance cannot be created from an instance type with a higher priority, Auto Scaling automatically tries the next instance type in the list.
        self.instance_types = instance_types
        # The billing method for network usage. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth. InternetMaxBandwidthOut specifies the fixed bandwidth.
        # 
        # - PayByTraffic: pay-by-data-transfer. InternetMaxBandwidthOut specifies the maximum bandwidth. You are charged for the actual data transfer.
        # 
        # If you do not specify this parameter, the default value is PayByBandwidth for classic network and PayByTraffic for VPC.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # 
        # - If the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is I/O optimized. Valid values:
        # 
        # none: The instance is not I/O optimized.
        # optimized: The instance is I/O optimized.
        # 
        # For retired instance types, the default value is none. For other instance types, the default value is optimized.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses to assign to the ENI.
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair to use to log on to the ECS instance.
        # 
        # - For Windows instances, this parameter is ignored. The default value is empty.
        # 
        # - For Linux instances, password-based logon is disabled.
        self.key_pair_name = key_pair_name
        # The weight of the ECS instance as a backend server of the load balancer. Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # 
        # You can specify both Cpu and Memory to define a range of instance types. For example, if you set Cpu to 2 and Memory to 16, all instance types with 2 vCPUs and 16 GiB of memory are selected. Auto Scaling determines the available instance types based on factors such as I/O optimization and zone, and then creates an instance of the instance type that has the lowest price.
        # 
        # > This configuration is effective only when the cost optimization policy is enabled for the scaling group and no instance types are specified in the scaling configuration.
        self.memory = memory
        # The list of ENIs.
        self.network_interfaces = network_interfaces
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the ECS instance. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters can be:
        # 
        # \\`()` ~!@#$%^&*-_+=\\|{}[]:;\\"<>,.?/`
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you specify the Password parameter, we recommend that you send the request over HTTPS to prevent password leaks.
        self.password = password
        # Specifies whether to use the password preset in the image. If you use this parameter, make sure that a password is preset in the image. Valid values:
        # 
        # - true: uses the preset password.
        # 
        # - false: does not use the preset password.
        self.password_inherit = password_inherit
        # The name of the RAM role for the ECS instance. The name is provided and maintained by RAM. You can call the ListRoles operation to query the available RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The resource pool policy to use when creating an instance. Note the following when you set this parameter:
        # 
        # - This parameter takes effect only when creating pay-as-you-go instances.
        # 
        # - You cannot set this parameter at the same time as PrivatePoolOptions.MatchCriteria and PrivatePoolOptions.Id.
        self.resource_pool_options = resource_pool_options
        # The name of the scaling configuration. The name must be 2 to 64 characters in length, and can contain digits, underscores (_), hyphens (-), and periods (.). It must start with a digit, a letter, or a Chinese character.
        # 
        # The name of a scaling configuration must be unique within a scaling group in a region. If you do not specify this parameter, the ID of the scaling configuration is used.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The scheduling options.
        self.scheduler_options = scheduler_options
        # Specifies whether to enable security hardening. Valid values:
        # 
        # - Active: enables security hardening. This setting is valid only for public images.
        # 
        # - Deactive: disables security hardening. This setting is valid for all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the ECS instance belongs. ECS instances in the same security group can communicate with each other.
        self.security_group_id = security_group_id
        # Adds the ECS instance to multiple security groups. For more information, see the Security groups section in [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > You cannot specify both SecurityGroupId and SecurityGroupIds.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the preemptible instance. Unit: hours. Valid values:
        # 
        # - 1: The instance is retained for 1 hour after it is created. After 1 hour, the system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # - 0: The instance is not guaranteed to be retained for 1 hour after it is created. The system compares the bid price with the market price and checks the resource inventory to determine whether to retain or release the instance.
        # 
        # > Alibaba Cloud sends a notification to you through an ECS system event 5 minutes before the instance is released. Preemptible instances are billed by the second. We recommend that you select a protection period based on the time required for your task to complete.
        # 
        # Default value: 1.
        self.spot_duration = spot_duration
        # The interruption mode of the preemptible instance. Currently, only terminate is supported, which releases the instance by default.
        self.spot_interruption_behavior = spot_interruption_behavior
        # A collection of billing information for preemptible instances.
        self.spot_price_limits = spot_price_limits
        # The preemption policy for pay-as-you-go instances. Valid values:
        # 
        # - NoSpot: The instance is a regular pay-as-you-go instance.
        # 
        # - SpotWithPriceLimit: The instance is a preemptible instance with a user-defined maximum hourly price.
        # 
        # - SpotAsPriceGo: The instance is a preemptible instance for which the price is automatically bid based on the current market price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. The value must be greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # Multiple disk categories for the system disk. When a disk of a higher-priority category is unavailable, Auto Scaling automatically tries the next lower-priority category to create the system disk. Valid values:
        # 
        # - cloud: basic disk.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # > If you specify this parameter, you cannot specify `SystemDisk.Category`.
        self.system_disk_categories = system_disk_categories
        # The tags of the ECS instance. You can specify up to 20 tags in key-value pairs. The following limits apply to keys and values:
        # 
        # - A key can be up to 64 characters in length and cannot start with aliyun or acs:. It cannot contain `http://` or `https://`. If you use tags, the key cannot be an empty string.
        # 
        # - A value can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain `http://` or `https://`. The value can be an empty string.
        self.tags = tags
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # 
        # - default: creates the instance on a non-dedicated host.
        # 
        # - host: creates the instance on a dedicated host. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a dedicated host for the instance.
        # 
        # Default value: default.
        self.tenancy = tenancy
        # The custom data of the ECS instance. The data must be Base64 encoded. The raw data can be up to 32 KB in size.
        self.user_data = user_data
        # The ID of the zone to which the ECS instance belongs.
        self.zone_id = zone_id

    def validate(self):
        if self.image_options:
            self.image_options.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.system_disk:
            self.system_disk.validate()
        if self.custom_priorities:
            for v1 in self.custom_priorities:
                 if v1:
                    v1.validate()
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.instance_pattern_infos:
            for v1 in self.instance_pattern_infos:
                 if v1:
                    v1.validate()
        if self.instance_type_candidate_options:
            self.instance_type_candidate_options.validate()
        if self.instance_type_overrides:
            for v1 in self.instance_type_overrides:
                 if v1:
                    v1.validate()
        if self.network_interfaces:
            for v1 in self.network_interfaces:
                 if v1:
                    v1.validate()
        if self.resource_pool_options:
            self.resource_pool_options.validate()
        if self.security_options:
            self.security_options.validate()
        if self.spot_price_limits:
            for v1 in self.spot_price_limits:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_options is not None:
            result['ImageOptions'] = self.image_options.to_map()

        if self.private_pool_options is not None:
            result['PrivatePoolOptions'] = self.private_pool_options.to_map()

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.credit_specification is not None:
            result['CreditSpecification'] = self.credit_specification

        result['CustomPriorities'] = []
        if self.custom_priorities is not None:
            for k1 in self.custom_priorities:
                result['CustomPriorities'].append(k1.to_map() if k1 else None)

        result['DataDisks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['DataDisks'].append(k1.to_map() if k1 else None)

        if self.dedicated_host_cluster_id is not None:
            result['DedicatedHostClusterId'] = self.dedicated_host_cluster_id

        if self.dedicated_host_id is not None:
            result['DedicatedHostId'] = self.dedicated_host_id

        if self.deletion_protection is not None:
            result['DeletionProtection'] = self.deletion_protection

        if self.deployment_set_id is not None:
            result['DeploymentSetId'] = self.deployment_set_id

        if self.host_name is not None:
            result['HostName'] = self.host_name

        if self.hpc_cluster_id is not None:
            result['HpcClusterId'] = self.hpc_cluster_id

        if self.http_endpoint is not None:
            result['HttpEndpoint'] = self.http_endpoint

        if self.http_tokens is not None:
            result['HttpTokens'] = self.http_tokens

        if self.image_family is not None:
            result['ImageFamily'] = self.image_family

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_name is not None:
            result['ImageName'] = self.image_name

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        result['InstancePatternInfos'] = []
        if self.instance_pattern_infos is not None:
            for k1 in self.instance_pattern_infos:
                result['InstancePatternInfos'].append(k1.to_map() if k1 else None)

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_candidate_options is not None:
            result['InstanceTypeCandidateOptions'] = self.instance_type_candidate_options.to_map()

        result['InstanceTypeOverrides'] = []
        if self.instance_type_overrides is not None:
            for k1 in self.instance_type_overrides:
                result['InstanceTypeOverrides'].append(k1.to_map() if k1 else None)

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.internet_charge_type is not None:
            result['InternetChargeType'] = self.internet_charge_type

        if self.internet_max_bandwidth_in is not None:
            result['InternetMaxBandwidthIn'] = self.internet_max_bandwidth_in

        if self.internet_max_bandwidth_out is not None:
            result['InternetMaxBandwidthOut'] = self.internet_max_bandwidth_out

        if self.io_optimized is not None:
            result['IoOptimized'] = self.io_optimized

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight

        if self.memory is not None:
            result['Memory'] = self.memory

        result['NetworkInterfaces'] = []
        if self.network_interfaces is not None:
            for k1 in self.network_interfaces:
                result['NetworkInterfaces'].append(k1.to_map() if k1 else None)

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.password is not None:
            result['Password'] = self.password

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_pool_options is not None:
            result['ResourcePoolOptions'] = self.resource_pool_options.to_map()

        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options

        if self.security_enhancement_strategy is not None:
            result['SecurityEnhancementStrategy'] = self.security_enhancement_strategy

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        if self.security_options is not None:
            result['SecurityOptions'] = self.security_options.to_map()

        if self.spot_duration is not None:
            result['SpotDuration'] = self.spot_duration

        if self.spot_interruption_behavior is not None:
            result['SpotInterruptionBehavior'] = self.spot_interruption_behavior

        result['SpotPriceLimits'] = []
        if self.spot_price_limits is not None:
            for k1 in self.spot_price_limits:
                result['SpotPriceLimits'].append(k1.to_map() if k1 else None)

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        if self.storage_set_id is not None:
            result['StorageSetId'] = self.storage_set_id

        if self.storage_set_partition_number is not None:
            result['StorageSetPartitionNumber'] = self.storage_set_partition_number

        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.custom_priorities = []
        if m.get('CustomPriorities') is not None:
            for k1 in m.get('CustomPriorities'):
                temp_model = main_models.CreateScalingConfigurationRequestCustomPriorities()
                self.custom_priorities.append(temp_model.from_map(k1))

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.CreateScalingConfigurationRequestDataDisks()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('DedicatedHostClusterId') is not None:
            self.dedicated_host_cluster_id = m.get('DedicatedHostClusterId')

        if m.get('DedicatedHostId') is not None:
            self.dedicated_host_id = m.get('DedicatedHostId')

        if m.get('DeletionProtection') is not None:
            self.deletion_protection = m.get('DeletionProtection')

        if m.get('DeploymentSetId') is not None:
            self.deployment_set_id = m.get('DeploymentSetId')

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        if m.get('HpcClusterId') is not None:
            self.hpc_cluster_id = m.get('HpcClusterId')

        if m.get('HttpEndpoint') is not None:
            self.http_endpoint = m.get('HttpEndpoint')

        if m.get('HttpTokens') is not None:
            self.http_tokens = m.get('HttpTokens')

        if m.get('ImageFamily') is not None:
            self.image_family = m.get('ImageFamily')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageName') is not None:
            self.image_name = m.get('ImageName')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k1 in m.get('InstancePatternInfos'):
                temp_model = main_models.CreateScalingConfigurationRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeCandidateOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestInstanceTypeCandidateOptions()
            self.instance_type_candidate_options = temp_model.from_map(m.get('InstanceTypeCandidateOptions'))

        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k1 in m.get('InstanceTypeOverrides'):
                temp_model = main_models.CreateScalingConfigurationRequestInstanceTypeOverrides()
                self.instance_type_overrides.append(temp_model.from_map(k1))

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('InternetChargeType') is not None:
            self.internet_charge_type = m.get('InternetChargeType')

        if m.get('InternetMaxBandwidthIn') is not None:
            self.internet_max_bandwidth_in = m.get('InternetMaxBandwidthIn')

        if m.get('InternetMaxBandwidthOut') is not None:
            self.internet_max_bandwidth_out = m.get('InternetMaxBandwidthOut')

        if m.get('IoOptimized') is not None:
            self.io_optimized = m.get('IoOptimized')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        self.network_interfaces = []
        if m.get('NetworkInterfaces') is not None:
            for k1 in m.get('NetworkInterfaces'):
                temp_model = main_models.CreateScalingConfigurationRequestNetworkInterfaces()
                self.network_interfaces.append(temp_model.from_map(k1))

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourcePoolOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('ResourcePoolOptions'))

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationRequestSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k1 in m.get('SpotPriceLimits'):
                temp_model = main_models.CreateScalingConfigurationRequestSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k1))

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class CreateScalingConfigurationRequestSpotPriceLimits(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        # The instance type of the preemptible instance. This parameter takes effect when SpotStrategy is set to SpotWithPriceLimit.
        self.instance_type = instance_type
        # The bid price for the preemptible instance. This parameter takes effect when SpotStrategy is set to SpotWithPriceLimit.
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.price_limit is not None:
            result['PriceLimit'] = self.price_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('PriceLimit') is not None:
            self.price_limit = m.get('PriceLimit')

        return self

class CreateScalingConfigurationRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        confidential_computing_mode: str = None,
    ):
        # The confidential computing mode. Possible values:
        # 
        # - Enclave: The ECS instance uses an Enclave to build a confidential computing environment. For more information, see [Build a confidential computing environment using an Enclave](https://help.aliyun.com/document_detail/203433.html).
        # 
        # - TDX: Builds a TDX confidential computing environment. For more information, see [Build a TDX confidential computing environment](https://help.aliyun.com/document_detail/479090.html).
        self.confidential_computing_mode = confidential_computing_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.confidential_computing_mode is not None:
            result['ConfidentialComputingMode'] = self.confidential_computing_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfidentialComputingMode') is not None:
            self.confidential_computing_mode = m.get('ConfidentialComputingMode')

        return self

class CreateScalingConfigurationRequestResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        private_pool_tags: List[main_models.CreateScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags] = None,
        strategy: str = None,
    ):
        # The ID of the private pool. This is the ID of the Elastic Assurance or Capacity Reservation service. This parameter can only accept Target mode private pool IDs and cannot be specified at the same time as the PrivatePoolTags parameter.
        self.private_pool_ids = private_pool_ids
        # Filter available Target private pools by tags. N is an integer from 1 to 20.
        # Note:
        # 
        # - When this parameter is configured, the system only selects from the associated Target private pools under the account that have matching tags and also meet the scaling group constraints (such as zone, instance type, etc.).
        # 
        # - Tag matching rule: The private pool must match all specified tags.
        # 
        # - This parameter cannot be specified at the same time as the PrivatePoolIds parameter.
        self.private_pool_tags = private_pool_tags
        # The resource pool, which includes private pools generated after an Elastic Assurance or Capacity Reservation service takes effect, and the public pool, can be selected for instance startup. Valid values:
        # 
        # - PrivatePoolFirst: Private pool first. When this policy is selected, if you specify ResourcePoolOptions.PrivatePoolIds or meet the PrivatePoolTags conditions, the corresponding private pool is used first. If no private pool is specified or the specified private pool has insufficient capacity, the system automatically matches an open-type private pool. If no eligible private pool is found, the instance is created using the public pool.
        # 
        # - PrivatePoolOnly: Private pool only. When this policy is selected, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pool has insufficient capacity, the instance fails to start.
        # 
        # - PublicPoolFirst: Public pool resources first. The system prioritizes creating the instance using the public pool. When public pool resources are insufficient, private pool resources are used as a supplement. The system first automatically matches an open-type private pool. If no eligible private pool is found, it uses a Target-type private pool that is specified by ResourcePoolOptions.PrivatePoolIds or meets the PrivatePoolTags conditions. (This policy is in invitational preview and is not yet available for use.)
        # 
        # - None: No resource pool policy is used.
        # 
        # Default value: None.
        self.strategy = strategy

    def validate(self):
        if self.private_pool_tags:
            for v1 in self.private_pool_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.private_pool_ids is not None:
            result['PrivatePoolIds'] = self.private_pool_ids

        result['PrivatePoolTags'] = []
        if self.private_pool_tags is not None:
            for k1 in self.private_pool_tags:
                result['PrivatePoolTags'].append(k1.to_map() if k1 else None)

        if self.strategy is not None:
            result['Strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivatePoolIds') is not None:
            self.private_pool_ids = m.get('PrivatePoolIds')

        self.private_pool_tags = []
        if m.get('PrivatePoolTags') is not None:
            for k1 in m.get('PrivatePoolTags'):
                temp_model = main_models.CreateScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags()
                self.private_pool_tags.append(temp_model.from_map(k1))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the private pool.
        self.key = key
        # The tag value of the private pool.
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

class CreateScalingConfigurationRequestNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        secondary_private_ip_address_count: int = None,
        security_group_ids: List[str] = None,
    ):
        # The type of ENI. When using this parameter, you must use NetworkInterfaces to set the primary NIC and cannot set the SecurityGroupId or SecurityGroupIds parameters. Valid values:
        # 
        # - Primary: primary NIC.
        # 
        # - Secondary: secondary NIC.
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses to assign to the primary NIC.
        # Note:
        # 
        # - This parameter takes effect only when NetworkInterface.InstanceType is set to Primary. If NetworkInterface.InstanceType is set to Secondary or is empty, you cannot set this parameter.
        # 
        # - If you set this parameter, you cannot set Ipv6AddressCount.
        self.ipv_6address_count = ipv_6address_count
        # The communication mode of the NIC. Valid values:
        # 
        # - Standard: uses TCP communication mode.
        # 
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses RDMA communication mode.
        # 
        # Default value: Standard.
        # 
        # > The number of ENIs in RDMA mode cannot exceed the limit for the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of secondary private IPv4 addresses to assign to the NIC. Valid values: 1 to 49.
        # 
        # - The value cannot exceed the IP address limit for the instance type. For more information, see [Instance families](https://help.aliyun.com/en/ecs/user-guide/overview-of-instance-families).
        # 
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount is used to assign a number of secondary private IPv4 addresses to the NIC (excluding the primary private IP address). The system randomly assigns these addresses from the available CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) where the NIC is located.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # One or more security group IDs to which the ENI belongs.
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.network_interface_traffic_mode is not None:
            result['NetworkInterfaceTrafficMode'] = self.network_interface_traffic_mode

        if self.secondary_private_ip_address_count is not None:
            result['SecondaryPrivateIpAddressCount'] = self.secondary_private_ip_address_count

        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('NetworkInterfaceTrafficMode') is not None:
            self.network_interface_traffic_mode = m.get('NetworkInterfaceTrafficMode')

        if m.get('SecondaryPrivateIpAddressCount') is not None:
            self.secondary_private_ip_address_count = m.get('SecondaryPrivateIpAddressCount')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

class CreateScalingConfigurationRequestInstanceTypeOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        # If you want the scaling group to scale based on the capacity of instance types, specify both this parameter and WeightedCapacity.
        # 
        # This parameter specifies the instance type and overwrites the instance type in the launch template. You can specify this parameter up to 20 times. N is an integer from 1 to 20.
        # 
        # > This parameter takes effect only when a launch template is specified by the LaunchTemplateId parameter.
        # 
        # Valid values for InstanceType: available ECS instance types.
        self.instance_type = instance_type
        # To specify the capacity of an instance type in the scaling configuration, specify this parameter after you specify InstanceTypeOverrides.InstanceType.
        # 
        # This parameter specifies the weight of the instance type. The weight indicates the capacity of a single instance of the specified instance type in the scaling group. A higher weight means that fewer instances of that type are needed to meet the desired capacity.
        # 
        # You can configure different weights for different instance types based on their performance metrics, such as the number of vCPUs and memory size.
        # 
        # For example:
        # 
        # - Current capacity: 0.
        # 
        # - Expected capacity: 6.
        # 
        # - Capacity of ecs.c5.xlarge: 4.
        # 
        # To meet the expected capacity, the scaling group will scale out two ecs.c5.xlarge instances.
        # 
        # > During a scale-out, the capacity of the scaling group cannot exceed the sum of MaxSize and the maximum weight of the instance type.
        # 
        # Valid values for WeightedCapacity: 1 to 500.
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

        if self.weighted_capacity is not None:
            result['WeightedCapacity'] = self.weighted_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('WeightedCapacity') is not None:
            self.weighted_capacity = m.get('WeightedCapacity')

        return self

class CreateScalingConfigurationRequestInstanceTypeCandidateOptions(DaraModel):
    def __init__(
        self,
        allow_cidr_blocks: List[str] = None,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        enabled: bool = None,
        max_price: float = None,
    ):
        # When supplementing with vSwitches from other zones is allowed, you must specify the CIDR blocks for the candidate vSwitches.
        self.allow_cidr_blocks = allow_cidr_blocks
        # Specifies whether to allow supplementing with vSwitches from other zones.
        # 
        # > The instance type remains unchanged; only new zones are considered as candidates. When a scaling group cannot scale out in any of the selected zones due to issues like insufficient inventory, this configuration allows ESS to automatically add a vSwitch from a new zone to the scaling group.
        # > For example, if a scaling group is configured for zones cn-hangzhou-h and cn-hangzhou-g, and neither can be scaled out, ESS might create and add a vSwitch in cn-hangzhou-k based on real-time inventory.
        self.allow_cross_az = allow_cross_az
        # Specifies whether to allow supplementing with instance types from other generations.
        # 
        # - For example, if the current instance type is ecs.c7.large, enabling this allows ecs.c6.large and ecs.c8.large as candidate types.
        self.allow_different_generation = allow_different_generation
        # Specifies whether to enable the candidate mode.
        self.enabled = enabled
        # The maximum price for candidate instance types.
        self.max_price = max_price

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_cidr_blocks is not None:
            result['AllowCidrBlocks'] = self.allow_cidr_blocks

        if self.allow_cross_az is not None:
            result['AllowCrossAz'] = self.allow_cross_az

        if self.allow_different_generation is not None:
            result['AllowDifferentGeneration'] = self.allow_different_generation

        if self.enabled is not None:
            result['Enabled'] = self.enabled

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowCidrBlocks') is not None:
            self.allow_cidr_blocks = m.get('AllowCidrBlocks')

        if m.get('AllowCrossAz') is not None:
            self.allow_cross_az = m.get('AllowCrossAz')

        if m.get('AllowDifferentGeneration') is not None:
            self.allow_different_generation = m.get('AllowDifferentGeneration')

        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        return self

class CreateScalingConfigurationRequestInstancePatternInfos(DaraModel):
    def __init__(
        self,
        architectures: List[str] = None,
        burstable_performance: str = None,
        cores: int = None,
        cpu_architectures: List[str] = None,
        excluded_instance_types: List[str] = None,
        gpu_specs: List[str] = None,
        instance_categories: List[str] = None,
        instance_family_level: str = None,
        instance_type_families: List[str] = None,
        max_price: float = None,
        maximum_cpu_core_count: int = None,
        maximum_gpu_amount: int = None,
        maximum_memory_size: float = None,
        memory: float = None,
        minimum_baseline_credit: int = None,
        minimum_cpu_core_count: int = None,
        minimum_eni_ipv_6address_quantity: int = None,
        minimum_eni_private_ip_address_quantity: int = None,
        minimum_eni_quantity: int = None,
        minimum_gpu_amount: int = None,
        minimum_initial_credit: int = None,
        minimum_memory_size: float = None,
        physical_processor_models: List[str] = None,
    ):
        # The architecture type of the instance type. Valid values:
        # 
        # - X86: X86 compute.
        # 
        # - Heterogeneous: heterogeneous computing, such as GPU or FPGA.
        # 
        # - BareMental: ECS Bare Metal Instance.
        # 
        # - Arm: Arm compute.
        # 
        # Default value: all architecture types are included.
        self.architectures = architectures
        # Specifies whether to include burstable instance types. Valid values:
        # 
        # - Exclude: does not include burstable instance types.
        # 
        # - Include: includes burstable instance types.
        # 
        # - Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # In intelligent configuration mode, the number of vCPU cores of the instance type. This is used to filter instance types that meet the requirements. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # Note the following:
        # 
        # - The InstancePatternInfos parameter applies only when the network type of the scaling group is VPC.
        # 
        # - When using InstancePatternInfos, you must specify both InstancePatternInfos.Cores and InstancePatternInfos.Memory.
        # 
        # - If you have already specified instance types using the InstanceType or InstanceTypes parameter, Auto Scaling prioritizes the specified instance types for scale-outs. If the specified instance types are out of stock, Auto Scaling uses the instance type with the lowest price from the instance types that match the InstancePatternInfos parameter.
        self.cores = cores
        # The CPU architecture of the instance. Valid values:
        # 
        # > You can specify multiple CPU architectures. N is an integer from 1 to 2.
        # 
        # - X86.
        # 
        # - ARM.
        self.cpu_architectures = cpu_architectures
        # The instance types to exclude. You can use a wildcard character (\\*) to exclude a single instance type or an entire instance family. For example:
        # 
        # - ecs.c6.large: excludes the ecs.c6.large instance type.
        # 
        # - ecs.c6.\\*: excludes all instance types in the c6 family.
        self.excluded_instance_types = excluded_instance_types
        # The GPU type.
        self.gpu_specs = gpu_specs
        # The category of the instance. Valid values:
        # 
        # > You can specify multiple instance categories. N is an integer from 1 to 10.
        # 
        # - General-purpose: General-purpose.
        # 
        # - Compute-optimized: compute-optimized.
        # 
        # - Memory-optimized: memory-optimized.
        # 
        # - Big data: big data.
        # 
        # - Local SSDs : local SSDs.
        # 
        # - High Clock Speed : high frequency.
        # 
        # - Enhanced : enhanced instance families.
        # 
        # - Shared: shared-resource instances.
        # 
        # - Compute-optimized with GPU : GPU compute-optimized.
        # 
        # - Visual Compute-optimized : visual compute-optimized.
        # 
        # - Heterogeneous Service : heterogeneous service.
        # 
        # - Compute-optimized with FPGA : FPGA compute-optimized.
        # 
        # - Compute-optimized with NPU : NPU compute-optimized.
        # 
        # - ECS Bare Metal : ECS Bare Metal Instance.
        # 
        # - High Performance Compute: high-performance computing.
        self.instance_categories = instance_categories
        # The level of the instance family, used to filter instance types that meet the requirements. This parameter takes effect when `CostOptimization` is enabled. Valid values:
        # 
        # - EntryLevel: entry-level, which refers to shared-resource instances. This level offers lower costs but cannot guarantee stable computing performance. It is suitable for business scenarios with low CPU utilization. For more information, see [Shared-resource instances](https://help.aliyun.com/document_detail/108489.html).
        # 
        # - EnterpriseLevel: enterprise-level. This level provides stable performance and dedicated resources, suitable for business scenarios that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # - CreditEntryLevel: credit entry-level, which refers to burstable instances. This level uses CPU credits to ensure computing performance and is suitable for business scenarios with low CPU utilization and occasional CPU bursts. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families to query. You can specify multiple instance families. N is an integer from 1 to 10.
        self.instance_type_families = instance_type_families
        # In intelligent configuration mode, the maximum hourly price you are willing to pay for a pay-as-you-go or preemptible instance. This is used to filter instance types that meet the requirements.
        # 
        # > This parameter is required when SpotStrategy is set to SpotWithPriceLimit. In other cases, this parameter is optional.
        self.max_price = max_price
        # The maximum number of vCPU cores for the instance type.
        # 
        # > MaximumCpuCoreCount cannot be more than four times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs for the instance. The value must be a positive integer.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size of the instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # In intelligent configuration mode, the memory size of the instance type. Unit: GiB. This is used to filter instance types that meet the requirements.
        self.memory = memory
        # The minimum baseline vCPU performance (the sum of all vCPUs) for burstable instances of the t5 or t6 family.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPU cores for the instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum number of IPv6 addresses that can be assigned to a single ENI.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of private IPv4 addresses to assign to a single elastic network interface (ENI) of an instance.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) that can be attached to an instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs for the instance. The value must be a positive integer.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The minimum initial vCPU credit for burstable instances of the t5 or t6 family.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size of the instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor model of the instance. You can specify multiple processor models. N is an integer from 1 to 10.
        self.physical_processor_models = physical_processor_models

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

        if self.cpu_architectures is not None:
            result['CpuArchitectures'] = self.cpu_architectures

        if self.excluded_instance_types is not None:
            result['ExcludedInstanceTypes'] = self.excluded_instance_types

        if self.gpu_specs is not None:
            result['GpuSpecs'] = self.gpu_specs

        if self.instance_categories is not None:
            result['InstanceCategories'] = self.instance_categories

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_type_families is not None:
            result['InstanceTypeFamilies'] = self.instance_type_families

        if self.max_price is not None:
            result['MaxPrice'] = self.max_price

        if self.maximum_cpu_core_count is not None:
            result['MaximumCpuCoreCount'] = self.maximum_cpu_core_count

        if self.maximum_gpu_amount is not None:
            result['MaximumGpuAmount'] = self.maximum_gpu_amount

        if self.maximum_memory_size is not None:
            result['MaximumMemorySize'] = self.maximum_memory_size

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.minimum_baseline_credit is not None:
            result['MinimumBaselineCredit'] = self.minimum_baseline_credit

        if self.minimum_cpu_core_count is not None:
            result['MinimumCpuCoreCount'] = self.minimum_cpu_core_count

        if self.minimum_eni_ipv_6address_quantity is not None:
            result['MinimumEniIpv6AddressQuantity'] = self.minimum_eni_ipv_6address_quantity

        if self.minimum_eni_private_ip_address_quantity is not None:
            result['MinimumEniPrivateIpAddressQuantity'] = self.minimum_eni_private_ip_address_quantity

        if self.minimum_eni_quantity is not None:
            result['MinimumEniQuantity'] = self.minimum_eni_quantity

        if self.minimum_gpu_amount is not None:
            result['MinimumGpuAmount'] = self.minimum_gpu_amount

        if self.minimum_initial_credit is not None:
            result['MinimumInitialCredit'] = self.minimum_initial_credit

        if self.minimum_memory_size is not None:
            result['MinimumMemorySize'] = self.minimum_memory_size

        if self.physical_processor_models is not None:
            result['PhysicalProcessorModels'] = self.physical_processor_models

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architectures') is not None:
            self.architectures = m.get('Architectures')

        if m.get('BurstablePerformance') is not None:
            self.burstable_performance = m.get('BurstablePerformance')

        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        if m.get('CpuArchitectures') is not None:
            self.cpu_architectures = m.get('CpuArchitectures')

        if m.get('ExcludedInstanceTypes') is not None:
            self.excluded_instance_types = m.get('ExcludedInstanceTypes')

        if m.get('GpuSpecs') is not None:
            self.gpu_specs = m.get('GpuSpecs')

        if m.get('InstanceCategories') is not None:
            self.instance_categories = m.get('InstanceCategories')

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypeFamilies') is not None:
            self.instance_type_families = m.get('InstanceTypeFamilies')

        if m.get('MaxPrice') is not None:
            self.max_price = m.get('MaxPrice')

        if m.get('MaximumCpuCoreCount') is not None:
            self.maximum_cpu_core_count = m.get('MaximumCpuCoreCount')

        if m.get('MaximumGpuAmount') is not None:
            self.maximum_gpu_amount = m.get('MaximumGpuAmount')

        if m.get('MaximumMemorySize') is not None:
            self.maximum_memory_size = m.get('MaximumMemorySize')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('MinimumBaselineCredit') is not None:
            self.minimum_baseline_credit = m.get('MinimumBaselineCredit')

        if m.get('MinimumCpuCoreCount') is not None:
            self.minimum_cpu_core_count = m.get('MinimumCpuCoreCount')

        if m.get('MinimumEniIpv6AddressQuantity') is not None:
            self.minimum_eni_ipv_6address_quantity = m.get('MinimumEniIpv6AddressQuantity')

        if m.get('MinimumEniPrivateIpAddressQuantity') is not None:
            self.minimum_eni_private_ip_address_quantity = m.get('MinimumEniPrivateIpAddressQuantity')

        if m.get('MinimumEniQuantity') is not None:
            self.minimum_eni_quantity = m.get('MinimumEniQuantity')

        if m.get('MinimumGpuAmount') is not None:
            self.minimum_gpu_amount = m.get('MinimumGpuAmount')

        if m.get('MinimumInitialCredit') is not None:
            self.minimum_initial_credit = m.get('MinimumInitialCredit')

        if m.get('MinimumMemorySize') is not None:
            self.minimum_memory_size = m.get('MinimumMemorySize')

        if m.get('PhysicalProcessorModels') is not None:
            self.physical_processor_models = m.get('PhysicalProcessorModels')

        return self

class CreateScalingConfigurationRequestDataDisks(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        categories: List[str] = None,
        category: str = None,
        delete_with_instance: bool = None,
        description: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        # The ID of the automatic snapshot policy to apply to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable performance burst for the system disk. Valid values:
        # 
        # - true: Enables performance burst.
        # 
        # - false: Disables performance burst.
        # 
        # > This parameter is available only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">
        # 
        # For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # Multiple disk categories for the data disk. When a disk of a higher-priority category is unavailable, Auto Scaling automatically tries the next lower-priority category. Valid values:
        # 
        # - cloud: basic disk. The DeleteWithInstance attribute of a basic disk created with an instance is true.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # > If you specify this parameter, you cannot specify `DataDisks.Category`.
        self.categories = categories
        # The category of the data disk. Valid values:
        # 
        # - cloud: basic disk.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - ephemeral_ssd: local SSD.
        # 
        # - cloud_auto: ESSD AutoPL disk.
        # 
        # You cannot specify this parameter and DataDisk.Categories at the same time. If you do not specify this parameter or DataDisk.Categories, the default value of this parameter is used:
        # 
        # - For I/O optimized instances, the default value is cloud_efficiency.
        # 
        # - For non-I/O optimized instances, the default value is cloud.
        self.category = category
        # Specifies whether to release the data disk when the instance is released. Valid values:
        # 
        # - true: releases the disk when the instance is released.
        # 
        # - false: retains the disk when the instance is released.
        # 
        # This parameter can be set only for separately purchased cloud disks (DataDisks.Category is cloud, cloud_efficiency, cloud_ssd, or cloud_essd). Otherwise, an error occurs.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data disk. If you do not specify this parameter, the system automatically assigns a mount point when creating the ECS instance, starting from /dev/xvdb and ending at /dev/xvdz.
        self.device = device
        # The name of the data disk. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # Specifies whether to encrypt the data disk. Valid values:
        # 
        # - true: encrypts the disk.
        # 
        # - false: does not encrypt the disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the KMS key for the data disk.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD that is used as the data disk. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # 
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # 
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # 
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > For information about how to select an ESSD performance level, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned IOPS of the data disk.
        # 
        # > IOPS (input/output operations per second) indicates the number of I/O operations that a block storage device can process per second. It represents the read and write capabilities of the device.
        self.provisioned_iops = provisioned_iops
        # The size of the data disk. Unit: GiB. Valid values:
        # 
        # - cloud: 5 to 2000.
        # 
        # - cloud_efficiency: 20 to 32768.
        # 
        # - cloud_essd: 20 to 32768.
        # 
        # - ephemeral_ssd: 5 to 800.
        # 
        # If you specify this parameter, the disk size must be greater than or equal to the snapshot size specified by SnapshotId.
        self.size = size
        # The snapshot to use to create the data disk. If you specify this parameter, DataDisks.Size is ignored. The size of the created disk is the size of the specified snapshot.
        # 
        # If the snapshot was created on or before July 15, 2013, the call is rejected and an InvalidSnapshot.TooOld error is returned.
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

        if self.categories is not None:
            result['Categories'] = self.categories

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

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

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

        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

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

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        return self

class CreateScalingConfigurationRequestCustomPriorities(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        vswitch_id: str = None,
    ):
        # The instance type of the ECS instance.
        # 
        # >Notice: 
        # 
        # Must be included in the list of instance types in the scaling configuration.
        self.instance_type = instance_type
        # The ID of the vSwitch.
        # 
        # >Notice: 
        # 
        # Must be included in the list of vSwitches in the scaling group.
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')

        return self

class CreateScalingConfigurationRequestSystemDisk(DaraModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        description: str = None,
        disk_name: str = None,
        encrypt_algorithm: str = None,
        encrypted: bool = None,
        kmskey_id: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
    ):
        # The ID of the automatic snapshot policy to apply to the system disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature for the system disk. Valid values:
        # 
        # - true: enables the feature.
        # 
        # - false: disables the feature.
        # 
        # > You can set this parameter only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">
        # 
        # For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of the system disk. Valid values:
        # 
        # - cloud: basic disk.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - ephemeral_ssd: local SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud_auto: ESSD AutoPL disk.
        # 
        # You cannot specify this parameter and `SystemDiskCategories` at the same time. If you do not specify this parameter or `SystemDiskCategories`, the default value of this parameter is used:
        # 
        # - For I/O optimized instances, the default value is cloud_efficiency.
        # 
        # - For non-I/O optimized instances, the default value is cloud.
        self.category = category
        # The description of the system disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length. It must start with a letter or a Chinese character and cannot start with `http://` or `https://`. It can contain digits, colons (:), underscores (_), and hyphens (-).
        self.disk_name = disk_name
        # The encryption algorithm for the system disk. Valid values:
        # 
        # - AES-256.
        # 
        # - SM4-128.
        # 
        # Default value: AES-256.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypts the disk.
        # 
        # - false: does not encrypt the disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the KMS key to use for the system disk.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD that is used as the system disk. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # 
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # 
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # 
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        self.performance_level = performance_level
        # The provisioned IOPS of the system disk.
        # 
        # > IOPS (input/output operations per second) indicates the number of I/O operations that a block storage device can process per second. It represents the read and write capabilities of the device.
        self.provisioned_iops = provisioned_iops
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # - Basic disk: 20 to 500.
        # 
        # - ESSD:
        # 
        #   - PL0: 1 to 2048.
        # 
        #   - PL1: 20 to 2048.
        # 
        #   - PL2: 461 to 2048.
        # 
        #   - PL3: 1261 to 2048.
        # 
        # - ESSD AutoPL disk: 1 to 2048.
        # 
        # - Other disk categories: 20 to 2048.
        # 
        # The value of this parameter must be greater than or equal to max{1, ImageSize}.
        # 
        # Default value: max{40, ImageSize}.
        self.size = size

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

        if self.description is not None:
            result['Description'] = self.description

        if self.disk_name is not None:
            result['DiskName'] = self.disk_name

        if self.encrypt_algorithm is not None:
            result['EncryptAlgorithm'] = self.encrypt_algorithm

        if self.encrypted is not None:
            result['Encrypted'] = self.encrypted

        if self.kmskey_id is not None:
            result['KMSKeyId'] = self.kmskey_id

        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.provisioned_iops is not None:
            result['ProvisionedIops'] = self.provisioned_iops

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoSnapshotPolicyId') is not None:
            self.auto_snapshot_policy_id = m.get('AutoSnapshotPolicyId')

        if m.get('BurstingEnabled') is not None:
            self.bursting_enabled = m.get('BurstingEnabled')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DiskName') is not None:
            self.disk_name = m.get('DiskName')

        if m.get('EncryptAlgorithm') is not None:
            self.encrypt_algorithm = m.get('EncryptAlgorithm')

        if m.get('Encrypted') is not None:
            self.encrypted = m.get('Encrypted')

        if m.get('KMSKeyId') is not None:
            self.kmskey_id = m.get('KMSKeyId')

        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('ProvisionedIops') is not None:
            self.provisioned_iops = m.get('ProvisionedIops')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class CreateScalingConfigurationRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private pool. This is the ID of the Elastic Assurance or Capacity Reservation service.
        self.id = id
        # The private pool capacity option for instance startup. After an Elastic Assurance or a Capacity Reservation service takes effect, a private pool is generated. You can select a private pool to start an instance. Valid values:
        # 
        # - Open: open mode. The system automatically matches the instance with an open private pool. If no eligible private pool is found, the instance is started using public pool resources. You do not need to set the PrivatePoolOptions.Id parameter in this mode.
        # 
        # - Target: specified mode. The instance is started using the capacity of a specified private pool. If the specified private pool is unavailable, the instance fails to start. You must set the PrivatePoolOptions.Id parameter in this mode.
        # 
        # - None: no private pool is used. The instance is started without using a private pool.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.match_criteria is not None:
            result['MatchCriteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchCriteria') is not None:
            self.match_criteria = m.get('MatchCriteria')

        return self

class CreateScalingConfigurationRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether to use the ecs-user user to log on to the ECS instance. For more information, see [Manage logon usernames of ECS instances](https://help.aliyun.com/document_detail/388447.html). Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        # 
        # Default value: false.
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

