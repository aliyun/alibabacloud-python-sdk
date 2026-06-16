# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeScalingConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_configurations: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurations] = None,
        total_count: int = None,
    ):
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The collection of scaling configuration information.
        self.scaling_configurations = scaling_configurations
        # The total number of scaling configurations.
        self.total_count = total_count

    def validate(self):
        if self.scaling_configurations:
            for v1 in self.scaling_configurations:
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

        result['ScalingConfigurations'] = []
        if self.scaling_configurations is not None:
            for k1 in self.scaling_configurations:
                result['ScalingConfigurations'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.scaling_configurations = []
        if m.get('ScalingConfigurations') is not None:
            for k1 in m.get('ScalingConfigurations'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurations()
                self.scaling_configurations.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeScalingConfigurationsResponseBodyScalingConfigurations(DaraModel):
    def __init__(
        self,
        affinity: str = None,
        cpu: int = None,
        cpu_options: main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsCpuOptions = None,
        creation_time: str = None,
        credit_specification: str = None,
        custom_priorities: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsCustomPriorities] = None,
        data_disks: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks] = None,
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
        image_options_login_as_non_root: bool = None,
        image_owner_alias: str = None,
        instance_description: str = None,
        instance_generation: str = None,
        instance_name: str = None,
        instance_pattern_infos: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos] = None,
        instance_type: str = None,
        instance_type_candidate_options: main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstanceTypeCandidateOptions = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_in: int = None,
        internet_max_bandwidth_out: int = None,
        io_optimized: str = None,
        ipv_6address_count: int = None,
        key_pair_name: str = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        memory: int = None,
        network_interfaces: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsNetworkInterfaces] = None,
        password_inherit: bool = None,
        password_setted: bool = None,
        private_pool_options_id: str = None,
        private_pool_options_match_criteria: str = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_pool_options: main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptions = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        scheduler_options: main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions = None,
        security_enhancement_strategy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_options: main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSecurityOptions = None,
        spot_duration: int = None,
        spot_interruption_behavior: str = None,
        spot_price_limits: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits] = None,
        spot_strategy: str = None,
        storage_set_id: str = None,
        storage_set_partition_number: int = None,
        system_disk_auto_snapshot_policy_id: str = None,
        system_disk_bursting_enabled: bool = None,
        system_disk_categories: List[str] = None,
        system_disk_category: str = None,
        system_disk_description: str = None,
        system_disk_encrypt_algorithm: str = None,
        system_disk_encrypted: bool = None,
        system_disk_kmskey_id: str = None,
        system_disk_name: str = None,
        system_disk_performance_level: str = None,
        system_disk_provisioned_iops: int = None,
        system_disk_size: int = None,
        tags: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags] = None,
        tenancy: str = None,
        user_data: str = None,
        weighted_capacities: List[int] = None,
        zone_id: str = None,
    ):
        # Whether the Dedicated Host instance is associated with a dedicated host. Valid values:
        # 
        # - default: The instance is not associated with a dedicated host. If economical mode is enabled, when the instance restarts after being stopped and the original dedicated host lacks sufficient resources, the instance is placed on another dedicated host in the automatic deployment resource pool.
        # 
        # - host: The instance is associated with a dedicated host. If economical mode is enabled, when the instance restarts after being stopped, it remains on the original dedicated host. If the original dedicated host lacks sufficient resources, the instance fails to restart.
        self.affinity = affinity
        # The number of vCPUs.
        # 
        # Specifying both CPU and Memory defines a range of instance types. For example, CPU=2 and Memory=16 defines all instance types with 2 vCPUs and 16 GiB memory. Auto Scaling determines available instance types based on I/O optimization, zone, and other factors, then creates the lowest-priced instance according to price sorting.
        # 
        # > This range-based configuration takes effect only in cost optimization mode when no instance type is specified in the scaling configuration.
        self.cpu = cpu
        # CPU options.
        self.cpu_options = cpu_options
        # The creation time of the scaling configuration.
        self.creation_time = creation_time
        # The operating mode for burstable instances. Valid values:
        # 
        # - Standard: Standard mode. For performance details, see the Performance-constrained mode section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html)
        # 
        # - Unlimited: Unlimited mode. For performance details, see the Unlimited mode section in [What are burstable instances?](https://help.aliyun.com/document_detail/59977.html)
        self.credit_specification = credit_specification
        # The custom priority for ECS instance type plus vSwitch combinations.
        # >Notice: This parameter takes effect only when the scaling group\\"s scaling policy is set to priority-based.
        # 
        # If Auto Scaling cannot create an instance using a higher-priority instance type plus vSwitch combination, it automatically tries the next priority combination.
        # 
        # > If you specify custom priorities for only some instance type plus vSwitch combinations, unspecified combinations have lower priority. Among unspecified combinations, priority follows the scaling group\\"s vSwitch order and the scaling configuration\\"s instance type order.
        # >
        # > - Example: Scaling group vSwitch order is vsw1, vsw2. Scaling configuration instance type order is type1, type2. Custom priority order is ["vsw2+type2", "vsw1+type2"]. Final priority order is: "vsw2+type2" > "vsw1+type2" > "vsw1+type1" > "vsw2+type1".
        self.custom_priorities = custom_priorities
        # The collection of data disk information.
        self.data_disks = data_disks
        # The dedicated host cluster ID.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # Whether to create the ECS instance on a Dedicated Host. Since Dedicated Hosts do not support spot instances, specifying DedicatedHostId automatically ignores SpotStrategy and SpotPriceLimit settings in the request.
        # 
        # You can call the DescribeDedicatedHosts API to query the list of Dedicated Host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The instance release protection attribute, specifying whether the instance can be directly released through the ECS console or API (DeleteInstance). Valid values:
        # 
        # - true: Enable instance release protection. The instance cannot be directly released through the ECS console or API (DeleteInstance).
        # 
        # - false: Disable instance release protection. The instance can be directly released through the ECS console or API (DeleteInstance).
        # 
        # > This attribute applies only to pay-as-you-go instances to prevent accidental deletion of instances scaled out by Auto Scaling. It does not affect normal scale-in activities. Instances with release protection enabled can still be released during scale-in activities.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the ECS instance belongs.
        self.deployment_set_id = deployment_set_id
        # The hostname of the ECS instance.
        self.host_name = host_name
        # The ID of the HPC cluster to which the ECS instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Whether to enable the instance metadata access channel. Valid values:
        # 
        # - enabled: Enabled.
        # 
        # - disabled: Disabled.
        self.http_endpoint = http_endpoint
        # Whether to enforce hardened mode (IMDSv2) when accessing instance metadata. Valid values:
        # 
        # - optional: Do not enforce.
        # 
        # - required: Enforce. When set, standard mode cannot access instance metadata.
        self.http_tokens = http_tokens
        # The image family name. Setting this parameter retrieves the latest available image within the specified image family for instance creation. If ImageId is already set, do not set this parameter.
        self.image_family = image_family
        # The image file ID used as the image resource for automatic instance creation.
        self.image_id = image_id
        # The image file name.
        self.image_name = image_name
        # Whether the ECS instance uses the ecs-user account to log on. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        self.image_options_login_as_non_root = image_options_login_as_non_root
        # The image source. Valid values:
        # 
        # - system: Public images provided by Alibaba Cloud.
        # 
        # - self: Custom images you created.
        # 
        # - others: Shared or community images provided by other Alibaba Cloud users.
        # 
        # - marketplace: Images provided by Alibaba Cloud Marketplace.
        self.image_owner_alias = image_owner_alias
        # The description of the ECS instance.
        self.instance_description = instance_description
        # The series of the ECS instance.
        self.instance_generation = instance_generation
        # The name of the ECS instance.
        self.instance_name = instance_name
        # The collection of intelligent configuration information used to filter eligible instance type ranges.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance type of the ECS instance.
        self.instance_type = instance_type
        # When alternative mode is enabled, if issues like inventory shortages occur, similar instance types of the same size are supplemented based on the currently selected instance type, or switches in alternative zones are created and added to the scaling group.
        self.instance_type_candidate_options = instance_type_candidate_options
        # The collection of ECS instance types.
        self.instance_types = instance_types
        # The network billing type. Valid values:
        # 
        # - PayByBandwidth: Pay-by-bandwidth. InternetMaxBandwidthOut is the fixed bandwidth value.
        # 
        # - PayByTraffic: Pay-by-data-transfer. InternetMaxBandwidthOut is only a bandwidth cap. Billing is based on actual network traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Whether the instance is I/O optimized. Valid values:
        # 
        # - none: Not I/O optimized.
        # 
        # - optimized: I/O optimized.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses assigned to the elastic network interface.
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair used to log on to the ECS instance.
        self.key_pair_name = key_pair_name
        # The status of the scaling configuration within the scaling group. Valid values:
        # 
        # - Active: The scaling configuration is active. The scaling group uses active scaling configurations to automatically create ECS instances.
        # 
        # - Inactive: The scaling configuration is inactive. Inactive scaling configurations exist in the scaling group but are not used to automatically create ECS instances.
        self.lifecycle_state = lifecycle_state
        # The weight of the ECS instance as a backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # Memory size. Unit: GiB.
        # 
        # Specifying both CPU and Memory defines a range of instance types. For example, CPU=2 and Memory=16 defines all instance types with 2 vCPUs and 16 GiB memory. Auto Scaling determines available instance types based on I/O optimization, zone, and other factors, then creates the lowest-priced instance according to price sorting.
        # 
        # > This range-based configuration takes effect only in cost optimization mode when no instance type is specified in the scaling configuration.
        self.memory = memory
        # The list of elastic network interfaces.
        self.network_interfaces = network_interfaces
        # Whether to use the password preset in the image.
        self.password_inherit = password_inherit
        # Whether to set an instance password. Valid values:
        # 
        # - true: Set instance password.
        # 
        # - false: Do not set instance password.
        self.password_setted = password_setted
        # The private pool ID. This is either the elastic provisioning service ID or the capacity reservation service ID.
        self.private_pool_options_id = private_pool_options_id
        # The private pool capacity option for instance startup. After elastic provisioning or capacity reservation services take effect, they generate private pool capacity for instance startup selection. Valid values:
        # 
        # - Open: Open mode. Automatically matches open-type private pool capacity. If no matching private pool capacity exists, uses public pool resources to start the instance.
        # 
        # - Target: Target mode. Starts the instance using the specified private pool capacity. If that capacity is unavailable, the instance fails to start.
        # 
        # - None: Do not use mode. Instance startup does not use private pool capacity.
        self.private_pool_options_match_criteria = private_pool_options_match_criteria
        # The RAM role name of the ECS instance. RAM role names are provided and maintained by RAM. You can call ListRoles to query available RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instance belongs.
        self.resource_group_id = resource_group_id
        # The resource pool strategy used when creating instances.
        # 
        # - This parameter takes effect only when creating pay-as-you-go instances.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        self.scaling_group_id = scaling_group_id
        # > This parameter is in invitational preview and is not yet available for general use.
        self.scheduler_options = scheduler_options
        # Whether to enable security hardening. Valid values:
        # 
        # - Active: Enable security hardening. Applies only to public images.
        # 
        # - Deactive: Disable security hardening. Applies to all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the ECS instance belongs. ECS instances in the same security group can access each other.
        self.security_group_id = security_group_id
        # The IDs of multiple security groups to which the ECS instance belongs. ECS instances in the same security group can access each other.
        self.security_group_ids = security_group_ids
        # Security options.
        self.security_options = security_options
        # The reserved duration for the spot instance. Unit: hours.
        self.spot_duration = spot_duration
        # The interruption mode for spot instances.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The collection of spot instance information.
        self.spot_price_limits = spot_price_limits
        # The preemption policy for pay-as-you-go instances. Valid values:
        # 
        # - NoSpot: standard pay-as-you-go instance.
        # 
        # - SpotWithPriceLimit: spot instance with a maximum price limit.
        # 
        # - SpotAsPriceGo: system automatically bids based on current market price.
        self.spot_strategy = spot_strategy
        # The storage set ID.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. Value must be an integer greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The ID of the automatic snapshot policy applied to the system disk.
        self.system_disk_auto_snapshot_policy_id = system_disk_auto_snapshot_policy_id
        # Whether Burst (performance burst) is enabled for the system disk. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # > This parameter is supported only when SystemDisk.Category is cloud_auto.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Multiple disk categories for the system disk. The first disk category has the highest priority, followed by others in descending order. If Auto Scaling cannot use a higher-priority disk category, it automatically tries the next priority category to create the system disk. Valid values:
        # 
        # - cloud: basic disk.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - cloud_essd: ESSD.
        self.system_disk_categories = system_disk_categories
        # The disk category of the system disk. Valid values:
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
        # - cloud_auto: ESSD AutoPL.
        self.system_disk_category = system_disk_category
        # The description of the system disk.
        self.system_disk_description = system_disk_description
        # The encryption algorithm used for the system disk. Valid values:
        # 
        # - AES-256.
        # 
        # - SM4-128.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Whether the system disk is encrypted. Valid values:
        # 
        # - true: Encrypted.
        # 
        # - false: Not encrypted.
        self.system_disk_encrypted = system_disk_encrypted
        # The KMS key ID used for the system disk.
        self.system_disk_kmskey_id = system_disk_kmskey_id
        # The name of the system disk.
        self.system_disk_name = system_disk_name
        # The performance level of the ESSD system disk.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metric for the system disk.
        # 
        # > IOPS (Input/Output Operations Per Second) measures the number of I/O operations per second, indicating block storage read/write capability. Unit: operations.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The collection of tag information.
        self.tags = tags
        # Whether to create the instance on a Dedicated Host. Valid values:
        # 
        # - default: Create a non-Dedicated Host instance.
        # 
        # - host: Create a Dedicated Host instance. If you do not specify DedicatedHostId, Alibaba Cloud automatically selects a Dedicated Host to place the instance.
        # 
        # Default value: default.
        self.tenancy = tenancy
        # The custom data for the ECS instance.
        self.user_data = user_data
        # The weights corresponding to specified instance types, representing the capacity size of a single instance in the scaling group. Higher weights require fewer instances of that type to meet the desired capacity.
        self.weighted_capacities = weighted_capacities
        # The zone ID of the instance. You can call DescribeZones to get the zone list.
        self.zone_id = zone_id

    def validate(self):
        if self.cpu_options:
            self.cpu_options.validate()
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
        if self.network_interfaces:
            for v1 in self.network_interfaces:
                 if v1:
                    v1.validate()
        if self.resource_pool_options:
            self.resource_pool_options.validate()
        if self.scheduler_options:
            self.scheduler_options.validate()
        if self.security_options:
            self.security_options.validate()
        if self.spot_price_limits:
            for v1 in self.spot_price_limits:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affinity is not None:
            result['Affinity'] = self.affinity

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_options is not None:
            result['CpuOptions'] = self.cpu_options.to_map()

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

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

        if self.image_options_login_as_non_root is not None:
            result['ImageOptionsLoginAsNonRoot'] = self.image_options_login_as_non_root

        if self.image_owner_alias is not None:
            result['ImageOwnerAlias'] = self.image_owner_alias

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_generation is not None:
            result['InstanceGeneration'] = self.instance_generation

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

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight

        if self.memory is not None:
            result['Memory'] = self.memory

        result['NetworkInterfaces'] = []
        if self.network_interfaces is not None:
            for k1 in self.network_interfaces:
                result['NetworkInterfaces'].append(k1.to_map() if k1 else None)

        if self.password_inherit is not None:
            result['PasswordInherit'] = self.password_inherit

        if self.password_setted is not None:
            result['PasswordSetted'] = self.password_setted

        if self.private_pool_options_id is not None:
            result['PrivatePoolOptions.Id'] = self.private_pool_options_id

        if self.private_pool_options_match_criteria is not None:
            result['PrivatePoolOptions.MatchCriteria'] = self.private_pool_options_match_criteria

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_pool_options is not None:
            result['ResourcePoolOptions'] = self.resource_pool_options.to_map()

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        if self.scheduler_options is not None:
            result['SchedulerOptions'] = self.scheduler_options.to_map()

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

        if self.system_disk_auto_snapshot_policy_id is not None:
            result['SystemDiskAutoSnapshotPolicyId'] = self.system_disk_auto_snapshot_policy_id

        if self.system_disk_bursting_enabled is not None:
            result['SystemDiskBurstingEnabled'] = self.system_disk_bursting_enabled

        if self.system_disk_categories is not None:
            result['SystemDiskCategories'] = self.system_disk_categories

        if self.system_disk_category is not None:
            result['SystemDiskCategory'] = self.system_disk_category

        if self.system_disk_description is not None:
            result['SystemDiskDescription'] = self.system_disk_description

        if self.system_disk_encrypt_algorithm is not None:
            result['SystemDiskEncryptAlgorithm'] = self.system_disk_encrypt_algorithm

        if self.system_disk_encrypted is not None:
            result['SystemDiskEncrypted'] = self.system_disk_encrypted

        if self.system_disk_kmskey_id is not None:
            result['SystemDiskKMSKeyId'] = self.system_disk_kmskey_id

        if self.system_disk_name is not None:
            result['SystemDiskName'] = self.system_disk_name

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_provisioned_iops is not None:
            result['SystemDiskProvisionedIops'] = self.system_disk_provisioned_iops

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.tenancy is not None:
            result['Tenancy'] = self.tenancy

        if self.user_data is not None:
            result['UserData'] = self.user_data

        if self.weighted_capacities is not None:
            result['WeightedCapacities'] = self.weighted_capacities

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Affinity') is not None:
            self.affinity = m.get('Affinity')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuOptions') is not None:
            temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('CpuOptions'))

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('CreditSpecification') is not None:
            self.credit_specification = m.get('CreditSpecification')

        self.custom_priorities = []
        if m.get('CustomPriorities') is not None:
            for k1 in m.get('CustomPriorities'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsCustomPriorities()
                self.custom_priorities.append(temp_model.from_map(k1))

        self.data_disks = []
        if m.get('DataDisks') is not None:
            for k1 in m.get('DataDisks'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks()
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

        if m.get('ImageOptionsLoginAsNonRoot') is not None:
            self.image_options_login_as_non_root = m.get('ImageOptionsLoginAsNonRoot')

        if m.get('ImageOwnerAlias') is not None:
            self.image_owner_alias = m.get('ImageOwnerAlias')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceGeneration') is not None:
            self.instance_generation = m.get('InstanceGeneration')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        self.instance_pattern_infos = []
        if m.get('InstancePatternInfos') is not None:
            for k1 in m.get('InstancePatternInfos'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos()
                self.instance_pattern_infos.append(temp_model.from_map(k1))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeCandidateOptions') is not None:
            temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstanceTypeCandidateOptions()
            self.instance_type_candidate_options = temp_model.from_map(m.get('InstanceTypeCandidateOptions'))

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

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        self.network_interfaces = []
        if m.get('NetworkInterfaces') is not None:
            for k1 in m.get('NetworkInterfaces'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsNetworkInterfaces()
                self.network_interfaces.append(temp_model.from_map(k1))

        if m.get('PasswordInherit') is not None:
            self.password_inherit = m.get('PasswordInherit')

        if m.get('PasswordSetted') is not None:
            self.password_setted = m.get('PasswordSetted')

        if m.get('PrivatePoolOptions.Id') is not None:
            self.private_pool_options_id = m.get('PrivatePoolOptions.Id')

        if m.get('PrivatePoolOptions.MatchCriteria') is not None:
            self.private_pool_options_match_criteria = m.get('PrivatePoolOptions.MatchCriteria')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourcePoolOptions') is not None:
            temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('ResourcePoolOptions'))

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        if m.get('SchedulerOptions') is not None:
            temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions()
            self.scheduler_options = temp_model.from_map(m.get('SchedulerOptions'))

        if m.get('SecurityEnhancementStrategy') is not None:
            self.security_enhancement_strategy = m.get('SecurityEnhancementStrategy')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        if m.get('SecurityOptions') is not None:
            temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSecurityOptions()
            self.security_options = temp_model.from_map(m.get('SecurityOptions'))

        if m.get('SpotDuration') is not None:
            self.spot_duration = m.get('SpotDuration')

        if m.get('SpotInterruptionBehavior') is not None:
            self.spot_interruption_behavior = m.get('SpotInterruptionBehavior')

        self.spot_price_limits = []
        if m.get('SpotPriceLimits') is not None:
            for k1 in m.get('SpotPriceLimits'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits()
                self.spot_price_limits.append(temp_model.from_map(k1))

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        if m.get('StorageSetId') is not None:
            self.storage_set_id = m.get('StorageSetId')

        if m.get('StorageSetPartitionNumber') is not None:
            self.storage_set_partition_number = m.get('StorageSetPartitionNumber')

        if m.get('SystemDiskAutoSnapshotPolicyId') is not None:
            self.system_disk_auto_snapshot_policy_id = m.get('SystemDiskAutoSnapshotPolicyId')

        if m.get('SystemDiskBurstingEnabled') is not None:
            self.system_disk_bursting_enabled = m.get('SystemDiskBurstingEnabled')

        if m.get('SystemDiskCategories') is not None:
            self.system_disk_categories = m.get('SystemDiskCategories')

        if m.get('SystemDiskCategory') is not None:
            self.system_disk_category = m.get('SystemDiskCategory')

        if m.get('SystemDiskDescription') is not None:
            self.system_disk_description = m.get('SystemDiskDescription')

        if m.get('SystemDiskEncryptAlgorithm') is not None:
            self.system_disk_encrypt_algorithm = m.get('SystemDiskEncryptAlgorithm')

        if m.get('SystemDiskEncrypted') is not None:
            self.system_disk_encrypted = m.get('SystemDiskEncrypted')

        if m.get('SystemDiskKMSKeyId') is not None:
            self.system_disk_kmskey_id = m.get('SystemDiskKMSKeyId')

        if m.get('SystemDiskName') is not None:
            self.system_disk_name = m.get('SystemDiskName')

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskProvisionedIops') is not None:
            self.system_disk_provisioned_iops = m.get('SystemDiskProvisionedIops')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Tenancy') is not None:
            self.tenancy = m.get('Tenancy')

        if m.get('UserData') is not None:
            self.user_data = m.get('UserData')

        if m.get('WeightedCapacities') is not None:
            self.weighted_capacities = m.get('WeightedCapacities')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the instance. N ranges from 1 to 20.
        # 
        # If you specify this value, it cannot be an empty string. It can contain up to 128 characters, must not start with `aliyun` or `acs:`, and must not contain `http://` or `https://`.
        self.key = key
        # The tag value of the instance. N ranges from 1 to 20.
        # 
        # If you specify this value, it can be an empty string. It can contain up to 128 characters, must not start with `acs:`, and must not contain `http://` or `https://`.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSpotPriceLimits(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: float = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # The bid price for the spot instance.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSecurityOptions(DaraModel):
    def __init__(
        self,
        confidential_computing_mode: str = None,
    ):
        # The confidential computing mode. Valid values:
        # 
        # - Enclave: The ECS instance uses Enclave to build a confidential computing environment. For more information, see [Use Enclave to build a confidential computing environment](https://help.aliyun.com/document_detail/203433.html).
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions(DaraModel):
    def __init__(
        self,
        managed_private_space_id: str = None,
    ):
        # > This parameter is in invitational preview and is not yet available for general use.
        self.managed_private_space_id = managed_private_space_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.managed_private_space_id is not None:
            result['ManagedPrivateSpaceId'] = self.managed_private_space_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ManagedPrivateSpaceId') is not None:
            self.managed_private_space_id = m.get('ManagedPrivateSpaceId')

        return self

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        private_pool_tags: List[main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptionsPrivatePoolTags] = None,
        strategy: str = None,
    ):
        # The private pool ID. This is either the elastic provisioning service ID or the capacity reservation service ID.
        self.private_pool_ids = private_pool_ids
        # Filters available Target private pools by tag.
        self.private_pool_tags = private_pool_tags
        # Resource pools include private pools generated after elastic provisioning or capacity reservation services take effect, along with public pools, for instance startup selection. Valid values:
        # 
        # - PrivatePoolFirst: Private pool first. With this strategy, if ResourcePoolOptions.PrivatePoolIds is specified or PrivatePoolTags conditions are met, the corresponding private pool is prioritized. If no private pool is specified or the specified private pool lacks capacity, open-type private pools are automatically matched. If no matching private pool exists, public pool resources are used.
        # 
        # - PrivatePoolOnly: Private pool only. With this strategy, ResourcePoolOptions.PrivatePoolIds must be specified. If the specified private pool lacks capacity, the instance fails to start.
        # 
        # - PublicPoolFirst: Public pool first. Public pool resources are prioritized for instance creation. If public pool resources are insufficient, private pool resources supplement them. Open-type private pools are automatically matched first. If no matching private pool exists, specified ResourcePoolOptions.PrivatePoolIds or Target-type private pools meeting PrivatePoolTags conditions are used.
        # 
        # - None: Do not use resource pool strategy.
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
                temp_model = main_models.DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptionsPrivatePoolTags()
                self.private_pool_tags.append(temp_model.from_map(k1))

        if m.get('Strategy') is not None:
            self.strategy = m.get('Strategy')

        return self

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsResourcePoolOptionsPrivatePoolTags(DaraModel):
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        secondary_private_ip_address_count: int = None,
        security_group_ids: List[str] = None,
    ):
        # The elastic network interface type. Valid values:
        # 
        # - Primary: Primary network interface.
        # 
        # - Secondary: Secondary elastic network interface.
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses assigned to the primary network interface.
        self.ipv_6address_count = ipv_6address_count
        # The communication mode of the elastic network interface. Valid values:
        # 
        # - Standard: Uses TCP communication mode.
        # 
        # - HighPerformance: Enables ERI (Elastic RDMA Interface) and uses RDMA communication mode.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of secondary private IPv4 addresses assigned to the network interface. Valid values: 1–49.
        # 
        # - The value cannot exceed the IP address limit for the instance type. For more information, see [Instance families](https://help.aliyun.com/zh/ecs/user-guide/overview-of-instance-families).
        # 
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount assigns secondary private IPv4 addresses (excluding the primary private IP) to the network interface. The system randomly assigns addresses from the available CIDR block of the virtual switch (NetworkInterface.N.VSwitchId).
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The IDs of one or more security groups to which the elastic network interface belongs.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstanceTypeCandidateOptions(DaraModel):
    def __init__(
        self,
        allow_cidr_blocks: List[str] = None,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        enabled: bool = None,
        max_price: float = None,
    ):
        # When supplementing switches in other zones, specify the CIDR blocks for eligible switches.
        self.allow_cidr_blocks = allow_cidr_blocks
        # Indicates whether ESS can add vSwitches from other zones.
        # 
        # > The instance type remains unchanged. Only alternative zones are considered. If all selected zones in the scaling group cannot scale out due to inventory shortages or similar issues, ESS automatically adds a vSwitch from a new zone to the scaling group based on this setting.
        # > For example, if the scaling group is configured with zones cn-hangzhou-h and cn-hangzhou-g, and neither zone can scale out, ESS might create a vSwitch in zone cn-hangzhou-k based on real-time inventory availability and add it to the scaling group.
        self.allow_cross_az = allow_cross_az
        # Whether to allow supplementing instance types from different generations.
        # 
        # - For example, if the current type is ecs.c7.large, enabling this allows alternatives like ecs.c6.large and ecs.c8.large.
        self.allow_different_generation = allow_different_generation
        # Whether to enable alternative mode.
        self.enabled = enabled
        # The price cap for alternative instance types.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstancePatternInfos(DaraModel):
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
        # - Heterogeneous: Heterogeneous compute, such as GPU or FPGA.
        # 
        # - BareMetal: ECS Bare Metal Instance.
        # 
        # - Arm: Arm compute.
        self.architectures = architectures
        # Whether the instance type supports performance burst. Valid values:
        # 
        # - Exclude: Exclude burstable instance types.
        # 
        # - Include: Include burstable instance types.
        # 
        # - Required: Include only burstable instance types.
        self.burstable_performance = burstable_performance
        # The number of vCPU cores for the instance type.
        self.cores = cores
        # The CPU architecture of the instance type. Valid values:
        # 
        # > N indicates multiple CPU architectures can be specified. N ranges from 1 to 2.
        # 
        # - X86.
        # 
        # - ARM.
        self.cpu_architectures = cpu_architectures
        # The instance types to exclude. Use wildcard characters (\\*) to exclude a single instance type or an entire instance family. Examples:
        # 
        # - ecs.c6.large: Excludes the ecs.c6.large instance type.
        # 
        # - ecs.c6.\\*: Excludes all instance types in the c6 family.
        self.excluded_instance_types = excluded_instance_types
        # GPU types.
        self.gpu_specs = gpu_specs
        # Instance categories. Valid values:
        # 
        # > N indicates multiple instance categories can be specified. N ranges from 1 to 10.
        # 
        # - General-purpose: General-purpose.
        # 
        # - Compute-optimized: Compute-optimized.
        # 
        # - Memory-optimized: Memory-optimized.
        # 
        # - Big data: Big data.
        # 
        # - Local SSDs: Local SSD.
        # 
        # - High Clock Speed: High frequency.
        # 
        # - Enhanced: Enhanced.
        # 
        # - Shared: Shared-resource.
        # 
        # - Compute-optimized with GPU: GPU.
        # 
        # - Visual Compute-optimized: Visual compute.
        # 
        # - Heterogeneous Service: Heterogeneous computing.
        # 
        # - Compute-optimized with FPGA: FPGA.
        # 
        # - Compute-optimized with NPU: NPU.
        # 
        # - ECS Bare Metal: ECS Bare Metal Instance.
        # 
        # - High Performance Compute: High-performance computing (HPC).
        self.instance_categories = instance_categories
        # The instance family level.
        # 
        # - EntryLevel: Entry-level, i.e., shared-resource instances. Lower cost but cannot guarantee stable compute performance. Suitable for workloads with low average CPU usage. For more information, see [Shared-resource instances](https://help.aliyun.com/document_detail/108489.html).
        # 
        # - EnterpriseLevel: Enterprise-level. Stable performance with dedicated resources. Suitable for workloads requiring high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # 
        # - CreditEntryLevel: Credit entry-level, i.e., burstable instances. Uses CPU credits to ensure compute performance. Suitable for workloads with low average CPU usage and occasional bursts. For more information, see [Burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families to query. N indicates multiple instance families can be specified. N ranges from 1 to 10.
        self.instance_type_families = instance_type_families
        # The maximum hourly price acceptable for pay-as-you-go or spot instances.
        self.max_price = max_price
        # The maximum number of vCPU cores for the instance type.
        # 
        # > MaximumCpuCoreCount cannot exceed four times MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs. Valid values: positive integers.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size for the instance type. Unit: GiB.
        self.memory = memory
        # The minimum baseline vCPU compute performance (sum of all vCPUs) for burstable instances t5 and t6.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPU cores for the instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum number of IPv6 addresses per ENI.
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum number of IPv4 addresses per ENI.
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum number of elastic network interfaces (ENIs) that the instance type supports attaching.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs. Valid values: positive integers.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The minimum initial vCPU credit for burstable instances t5 and t6.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor models of the instance. N indicates multiple processor models can be specified. N ranges from 1 to 10.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsDataDisks(DaraModel):
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
        # The ID of the automatic snapshot policy applied to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Whether Burst (performance burst) is enabled for the data disk. Valid values:
        # 
        # - true: Enabled.
        # 
        # - false: Disabled.
        # 
        # > This parameter appears only when `DataDisk.Category` is `cloud_auto`.
        # 
        # <props="china">
        # 
        # For more information, see [ESSD AutoPL](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # Multiple disk categories for the data disk. The first disk category has the highest priority, followed by others in descending order. If Auto Scaling cannot use a higher-priority disk category, it automatically tries the next priority category to create the data disk. Valid values:
        # 
        # - cloud: basic disk. Basic disks created with an instance have DeleteWithInstance set to true.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - cloud_essd: ESSD.
        self.categories = categories
        # The disk category of the data disk. Valid values:
        # 
        # - cloud: basic disk. Basic disks created with an instance have DeleteWithInstance set to true.
        # 
        # - cloud_efficiency: ultra disk.
        # 
        # - cloud_ssd: standard SSD.
        # 
        # - ephemeral_ssd: local SSD.
        # 
        # - cloud_essd: ESSD.
        # 
        # - cloud_auto: ESSD AutoPL.
        self.category = category
        # Whether to release the data disk when releasing the instance. Valid values:
        # 
        # - true: Release the disk along with the instance.
        # 
        # - false: Keep the disk when releasing the instance.
        self.delete_with_instance = delete_with_instance
        # The description of the data disk.
        self.description = description
        # The mount target of the data disk.
        self.device = device
        # The name of the data disk.
        self.disk_name = disk_name
        # Whether the data disk is encrypted. Valid values:
        # 
        # - true: Encrypted.
        # 
        # - false: Not encrypted.
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The KMS key ID corresponding to the data disk.
        self.kmskey_id = kmskey_id
        # The performance level of the ESSD data disk.
        self.performance_level = performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metric for the data disk.
        # 
        # > IOPS (Input/Output Operations Per Second) measures the number of I/O operations per second, indicating block storage read/write capability. Unit: operations.
        self.provisioned_iops = provisioned_iops
        # The size of the data disk. Unit: GiB. Valid values:
        # 
        # - cloud: 5–2000.
        # 
        # - cloud_efficiency: 20–32768.
        # 
        # - cloud_ssd: 20–32768.
        # 
        # - cloud_essd: 20–32768.
        # 
        # - ephemeral_ssd: 5–800.
        self.size = size
        # The snapshot ID used to create the data disk.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsCustomPriorities(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        vswitch_id: str = None,
    ):
        # The instance type of the ECS instance.
        self.instance_type = instance_type
        # The ID of the virtual switch.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsCpuOptions(DaraModel):
    def __init__(
        self,
        nested_virtualization: str = None,
    ):
        # Nested virtualization, whether to enable hardware-based nested virtualization. Valid values:
        # 
        # - enabled: Enabled.
        # 
        # - disabled: Disabled.
        self.nested_virtualization = nested_virtualization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nested_virtualization is not None:
            result['NestedVirtualization'] = self.nested_virtualization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NestedVirtualization') is not None:
            self.nested_virtualization = m.get('NestedVirtualization')

        return self

