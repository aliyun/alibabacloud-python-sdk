# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ess20220222 import models as main_models
from darabonba.model import DaraModel

class ModifyEciScalingConfigurationRequest(DaraModel):
    def __init__(
        self,
        acr_registry_infos: List[main_models.ModifyEciScalingConfigurationRequestAcrRegistryInfos] = None,
        active_deadline_seconds: int = None,
        auto_create_eip: bool = None,
        auto_match_image_cache: bool = None,
        container_group_name: str = None,
        containers: List[main_models.ModifyEciScalingConfigurationRequestContainers] = None,
        containers_update_type: str = None,
        cost_optimization: bool = None,
        cpu: float = None,
        cpu_options_core: int = None,
        cpu_options_threads_per_core: int = None,
        data_cache_bucket: str = None,
        data_cache_bursting_enabled: bool = None,
        data_cache_pl: str = None,
        data_cache_provisioned_iops: int = None,
        description: str = None,
        dns_config_name_servers: List[str] = None,
        dns_config_options: List[main_models.ModifyEciScalingConfigurationRequestDnsConfigOptions] = None,
        dns_config_searchs: List[str] = None,
        dns_policy: str = None,
        egress_bandwidth: int = None,
        eip_bandwidth: int = None,
        enable_sls: bool = None,
        ephemeral_storage: int = None,
        gpu_driver_version: str = None,
        host_aliases: List[main_models.ModifyEciScalingConfigurationRequestHostAliases] = None,
        host_name: str = None,
        image_registry_credentials: List[main_models.ModifyEciScalingConfigurationRequestImageRegistryCredentials] = None,
        image_snapshot_id: str = None,
        ingress_bandwidth: int = None,
        init_containers: List[main_models.ModifyEciScalingConfigurationRequestInitContainers] = None,
        instance_family_level: str = None,
        instance_types: List[str] = None,
        ipv_6address_count: int = None,
        load_balancer_weight: int = None,
        memory: float = None,
        ntp_servers: List[str] = None,
        override: bool = None,
        owner_id: int = None,
        ram_role_name: str = None,
        resource_group_id: str = None,
        resource_owner_account: str = None,
        restart_policy: str = None,
        scaling_configuration_id: str = None,
        scaling_configuration_name: str = None,
        security_context_sys_ctls: List[main_models.ModifyEciScalingConfigurationRequestSecurityContextSysCtls] = None,
        security_group_id: str = None,
        spot_price_limit: float = None,
        spot_strategy: str = None,
        tags: List[main_models.ModifyEciScalingConfigurationRequestTags] = None,
        termination_grace_period_seconds: int = None,
        volumes: List[main_models.ModifyEciScalingConfigurationRequestVolumes] = None,
    ):
        # The information about ACR Enterprise Edition instances.
        self.acr_registry_infos = acr_registry_infos
        # The validity period. Unit: seconds.
        self.active_deadline_seconds = active_deadline_seconds
        # Specifies whether automatic creation of an elastic IP address (EIP) is enabled and the EIP is attached to the ECI instance.
        self.auto_create_eip = auto_create_eip
        # Specifies whether to automatically match an image cache.
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The name of the ECI, which is the name of the container group. The name must meet the following requirements:
        # 
        # - The name must be 2 to 128 characters in length.
        # - The name can contain lowercase letters, digits, and hyphens (-), and cannot start or end with a hyphen (-).
        self.container_group_name = container_group_name
        # The list of containers.
        self.containers = containers
        # The control parameter for the update method of the Containers parameter. Valid values:
        # 
        # - RenewUpdate: full update. The Containers parameter in the update request prevails and overwrites the original Containers parameter configuration.
        # - IncrementalUpdate: incremental update. Containers are matched based on Container.name, and only the parameters specified in the request are updated.
        # 
        # Default value: RenewUpdate.
        self.containers_update_type = containers_update_type
        # Specifies whether to enable cost optimization. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        self.cost_optimization = cost_optimization
        # The number of vCPUs for the instance. Unit: cores.
        self.cpu = cpu
        # The number of physical CPU cores. Only specific instance types support custom settings. For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_core = cpu_options_core
        # The number of threads per core. Only specific instance types support custom settings. A value of 1 indicates that hyper-threading is disabled. For more information, see [Customize CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        # The data cache bucket.
        self.data_cache_bucket = data_cache_bucket
        # Specifies whether to enable the burst feature for the ESSD AutoPL cloud disk used for data caching. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: false.
        # 
        # > For more information about ESSD AutoPL cloud disks, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_bursting_enabled = data_cache_bursting_enabled
        # The performance level of the cloud disk used for data caching. Use ESSDs. Valid values for the performance level of an ESSD:
        # 
        # - PL0: A single ESSD can deliver up to 10,000 random read/write IOPS.
        # - PL1: A single ESSD can deliver up to 50,000 random read/write IOPS.
        # - PL2: A single ESSD can deliver up to 100,000 random read/write IOPS.
        # - PL3: A single ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        # 
        # > For more information about ESSDs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.data_cache_pl = data_cache_pl
        # The provisioned read and write IOPS of the ESSD AutoPL cloud disk used for data caching. Valid values: 0 to min{50000, 1000 × capacity - baseline performance}, where baseline performance = min{1800 + 50 × capacity, 50000}.
        # 
        # > For more information about ESSD AutoPL cloud disks, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_provisioned_iops = data_cache_provisioned_iops
        # > This parameter is not available.
        self.description = description
        # The list of IP addresses of DNS servers.
        self.dns_config_name_servers = dns_config_name_servers
        # The list of object options. Each object consists of a Name and an optional Value.
        self.dns_config_options = dns_config_options
        # The list of DNS search domains.
        self.dns_config_searchs = dns_config_searchs
        # The DNS policy. Valid values:
        # 
        # - None: uses the DNS settings specified in the DnsConfig field.
        # 
        # - Default: inherits the DNS settings from the runtime environment.
        self.dns_policy = dns_policy
        # The outbound bandwidth limit. Unit: bytes.
        self.egress_bandwidth = egress_bandwidth
        # The bandwidth of the EIP.
        # 
        # Default value: 5 Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # > This parameter is not available.
        self.enable_sls = enable_sls
        # The size of the temporary storage space. By default, PL1 ESSDs are used. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The specified GPU driver version. Valid values:
        # - tesla=470.82.01 (default)
        # - tesla=525.85.12
        # 
        # > Only specific instance types support switching the GPU driver version. For more information, see [Create an instance by specifying a GPU instance type](https://help.aliyun.com/document_detail/2579486.html).
        self.gpu_driver_version = gpu_driver_version
        # The host-related information.
        self.host_aliases = host_aliases
        # The hostname, which is the name of the container group.
        self.host_name = host_name
        # The details of the image registry.
        self.image_registry_credentials = image_registry_credentials
        # The ID of the image cache.
        self.image_snapshot_id = image_snapshot_id
        # The inbound bandwidth limit. Unit: bytes.
        self.ingress_bandwidth = ingress_bandwidth
        # The list of init containers.
        self.init_containers = init_containers
        # The level of the instance family. This parameter is used to filter instance types that meet your requirements and takes effect only when CostOptimization is set to true. Valid values:
        # 
        # - EntryLevel: shared instance types. Shared instance types are more cost-effective but cannot guarantee stable computing performance. They are suitable for business scenarios with low CPU utilization. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # - EnterpriseLevel: enterprise-level instance types. Enterprise-level instance types provide stable performance and dedicated resources. They are suitable for business scenarios that require high stability. For more information, see [Instance families](https://help.aliyun.com/document_detail/25378.html).
        # - CreditEntryLevel: burstable instance types. Burstable instance types use CPU credits to ensure computing performance. They are suitable for business scenarios with low CPU utilization but occasional CPU usage spikes. For more information, see [Overview of burstable instances](https://help.aliyun.com/document_detail/59977.html).
        self.instance_family_level = instance_family_level
        # The specified ECS instance types. You can specify up to five instance types.
        self.instance_types = instance_types
        # The number of IPv6 addresses.
        self.ipv_6address_count = ipv_6address_count
        # The weight of the backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size for the instance. Unit: GiB.
        self.memory = memory
        # The NTP server.
        self.ntp_servers = ntp_servers
        # Specifies whether to overwrite. Valid values:
        # 
        # - true: Overwrite.
        # - false: Do not overwrite.
        self.override = override
        self.owner_id = owner_id
        # The name of the RAM role for the instance. ECIs and ECS instances share the same instance RAM roles. For more information, see [Use an instance RAM role by calling API operations](https://help.aliyun.com/document_detail/61178.html).
        self.ram_role_name = ram_role_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The restart policy of the instance. Valid values:
        # - Always: always restarts the instance.
        # - Never: never restarts the instance.
        # - OnFailure: restarts the instance when it fails.
        # 
        # Default value: Always.
        self.restart_policy = restart_policy
        # The ID of the scaling configuration to be modified.
        # 
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration. The name must be 2 to 64 characters in length, and can contain digits, letters, and Chinese characters. It must start with a digit, a letter, or a Chinese character, and can contain digits, underscores (_), hyphens (-), and periods (.).
        # 
        # The name of a scaling configuration must be unique within a scaling group in a region. If you do not specify this parameter, the ID of the scaling configuration is used by default.
        self.scaling_configuration_name = scaling_configuration_name
        # The system information of the contextual security context in which the instance runs.
        self.security_context_sys_ctls = security_context_sys_ctls
        # The ID of the security group to which the ECI instance belongs. ECI instances in the same security group can access each other.
        # 
        # If you do not specify a security group, the system automatically uses the default security group in the selected region. You must ensure that the inbound rules of the security group include the protocols and ports that the containers need to expose. If no default security group exists in the region, the system performs automatic creation of a default security group and adds the declared container protocols and ports to the inbound rules of the security group.
        self.security_group_id = security_group_id
        # The maximum hourly price for the spot instance. The value can be accurate to three decimal places.
        # 
        # This parameter is required when SpotStrategy is set to SpotWithPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The preemption policy for the instance. Valid values:
        # 
        # - NoSpot: applies to regular pay-as-you-go instances.
        # - SpotWithPriceLimit: applies to spot instances that have maximum hourly prices.
        # - SpotAsPriceGo: applies to spot instances whose prices are automatically set by the system based on the current market price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The tags.
        self.tags = tags
        # The buffer time for the program to handle operations before shutdown. Unit: seconds.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The volume information.
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

        if self.containers_update_type is not None:
            result['ContainersUpdateType'] = self.containers_update_type

        if self.cost_optimization is not None:
            result['CostOptimization'] = self.cost_optimization

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.cpu_options_core is not None:
            result['CpuOptionsCore'] = self.cpu_options_core

        if self.cpu_options_threads_per_core is not None:
            result['CpuOptionsThreadsPerCore'] = self.cpu_options_threads_per_core

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

        if self.dns_config_searchs is not None:
            result['DnsConfigSearchs'] = self.dns_config_searchs

        if self.dns_policy is not None:
            result['DnsPolicy'] = self.dns_policy

        if self.egress_bandwidth is not None:
            result['EgressBandwidth'] = self.egress_bandwidth

        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.enable_sls is not None:
            result['EnableSls'] = self.enable_sls

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

        if self.load_balancer_weight is not None:
            result['LoadBalancerWeight'] = self.load_balancer_weight

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.ntp_servers is not None:
            result['NtpServers'] = self.ntp_servers

        if self.override is not None:
            result['Override'] = self.override

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.ram_role_name is not None:
            result['RamRoleName'] = self.ram_role_name

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy

        if self.scaling_configuration_id is not None:
            result['ScalingConfigurationId'] = self.scaling_configuration_id

        if self.scaling_configuration_name is not None:
            result['ScalingConfigurationName'] = self.scaling_configuration_name

        result['SecurityContextSysCtls'] = []
        if self.security_context_sys_ctls is not None:
            for k1 in self.security_context_sys_ctls:
                result['SecurityContextSysCtls'].append(k1.to_map() if k1 else None)

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

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
                temp_model = main_models.ModifyEciScalingConfigurationRequestAcrRegistryInfos()
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
                temp_model = main_models.ModifyEciScalingConfigurationRequestContainers()
                self.containers.append(temp_model.from_map(k1))

        if m.get('ContainersUpdateType') is not None:
            self.containers_update_type = m.get('ContainersUpdateType')

        if m.get('CostOptimization') is not None:
            self.cost_optimization = m.get('CostOptimization')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('CpuOptionsCore') is not None:
            self.cpu_options_core = m.get('CpuOptionsCore')

        if m.get('CpuOptionsThreadsPerCore') is not None:
            self.cpu_options_threads_per_core = m.get('CpuOptionsThreadsPerCore')

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
                temp_model = main_models.ModifyEciScalingConfigurationRequestDnsConfigOptions()
                self.dns_config_options.append(temp_model.from_map(k1))

        if m.get('DnsConfigSearchs') is not None:
            self.dns_config_searchs = m.get('DnsConfigSearchs')

        if m.get('DnsPolicy') is not None:
            self.dns_policy = m.get('DnsPolicy')

        if m.get('EgressBandwidth') is not None:
            self.egress_bandwidth = m.get('EgressBandwidth')

        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('EnableSls') is not None:
            self.enable_sls = m.get('EnableSls')

        if m.get('EphemeralStorage') is not None:
            self.ephemeral_storage = m.get('EphemeralStorage')

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        self.host_aliases = []
        if m.get('HostAliases') is not None:
            for k1 in m.get('HostAliases'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestHostAliases()
                self.host_aliases.append(temp_model.from_map(k1))

        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')

        self.image_registry_credentials = []
        if m.get('ImageRegistryCredentials') is not None:
            for k1 in m.get('ImageRegistryCredentials'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestImageRegistryCredentials()
                self.image_registry_credentials.append(temp_model.from_map(k1))

        if m.get('ImageSnapshotId') is not None:
            self.image_snapshot_id = m.get('ImageSnapshotId')

        if m.get('IngressBandwidth') is not None:
            self.ingress_bandwidth = m.get('IngressBandwidth')

        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k1 in m.get('InitContainers'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainers()
                self.init_containers.append(temp_model.from_map(k1))

        if m.get('InstanceFamilyLevel') is not None:
            self.instance_family_level = m.get('InstanceFamilyLevel')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Ipv6AddressCount') is not None:
            self.ipv_6address_count = m.get('Ipv6AddressCount')

        if m.get('LoadBalancerWeight') is not None:
            self.load_balancer_weight = m.get('LoadBalancerWeight')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('NtpServers') is not None:
            self.ntp_servers = m.get('NtpServers')

        if m.get('Override') is not None:
            self.override = m.get('Override')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RamRoleName') is not None:
            self.ram_role_name = m.get('RamRoleName')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')

        if m.get('ScalingConfigurationId') is not None:
            self.scaling_configuration_id = m.get('ScalingConfigurationId')

        if m.get('ScalingConfigurationName') is not None:
            self.scaling_configuration_name = m.get('ScalingConfigurationName')

        self.security_context_sys_ctls = []
        if m.get('SecurityContextSysCtls') is not None:
            for k1 in m.get('SecurityContextSysCtls'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestSecurityContextSysCtls()
                self.security_context_sys_ctls.append(temp_model.from_map(k1))

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('SpotStrategy') is not None:
            self.spot_strategy = m.get('SpotStrategy')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TerminationGracePeriodSeconds') is not None:
            self.termination_grace_period_seconds = m.get('TerminationGracePeriodSeconds')

        self.volumes = []
        if m.get('Volumes') is not None:
            for k1 in m.get('Volumes'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestVolumes()
                self.volumes.append(temp_model.from_map(k1))

        return self

class ModifyEciScalingConfigurationRequestVolumes(DaraModel):
    def __init__(
        self,
        disk_volume: main_models.ModifyEciScalingConfigurationRequestVolumesDiskVolume = None,
        empty_dir_volume: main_models.ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume = None,
        flex_volume: main_models.ModifyEciScalingConfigurationRequestVolumesFlexVolume = None,
        host_path_volume: main_models.ModifyEciScalingConfigurationRequestVolumesHostPathVolume = None,
        nfsvolume: main_models.ModifyEciScalingConfigurationRequestVolumesNFSVolume = None,
        config_file_volume_config_file_to_path: List[main_models.ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath] = None,
        config_file_volume_default_mode: int = None,
        name: str = None,
        type: str = None,
    ):
        self.disk_volume = disk_volume
        self.empty_dir_volume = empty_dir_volume
        self.flex_volume = flex_volume
        self.host_path_volume = host_path_volume
        self.nfsvolume = nfsvolume
        # The list of configuration file paths.
        self.config_file_volume_config_file_to_path = config_file_volume_config_file_to_path
        # The default permissions for the ConfigFileVolume.
        self.config_file_volume_default_mode = config_file_volume_default_mode
        # The name of the volume.
        self.name = name
        # The volume type. Valid values:
        # - EmptyDirVolume
        # - NFSVolume
        # - ConfigFileVolume
        # - FlexVolume
        self.type = type

    def validate(self):
        if self.disk_volume:
            self.disk_volume.validate()
        if self.empty_dir_volume:
            self.empty_dir_volume.validate()
        if self.flex_volume:
            self.flex_volume.validate()
        if self.host_path_volume:
            self.host_path_volume.validate()
        if self.nfsvolume:
            self.nfsvolume.validate()
        if self.config_file_volume_config_file_to_path:
            for v1 in self.config_file_volume_config_file_to_path:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_volume is not None:
            result['DiskVolume'] = self.disk_volume.to_map()

        if self.empty_dir_volume is not None:
            result['EmptyDirVolume'] = self.empty_dir_volume.to_map()

        if self.flex_volume is not None:
            result['FlexVolume'] = self.flex_volume.to_map()

        if self.host_path_volume is not None:
            result['HostPathVolume'] = self.host_path_volume.to_map()

        if self.nfsvolume is not None:
            result['NFSVolume'] = self.nfsvolume.to_map()

        result['ConfigFileVolumeConfigFileToPath'] = []
        if self.config_file_volume_config_file_to_path is not None:
            for k1 in self.config_file_volume_config_file_to_path:
                result['ConfigFileVolumeConfigFileToPath'].append(k1.to_map() if k1 else None)

        if self.config_file_volume_default_mode is not None:
            result['ConfigFileVolumeDefaultMode'] = self.config_file_volume_default_mode

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskVolume') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesDiskVolume()
            self.disk_volume = temp_model.from_map(m.get('DiskVolume'))

        if m.get('EmptyDirVolume') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume()
            self.empty_dir_volume = temp_model.from_map(m.get('EmptyDirVolume'))

        if m.get('FlexVolume') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesFlexVolume()
            self.flex_volume = temp_model.from_map(m.get('FlexVolume'))

        if m.get('HostPathVolume') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesHostPathVolume()
            self.host_path_volume = temp_model.from_map(m.get('HostPathVolume'))

        if m.get('NFSVolume') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesNFSVolume()
            self.nfsvolume = temp_model.from_map(m.get('NFSVolume'))

        self.config_file_volume_config_file_to_path = []
        if m.get('ConfigFileVolumeConfigFileToPath') is not None:
            for k1 in m.get('ConfigFileVolumeConfigFileToPath'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath()
                self.config_file_volume_config_file_to_path.append(temp_model.from_map(k1))

        if m.get('ConfigFileVolumeDefaultMode') is not None:
            self.config_file_volume_default_mode = m.get('ConfigFileVolumeDefaultMode')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ModifyEciScalingConfigurationRequestVolumesConfigFileVolumeConfigFileToPath(DaraModel):
    def __init__(
        self,
        content: str = None,
        mode: int = None,
        path: str = None,
    ):
        # The content of the configuration file (32 KB).
        self.content = content
        # The directory permissions for the ConfigFileVolume.
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

class ModifyEciScalingConfigurationRequestVolumesNFSVolume(DaraModel):
    def __init__(
        self,
        path: str = None,
        read_only: bool = None,
        server: str = None,
    ):
        # The path of the NFS volume.
        self.path = path
        # Specifies whether the NFS volume is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The address of the NFS server.
        self.server = server

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.server is not None:
            result['Server'] = self.server

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('Server') is not None:
            self.server = m.get('Server')

        return self

class ModifyEciScalingConfigurationRequestVolumesHostPathVolume(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The absolute path on the host.
        self.path = path
        # The type of the host directory, such as File, Directory, or Socket.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ModifyEciScalingConfigurationRequestVolumesFlexVolume(DaraModel):
    def __init__(
        self,
        driver: str = None,
        fs_type: str = None,
        options: str = None,
    ):
        # The name of the driver used for the FlexVolume.
        self.driver = driver
        # The type of the file system to be mounted. The default value depends on the script of the FlexVolume.
        self.fs_type = fs_type
        # The list of options for the FlexVolume object. The options are passed as key-value pairs in JSON format.
        # 
        # Example: When you mount a cloud disk by using FlexVolume, the format of Options is `{"volumeId":"d-2zehdahrwoa7srg****","performanceLevel": "PL2"}`.
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.driver is not None:
            result['Driver'] = self.driver

        if self.fs_type is not None:
            result['FsType'] = self.fs_type

        if self.options is not None:
            result['Options'] = self.options

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        return self

class ModifyEciScalingConfigurationRequestVolumesEmptyDirVolume(DaraModel):
    def __init__(
        self,
        medium: str = None,
        size_limit: str = None,
    ):
        # The storage medium of the EmptyDirVolume. The default value is empty, which indicates that the node file system is used. If this parameter is set to memory, the memory is used.
        self.medium = medium
        # The size of the EmptyDir volume. Specify a unit for the value, such as Gi or Mi.
        self.size_limit = size_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.medium is not None:
            result['Medium'] = self.medium

        if self.size_limit is not None:
            result['SizeLimit'] = self.size_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')

        if m.get('SizeLimit') is not None:
            self.size_limit = m.get('SizeLimit')

        return self

class ModifyEciScalingConfigurationRequestVolumesDiskVolume(DaraModel):
    def __init__(
        self,
        disk_id: str = None,
        disk_size: int = None,
        fs_type: str = None,
    ):
        # The ID of the disk volume.
        self.disk_id = disk_id
        # The size of the disk volume. Unit: GiB.
        self.disk_size = disk_size
        # This file system type is deprecated. Use the FlexVolume.FsType parameter.
        self.fs_type = fs_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.disk_id is not None:
            result['DiskId'] = self.disk_id

        if self.disk_size is not None:
            result['DiskSize'] = self.disk_size

        if self.fs_type is not None:
            result['FsType'] = self.fs_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DiskId') is not None:
            self.disk_id = m.get('DiskId')

        if m.get('DiskSize') is not None:
            self.disk_size = m.get('DiskSize')

        if m.get('FsType') is not None:
            self.fs_type = m.get('FsType')

        return self

class ModifyEciScalingConfigurationRequestTags(DaraModel):
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

class ModifyEciScalingConfigurationRequestSecurityContextSysCtls(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The system name of the security context in which the instance runs.
        self.name = name
        # The variable value of the contextual security context in which the instance runs.
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

class ModifyEciScalingConfigurationRequestInitContainers(DaraModel):
    def __init__(
        self,
        security_context: main_models.ModifyEciScalingConfigurationRequestInitContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        gpu: int = None,
        image: str = None,
        image_pull_policy: str = None,
        init_container_environment_vars: List[main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars] = None,
        init_container_ports: List[main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts] = None,
        init_container_volume_mounts: List[main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts] = None,
        memory: float = None,
        name: str = None,
        working_dir: str = None,
    ):
        self.security_context = security_context
        # The startup arguments for the container.
        self.args = args
        # The startup commands for the container.
        self.commands = commands
        # The number of vCPUs allocated to the container.
        self.cpu = cpu
        # The number of GPUs allocated to the container.
        self.gpu = gpu
        # The image used by the container.
        self.image = image
        # The image pull policy for the container. Valid values:
        # 
        # - Always: Always pulls the image.
        # - IfNotPresent: Pulls the image only if it is not present locally.
        # - Never: Never pulls the image. Only local images are used.
        self.image_pull_policy = image_pull_policy
        # The environment variable information of the init container.
        self.init_container_environment_vars = init_container_environment_vars
        # The port information of the init container.
        self.init_container_ports = init_container_ports
        # The array of mount point information for the init container.
        self.init_container_volume_mounts = init_container_volume_mounts
        # The memory size. Unit: GiB.
        self.memory = memory
        # The name of the container.
        self.name = name
        # The working directory.
        self.working_dir = working_dir

    def validate(self):
        if self.security_context:
            self.security_context.validate()
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
        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()

        if self.args is not None:
            result['Args'] = self.args

        if self.commands is not None:
            result['Commands'] = self.commands

        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.gpu is not None:
            result['Gpu'] = self.gpu

        if self.image is not None:
            result['Image'] = self.image

        if self.image_pull_policy is not None:
            result['ImagePullPolicy'] = self.image_pull_policy

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

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityContext') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersSecurityContext()
            self.security_context = temp_model.from_map(m.get('SecurityContext'))

        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Gpu') is not None:
            self.gpu = m.get('Gpu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImagePullPolicy') is not None:
            self.image_pull_policy = m.get('ImagePullPolicy')

        self.init_container_environment_vars = []
        if m.get('InitContainerEnvironmentVars') is not None:
            for k1 in m.get('InitContainerEnvironmentVars'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars()
                self.init_container_environment_vars.append(temp_model.from_map(k1))

        self.init_container_ports = []
        if m.get('InitContainerPorts') is not None:
            for k1 in m.get('InitContainerPorts'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts()
                self.init_container_ports.append(temp_model.from_map(k1))

        self.init_container_volume_mounts = []
        if m.get('InitContainerVolumeMounts') is not None:
            for k1 in m.get('InitContainerVolumeMounts'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts()
                self.init_container_volume_mounts.append(temp_model.from_map(k1))

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class ModifyEciScalingConfigurationRequestInitContainersInitContainerVolumeMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory where the volume is mounted in the container.
        # 
        # > The contents of the mount path in the container are directly overwritten by the contents of the volume. Use this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings for the volume. Mount propagation allows a volume mounted to a container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # - None: The volume is not aware of any subsequent mount operations performed on the volume or its subdirectories.
        # - HostToCotainer: The volume is aware of subsequent mount operations performed on the volume or its subdirectories.
        # - Bidirectional: Similar to HostToCotainer, the volume is aware of mount operations. In addition, the volume is propagated back to the host and to all containers of all pods that use the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the mounted volume.
        self.name = name
        # Specifies whether the mount path is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The subdirectory under the volume. This allows a pod to mount different directories under the same volume to different directories in the container.
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

class ModifyEciScalingConfigurationRequestInitContainersInitContainerPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type. Valid values:
        # 
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

class ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref: main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable. The name must be 1 to 128 characters in length. It can contain letters, digits, and underscores (_), and cannot start with a digit.
        self.key = key
        # The value of the environment variable. The value can be up to 256 characters in length.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef()
            self.field_ref = temp_model.from_map(m.get('FieldRef'))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ModifyEciScalingConfigurationRequestInitContainersInitContainerEnvironmentVarsFieldRef(DaraModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        # > This parameter is not available.
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_path is not None:
            result['FieldPath'] = self.field_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')

        return self

class ModifyEciScalingConfigurationRequestInitContainersSecurityContext(DaraModel):
    def __init__(
        self,
        capability: main_models.ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        # > This parameter is not available.
        self.read_only_root_filesystem = read_only_root_filesystem
        # The user ID to run the container.
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()

        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem

        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m.get('Capability'))

        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')

        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')

        return self

class ModifyEciScalingConfigurationRequestInitContainersSecurityContextCapability(DaraModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        # Grants specific privileges to processes in the container. Valid values: NET_ADMIN and NET_RAW.
        # 
        # > NET_RAW is not supported by default. To use NET_RAW, submit a ticket.
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adds is not None:
            result['Adds'] = self.adds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')

        return self

class ModifyEciScalingConfigurationRequestImageRegistryCredentials(DaraModel):
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

class ModifyEciScalingConfigurationRequestHostAliases(DaraModel):
    def __init__(
        self,
        hostnames: List[str] = None,
        ip: str = None,
    ):
        # The hostname to be added.
        self.hostnames = hostnames
        # The IP address to be added.
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

class ModifyEciScalingConfigurationRequestDnsConfigOptions(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the object variable.
        self.name = name
        # The value of the object variable.
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

class ModifyEciScalingConfigurationRequestContainers(DaraModel):
    def __init__(
        self,
        liveness_probe: main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbe = None,
        readiness_probe: main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbe = None,
        security_context: main_models.ModifyEciScalingConfigurationRequestContainersSecurityContext = None,
        args: List[str] = None,
        commands: List[str] = None,
        cpu: float = None,
        environment_vars: List[main_models.ModifyEciScalingConfigurationRequestContainersEnvironmentVars] = None,
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
        memory: float = None,
        name: str = None,
        ports: List[main_models.ModifyEciScalingConfigurationRequestContainersPorts] = None,
        stdin: bool = None,
        stdin_once: bool = None,
        tty: bool = None,
        volume_mounts: List[main_models.ModifyEciScalingConfigurationRequestContainersVolumeMounts] = None,
        working_dir: str = None,
    ):
        self.liveness_probe = liveness_probe
        self.readiness_probe = readiness_probe
        self.security_context = security_context
        # The arguments for the container startup command. A maximum of 10 arguments are supported.
        self.args = args
        # The startup commands for the container. A maximum of 20 commands are supported. Each command can contain up to 256 characters.
        self.commands = commands
        # The number of vCPUs allocated to the container.
        self.cpu = cpu
        # The environment variable information.
        self.environment_vars = environment_vars
        # The number of GPUs allocated to the container.
        self.gpu = gpu
        # The container image.
        self.image = image
        # The image pull policy for the container. Valid values:
        # 
        # - Always: Always pulls the image.
        # - IfNotPresent: Pulls the image only if it is not present locally.
        # - Never: Never pulls the image. Only local images are used.
        self.image_pull_policy = image_pull_policy
        # The command executed in the container when the command line is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_execs = lifecycle_post_start_handler_execs
        # The host address that accepts the HTTP GET request when the HTTP request method is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        # The path to which the HTTP GET request is sent when the HTTP request method is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        # The port number to which the HTTP GET request is sent when the HTTP request method is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        # The protocol type of the HTTP GET request when the HTTP request method is used for the postStart callback function Settings. Valid values:
        # 
        # - HTTP
        # - HTTPS
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        # The host address on which the TCP socket check is performed when the TCP socket method is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        # The port number on which the TCP socket check is performed when the TCP socket method is used for the postStart callback function Settings.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        # The command executed in the container when the command line is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_execs = lifecycle_pre_stop_handler_execs
        # The host address that accepts the HTTP GET request when the HTTP request method is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        # The path to which the HTTP GET request is sent when the HTTP request method is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        # The port number to which the HTTP GET request is sent when the HTTP request method is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        # The protocol type of the HTTP GET request when the HTTP request method is used for the preStop callback function Settings. Valid values:
        # 
        # - HTTP
        # - HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        # The host address on which the TCP socket check is performed when the TCP socket method is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        # The port number on which the TCP socket check is performed when the TCP socket method is used for the preStop callback function Settings.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        # The memory size of the container, in GiB.
        self.memory = memory
        # The name of the container image.
        self.name = name
        # The port information.
        self.ports = ports
        # Specifies whether to allocate a buffer for standard input while the container is running. If this parameter is not set, a read from standard input results in an EOF.
        # 
        # Default value: false.
        self.stdin = stdin
        # Specifies whether the standard input stream maintains the enabling status across multiple attached sessions when standard input is true.
        # 
        # If StdinOnce is set to true, standard input is opened when the container starts, remains empty until the first client attaches to it, and then maintains the enabling status to accept data until the client disconnects. After the client disconnects, standard input enters shutdown and remains in shutdown until the container is restarted.
        self.stdin_once = stdin_once
        # Specifies whether to allocate a TTY for the container. Default value: false.
        # 
        # Set this parameter to true when the Command parameter is set to /bin/bash.
        self.tty = tty
        # The volume mount information for the container.
        self.volume_mounts = volume_mounts
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.liveness_probe:
            self.liveness_probe.validate()
        if self.readiness_probe:
            self.readiness_probe.validate()
        if self.security_context:
            self.security_context.validate()
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
        if self.liveness_probe is not None:
            result['LivenessProbe'] = self.liveness_probe.to_map()

        if self.readiness_probe is not None:
            result['ReadinessProbe'] = self.readiness_probe.to_map()

        if self.security_context is not None:
            result['SecurityContext'] = self.security_context.to_map()

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

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.name is not None:
            result['Name'] = self.name

        result['Ports'] = []
        if self.ports is not None:
            for k1 in self.ports:
                result['Ports'].append(k1.to_map() if k1 else None)

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
        if m.get('LivenessProbe') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbe()
            self.liveness_probe = temp_model.from_map(m.get('LivenessProbe'))

        if m.get('ReadinessProbe') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbe()
            self.readiness_probe = temp_model.from_map(m.get('ReadinessProbe'))

        if m.get('SecurityContext') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersSecurityContext()
            self.security_context = temp_model.from_map(m.get('SecurityContext'))

        if m.get('Args') is not None:
            self.args = m.get('Args')

        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestContainersEnvironmentVars()
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

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.ports = []
        if m.get('Ports') is not None:
            for k1 in m.get('Ports'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestContainersPorts()
                self.ports.append(temp_model.from_map(k1))

        if m.get('Stdin') is not None:
            self.stdin = m.get('Stdin')

        if m.get('StdinOnce') is not None:
            self.stdin_once = m.get('StdinOnce')

        if m.get('Tty') is not None:
            self.tty = m.get('Tty')

        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k1 in m.get('VolumeMounts'):
                temp_model = main_models.ModifyEciScalingConfigurationRequestContainersVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k1))

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class ModifyEciScalingConfigurationRequestContainersVolumeMounts(DaraModel):
    def __init__(
        self,
        mount_path: str = None,
        mount_propagation: str = None,
        name: str = None,
        read_only: bool = None,
        sub_path: str = None,
    ):
        # The directory where the volume is mounted in the container.
        # 
        # > The contents of the mount path in the container are directly overwritten by the contents of the volume. Use this parameter with caution.
        self.mount_path = mount_path
        # The mount propagation settings for the volume. Mount propagation allows volumes mounted by a container to be shared with other containers in the same pod, or even with other pods on the same node. Valid values:
        # 
        # - None: The volume does not receive any subsequent mounts that are performed on the volume or its subdirectories.
        # - HostToCotainer: The volume receives all subsequent mounts that are performed on the volume or its subdirectories.
        # - Bidirectional: Similar to HostToContainer, the volume receives all subsequent mounts. In addition, all mounts created by the container are propagated back to the host and to all containers of all pods that use the same volume.
        self.mount_propagation = mount_propagation
        # The name of the volume. The value must be the same as the Name parameter in Volume.
        self.name = name
        # Specifies whether the volume is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The subpath of the volume.
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

class ModifyEciScalingConfigurationRequestContainersPorts(DaraModel):
    def __init__(
        self,
        port: int = None,
        protocol: str = None,
    ):
        # The port number. Valid values: 1 to 65535.
        self.port = port
        # The protocol type. Valid values:
        # 
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

class ModifyEciScalingConfigurationRequestContainersEnvironmentVars(DaraModel):
    def __init__(
        self,
        field_ref: main_models.ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef = None,
        key: str = None,
        value: str = None,
    ):
        self.field_ref = field_ref
        # The name of the environment variable. The name must be 1 to 128 characters in length, match the `[0-9a-zA-Z]` format, and can contain underscores (_). It cannot start with a digit.
        self.key = key
        # The value of the environment variable. The value can be up to 256 characters in length.
        self.value = value

    def validate(self):
        if self.field_ref:
            self.field_ref.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_ref is not None:
            result['FieldRef'] = self.field_ref.to_map()

        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldRef') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef()
            self.field_ref = temp_model.from_map(m.get('FieldRef'))

        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ModifyEciScalingConfigurationRequestContainersEnvironmentVarsFieldRef(DaraModel):
    def __init__(
        self,
        field_path: str = None,
    ):
        # > This parameter is not available.
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_path is not None:
            result['FieldPath'] = self.field_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FieldPath') is not None:
            self.field_path = m.get('FieldPath')

        return self

class ModifyEciScalingConfigurationRequestContainersSecurityContext(DaraModel):
    def __init__(
        self,
        capability: main_models.ModifyEciScalingConfigurationRequestContainersSecurityContextCapability = None,
        read_only_root_filesystem: bool = None,
        run_as_user: int = None,
    ):
        self.capability = capability
        # Specifies whether the root file system of the container is read-only. Only true is supported.
        self.read_only_root_filesystem = read_only_root_filesystem
        # The user ID to run the container.
        self.run_as_user = run_as_user

    def validate(self):
        if self.capability:
            self.capability.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capability is not None:
            result['Capability'] = self.capability.to_map()

        if self.read_only_root_filesystem is not None:
            result['ReadOnlyRootFilesystem'] = self.read_only_root_filesystem

        if self.run_as_user is not None:
            result['RunAsUser'] = self.run_as_user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capability') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersSecurityContextCapability()
            self.capability = temp_model.from_map(m.get('Capability'))

        if m.get('ReadOnlyRootFilesystem') is not None:
            self.read_only_root_filesystem = m.get('ReadOnlyRootFilesystem')

        if m.get('RunAsUser') is not None:
            self.run_as_user = m.get('RunAsUser')

        return self

class ModifyEciScalingConfigurationRequestContainersSecurityContextCapability(DaraModel):
    def __init__(
        self,
        adds: List[str] = None,
    ):
        # Grants specific privileges to processes in the container. Valid values: NET_ADMIN and NET_RAW.
        # 
        # > NET_RAW is not supported by default. To use NET_RAW, submit a ticket.
        self.adds = adds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.adds is not None:
            result['Adds'] = self.adds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Adds') is not None:
            self.adds = m.get('Adds')

        return self

class ModifyEciScalingConfigurationRequestContainersReadinessProbe(DaraModel):
    def __init__(
        self,
        exec: main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeExec = None,
        failure_threshold: int = None,
        http_get: main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        # The minimum consecutive failures for the liveness check to be considered failed after having succeeded.
        # 
        # Default value: 3.
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        # The number of seconds after the container has started before the readiness check is initiated.
        self.initial_delay_seconds = initial_delay_seconds
        # The period for executing the liveness check, in seconds. Default value: 10. Minimum value: 1.
        self.period_seconds = period_seconds
        # The minimum consecutive successes for the readiness check to be considered successful after having failed. Default value: 1. The value must be 1.
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        # The timeout period for the readiness check, in seconds. Default value: 1. Minimum value: 1.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()

        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold

        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()

        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds

        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold

        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeExec()
            self.exec = temp_model.from_map(m.get('Exec'))

        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')

        if m.get('HttpGet') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet()
            self.http_get = temp_model.from_map(m.get('HttpGet'))

        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')

        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')

        if m.get('TcpSocket') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m.get('TcpSocket'))

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

class ModifyEciScalingConfigurationRequestContainersReadinessProbeTcpSocket(DaraModel):
    def __init__(
        self,
        port: int = None,
    ):
        # The port number on which the TCP socket check is performed when TCP socket is used for health checks.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class ModifyEciScalingConfigurationRequestContainersReadinessProbeHttpGet(DaraModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # The path to which the HTTP GET request is sent when HTTP GET is used for health checks.
        self.path = path
        # The port number to which the HTTP GET request is sent when HTTP GET is used for health checks.
        self.port = port
        # The protocol type of the HTTP GET request when HTTP GET is used for health checks. Valid values:
        # 
        # - HTTP
        # - HTTPS
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        return self

class ModifyEciScalingConfigurationRequestContainersReadinessProbeExec(DaraModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        # The command executed in the container when the exec action is used for health checks.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

class ModifyEciScalingConfigurationRequestContainersLivenessProbe(DaraModel):
    def __init__(
        self,
        exec: main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeExec = None,
        failure_threshold: int = None,
        http_get: main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet = None,
        initial_delay_seconds: int = None,
        period_seconds: int = None,
        success_threshold: int = None,
        tcp_socket: main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket = None,
        timeout_seconds: int = None,
    ):
        self.exec = exec
        # The minimum consecutive failures for the liveness check to be considered failed after having succeeded.
        # 
        # Default value: 3.
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        # The number of seconds after the container has started before the readiness check is initiated.
        self.initial_delay_seconds = initial_delay_seconds
        # The period for executing the liveness check, in seconds. Default value: 10. Minimum value: 1.
        self.period_seconds = period_seconds
        # The minimum consecutive successes for the liveness check to be considered successful after having failed. Default value: 1. The value must be 1.
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
        # The timeout period for the readiness check, in seconds. Default value: 1. Minimum value: 1.
        self.timeout_seconds = timeout_seconds

    def validate(self):
        if self.exec:
            self.exec.validate()
        if self.http_get:
            self.http_get.validate()
        if self.tcp_socket:
            self.tcp_socket.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec is not None:
            result['Exec'] = self.exec.to_map()

        if self.failure_threshold is not None:
            result['FailureThreshold'] = self.failure_threshold

        if self.http_get is not None:
            result['HttpGet'] = self.http_get.to_map()

        if self.initial_delay_seconds is not None:
            result['InitialDelaySeconds'] = self.initial_delay_seconds

        if self.period_seconds is not None:
            result['PeriodSeconds'] = self.period_seconds

        if self.success_threshold is not None:
            result['SuccessThreshold'] = self.success_threshold

        if self.tcp_socket is not None:
            result['TcpSocket'] = self.tcp_socket.to_map()

        if self.timeout_seconds is not None:
            result['TimeoutSeconds'] = self.timeout_seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Exec') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeExec()
            self.exec = temp_model.from_map(m.get('Exec'))

        if m.get('FailureThreshold') is not None:
            self.failure_threshold = m.get('FailureThreshold')

        if m.get('HttpGet') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet()
            self.http_get = temp_model.from_map(m.get('HttpGet'))

        if m.get('InitialDelaySeconds') is not None:
            self.initial_delay_seconds = m.get('InitialDelaySeconds')

        if m.get('PeriodSeconds') is not None:
            self.period_seconds = m.get('PeriodSeconds')

        if m.get('SuccessThreshold') is not None:
            self.success_threshold = m.get('SuccessThreshold')

        if m.get('TcpSocket') is not None:
            temp_model = main_models.ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket()
            self.tcp_socket = temp_model.from_map(m.get('TcpSocket'))

        if m.get('TimeoutSeconds') is not None:
            self.timeout_seconds = m.get('TimeoutSeconds')

        return self

class ModifyEciScalingConfigurationRequestContainersLivenessProbeTcpSocket(DaraModel):
    def __init__(
        self,
        port: int = None,
    ):
        # The port number on which the TCP socket check is performed when TCP socket is used for health checks.
        self.port = port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.port is not None:
            result['Port'] = self.port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Port') is not None:
            self.port = m.get('Port')

        return self

class ModifyEciScalingConfigurationRequestContainersLivenessProbeHttpGet(DaraModel):
    def __init__(
        self,
        path: str = None,
        port: int = None,
        scheme: str = None,
    ):
        # The path to which the HTTP GET request is sent when HTTP GET is used for health checks.
        self.path = path
        # The port number to which the HTTP GET request is sent when HTTP GET is used for health checks.
        self.port = port
        # The protocol type of the HTTP GET request when HTTP GET is used for health checks. Valid values:
        # - HTTP
        # - HTTPS
        self.scheme = scheme

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.port is not None:
            result['Port'] = self.port

        if self.scheme is not None:
            result['Scheme'] = self.scheme

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('Scheme') is not None:
            self.scheme = m.get('Scheme')

        return self

class ModifyEciScalingConfigurationRequestContainersLivenessProbeExec(DaraModel):
    def __init__(
        self,
        commands: List[str] = None,
    ):
        # The command executed in the container when the exec action is used for health checks.
        self.commands = commands

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commands is not None:
            result['Commands'] = self.commands

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Commands') is not None:
            self.commands = m.get('Commands')

        return self

class ModifyEciScalingConfigurationRequestAcrRegistryInfos(DaraModel):
    def __init__(
        self,
        domains: List[str] = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
    ):
        # The domain names of the ACR Enterprise Edition instance. By default, all domain names of the instance are used. You can specify individual domain names and separate multiple domain names with commas (,).
        self.domains = domains
        # The ID of the ACR Enterprise Edition instance.
        self.instance_id = instance_id
        # The name of the ACR Enterprise Edition instance.
        self.instance_name = instance_name
        # The region ID of the ACR Enterprise Edition instance.
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

