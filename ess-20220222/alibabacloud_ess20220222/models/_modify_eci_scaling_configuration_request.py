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
        # The Container Registry Enterprise Edition instances.
        self.acr_registry_infos = acr_registry_infos
        # The validity period of the scaling configuration. Unit: seconds.
        self.active_deadline_seconds = active_deadline_seconds
        # Specifies whether to automatically create elastic IP addresses (EIPs) and bind the EIPs to elastic container instances.
        self.auto_create_eip = auto_create_eip
        # Specifies whether to automatically match image caches.
        # 
        # Default value: false.
        self.auto_match_image_cache = auto_match_image_cache
        # The name series of elastic container instances. Naming conventions:
        # 
        # *   The name must be 2 to 128 characters in length.
        # *   The name can contain only lowercase letters, digits, and hyphens (-). It cannot start or end with a hyphen (-).
        self.container_group_name = container_group_name
        # The containers.
        self.containers = containers
        # The update mode of containers. Valid values:
        # 
        # *   RenewUpdate: full update mode. This value takes effect based on the value of Containers in an update request. This value indicates that the previous setting of Containers is overwritten.
        # *   IncrementalUpdate: incremental update mode. Container matching is performed based on the Container.name value. Only the parameters that are included in the request parameters are updated.
        # 
        # Default value: RenewUpdate.
        self.containers_update_type = containers_update_type
        # Specifies whether to enable the Cost Optimization feature. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        self.cost_optimization = cost_optimization
        # The number of vCPUs per elastic container instance.
        self.cpu = cpu
        # The number of physical CPU cores. You can specify this parameter for only specific ECS instance types. For more information, see [Specify CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_core = cpu_options_core
        # The number of threads per core. You can specify this parameter for only specific instance types. A value of 1 specifies that Hyper-Threading is disabled. For more information, see [Specify CPU options](https://help.aliyun.com/document_detail/197781.html).
        self.cpu_options_threads_per_core = cpu_options_threads_per_core
        # The bucket in which data caches are stored.
        self.data_cache_bucket = data_cache_bucket
        # Specifies whether to enable the Performance Burst feature for the ESSD AutoPL disk in which data caches are stored. Valid values:
        # 
        # *   true
        # *   false
        # 
        # Default value: false.
        # 
        # >  For more information about ESSD AutoPL disks, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_bursting_enabled = data_cache_bursting_enabled
        # The performance level (PL) of the cloud disk in which data caches are stored. We recommend that you use Enterprise SSDs (ESSDs). Valid values:
        # 
        # *   PL0: An ESSD can deliver up to 10,000 random read/write IOPS.
        # *   PL1: An ESSD can deliver up to 50,000 random read/write IOPS.
        # *   PL2: An ESSD can deliver up to 100,000 random read/write IOPS.
        # *   PL3: An ESSD can deliver up to 1,000,000 random read/write IOPS.
        # 
        # Default value: PL1.
        # 
        # >  For more information about ESSDs, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        self.data_cache_pl = data_cache_pl
        # The provisioned read/write IOPS of the ESSD AutoPL disk in which data caches are stored. Valid values: 0 to min{50,000, 1,000 × *Capacity - Baseline IOPS}. Baseline IOPS = min{1,800+50 x *Capacity, 50,000}.
        # 
        # >  For more information about ESSD AutoPL disks, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.data_cache_provisioned_iops = data_cache_provisioned_iops
        # >  This parameter is unavailable for use.
        self.description = description
        # The IP addresses of DNS servers.
        self.dns_config_name_servers = dns_config_name_servers
        # The options. Each option is a name-value pair. The value in the name-value pair is optional.
        self.dns_config_options = dns_config_options
        # The search domains of DNS servers.
        self.dns_config_searchs = dns_config_searchs
        # The Domain Name System (DNS) policy. Valid values:
        # 
        # *   None: uses the DNS that is specified by DnsConfig.
        # *   Default: uses the DNS that is specified for the runtime environment.
        self.dns_policy = dns_policy
        # The maximum outbound bandwidth. Unit: bit/s.
        self.egress_bandwidth = egress_bandwidth
        # The EIP bandwidth.
        # 
        # Default value: 5. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # >  This parameter is not available for use.
        self.enable_sls = enable_sls
        # The size of the temporary storage space. By default, an Enterprise SSD (ESSD) of the PL1 type is used. Unit: GiB.
        self.ephemeral_storage = ephemeral_storage
        # The version of the GPU driver. Valid values:
        # 
        # *   tesla=470.82.01 (default)
        # *   tesla=525.85.12
        # 
        # >  You can switch the GPU driver version only for a few Elastic Compute Service (ECS) instance types. For more information, see [Specify GPU-accelerated ECS instance types to create an elastic container instance](https://help.aliyun.com/document_detail/2579486.html).
        self.gpu_driver_version = gpu_driver_version
        # The hosts.
        self.host_aliases = host_aliases
        # The hostname series of elastic container instances.
        self.host_name = host_name
        # The image repositories.
        self.image_registry_credentials = image_registry_credentials
        # The ID of the image cache.
        self.image_snapshot_id = image_snapshot_id
        # The maximum inbound bandwidth. Unit: bit/s.
        self.ingress_bandwidth = ingress_bandwidth
        # The init containers.
        self.init_containers = init_containers
        # The level of the instance family, which is used to filter instance types that meet the specified criteria. This parameter takes effect only if you set `CostOptimization` to true. Valid values:
        # 
        # *   EntryLevel: entry level (shared instance type). Instance types of this level are the most cost-effective but may not provide stable computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low. For more information, see [Shared instance families](https://help.aliyun.com/document_detail/108489.html).
        # *   EnterpriseLevel: enterprise level. Instance types of this level provide stable performance and dedicated resources, and are suitable for business scenarios that require high stability. For more information, see [Overview of instance families](https://help.aliyun.com/document_detail/25378.html).
        # *   CreditEntryLevel: credit-based entry level (burstable instance types). CPU credits are used to ensure computing performance. Instance types of this level are suitable for scenarios in which the CPU utilization is low but may fluctuate in specific cases. For more information, see [Overview](https://help.aliyun.com/document_detail/59977.html) of burstable instances.
        self.instance_family_level = instance_family_level
        # The ECS instance types. You can specify up to five instance types.
        self.instance_types = instance_types
        # The number of IPv6 addresses.
        self.ipv_6address_count = ipv_6address_count
        # The load balancing weight of each backend server. Valid values: 1 to 100.
        self.load_balancer_weight = load_balancer_weight
        # The memory size per elastic container instance. Unit: GiB.
        self.memory = memory
        # The endpoints of Network Time Protocol (NTP) servers.
        self.ntp_servers = ntp_servers
        # Specifies whether to override existing data. Valid Values:
        # 
        # true false
        self.override = override
        self.owner_id = owner_id
        # The name of the instance Resource Access Management (RAM) role. You can use the same RAM role to access elastic container instances and Elastic Compute Service (ECS) instances. For more information, see [Use an instance RAM role by calling API operations](https://help.aliyun.com/document_detail/61178.html).
        self.ram_role_name = ram_role_name
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        self.resource_owner_account = resource_owner_account
        # The instance restart policy. Valid values:
        # 
        # *   Always: always restarts elastic container instances.
        # *   Never: never restarts elastic container instances.
        # *   OnFailure: restarts elastic container instances upon failures.
        # 
        # Default value: Always.
        self.restart_policy = restart_policy
        # The ID of the scaling configuration that you want to modify.
        # 
        # This parameter is required.
        self.scaling_configuration_id = scaling_configuration_id
        # The name of the scaling configuration. The name must be 2 to 64 characters in length, and can contain letters, digits, underscores (_), hyphens (-), and periods (.). The name must start with a letter or a digit.
        # 
        # The name of a scaling configuration must be unique in the specified region. If you do not specify this parameter, the value of ScalingConfigurationId is used.
        self.scaling_configuration_name = scaling_configuration_name
        # The security contexts in which the elastic container instance runs.
        self.security_context_sys_ctls = security_context_sys_ctls
        # The ID of the security group to which elastic container instances belong. Elastic container instances that belong to the same security group can communicate with each other.
        # 
        # If you do not specify a security group, the system uses the default security group in the region that you selected. Make sure that the inbound rules of the security group contain the protocols and port numbers of the containers that you want to expose. If you do not have a default security group in the region, the system creates a default security group and then adds the container protocols and port numbers that you specified to the inbound rules of the security group.
        self.security_group_id = security_group_id
        # The maximum hourly price of preemptible elastic container instances. The value can be accurate to three decimal places.
        # 
        # If you set SpotStrategy to SpotWithPriceLimit, you must specify SpotPriceLimit.
        self.spot_price_limit = spot_price_limit
        # The instance bidding policy. Valid values:
        # 
        # *   NoSpot: The instances are created as pay-as-you-go instances.
        # *   SpotWithPriceLimit: The instances are preemptible instances for which you can specify the maximum hourly price.
        # *   SpotAsPriceGo: The instances are created as preemptible instances for which the market price at the time of purchase is used as the bid price.
        # 
        # Default value: NoSpot.
        self.spot_strategy = spot_strategy
        # The tags.
        self.tags = tags
        # The buffer period during which the program handles operations before the program is stopped. Unit: seconds.
        self.termination_grace_period_seconds = termination_grace_period_seconds
        # The volumes.
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
        # The paths to the configuration files.
        self.config_file_volume_config_file_to_path = config_file_volume_config_file_to_path
        # The default permissions on the ConfigFile volume.
        self.config_file_volume_default_mode = config_file_volume_default_mode
        # The volume name.
        self.name = name
        # The type of the Host directory. Examples: File, Directory, and Socket.
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
        # The permissions on the ConfigFile volume.
        self.mode = mode
        # The relative path to the configuration file.
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
        self.path = path
        self.read_only = read_only
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
        self.path = path
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
        self.driver = driver
        self.fs_type = fs_type
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
        self.medium = medium
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
        self.disk_id = disk_id
        self.disk_size = disk_size
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
        # The variable name of the security context in which the elastic container instance runs.
        self.name = name
        # The variable value of the security context in which the elastic container instance runs.
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
        # The container startup arguments.
        self.args = args
        # The commands that you can run to start the init container.
        self.commands = commands
        # The number of vCPUs per init container.
        self.cpu = cpu
        # The number of GPUs per init container.
        self.gpu = gpu
        # The image of the init container.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Image pulling is performed each time instances are created.
        # *   IfNotPresent: Image pulling is performed as needed. On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The environment variables of the init container.
        self.init_container_environment_vars = init_container_environment_vars
        # The ports of the init container.
        self.init_container_ports = init_container_ports
        # The volume mounts of the init container.
        self.init_container_volume_mounts = init_container_volume_mounts
        # The memory size per init container. Unit: GiB.
        self.memory = memory
        # The name of the init container.
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
        # The directory within the init container onto which you want to mount the volume.
        # 
        # >  The information stored within this directory is overwritten by the data on the mounted volume. Exercise caution when you specify this parameter.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation enables volumes mounted on one container to be shared among other containers within the same pod or across distinct pods residing on the same node. Valid values:
        # 
        # *   None: Subsequent mounts executed on the volume or its subdirectories do not propagate to the volume.
        # *   HostToCotainer: Subsequent mounts executed on the volume or its subdirectories propagate to the volume.
        # *   Bidirectional: This value is similar to HostToCotainer. Subsequent mounts executed on the volume or its subdirectories propagate to the volume. In addition, volume mounts executed on the container propagate back to the underlying instance and to all containers across every pod that uses the same volume.
        # 
        # Default value: None.
        self.mount_propagation = mount_propagation
        # The name of the volume.
        self.name = name
        # Specifies whether the mount path is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The volume subdirectory. The pod can mount different directories of the same volume to different subdirectories of init containers.
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
        # *   TCP
        # *   UDP
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
        # The name of the environment variable. The name can be 1 to 128 characters in length, and can contain letters, underscores (_), and digits. The name cannot start with a digit. Specify the value in the `[0-9a-zA-Z]` format.
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
        self.read_only_root_filesystem = read_only_root_filesystem
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
        # The password of the image repository.
        self.password = password
        # The address of the image repository.
        self.server = server
        # The username of the image repository.
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
        # The names of the hosts that you want to add.
        self.hostnames = hostnames
        # The IP address that you want to add.
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
        # The variable name of the option.
        self.name = name
        # The variable value of the option.
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
        # The container startup arguments. You can specify up to 10 arguments.
        self.args = args
        # The commands that you can run in the container when you use the CLI to perform a liveness probe.
        self.commands = commands
        # The number of vCPUs per container.
        self.cpu = cpu
        # The environment variables.
        self.environment_vars = environment_vars
        # The number of GPUs per container.
        self.gpu = gpu
        # The container image.
        self.image = image
        # The image pulling policy. Valid values:
        # 
        # *   Always: Image pulling is performed each time instances are created.
        # *   IfNotPresent: Image pulling is performed as needed. On-premises images are preferentially used. If no on-premises images are available, image pulling is performed.
        # *   Never: On-premises images are always used. Image pulling is not performed.
        self.image_pull_policy = image_pull_policy
        # The commands that you can run within the container to configure the postStart callback function.
        self.lifecycle_post_start_handler_execs = lifecycle_post_start_handler_execs
        # The IP address of the host to which you want to send the HTTP GET request to configure the postStart callback function.
        self.lifecycle_post_start_handler_http_get_host = lifecycle_post_start_handler_http_get_host
        # The path to which you want to send the HTTP GET request to configure the postStart callback function.
        self.lifecycle_post_start_handler_http_get_path = lifecycle_post_start_handler_http_get_path
        # The port over which you want to send the HTTP GET request to configure the postStart callback function.
        self.lifecycle_post_start_handler_http_get_port = lifecycle_post_start_handler_http_get_port
        # The protocol type of the HTTP GET request that you want to send to configure the postStart callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_post_start_handler_http_get_scheme = lifecycle_post_start_handler_http_get_scheme
        # The IP address of the host detected by the TCP socket that you want to use to configure the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_host = lifecycle_post_start_handler_tcp_socket_host
        # The port detected by the TCP socket that you want to use to configure the postStart callback function.
        self.lifecycle_post_start_handler_tcp_socket_port = lifecycle_post_start_handler_tcp_socket_port
        # The commands that you can run within the container to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_execs = lifecycle_pre_stop_handler_execs
        # The IP address of the host to which you want to send the HTTP GET request to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_host = lifecycle_pre_stop_handler_http_get_host
        # The path to which you want to send the HTTP GET request to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_path = lifecycle_pre_stop_handler_http_get_path
        # The port over which you want to send the HTTP GET request to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_http_get_port = lifecycle_pre_stop_handler_http_get_port
        # The protocol type of the HTTP GET request that you want to send to configure the preStop callback function. Valid values:
        # 
        # *   HTTP
        # *   HTTPS
        self.lifecycle_pre_stop_handler_http_get_scheme = lifecycle_pre_stop_handler_http_get_scheme
        # The IP address of the host detected by the TCP socket that you want to use to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_host = lifecycle_pre_stop_handler_tcp_socket_host
        # The port detected by the TCP socket that you want to use to configure the preStop callback function.
        self.lifecycle_pre_stop_handler_tcp_socket_port = lifecycle_pre_stop_handler_tcp_socket_port
        # The memory size per container. Unit: GiB.
        self.memory = memory
        # The name of the container image.
        self.name = name
        # The ports.
        self.ports = ports
        # Specifies whether the container allocates buffer resources to standard input streams during its active runtime. If you do not specify this parameter, an end-of-file (EOF) error occurs when standard input streams in the container are read.
        # 
        # Default value: false.
        self.stdin = stdin
        # Specifies whether standard input streams remain connected during multiple sessions when StdinOnce is set to true.
        # 
        # If you set StdinOnce to true, standard input streams are connected after the container is started, and remain idle until a client is connected to receive data. After the client is disconnected, streams are also disconnected and remain disconnected until the container is restarted.
        self.stdin_once = stdin_once
        # Specifies whether to enable Interaction. Default value: false.
        # 
        # If the command is a /bin/bash command, set this parameter to true.
        self.tty = tty
        # The volume mounts of the container.
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
        # The directory within the container onto which you want to mount the volume.
        # 
        # >  The information stored within this directory is overwritten by the data on the mounted volume. Exercise caution when you specify this parameter.
        self.mount_path = mount_path
        # The mount propagation settings of the volume. Mount propagation enables volumes mounted on one container to be shared among other containers within the same pod or across distinct pods residing on the same node. Valid values:
        # 
        # *   None: Subsequent mounts executed on the volume or its subdirectories do not propagate to the volume.
        # *   HostToCotainer: Subsequent mounts executed on the volume or its subdirectories propagate to the volume.
        # *   Bidirectional: This value is similar to HostToCotainer. Subsequent mounts executed on the volume or its subdirectories propagate to the volume. In addition, volume mounts executed on the container propagate back to the underlying instance and to all containers across every pod that uses the same volume.
        self.mount_propagation = mount_propagation
        # The volume name. The value of this parameter is the same as the name of the volume that is mounted to containers.
        self.name = name
        # Specifies whether the volume is read-only.
        # 
        # Default value: false.
        self.read_only = read_only
        # The volume subdirectory.
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
        # *   TCP
        # *   UDP
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
        # The name of the environment variable. The name can be 1 to 128 characters in length, and can contain letters, underscores (_), and digits. The name cannot start with a digit. Specify the value in the `[0-9a-zA-Z]` format.
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
        self.read_only_root_filesystem = read_only_root_filesystem
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
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
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
        self.path = path
        self.port = port
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
        self.failure_threshold = failure_threshold
        self.http_get = http_get
        self.initial_delay_seconds = initial_delay_seconds
        self.period_seconds = period_seconds
        self.success_threshold = success_threshold
        self.tcp_socket = tcp_socket
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
        self.path = path
        self.port = port
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
        # The domain names of the Container Registry Enterprise Edition instance. By default, all domain names of the instance are displayed. Separate multiple domain names with commas (,).
        self.domains = domains
        # The ID of the Container Registry Enterprise Edition instance.
        self.instance_id = instance_id
        # The name of the Container Registry Enterprise Edition instance.
        self.instance_name = instance_name
        # The region ID of the Container Registry Enterprise Edition instance.
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

