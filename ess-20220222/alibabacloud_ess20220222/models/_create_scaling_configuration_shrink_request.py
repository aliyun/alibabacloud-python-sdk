# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class CreateScalingConfigurationShrinkRequest(DaraModel):
    def __init__(
        self,
        image_options: main_models.CreateScalingConfigurationShrinkRequestImageOptions = None,
        private_pool_options: main_models.CreateScalingConfigurationShrinkRequestPrivatePoolOptions = None,
        system_disk: main_models.CreateScalingConfigurationShrinkRequestSystemDisk = None,
        affinity: str = None,
        client_token: str = None,
        cpu: int = None,
        credit_specification: str = None,
        custom_priorities: List[main_models.CreateScalingConfigurationShrinkRequestCustomPriorities] = None,
        data_disks: List[main_models.CreateScalingConfigurationShrinkRequestDataDisks] = None,
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
        instance_pattern_infos: List[main_models.CreateScalingConfigurationShrinkRequestInstancePatternInfos] = None,
        instance_type: str = None,
        instance_type_candidate_options: main_models.CreateScalingConfigurationShrinkRequestInstanceTypeCandidateOptions = None,
        instance_type_overrides: List[main_models.CreateScalingConfigurationShrinkRequestInstanceTypeOverrides] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        network_interfaces: List[main_models.CreateScalingConfigurationShrinkRequestNetworkInterfaces] = None,
        owner_account: str = None,
        owner_id: int = None,
        password: str = None,
        password_inherit: bool = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        resource_pool_options: main_models.CreateScalingConfigurationShrinkRequestResourcePoolOptions = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options_shrink: str = None,
        secondary_eni_vswitch_constraint: str = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_options: main_models.CreateScalingConfigurationShrinkRequestSecurityOptions = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[main_models.CreateScalingConfigurationShrinkRequestSpotPriceLimits] = None,
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
        # Specifies whether to associate the instance on a dedicated host with the dedicated host. Valid values:
        # 
        # - default: The instance is not associated with the dedicated host. If an instance with the economical mode enabled is stopped and then started, and the resources of the original dedicated host are insufficient, the instance is automatically deployed to another dedicated host in the automatic deployment resource pool.
        # 
        # - host: The instance is associated with the dedicated host. If an instance with the economical mode enabled is stopped and then started, it remains on the original dedicated host. If the resources of the original dedicated host are insufficient, the instance fails to start.
        # 
        # Default value: default.
        self.affinity = affinity
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length. For more information, see [Ensure idempotence](https://help.aliyun.com/document_detail/25693.html).
        self.client_token = client_token
        # The number of vCPUs. Unit: cores.
        # 
        # You can specify both Cpu and Memory to define the range of instance types. For example, if you set Cpu to 2 and Memory to 16, all instance types with 2 vCPUs and 16 GiB of memory are matched. Auto Scaling determines the available instance types based on factors such as I/O optimization and zone, and creates instances with the lowest price.
        # > This configuration takes effect only when the scaling mode is set to cost optimization and no instance type is specified in the scaling configuration.
        self.cpu = cpu
        # Specifies the running pattern of the burstable instance. Valid values:
        # 
        # - Standard: standard pattern.
        # 
        # - Unlimited: unlimited pattern.
        # 
        # For more information, see the performance schema section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The custom priority of the ECS instance type and vSwitch combination.
        # >Notice: This parameter takes effect only when the scaling policy of the scaling group is set to the priority-based policy.
        # 
        # If an instance cannot be created based on the instance type and vSwitch combination with a higher priority, Auto Scaling automatically selects the combination with the next highest priority to create the instance.
        # 
        # > If you specify custom priorities for only some instance type and vSwitch combinations, the unspecified combinations have lower priorities than the specified ones. The priorities of the unspecified combinations are determined based on the vSwitch sequence in the scaling group and the instance type sequence in the scaling configuration.
        # > - Example: If the vSwitch sequence in the scaling group is vsw1 and vsw2, the instance type sequence in the scaling configuration is type1 and type2, and the custom priority sequence is ["vsw2+type2", "vsw1+type2"], the final priority sequence is: "vsw2+type2" > "vsw1+type2" > "vsw1+type1" > "vsw2+type1".
        self.custom_priorities = custom_priorities
        # The collection of data cloud disk information.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # Specifies whether to create the ECS instance on a dedicated host. Because dedicated hosts do not support spot instances, the SpotStrategy and SpotPriceLimit parameters are automatically ignored if DedicatedHostId is specified.
        # 
        # You can call the DescribeDedicatedHosts operation to query the list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The release protection property of the instance. This property specifies whether the instance can be directly released by using the ECS console or the DeleteInstance API operation, which prevents accidental deletion of the instance. Valid values:
        # 
        # - true: enables release protection for the instance. The instance cannot be directly released by using the ECS console or the DeleteInstance API operation.
        # 
        # - false: shutdown release protection for the instance. The instance can be directly released by using the ECS console or the DeleteInstance API operation.
        # 
        # Default value: false.
        # > This property applies only to pay-as-you-go instances to prevent instances created by Auto Scaling during scale-out from being accidentally deleted. It does not affect normal scale-in activities. Instances with release protection enabled can still be released during scale-in activities.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the ECS instance belongs.
        self.deployment_set_id = deployment_set_id
        # The hostname of the ECS instance. The hostname cannot start or end with a period (.) or a hyphen (-) and cannot contain consecutive periods (.) or hyphens (-). The naming requirements for different instance types are as follows:
        # 
        # - Windows instances: The hostname must be 2 to 15 characters in length and can contain letters, digits, and hyphens (-). It cannot contain periods (.) or contain only digits.
        # - Other instance types such as Linux instances: The hostname must be 2 to 64 characters in length and can contain multiple periods (.). The string between two periods is a segment, which can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the HPC cluster to which the ECS instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # - enabled: enables the access channel.
        # - disabled: disables the access channel.
        # 
        # Default value: enabled.
        # 
        # > For more information about instance metadata, see [Overview of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # Specifies whether to forcibly use the security-hardened mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # - optional: does not forcibly use the security-hardened mode.
        # - required: forcibly uses the security-hardened mode. After you set this value, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # 
        # > For more information about the modes for accessing instance metadata, see [Access modes of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image in the image family to create instances. If `ImageId` is specified, you cannot specify this parameter.
        self.image_family = image_family
        # The ID of the image file. The image resource used during automatic creation of instances.
        self.image_id = image_id
        # The name of the image file. The image name must be unique within a region. If ImageId is specified, ImageName is ignored.
        # 
        # 
        # You cannot use ImageName to specify an Alibaba Cloud Marketplace image.
        self.image_name = image_name
        # The description of the ECS instance. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.instance_description = instance_description
        # The name of the ECS instance during automatic creation by using this scaling configuration.
        self.instance_name = instance_name
        # The collection of intelligent configuration information used to filter instance types that meet your requirements.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance type of the ECS instance. For more information, see instance families.
        self.instance_type = instance_type
        # After you enable the candidate mode, if issues such as insufficient stock occur, the system supplements the currently selected instance types with similar instance types of the same size, or creates vSwitches in candidate zones and adds them to the scaling group.
        self.instance_type_candidate_options = instance_type_candidate_options
        # The information used to specify instance types.
        self.instance_type_overrides = instance_type_overrides
        # The multiple instance types. If InstanceTypes is specified, InstanceType is ignored.
        # 
        # If an instance cannot be created based on the instance type with a higher priority, Auto Scaling automatically selects the instance type with the next highest priority to create the instance.
        self.instance_types = instance_types
        # The network billing method. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth. In this case, InternetMaxBandwidthOut specifies the fixed bandwidth value.
        # 
        # - PayByTraffic: pay-by-traffic. In this case, InternetMaxBandwidthOut specifies only the maximum bandwidth, and you are billed based on the actual network traffic.
        # 
        # If this parameter is not specified, the default value is PayByBandwidth for the classic network and PayByTraffic for a VPC.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # - If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s: 1 to 10. Default value: 10.
        # - If the purchased outbound public bandwidth is greater than 10 Mbit/s: 1 to the value of `InternetMaxBandwidthOut`. Default value: the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimization instance. Valid values:
        # 
        # - none: The instance is not an I/O optimization instance.
        # - optimized: The instance is an I/O optimization instance.
        # 
        # The default value is none for retired instance types and optimized for other instance types.
        self.io_optimized = io_optimized
        # The number of IPv6 addresses that are randomly generated for the network interface controller (NIC).
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair used to log on to the ECS instance. 
        #          
        # - For Windows instances, this parameter is ignored and left empty by default. 
        # - For Linux instances, password-based logon is disabled by default.
        self.key_pair_name = key_pair_name
        # The weight of the ECS instance as a load balancing backend server. Valid values: 1 to 100.
        # 
        # Default value: 50.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # 
        # You can specify both Cpu and Memory to define the range of instance types. For example, if you set Cpu to 2 and Memory to 16, all instance types with 2 vCPUs and 16 GiB of memory are matched. Auto Scaling determines the available instance types based on factors such as I/O optimization and zone, and creates instances with the lowest price.
        # 
        # > This configuration takes effect only when the scaling mode is set to cost optimization and no instance type is specified in the scaling configuration.
        self.memory = memory
        # The list of network interface controller (NIC) devices.
        self.network_interfaces = network_interfaces
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the ECS instance. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Special characters include:
        # 
        # \\`()` ~!@#$%^&*-_+=\\|{}[]:;\\"<>,.?/`
        # 
        # For Windows instances, the password cannot start with a forward slash (/).
        # 
        # > If you specify the Password parameter, send requests over HTTPS to prevent password leaks.
        self.password = password
        # Specifies whether to use the preset password of the image. When you use this parameter, make sure that a password is preset in the image. Valid values:
        # 
        # - true: uses the preset password of the image.
        # - false: does not use the preset password of the image.
        self.password_inherit = password_inherit
        # The name of the Resource Access Management (RAM) role for the ECS instance. RAM roles are provided and maintained by RAM. You can call the ListRoles operation to query available RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instance belongs.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The resource pool policy used when creating the instance. Take note of the following items when you configure this parameter:
        # 
        # - This parameter takes effect only when you create pay-as-you-go instances.
        # 
        # - You cannot configure this parameter together with PrivatePoolOptions.MatchCriteria or PrivatePoolOptions.Id.
        self.resource_pool_options = resource_pool_options
        # The name of the scaling configuration. The name must be 2 to 64 characters in length and can contain letters, digits, underscores (_), hyphens (-), and periods (.). It must start with a letter, digit, or Chinese character.
        # 
        # The name must be unique within a scaling group in a region. If you do not specify this parameter, the ID of the scaling configuration is used by default.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        # 
        # This parameter is required.
        self.scaling_group_id = scaling_group_id
        # The scheduling options.
        self.scheduler_options_shrink = scheduler_options_shrink
        # Specifies whether a vSwitch available for secondary elastic network interfaces (ENIs) must be selected from the list when the VSwitchIds parameter is specified for the secondary ENIs. Valid values:
        # - Strict: strict mode. If no vSwitch in the VSwitchIds list meets the requirements, instance creation fails.
        # - Tolerant: fault-tolerant mode. If no vSwitch in the VSwitchIds list meets the requirements, no secondary ENI is configured, and the instance is still created.
        # 
        # Default value: Strict.
        self.secondary_eni_vswitch_constraint = secondary_eni_vswitch_constraint
        # Specifies whether to enable security hardening. Valid values:
        # 
        # - Active: enables security hardening. This value applies only to public images.
        # - Deactive: disables security hardening. This value applies to all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the ECS instance belongs. ECS instances in the same security group can access each other.
        self.security_group_id = security_group_id
        # Adds the ECS instance to multiple security groups at the same time. For more information, see the Security groups section in [Limits](https://help.aliyun.com/document_detail/25412.html).
        # 
        # > You cannot specify both SecurityGroupId and SecurityGroupIds at the same time.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours. Valid values:
        # 
        # - 1: Alibaba Cloud guarantees that the instance runs for 1 hour after it is created and is not automatically released. After 1 hour, the system automatically compares your bid with the market price and checks resource inventory to determine whether to retain automatic release the instance.
        # - 0: Alibaba Cloud does not guarantee that the instance runs for 1 hour after it is created. The system automatically compares your bid with the market price and checks resource inventory to determine whether to retain automatic release the instance.
        # 
        # > Alibaba Cloud sends you a notification by using ECS system events 5 minutes before the instance is released. Spot instances are billed by the second. Select an appropriate protection period based on the execution duration of your tasks.
        # 
        # Default value: 1.
        self.spot_duration = spot_duration
        # The break mode of the spot instance. Currently, only terminate (default) is supported, which releases the instance directly.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The collection of billing information for spot instances.
        self.spot_price_limits = spot_price_limits
        # The preemption policy for the pay-as-you-go instance. Valid values:
        #          
        # - NoSpot: regular pay-as-you-go instance.
        # - SpotWithPriceLimit: spot instance with a maximum hourly price.
        # - SpotAsPriceGo: spot instance whose price is automatically set based on the current market price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. Valid values: integers greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The disk types for the system cloud disk. If a disk type with a higher priority is unavailable, Auto Scaling automatically attempts to use the disk type with the next highest priority to create the system cloud disk. Valid values:
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD cloud disk.
        # - cloud_essd: ESSD cloud disk.
        # 
        # > You cannot specify both this parameter and `SystemDisk.Category` at the same time.
        self.system_disk_categories = system_disk_categories
        # The tags of the ECS instance. Tags are passed in as key-value pairs. You can add up to 20 tags. The requirements for keys and values are as follows:
        #          
        # - A key can be up to 64 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`. A key cannot be an empty string.
        # - A value can be up to 128 characters in length. It cannot start with aliyun or acs: and cannot contain `http://` or `https://`. A value can be an empty string.
        self.tags = tags
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # 
        # - default: creates the instance on a non-dedicated host.
        # 
        # - host: creates the instance on a dedicated host. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a dedicated host for the instance.
        # 
        # Default value: default.
        self.tenancy = tenancy
        # The user data of the ECS instance. It must be encoded in Base64. The maximum size of the raw data before encoding is 32 KB.
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

        if self.scheduler_options_shrink is not None:
            result['SchedulerOptions'] = self.scheduler_options_shrink

        if self.secondary_eni_vswitch_constraint is not None:
            result['SecondaryEniVSwitchConstraint'] = self.secondary_eni_vswitch_constraint

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
            temp_model = main_models.CreateScalingConfigurationShrinkRequestImageOptions()
            self.image_options = temp_model.from_map(m.get('ImageOptions'))

        if m.get('PrivatePoolOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationShrinkRequestPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('PrivatePoolOptions'))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.CreateScalingConfigurationShrinkRequestSystemDisk()
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
                temp_model = main_models.CreateScalingConfigurationShrinkRequestCustomPriorities()
                self.custom_priorities.append(temp_model.from_map(k1))

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.CreateScalingConfigurationShrinkRequestDataDisks()
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
                temp_model = main_models.CreateScalingConfigurationShrinkRequestInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeCandidateOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationShrinkRequestInstanceTypeCandidateOptions()
            self.instance_type_candidate_options = temp_model.from_map(m.get('InstanceTypeCandidateOptions'))

        self.instance_type_overrides = []
        if m.get('InstanceTypeOverrides') is not None:
            for k1 in m.get('InstanceTypeOverrides'):
                temp_model = main_models.CreateScalingConfigurationShrinkRequestInstanceTypeOverrides()
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
                temp_model = main_models.CreateScalingConfigurationShrinkRequestNetworkInterfaces()
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
            temp_model = main_models.CreateScalingConfigurationShrinkRequestResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('ResourcePoolOptions'))

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SchedulerOptions') is not None:
            self.scheduler_options_shrink = m.get('SchedulerOptions')

        if m.get('SecondaryEniVSwitchConstraint') is not None:
            self.secondary_eni_vswitch_constraint = m.get('SecondaryEniVSwitchConstraint')

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.CreateScalingConfigurationShrinkRequestSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k1 in m.get('SpotPriceLimits'):
                temp_model = main_models.CreateScalingConfigurationShrinkRequestSpotPriceLimits()
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

class CreateScalingConfigurationShrinkRequestSpotPriceLimits(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        # The instance type of the spot instance. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit.
        self.instance_type = instance_type
        # The maximum hourly price for the spot instance. This parameter takes effect only when SpotStrategy is set to SpotWithPriceLimit.
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

class CreateScalingConfigurationShrinkRequestSecurityOptions(DaraModel):
    def __init__(
        self,
        confidential_computing_mode: str = None,
    ):
        # The confidential computing mode. Valid values:
        # -  Enclave: The ECS instance uses Enclave to build a confidential computing environment. For more information, see [Build a confidential computing environment by using Enclave](https://help.aliyun.com/document_detail/203433.html).
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

class CreateScalingConfigurationShrinkRequestResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        private_pool_tags: List[main_models.CreateScalingConfigurationShrinkRequestResourcePoolOptionsPrivatePoolTags] = None,
        strategy: str = None,
    ):
        # The ID of the private pool, which is the ID of the elasticity assurance or capacity reservation service. You can only specify the ID of a private pool in Target mode, and you cannot specify this parameter together with PrivatePoolTags.
        self.private_pool_ids = private_pool_ids
        # Filters available Target private pools by tag. Valid values of N: 1 to 20.
        # Note:
        # - When you configure this parameter, the system filters private pools from the Target private pools associated with your account. The filtered private pools must match the tags and meet the scaling group constraints, such as zone and instance type.
        # - Tag matching rule: The private pool must match all specified tags.
        # - You cannot specify this parameter together with PrivatePoolIds.
        self.private_pool_tags = private_pool_tags
        # Resource pools include private pools generated after the elasticity assurance or capacity reservation service takes effect, as well as public pools. They are available for selection when the instance starts. Valid values:
        # 
        # - PrivatePoolFirst: private pools take precedence. When you select this policy, if ResourcePoolOptions.PrivatePoolIds is specified or the PrivatePoolTags condition is met, the corresponding private pool is preferentially used. If no private pool is specified or the specified private pool has insufficient capacity, the system automatically matches an open private pool. If no eligible private pool is available, the public pool is used to create the instance.
        # 
        # - PrivatePoolOnly: only private pools are used. When you select this policy, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pool has insufficient capacity, the instance fails to start.
        # 
        # - PublicPoolFirst: public pool resources take precedence. The public pool is preferentially used to create the instance. When public pool resources are insufficient, private pool resources are used as a supplement. The system preferentially and automatically matches an open private pool. If no eligible private pool is available, the specified ResourcePoolOptions.PrivatePoolIds or a Target private pool that meets the PrivatePoolTags condition is used. (This policy is in invitational preview and is not supported yet.)
        # 
        # - None: no resource pool policy is used.
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
                temp_model = main_models.CreateScalingConfigurationShrinkRequestResourcePoolOptionsPrivatePoolTags()
                self.private_pool_tags.append(temp_model.from_map(k1))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class CreateScalingConfigurationShrinkRequestResourcePoolOptionsPrivatePoolTags(DaraModel):
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

class CreateScalingConfigurationShrinkRequestNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        secondary_private_ip_address_count: int = None,
        security_group_ids: List[str] = None,
        v_switch_ids: List[str] = None,
    ):
        # The elastic network interfaces (ENIs) type. When you use this parameter, you must use the NetworkInterfaces Settings for the primary network interface controller (NIC), and you cannot set the SecurityGroupId or SecurityGroupIds parameter. Valid values:
        # 
        # - Primary: primary elastic network interface (ENI).
        # 
        # - Secondary: secondary elastic network interface (ENI).
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses for the primary ENI.
        # Take note of the following items:
        # 
        # - This parameter takes effect only when NetworkInterface.InstanceType is set to Primary. If NetworkInterface.InstanceType is set to Secondary or left empty, you cannot configure this parameter.
        # 
        # - After you configure this parameter, you cannot configure Ipv6AddressCount.
        self.ipv_6address_count = ipv_6address_count
        # The communication pattern of the network interface controller (NIC). Valid values of the parameter:
        # 
        # - Standard: uses the TCP communication pattern.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication pattern.
        # 
        # Default value: Standard.
        # 
        # > The number of elastic network interfaces (ENIs) in RDMA pattern cannot exceed the limit of the instance family. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of secondary private IPv4 addresses to be assigned to the ENI. Valid values: 1 to 49.
        # 
        # - The value cannot exceed the limit on the number of IP addresses for the instance type. For more information, see [Instance families](https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families).
        # 
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount specifies the number of secondary private IPv4 addresses to be assigned to the ENI, excluding the primary private IP address of the ENI. The system randomly assigns these addresses from the available CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the ENI belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The IDs of one or more security groups to which the elastic network interfaces (ENIs) belong.
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch to which the elastic network interfaces (ENIs) belong. N indicates the Settings for multiple vSwitches. Valid values of N: 1 to 10.
        # 
        # Take note of the following items:
        # - If InstanceType is set to Primary, you cannot set this parameter. The default value is the vSwitch to which the instance belongs.
        # - If InstanceType is set to Secondary or left empty, this parameter is optional.
        # - The system selects a vSwitch that is in the same zone as the primary network interface controller (NIC) and has the most active IP addresses.
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

class CreateScalingConfigurationShrinkRequestInstanceTypeOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        # When you need the scaling group to scale based on the capacity of the instance type, specify both this parameter and WeightedCapacity.
        # 
        # This parameter specifies the instance type and overrides the instance type in the launch template. You can specify N instance types to extend the launch template to support N instance types. Valid values of N: 1 to 20.
        # 
        # > This parameter takes effect only when LaunchTemplateId is specified.
        # 
        # Valid values of InstanceType: available ECS instance types.
        self.instance_type = instance_type
        # When you need to specify the capacity of the instance type in the scaling configuration, specify this parameter after you specify InstanceTypeOverrides.InstanceType.
        # 
        # This parameter specifies the weight of the instance type, which indicates the capacity that a single instance of the instance type provides in the scaling group. A greater weight indicates that fewer instances of this instance type are required to meet the expected capacity.
        # 
        # Because instance types have different performance metrics such as the number of vCPUs and memory size, you can configure different weights for different instance types based on your business requirements.
        # 
        # Example:
        # 
        # - Current capacity: 0.
        # - Expected capacity: 6.
        # - Capacity of the ecs.c5.xlarge instance type: 4.
        # 
        # To meet the expected capacity, the scaling group scales out by adding two ecs.c5.xlarge instances.
        # 
        # > During scale-out, the capacity of the scaling group cannot exceed the sum of the maximum capacity (MaxSize) and the maximum weight of the instance type.
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

class CreateScalingConfigurationShrinkRequestInstanceTypeCandidateOptions(DaraModel):
    def __init__(
        self,
        allow_cidr_blocks: List[str] = None,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        enabled: bool = None,
        max_price: float = None,
    ):
        # Specifies the CIDR blocks of the optional vSwitches when you add vSwitches in other zones.
        self.allow_cidr_blocks = allow_cidr_blocks
        # Specifies whether to allow supplementing vSwitches in other zones.
        # > The instance types remain unchanged, and only new zones are used as candidates. If the scaling group cannot scale out in all selected zones due to issues such as insufficient stock, the system automatically adds vSwitches in new zones to the scaling group based on this configuration.
        # > For example, if the scaling group is configured with the cn-hangzhou-h and cn-hangzhou-g zones, and scale-out fails in both zones, Auto Scaling may create a vSwitch in the cn-hangzhou-k zone and add it to the scaling group based on real-time stock availability.
        self.allow_cross_az = allow_cross_az
        # Specifies whether to allow supplementing instance types of other generations.
        # 
        # - For example, if the current instance type is ecs.c7.large, instance types such as ecs.c6.large and ecs.c8.large can be used as candidates after this feature is enabled.
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

class CreateScalingConfigurationShrinkRequestInstancePatternInfos(DaraModel):
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
        # - X86: x86 computing.
        # - Heterogeneous: heterogeneous computing, such as GPU or FPGA.
        # - BareMental: ECS bare metal server.
        # - Arm: Arm computing.
        # 
        # Default value: all architecture types.
        self.architectures = architectures
        # Specifies whether the instance type is a burstable instance type. Valid values:
        # 
        # - Exclude: does not include burstable instance types.
        # - Include: includes burstable instance types.
        # - Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The number of vCPUs of the instance type in intelligent configuration mode. This parameter is used to filter instance types that meet your requirements. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # Take note of the following items:
        # 
        # - The InstancePatternInfos parameter is applicable only when the network type of the scaling group is VPC.
        # 
        # - You must configure both InstancePatternInfos.Cores and InstancePatternInfos.Memory when you use the InstancePatternInfos parameter.
        # 
        # - If you have already specified instance types by using the InstanceType or InstanceTypes parameter, Auto Scaling preferentially uses the specified instance types for scale-out. If the specified instance types are out of stock, Auto Scaling preferentially uses the instance type that has the lowest price among the instance types that meet the requirements specified by the InstancePatternInfos parameter.
        self.cores = cores
        # The CPU architecture of the instance. Valid values:
        # 
        # >N indicates that you can specify multiple CPU architectures. Valid values of N: 1 to 2.
        # 
        # - X86.
        # - ARM.
        self.cpu_architectures = cpu_architectures
        # The instance types to be excluded. You can use a wildcard (*) to exclude a single instance type or an entire instance family. Examples:
        # 
        # - ecs.c6.large: excludes the ecs.c6.large instance type.
        # - ecs.c6.*: excludes all instance types in the c6 instance family.
        self.excluded_instance_types = excluded_instance_types
        # The GPU type.
        self.gpu_specs = gpu_specs
        # The instance categorization. Valid values:
        # 
        # >N indicates the Settings for multiple instance categories. Valid values of N: 1 to 10.
        # 
        # - General-purpose: general-purpose.
        # - Compute-optimized: compute-optimized.
        # - Memory-optimized: memory-optimized.
        # - Big data: big data.
        # - Local SSDs: local SSD.
        # - High Clock Speed: high frequency.
        # - Enhanced: enhanced.
        # - Shared: shared.
        # - Compute-optimized with GPU: GPU computing.
        # - Visual Compute-optimized: visual compute-optimized.
        # - Heterogeneous Service: heterogeneous service.
        # - Compute-optimized with FPGA: FPGA-accelerated compute-optimized.
        # - Compute-optimized with NPU: NPU-accelerated compute-optimized.
        # - ECS Bare Metal: ECS Bare Metal Instance.
        # - High Performance Compute: high-performance computing (HPC).
        self.instance_categories = instance_categories
        # The level of the instance family. This parameter is used to filter instance types that meet your requirements and takes effect when `CostOptimization` is enabled. Valid values:
        # 
        # - EntryLevel: shared instance types. These instance types are more cost-effective but cannot ensure consistent computing performance. They are suitable for scenarios where the CPU utilization is typically low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # - EnterpriseLevel: enterprise-level instance types. These instance types provide consistent performance and dedicated resources. They are suitable for scenarios that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # - CreditEntryLevel: credit-based entry-level instance types, which are burstable instances. These instance types use CPU credits to ensure computing performance and are suitable for scenarios where the CPU utilization is typically low but occasionally bursts. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families to be queried. N indicates that you can specify multiple instance families. Valid values of N: 1 to 10.
        self.instance_type_families = instance_type_families
        # The maximum acceptable hourly price for pay-as-you-go or spot instances in intelligent configuration mode. This parameter is used to filter instance types that meet your requirements.
        # 
        # > This parameter is required when SpotStrategy is set to SpotWithPriceLimit. In other cases, this parameter is optional.
        self.max_price = max_price
        # The maximum number of vCPUs of the instance type.
        # 
        # > The value of MaximumCpuCoreCount cannot exceed four times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs for the instance. Valid values: positive integers.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size of the instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size of the instance type in intelligent configuration mode. Unit: GiB. This parameter is used to filter instance types that meet your requirements.
        self.memory = memory
        # The minimum baseline vCPU computing performance (the sum of all vCPUs) for t5 and t6 burstable instances.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPUs of the instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum upper limit on the number of IPv6 addresses per elastic network interfaces (ENIs) or network interface controller (NIC) for the instance.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum upper limit on the number of IPv4 addresses per elastic network interfaces (ENIs) or network interface controller (NIC) for the instance.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum upper limit on the number of network interface controller (NIC) devices that can be mounted to the instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs for the instance. Valid values: positive integers.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The minimum initial vCPU credit value for t5 and t6 burstable instances.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size of the instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The physical processor model of the instance. N indicates that you can specify multiple processor models. Valid values of N: 1 to 10.
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

class CreateScalingConfigurationShrinkRequestDataDisks(DaraModel):
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
        # Specifies whether to enable the burstable performance feature for the data cloud disk. Valid values:
        # 
        # - true: enables the feature.
        # - false: disables the feature. 
        # > You can set this parameter only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The multiple disk types of the data cloud disk. If the disk type with a higher priority is unavailable, Auto Scaling automatically tries the disk type with the next highest priority to create the data cloud disk. Valid values:
        # - cloud: basic cloud disk. The DeleteWithInstance property of a basic cloud disk created together with the instance is set to true.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_auto: ESSD AutoPL.
        # - cloud_regional_disk_auto: regional ESSD.
        # 
        # > If you specify this parameter, you cannot specify `DataDisks.Category` at the same time.
        self.categories = categories
        # The category of the data cloud disk. Valid values:
        # 
        # - cloud: basic cloud disk. The DeleteWithInstance attribute of a basic cloud disk created together with the instance is set to true.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD cloud disk.
        # - cloud_essd: ESSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_auto: ESSD AutoPL.
        # - cloud_regional_disk_auto: regional ESSD.
        # 
        # You cannot specify this parameter together with DataDisk.Categories. If neither this parameter nor DataDisk.Categories is specified, the default value is used:
        # - For I/O optimized instances, the default value is cloud_efficiency.
        # - For non-I/O optimized instances, the default value is cloud.
        self.category = category
        # Specifies whether to release the data cloud disk when the instance is released. Valid values:
        # 
        # - true: releases the data cloud disk when the instance is released.
        # - false: retains the data cloud disk when the instance is released.
        # 
        # You can set this parameter only for independent cloud disks (when DataDisks.Category is set to cloud, cloud_efficiency, cloud_ssd, or cloud_essd). Otherwise, an error is returned.
        # 
        # Default value: true.
        self.delete_with_instance = delete_with_instance
        # The description of the data cloud disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The mount point of the data cloud disk. If you do not specify this parameter, the system automatically allocates a mount point by default during automatic creation of the ECS instance. The mount point starts from /dev/xvdb and ends at /dev/xvdz.
        self.device = device
        # The name of the data cloud disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.disk_name = disk_name
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # 
        # - true: encrypts the data cloud disk.
        # - false: does not encrypt the data cloud disk.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key used by the data cloud disk.
        self.kmskey_id = kmskey_id
        # The settings of the performance level for the data cloud disk when it is an ESSD. Valid values:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > For more information about how to select the performance level of an ESSD, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics of the data cloud disk.
        # 
        # > IOPS indicates the number of I/O operations that can be processed per second. It measures the read and write capabilities of block storage. Unit: operations per second.
        self.provisioned_iops = provisioned_iops
        # The size of the data cloud disk. Unit: GiB. Valid values:
        # 
        # - cloud: 5 to 2000.
        # - cloud_efficiency: 20 to 32768.
        # - cloud_essd: 20 to 32768.
        # - ephemeral_ssd: 5 to 800.
        # 
        # If you specify this parameter, the disk size must be greater than or equal to the snapshot size specified by SnapshotId.
        self.size = size
        # The snapshot used to create the data cloud disk. If this parameter is specified, DataDisks.Size is ignored, and the actual size of the created disk is the size of the specified snapshot.
        # 
        # If the snapshot was created on or before July 15, 2013, the call is rejected and the InvalidSnapshot.TooOld error code is returned.
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

class CreateScalingConfigurationShrinkRequestCustomPriorities(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        vswitch_id: str = None,
    ):
        # The instance type of the ECS instance.
        # 
        # >Notice: The instance type must be included in the instance type list of the scaling configuration.
        self.instance_type = instance_type
        # The ID of the vSwitch.
        # 
        # >Notice: The vSwitch must be included in the vSwitch list of the scaling group.
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

class CreateScalingConfigurationShrinkRequestSystemDisk(DaraModel):
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
        # Specifies whether to enable the burst (performance burst) feature for the system cloud disk. Valid values:
        # 
        # - true: enables the feature.
        # - false: disables the feature.
        # > This parameter is supported only when `SystemDisk.Category` is set to `cloud_auto`.
        # 
        # <props="china">For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The category of the system cloud disk. Valid values:
        # 
        # - cloud: basic cloud disk.
        # 
        # - cloud_efficiency: ultra cloud disk.
        # 
        # - cloud_ssd: standard SSD cloud disk.
        # 
        # - ephemeral_ssd: local SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud_auto: ESSD AutoPL.
        # 
        # You cannot specify this parameter together with `SystemDiskCategories`. If neither this parameter nor `SystemDiskCategories` is specified, the default value is used:
        # 
        # - For I/O optimized instances, the default value is cloud_efficiency.
        # - For non-I/O optimized instances, the default value is cloud.
        # 
        # This parameter specifies only one system cloud disk type. If you want the system to automatically try other types when the preferred disk type is unavailable, use `SystemDiskCategories` and configure multiple disk types in order of priority.
        self.category = category
        # The description of the system cloud disk. The description must be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system cloud disk. The name must be 2 to 128 characters in length and can contain letters, digits, colons (:), underscores (_), and hyphens (-). It must start with a letter and cannot start with `http://` or `https://`.
        self.disk_name = disk_name
        # The encryption algorithm used for the system cloud disk. Valid values:
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
        # The settings of the performance level for the system cloud disk when it is an ESSD. Valid values:
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
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics for the system cloud disk.
        # 
        # > IOPS refers to the number of I/O operations that can be processed per second. It indicates the read and write processing capability of block storage. Unit: operations per second.
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

class CreateScalingConfigurationShrinkRequestPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private pool. It is the ID of the elasticity assurance or capacity reservation.
        self.id = id
        # The private pool options for instance startup. After an elasticity assurance or a capacity reservation takes effect, a private pool is generated for you to select when you start instances. Valid values:
        # 
        # - Open: open mode. The system automatically matches an open private pool. If no matching private pool is available, the system uses resources from the public pool. In this mode, you do not need to specify the PrivatePoolOptions.Id parameter.
        # 
        # - Target: specified mode. The system uses the specified private pool to start the instance. If the specified private pool is unavailable, the instance fails to start. In this mode, you must specify the private pool ID by using the PrivatePoolOptions.Id parameter.
        # 
        # - None: no private pool. The system does not use private pools to start the instance.
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

class CreateScalingConfigurationShrinkRequestImageOptions(DaraModel):
    def __init__(
        self,
        login_as_non_root: bool = None,
    ):
        # Specifies whether to log on to the ECS instance as the ecs-user user. For more information, see [Manage the logon username of an ECS instance](https://help.aliyun.com/document_detail/388447.html). Valid values:
        # 
        # - true: yes.
        # 
        # - false: no.
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

