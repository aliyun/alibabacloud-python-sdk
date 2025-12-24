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
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
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
        # Indicates whether the ECS instance on a dedicated host is associated with the dedicated host. Valid values:
        # 
        # *   default: The instance is not associated with the dedicated host. If you restart an instance that was stopped in Economical Mode and the original dedicated host of the instance has insufficient resources, the instance is automatically deployed to another dedicated host in the automatic deployment resource pool.
        # *   host: The instance is associated with the dedicated host. If you restart an instance that was stopped in Economical Mode, the instance remains on the original dedicated host. If the available resources of the original dedicated host are insufficient, the instance cannot be restarted.
        self.affinity = affinity
        # The number of vCPUs.
        # 
        # You can specify CPU and Memory to define the range of instance types. For example, if you set CPU to 2 and Memory to 16, the instance types that have 2 vCPUs and 16 GiB are returned. If you specify CPU and Memory, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones and preferentially creates instances by using the lowest-priced instance type.
        # 
        # >  You can specify CPU and Memory to define instance types only when you set Scaling Policy to Cost Optimization and no instance type is specified in the scaling configuration.
        self.cpu = cpu
        # The time at which the scaling configuration was created.
        self.creation_time = creation_time
        # The performance mode of the burstable instances. Valid values:
        # 
        # *   Standard: the standard mode. For more information, see the "Standard mode" section in the [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html) topic.
        # *   Unlimited: the unlimited mode. For more information, see the "Unlimited mode" section in [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.credit_specification = credit_specification
        # The priority of the custom ECS instance type + vSwitch combination.
        # 
        # >  This parameter takes effect only when Scaling Policy of the scaling group is set to Priority Policy.
        # 
        # If Auto Scaling cannot create ECS instances by using the custom ECS instance type + vSwitch combination of the highest priority, Auto Scaling creates ECS instances by using the custom ECS instance type + vSwitch combination of the next highest priority.
        # 
        # >  If you specify the priorities of only a portion of custom ECS instance type + vSwitch combinations, Auto Scaling preferentially creates ECS instances by using the custom combinations that have specified priorities. If the custom combinations that have specified priorities do not provide sufficient resources, Auto Scaling creates ECS instances by using the custom combinations that do not have specified priorities based on the specified orders of vSwitches and instance types.
        # 
        # *   Example: the specified order of vSwitches for your scaling group is vsw1 and vsw2 and the specified order of instance types in your scaling configuration is type1 and type 2. In addition, you use CustomPriorities to specify ["vsw2+type2", "vsw1+type2"]. In this example, the vsw2+type2 combination has the highest priority and the vsw2+type1 combination has the lowest priority. The vsw1+type2 combination has a higher priority than the vsw1+type1 combination.
        self.custom_priorities = custom_priorities
        # The data disks.
        self.data_disks = data_disks
        # The ID of the dedicated host cluster.
        self.dedicated_host_cluster_id = dedicated_host_cluster_id
        # The ID of the dedicated host on which the ECS instance is created. Preemptible instances are not supported by dedicated hosts. Therefore, if you specify DedicatedHostId, SpotStrategy and SpotPriceLimit are ignored.
        # 
        # You can call the DescribeDedicatedHosts operation to query the IDs of dedicated hosts.
        self.dedicated_host_id = dedicated_host_id
        # Indicates whether Release Protection is enabled for the ECS instances. You can specify this parameter to determine whether the ECS instances can be deleted by using the ECS console or calling the DeleteInstance operation. Valid values:
        # 
        # *   true: Release Protection is enabled for the ECS instances. You cannot delete the ECS instances by using the ECS console or calling the DeleteInstance operation.
        # *   false: Release Protection is disabled for the ECS instances. You can delete the ECS instances by using the ECS console or calling the DeleteInstance operation.
        # 
        # >  You can enable Release Protection for only pay-as-you-go instances to prevent unexpected instance deletion during scale-in events. The Release Protection feature does not affect normal scaling activities. In other words, an instance that meets the criteria of scale-in policies may be removed from a scaling group during a scale-in event even if you enabled Release Protection for the instance.
        self.deletion_protection = deletion_protection
        # The ID of the deployment set to which the Elastic Compute Service (ECS) instances belong.
        self.deployment_set_id = deployment_set_id
        # The hostname series of the ECS instances.
        self.host_name = host_name
        # The ID of the High Performance Computing (HPC) cluster to which the ECS instances belong.
        self.hpc_cluster_id = hpc_cluster_id
        # Indicates whether the access channel is enabled for instance metadata. Valid values:
        # 
        # *   enabled
        # *   disabled
        self.http_endpoint = http_endpoint
        # Indicates whether the security hardening mode (IMDSv2) is forcefully used to access instance metadata. Valid values:
        # 
        # *   optional: The security hardening mode IMDSv2 is not forcibly used.
        # *   required: The security hardening mode (IMDSv2) is forcibly used. After you set this parameter to required, you cannot access instance metadata in normal mode.
        self.http_tokens = http_tokens
        # The name of the image family. You can specify this parameter to obtain the latest available images in the current image family for instance creation. If you specify ImageId, you cannot specify `ImageFamily`.
        self.image_family = image_family
        # The ID of the image file that provides the image resource for Auto Scaling to create ECS instances.
        self.image_id = image_id
        # The name of the image file.
        self.image_name = image_name
        # Indicates whether the ecs-user username can be used to log on to an ECS instance created from the scaling configuration. Valid values:
        # 
        # *   true
        # *   false
        self.image_options_login_as_non_root = image_options_login_as_non_root
        # The image source. Valid values:
        # 
        # *   system: a public image provided by Alibaba Cloud
        # *   self: a custom image that you created
        # *   others: a shared image from another Alibaba Cloud account or a community image published by another Alibaba Cloud account
        # *   marketplace: an Alibaba Cloud Marketplace image
        self.image_owner_alias = image_owner_alias
        # The description of the ECS instances.
        self.instance_description = instance_description
        # The generation of the ECS instances.
        self.instance_generation = instance_generation
        # The naming series of the ECS instances.
        self.instance_name = instance_name
        # The intelligent configuration settings, which determine the available instance types.
        self.instance_pattern_infos = instance_pattern_infos
        # The instance types of the ECS instances.
        self.instance_type = instance_type
        # The ECS instance types.
        self.instance_types = instance_types
        # The billing method for network usage. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth. You are charged for the bandwidth that you specified by using InternetMaxBandwidthOut.
        # *   PayByTraffic: pay-by-traffic. You are charged for the actual traffic that you used. InternetMaxBandwidthOut specifies only the maximum available bandwidth.
        self.internet_charge_type = internet_charge_type
        # The maximum inbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_in = internet_max_bandwidth_in
        # The maximum outbound public bandwidth. Unit: Mbit/s.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Indicates whether the ECS instances are I/O optimized. Valid values:
        # 
        # *   none: The ECS instances are not I/O optimized.
        # *   optimized: The ECS instances are I/O optimized.
        self.io_optimized = io_optimized
        # The number of randomly generated IPv6 addresses that are allocated to the elastic network interface (ENI).
        self.ipv_6address_count = ipv_6address_count
        # The name of the key pair that is used to log on to an ECS instance created from the scaling configuration.
        self.key_pair_name = key_pair_name
        # The status of the scaling configuration in the scaling group. Valid values:
        # 
        # *   Active: The scaling configuration is active in the scaling group. Auto Scaling uses the scaling configuration that is in the Active state to create ECS instances during scale-out events.
        # *   Inactive: The scaling configuration is inactive in the scaling group. Scaling configurations that are in the Inactive state are still contained in the scaling group, but Auto Scaling does not use the inactive scaling configurations to create ECS instances during scale-out events.
        self.lifecycle_state = lifecycle_state
        # The weight of an ECS instance as a backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size. Unit: GiB.
        # 
        # You can specify CPU and Memory to define the range of instance types. For example, if you set CPU to 2 and Memory to 16, the instance types that have 2 vCPUs and 16 GiB are returned. If you specify CPU and Memory, Auto Scaling determines the available instance types based on factors such as I/O optimization requirements and zones and preferentially creates instances by using the lowest-priced instance type.
        # 
        # >  You can specify CPU and Memory to define instance types only when you set Scaling Policy to Cost Optimization and no instance type is specified in the scaling configuration.
        self.memory = memory
        # The ENIs.
        self.network_interfaces = network_interfaces
        # Indicates whether the password preconfigured in the image is used.
        self.password_inherit = password_inherit
        # Indicates whether a password is configured for the instance.
        self.password_setted = password_setted
        self.private_pool_options_id = private_pool_options_id
        self.private_pool_options_match_criteria = private_pool_options_match_criteria
        # The name of the Resource Access Management (RAM) role assumed by the ECS instances. This name is provided and maintained by RAM. You can call the ListRoles operation to query the available RAM roles.
        self.ram_role_name = ram_role_name
        # The ID of the resource group to which the ECS instances belong.
        self.resource_group_id = resource_group_id
        # The resource pools used for instance creation, which can be the public pool or a private pool associated with any active elasticity assurance or capacity reservation.
        # 
        # *   This parameter takes effect only when you create pay-as-you-go instances.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        self.scaling_group_id = scaling_group_id
        # >  This parameter is in invitational preview and is not available for use.
        self.scheduler_options = scheduler_options
        # Indicates whether Security Hardening is enabled. Valid values:
        # 
        # *   Active: Security Hardening is enabled. This value is applicable to only public images.
        # *   Deactive: Security Hardening is disabled. This value is applicable to all images.
        self.security_enhancement_strategy = security_enhancement_strategy
        # The ID of the security group to which the ECS instances belong. ECS instances that belong to the same security group can communicate with each other.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the ECS instances belong. ECS instances that belong to the same security group can communicate with each other.
        self.security_group_ids = security_group_ids
        self.security_options = security_options
        # The protection period of the preemptible instances. Unit: hours.
        self.spot_duration = spot_duration
        # The interruption event of the preemptible instances.
        self.spot_interruption_behavior = spot_interruption_behavior
        # The preemptible instances.
        self.spot_price_limits = spot_price_limits
        # The preemption policy that is applied to pay-as-you-go instances. Valid values:
        # 
        # *   NoSpot: The instances are created as regular pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are created as preemptible instances that have a user-defined maximum hourly price.
        # *   SpotAsPriceGo: The instances are preemptible instances for which the market price at the time of purchase is automatically used as the bid price.
        self.spot_strategy = spot_strategy
        # The ID of the storage set.
        self.storage_set_id = storage_set_id
        # The maximum number of partitions in the storage set. The value is an integer that is greater than or equal to 2.
        self.storage_set_partition_number = storage_set_partition_number
        # The ID of the automatic snapshot policy that is applied to the system disk.
        self.system_disk_auto_snapshot_policy_id = system_disk_auto_snapshot_policy_id
        # Indicates whether the Performance Burst feature is enabled for the system disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is available only when you set SystemDisk.Category to cloud_auto.
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The categories of the system disks. The values are sorted based on their priorities. The first value has the highest priority. If Auto Scaling cannot create instances by using the disk category of the highest priority, Auto Scaling creates instances by using the disk category of the next highest priority. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   cloud_essd: ESSD
        self.system_disk_categories = system_disk_categories
        # The category of the system disk. Valid values:
        # 
        # *   cloud: basic disk
        # *   cloud_efficiency: ultra disk
        # *   cloud_ssd: standard SSD
        # *   ephemeral_ssd: local SSD
        # *   cloud_essd: enterprise SSD (ESSD)
        # *   cloud_auto: ESSD AutoPL
        self.system_disk_category = system_disk_category
        # The description of the system disk.
        self.system_disk_description = system_disk_description
        # The encryption algorithm that is applied to the system disk. Valid values:
        # 
        # *   AES-256
        # *   SM4-128
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Indicates whether the system disk is encrypted. Valid values:
        # 
        # *   true
        # *   false
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key that is applied to the system disk.
        self.system_disk_kmskey_id = system_disk_kmskey_id
        # The name of the system disk.
        self.system_disk_name = system_disk_name
        # The performance level (PL) of the system disk that is an ESSD.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned IOPS of the system disk.
        # 
        # >  IOPS measures the number of read and write operations that an EBS device can process per second.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk. Unit: GiB.
        self.system_disk_size = system_disk_size
        # The tags.
        self.tags = tags
        # Indicates whether the ECS instance is created on a dedicated host. Valid values:
        # 
        # *   default: The ECS instance is created on a non-dedicated host.
        # *   host: The ECS instance is created on a dedicated host. If you do not specify DedicatedHostId, the system selects a dedicated host for the ECS instance.
        # 
        # Default value: default.
        self.tenancy = tenancy
        # The user data of the ECS instances.
        self.user_data = user_data
        # The weights of the instance types. The value of this parameter indicates the capacity of an instance of the specified instance type in the scaling group. A higher weight indicates that a smaller number of instances of the instance type are required to meet the expected capacity requirement.
        self.weighted_capacities = weighted_capacities
        # The ID of the zone in which the ECS instances are created. You can call the DescribeZones operation to query the zone IDs.
        self.zone_id = zone_id

    def validate(self):
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
        # The tag key of the ECS instance. You can specify up to 20 tags for each ECS instance.
        # 
        # The tag key cannot be an empty string. The tag key can be up to 128 characters in length. It cannot start with `acs:` or `aliyun` and cannot contain `http://` or `https://`.
        self.key = key
        # The tag value of the ECS instance. You can specify up to 20 tags for each ECS instance.
        # 
        # The tag value can be an empty string. The tag value can be up to 128 characters in length. It cannot start with `acs:` and cannot contain `http://` or `https://`.
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
        # The instance type of the preemptible instances.
        self.instance_type = instance_type
        # The price limit of the preemptible instances.
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
        # >  This parameter is in invitational preview and is not available for use.
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
        strategy: str = None,
    ):
        # The IDs of private pools. The ID of a private pool is the same as the ID of the elasticity assurance or capacity reservation that is associated with the private pool.
        self.private_pool_ids = private_pool_ids
        # The resource pool used for instance creation, which can be the public pool or a private pool associated with any active elasticity assurance or capacity reservation. Valid values:
        # 
        # *   PrivatePoolFirst: prioritizes private pools. When this option is set along with ResourcePoolOptions.PrivatePoolIds, the specified private pools are used first. If you leave ResourcePoolOptions.PrivatePoolIds empty or if the specified private pools lack sufficient capacity, the system will automatically use available open private pools instead. If no matching private pools are available, the system defaults to the public pool.
        # *   PrivatePoolOnly: uses only private pools. If you use this value, you must specify ResourcePoolOptions.PrivatePoolIds. If the specified private pools lack sufficient capacity, instance creation will fail.
        # *   None: uses no resource pools.
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

class DescribeScalingConfigurationsResponseBodyScalingConfigurationsNetworkInterfaces(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        ipv_6address_count: int = None,
        network_interface_traffic_mode: str = None,
        security_group_ids: List[str] = None,
    ):
        # The ENI type. Valid values:
        # 
        # *   Primary: the primary ENI
        # *   Secondary: the secondary ENI
        self.instance_type = instance_type
        # The number of randomly generated IPv6 addresses that are allocated to the primary ENI.
        self.ipv_6address_count = ipv_6address_count
        # The communication mode of the ENI. Valid values:
        # 
        # *   Standard: The TCP communication mode is used.
        # *   HighPerformance: The Elastic RDMA Interface (ERI) is enabled and the remote direct memory access (RDMA) communication mode is used.
        self.network_interface_traffic_mode = network_interface_traffic_mode
        # The IDs of the security groups to which the ENIs belong.
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
        # The architectures of instance types. Valid values:
        # 
        # *   X86: x86.
        # *   Heterogeneous: heterogeneous computing, such as GPU-accelerated or FPGA-accelerated.
        # *   BareMetal: ECS Bare Metal Instance.
        # *   Arm: Arm.
        self.architectures = architectures
        # Indicates whether burstable instance types are included. Valid values:
        # 
        # *   Exclude: Burstable instance types are not included.
        # *   Include: Burstable instance types are included.
        # *   Required: Only burstable instance types are included.
        self.burstable_performance = burstable_performance
        # The number of vCPUs of the instance type.
        self.cores = cores
        # The CPU architectures of the instance types. Valid values:
        # 
        # >  You can specify 1 to 2 CPU architectures.
        # 
        # *   x86
        # *   Arm
        self.cpu_architectures = cpu_architectures
        # The instance types that are excluded. You can use wildcard characters, such as an asterisk (\\*), to exclude an instance type or an instance family. Examples:
        # 
        # *   ecs.c6.large: The ecs.c6.large instance type is excluded.
        # *   ecs.c6.\\*: The c6 instance family is excluded.
        self.excluded_instance_types = excluded_instance_types
        # The GPU models.
        self.gpu_specs = gpu_specs
        # The categories of ECS instances. Valid values:
        # 
        # >  Up to 10 categories of ECS instances are supported.
        # 
        # *   General-purpose: general-purpose instance type.
        # *   Compute-optimized: compute-optimized instance type.
        # *   Memory-optimized: memory-optimized instance type.
        # *   Big data: big data instance type.
        # *   Local SSDs: instance type with local SSDs.
        # *   High Clock Speed: instance type with high clock speeds.
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
        # The level of the instance family.
        # 
        # *   EntryLevel: entry level (shared instance types). Instance types of this level are the most cost-effective but may not provide stable computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # *   EnterpriseLevel: enterprise level. Instance types of this level provide stable performance and dedicated resources, and are suitable for scenarios that require high stability. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # *   CreditEntryLevel: credit entry level (burstable instance types). CPU credits are used to ensure computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low but may fluctuate in specific cases. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The instance families that are queried. You can query 1 to 10 instance families in each call.
        self.instance_type_families = instance_type_families
        # The maximum hourly price for the pay-as-you-go or preemptible instances.
        self.max_price = max_price
        # The maximum number of vCPUs per instance type.
        # 
        # >  The value of MaximumCpuCoreCount cannot exceed four times the value of MinimumCpuCoreCount.
        self.maximum_cpu_core_count = maximum_cpu_core_count
        # The maximum number of GPUs per instance. The value must be a positive integer.
        self.maximum_gpu_amount = maximum_gpu_amount
        # The maximum memory size per instance. Unit: GiB.
        self.maximum_memory_size = maximum_memory_size
        # The memory size of the instance type. Unit: GiB.
        self.memory = memory
        # The baseline vCPU computing performance (overall baseline performance of all vCPUs) per t5 or t6 burstable instance.
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
        # The initial vCPU credits per t5 or t6 burstable instance.
        self.minimum_initial_credit = minimum_initial_credit
        # The minimum memory size per instance. Unit: GiB.
        self.minimum_memory_size = minimum_memory_size
        # The processor models of the instance types. You can specify 1 to 10 processor models.
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
        # The ID of the automatic snapshot policy that is applied to the data disk.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # Indicates whether the Performance Burst feature is enabled for the data disk. Valid values:
        # 
        # *   true
        # *   false
        # 
        # >  This parameter is available only when you set `DataDisk.Category` to `cloud_auto`.
        self.bursting_enabled = bursting_enabled
        # The categories of the data disks. The values are sorted based on their priorities. The first value has the highest priority. If Auto Scaling cannot create instances by using the disk category of the highest priority, Auto Scaling creates instances by using the disk category of the next highest priority. Valid values:
        # 
        # *   cloud: basic disk. DeleteWithInstance of a basic disk created along with the ECS instance is set to true.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   cloud_essd: ESSD.
        self.categories = categories
        # The category of the data disk. Valid values:
        # 
        # *   cloud: basic disk. DeleteWithInstance of a basic disk created along with the ECS instance is set to true.
        # *   cloud_efficiency: ultra disk.
        # *   cloud_ssd: standard SSD.
        # *   ephemeral_ssd: local SSD.
        # *   cloud_essd: ESSD.
        # *   cloud_auto: ESSD AutoPL.
        self.category = category
        # Indicates whether the data disk is released when the instance to which the data disk is attached is released. Valid values:
        # 
        # *   true
        # *   false
        self.delete_with_instance = delete_with_instance
        # The description of the data disk.
        self.description = description
        # The mount target of the data disk.
        self.device = device
        # The name of the data disk.
        self.disk_name = disk_name
        # Indicates whether the data disk is encrypted. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.encrypted = encrypted
        # The ID of the Key Management Service (KMS) key that is applied to the data disk.
        self.kmskey_id = kmskey_id
        # The PL of the data disk that is an ESSD.
        self.performance_level = performance_level
        # The provisioned IOPS of the data disk.
        # 
        # >  IOPS measures the number of read and write operations that an Elastic Block Storage (EBS) device can process per second.
        self.provisioned_iops = provisioned_iops
        # The size of the data disk. Unit: GB. Valid values:
        # 
        # *   5 to 2000 if you set Category to cloud.
        # *   20 to 32768 if you set Category to cloud_efficiency.
        # *   20 to 32768 if you set Category to cloud_ssd.
        # *   20 to 32768 if you set Category to cloud_essd.
        # *   5 to 800 if you set Category to ephemeral_ssd.
        self.size = size
        # The ID of the snapshot based on which the data disk is created.
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
        # The ECS instance type.
        self.instance_type = instance_type
        # The vSwitch ID.
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

