# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class DescribeEciScalingConfigurationsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        scaling_configurations: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurations] = None,
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
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurations()
                self.scaling_configurations.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurations(DaraModel):
    def __init__(
        self,
        acr_registry_infos: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        container_group_name: str = None,
        containers: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers] = None,
        cost_optimization: bool = None,
        cpu: float = None,
        cpu_options_core: int = None,
        cpu_options_threads_per_core: int = None,
        creation_time: str = None,
        data_cache_bucket: str = None,
        data_cache_bursting_enabled: bool = None,
        data_cache_pl: str = None,
        data_cache_provisioned_iops: int = None,
        description: str = None,
        dns_config_name_servers: List[str] = None,
        dns_config_options: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions] = None,
        dns_config_searches: List[str] = None,
        dns_policy: str = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        ephemeral_storage: int = None,
        gpu_driver_version: str = None,
        host_aliases: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases] = None,
        host_name: str = None,
        image_registry_credentials: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_containers: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers] = None,
        instance_family_level: str = None,
        instance_types: List[str] = None,
        ipv_6address_count: int = None,
        lifecycle_state: str = None,
        load_balancer_weight: int = None,
        memory: float = None,
        ntp_servers: List[str] = None,
        ram_role_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        restart_policy: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        scaling_group_id: str = None,
        security_context_sys_ctls: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls] = None,
        security_group_id: str = None,
        sls_enable: bool = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tags: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags] = None,
        termination_grace_period_seconds: int = None,
        volumes: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes] = None,
    ):
        # The information about the ACR Enterprise instance.
        self.acr_registry_infos = acr_registry_infos
        # The validity period. Unit: seconds.
        self.active_deadline_seconds = active_deadline_seconds
        # Specifies whether the automatic creation of an elastic IP address (EIP) and attaching it to the ECI instance is enabled.
        self.auto_create_eip = auto_create_eip
        # Specifies whether to automatically match an image cache.
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The name of the ECI instance, which is also the name of the pod.
        self.container_group_name = container_group_name
        # The list of containers included in the ECI instance.
        self.containers = containers
        # Specifies whether to enable cost optimization. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        self.cost_optimization = cost_optimization
        # The number of vCPUs for the instance.
        self.cpu = cpu
        # The number of physical CPU cores. Only specific instance types support custom settings. For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_core = cpu_options_core
        # The number of threads per core. Only specific instance types support custom settings. A value of 1 indicates that hyper-threading is disabled. For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        # The time when the scaling configuration was created. The time is displayed in UTC and follows the ISO 8601 standard in the YYYY-MM-DDTHH:mmZ format.
        self.creation_time = creation_time
        # The bucket for data caching.
        self.data_cache_bucket = data_cache_bucket
        # Specifies whether to enable the burst feature for the ESSD AutoPL cloud disk used for data caching. Valid values:
        # - true: Enabled.
        # - false: Disabled.
        # > For more information about ESSD AutoPL cloud disks, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_bursting_enabled = data_cache_bursting_enabled
        # The performance level of the cloud disk used for data caching. We recommend using ESSD (standard SSD). Valid values for the performance level of an ESSD (standard SSD):
        # 
        # - PL0: A single ESSD (standard SSD) can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD (standard SSD) can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD (standard SSD) can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD (standard SSD) can deliver up to 1,000,000 random read/write IOPS.
        # 
        # > For more information about ESSD (standard SSD), see [ESSD (standard SSD)](https://help.aliyun.com/document_detail/122389.html).
        self.data_cache_pl = data_cache_pl
        # The provisioned read/write IOPS of the ESSD AutoPL cloud disk used for data caching. Valid values: 0 to min{50000, 1000 × capacity - baseline performance}. The baseline performance is calculated by using the following formula: min{1800 + 50 × capacity, 50000}.
        # > For more information about ESSD AutoPL cloud disks, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_provisioned_iops = data_cache_provisioned_iops
        # This parameter is unavailable.
        self.description = description
        # The list of IP addresses of the DNS servers.
        self.dns_config_name_servers = dns_config_name_servers
        # The list of DNS configuration options. Each option consists of a name and an optional value.
        self.dns_config_options = dns_config_options
        # The list of DNS search domains.
        self.dns_config_searches = dns_config_searches
        # The DNS policy.
        self.dns_policy = dns_policy
        # The outbound bandwidth limit. Unit: bytes.
        self.egress_bandwidth = egress_bandwidth
        # The bandwidth of the EIP. Default value: 5 Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # The size of the ephemeral storage space. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The specified GPU driver version.
        self.gpu_driver_version = gpu_driver_version
        # The custom hostname mappings for a container in the instance.
        self.host_aliases = host_aliases
        # The hostname.
        self.host_name = host_name
        # The image registry information.
        self.image_registry_credentials = image_registry_credentials
        # The ID of the image cache.
        self.image_snapshot_id = image_snapshot_id
        # The inbound bandwidth limit. Unit: bytes.
        self.ingress_bandwidth = ingress_bandwidth
        # The list of init containers.
        self.init_containers = init_containers
        # The level of the instance family. This parameter is used to filter instance types that meet the requirements and takes effect only when `CostOptimization` is enabled. Valid values:
        # - EntryLevel: shared instance types. These instance types are more cost-effective but cannot guarantee stable computing performance. They are suitable for workloads with low CPU utilization. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # - EnterpriseLevel: enterprise-level instance types. These instance types provide stable performance and dedicated resources, and are suitable for workloads that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # - CreditEntryLevel: burstable instance types. These instance types use CPU credits to ensure computing performance and are suitable for workloads that have low CPU utilization but occasionally experience CPU usage spikes. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The specified ECS instance types. You can specify up to five instance types.
        self.instance_types = instance_types
        # The number of IPv6 addresses.
        self.ipv_6address_count = ipv_6address_count
        # The state of the scaling configuration in the scaling group. Valid values:
        # - Active: The scaling configuration is active. The scaling group uses active scaling configurations for the automatic creation of ECS instances.
        # - Inacitve: The scaling configuration is inactive. Inactive scaling configurations exist in the scaling group, but the scaling group does not use them for the automatic creation of ECS instances.
        self.lifecycle_state = lifecycle_state
        # The weight of the ECI instance when it serves as a backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size.
        # You can specify both CPU and Memory to define a range of instance types. For example, if you set CPU to 2 and Memory to 16, all instance types that have 2 vCPUs and 16 GiB of memory are matched. Auto Scaling determines the available instance types based on factors such as I/O optimization and zone, and creates the instance type that has the lowest price.
        # > This configuration takes effect only when the cost optimization mode is used and no instance types are specified in the scaling configuration.
        self.memory = memory
        # The NTP servers.
        self.ntp_servers = ntp_servers
        # The name of the instance RAM role. ECI and ECS share the same instance RAM role. For more information, see [Use an instance RAM role by calling API operations](https://help.aliyun.com/document_detail/61178.html).
        self.ram_role_name = ram_role_name
        # The region ID of the ECI instance.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The restart policy for the pod. Valid values:
        # - Never: The pod is not restarted.
        # - Always: The pod is always restarted.
        # - OnFailure: The pod is restarted upon failure.
        self.restart_policy = restart_policy
        # The ID of the scaling configuration.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration.
        self.scaling_configuration_name = scaling_configuration_name
        # The ID of the scaling group to which the scaling configuration belongs.
        self.scaling_group_id = scaling_group_id
        # The system info of the contextual security for the running instance.
        self.security_context_sys_ctls = security_context_sys_ctls
        # The ID of the security group to which the Elastic Container Instance (ECI) belongs. ECI instances in the same security group can access each other.
        self.security_group_id = security_group_id
        # This parameter is unavailable.
        self.sls_enable = sls_enable
        # The maximum hourly price for the spot instance.
        # This parameter is returned only when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The preemption policy for the instance. Valid values:
        # - NoSpot: regular pay-as-you-go instance
        # - SpotWithPriceLimit: spot instance with a maximum price
        # - SpotAsPriceGo: spot instance with a price automatically offered by the system based on the current market price
        self.spot_strategy = spot_strategy
        # The tag key-value pairs of the instance.
        self.tags = tags
        # The grace period for the program to handle operations before termination.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The data volume information.
        self.volumes = volumes

    def validate(self):
        if self.acr_registry_infos:
            for v1 in self.acr_registry_infos:
                 if v1:
                    v1.validate()
        if self.containers:
            for v1 in self.containers:
                 if v1:
                    v1.validate()
        if self.dns_config_options:
            for v1 in self.dns_config_options:
                 if v1:
                    v1.validate()
        if self.host_aliases:
            for v1 in self.host_aliases:
                 if v1:
                    v1.validate()
        if self.image_registry_credentials:
            for v1 in self.image_registry_credentials:
                 if v1:
                    v1.validate()
        if self.init_containers:
            for v1 in self.init_containers:
                 if v1:
                    v1.validate()
        if self.security_context_sys_ctls:
            for v1 in self.security_context_sys_ctls:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.volumes:
            for v1 in self.volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AcrRegistryInfos'] = []
        if self.acr_registry_infos is not None:
            for k1 in self.acr_registry_infos:
                result['AcrRegistryInfos'].append(k1.to_map() if k1 else None)

        if self.active_deadline_seconds is not None:
            result['ActiveDeadlineSeconds'] = self.active_deadline_seconds

        if self.auto_create_eip is not None:
            result['AutoCreateEip'] = self.auto_create_eip

        if self.auto_match_image_cache is not None:
            result['AutoMatchImageCache'] = self.auto_match_image_cache

        if self.container_group_name is not None:
            result['ContainerGroupName'] = self.container_group_name

        result['Containers'] = []
        if self.containers is not None:
            for k1 in self.containers:
                result['Containers'].append(k1.to_map() if k1 else None)

        if self.cost_optimization is not None:
            result['CostOptimization'] = self.cost_optimization

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core

        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_cache_bucket is not None:
            result['DataCacheBucket'] = self.data_cache_bucket

        if self.data_cache_bursting_enabled is not None:
            result['DataCacheBurstingEnabled'] = self.data_cache_bursting_enabled

        if self.data_cache_pl is not None:
            result['DataCachePL'] = self.data_cache_pl

        if self.data_cache_provisioned_iops is not None:
            result['DataCacheProvisionedIops'] = self.data_cache_provisioned_iops

        if self.description is not None:
            result['Description'] = self.description

        if self.dns_config_name_servers is not None:
            result['DnsConfigNameServers'] = self.dns_config_name_servers

        result['DnsConfigOptions'] = []
        if self.dns_config_options is not None:
            for k1 in self.dns_config_options:
                result['DnsConfigOptions'].append(k1.to_map() if k1 else None)

        if self.dns_config_searches is not None:
            result['DnsConfigSearches'] = self.dns_config_searches

        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy

        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth

        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.ephemeral_storage is not None:
            result['EphemeralStorage'] = self.ephemeral_storage

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        result['HostAliases'] = []
        if self.host_aliases is not None:
            for k1 in self.host_aliases:
                result['HostAliases'].append(k1.to_map() if k1 else None)

        if self.host_name is not None:
            result['HostName'] = self.host_name

        result['ImageRegistryCredentials'] = []
        if self.image_registry_credentials is not None:
            for k1 in self.image_registry_credentials:
                result['ImageRegistryCredentials'].append(k1.to_map() if k1 else None)

        if self.image_snapshot_id is not None:
            result['ImageSnapshotId'] = self.image_snapshot_id

        if self.ingress_bandwidth is not None:
            result['IngressBandwidth'] = self.ingress_bandwidth

        result['InitContainers'] = []
        if self.init_containers is not None:
            for k1 in self.init_containers:
                result['InitContainers'].append(k1.to_map() if k1 else None)

        if self.instance_family_level is not None:
            result['InstanceFamilyLevel'] = self.instance_family_level

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.ipv_6address_count is not None:
            result['Ipv6AddressCount'] = self.ipv_6address_count

        if self.lifecycle_state is not None:
            result['LifecycleState'] = self.lifecycle_state

        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.ntp_servers is not None:
            result['NtpServers'] = self.ntp_servers

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name

        if self.scaling_group_id is not None:
            result['ScalingGroupId'] = self.scaling_group_id

        result['SecurityContextSysCtls'] = []
        if self.security_context_sys_ctls is not None:
            for k1 in self.security_context_sys_ctls:
                result['SecurityContextSysCtls'].append(k1.to_map() if k1 else None)

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.sls_enable is not None:
            result['SlsEnable'] = self.sls_enable

        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.spot_strategy is not None:
            result['SpotStrategy'] = self.spot_strategy

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.termination_grace_period_seconds is not None:
            result['TerminationGracePeriodSeconds'] = self.termination_grace_period_seconds

        result['Volumes'] = []
        if self.volumes is not None:
            for k1 in self.volumes:
                result['Volumes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.acr_registry_infos = []
        if m.get('AcrRegistryInfos') is not None:
            for k1 in m.get('AcrRegistryInfos'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos()
                self.acr_registry_infos.append(temp_model.from_map(k1))

        if m.get('ActiveDeadlineSeconds') is not None:
            self.active_deadline_seconds = m.get('ActiveDeadlineSeconds')

        if m.get('AutoCreateEip') is not None:
            self.auto_create_eip = m.get('AutoCreateEip')

        if m.get('AutoMatchImageCache') is not None:
            self.auto_match_image_cache = m.get('AutoMatchImageCache')

        if m.get('ContainerGroupName') is not None:
            self.container_group_name = m.get('ContainerGroupName')

        self.containers = []
        if m.get('Containers') is not None:
            for k1 in m.get('Containers'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('CostOptimization') is not None:
            self.cost_optimization = m.get('CostOptimization')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')

        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataCacheBucket') is not None:
            self.data_cache_bucket = m.get('DataCacheBucket')

        if m.get('DataCacheBurstingEnabled') is not None:
            self.data_cache_bursting_enabled = m.get('DataCacheBurstingEnabled')

        if m.get('DataCachePL') is not None:
            self.data_cache_pl = m.get('DataCachePL')

        if m.get('DataCacheProvisionedIops') is not None:
            self.data_cache_provisioned_iops = m.get('DataCacheProvisionedIops')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DnsConfigNameServers') is not None:
            self.dns_config_name_servers = m.get('DnsConfigNameServers')

        self.dns_config_options = []
        if m.get('DnsConfigOptions') is not None:
            for k1 in m.get('DnsConfigOptions'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions()
                self.dns_config_options.append(temp_model.from_map(k1))

        if m.get('DnsConfigSearches') is not None:
            self.dns_config_searches = m.get('DnsConfigSearches')

        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')

        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')

        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k1 in m.get('HostAliases'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases()
                self.host_aliases.append(temp_model.from_map(k1))

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k1 in m.get('ImageRegistryCredentials'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k1))

        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')

        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')

        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k1 in m.get('InitContainers'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers()
                self.init_containers.append(temp_model.from_map(k1))

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('LifecycleState') is not None:
            self.lifecycle_state = m.get('LifecycleState')

        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NtpServers') is not None:
            self.ntp_servers = m.get('NtpServers')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        if m.get('ScalingGroupId') is not None:
            self.scaling_group_id = m.get('ScalingGroupId')

        self.security_context_sys_ctls = []
        if m.get('SecurityContextSysCtls') is not None:
            for k1 in m.get('SecurityContextSysCtls'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls()
                self.security_context_sys_ctls.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SlsEnable') is not None:
            self.sls_enable = m.get('SlsEnable')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        self.volumes = []
        if m.get('Volumes') is not None:
            for k1 in m.get('Volumes'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes()
                self.volumes.append(temp_model.from_map(k1))

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumes(DaraModel):
    def __init__(
        self,
        config_file_volume_config_file_to_paths: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths] = None,
        config_file_volume_default_mode: int = None,
        disk_volume_disk_id: str = None,
        disk_volume_disk_size: int = None,
        disk_volume_fs_type: str = None,
        empty_dir_volume_medium: str = None,
        empty_dir_volume_size_limit: str = None,
        flex_volume_driver: str = None,
        flex_volume_fs_type: str = None,
        flex_volume_options: str = None,
        host_path_volume_path: str = None,
        host_path_volume_type: str = None,
        nfsvolume_path: str = None,
        nfsvolume_read_only: bool = None,
        nfsvolume_server: str = None,
        name: str = None,
        type: str = None,
    ):
        # The list of configuration file paths.
        self.config_file_volume_config_file_to_paths = config_file_volume_config_file_to_paths
        # The default permissions of the ConfigFileVolume.
        self.config_file_volume_default_mode = config_file_volume_default_mode
        # The size of the disk volume. Unit: GiB.
        self.disk_volume_disk_id = disk_volume_disk_id
        # The size of the disk volume. Unit: GiB.
        self.disk_volume_disk_size = disk_volume_disk_size
        # The file system type of the disk volume.
        self.disk_volume_fs_type = disk_volume_fs_type
        # The storage medium of the EmptyDirVolume. The default value is empty, which indicates that the node file system is used. A value of memory indicates that memory is used.
        self.empty_dir_volume_medium = empty_dir_volume_medium
        # The size of the EmptyDir data volume.
        self.empty_dir_volume_size_limit = empty_dir_volume_size_limit
        # The name of the driver used for FlexVolume.
        self.flex_volume_driver = flex_volume_driver
        # The file system type to be mounted. The default value depends on the script of the FlexVolume.
        self.flex_volume_fs_type = flex_volume_fs_type
        # The list of options for the FlexVolume object. The options are passed in JSON format as key-value pairs.
        # For example, when you mount a cloud disk by using FlexVolume, the options are in the following format: `{"volumeId":"d-2zehdahrwoa7srg****","performanceLevel": "PL2"}`.
        self.flex_volume_options = flex_volume_options
        # The directory path of the HostPath volume on the host.
        self.host_path_volume_path = host_path_volume_path
        # The type of the HostPath volume.
        self.host_path_volume_type = host_path_volume_type
        # The path of the NFS volume.
        self.nfsvolume_path = nfsvolume_path
        # Specifies whether the NFS volume is read-only.
        # 
        # Default value: false.
        self.nfsvolume_read_only = nfsvolume_read_only
        # The address of the NFS server.
        self.nfsvolume_server = nfsvolume_server
        # The name of the data volume.
        self.name = name
        # The data volume type. Valid values:
        # - EmptyDirVolume.
        # - NFSVolume.
        # - ConfigFileVolume.
        # - FlexVolume.
        self.type = type

    def validate(self):
        if self.config_file_volume_config_file_to_paths:
            for v1 in self.config_file_volume_config_file_to_paths:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ConfigFileVolumeConfigFileToPaths'] = []
        if self.config_file_volume_config_file_to_paths is not None:
            for k1 in self.config_file_volume_config_file_to_paths:
                result['ConfigFileVolumeConfigFileToPaths'].append(k1.to_map() if k1 else None)

        if self.config_file_volume_default_mode is not None:
            result['ConfigFileVolumeDefaultMode'] = self.config_file_volume_default_mode

        if self.disk_volume_disk_id is not None:
            result['DiskVolumeDiskId'] = self.disk_volume_disk_id

        if self.disk_volume_disk_size is not None:
            result['DiskVolumeDiskSize'] = self.disk_volume_disk_size

        if self.disk_volume_fs_type is not None:
            result['DiskVolumeFsType'] = self.disk_volume_fs_type

        if self.empty_dir_volume_medium is not None:
            result['EmptyDirVolumeMedium'] = self.empty_dir_volume_medium

        if self.empty_dir_volume_size_limit is not None:
            result['EmptyDirVolumeSizeLimit'] = self.empty_dir_volume_size_limit

        if self.flex_volume_driver is not None:
            result['FlexVolumeDriver'] = self.flex_volume_driver

        if self.flex_volume_fs_type is not None:
            result['FlexVolumeFsType'] = self.flex_volume_fs_type

        if self.flex_volume_options is not None:
            result['FlexVolumeOptions'] = self.flex_volume_options

        if self.host_path_volume_path is not None:
            result['HostPathVolumePath'] = self.host_path_volume_path

        if self.host_path_volume_type is not None:
            result['HostPathVolumeType'] = self.host_path_volume_type

        if self.nfsvolume_path is not None:
            result['NFSVolumePath'] = self.nfsvolume_path

        if self.nfsvolume_read_only is not None:
            result['NFSVolumeReadOnly'] = self.nfsvolume_read_only

        if self.nfsvolume_server is not None:
            result['NFSVolumeServer'] = self.nfsvolume_server

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.config_file_volume_config_file_to_paths = []
        if m.get('ConfigFileVolumeConfigFileToPaths') is not None:
            for k1 in m.get('ConfigFileVolumeConfigFileToPaths'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths()
                self.config_file_volume_config_file_to_paths.append(temp_model.from_map(k1))

        if m.get('ConfigFileVolumeDefaultMode') is not None:
            self.config_file_volume_default_mode = m.get('ConfigFileVolumeDefaultMode')

        if m.get('DiskVolumeDiskId') is not None:
            self.disk_volume_disk_id = m.get('DiskVolumeDiskId')

        if m.get('DiskVolumeDiskSize') is not None:
            self.disk_volume_disk_size = m.get('DiskVolumeDiskSize')

        if m.get('DiskVolumeFsType') is not None:
            self.disk_volume_fs_type = m.get('DiskVolumeFsType')

        if m.get('EmptyDirVolumeMedium') is not None:
            self.empty_dir_volume_medium = m.get('EmptyDirVolumeMedium')

        if m.get('EmptyDirVolumeSizeLimit') is not None:
            self.empty_dir_volume_size_limit = m.get('EmptyDirVolumeSizeLimit')

        if m.get('FlexVolumeDriver') is not None:
            self.flex_volume_driver = m.get('FlexVolumeDriver')

        if m.get('FlexVolumeFsType') is not None:
            self.flex_volume_fs_type = m.get('FlexVolumeFsType')

        if m.get('FlexVolumeOptions') is not None:
            self.flex_volume_options = m.get('FlexVolumeOptions')

        if m.get('HostPathVolumePath') is not None:
            self.host_path_volume_path = m.get('HostPathVolumePath')

        if m.get('HostPathVolumeType') is not None:
            self.host_path_volume_type = m.get('HostPathVolumeType')

        if m.get('NFSVolumePath') is not None:
            self.nfsvolume_path = m.get('NFSVolumePath')

        if m.get('NFSVolumeReadOnly') is not None:
            self.nfsvolume_read_only = m.get('NFSVolumeReadOnly')

        if m.get('NFSVolumeServer') is not None:
            self.nfsvolume_server = m.get('NFSVolumeServer')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsVolumesConfigFileVolumeConfigFileToPaths(DaraModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        # The content of the configuration file (32 KB).
        self.content = content
        # The directory permissions of the ConfigFileVolume.
        self.mode = mode
        # The relative file path.
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsSecurityContextSysCtls(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the system control parameter.
        self.name = name
        # The variable value of the contextual security for the running instance.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainers(DaraModel):
    def __init__(
        self,
        cpu: float = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        init_container_args: List[str] = None,
        init_container_commands: List[str] = None,
        init_container_environment_vars: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars] = None,
        init_container_ports: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts] = None,
        init_container_volume_mounts: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts] = None,
        memory: float = None,
        name: str = None,
        security_context_capability_adds: List[str] = None,
        security_context_read_only_root_filesystem: bool = None,
        security_context_run_as_user: str = None,
        working_dir: str = None,
    ):
        # The CPU size.
        self.cpu = cpu
        # The number of GPUs used by the container.
        self.gpu = gpu
        # The image used by the container.
        self.image = image
        # The image pull policy.
        self.image_pull_policy = image_pull_policy
        # The startup arguments for the container.
        self.init_container_args = init_container_args
        # The startup commands for the container.
        self.init_container_commands = init_container_commands
        # The information about the environment variable.
        self.init_container_environment_vars = init_container_environment_vars
        # The collection of port information for the init container.
        self.init_container_ports = init_container_ports
        # The data volume mounts.
        self.init_container_volume_mounts = init_container_volume_mounts
        # The memory size.
        self.memory = memory
        # The name of the container.
        self.name = name
        # The specific permissions granted to processes in the container. Currently, only NET_ADMIN and NET_RAW are supported.
        # 
        # > By default, NET_RAW is not supported. To use NET_RAW, submit a ticket.
        self.security_context_capability_adds = security_context_capability_adds
        # Specifies whether the root file system where the container runs is read-only. Currently, only true is supported.
        self.security_context_read_only_root_filesystem = security_context_read_only_root_filesystem
        # The user ID used to run the container.
        self.security_context_run_as_user = security_context_run_as_user
        # The working directory.
        self.working_dir = working_dir

    def validate(self):
        if self.init_container_environment_vars:
            for v1 in self.init_container_environment_vars:
                 if v1:
                    v1.validate()
        if self.init_container_ports:
            for v1 in self.init_container_ports:
                 if v1:
                    v1.validate()
        if self.init_container_volume_mounts:
            for v1 in self.init_container_volume_mounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.image is not None:
            result['Image'] = self.image

        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy

        if self.init_container_args is not None:
            result['InitContainerArgs'] = self.init_container_args

        if self.init_container_commands is not None:
            result['InitContainerCommands'] = self.init_container_commands

        result['InitContainerEnvironmentVars'] = []
        if self.init_container_environment_vars is not None:
            for k1 in self.init_container_environment_vars:
                result['InitContainerEnvironmentVars'].append(k1.to_map() if k1 else None)

        result['InitContainerPorts'] = []
        if self.init_container_ports is not None:
            for k1 in self.init_container_ports:
                result['InitContainerPorts'].append(k1.to_map() if k1 else None)

        result['InitContainerVolumeMounts'] = []
        if self.init_container_volume_mounts is not None:
            for k1 in self.init_container_volume_mounts:
                result['InitContainerVolumeMounts'].append(k1.to_map() if k1 else None)

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        if self.security_context_capability_adds is not None:
            result['SecurityContextCapabilityAdds'] = self.security_context_capability_adds

        if self.security_context_read_only_root_filesystem is not None:
            result['SecurityContextReadOnlyRootFilesystem'] = self.security_context_read_only_root_filesystem

        if self.security_context_run_as_user is not None:
            result['SecurityContextRunAsUser'] = self.security_context_run_as_user

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')

        if m.get('InitContainerArgs') is not None:
            self.init_container_args = m.get('InitContainerArgs')

        if m.get('InitContainerCommands') is not None:
            self.init_container_commands = m.get('InitContainerCommands')

        self.init_container_environment_vars = []
        if m.get('InitContainerEnvironmentVars') is not None:
            for k1 in m.get('InitContainerEnvironmentVars'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars()
                self.init_container_environment_vars.append(temp_model.from_map(k1))

        self.init_container_ports = []
        if m.get('InitContainerPorts') is not None:
            for k1 in m.get('InitContainerPorts'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts()
                self.init_container_ports.append(temp_model.from_map(k1))

        self.init_container_volume_mounts = []
        if m.get('InitContainerVolumeMounts') is not None:
            for k1 in m.get('InitContainerVolumeMounts'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts()
                self.init_container_volume_mounts.append(temp_model.from_map(k1))

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SecurityContextCapabilityAdds') is not None:
            self.security_context_capability_adds = m.get('SecurityContextCapabilityAdds')

        if m.get('SecurityContextReadOnlyRootFilesystem') is not None:
            self.security_context_read_only_root_filesystem = m.get('SecurityContextReadOnlyRootFilesystem')

        if m.get('SecurityContextRunAsUser') is not None:
            self.security_context_run_as_user = m.get('SecurityContextRunAsUser')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerVolumeMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The mount directory. The content in the mount directory of the container is directly overwritten by the content of the volume. Use this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings for the data volume. Mount propagation allows volumes mounted by a container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # - None: The volume is not aware of any subsequent mount operations performed on the volume or its subdirectories.
        # - HostToCotainer: The volume is aware of subsequent mount operations performed on the volume or its subdirectories.
        # - Bidirectional: Similar to HostToCotainer, the volume is aware of mount operations. In addition, the volume is propagated back to the host and to all containers of all pods that use the same volume.
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the mounted data volume.
        self.name = name
        # Specifies whether the mount path is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The subdirectory in the data volume. This allows a pod to mount different directories in the same volume to different directories in the container.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation

        if self.name is not None:
            result['Name'] = self.name

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.sub_path is not None:
            result['SubPath'] = self.sub_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type. Valid values:
        # 
        # - TCP.
        # - UDP.
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsInitContainersInitContainerEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        # This parameter is unavailable.
        self.field_ref_field_path = field_ref_field_path
        # The name of the environment variable.
        self.key = key
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsImageRegistryCredentials(DaraModel):
    def __init__(
        self,
        password: str = None,
        server: str = None,
        user_name: str = None,
    ):
        # The password for the image registry.
        self.password = password
        # The address of the image registry.
        self.server = server
        # The username for the image registry.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['Password'] = self.password

        if self.server is not None:
            result['Server'] = self.server

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsHostAliases(DaraModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        # The hostnames to add.
        self.hostnames = hostnames
        # The IP address to add.
        self.ip = ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hostnames is not None:
            result['Hostnames'] = self.hostnames

        if self.ip is not None:
            result['Ip'] = self.ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hostnames') is not None:
            self.hostnames = m.get('Hostnames')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsDnsConfigOptions(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the option.
        self.name = name
        # The value of the option.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainers(DaraModel):
    def __init__(
        self,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars] = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        lifecycle_post_start_handler_execs: List[str] = None,
        lifecycle_post_start_handler_http_get_host: str = None,
        lifecycle_post_start_handler_http_get_path: str = None,
        lifecycle_post_start_handler_http_get_port: int = None,
        lifecycle_post_start_handler_http_get_scheme: str = None,
        lifecycle_post_start_handler_tcp_socket_host: str = None,
        lifecycle_post_start_handler_tcp_socket_port: int = None,
        lifecycle_pre_stop_handler_execs: List[str] = None,
        lifecycle_pre_stop_handler_http_get_host: str = None,
        lifecycle_pre_stop_handler_http_get_path: str = None,
        lifecycle_pre_stop_handler_http_get_port: int = None,
        lifecycle_pre_stop_handler_http_get_scheme: str = None,
        lifecycle_pre_stop_handler_tcp_socket_host: str = None,
        lifecycle_pre_stop_handler_tcp_socket_port: int = None,
        liveness_probe_exec_commands: List[str] = None,
        liveness_probe_failure_threshold: int = None,
        liveness_probe_http_get_path: str = None,
        liveness_probe_http_get_port: int = None,
        liveness_probe_http_get_scheme: str = None,
        liveness_probe_initial_delay_seconds: int = None,
        liveness_probe_period_seconds: int = None,
        liveness_probe_success_threshold: int = None,
        liveness_probe_tcp_socket_port: int = None,
        liveness_probe_timeout_seconds: int = None,
        memory: float = None,
        name: str = None,
        ports: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts] = None,
        readiness_probe_exec_commands: List[str] = None,
        readiness_probe_failure_threshold: int = None,
        readiness_probe_http_get_path: str = None,
        readiness_probe_http_get_port: int = None,
        readiness_probe_http_get_scheme: str = None,
        readiness_probe_initial_delay_seconds: int = None,
        readiness_probe_period_seconds: int = None,
        readiness_probe_success_threshold: int = None,
        readiness_probe_tcp_socket_port: int = None,
        readiness_probe_timeout_seconds: int = None,
        security_context_capability_adds: List[str] = None,
        security_context_read_only_root_filesystem: bool = None,
        security_context_run_as_user: int = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        # The list of arguments for the container startup commands. A maximum of 10 arguments can be specified.
        self.args = args
        # The list of startup commands for the container. A maximum of 20 commands can be specified. Each command can contain up to 256 characters.
        self.commands = commands
        # The number of vCPUs for the container.
        self.cpu = cpu
        # The list of environment variables.
        self.environment_vars = environment_vars
        # The number of GPUs.
        self.gpu = gpu
        # The container image.
        self.image = image
        # The image pull policy. Valid values:
        # - Alway: The image is always pulled.
        # - IfNotPresent: The image is pulled on demand. The local image is used first. If no local image is available, the image is pulled.
        # - Never: The image is never pulled. The local image is used.
        self.image_pull_policy = image_pull_policy
        # The command executed in the container when the postStart callback function is configured by using the command line.
        self.lifecycle_post_start_handler_execs = lifecycle_post_start_handler_execs
        # The host address that receives the HTTP GET request when the postStart callback function is configured by using an HTTP request.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        # The path checked by the HTTP GET request when the postStart callback function is configured by using an HTTP request.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        # The port number checked by the HTTP GET request when the postStart callback function is configured by using an HTTP request.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        # The protocol type used for the HTTP GET request when the postStart callback function is configured by using an HTTP request.
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        # The host address checked by the TCP socket when the postStart callback function is configured by using a TCP socket.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        # The port checked by the TCP socket when the postStart callback function is configured by using a TCP socket.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        # The command executed in the container when the preStop callback function is configured by using the command line.
        self.lifecycle_pre_stop_handler_execs = lifecycle_pre_stop_handler_execs
        # The host address that receives the HTTP GET request when the preStop callback function is configured by using an HTTP request.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        # The path checked by the HTTP GET request when the preStop callback function is configured by using an HTTP request.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        # The port number checked by the HTTP GET request when the preStop callback function is configured by using an HTTP request.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        # The protocol type used for the HTTP GET request when the preStop callback function is configured by using an HTTP request.
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        # The host address checked by the TCP socket when the preStop callback function is configured by using a TCP socket.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        # The port checked by the TCP socket when the preStop callback function is configured by using a TCP socket.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        # The list of commands executed in the container for command-line-based health checks.
        self.liveness_probe_exec_commands = liveness_probe_exec_commands
        # The minimum consecutive failures for the readiness probe to be considered failed after having succeeded.
        # Default value: 3.
        self.liveness_probe_failure_threshold = liveness_probe_failure_threshold
        # The path for the HTTP GET readiness probe.
        self.liveness_probe_http_get_path = liveness_probe_http_get_path
        # The port for the HTTP GET liveness probe.
        self.liveness_probe_http_get_port = liveness_probe_http_get_port
        # The protocol type for the HTTP GET request when HTTP requests are used for health checks. Valid values:
        # - HTTP
        # - HTTPS
        self.liveness_probe_http_get_scheme = liveness_probe_http_get_scheme
        # The delay before the readiness probe is initiated after the container starts.
        self.liveness_probe_initial_delay_seconds = liveness_probe_initial_delay_seconds
        # The execution period of the liveness probe. Default value: 10 seconds. Minimum value: 1 second.
        self.liveness_probe_period_seconds = liveness_probe_period_seconds
        # The minimum consecutive successes for the readiness probe to be considered successful after having failed. Default value: 1. The current value must be 1.
        self.liveness_probe_success_threshold = liveness_probe_success_threshold
        # The port number for the TCP socket liveness probe.
        self.liveness_probe_tcp_socket_port = liveness_probe_tcp_socket_port
        # The timeout period for the liveness probe. Default value: 1 second. Minimum value: 1 second.
        self.liveness_probe_timeout_seconds = liveness_probe_timeout_seconds
        # The memory size of the container.
        self.memory = memory
        # The custom name of the container.
        self.name = name
        # The list of exposed ports and protocols.
        self.ports = ports
        # The list of commands executed in the container for command-line-based health checks.
        self.readiness_probe_exec_commands = readiness_probe_exec_commands
        # The minimum consecutive failures for the readiness probe to be considered failed after having succeeded.
        # Default value: 3.
        self.readiness_probe_failure_threshold = readiness_probe_failure_threshold
        # The path for the HTTP GET readiness probe.
        self.readiness_probe_http_get_path = readiness_probe_http_get_path
        # The path for the HTTP GET readiness probe.
        self.readiness_probe_http_get_port = readiness_probe_http_get_port
        # The protocol type for the HTTP GET request when HTTP requests are used for health checks. Valid values:
        # - HTTP
        # - HTTPS
        self.readiness_probe_http_get_scheme = readiness_probe_http_get_scheme
        # The delay before the readiness probe is initiated after the container starts.
        self.readiness_probe_initial_delay_seconds = readiness_probe_initial_delay_seconds
        # The execution period of the readiness probe. Default value: 10 seconds. Minimum value: 1 second.
        self.readiness_probe_period_seconds = readiness_probe_period_seconds
        # The minimum consecutive successes for the readiness probe to be considered successful after having failed. Default value: 1. The current value must be 1.
        self.readiness_probe_success_threshold = readiness_probe_success_threshold
        # The port number for the TCP socket liveness probe.
        self.readiness_probe_tcp_socket_port = readiness_probe_tcp_socket_port
        # The timeout period for the readiness probe. Default value: 1 second. Minimum value: 1 second.
        self.readiness_probe_timeout_seconds = readiness_probe_timeout_seconds
        # The specific permissions granted to processes in the container. Currently, only NET_ADMIN and NET_RAW are supported.
        # 
        # > By default, NET_RAW is not supported. To use NET_RAW, submit a ticket.
        self.security_context_capability_adds = security_context_capability_adds
        # Specifies whether the root file system is read-only. Only true is supported.
        self.security_context_read_only_root_filesystem = security_context_read_only_root_filesystem
        # The UID used to run the entrypoint of the container process.
        self.security_context_run_as_user = security_context_run_as_user
        # Specifies whether to allocate a buffer for standard input during container runtime. If this parameter is not set, reading from standard input in the container results in an EOF. Default value: false.
        self.stdin = stdin
        # Specifies whether the standard input stream remains in the enabling status across multiple attached sessions when standard input is set to true.
        # 
        # If StdinOnce is set to true, standard input is opened when the container starts, remains empty until the first client attaches to it, and then stays in the enabling status to accept data until the client connection is disconnected. At this point, standard input is shutdown and remains shutdown until the container is restarted.
        self.stdin_once = stdin_once
        # Specifies whether to enable interaction. Valid values:
        # - true: enabled
        # - false: disabled
        # For example, if Command is set to /bin/bash, you must set this parameter to true.
        # Default value: false.
        self.tty = tty
        # The list of volume mounts.
        self.volume_mounts = volume_mounts
        # The working directory in the container.
        self.working_dir = working_dir

    def validate(self):
        if self.environment_vars:
            for v1 in self.environment_vars:
                 if v1:
                    v1.validate()
        if self.ports:
            for v1 in self.ports:
                 if v1:
                    v1.validate()
        if self.volume_mounts:
            for v1 in self.volume_mounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.args is not None:
            result['Args'] = self.args

        if self.commands is not None:
            result['Commands'] = self.commands

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.image is not None:
            result['Image'] = self.image

        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy

        if self.lifecycle_post_start_handler_execs is not None:
            result['LifecyclePostStartHandlerExecs'] = self.lifecycle_post_start_handler_execs

        if self.lifecycle_post_start_handler_http_get_host is not None:
            result['LifecyclePostStartHandlerHttpGetHost'] = self.lifecycle_post_start_handler_http_get_host

        if self.lifecycle_post_start_handler_http_get_path is not None:
            result['LifecyclePostStartHandlerHttpGetPath'] = self.lifecycle_post_start_handler_http_get_path

        if self.lifecycle_post_start_handler_http_get_port is not None:
            result['LifecyclePostStartHandlerHttpGetPort'] = self.lifecycle_post_start_handler_http_get_port

        if self.lifecycle_post_start_handler_http_get_scheme is not None:
            result['LifecyclePostStartHandlerHttpGetScheme'] = self.lifecycle_post_start_handler_http_get_scheme

        if self.lifecycle_post_start_handler_tcp_socket_host is not None:
            result['LifecyclePostStartHandlerTcpSocketHost'] = self.lifecycle_post_start_handler_tcp_socket_host

        if self.lifecycle_post_start_handler_tcp_socket_port is not None:
            result['LifecyclePostStartHandlerTcpSocketPort'] = self.lifecycle_post_start_handler_tcp_socket_port

        if self.lifecycle_pre_stop_handler_execs is not None:
            result['LifecyclePreStopHandlerExecs'] = self.lifecycle_pre_stop_handler_execs

        if self.lifecycle_pre_stop_handler_http_get_host is not None:
            result['LifecyclePreStopHandlerHttpGetHost'] = self.lifecycle_pre_stop_handler_http_get_host

        if self.lifecycle_pre_stop_handler_http_get_path is not None:
            result['LifecyclePreStopHandlerHttpGetPath'] = self.lifecycle_pre_stop_handler_http_get_path

        if self.lifecycle_pre_stop_handler_http_get_port is not None:
            result['LifecyclePreStopHandlerHttpGetPort'] = self.lifecycle_pre_stop_handler_http_get_port

        if self.lifecycle_pre_stop_handler_http_get_scheme is not None:
            result['LifecyclePreStopHandlerHttpGetScheme'] = self.lifecycle_pre_stop_handler_http_get_scheme

        if self.lifecycle_pre_stop_handler_tcp_socket_host is not None:
            result['LifecyclePreStopHandlerTcpSocketHost'] = self.lifecycle_pre_stop_handler_tcp_socket_host

        if self.lifecycle_pre_stop_handler_tcp_socket_port is not None:
            result['LifecyclePreStopHandlerTcpSocketPort'] = self.lifecycle_pre_stop_handler_tcp_socket_port

        if self.liveness_probe_exec_commands is not None:
            result['LivenessProbeExecCommands'] = self.liveness_probe_exec_commands

        if self.liveness_probe_failure_threshold is not None:
            result['LivenessProbeFailureThreshold'] = self.liveness_probe_failure_threshold

        if self.liveness_probe_http_get_path is not None:
            result['LivenessProbeHttpGetPath'] = self.liveness_probe_http_get_path

        if self.liveness_probe_http_get_port is not None:
            result['LivenessProbeHttpGetPort'] = self.liveness_probe_http_get_port

        if self.liveness_probe_http_get_scheme is not None:
            result['LivenessProbeHttpGetScheme'] = self.liveness_probe_http_get_scheme

        if self.liveness_probe_initial_delay_seconds is not None:
            result['LivenessProbeInitialDelaySeconds'] = self.liveness_probe_initial_delay_seconds

        if self.liveness_probe_period_seconds is not None:
            result['LivenessProbePeriodSeconds'] = self.liveness_probe_period_seconds

        if self.liveness_probe_success_threshold is not None:
            result['LivenessProbeSuccessThreshold'] = self.liveness_probe_success_threshold

        if self.liveness_probe_tcp_socket_port is not None:
            result['LivenessProbeTcpSocketPort'] = self.liveness_probe_tcp_socket_port

        if self.liveness_probe_timeout_seconds is not None:
            result['LivenessProbeTimeoutSeconds'] = self.liveness_probe_timeout_seconds

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

        if self.readiness_probe_exec_commands is not None:
            result['ReadinessProbeExecCommands'] = self.readiness_probe_exec_commands

        if self.readiness_probe_failure_threshold is not None:
            result['ReadinessProbeFailureThreshold'] = self.readiness_probe_failure_threshold

        if self.readiness_probe_http_get_path is not None:
            result['ReadinessProbeHttpGetPath'] = self.readiness_probe_http_get_path

        if self.readiness_probe_http_get_port is not None:
            result['ReadinessProbeHttpGetPort'] = self.readiness_probe_http_get_port

        if self.readiness_probe_http_get_scheme is not None:
            result['ReadinessProbeHttpGetScheme'] = self.readiness_probe_http_get_scheme

        if self.readiness_probe_initial_delay_seconds is not None:
            result['ReadinessProbeInitialDelaySeconds'] = self.readiness_probe_initial_delay_seconds

        if self.readiness_probe_period_seconds is not None:
            result['ReadinessProbePeriodSeconds'] = self.readiness_probe_period_seconds

        if self.readiness_probe_success_threshold is not None:
            result['ReadinessProbeSuccessThreshold'] = self.readiness_probe_success_threshold

        if self.readiness_probe_tcp_socket_port is not None:
            result['ReadinessProbeTcpSocketPort'] = self.readiness_probe_tcp_socket_port

        if self.readiness_probe_timeout_seconds is not None:
            result['ReadinessProbeTimeoutSeconds'] = self.readiness_probe_timeout_seconds

        if self.security_context_capability_adds is not None:
            result['SecurityContextCapabilityAdds'] = self.security_context_capability_adds

        if self.security_context_read_only_root_filesystem is not None:
            result['SecurityContextReadOnlyRootFilesystem'] = self.security_context_read_only_root_filesystem

        if self.security_context_run_as_user is not None:
            result['SecurityContextRunAsUser'] = self.security_context_run_as_user

        if self.stdin is not None:
            result['Stdin'] = self.stdin

        if self.stdin_once is not None:
            result['StdinOnce'] = self.stdin_once

        if self.tty is not None:
            result['Tty'] = self.tty

        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k1 in self.volume_mounts:
                result['VolumeMounts'].append(k1.to_map() if k1 else None)

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')

        if m.get('LifecyclePostStartHandlerExecs') is not None:
            self.lifecycle_post_start_handler_execs = m.get('LifecyclePostStartHandlerExecs')

        if m.get('LifecyclePostStartHandlerHttpGetHost') is not None:
            self.lifecycle_post_start_handler_http_get_host = m.get('LifecyclePostStartHandlerHttpGetHost')

        if m.get('LifecyclePostStartHandlerHttpGetPath') is not None:
            self.lifecycle_post_start_handler_http_get_path = m.get('LifecyclePostStartHandlerHttpGetPath')

        if m.get('LifecyclePostStartHandlerHttpGetPort') is not None:
            self.lifecycle_post_start_handler_http_get_port = m.get('LifecyclePostStartHandlerHttpGetPort')

        if m.get('LifecyclePostStartHandlerHttpGetScheme') is not None:
            self.lifecycle_post_start_handler_http_get_scheme = m.get('LifecyclePostStartHandlerHttpGetScheme')

        if m.get('LifecyclePostStartHandlerTcpSocketHost') is not None:
            self.lifecycle_post_start_handler_tcp_socket_host = m.get('LifecyclePostStartHandlerTcpSocketHost')

        if m.get('LifecyclePostStartHandlerTcpSocketPort') is not None:
            self.lifecycle_post_start_handler_tcp_socket_port = m.get('LifecyclePostStartHandlerTcpSocketPort')

        if m.get('LifecyclePreStopHandlerExecs') is not None:
            self.lifecycle_pre_stop_handler_execs = m.get('LifecyclePreStopHandlerExecs')

        if m.get('LifecyclePreStopHandlerHttpGetHost') is not None:
            self.lifecycle_pre_stop_handler_http_get_host = m.get('LifecyclePreStopHandlerHttpGetHost')

        if m.get('LifecyclePreStopHandlerHttpGetPath') is not None:
            self.lifecycle_pre_stop_handler_http_get_path = m.get('LifecyclePreStopHandlerHttpGetPath')

        if m.get('LifecyclePreStopHandlerHttpGetPort') is not None:
            self.lifecycle_pre_stop_handler_http_get_port = m.get('LifecyclePreStopHandlerHttpGetPort')

        if m.get('LifecyclePreStopHandlerHttpGetScheme') is not None:
            self.lifecycle_pre_stop_handler_http_get_scheme = m.get('LifecyclePreStopHandlerHttpGetScheme')

        if m.get('LifecyclePreStopHandlerTcpSocketHost') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_host = m.get('LifecyclePreStopHandlerTcpSocketHost')

        if m.get('LifecyclePreStopHandlerTcpSocketPort') is not None:
            self.lifecycle_pre_stop_handler_tcp_socket_port = m.get('LifecyclePreStopHandlerTcpSocketPort')

        if m.get('LivenessProbeExecCommands') is not None:
            self.liveness_probe_exec_commands = m.get('LivenessProbeExecCommands')

        if m.get('LivenessProbeFailureThreshold') is not None:
            self.liveness_probe_failure_threshold = m.get('LivenessProbeFailureThreshold')

        if m.get('LivenessProbeHttpGetPath') is not None:
            self.liveness_probe_http_get_path = m.get('LivenessProbeHttpGetPath')

        if m.get('LivenessProbeHttpGetPort') is not None:
            self.liveness_probe_http_get_port = m.get('LivenessProbeHttpGetPort')

        if m.get('LivenessProbeHttpGetScheme') is not None:
            self.liveness_probe_http_get_scheme = m.get('LivenessProbeHttpGetScheme')

        if m.get('LivenessProbeInitialDelaySeconds') is not None:
            self.liveness_probe_initial_delay_seconds = m.get('LivenessProbeInitialDelaySeconds')

        if m.get('LivenessProbePeriodSeconds') is not None:
            self.liveness_probe_period_seconds = m.get('LivenessProbePeriodSeconds')

        if m.get('LivenessProbeSuccessThreshold') is not None:
            self.liveness_probe_success_threshold = m.get('LivenessProbeSuccessThreshold')

        if m.get('LivenessProbeTcpSocketPort') is not None:
            self.liveness_probe_tcp_socket_port = m.get('LivenessProbeTcpSocketPort')

        if m.get('LivenessProbeTimeoutSeconds') is not None:
            self.liveness_probe_timeout_seconds = m.get('LivenessProbeTimeoutSeconds')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('ReadinessProbeExecCommands') is not None:
            self.readiness_probe_exec_commands = m.get('ReadinessProbeExecCommands')

        if m.get('ReadinessProbeFailureThreshold') is not None:
            self.readiness_probe_failure_threshold = m.get('ReadinessProbeFailureThreshold')

        if m.get('ReadinessProbeHttpGetPath') is not None:
            self.readiness_probe_http_get_path = m.get('ReadinessProbeHttpGetPath')

        if m.get('ReadinessProbeHttpGetPort') is not None:
            self.readiness_probe_http_get_port = m.get('ReadinessProbeHttpGetPort')

        if m.get('ReadinessProbeHttpGetScheme') is not None:
            self.readiness_probe_http_get_scheme = m.get('ReadinessProbeHttpGetScheme')

        if m.get('ReadinessProbeInitialDelaySeconds') is not None:
            self.readiness_probe_initial_delay_seconds = m.get('ReadinessProbeInitialDelaySeconds')

        if m.get('ReadinessProbePeriodSeconds') is not None:
            self.readiness_probe_period_seconds = m.get('ReadinessProbePeriodSeconds')

        if m.get('ReadinessProbeSuccessThreshold') is not None:
            self.readiness_probe_success_threshold = m.get('ReadinessProbeSuccessThreshold')

        if m.get('ReadinessProbeTcpSocketPort') is not None:
            self.readiness_probe_tcp_socket_port = m.get('ReadinessProbeTcpSocketPort')

        if m.get('ReadinessProbeTimeoutSeconds') is not None:
            self.readiness_probe_timeout_seconds = m.get('ReadinessProbeTimeoutSeconds')

        if m.get('SecurityContextCapabilityAdds') is not None:
            self.security_context_capability_adds = m.get('SecurityContextCapabilityAdds')

        if m.get('SecurityContextReadOnlyRootFilesystem') is not None:
            self.security_context_read_only_root_filesystem = m.get('SecurityContextReadOnlyRootFilesystem')

        if m.get('SecurityContextRunAsUser') is not None:
            self.security_context_run_as_user = m.get('SecurityContextRunAsUser')

        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')

        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')

        if m.get('Tty') is not None:
            self.tty = m.get('Tty')

        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k1 in m.get('VolumeMounts'):
                temp_model = main_models.DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k1))

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersVolumeMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory where the container mounts the data volume.
        # 
        # >Notice: The content in the mount directory of the container is directly overwritten by the content of the volume. Use this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings for the data volume. Mount propagation allows volumes mounted by a container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # - None: The volume is not aware of any subsequent mount operations performed on the volume or its subdirectories.
        # - HostToCotainer: The volume is aware of subsequent mount operations performed on the volume or its subdirectories.
        # - Bidirectional: Similar to HostToCotainer, the volume is aware of mount operations. In addition, the volume is propagated back to the host and to all containers of all pods that use the same volume.
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the data volume. This name must be the same as the Name parameter in Volume.
        self.name = name
        # Specifies whether the data volume is read-only.
        # Default value: false.
        self.read_only = read_only
        # The subpath of the data volume.
        self.sub_path = sub_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.mount_propagation is not None:
            result['MountPropagation'] = self.mount_propagation

        if self.name is not None:
            result['Name'] = self.name

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.sub_path is not None:
            result['SubPath'] = self.sub_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('MountPropagation') is not None:
            self.mount_propagation = m.get('MountPropagation')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('SubPath') is not None:
            self.sub_path = m.get('SubPath')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type. Valid values:
        # - TCP
        # - UDP
        self.protocol = protocol

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsContainersEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref_field_path: str = None,
        key: str = None,
        value: str = None,
    ):
        # This parameter is unavailable.
        self.field_ref_field_path = field_ref_field_path
        # The name of the environment variable.
        self.key = key
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref_field_path is not None:
            result['FieldRefFieldPath'] = self.field_ref_field_path

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRefFieldPath') is not None:
            self.field_ref_field_path = m.get('FieldRefFieldPath')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeEciScalingConfigurationsResponseBodyScalingConfigurationsAcrRegistryInfos(DaraModel):
    def __init__(
        self,
        domains: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The domain names of the ACR Enterprise instance. By default, all domain names of the instance are used. You can specify one or more domain names. Separate multiple domain names with commas (,).
        self.domains = domains
        # The instance ID of the ACR Enterprise instance.
        self.instance_id = instance_id
        # The name of the ACR Enterprise instance.
        self.instance_name = instance_name
        # The region where the ACR Enterprise instance resides.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domains is not None:
            result['Domains'] = self.domains

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

