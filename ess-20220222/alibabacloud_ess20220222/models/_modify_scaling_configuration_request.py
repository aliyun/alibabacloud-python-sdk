# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyScalingConfigurationRequest(DaraModel):
    def __init__(
        self,
        image_options: main_models.ModifyScalingConfigurationRequestImageOptions = None,
        private_pool_options: main_models.ModifyScalingConfigurationRequestPrivatePoolOptions = None,
        system_disk: main_models.ModifyScalingConfigurationRequestSystemDisk = None,
        affinity: str = None,
        cpu: int = None,
        credit_specification: str = None,
        custom_priorities: List[main_models.ModifyScalingConfigurationRequestCustomPriorities] = None,
        data_disks: List[main_models.ModifyScalingConfigurationRequestDataDisks] = None,
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
        instance_pattern_infos: List[main_models.ModifyScalingConfigurationRequestInstancePatternInfos] = None,
        instance_type_candidate_options: main_models.ModifyScalingConfigurationRequestInstanceTypeCandidateOptions = None,
        instance_type_overrides: List[main_models.ModifyScalingConfigurationRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        network_interfaces: List[main_models.ModifyScalingConfigurationRequestNetworkInterfaces] = None,
        override: bool = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_pool_options: main_models.ModifyScalingConfigurationRequestResourcePoolOptions = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scheduler_options: Dict[str, Any] = None,
        secondary_eni_vswitch_constraint: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_options: main_models.ModifyScalingConfigurationRequestSecurityOptions = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[main_models.ModifyScalingConfigurationRequestSpotPriceLimits] = None,
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
        # Specifies whether the instance on a dedicated host is associated with the dedicated host. Valid values:
        # 
        # - default: The instance is not associated with the dedicated host. When an instance that has the economical mode enabled is restarted, the instance may be placed on another dedicated host in the automatic deployment resource pool if the original dedicated host has insufficient resources.
        # 
        # - host: The instance is associated with the dedicated host. When an instance that has the economical mode enabled is restarted, the instance remains on the original dedicated host. If the original dedicated host has insufficient resources, the instance fails to restart.
        self.affinity = affinity
        # The number of vCPUs. Unit: cores.
        # 
        # You can specify both CPU and Memory to define the range of instance types. For example, CPU=2 and Memory=16 defines all instance types with 2 vCPUs and 16 GiB of memory. Auto Scaling determines the set of active instance types based on factors such as I/O optimization and zones, and then creates instances of the lowest-priced instance type based on sorting by price.
        # 
        # > This configuration takes effect only when the cost optimization mode is enabled and no instance type is specified in the scaling configuration.
        self.cpu = cpu
        # Modifies the running mode of a burstable instance. Valid values:
        # 
        # - Standard: standard mode. For more information, see the performance constrained mode section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # 
        # - Unlimited: unlimited mode. For more information, see the unlimited mode section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The custom priorities for ECS instance type + vSwitch combinations.
        # >Notice: This parameter takes effect only when the scaling policy of the scaling group is set to priority-based policy.
        # 
        # When an instance cannot be created based on the instance type and vSwitch combination with a higher priority, Auto Scaling automatically selects the next-priority instance type and vSwitch combination to create the instance.
        # 
        # > If you specify custom priorities for only some instance type + vSwitch combinations, the unspecified combinations have lower priorities than the specified ones. The unspecified combinations are still prioritized based on the vSwitch order of the scaling group and the instance type order of the scaling configuration.
        # > - For example, if the vSwitch order of the scaling group is vsw1 and vsw2, the instance type order of the scaling configuration is type1 and type2, and the custom priority order is ["vsw2+type2", "vsw1+type2"], the final priority is: "vsw2+type2" > "vsw1+type2" > "vsw1+type1" > "vsw2+type1".
        self.custom_priorities = custom_priorities
        # The collection of data cloud disk information.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # Specifies whether to create the ECS instance on a dedicated host. Because dedicated hosts do not support the creation of spot instances, if you specify the DedicatedHostId parameter, the SpotStrategy and SpotPriceLimit settings in the request are automatically ignored.
        # 
        # You can call the DescribeDedicatedHosts operation to query the list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The release protection property of the instance. Specifies whether the instance can be directly released from the ECS console or by calling the DeleteInstance operation, to prevent accidental deletion. Valid values:
        # 
        # - true: Enables release protection. The instance cannot be directly released from the ECS console or by calling the DeleteInstance operation.
        # 
        # - false: Disables release protection. The instance can be directly released from the ECS console or by calling the DeleteInstance operation.
        # 
        # > This property applies only to pay-as-you-go instances. It prevents instances created by Auto Scaling scale-out activities from being accidentally deleted, but does not affect normal scale-in activities. Instances with release protection enabled can still be released by scale-in activities.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the ECS instance belongs.
        self.deployment_set_id = deployment_set_id
        # The hostname of the Elastic Compute Service (ECS) server. A period (.) or a hyphen (-) cannot be used as the first or last character, or used consecutively. In addition, the naming conventions for different types of instances are as follows: 
        # 
        # - Windows instances: The hostname must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot contain periods (.) or consist entirely of digits. 
        # - Other instances (such as Linux): The hostname must be 2 to 64 characters in length and can contain multiple periods (.). Each segment between two periods (.) can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the HPC cluster to which the ECS instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # - enabled: enabled.
        # - disabled: disabled.
        # 
        # Default value: enabled.
        # 
        # > For information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # Specifies whether to forcefully use the security-hardened mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # - optional: does not forcefully use the security-hardened mode.
        # - required: forcefully uses the security-hardened mode. After you set this value, instance metadata cannot be accessed in normal mode.
        # 
        # Default value: optional.
        # 
        # > For more information about the modes for accessing instance metadata, see [Instance metadata access modes](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image from the specified image family for instance creation. If you have specified the `ImageId` parameter, you cannot specify this parameter.
        self.image_family = image_family
        # The ID of the image file used for automatic creation of instances.
        # 
        # > If the image previously used in the scaling configuration includes a system cloud disk and data cloud disks, the data cloud disk information is purged after you change the image.
        self.image_id = image_id
        # The name of the image. Image names must be unique within a region. If you specify ImageId, ImageName is ignored.
        # 
        # You cannot use ImageName to specify images from Alibaba Cloud Marketplace.
        self.image_name = image_name
        # The description of the ECS instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.instance_description = instance_description
        # The name of the ECS instance that is automatically created by using the scaling configuration.
        self.instance_name = instance_name
        # The collection of intelligent configuration information used to filter instance types that meet the requirements.
        self.instance_pattern_infos = instance_pattern_infos
        # After the fallback mode is enabled, when issues such as insufficient inventory are encountered, similar instance types of the same size are supplemented based on the currently selected instance types, or vSwitches in alternative zones are created and added to the scaling group.
        self.instance_type_candidate_options = instance_type_candidate_options
        # The information about specified instance types.
        self.instance_type_overrides = instance_type_overrides
        # The instance types for multiple instance type support. If InstanceTypes is specified, InstanceType is ignored.
        # 
        # When instances cannot be created by using the instance type with a higher priority, Auto Scaling automatically selects the instance type with the next priority to create instances.
        self.instance_types = instance_types
        # The billing method for network usage. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth. In this case, the value of InternetMaxBandwidthOut specifies the fixed bandwidth value. 
        # - PayByTraffic: pay-by-traffic. In this case, the value of InternetMaxBandwidthOut specifies only the maximum bandwidth, and billing is based on the actual network traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - If the purchased maximum outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - If the purchased maximum outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. Valid values:
        # - none: The instance is not an I/O optimized instance.
        # - optimized: The instance is an I/O optimization instance.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses allocated to the elastic network interfaces (ENIs).
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair used to log on to the ECS instance. 
        #          
        # - For Windows instances, this parameter is ignored and is empty by default. 
        # - For Linux instances, password-based logon is disabled during initialization.
        self.key_pair_name = key_pair_name
        # The weight of SLB backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # 
        # You can specify both CPU and Memory to define the range of instance types. For example, CPU=2 and Memory=16 defines all instance types with 2 vCPUs and 16 GiB of memory. Auto Scaling determines the set of active instance types based on factors such as I/O optimization and zones, and then creates instances of the lowest-priced instance type based on sorting by price.
        # 
        # > This configuration takes effect only when the cost optimization mode is enabled and no instance type is specified in the scaling configuration.
        self.memory = memory
        # The list of elastic network interfaces (ENIs).
        self.network_interfaces = network_interfaces
        # Specifies whether to override existing data. Valid values:
        # - true: overrides existing data.
        # - false: does not override existing data.
        self.override = override
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the ECS instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        # 
        # `()~!@#$%^&*-_+=\\|{}[]:;\\"<>,.?/
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you specify the Password parameter, we recommend that you send the request over HTTPS to prevent password leaks.
        self.password = password
        # Specifies whether to use the password preset in the image. To use this parameter, ensure that a password is configured for the image.
        self.password_inherit = password_inherit
        # The name of the RAM role associated with the ECS instance. This name is provided and maintained by RAM. You can call the ListRoles operation to query available RAM roles. For more information about how to create a RAM role, see the CreateRole operation.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The resource pool policy used when creating instances. After you specify this parameter, note the following items:
        # 
        # - This parameter takes effect only when pay-as-you-go instances are created.
        # 
        # - This parameter cannot be specified together with PrivatePoolOptions.MatchCriteria or PrivatePoolOptions.Id.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling configuration that you want to modify.
        # 
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration. The name must be 2 to 64 characters in length and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter, digit, or Chinese character.
        # 
        # The name of the scaling configuration must be unique within a scaling group in the same region. If you do not specify this parameter, the ID of the scaling configuration is used by default.
        self.scaling_configuration_name = scaling_configuration_name
        # The scheduler options.
        self.scheduler_options = scheduler_options
        # Specifies whether a vSwitch must be selected from the VSwitchIds list for the secondary elastic network interfaces (ENIs) when the VSwitchIds parameter is set for the secondary network interface controller (NIC).
        # 
        # - Strict: strict mode. If no vSwitch in VSwitchIds meets the conditional requirements, instance creation fails.
        # - Tolerant: tolerant mode. If no vSwitch in VSwitchIds meets the conditional requirements, no secondary network interface controller (NIC) is configured, but the instance is still created as active.
        # 
        # Default value: Strict.
        self.secondary_eni_vswitch_constraint = secondary_eni_vswitch_constraint
        # The ID of the security group to which the ECS instance belongs. ECS instances in the same security group can access each other.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the instance belongs.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours. Valid values:
        # 
        # - 1: After a spot instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After 1 hour, the system compares the bid price with the market price and checks resource availability to determine whether to retain automatic release the instance.
        # - 0: After a spot instance is created, Alibaba Cloud does not ensure that the instance runs for 1 hour. The system compares the bid price with the market price and checks resource availability to determine whether to retain automatic release the instance.
        # 
        # > Alibaba Cloud sends an ECS system event notification 5 minutes before the instance is released. Spot instances are billed by second. We recommend that you select an appropriate protection period based on the expected task execution duration.
        # 
        # Default value: 1.
        self.spot_duration = spot_duration
        # The interruption mode of the spot instance. Currently, only Terminate (default) is supported, which directly releases the instance.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The information about spot instance types.
        self.spot_price_limits = spot_price_limits
        # The preemption policy for pay-as-you-go instances. Valid values:
        #          
        # - NoSpot: a regular pay-as-you-go instance.
        # - SpotWithPriceLimit: a spot instance with a user-defined maximum hourly price.
        # - SpotAsPriceGo: a spot instance for which the market price at the time of purchase is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        # The storage set ID.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. The value must be an integer that is greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The multi-disk types for the system cloud disk. When a disk type with a higher priority is unavailable, Auto Scaling automatically attempts the next-priority disk type to create the system cloud disk. Valid values:
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: Enterprise SSD (ESSD).
        # 
        # > If you specify this parameter, you cannot specify `SystemDisk.Category` at the same time.
        self.system_disk_categories = system_disk_categories
        # The tags of the ECS instance. Tags are specified as key-value pairs. You can specify up to 20 tags. The following limits apply to Key and Value: 
        #          
        # - Key can be up to 64 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. Key cannot be an empty string. 
        # - Value can be up to 128 characters in length and cannot start with `aliyun` or `acs:`. It cannot contain `http://` or `https://`. Value can be an empty string.
        self.tags = tags
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # 
        # - default: creates an instance that is not on a dedicated host.
        # 
        # - host: creates an instance on a dedicated host. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a dedicated host for the instance.
        self.tenancy = tenancy
        # The user data of the ECS instance. The data must be encoded in Base64. The maximum size of the raw data before encoding is 32 KB.
        self.user_data = user_data
        # The zone ID of the ECS instance.
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

        if self.override is not None:
            result['Override'] = self.override

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

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options

        if self.secondary_eni_vswitch_constraint is not None:
            result['SecondaryEniVSwitchConstraint'] = self.secondary_eni_vswitch_constraint

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
            temp_model = main_models.ModifyScalingConfigurationRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.ModifyScalingConfigurationRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.ModifyScalingConfigurationRequestSystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.custom_priorities = []
        if m.get('CustomPriorities') is not None:
            for k1 in m.get('CustomPriorities'):
                temp_model = main_models.ModifyScalingConfigurationRequestCustomPriorities()
                self.custom_priorities.append(temp_model.from_map(k1))

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.ModifyScalingConfigurationRequestDataDisks()
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
                temp_model = main_models.ModifyScalingConfigurationRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k1))

        if m.get('InstanceTypeCandidateOptions') is not None:
            temp_model = main_models.ModifyScalingConfigurationRequestInstanceTypeCandidateOptions()
            self.instance_type_candidate_options = temp_model.from_map(m.get('InstanceTypeCandidateOptions'))

        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k1 in m.get('InstanceTypeOverrides'):
                temp_model = main_models.ModifyScalingConfigurationRequestInstanceTypeOverrides()
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
                temp_model = main_models.ModifyScalingConfigurationRequestNetworkInterfaces()
                self.network_interfaces.append(temp_model.from_map(k1))

        if m.get('Override') is not None:
            self.override = m.get('Override')

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
            temp_model = main_models.ModifyScalingConfigurationRequestResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('ResourcePoolOptions'))

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        if m.get('SchedulerOptions') is not None:
            self.scheduler_options = m.get('SchedulerOptions')

        if m.get('SecondaryEniVSwitchConstraint') is not None:
            self.secondary_eni_vswitch_constraint = m.get('SecondaryEniVSwitchConstraint')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.ModifyScalingConfigurationRequestSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k1 in m.get('SpotPriceLimits'):
                temp_model = main_models.ModifyScalingConfigurationRequestSpotPriceLimits()
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

class ModifyScalingConfigurationRequestSpotPriceLimits(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        # The instance type of the spot instance. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit.
        self.instance_type = instance_type
        # The bid price for the spot instance. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit.
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

class ModifyScalingConfigurationRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        confidential_computing_mode: str = None,
    ):
        # The confidential computing mode. Valid values:
        # - Enclave: The ECS instance uses Enclave to build a confidential computing environment. For more information, see [Build a confidential computing environment by using Enclave](https://help.aliyun.com/document_detail/203433.html).
        # - TDX: builds a TDX confidential computing environment. For more information, see [Build a TDX confidential computing environment](https://help.aliyun.com/document_detail/479090.html).
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

class ModifyScalingConfigurationRequestResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        private_pool_tags: List[main_models.ModifyScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags] = None,
        strategy: str = None,
    ):
        # The private pool IDs, which are the elasticity assurance IDs or capacity reservation IDs. Only Target-type private pool IDs can be specified for this parameter. This parameter cannot be specified together with the PrivatePoolTags parameter.
        self.private_pool_ids = private_pool_ids
        # Filters available Target private pools by tags. Valid values of N: 1 to 20.
        # Note:
        # - When this parameter is specified, the system filters only the Target private pools associated with the account that match the tags and satisfy the scaling group constraints (such as zone and instance type).
        # - Tag matching rule: A private pool must match all specified tags.
        # - This parameter cannot be specified together with the PrivatePoolIds parameter.
        self.private_pool_tags = private_pool_tags
        # Resource pools include private pools generated after elasticity assurance or capacity reservation takes effect, and public pools, which are available for instance startup. Valid values:
        # 
        # - PrivatePoolFirst: private pool first. When this strategy is selected, if ResourcePoolOptions.PrivatePoolIds is specified or PrivatePoolTags conditions are met, the corresponding private pools are used first. If no private pool is specified or the specified private pool has insufficient capacity, open-type private pools are automatically matched. If no eligible private pool is available, the public pool is used to create instances.
        # 
        # - PrivatePoolOnly: private pool only. When this strategy is selected, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pool has insufficient capacity, the instance fails to start.
        # 
        # - PublicPoolFirst: public pool first. The public pool is used first to create instances. When public pool resources are insufficient, private pool resources are used as a supplement. Open-type private pools are automatically matched first. If no eligible private pool is available, the Target-type private pools specified by ResourcePoolOptions.PrivatePoolIds or matching PrivatePoolTags conditions are used. (This strategy is in invitational preview and is not available for use.)
        # 
        # - None: does not use a resource pool strategy.
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
                temp_model = main_models.ModifyScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags()
                self.private_pool_tags.append(temp_model.from_map(k1))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class ModifyScalingConfigurationRequestResourcePoolOptionsPrivatePoolTags(DaraModel):
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

class ModifyScalingConfigurationRequestNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        secondary_private_ip_address_count: int = None,
        security_group_ids: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        # The type of the elastic network interfaces (ENIs). When you use this parameter, you must use NetworkInterfaces to set the primary network interface controller (NIC). You cannot set SecurityGroupId or SecurityGroupIds at the same time. Valid values:
        # 
        # - Primary: primary network interface controller (NIC).
        # - Secondary: secondary network interface controller (NIC).
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses for the primary ENI. Note the following items:
        # 
        # This parameter takes effect only when NetworkInterface.InstanceType is set to Primary. If NetworkInterface.InstanceType is set to Secondary or left empty, you cannot specify this parameter.
        # 
        # After you specify this parameter, you cannot specify Ipv6AddressCount.
        self.ipv_6address_count = ipv_6address_count
        # The communication mode of the network interface controller (NIC). Valid values:
        # 
        # - Standard: uses the TCP communication mode.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication mode.
        # 
        # Default value: Standard.
        # 
        # > The number of elastic network interfaces (ENIs) in RDMA mode cannot exceed the limit of the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of secondary private IPv4 addresses to assign to the ENI. Valid values: 1 to 49.
        # 
        # - The value cannot exceed the limit on the number of IP addresses for the instance type. For more information, see [Instance families](https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families).
        # 
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount specifies the number of secondary private IPv4 addresses to assign to the ENI (excluding the primary private IP address of the ENI). The system randomly assigns IP addresses from the available CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the ENI belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The IDs of one or more security groups to which the elastic network interfaces (ENIs) belongs.
        self.security_group_ids = security_group_ids
        # The IDs of the vSwitches to which the elastic network interfaces (ENIs) belongs. N specifies that you can set multiple vSwitches. Valid values of N: 1 to 10.
        # 
        # Note the following items:
        # 
        # - If InstanceType is set to Primary, you cannot set this parameter. The default value is the vSwitch of the instance.
        # - If InstanceType is set to Secondary or left empty, this parameter is optional.
        # - The system selects a vSwitch that is in the same zone as the primary network interface controller (NIC) and has the most available IP addresses.
        self.v_switch_ids = v_switch_ids

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

        if self.v_switch_ids is not None:
            result['VSwitchIds'] = self.v_switch_ids

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

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids = m.get('VSwitchIds')

        return self

class ModifyScalingConfigurationRequestInstanceTypeOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        # To specify the capacity of an instance type in the scaling configuration, specify both this parameter and InstanceTypeOverride.WeightedCapacity.
        # 
        # This parameter specifies the instance type. You can specify multiple instance types and use the InstanceTypeOverride.WeightedCapacity parameter to extend multi-instance-type support with custom weights.
        # 
        # > You cannot specify this parameter together with instanceTypes.
        # 
        # Valid values of InstanceType: ECS instance types that are available for purchase.
        self.instance_type = instance_type
        # To scale the scaling group based on instance type capacity, specify this parameter after specifying LaunchTemplateOverride.InstanceType.
        # 
        # This parameter specifies the weight of the instance type, which represents the capacity of a single instance of this type in the scaling group. A larger weight means fewer instances of this type are required to meet the expected capacity.
        # 
        # Because instance types differ in vCPUs, memory, and other performance metrics, you can assign different weights to different instance types based on your requirements.
        # 
        # Example:
        # 
        # - Current capacity: 0.
        # - Expected number of instances: 6.
        # - Capacity of ecs.c5.xlarge: 4.
        # 
        # To meet the expected capacity, the scaling group scales out 2 ecs.c5.xlarge instances.
        # 
        # > During scale-out, the capacity of the scaling group cannot exceed the sum of the maximum capacity (MaxSize) and the maximum weight of the instance types.
        # 
        # Valid values of WeightedCapacity: 1 to 500.
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

class ModifyScalingConfigurationRequestInstanceTypeCandidateOptions(DaraModel):
    def __init__(
        self,
        allow_cidr_blocks: List[str] = None,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        enabled: bool = None,
        max_price: float = None,
    ):
        # The CIDR blocks for optional vSwitches when supplementing vSwitches in other zones.
        self.allow_cidr_blocks = allow_cidr_blocks
        # Specifies whether to allow supplementing vSwitches in other zones.
        # > The instance type remains unchanged. Only alternative zones are selected. When all selected zones of the scaling group cannot be used for scale-out due to issues such as insufficient inventory, new zone vSwitches are automatically added to the scaling group based on this configuration.
        # > For example, if the scaling group is configured with the cn-hangzhou-h and cn-hangzhou-g zones, and neither zone can be used for scale-out, Auto Scaling may create a vSwitch in cn-hangzhou-k based on real-time inventory and add it to the scaling group.
        self.allow_cross_az = allow_cross_az
        # Specifies whether to allow supplementing instance types from other generations.
        # 
        # - For example, if the current instance type is ecs.c7.large, enabling this option allows fallback to instance types such as ecs.c6.large and ecs.c8.large.
        self.allow_different_generation = allow_different_generation
        # Specifies whether to enable the fallback mode.
        self.enabled = enabled
        # The maximum price for fallback instance types.
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

class ModifyScalingConfigurationRequestInstancePatternInfos(DaraModel):
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
        # The architecture types of the instance type. Valid values:
        # 
        # - X86: x86 computing.
        # - Heterogeneous: heterogeneous computing, such as GPU or FPGA.
        # - BareMental: ECS Bare Metal Instance.
        # - Arm: Arm computing.
        # 
        # Default value: all architecture types are included.
        self.architectures = architectures
        # Specifies whether to include burstable instance types. Valid values:
        # - Exclude: excludes burstable instance types.
        # - Include: includes burstable instance types.
        # - Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The number of vCPU cores of the instance type in intelligent configuration mode, used to filter instance types that meet the requirements. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # Note the following information:
        # 
        # - The InstancePatternInfo parameter applies only to scaling groups whose network type is VPC.
        # 
        # - You must specify both InstancePatternInfo.Cores and InstancePatternInfo.Memory.
        # 
        # - If you have specified instance types by using the InstanceType or InstanceTypes parameter, Auto Scaling preferentially uses the specified instance types for scale-out. When the specified instance types are out of stock, Auto Scaling selects the lowest-priced instance type from those that match the InstancePatternInfo parameter values.
        self.cores = cores
        # The CPU architectures of the instance. Valid values:
        # 
        # > N indicates that you can specify multiple CPU architectures. Valid values of N: 1 to 2.
        # 
        # - X86.
        # - ARM.
        self.cpu_architectures = cpu_architectures
        # The instance types to exclude. You can use wildcard characters (*) to exclude a single instance type or an entire instance family. Examples:
        # 
        # - ecs.c6.large: excludes the ecs.c6.large instance type.
        # - ecs.c6.*: excludes the entire c6 instance family.
        self.excluded_instance_types = excluded_instance_types
        # The GPU types.
        self.gpu_specs = gpu_specs
        # The categorization of the instance type. Valid values:
        # - General-purpose: general-purpose.
        # - Compute-optimized: compute-optimized.
        # - Memory-optimized: memory-optimized.
        # - Big data: big data.
        # - Local SSDs: local SSD.
        # - High Clock Speed: high frequency.
        # - Enhanced: enhanced.
        # - Shared: shared.
        # - Compute-optimized with GPU: GPU-accelerated compute-optimized.
        # - Visual Compute-optimized: visual compute-optimized.
        # - Heterogeneous Service: heterogeneous service.
        # - Compute-optimized with FPGA: FPGA compute-optimized.
        # - Compute-optimized with NPU: NPU compute-optimized.
        # - ECS Bare Metal: ECS Bare Metal Instance.
        # - High Performance Compute: high-performance computing (HPC).
        self.instance_categories = instance_categories
        # The level of the instance family, used to filter instance types that meet the requirements. This parameter takes effect when `CostOptimization` is enabled. Valid values:
        # 
        # - EntryLevel: entry level, which refers to shared instance types. These instance types are more cost-effective but cannot guarantee stable computing performance. They are suitable for scenarios with low CPU utilization. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # - EnterpriseLevel: enterprise level. These instance types provide stable performance and dedicated resources. They are suitable for scenarios that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # - CreditEntryLevel: credit entry level, which refers to burstable instances. These instance types use CPU credits to ensure computing performance. They are suitable for scenarios with low average CPU utilization and occasional bursts. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families to query. N indicates that you can specify multiple instance families. Valid values of N: 1 to 10.
        self.instance_type_families = instance_type_families
        # The maximum hourly price for pay-as-you-go or spot instances in intelligent configuration mode, used to filter instance types that meet the requirements.
        # 
        # > This parameter is required when SpotStrategy is set to SpotWithPriceLimit. In other cases, this parameter is optional.
        self.max_price = max_price
        # The maximum number of vCPU cores of the instance type.
        # 
        # > MaximumCpuCoreCount cannot exceed 4 times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs of the instance. Valid values: positive integers.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size of the instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size of the instance type in intelligent configuration mode. Unit: GiB. This parameter is used to filter instance types that meet the requirements.
        self.memory = memory
        # The minimum baseline vCPU computing performance (sum of all vCPUs) for burstable instances (t5 and t6).
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPU cores of the instance.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum upper limit of IPv6 addresses on a single elastic network interfaces (ENIs) of the instance.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of IPv4 addresses per ENI supported by the instance.
        # [_single.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) supported by the instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs of the instance. Valid values: positive integers.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The minimum initial vCPU credits for burstable instances (t5 and t6).
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size of the instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor models of the instance. N indicates that you can specify multiple processor models. Valid values of N: 1 to 10.
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

class ModifyScalingConfigurationRequestDataDisks(DaraModel):
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
        # The ID of the automatic snapshot policy applied to the data cloud disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the burst feature for the data cloud disk. Valid values:
        # 
        # - true: enables the burst feature.
        # - false: does not enable the burst feature.
        # > This parameter is supported only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The multiple disk types of the data cloud disk. Valid values:
        # - cloud: basic cloud disk. The DeleteWithInstance property of a basic cloud disk created along with the instance is set to true.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_auto: ESSD AutoPL.
        # - cloud_regional_disk_auto: regional ESSD.
        # 
        # > You cannot specify this parameter together with `DataDisk.Category`.
        self.categories = categories
        # The category of the data cloud disk. Valid values:
        # - cloud: basic cloud disk. The DeleteWithInstance attribute of a basic cloud disk created along with the instance is set to true.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_auto: ESSD AutoPL.
        # - cloud_regional_disk_auto: regional ESSD.
        # 
        # This parameter cannot be specified together with `DataDisk.Categories`. If neither this parameter nor `DataDisk.Categories` is specified, the default value is used:
        # 
        # - For I/O optimized instances, the default value is cloud_efficiency.
        # 
        # - For non-I/O optimized instances, the default value is cloud.
        self.category = category
        # Specifies whether the data cloud disk is released when the instance is released. Valid values:
        # 
        # - true: The data cloud disk is released when the instance is released.
        # - false: The data cloud disk is retained when the instance is released.
        # 
        # This parameter can be set only for independent cloud disks (DataDisk.Category is set to cloud, cloud_efficiency, cloud_ssd, cloud_essd, or cloud_auto). Otherwise, an error is returned.
        self.delete_with_instance = delete_with_instance
        # The description of the system cloud disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data cloud disk. If you do not specify this parameter, the system uses the default behavior to allocate a mount point during automatic creation of the ECS instance. The mount points range from /dev/xvdb to /dev/xvdz.
        self.device = device
        # The name of the data cloud disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter or Chinese character and cannot start with `http://` or `https://`.
        self.disk_name = disk_name
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - true: encrypts the data cloud disk.
        # - false: does not encrypt the data cloud disk.
        self.encrypted = encrypted
        # The ID of the KMS key for the data cloud disk.
        self.kmskey_id = kmskey_id
        # The performance level of the data cloud disk when the disk is an ESSD. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > For more information about how to select an ESSD performance level, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics of the data cloud disk.
        # 
        # > IOPS (Input/Output Operations Per Second) measures the number of read and write operations that a block storage device can process per second.
        self.provisioned_iops = provisioned_iops
        # The size of the data cloud disk. Unit: GiB. Valid values:
        # 
        # - cloud: 5 to 2000.
        # - cloud_efficiency: 20 to 32768.
        # - cloud_ssd: 20 to 32768.
        # - cloud_essd: 20 to 32768.
        # - ephemeral_ssd: 5 to 800.
        # 
        # After you specify this parameter, the disk size must be greater than or equal to the size of the snapshot specified by SnapshotId.
        self.size = size
        # The ID of the snapshot used to create the data cloud disk. After this parameter is specified, DataDisk.Size is ignored, and the size of the created disk is the size of the specified snapshot.
        # 
        # If the snapshot was created on or before July 15, 2013, the request is rejected and the error message InvalidSnapshot.TooOld is returned.
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

class ModifyScalingConfigurationRequestCustomPriorities(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        vswitch_id: str = None,
    ):
        # The instance type of the ECS instance.
        # 
        # > The instance type must be included in the instance type list of the scaling configuration.
        self.instance_type = instance_type
        # The ID of the vSwitch.
        # 
        # > The vSwitch must be included in the vSwitch list of the scaling group.
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

class ModifyScalingConfigurationRequestSystemDisk(DaraModel):
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
        # The ID of the automatic snapshot policy applied to the system cloud disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the burst feature for the system cloud disk. Valid values:
        # 
        # - true: enables the burst feature.
        # - false: does not enable the burst feature.
        # > This parameter is supported only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">For more information, see [ESSD AutoPL disks](
        # [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html)
        self.bursting_enabled = bursting_enabled
        # The category of the system cloud disk. Valid values:
        # 
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: Enterprise SSD (ESSD).
        # - ephemeral_ssd: local SSD.
        # 
        # This parameter cannot be specified together with `SystemDiskCategories`. If neither this parameter nor `SystemDiskCategories` is specified, a default value is used. If the instance type belongs to Generation I instance families and the instance is not an I/O optimization instance, the default value is cloud. Otherwise, the default value is cloud_efficiency.
        self.category = category
        # The description of the system cloud disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system cloud disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter or Chinese character and cannot start with http:// or https://. Default value: empty.
        self.disk_name = disk_name
        # The encryption algorithm for the system cloud disk. Valid values:
        # 
        # - AES-256.
        # - SM4-128.
        # 
        # Default value: AES-256.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system cloud disk. Valid values:
        # 
        # - true: encrypts the system cloud disk.
        # - false: does not encrypt the system cloud disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the KMS key used for the system cloud disk.
        self.kmskey_id = kmskey_id
        # The performance level (PL) of the system cloud disk when the disk is an ESSD. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > For more information about how to select an ESSD performance level, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics for the system cloud disk.
        # 
        # > IOPS (Input/Output Operations Per Second) refers to the number of I/O operations that can be processed per second, representing the read/write (output/input) capability of block storage. Unit: operations per second.
        self.provisioned_iops = provisioned_iops
        # The size of the system cloud disk. Unit: GiB. Valid values:
        # 
        # - Basic cloud disk: 20 to 500.
        # - ESSD:
        #   - PL0: 1 to 2048.
        #   - PL1: 20 to 2048.
        #   - PL2: 461 to 2048.
        #   - PL3: 1261 to 2048.
        # - ESSD AutoPL: 1 to 2048.
        # - Other cloud disk types: 20 to 2048.
        # 
        # The value of this parameter must be greater than or equal to max{1, ImageSize}.
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

class ModifyScalingConfigurationRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The private pool ID, which is the ID of the elasticity assurance or capacity reservation.
        self.id = id
        # The private pool option for instance startup. A private pool is generated after an elasticity assurance or capacity reservation takes effect. You can select a private pool when you start an instance. Valid values:
        # 
        # - Open: open mode. The system automatically matches an open private pool. If no matching private pool is available, the public pool is used to start the instance. You do not need to specify PrivatePoolOptions.Id in this mode.
        # 
        # - Target: specified mode. A specified private pool is used to start the instance. If the specified private pool is unavailable, the instance fails to start. In this mode, you must specify the private pool ID, which means PrivatePoolOptions.Id is required.
        # 
        # - None: no private pool is used. The instance does not use any private pool capacity for startup.
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

class ModifyScalingConfigurationRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether the ECS instance uses the ecs-user account to log on. For more information, see [Manage the logon name of an ECS instance](https://help.aliyun.com/document_detail/388447.html). Valid values:
        # 
        # - true: The ecs-user account is used.
        # 
        # - false: The ecs-user account is not used.
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

