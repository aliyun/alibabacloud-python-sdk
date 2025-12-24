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
        # Specifies whether to associate the instance on a dedicated host with the dedicated host. Valid values:
        # 
        # *   default: does not associate the instance on the dedicated host with the dedicated host. If you restart an instance that was stopped in Economical Mode and the original dedicated host of the instance has insufficient resources, the instance is automatically deployed to another dedicated host in the automatic deployment resource pool.
        # *   host: associates the instance on a dedicated host with the dedicated host. If you restart an instance that was stopped in Economical Mode, the instance remains on the original dedicated host. If the original dedicated host has insufficient resources, the instance cannot be started.
        self.affinity = affinity
        # The number of vCPUs.
        # 
        # You can specify the number of vCPUs and the memory size to determine the range of instance types. For example, you can set Cpu to 2 and Memory to 16 to specify instance types that have 2 vCPUs and 16 GiB of memory. If you specify Cpu and Memory, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates instances by using the lowest-priced instance type.
        # 
        # > You can specify CPU and Memory to determine the range of instance types only if you set Scaling Policy to Cost Optimization Policy and you do not specify an instance type in the scaling configuration.
        self.cpu = cpu
        # The performance mode of burstable instances. Valid values:
        # 
        # *   Standard: the standard mode. For more information, see the "Standard mode" section in the [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html) topic.
        # *   Unlimited: the unlimited mode. For more information, see the "Unlimited mode" section in the [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html) topic.
        self.credit_specification = credit_specification
        # The priority of the custom "ECS instance type + vSwitch" combination.
        # 
        # >  This setting is valid only if the scaling policy of the scaling group is a priority policy.
        # 
        # If Auto Scaling cannot create ECS instances by using the custom "ECS instance type + vSwitch" combination of the highest priority, Auto Scaling creates ECS instances by using the custom "ECS instance type + vSwitch" combination of the next highest priority.
        # 
        # >  If you specify the priorities of only a part of custom "ECS instance type + vSwitch" combinations, Auto Scaling preferentially creates ECS instances by using the custom combinations that have the specified priorities. If the custom combinations that have the specified priorities do not provide sufficient resources, Auto Scaling creates ECS instances by using the custom combinations that do not have the specified priorities based on the specified orders of vSwitches and instance types.
        # 
        # *   Example: The specified order of vSwitches for your scaling group is vsw1 and vsw2, and the specified order of instance types in your scaling configuration is type1 and type 2. In addition, you use CustomPriorities to specify ["vsw2+type2", "vsw1+type2"]. In this example, the vsw2+type2 combination has the highest priority and the vsw2+type1 combination has the lowest priority. The vsw1+type2 combination has a higher priority than the vsw1+type1 combination.
        self.custom_priorities = custom_priorities
        # The data disks.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host on which you want to create ECS instances. You cannot create preemptible instances on dedicated hosts. If you specify DedicatedHostId, SpotStrategy and SpotPriceLimit are ignored.
        # 
        # You can call the DescribeDedicatedHosts operation to query the most recent list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # Specifies whether to enable the Release Protection feature for ECS instances. If you enable this feature, you cannot directly release the ECS instances in the ECS console or by calling the DeleteInstance operation. Valid values:
        # 
        # *   true: enables the Release Protection feature. In this case, you cannot directly release the ECS instances in the ECS console or by calling the DeleteInstance operation.
        # *   false: disables the Release Protection feature. In this case, you can directly release the ECS instances in the ECS console or by calling the DeleteInstance operation.
        # 
        # >  You can enable the Release Protection feature only for pay-as-you-go instances to prevent accidental instance deletion. The Release Protection feature does not affect normal scaling activities. An instance that meets the criteria of scale-in policies can be removed from a scaling group during a scale-in event, regardless of whether you enabled the Release Protection feature for the instance.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set of the ECS instances that are created by using the scaling configuration.
        self.deployment_set_id = deployment_set_id
        # The hostname of the ECS instance. The hostname cannot start or end with a period (.) or a hyphen (-). The hostname cannot contain consecutive periods (.) or hyphens (-). Naming conventions for different types of instances:
        # 
        # *   Windows instances: The hostname must be 2 to 15 characters in length, and can contain letters, digits, and hyphens (-). The hostname cannot contain periods (.) or contain only digits.
        # *   Other instances, such as Linux instances: The hostname must be 2 to 64 characters in length. Separate a hostname into multiple segments with periods (.). Each segment can contain letters, digits, and hyphens (-).
        self.host_name = host_name
        # The ID of the Elastic High Performance Computing (E-HPC) cluster to which the ECS instances belong.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # 
        # *   enabled
        # *   disabled
        # 
        # Default value: enabled.
        # 
        # >  For information about instance metadata, see [Obtain instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_endpoint = http_endpoint
        # Specifies whether to forcibly use the security hardening mode (IMDSv2) to access instance metadata. Valid values:
        # 
        # *   optional: does not forcibly use the security hardening mode (IMDSv2).
        # *   required: forcibly uses the security hardening mode (IMDSv2). If you set this parameter to required, you cannot access instance metadata in normal mode.
        # 
        # Default value: optional.
        # 
        # >  For more information about instance metadata access modes, see [Access modes of instance metadata](https://help.aliyun.com/document_detail/108460.html).
        self.http_tokens = http_tokens
        # The name of the image family. If you specify this parameter, the latest custom images that are available in the specified image family are returned. Then, you can use the images to create instances. If you specify ImageId, you cannot specify ImageFamily.
        self.image_family = image_family
        # The ID of the image that is used by Auto Scaling to automatically create ECS instances.
        # 
        # > If the image that is specified in the scaling configuration contains system disks and data disks, the data that is stored in the data disks is cleared after you modify the image.
        self.image_id = image_id
        # The name of the image. Each image name must be unique in a region. If you specify ImageId, ImageName is ignored.
        # 
        # You cannot use ImageName to specify images from Alibaba Cloud Marketplace.
        self.image_name = image_name
        # The description of the ECS instance. The description must be 2 to 256 characters in length. The description can contain letters but cannot start with `http://` or `https://`.
        self.instance_description = instance_description
        # The name of the Elastic Compute Service (ECS) instance that is automatically created by using the scaling configuration.
        self.instance_name = instance_name
        # The intelligent configuration settings, which determine the available instance types.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance types.
        self.instance_type_overrides = instance_type_overrides
        # The instance types. If you specify InstanceTypes, InstanceType is ignored.
        # 
        # Auto Scaling creates instances based on a priority list of instance types. If it fails to create instances using the highest-priority type, it automatically moves to the next type in the priority order.
        self.instance_types = instance_types
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth. You are charged for the bandwidth specified by InternetMaxBandwidthOut.
        # *   PayByTraffic: pay-by-traffic. You are charged for the actual traffic generated. InternetMaxBandwidthOut specifies only the maximum available bandwidth.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s. Valid values:
        # 
        # *   If the purchased outbound public bandwidth is less than or equal to 10 Mbit/s, the valid values of this parameter are 1 to 10. The default value is 10.
        # *   If the purchased outbound public bandwidth is greater than 10 Mbit/s, the valid values of this parameter are 1 to the value of `InternetMaxBandwidthOut`. The default value is the value of `InternetMaxBandwidthOut`.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s. Valid values: 0 to 100.
        # 
        # Default value: 0.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether to create I/O optimized instances from the scaling configuration. Valid values:
        # 
        # *   none: creates non-I/O optimized instances from the scaling configuration.
        # *   optimized: creates I/O optimized instances from the scaling configuration.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses that you want to allocate to the elastic network interface (ENI).
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair that you can use to log on to an ECS instance.
        # 
        # *   Windows instances do not support this parameter.
        # *   By default, the username and password authentication method is disabled for Linux instances.
        self.key_pair_name = key_pair_name
        # The weight of an ECS instance as a backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # 
        # You can specify the number of vCPUs and the memory size to determine the range of instance types. For example, you can set Cpu to 2 and Memory to 16 to specify instance types that have 2 vCPUs and 16 GiB of memory. If you specify Cpu and Memory, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones. Then, Auto Scaling preferentially creates instances by using the lowest-priced instance type.
        # 
        # > You can specify CPU and Memory to determine the range of instance types only if you set Scaling Policy to Cost Optimization Policy and you do not specify an instance type in the scaling configuration.
        self.memory = memory
        # The ENIs.
        self.network_interfaces = network_interfaces
        # Specifies whether to overwrite existing data. Valid values:
        # 
        # *   true
        # *   false
        self.override = override
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The password of the ECS instance. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported:
        # 
        # \\`()~!@#$%^&\\*-_+=|{}[]:;\\"<>,.?/
        # 
        # The password of a Windows instance cannot start with a forward slash (/).
        # 
        # >  We recommend that you use HTTPS to send requests if you specify Password to avoid password leakage.
        self.password = password
        # Specifies whether to use the password that is preconfigured in the image. Before you use this parameter, make sure that a password is configured in the image.
        self.password_inherit = password_inherit
        # The name of the RAM role that you want to attach to the ECS instance. The name is provided and maintained by Resource Access Management (RAM). You can call the ListRoles operation to query the available RAM roles. You can call the CreateRole operation to create RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instances belong.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The resource pools used for instance creation, which can be the public pool or a private pool associated with any active elasticity assurance or capacity reservation. When you specify this parameter, take note of the following items:
        # 
        # *   This parameter takes effect only when you create pay-as-you-go instances.
        # *   If you specify this parameter, you cannot specify PrivatePoolOptions.MatchCriteria or PrivatePoolOptions.Id.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling configuration that you want to modify.
        # 
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit.
        # 
        # The name of the scaling configuration must be unique in a region. If you do not specify this parameter, the scaling configuration ID is used.
        self.scaling_configuration_name = scaling_configuration_name
        # The scheduler options.
        self.scheduler_options = scheduler_options
        # The ID of the security group with which ECS instances are associated. The ECS instances that are associated with the same security group can access each other.
        self.security_group_id = security_group_id
        # The IDs of the security groups.
        self.security_group_ids = security_group_ids
        self.security_options = security_options
        # The protection period of preemptible instances. Unit: hours. Valid values:
        # 
        # *   1: After a preemptible instance is created, Alibaba Cloud ensures that the instance is not automatically released within 1 hour. After the 1-hour protection period ends, Alibaba Cloud compares the bidding price with the market price and checks the resource inventory to determine whether to release the instance.
        # *   0: After a preemptible instance is created, Alibaba Cloud does not ensure that the instance is not automatically released within 1 hour. Alibaba Cloud compares the biding price with the market price and checks the resource inventory to determine whether to release the instance.
        # 
        # >  Alibaba Cloud notifies you of ECS system events 5 minutes before an instance is released. Preemptible instances are billed by second. We recommend that you specify a protection period based on your business requirements.
        # 
        # Default value: 1.
        self.spot_duration = spot_duration
        # The interruption mode of the preemptible instance. Default value: Terminate. Set the value to Terminate. This value specifies that the preemptible instance is to be released.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The preemptible instance types.
        self.spot_price_limits = spot_price_limits
        # The preemption policy of pay-as-you-go instances. Valid values:
        # 
        # *   NoSpot: The instances are created as regular pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are preemptible instances that have a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are preemptible instances for which the market price at the time of purchase is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        self.storage_set_id = storage_set_id
        self.storage_set_partition_number = storage_set_partition_number
        # The categories of the system disks. If Auto Scaling cannot create disks by using the disk category of the highest priority, Auto Scaling creates disks by using the disk category of the next highest priority. Valid values:
        # 
        # *   cloud: basic disk.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: ESSD.
        # 
        # >  If you specify this parameter, you cannot specify `SystemDisk.Category`.
        self.system_disk_categories = system_disk_categories
        # The tags of the ECS instance. Specify the tags as key-value pairs. You can specify up to 20 tags. When you specify tag keys and tag values, take note of the following items:
        # 
        # *   A tag key can be up to 64 characters in length. The key cannot start with `acs:` or `aliyun`, and cannot contain `http://` or `https://`. The tag key cannot be an empty string.
        # *   A tag value can be up to 128 characters in length. The value cannot start with `acs:` or `aliyun`, and cannot contain `http://` or `https://`. The tag value can be an empty string.
        self.tags = tags
        # Specifies whether to create ECS instances on dedicated hosts. Valid values:
        # 
        # *   default: creates ECS instances on non-dedicated hosts.
        # *   host: creates ECS instances on dedicated hosts. If you do not specify DedicatedHostId, the system randomly selects a dedicated host for an ECS instance.
        self.tenancy = tenancy
        # The user data of the Elastic Compute Service (ECS) instance. The user data must be encoded in Base64 format. The size of raw data before Base64 encoding cannot exceed 32 KB.
        self.user_data = user_data
        # The zone ID of the ECS instances that are created by using the scaling configuration.
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
        # The instance type of the preemptible instance. This parameter takes effect only if you set SpotStrategy to SpotWithPriceLimit.
        self.instance_type = instance_type
        # The price limit of the preemptible instance. This parameter takes effect only if you set SpotStrategy to SpotWithPriceLimit.
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
        # 
        # *   Enclave: An enclave-based confidential computing environment is built on the instance. For more information, see [Build a confidential computing environment by using Enclave](https://help.aliyun.com/document_detail/203433.html).
        # *   TDX: A Trust Domain Extensions (TDX) confidential computing environment is built on the instance. For more information, see [Build a TDX confidential computing environment](https://help.aliyun.com/document_detail/479090.html).
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
        strategy: str = None,
    ):
        # The IDs of private pools. The ID of a private pool is the same as that of the elasticity assurance or capacity reservation for which the private pool is generated. You can specify the IDs of only targeted private pools for this parameter.
        self.private_pool_ids = private_pool_ids
        # The resource pool used for instance creation, which can be the public pool or a private pool associated with any active elasticity assurance or capacity reservation. Valid values:
        # 
        # *   PrivatePoolFirst: prioritizes private pools. When this option is set along with ResourcePoolOptions.PrivatePoolIds, the specified private pools are used first. If you leave ResourcePoolOptions.PrivatePoolIds empty or if the specified private pools lack sufficient capacity, the system will automatically use available open private pools instead. If no matching private pools are available, the system defaults to the public pool.
        # *   PrivatePoolOnly: uses only private pools. If you use this value, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pools lack sufficient capacity, instance creation will fail.
        # *   None: uses no resource pools.
        # 
        # Default value: None.
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

class ModifyScalingConfigurationRequestNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        security_group_ids: List[str] = None,
    ):
        # The ENI type. If you specify this parameter, you must use NetworkInterfaces to specify a primary ENI. In addition, you cannot specify SecurityGroupId or SecurityGroupIds. Valid values:
        # 
        # *   Primary: the primary ENI.
        # *   Secondary: the secondary ENI.
        # 
        # Default value: Secondary.
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses that you want to allocate to the primary ENI. Before you specify this parameter, take note of the following items:
        # 
        # This parameter takes effect only if you set NetworkInterface.InstanceType to Primary. If you set NetworkInterface.InstanceType to Secondary or leave it empty, you cannot specify this parameter.
        # 
        # After you specify this parameter, you can no longer specify Ipv6AddressCount.
        self.ipv_6address_count = ipv_6address_count
        # The communication mode of the ENI. Valid values:
        # 
        # *   Standard: uses the TCP communication mode.
        # *   HighPerformance: uses the remote direct memory access (RDMA) communication mode with Elastic RDMA Interface (ERI) enabled.
        # 
        # Default value: Standard.
        # 
        # >  The number of ERIs on an instance cannot exceed the maximum number of ERIs supported by the instance type. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The IDs of the security groups to which you want to assign the ENI.
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

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

class ModifyScalingConfigurationRequestInstanceTypeOverrides(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        weighted_capacity: int = None,
    ):
        # The instance type. If you want to specify the capacity of instance types in the scaling configuration, specify InstanceType and WeightedCapacity at the same time.
        # 
        # You can use InstanceType to specify multiple instance types and WeightedCapacity to specify the weights of the instance types.
        # 
        # > If you specify InstanceType, you cannot specify InstanceTypes.
        # 
        # You can use InstanceType to specify only instance types that are available for purchase.
        self.instance_type = instance_type
        # The weight of the instance type. The weight specifies the capacity of an instance of the specified instance type in the scaling group. If you want Auto Scaling to scale instances in the scaling group based on the weighted capacity of the instances, specify WeightedCapacity after you specify InstanceType.
        # 
        # A higher weight specifies that a smaller number of instances of the specified instance type are required to meet the expected capacity requirement.
        # 
        # Performance metrics, such as the number of vCPUs and the memory size of each instance type, may vary. You can specify different weights for different instance types based on your business requirements.
        # 
        # Example:
        # 
        # *   Current capacity: 0
        # *   Expected capacity: 6
        # *   Capacity of ecs.c5.xlarge: 4
        # 
        # To meet the expected capacity requirement, Auto Scaling must create and add two ecs.c5.xlarge instances.
        # 
        # > The capacity of the scaling group cannot exceed the sum of the maximum number of instances that is specified by MaxSize and the maximum weight of the instance types.
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
        # The architecture types of the instance types. Valid values:
        # 
        # *   X86: x86.
        # *   Heterogeneous: heterogeneous computing, such as GPU-accelerated or FPGA-accelerated.
        # *   BareMetal: ECS Bare Metal Instance.
        # *   Arm: Arm.
        # 
        # By default, all values are selected.
        self.architectures = architectures
        # Specifies whether to include burstable instance types. Valid values:
        # 
        # *   Exclude: excludes burstable instance types.
        # *   Include: includes burstable instance types.
        # *   Required: includes only burstable instance types.
        # 
        # Default value: Include.
        self.burstable_performance = burstable_performance
        # The number of vCPUs per instance type in intelligent configuration mode. You can specify this parameter to filter the available instance types. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # Before you specify this parameter, take note of the following items:
        # 
        # *   You can specify InstancePatternInfo only if your scaling group resides in a virtual private cloud (VPC).
        # *   If you specify InstancePatternInfo, you must also specify InstancePatternInfo.Cores and InstancePatternInfo.Memory.
        # *   Auto Scaling preferentially uses the instance type specified by InstanceType or InstanceTypes to create instances. If the specified instance type does not have sufficient inventory, Auto Scaling selects the lowest-priced instance type specified by InstancePatternInfo to create instances.
        self.cores = cores
        # The CPU architectures of the instance types. Valid values:
        # 
        # >  You can specify up to two CPU architectures.
        # 
        # *   x86
        # *   Arm
        self.cpu_architectures = cpu_architectures
        # The instance types that you want to exclude. You can use an asterisk (\\*) as a wildcard character to exclude an instance type or an instance family. Examples:
        # 
        # *   ecs.c6.large: excludes the ecs.c6.large instance type.
        # *   ecs.c6.\\*: excludes the c6 instance family.
        self.excluded_instance_types = excluded_instance_types
        # The GPU models.
        self.gpu_specs = gpu_specs
        # The categories of the instance types. Valid values:
        # 
        # *   General-purpose: general-purpose instance type.
        # *   Compute-optimized: compute-optimized instance type.
        # *   Memory-optimized: memory-optimized instance type.
        # *   Big data: big data instance type.
        # *   Local SSDs: instance type that uses local SSDs.
        # *   High Clock Speed: instance type that has a high clock speed.
        # *   Enhanced: enhanced instance type.
        # *   Shared: shared instance type.
        # *   Compute-optimized with GPU: GPU-accelerated compute-optimized instance type.
        # *   Visual Compute-optimized: visual compute-optimized instance type.
        # *   Heterogeneous Service: heterogeneous service instance type.
        # *   Compute-optimized with FPGA: FPGA-accelerated compute-optimized instance type.
        # *   Compute-optimized with NPU: NPU-accelerated compute-optimized instance type.
        # *   ECS Bare Metal: ECS Bare Metal Instance type.
        # *   High Performance Compute: HPC-optimized instance type.
        self.instance_categories = instance_categories
        # The level of the instance family. You can specify this parameter to obtain the available instance types. This parameter takes effect only if you set `CostOptimization` to true. Valid values:
        # 
        # *   EntryLevel: entry-level (shared instance types). Instance types of this level are the most cost-effective but may not ensure stable computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # *   EnterpriseLevel: enterprise-level. Instance types of this level provide stable performance and dedicated resources and are suitable for business scenarios that require high stability. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # *   CreditEntryLevel: credit entry-level (burstable instance types). CPU credits are used to ensure computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low but may fluctuate in specific cases. For more information, see [Overview](https://help.aliyun.com/document_detail/59977.html) of burstable instances.
        self.instance_family_level = instance_family_level
        # The instance families that you want to specify. You can specify up to 10 instance families in each call.
        self.instance_type_families = instance_type_families
        # The maximum hourly price of pay-as-you-go or preemptible instances in intelligent configuration mode. You can specify this parameter to obtain the available instance types.
        # 
        # >  If you set SpotStrategy to SpotWithPriceLimit, you must specify this parameter. In other cases, this parameter is optional.
        self.max_price = max_price
        # The maximum number of vCPUs per instance type.
        # 
        # >  The value of MaximumCpuCoreCount cannot exceed four times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs per instance. The value must be a positive integer.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size per instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size per instance type in intelligent configuration mode. Unit: GiB. You can specify this parameter to filter the available instance types.
        self.memory = memory
        # The baseline vCPU computing performance (overall baseline performance of all vCPUs) of each t5 or t6 burstable instance.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPUs per instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum number of IPv6 addresses per ENI.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of IPv4 addresses per ENI.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) per instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs per instance. The value must be a positive integer.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The initial vCPU credits of each t5 or t6 burstable instance.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size per instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor models of the instance types. You can specify up to 10 processor models.
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
        # The ID of the automatic snapshot policy that you want to apply to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the Burst feature for the system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you set `SystemDisk.Category` to `cloud_auto`, you can specify this parameter.
        self.bursting_enabled = bursting_enabled
        # The categories of data disks. Valid values:
        # 
        # *   cloud: basic disk. The DeleteWithInstance attribute of a basic disk created along with each ECS instance is set to true.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: ESSD.
        # 
        # >  If you specify this parameter, you cannot specify `DataDisk.Category`.
        self.categories = categories
        # The category of the data disk. Valid values:
        # 
        # *   cloud: basic disk. The DeleteWithInstance attribute of a basic disk created along with each ECS instance is set to true.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   ephemeral_ssd: local SSD.
        # *   cloud_essd: ESSD.
        # 
        # If you specify this parameter, you cannot specify `DataDisk.Categories`. If you leave this parameter and `DataDisk.Categories` empty at the same time, the default value of this parameter is used.
        # 
        # *   For I/O optimized instances, the default value is cloud_efficiency.
        # *   For non-I/O optimized instances, the default value is cloud.
        self.category = category
        # Specifies whether to release the data disk if the instance to which the data disk is attached is released. Valid values:
        # 
        # *   true
        # *   false
        # 
        # If you set DataDisk.Category to cloud, cloud_efficiency, cloud_ssd, cloud_essd, or cloud_auto, you can specify this parameter. If you specify this parameter for data disks of other categories, an error is returned.
        self.delete_with_instance = delete_with_instance
        # The description of the system disk. The description must be 2 to 256 characters in length, and cannot start with `http://` or `https://`.
        self.description = description
        # The mount target of the data disk. If you do not specify this parameter, the system automatically assigns a mount target when Auto Scaling creates an ECS instance. Valid values: /dev/xvdb to /dev/xvdz.
        self.device = device
        # The name of the system disk. The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter but cannot start with `http://` or `https://`.
        self.disk_name = disk_name
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # *   true
        # *   false
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key that you want to apply to the data disk.
        self.kmskey_id = kmskey_id
        # The PL of the data disk that is an ESSD. Valid values:
        # 
        # *   PL0: An ESSD can provide up to 10,000 random read/write IOPS.
        # *   PL1: An ESSD can provide up to 50,000 random read/write IOPS.
        # *   PL2: An ESSD can provide up to 100,000 random read/write IOPS.
        # *   PL3: An ESSD can provide up to 1,000,000 random read/write IOPS.
        # 
        # >  For more information about how to select ESSD PLs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The provisioned IOPS of the data disk.
        # 
        # >  IOPS measures the number of read and write operations that an Elastic Block Storage (EBS) device can process per second.
        self.provisioned_iops = provisioned_iops
        # The size of the data disk. Unit: GB. Valid values:
        # 
        # *   5 to 2000 if you set DataDisk.Category to cloud.
        # *   20 to 32768 if you set DataDisk.Category to cloud_efficiency.
        # *   20 to 32768 if you set DataDisk.Category to cloud_ssd.
        # *   20 to 32768 if you set DataDisk.Category to cloud_essd.
        # *   5 to 800 if you set DataDisk.Category to ephemeral_ssd.
        # 
        # Set Size to a value that is greater than or equal to the size of the snapshot specified by SnapshotId.
        self.size = size
        # The ID of the snapshot that you want to use to create data disks. If you specify this parameter, DataDisk.Size is ignored. The size of the data disk created by using the snapshot is the same as the size of the snapshot.
        # 
        # If the snapshot was created on or before July 15, 2013, the API request is rejected and the InvalidSnapshot.TooOld message is returned.
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
        # The ECS instance type.
        # 
        # >  The ECS instance type must be included in the instance types specified in the scaling configuration.
        self.instance_type = instance_type
        # The vSwitch ID.
        # 
        # >  The vSwitch must be included in the vSwitch list of the scaling group.
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
        # The ID of the automatic snapshot policy that you want to apply to the system disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the Burst feature for the system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  If you set `SystemDisk.Category` to `cloud_auto`, you can specify this parameter.
        self.bursting_enabled = bursting_enabled
        # The category of the system disk. Valid values:
        # 
        # *   cloud: basic disk.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: Enterprise SSD (ESSD).
        # *   ephemeral_ssd: local SSD.
        # 
        # If you specify SystemDisk.Category, you cannot specify `SystemDiskCategories`. If you do not specify SystemDisk.Category or `SystemDiskCategories`, the default value of SystemDisk.Category is used. The default value for non-I/O optimized instances of Generation I instance families is cloud. The default value for other instances is cloud_efficiency.
        self.category = category
        # The description of the system disk. The description must be 2 to 256 characters in length. The description can contain letters but cannot start with `http://` or `https://`.
        self.description = description
        # The name of the system disk. The name must be 2 to 128 characters in length, and can contain letters, digits, colons (:), underscores (_), and hyphens (-). The name must start with a letter but cannot start with `http:// `or `https://`. 
        # 
        # Default value: null.
        self.disk_name = disk_name
        # The encryption algorithm of the system disk. Valid values:
        # 
        # *   AES-256
        # *   SM4-128
        # 
        # Default value: AES-256.
        self.encrypt_algorithm = encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the KMS key that you want to use to encrypt the system disk.
        self.kmskey_id = kmskey_id
        # The performance level (PL) of the system disk that is an ESSD. Valid values:
        # 
        # *   PL0: An ESSD can provide up to 10,000 random read/write IOPS.
        # *   PL1: An ESSD can provide up to 50,000 random read/write IOPS.
        # *   PL2: An ESSD can provide up to 100,000 random read/write IOPS.
        # *   PL3: An ESSD can provide up to 1,000,000 random read/write IOPS.
        # 
        # >  For more information about how to select ESSD PLs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.performance_level = performance_level
        # The IOPS metric that is preconfigured for the system disk.
        # 
        # > IOPS measures the number of read and write operations that an EBS device can process per second.
        self.provisioned_iops = provisioned_iops
        # The size of the system disk. Unit: GiB. Valid values:
        # 
        # *   Basic disk: 20 to 500.
        # 
        # *   ESSD: Valid values vary based on the performance level of the ESSD.
        # 
        #     *   PL0 ESSD: 1 to 2048.
        #     *   PL1 ESSD: 20 to 2048.
        #     *   PL2 ESSD: 461 to 2048.
        #     *   PL3 ESSD: 1261 to 2048.
        # 
        # *   ESSD AutoPL disk: 1 to 2048.
        # 
        # *   Other disk categories: 20 to 2048.
        # 
        # The value of this parameter must be at least 1 and greater than or equal to the image size.
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
        # The ID of the private pool. The ID of a private pool is the same as the ID of the elasticity assurance or capacity reservation for which the private pool is generated.
        self.id = id
        # The type of the private pool that you want to use to start ECS instances. A private pool is generated when an elasticity assurance or a capacity reservation takes effect. You can specify a private pool for Auto Scaling to start ECS instances. Valid values:
        # 
        # *   Open: open private pool. Auto Scaling selects a matching open private pool to start ECS instances. If no matching open private pools exist, the resources in the public pool are used. In this case, you do not need to specify PrivatePoolOptions.Id.
        # *   Target: specified private pool. Auto Scaling uses the resources in the specified private pool to start ECS instances. If the specified private pool does not exist, Auto Scaling cannot start ECS instances. If you set this parameter to Target, you must specify PrivatePoolOptions.Id.
        # *   None: no private pool. Auto Scaling does not use the resources of private pools to start ECS instances.
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
        # Specifies whether to use ecs-user to log on to an ECS instance created from the scaling configuration. For information about logon usernames, see [Manage the logon username of an instance](https://help.aliyun.com/document_detail/388447.html). Valid values:
        # 
        # true
        # 
        # false
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

