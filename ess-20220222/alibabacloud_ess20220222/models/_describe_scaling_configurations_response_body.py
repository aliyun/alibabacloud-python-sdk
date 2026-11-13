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
        # The scaling configurations.
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
        secondary_eni_vswitch_constraint: str = None,
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
        # Specifies whether the instance on a dedicated host is associated with the dedicated host. Valid values:
        # - default: The instance is not associated with the dedicated host. If the economical mode is enabled and the original dedicated host has insufficient resources when the instance is restarted, the instance is automatically deployed to another dedicated host in the automatic deployment resource pool.
        # - host: The instance is associated with the dedicated host. If the economical mode is enabled and the original dedicated host has insufficient resources when the instance is restarted, the instance fails to be restarted.
        self.affinity = affinity
        # The number of vCPUs.
        # You can specify both the Cpu and Memory parameters to define the instance type range. For example, if you set Cpu to 2 and Memory to 16, all instance types that have 2 vCPUs and 16 GiB of memory are matched. Auto Scaling determines the available instance types based on factors such as I/O optimization and zones, and creates instances of the type that has the lowest price.
        # > This configuration takes effect only when the scaling mode is set to cost optimization and no instance types are specified in the scaling configuration.
        self.cpu = cpu
        # The CPU options.
        self.cpu_options = cpu_options
        # The time when the scaling configuration was created. The time follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format. The time is displayed in UTC.
        self.creation_time = creation_time
        # The performance mode of the burstable instance. Valid values:
        # - Standard: standard mode. For more information, see the "Standard mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        # - Unlimited: unlimited mode. For more information, see the "Unlimited mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The custom priority of ECS instance type and vSwitch combination.
        # >Notice: This parameter takes effect only when the scaling policy of the scaling group is set to priority-based policy.</notice>
        # If an instance cannot be created by using ECS instance type and vSwitch combination that has the highest priority, Auto Scaling automatically uses the combination that has the next highest priority to create ECS instance.
        # > If you specify custom priorities for only some instance type and vSwitch combinations, the unspecified combinations have lower priorities than the specified ones. The priorities of the unspecified combinations are determined based on the vSwitch sequence in the scaling group and ECS instance type sequence in the scaling configuration.
        # > - For example, if the vSwitch sequence in the scaling group is vsw1 and vsw2, ECS instance type sequence in the scaling configuration is type1 and type2, and the custom priority sequence is ["vsw2+type2", "vsw1+type2"], the final priority sequence is: "vsw2+type2" > "vsw1+type2" > "vsw1+type1" > "vsw2+type1".
        self.custom_priorities = custom_priorities
        # The data cloud disks.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host on which to create the ECS instance. Dedicated hosts do not support spot instances. If you specify the DedicatedHostId parameter, the SpotStrategy and SpotPriceLimit parameters are ignored.
        # You can call the DescribeDedicatedHosts operation to query the list of dedicated host IDs.
        self.dedicated_host_id = dedicated_host_id
        # The release protection property of the instance, which specifies whether the instance can be directly released by using the ECS console or the DeleteInstance API operation. Valid values:
        # - true: Release protection is enabled. The instance cannot be directly released by using the ECS console or the DeleteInstance API operation.
        # - false: Release protection is shutdown. The instance can be directly released by using the ECS console or the DeleteInstance API operation.
        # > This property applies only to pay-as-you-go instances. It prevents instances created by Auto Scaling during scale-out from being accidentally deleted, but does not affect normal scale-in activities. Instances with release protection enabled can still be released during scale-in activities.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the ECS instance belongs.
        self.deployment_set_id = deployment_set_id
        # The hostname of the ECS instance.
        self.host_name = host_name
        # The ID of the High Performance Computing (HPC) cluster to which the ECS instance belongs.
        self.hpc_cluster_id = hpc_cluster_id
        # Specifies whether to enable the access channel for instance metadata. Valid values:
        # - enabled: enabled.
        # - disabled: disabled.
        self.http_endpoint = http_endpoint
        # Specifies whether to forcibly use the security hardening mode (IMDSv2) when accessing instance metadata. Valid values:
        # - optional: not forcibly used.
        # - required: forcibly used. If this value is set, instance metadata cannot be accessed in normal mode.
        self.http_tokens = http_tokens
        # The name of the image family. You can set this parameter to obtain the latest available image in the image family to create instances. If the ImageId parameter is specified, you cannot specify this parameter.
        self.image_family = image_family
        # The ID of the image file, which is the image resource used for the automatic creation of instances.
        self.image_id = image_id
        # The name of the image.
        self.image_name = image_name
        # Specifies whether to log on to the ECS instance as the ecs-user user. Valid values:
        # - true: yes.
        # - false: no.
        self.image_options_login_as_non_root = image_options_login_as_non_root
        # The source of the image. Valid values:
        # - system: public images provided by Alibaba Cloud.
        # - self: custom images created by you.
        # - others: shared images or community images provided by other Alibaba Cloud users.
        # - marketplace: images provided by Alibaba Cloud Marketplace.
        self.image_owner_alias = image_owner_alias
        # The description of the ECS instance.
        self.instance_description = instance_description
        # The generation of the ECS instance.
        self.instance_generation = instance_generation
        # The name of the ECS instance.
        self.instance_name = instance_name
        # The collection of intelligent configuration information used to filter instance types that meet your requirements.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance type of the ECS instance.
        self.instance_type = instance_type
        # After the fallback mode is configured, if issues such as insufficient inventory occur, the system supplements the selected instance types with similar instance types of the same size, or creates vSwitches in fallback zones and adds them to the scaling group.
        self.instance_type_candidate_options = instance_type_candidate_options
        # The collection of instance types for ECS instances.
        self.instance_types = instance_types
        # The network billing method. Valid values:
        # - PayByBandwidth: pay-by-bandwidth. In this case, the InternetMaxBandwidthOut parameter specifies the fixed bandwidth value.
        # - PayByTraffic: pay-by-traffic. In this case, the InternetMaxBandwidthOut parameter specifies the bandwidth cap, and you are billed based on the actual network traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Specifies whether the instance is an I/O optimized instance. Valid values:
        # - none: non-I/O optimization.
        # - optimized: I/O optimization.
        self.io_optimized = io_optimized
        # The number of IPv6 addresses that are randomly generated for the elastic network interface controller (NIC).
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair used to log on to the ECS instance.
        self.key_pair_name = key_pair_name
        # The lifecycle status of the scaling configuration in the scaling group. Valid values:
        # - Active: The scaling configuration is active. The scaling group uses active scaling configurations for the automatic creation of ECS instances.
        # - Inacitve: The scaling configuration is inactive. Inactive scaling configurations exist in the scaling group, but the scaling group does not use them for the automatic creation of ECS instances.
        self.lifecycle_state = lifecycle_state
        # The weight of the ECS instance when it is used as an SLB backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # You can specify both the Cpu and Memory parameters to define the instance type range. For example, if you set Cpu to 2 and Memory to 16, all instance types that have 2 vCPUs and 16 GiB of memory are matched. Auto Scaling determines the available instance types based on factors such as I/O optimization and zones, and creates instances of the type that has the lowest price.
        # > This configuration takes effect only when the scaling mode is set to cost optimization and no instance types are specified in the scaling configuration.
        self.memory = memory
        # The list of elastic network interfaces (ENIs). Each ENI is a network interface controller (NIC).
        self.network_interfaces = network_interfaces
        # Specifies whether to use the password preset in the image.
        self.password_inherit = password_inherit
        # Specifies whether an instance password is set. Valid values:
        # - true: An instance password is set.
        # - false: No instance password is set.
        self.password_setted = password_setted
        # The ID of the private pool. The ID is the same as the ID of the elasticity assurance or capacity reservation.
        self.private_pool_options_id = private_pool_options_id
        # The private pool type for starting the instance. After an elasticity assurance or capacity reservation takes effect, a private pool is generated. You can select a private pool type when you start an instance. Valid values:
        # - Open: open mode. The system automatically matches a private pool of the Open type. If no matching private pool is available, the system uses resources from the public pool to start the instance.
        # - Target: targeted mode. The system uses the specified private pool to start the instance. If the specified private pool is unavailable, the instance fails to be started.
        # - None: no private pool. The system does not use private pools to start the instance.
        self.private_pool_options_match_criteria = private_pool_options_match_criteria
        # The name of the Resource Access Management (RAM) role for the ECS instance. RAM roles are provided and maintained by RAM. You can call the ListRoles operation to query available RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instance belongs.
        self.resource_group_id = resource_group_id
        # The resource pool policy used when creating instances.
        # - This parameter takes effect only when creating pay-as-you-go instances.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        self.scaling_group_id = scaling_group_id
        # > This parameter is in invitational preview and is not available for public use.
        self.scheduler_options = scheduler_options
        # Specifies whether a vSwitch available for secondary elastic network interfaces (ENIs) must be selected from the list when the VSwitchIds parameter is specified.
        self.secondary_eni_vswitch_constraint = secondary_eni_vswitch_constraint
        # Specifies whether to enable security hardening. Valid values:
        # - Active: enables security hardening. This value is applicable only to public images.
        # - Deactive: disables security hardening. This value is applicable to all image types.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the ECS instance belongs. ECS instances in the same security group can access each other.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the ECS instances belong. ECS instances in the same security group can access each other.
        self.security_group_ids = security_group_ids
        # The security options.
        self.security_options = security_options
        # The protection period of the spot instance. Unit: hours.
        self.spot_duration = spot_duration
        # The interruption pattern of the spot instance.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The spot instances.
        self.spot_price_limits = spot_price_limits
        # The preemption policy for the pay-as-you-go instance. Valid values:
        # - NoSpot: regular pay-as-you-go instances.
        # - SpotWithPriceLimit: spot instances that have a maximum hourly price.
        # - SpotAsPriceGo: spot instances for which the system automatically bids based on the current market price.
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. The value must be an integer greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The ID of the automatic snapshot policy applied to the system cloud disk.
        self.system_disk_auto_snapshot_policy_id = system_disk_auto_snapshot_policy_id
        # Specifies whether to enable the burst feature for the system cloud disk. Valid values:
        # - true: enabled.
        # - false: disabled.
        # > This parameter is supported only when SystemDisk.Category is set to cloud_auto.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The disk types for the system cloud disk. The first disk type has the highest priority, and the priorities of the other disk types decrease in sequence. If the disk type with a higher priority is unavailable, Auto Scaling automatically attempts to create the system cloud disk by using the disk type with the next highest priority. Valid values:
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD cloud disk.
        # - cloud_essd: ESSD cloud disk.
        self.system_disk_categories = system_disk_categories
        # The category of the system cloud disk. Valid values:
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_essd: ESSD.
        # - cloud_auto: ESSD AutoPL disk.
        self.system_disk_category = system_disk_category
        # The description of the system cloud disk.
        self.system_disk_description = system_disk_description
        # The encryption algorithm used for the system cloud disk. Valid values:
        # - AES-256.
        # - SM4-128.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether the system cloud disk is encrypted. Valid values:
        # - true: The system cloud disk is encrypted.
        # - false: The system cloud disk is not encrypted.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key used for the system cloud disk.
        self.system_disk_kmskey_id = system_disk_kmskey_id
        # The name of the system cloud disk.
        self.system_disk_name = system_disk_name
        # The performance level of the system cloud disk when it is an ESSD (standard SSD).
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics for the system cloud disk.
        # > IOPS refers to the number of I/O operations that can be processed per second, which indicates the read and write processing capability of the block storage. Unit: operations per second.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system cloud disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The tags.
        self.tags = tags
        # Specifies whether to create the instance on a dedicated host. Valid values:
        # - default: creates the instance on a non-dedicated host.
        # - host: creates the instance on a dedicated host. If you do not specify the DedicatedHostId parameter, Alibaba Cloud automatically selects a dedicated host for the instance.
        # Default value: default.
        self.tenancy = tenancy
        # The user data of the ECS instance.
        self.user_data = user_data
        # The weight of the specified instance type, which indicates the capacity that a single instance of the specified instance type provides in the scaling group. A greater weight indicates that fewer instances of the instance type are required to meet the expected capacity.
        self.weighted_capacities = weighted_capacities
        # The zone ID of the instance. You can call the DescribeZones operation to query the zone list.
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

        if m.get('SecondaryEniVSwitchConstraint') is not None:
            self.secondary_eni_vswitch_constraint = m.get('SecondaryEniVSwitchConstraint')

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
        # The key of tag N of the instance. Valid values of N: 1 to 20.
        # If you specify this parameter, it cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with aliyun or acs:, and cannot contain http:// or https://.
        self.key = key
        # The value of tag N of the instance. Valid values of N: 1 to 20.
        # If you specify this parameter, it can be an empty string. The tag value can be up to 128 characters in length. It cannot start with acs:, and cannot contain http:// or https://.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsSchedulerOptions(DaraModel):
    def __init__(
        self,
        managed_private_space_id: str = None,
    ):
        # > This parameter is in invitational preview and is not available for public use.
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
        # The ID of the private pool, which is the ID of the elasticity assurance or capacity reservation.
        self.private_pool_ids = private_pool_ids
        # Filters available Target private pools by tag.
        self.private_pool_tags = private_pool_tags
        # Resource pools include private pools generated after the elasticity assurance or capacity reservation service takes effect, as well as public pools, which are available for selection when an instance starts. Valid values:
        # - PrivatePoolFirst: private pool first. When this policy is selected, if ResourcePoolOptions.PrivatePoolIds is specified or the PrivatePoolTags condition is met, the corresponding private pool is used first. If no private pool is specified or the specified private pool has insufficient capacity, the system automatically matches an open private pool. If no eligible private pool is available, the public pool is used to create the instance.
        # - PrivatePoolOnly: private pool only. When this policy is selected, ResourcePoolOptions.PrivatePoolIds must be specified. If the specified private pool has insufficient capacity, the instance fails to start.
        # - PublicPoolFirst: public pool first. The public pool is used first to create the instance. When public pool resources are insufficient, private pool resources are used as a supplement. The system preferentially matches an open private pool. If no eligible private pool is available, the system uses the Target private pool specified by ResourcePoolOptions.PrivatePoolIds or the one that meets the PrivatePoolTags condition.
        # - None: no resource pool policy is used.
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
        v_switch_ids: List[str] = None,
    ):
        # The type of the elastic network interfaces (ENIs). Valid values:
        # 
        # - Primary: primary network interface controller (NIC).
        # 
        # - Secondary: secondary elastic network interfaces (ENIs).
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses specified for the primary ENI.
        self.ipv_6address_count = ipv_6address_count
        # The communication pattern of the elastic network interfaces (ENIs), which act as a network interface controller (NIC). Valid values:
        # 
        # - Standard: uses the TCP communication pattern.
        # - HighPerformance: enables the Elastic RDMA Interface (ERI) and uses the RDMA communication pattern.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The number of secondary private IPv4 addresses specified for the ENI. Valid values: 1 to 49.
        # - The value cannot exceed the limit on the number of IP addresses for the instance type. For more information, see [Instance families](https://www.alibabacloud.com/help/en/ecs/user-guide/overview-of-instance-families).
        # - NetworkInterface.N.SecondaryPrivateIpAddressCount is used to specify the number of secondary private IPv4 addresses (excluding the primary private IP address of the ENI) to be assigned to the ENI. The system randomly assigns the addresses from the available CIDR block of the vSwitch (NetworkInterface.N.VSwitchId) to which the ENI belongs.
        self.secondary_private_ip_address_count = secondary_private_ip_address_count
        # The IDs of one or more security groups to which the elastic network interfaces (ENIs) belong. Each ENI is a network interface controller (NIC).
        self.security_group_ids = security_group_ids
        # The ID of the vSwitch to which the elastic network interfaces (ENIs) belong. Each ENI is a network interface controller (NIC).
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsInstanceTypeCandidateOptions(DaraModel):
    def __init__(
        self,
        allow_cidr_blocks: List[str] = None,
        allow_cross_az: bool = None,
        allow_different_generation: bool = None,
        enabled: bool = None,
        max_price: float = None,
    ):
        # The CIDR blocks of the vSwitches that can be selected when adding vSwitches from other zones is allowed.
        self.allow_cidr_blocks = allow_cidr_blocks
        # Specifies whether to allow adding vSwitches from other zones.
        # > The instance types remain unchanged, and only new zones are selected as alternatives. When the scaling group fails to scale out in all selected zones due to inventory shortages or other issues, this configuration automatically adds vSwitches from new zones to the scaling group.
        # > For example, if the scaling group is configured with the cn-hangzhou-h and cn-hangzhou-g zones and fails to scale out in both zones, Auto Scaling may create a vSwitch in the cn-hangzhou-k zone and add it to the scaling group based on real-time inventory.
        self.allow_cross_az = allow_cross_az
        # Specifies whether to allow supplementing instance types from other generations.
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
        # - X86: x86 computing.
        # - Heterogeneous: heterogeneous computing, such as GPU or FPGA.
        # - BareMental: ECS Bare Metal server.
        # - Arm: Arm computing.
        self.architectures = architectures
        # Specifies whether the instance type is a burstable instance type. Valid values:
        # - Exclude: excludes burstable instance types.
        # - Include: includes burstable instance types.
        # - Required: includes only burstable instance types.
        self.burstable_performance = burstable_performance
        # The number of vCPU cores of the instance type.
        self.cores = cores
        # The CPU architecture of the instance type. Valid values:
        # > N indicates that you can specify multiple CPU architectures. Valid values of N: 1 to 2.
        # - X86.
        # - ARM.
        self.cpu_architectures = cpu_architectures
        # The instance types to be excluded. You can use a wildcard (*) to exclude a single instance type or an entire instance family. Examples:
        # - ecs.c6.large: excludes the ecs.c6.large instance type.
        # - ecs.c6.*: excludes all instance types in the c6 instance family.
        self.excluded_instance_types = excluded_instance_types
        # The GPU type.
        self.gpu_specs = gpu_specs
        # The instance categorization. Valid values:
        # > N indicates that you can specify multiple instance categories in the Settings. Valid values of N: 1 to 10.
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
        # - ECS Bare Metal: ECS Bare Metal server.
        # - High Performance Compute: high-performance computing (HPC).
        self.instance_categories = instance_categories
        # The level of the instance family. Valid values:
        # - EntryLevel: entry-level instance families, which are shared instance families. These instance families are more cost-effective but do not guarantee consistent computing performance. They are suitable for workloads with low CPU utilization. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # - EnterpriseLevel: enterprise-level instance families. These instance families provide stable performance and dedicated resources, and are suitable for workloads that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # - CreditEntryLevel: credit entry-level instance families, which are burstable instances. These instance families use CPU credits to maintain computing performance and are suitable for workloads with low CPU utilization but occasional CPU bursts. For more information, see [Burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families to be queried. N indicates that you can specify multiple instance families. Valid values of N: 1 to 10.
        self.instance_type_families = instance_type_families
        # The maximum hourly price acceptable for pay-as-you-go or spot instances.
        self.max_price = max_price
        # The maximum number of vCPU cores of the instance type.
        # > The value of MaximumCpuCoreCount cannot exceed four times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs for the instance. Valid values: positive integers.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size of the instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size of the instance type. Unit: GiB.
        self.memory = memory
        # The minimum baseline vCPU computing performance (the sum of all vCPUs) for t5 and t6 burstable instances.
        self.minimum_baseline_credit = minimum_baseline_credit
        # The minimum number of vCPU cores of the instance type.
        self.minimum_cpu_core_count = minimum_cpu_core_count
        # The minimum value for the maximum number of IPv6 addresses supported by a single elastic network interfaces (ENIs) on the instance. Each ENI is a network interface controller (NIC).
        self.minimum_eni_ipv_6address_quantity = minimum_eni_ipv_6address_quantity
        # The minimum value for the maximum number of IPv4 addresses supported by a single elastic network interfaces (ENIs) on the instance. Each ENI is a network interface controller (NIC).
        self.minimum_eni_private_ip_address_quantity = minimum_eni_private_ip_address_quantity
        # The minimum value for the maximum number of elastic network interfaces (ENIs) that can be attached to the instance.
        self.minimum_eni_quantity = minimum_eni_quantity
        # The minimum number of GPUs for the instance. Valid values: positive integers.
        self.minimum_gpu_amount = minimum_gpu_amount
        # The minimum initial vCPU credit value for t5 and t6 burstable instances.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size of the instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor model of the instance. N indicates that you can specify multiple processor models. Valid values of N: 1 to 10.
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
        # The ID of the automatic snapshot policy applied to the data cloud disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Specifies whether to enable the performance burst feature for the data cloud disk. Valid values:
        # - true: enables the feature.
        # - false: disables the feature.
        # > This parameter is displayed only when the DataDisk.Category parameter is set to cloud_auto.
        # <props="china">For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.bursting_enabled = bursting_enabled
        # The disk types of the data cloud disks. The first disk type has the highest priority, and the priorities of other disk types decrease in sequence. If a disk type with a higher priority is unavailable, Auto Scaling automatically attempts to create the data cloud disk by using the disk type with the next highest priority. Valid values:
        # - cloud: basic cloud disk. The DeleteWithInstance property of a basic cloud disk created along with an instance is set to true.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional ESSD.
        self.categories = categories
        # The category of the data cloud disk. Valid values:
        # - cloud: basic cloud disk. The DeleteWithInstance attribute of a basic cloud disk created along with an instance is set to true.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - ephemeral_ssd: local SSD.
        # - cloud_essd: ESSD.
        # - cloud_auto: ESSD AutoPL disk.
        # - cloud_regional_disk_auto: regional ESSD.
        self.category = category
        # Specifies whether to release the data cloud disk when the instance is released. Valid values:
        # - true: releases the data cloud disk when the instance is released.
        # - false: retains the data cloud disk when the instance is released.
        self.delete_with_instance = delete_with_instance
        # The description of the data cloud disk.
        self.description = description
        # The mount point of the data cloud disk.
        self.device = device
        # The name of the data cloud disk.
        self.disk_name = disk_name
        # Specifies whether to encrypt the data cloud disk. Valid values:
        # - true: encrypts the data cloud disk.
        # - false: does not encrypt the data cloud disk.
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key used to encrypt the data cloud disk.
        self.kmskey_id = kmskey_id
        # The performance level of the data cloud disk when it is an ESSD (standard SSD).
        self.performance_level = performance_level
        # The provisioned IOPS (Input/Output Operations Per Second) performance metrics of the data cloud disk.
        # > IOPS measures the number of I/O operations per second and indicates the read and write capabilities of the block storage. Unit: operations per second.
        self.provisioned_iops = provisioned_iops
        # The size of the data cloud disk. Unit: GiB. Valid values:
        # - cloud: 5 to 2000.
        # - cloud_efficiency: 20 to 32768.
        # - cloud_ssd: 20 to 32768.
        # - cloud_essd: 20 to 32768.
        # - ephemeral_ssd: 5 to 800.
        self.size = size
        # The ID of the snapshot used to create the data cloud disk.
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
        # The ID of the vSwitch.
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
        # Specifies whether to enable hardware-based nested virtualization. Valid values:
        # 
        # * enabled: Enabled.
        # * disabled: Disabled.
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

