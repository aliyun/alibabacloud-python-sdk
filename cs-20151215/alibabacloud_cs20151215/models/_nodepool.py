# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class Nodepool(DaraModel):
    def __init__(
        self,
        auto_scaling: main_models.NodepoolAutoScaling = None,
        count: int = None,
        interconnect_config: main_models.NodepoolInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: main_models.NodepoolKubernetesConfig = None,
        management: main_models.NodepoolManagement = None,
        max_nodes: int = None,
        node_components: List[main_models.NodepoolNodeComponents] = None,
        node_config: main_models.NodepoolNodeConfig = None,
        nodepool_info: main_models.NodepoolNodepoolInfo = None,
        scaling_group: main_models.NodepoolScalingGroup = None,
        tee_config: main_models.NodepoolTeeConfig = None,
    ):
        # The auto-scaling node pool configuration.
        self.auto_scaling = auto_scaling
        # **[Deprecated]** Use desired_size instead. The number of nodes in the node pool.
        self.count = count
        # **[Deprecated]** The configuration of the edge node pool.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter is valid only when type is set to edge. Valid values:
        # - basic: basic.
        # - private: dedicated. Supported in Kubernetes 1.22 and later.
        self.interconnect_mode = interconnect_mode
        # The cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # The managed node pool configuration.
        self.management = management
        # The maximum number of nodes that the edge node pool can accommodate. The value must be greater than or equal to 0. A value of 0 indicates no extra limit, meaning the node pool is only limited by the maximum number of nodes that the entire cluster can accommodate. This value is usually greater than 0 for edge node pools. For ess node pools and default edge node pools, this value is 0.
        self.max_nodes = max_nodes
        # The list of node components.
        self.node_components = node_components
        # The node configuration.
        self.node_config = node_config
        # The node pool configuration.
        self.nodepool_info = nodepool_info
        # The scaling group configuration of the node pool.
        self.scaling_group = scaling_group
        # The configuration of the confidential computing node pool.
        self.tee_config = tee_config

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.interconnect_config:
            self.interconnect_config.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
        if self.node_components:
            for v1 in self.node_components:
                 if v1:
                    v1.validate()
        if self.node_config:
            self.node_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()

        if self.count is not None:
            result['count'] = self.count

        if self.interconnect_config is not None:
            result['interconnect_config'] = self.interconnect_config.to_map()

        if self.interconnect_mode is not None:
            result['interconnect_mode'] = self.interconnect_mode

        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()

        if self.management is not None:
            result['management'] = self.management.to_map()

        if self.max_nodes is not None:
            result['max_nodes'] = self.max_nodes

        result['node_components'] = []
        if self.node_components is not None:
            for k1 in self.node_components:
                result['node_components'].append(k1.to_map() if k1 else None)

        if self.node_config is not None:
            result['node_config'] = self.node_config.to_map()

        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()

        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()

        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = main_models.NodepoolAutoScaling()
            self.auto_scaling = temp_model.from_map(m.get('auto_scaling'))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('interconnect_config') is not None:
            temp_model = main_models.NodepoolInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m.get('interconnect_config'))

        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')

        if m.get('kubernetes_config') is not None:
            temp_model = main_models.NodepoolKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('kubernetes_config'))

        if m.get('management') is not None:
            temp_model = main_models.NodepoolManagement()
            self.management = temp_model.from_map(m.get('management'))

        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')

        self.node_components = []
        if m.get('node_components') is not None:
            for k1 in m.get('node_components'):
                temp_model = main_models.NodepoolNodeComponents()
                self.node_components.append(temp_model.from_map(k1))

        if m.get('node_config') is not None:
            temp_model = main_models.NodepoolNodeConfig()
            self.node_config = temp_model.from_map(m.get('node_config'))

        if m.get('nodepool_info') is not None:
            temp_model = main_models.NodepoolNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('nodepool_info'))

        if m.get('scaling_group') is not None:
            temp_model = main_models.NodepoolScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('scaling_group'))

        if m.get('tee_config') is not None:
            temp_model = main_models.NodepoolTeeConfig()
            self.tee_config = temp_model.from_map(m.get('tee_config'))

        return self

class NodepoolTeeConfig(DaraModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        # Specifies whether the node pool is a confidential computing node pool.
        # 
        # This parameter is required.
        self.tee_enable = tee_enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')

        return self

class NodepoolScalingGroup(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        cpu_options: main_models.NodepoolScalingGroupCpuOptions = None,
        data_disks: List[main_models.DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        disk_init: List[main_models.DiskInit] = None,
        image_id: str = None,
        image_type: str = None,
        instance_charge_type: str = None,
        instance_metadata_options: main_models.InstanceMetadataOptions = None,
        instance_patterns: List[main_models.InstancePatterns] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair: str = None,
        login_as_non_root: bool = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: main_models.NodepoolScalingGroupPrivatePoolOptions = None,
        ram_role_name: str = None,
        rds_instances: List[str] = None,
        resource_pool_options: main_models.NodepoolScalingGroupResourcePoolOptions = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[main_models.NodepoolScalingGroupSpotPriceLimit] = None,
        spot_strategy: str = None,
        system_disk_bursting_enabled: bool = None,
        system_disk_categories: List[str] = None,
        system_disk_category: str = None,
        system_disk_encrypt_algorithm: str = None,
        system_disk_encrypted: bool = None,
        system_disk_kms_key_id: str = None,
        system_disk_performance_level: str = None,
        system_disk_provisioned_iops: int = None,
        system_disk_size: int = None,
        tags: List[main_models.NodepoolScalingGroupTags] = None,
        vswitch_ids: List[str] = None,
    ):
        # Specifies whether to enable auto-renewal for the node pool. This parameter takes effect only when instance_charge_type is set to PrePaid. Valid values:
        # - true: Enables auto-renewal.
        # - false: Disables auto-renewal.
        # 
        # Default value: true.
        self.auto_renew = auto_renew
        # The auto-renewal epoch for the node pool. This parameter is required and takes effect only when `instance_charge_type` is set to `PrePaid`.
        # 
        # If `PeriodUnit` is set to `Month`, valid values are 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to automatically create pay-as-you-go instances to meet the required number of ECS instances when multi_az_policy is set to COST_OPTIMIZED and sufficient spot instances cannot be created due to price or inventory constraints. Valid values:
        # - true: Allows automatic creation of pay-as-you-go instances to meet the required number of ECS instances.
        # - false: Does not allow automatic creation of pay-as-you-go instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The CPU configuration options.
        self.cpu_options = cpu_options
        # The data cloud disk configuration for the nodes in the node pool.
        self.data_disks = data_disks
        # The ID of the deployment set.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The block device initialization configuration.
        self.disk_init = disk_init
        # The ID of the custom image. By default, the system-provided image is used.
        self.image_id = image_id
        # The type of the operating system image. This parameter and platform are mutually exclusive. Valid values:
        # - AliyunLinux: Alinux2 image.
        # - AliyunLinux3: Alinux3 image.
        # - AliyunLinux3Arm64: Alinux3 ARM image.
        # - AliyunLinuxUEFI: Alinux2 UEFI image.
        # - CentOS: CentOS image.
        # - Windows: Windows image.
        # - WindowsCore: Windows Core image.
        # - ContainerOS: Container-optimized image.
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # - PrePaid: Subscription.
        # - PostPaid: Pay-as-you-go.
        # 
        # Default value: PostPaid.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The metadata access configuration for the ECS instance. This parameter is currently available only to whitelisted users. To use this parameter, submit a ticket.
        self.instance_metadata_options = instance_metadata_options
        # The instance properties.
        self.instance_patterns = instance_patterns
        # The instance types.
        # 
        # This parameter is required.
        self.instance_types = instance_types
        # The billing method for public IP addresses. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth for a public IP address of a node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must specify this parameter or `login_password`.
        # 
        # > If you create a managed node pool, only `key_pair` is supported.
        self.key_pair = key_pair
        # Specifies whether to log on to the created ECS instances as a non-root user.
        self.login_as_non_root = login_as_non_root
        # The SSH logon password. You must specify this parameter or `key_pair`. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The scaling policy for ECS instances in a multi-zone scaling group. Valid values:
        # 
        # - `PRIORITY`: scales ECS instances based on the priorities of vSwitches that you specify in VSwitchIds.N. If an ECS instance cannot be created in the zone of the highest-priority vSwitch, the system automatically uses the next highest-priority vSwitch to create the ECS instance.
        # 
        # - `COST_OPTIMIZED`: creates ECS instances based on the unit prices of vCPUs in ascending order. If the scaling configuration settings specify multiple instance types and the billing method for spot instances, the system preferentially creates the corresponding spot instances. You can use the `CompensateWithOnDemand` parameter to specify whether the system automatically creates pay-as-you-go instances when spot instances cannot be created due to insufficient resources.
        # 
        #   > `COST_OPTIMIZED` takes effect only when the scaling configuration settings specify multiple instance types or spot instances are selected.
        # 
        # - `BALANCE`: evenly distributes ECS instances across the zones specified in the scaling group. If the instances are unevenly distributed across zones due to insufficient resources, you can call the RebalanceInstances operation to balance the resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than this value, the system preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the minimum number of pay-as-you-go instances specified by `on_demand_base_capacity`. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of nodes in the node pool. This parameter is required and takes effect only when `instance_charge_type` is set to `PrePaid`. When `period_unit` is set to Month, valid values of `period` are 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.period = period
        # The subscription period of nodes in the node pool. You must specify this parameter when `instance_charge_type` is set to `PrePaid`.
        # 
        # `Month`: only months are supported.
        self.period_unit = period_unit
        # The operating system distribution. Valid values:
        # 
        # - `CentOS`
        # - `AliyunLinux`
        # - `Windows`
        # - `WindowsCore`
        # 
        # Default value: `AliyunLinux`.
        self.platform = platform
        # The private pool options.
        self.private_pool_options = private_pool_options
        # The name of the RAM role for worker nodes.
        # >Notice: Only ACK managed clusters of version 1.22 and later support configuring this parameter when you create a node pool.</notice>
        self.ram_role_name = ram_role_name
        # The list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The resource pool and resource pool policy used to create instances. Take note of the following items when you configure this parameter:
        # This parameter takes effect only when you create pay-as-you-go instances.
        # This parameter cannot be configured together with private_pool_options.match_criteria or private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # The scaling group mode. Valid values:
        # 
        # - `release`: standard pattern. The scaling group scales instances by creating and releasing ECS instances based on the usage of the requested resources.
        # - `recycle`: swift pattern. The scaling group scales instances by creating, stopping, and starting ECS instances to accelerate subsequent scaling operations. When an instance is stopped, you are not charged for compute resources, but you are still charged for storage resources, except for instances with local disks.
        # 
        # Default value: `release`.
        self.scaling_policy = scaling_policy
        # The ID of the security group to which the node pool belongs. You must specify this parameter or `security_group_ids`. We recommend that you specify `security_group_ids`.
        self.security_group_id = security_group_id
        # The list of security group IDs. You must specify this parameter or `security_group_id`. We recommend that you specify `security_group_ids`. If you specify both `security_group_id` and `security_group_ids`, `security_group_ids` takes precedence.
        self.security_group_ids = security_group_ids
        # The number of active instance types. The scaling group evenly creates spot instances based on the most cost-effective instance types. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable spot instance replenishment. After this feature is enabled, when the scaling group receives a system message indicating that a spot instance will be reclaimed, the scaling group attempts to create a new instance to replace the spot instance to be reclaimed. Valid values:
        # 
        # - `true`: enables spot instance replenishment.
        # - `false`: disables spot instance replenishment.
        self.spot_instance_remedy = spot_instance_remedy
        # The maximum price configuration for a single spot instance of a specific instance type in the current marketplace.
        self.spot_price_limit = spot_price_limit
        # The type of spot instance. Valid values:
        # - NoSpot: non-spot instance.
        # - SpotWithPriceLimit: spot instance with a maximum price.
        # - SpotAsPriceGo: spot instance whose price is automatically set by the system based on the current market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable bursting for the system disk of the node. Valid values:
        # 
        # - true: yes.
        # - false: no.
        # 
        # This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The categories of the system disk. If the system disk cannot be created by using the disk category with the highest priority, the system automatically tries the next disk category. Valid values:
        # 
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        self.system_disk_categories = system_disk_categories
        # The category of the system disk. Valid values:
        # 
        # - `cloud_efficiency`: ultra disk.
        # - `cloud_ssd`: standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL cloud disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # The encryption algorithm used for the system disk. Valid value: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # - true: encrypts the system disk.
        # - false: does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key used for the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system disk. This parameter takes effect only for ESSDs. Valid values:
        # 
        # - PL0: delivers medium maximum concurrent I/O performance and relatively stable read/write latency.
        # - PL1: delivers medium maximum concurrent I/O performance and relatively stable read/write latency.
        # - PL2: delivers high maximum concurrent I/O performance and stable read/write latency.
        # - PL3: delivers ultra-high maximum concurrent I/O performance and extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read and write IOPS for the system cloud disk of the node. Valid values: 0 to min{50,000, 1000 × Capacity - Baseline performance}. Baseline performance = min{1,800 + 50 × Capacity, 50,000}. This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system cloud disk for the node. Unit: GiB. Valid values: 40 to 500.
        self.system_disk_size = system_disk_size
        # The tags to add to ECS instances only. Tag keys must be unique and can be up to 128 characters in length. Neither tag keys nor tag values can start with "aliyun" or "acs:", or contain "https://" or "http://".
        self.tags = tags
        # The vSwitch IDs.
        # 
        # This parameter is required.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.cpu_options:
            self.cpu_options.validate()
        if self.data_disks:
            for v1 in self.data_disks:
                 if v1:
                    v1.validate()
        if self.disk_init:
            for v1 in self.disk_init:
                 if v1:
                    v1.validate()
        if self.instance_metadata_options:
            self.instance_metadata_options.validate()
        if self.instance_patterns:
            for v1 in self.instance_patterns:
                 if v1:
                    v1.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
        if self.resource_pool_options:
            self.resource_pool_options.validate()
        if self.spot_price_limit:
            for v1 in self.spot_price_limit:
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
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew

        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period

        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand

        if self.cpu_options is not None:
            result['cpu_options'] = self.cpu_options.to_map()

        result['data_disks'] = []
        if self.data_disks is not None:
            for k1 in self.data_disks:
                result['data_disks'].append(k1.to_map() if k1 else None)

        if self.deploymentset_id is not None:
            result['deploymentset_id'] = self.deploymentset_id

        if self.desired_size is not None:
            result['desired_size'] = self.desired_size

        result['disk_init'] = []
        if self.disk_init is not None:
            for k1 in self.disk_init:
                result['disk_init'].append(k1.to_map() if k1 else None)

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type

        if self.instance_metadata_options is not None:
            result['instance_metadata_options'] = self.instance_metadata_options.to_map()

        result['instance_patterns'] = []
        if self.instance_patterns is not None:
            for k1 in self.instance_patterns:
                result['instance_patterns'].append(k1.to_map() if k1 else None)

        if self.instance_types is not None:
            result['instance_types'] = self.instance_types

        if self.internet_charge_type is not None:
            result['internet_charge_type'] = self.internet_charge_type

        if self.internet_max_bandwidth_out is not None:
            result['internet_max_bandwidth_out'] = self.internet_max_bandwidth_out

        if self.key_pair is not None:
            result['key_pair'] = self.key_pair

        if self.login_as_non_root is not None:
            result['login_as_non_root'] = self.login_as_non_root

        if self.login_password is not None:
            result['login_password'] = self.login_password

        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy

        if self.on_demand_base_capacity is not None:
            result['on_demand_base_capacity'] = self.on_demand_base_capacity

        if self.on_demand_percentage_above_base_capacity is not None:
            result['on_demand_percentage_above_base_capacity'] = self.on_demand_percentage_above_base_capacity

        if self.period is not None:
            result['period'] = self.period

        if self.period_unit is not None:
            result['period_unit'] = self.period_unit

        if self.platform is not None:
            result['platform'] = self.platform

        if self.private_pool_options is not None:
            result['private_pool_options'] = self.private_pool_options.to_map()

        if self.ram_role_name is not None:
            result['ram_role_name'] = self.ram_role_name

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.resource_pool_options is not None:
            result['resource_pool_options'] = self.resource_pool_options.to_map()

        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy

        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id

        if self.security_group_ids is not None:
            result['security_group_ids'] = self.security_group_ids

        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools

        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy

        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k1 in self.spot_price_limit:
                result['spot_price_limit'].append(k1.to_map() if k1 else None)

        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy

        if self.system_disk_bursting_enabled is not None:
            result['system_disk_bursting_enabled'] = self.system_disk_bursting_enabled

        if self.system_disk_categories is not None:
            result['system_disk_categories'] = self.system_disk_categories

        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category

        if self.system_disk_encrypt_algorithm is not None:
            result['system_disk_encrypt_algorithm'] = self.system_disk_encrypt_algorithm

        if self.system_disk_encrypted is not None:
            result['system_disk_encrypted'] = self.system_disk_encrypted

        if self.system_disk_kms_key_id is not None:
            result['system_disk_kms_key_id'] = self.system_disk_kms_key_id

        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level

        if self.system_disk_provisioned_iops is not None:
            result['system_disk_provisioned_iops'] = self.system_disk_provisioned_iops

        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')

        if m.get('auto_renew_period') is not None:
            self.auto_renew_period = m.get('auto_renew_period')

        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')

        if m.get('cpu_options') is not None:
            temp_model = main_models.NodepoolScalingGroupCpuOptions()
            self.cpu_options = temp_model.from_map(m.get('cpu_options'))

        self.data_disks = []
        if m.get('data_disks') is not None:
            for k1 in m.get('data_disks'):
                temp_model = main_models.DataDisk()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('deploymentset_id') is not None:
            self.deploymentset_id = m.get('deploymentset_id')

        if m.get('desired_size') is not None:
            self.desired_size = m.get('desired_size')

        self.disk_init = []
        if m.get('disk_init') is not None:
            for k1 in m.get('disk_init'):
                temp_model = main_models.DiskInit()
                self.disk_init.append(temp_model.from_map(k1))

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')

        if m.get('instance_metadata_options') is not None:
            temp_model = main_models.InstanceMetadataOptions()
            self.instance_metadata_options = temp_model.from_map(m.get('instance_metadata_options'))

        self.instance_patterns = []
        if m.get('instance_patterns') is not None:
            for k1 in m.get('instance_patterns'):
                temp_model = main_models.InstancePatterns()
                self.instance_patterns.append(temp_model.from_map(k1))

        if m.get('instance_types') is not None:
            self.instance_types = m.get('instance_types')

        if m.get('internet_charge_type') is not None:
            self.internet_charge_type = m.get('internet_charge_type')

        if m.get('internet_max_bandwidth_out') is not None:
            self.internet_max_bandwidth_out = m.get('internet_max_bandwidth_out')

        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')

        if m.get('login_as_non_root') is not None:
            self.login_as_non_root = m.get('login_as_non_root')

        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')

        if m.get('multi_az_policy') is not None:
            self.multi_az_policy = m.get('multi_az_policy')

        if m.get('on_demand_base_capacity') is not None:
            self.on_demand_base_capacity = m.get('on_demand_base_capacity')

        if m.get('on_demand_percentage_above_base_capacity') is not None:
            self.on_demand_percentage_above_base_capacity = m.get('on_demand_percentage_above_base_capacity')

        if m.get('period') is not None:
            self.period = m.get('period')

        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')

        if m.get('platform') is not None:
            self.platform = m.get('platform')

        if m.get('private_pool_options') is not None:
            temp_model = main_models.NodepoolScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('private_pool_options'))

        if m.get('ram_role_name') is not None:
            self.ram_role_name = m.get('ram_role_name')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('resource_pool_options') is not None:
            temp_model = main_models.NodepoolScalingGroupResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('resource_pool_options'))

        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')

        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')

        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')

        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k1 in m.get('spot_price_limit'):
                temp_model = main_models.NodepoolScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k1))

        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')

        if m.get('system_disk_bursting_enabled') is not None:
            self.system_disk_bursting_enabled = m.get('system_disk_bursting_enabled')

        if m.get('system_disk_categories') is not None:
            self.system_disk_categories = m.get('system_disk_categories')

        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')

        if m.get('system_disk_encrypt_algorithm') is not None:
            self.system_disk_encrypt_algorithm = m.get('system_disk_encrypt_algorithm')

        if m.get('system_disk_encrypted') is not None:
            self.system_disk_encrypted = m.get('system_disk_encrypted')

        if m.get('system_disk_kms_key_id') is not None:
            self.system_disk_kms_key_id = m.get('system_disk_kms_key_id')

        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')

        if m.get('system_disk_provisioned_iops') is not None:
            self.system_disk_provisioned_iops = m.get('system_disk_provisioned_iops')

        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.NodepoolScalingGroupTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        return self

class NodepoolScalingGroupTags(DaraModel):
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
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class NodepoolScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # The maximum price for a single instance.
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type

        if self.price_limit is not None:
            result['price_limit'] = self.price_limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')

        if m.get('price_limit') is not None:
            self.price_limit = m.get('price_limit')

        return self

class NodepoolScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # The list of private pool IDs, which are the IDs of elasticity assurances or capacity reservations. You can only specify the IDs of private pools in Target mode. Valid values of N: 1 to 20.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy used to create instances. Resource pools include private pools generated after elasticity assurances or capacity reservations take effect, as well as the public pool. You can select a resource pool when you start instances. Valid values:
        # PrivatePoolFirst: private pools take precedence. If you select this policy and specify resource_pool_options.private_pool_ids, the specified private pools are preferentially used. If no private pool is specified or the specified private pools have insufficient capacity, the system automatically matches an open private pool. If no matching private pool is found, the system uses the public pool to create instances.
        # PrivatePoolOnly: only private pools are used. If you select this policy, you must specify resource_pool_options.private_pool_ids. If the specified private pools have insufficient capacity, the instances fail to start.
        # None: no resource pool policy is used.
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
            result['private_pool_ids'] = self.private_pool_ids

        if self.strategy is not None:
            result['strategy'] = self.strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('private_pool_ids') is not None:
            self.private_pool_ids = m.get('private_pool_ids')

        if m.get('strategy') is not None:
            self.strategy = m.get('strategy')

        return self

class NodepoolScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private pool.
        self.id = id
        # The type of the private pool, which specifies the capacity options of the private pool for instance startup. After an elasticity assurance or capacity reservation takes effect, a private pool is generated for you to select when you start instances. Valid values:
        # 
        # - `Open`: open mode. The system automatically matches an open private pool. If no matching open private pool is found, the system uses resources from the public pool.
        # 
        # - `Target`: targeted mode. The system uses the specified private pool to start instances. If the specified private pool is unavailable, the instances fail to start.
        # 
        # - `None`: no private pool. The system does not use private pools to start instances.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.match_criteria is not None:
            result['match_criteria'] = self.match_criteria

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('match_criteria') is not None:
            self.match_criteria = m.get('match_criteria')

        return self

class NodepoolScalingGroupCpuOptions(DaraModel):
    def __init__(
        self,
        nested_virtualization: str = None,
    ):
        # Specifies whether to enable nested virtualization. Valid values:
        # - disabled: Disables nested virtualization.
        # - enabled: Enables nested virtualization.
        self.nested_virtualization = nested_virtualization

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nested_virtualization is not None:
            result['nested_virtualization'] = self.nested_virtualization

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nested_virtualization') is not None:
            self.nested_virtualization = m.get('nested_virtualization')

        return self

class NodepoolNodepoolInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # The name of the node pool.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group to which the node pool belongs.
        self.resource_group_id = resource_group_id
        # The type of the node pool. Valid values:
        # - ess: Node pool.
        # - edge: Edge node pool.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class NodepoolNodeConfig(DaraModel):
    def __init__(
        self,
        kubelet_configuration: main_models.KubeletConfig = None,
    ):
        # The Kubelet parameter settings.
        self.kubelet_configuration = kubelet_configuration

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = main_models.KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m.get('kubelet_configuration'))

        return self

class NodepoolNodeComponents(DaraModel):
    def __init__(
        self,
        config: main_models.NodepoolNodeComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        # The node component configuration.
        self.config = config
        # The name of the node component.
        self.name = name
        # The version of the node component.
        self.version = version

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.NodepoolNodeComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class NodepoolNodeComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
        envs: List[main_models.NodepoolNodeComponentsConfigEnvs] = None,
    ):
        # The custom node component configuration.
        self.custom_config = custom_config
        # The environment variables for the node component.
        self.envs = envs

    def validate(self):
        if self.envs:
            for v1 in self.envs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['custom_config'] = self.custom_config

        result['envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['envs'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_config') is not None:
            self.custom_config = m.get('custom_config')

        self.envs = []
        if m.get('envs') is not None:
            for k1 in m.get('envs'):
                temp_model = main_models.NodepoolNodeComponentsConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        return self

class NodepoolNodeComponentsConfigEnvs(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        self.name = name
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class NodepoolManagement(DaraModel):
    def __init__(
        self,
        auto_fault_diagnosis: bool = None,
        auto_repair: bool = None,
        auto_repair_policy: main_models.NodepoolManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.NodepoolManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.NodepoolManagementAutoVulFixPolicy = None,
        drift_enabled: bool = None,
        enable: bool = None,
        upgrade_config: main_models.NodepoolManagementUpgradeConfig = None,
    ):
        # Specifies whether to enable ECS fault detection for node self-healing.
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Specifies whether to enable auto-repair. This parameter takes effect only when enable is set to true. Valid values:
        # - true: enables auto-repair.
        # - false: disables auto-repair.
        self.auto_repair = auto_repair
        # The auto-repair policy for nodes.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to enable auto upgrade.
        self.auto_upgrade = auto_upgrade
        # The auto upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically repair Common Vulnerabilities and Exposures (CVE).
        self.auto_vul_fix = auto_vul_fix
        # The policy for automatic CVE repair.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the node drift capability. This feature is only supported by smart managed node pools and is enabled by default. Regular node pools do not support this feature.
        self.drift_enabled = drift_enabled
        # Specifies whether to enable the managed node pool. Valid values:
        # - true: Enables the managed node pool.
        # - false: Does not enable the managed node pool. Other related configurations take effect only when enable is set to true.
        self.enable = enable
        # The auto upgrade configuration. This configuration takes effect only when enable is set to true.
        self.upgrade_config = upgrade_config

    def validate(self):
        if self.auto_repair_policy:
            self.auto_repair_policy.validate()
        if self.auto_upgrade_policy:
            self.auto_upgrade_policy.validate()
        if self.auto_vul_fix_policy:
            self.auto_vul_fix_policy.validate()
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_fault_diagnosis is not None:
            result['auto_fault_diagnosis'] = self.auto_fault_diagnosis

        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair

        if self.auto_repair_policy is not None:
            result['auto_repair_policy'] = self.auto_repair_policy.to_map()

        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade

        if self.auto_upgrade_policy is not None:
            result['auto_upgrade_policy'] = self.auto_upgrade_policy.to_map()

        if self.auto_vul_fix is not None:
            result['auto_vul_fix'] = self.auto_vul_fix

        if self.auto_vul_fix_policy is not None:
            result['auto_vul_fix_policy'] = self.auto_vul_fix_policy.to_map()

        if self.drift_enabled is not None:
            result['drift_enabled'] = self.drift_enabled

        if self.enable is not None:
            result['enable'] = self.enable

        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_fault_diagnosis') is not None:
            self.auto_fault_diagnosis = m.get('auto_fault_diagnosis')

        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')

        if m.get('auto_repair_policy') is not None:
            temp_model = main_models.NodepoolManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m.get('auto_repair_policy'))

        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('auto_upgrade_policy') is not None:
            temp_model = main_models.NodepoolManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m.get('auto_upgrade_policy'))

        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')

        if m.get('auto_vul_fix_policy') is not None:
            temp_model = main_models.NodepoolManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m.get('auto_vul_fix_policy'))

        if m.get('drift_enabled') is not None:
            self.drift_enabled = m.get('drift_enabled')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('upgrade_config') is not None:
            temp_model = main_models.NodepoolManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m.get('upgrade_config'))

        return self

class NodepoolManagementUpgradeConfig(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # Specifies whether to enable auto upgrade. Valid values:
        # - true: Enables auto upgrade.
        # - false: Disables auto upgrade.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of surge nodes.
        self.surge = surge
        # The percentage of surge nodes. This parameter and surge are mutually exclusive.
        self.surge_percentage = surge_percentage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade

        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable

        if self.surge is not None:
            result['surge'] = self.surge

        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('max_unavailable') is not None:
            self.max_unavailable = m.get('max_unavailable')

        if m.get('surge') is not None:
            self.surge = m.get('surge')

        if m.get('surge_percentage') is not None:
            self.surge_percentage = m.get('surge_percentage')

        return self

class NodepoolManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # Specifies whether to allow node restarts.
        self.restart_node = restart_node
        # The vulnerability levels that are allowed for automatic repair, separated by commas.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        if self.vul_level is not None:
            result['vul_level'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')

        if m.get('vul_level') is not None:
            self.vul_level = m.get('vul_level')

        return self

class NodepoolManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # Specifies whether to allow automatic kubelet upgrades.
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')

        return self

class NodepoolManagementAutoRepairPolicy(DaraModel):
    def __init__(
        self,
        max_parallel_repairing_nodes: str = None,
        max_unhealthy_nodes_threshold: str = None,
        restart_node: bool = None,
    ):
        # The maximum number of parallel repairs. When a large number of abnormal nodes exist in the node pool, this parameter specifies the maximum number or percentage of nodes that can be repaired at the same time. You can specify a number (such as 5, valid values: 1 to 100000) or a percentage (such as 10%, valid values: 1% to 100%). Default value: 1.
        self.max_parallel_repairing_nodes = max_parallel_repairing_nodes
        # The circuit breaker threshold for self-healing. When the number or percentage of faulty nodes exceeds this threshold, self-healing enters the circuit breaker state and stops initiating new self-healing actions. You can specify a number (such as 10, valid values: 1 to 100000) or a percentage (such as 20%, valid values: 1% to 100%). Default value: 100%.
        self.max_unhealthy_nodes_threshold = max_unhealthy_nodes_threshold
        # Specifies whether to allow node restarts.
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_parallel_repairing_nodes is not None:
            result['max_parallel_repairing_nodes'] = self.max_parallel_repairing_nodes

        if self.max_unhealthy_nodes_threshold is not None:
            result['max_unhealthy_nodes_threshold'] = self.max_unhealthy_nodes_threshold

        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_parallel_repairing_nodes') is not None:
            self.max_parallel_repairing_nodes = m.get('max_parallel_repairing_nodes')

        if m.get('max_unhealthy_nodes_threshold') is not None:
            self.max_unhealthy_nodes_threshold = m.get('max_unhealthy_nodes_threshold')

        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')

        return self

class NodepoolKubernetesConfig(DaraModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[main_models.Tag] = None,
        node_name_mode: str = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[main_models.Taint] = None,
        user_data: str = None,
    ):
        # Specifies whether to install CloudMonitor on ECS nodes. After installation, you can view the monitoring information of the created ECS instances in the CloudMonitor console. Enabling this feature is recommended. Valid values:
        # - true: installs CloudMonitor on ECS nodes.
        # - false: does not install CloudMonitor on ECS nodes.
        # Default value: false.
        self.cms_enabled = cms_enabled
        # The CPU management policy for nodes. The following two policies are supported when the cluster version is 1.12.6 or later:
        # - static: allows you to enhance CPU affinity and exclusivity for pods with specific resource characteristics on the node.
        # - none: uses the default CPU affinity scheme.
        # Default value: none.
        self.cpu_policy = cpu_policy
        # The node labels, which are added to the nodes in the Kubernetes cluster.
        self.labels = labels
        # The node name consists of three parts: prefix + node IP address + suffix.
        # - The prefix and suffix can each consist of one or more parts separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or a digit.
        # - The node IP address is the complete private IP address of the node.
        # The parameter value contains four parts separated by commas. For example, if the parameter is set to the "customized,aliyun,ip,com" string (where "customized" and "ip" are fixed strings, "aliyun" is the prefix, and "com" is the suffix), the node name is aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # The container runtime. Valid values:
        # - containerd: recommended. Supported by all cluster versions.
        # - Sandboxed-Container.runv: sandboxed container. Provides higher isolation. Supported by clusters of Kubernetes 1.24 and earlier.
        # - docker: supported by clusters of Kubernetes 1.22 and earlier.
        # Default value: containerd.
        # 
        # This parameter is required.
        self.runtime = runtime
        # The container runtime version.
        # 
        # This parameter is required.
        self.runtime_version = runtime_version
        # The taint configuration.
        self.taints = taints
        # The custom data of the node.
        self.user_data = user_data

    def validate(self):
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.taints:
            for v1 in self.taints:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled

        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy

        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version

        result['taints'] = []
        if self.taints is not None:
            for k1 in self.taints:
                result['taints'].append(k1.to_map() if k1 else None)

        if self.user_data is not None:
            result['user_data'] = self.user_data

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')

        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')

        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.Tag()
                self.labels.append(temp_model.from_map(k1))

        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')

        self.taints = []
        if m.get('taints') is not None:
            for k1 in m.get('taints'):
                temp_model = main_models.Taint()
                self.taints.append(temp_model.from_map(k1))

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        return self

class NodepoolInterconnectConfig(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        # **[Deprecated]** The network bandwidth of the edge-optimized node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # **[Deprecated]** The instance ID of the Cloud Connect Network (CCN) attached to the edge-optimized node pool.
        self.ccn_id = ccn_id
        # **[Deprecated]** The region of the CCN instance associated with the edge-optimized node pool.
        self.ccn_region_id = ccn_region_id
        # **[Deprecated]** The instance ID of the Cloud Enterprise Network (CEN) attached to the edge-optimized node pool.
        self.cen_id = cen_id
        # **[Deprecated]** The subscription duration of the edge-optimized node pool. Unit: months.
        self.improved_period = improved_period

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth

        if self.ccn_id is not None:
            result['ccn_id'] = self.ccn_id

        if self.ccn_region_id is not None:
            result['ccn_region_id'] = self.ccn_region_id

        if self.cen_id is not None:
            result['cen_id'] = self.cen_id

        if self.improved_period is not None:
            result['improved_period'] = self.improved_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')

        if m.get('ccn_id') is not None:
            self.ccn_id = m.get('ccn_id')

        if m.get('ccn_region_id') is not None:
            self.ccn_region_id = m.get('ccn_region_id')

        if m.get('cen_id') is not None:
            self.cen_id = m.get('cen_id')

        if m.get('improved_period') is not None:
            self.improved_period = m.get('improved_period')

        return self

class NodepoolAutoScaling(DaraModel):
    def __init__(
        self,
        eip_bandwidth: int = None,
        eip_internet_charge_type: str = None,
        enable: bool = None,
        is_bond_eip: bool = None,
        max_instances: int = None,
        min_instances: int = None,
        type: str = None,
    ):
        # **[Deprecated]** The peak bandwidth of the elastic IP address (EIP). Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # **[Deprecated]** The billing method of the EIP. Valid values:
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-data-transfer.
        # Default value: PayByBandwidth.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # - true: enables auto scaling for the node pool.
        # - false: disables auto scaling. If this parameter is set to false, other configuration parameters in auto_scaling do not take effect.
        # Default value: false.
        # 
        # This parameter is required.
        self.enable = enable
        # **[Deprecated]** Specifies whether to associate an EIP. Valid values:
        # - true: associates an EIP.
        # - false: does not associate an EIP.
        # Default value: false.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances in the auto-scaling group.
        # 
        # This parameter is required.
        self.max_instances = max_instances
        # The minimum number of instances in the auto-scaling group.
        # 
        # This parameter is required.
        self.min_instances = min_instances
        # The auto-scaling type, which is classified by the instance type used for auto scaling. Valid values:
        # - cpu: regular instance.
        # - gpu: GPU-accelerated instance.
        # - gpushare: shared GPU instance.
        # - spot: spot instance.
        # Default value: cpu.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth

        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type

        if self.enable is not None:
            result['enable'] = self.enable

        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip

        if self.max_instances is not None:
            result['max_instances'] = self.max_instances

        if self.min_instances is not None:
            result['min_instances'] = self.min_instances

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eip_bandwidth') is not None:
            self.eip_bandwidth = m.get('eip_bandwidth')

        if m.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = m.get('eip_internet_charge_type')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('is_bond_eip') is not None:
            self.is_bond_eip = m.get('is_bond_eip')

        if m.get('max_instances') is not None:
            self.max_instances = m.get('max_instances')

        if m.get('min_instances') is not None:
            self.min_instances = m.get('min_instances')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

