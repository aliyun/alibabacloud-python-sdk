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
        # The auto scaling configuration for the node pool.
        self.auto_scaling = auto_scaling
        # **This field is deprecated. Use desired_size instead.**
        # 
        # The number of nodes in the node pool.
        self.count = count
        # **This field is deprecated.**
        # 
        # The edge node pool configuration.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter is valid only for node pools whose `type` is `edge`. Valid values:
        # 
        # - `basic`: Basic.
        # - `private`: Dedicated. Supported in version 1.22 and later.
        self.interconnect_mode = interconnect_mode
        # The cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # The managed node pool configuration.
        self.management = management
        # The maximum number of nodes allowed in the edge node pool. This parameter must be greater than or equal to 0. A value of 0 indicates no additional limit (limited only by the maximum number of nodes the cluster can accommodate, with no additional limit on the node pool itself). This value is typically greater than 0 for edge node pools. For ess-type node pools and default edge-type node pools, this value is 0.
        self.max_nodes = max_nodes
        # The node component list.
        self.node_components = node_components
        # The node configuration.
        self.node_config = node_config
        # The node pool configuration.
        self.nodepool_info = nodepool_info
        # The scaling group configuration for the node pool.
        self.scaling_group = scaling_group
        # The confidential computing node pool configuration.
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
        # Specifies whether to enable auto-renewal for the node pool. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enables auto-renewal.
        # - `false`: Disables auto-renewal.
        # 
        # Default value: `true`.
        self.auto_renew = auto_renew
        # The auto-renewal epoch for the node pool. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # When `PeriodUnit=Month`, valid values: {1, 2, 3, 6, 12}.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # When `multi_az_policy` is set to `COST_OPTIMIZED`, specifies whether to allow automatic creation of pay-as-you-go instances to meet the required number of ECS instances when spot instances cannot be created due to price or inventory reasons. Valid values:
        # 
        # - `true`: Allows automatic creation of pay-as-you-go instances to meet the required number of ECS instances.
        # - `false`: Does not allow automatic creation of pay-as-you-go instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The CPU configuration options.
        self.cpu_options = cpu_options
        # The data cloud disk configuration for nodes in the node pool.
        self.data_disks = data_disks
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The desired number of nodes in the node pool.
        self.desired_size = desired_size
        # The block device initialization configuration.
        self.disk_init = disk_init
        # The custom image ID. The system-provided image is used by default.
        self.image_id = image_id
        # The operating system image type. Specify either this parameter or platform. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # - `AliyunLinux3`: Alinux3 image.
        # - `AliyunLinux3Arm64`: Alinux3 image for ARM.
        # - `AliyunLinuxUEFI`: Alinux2 UEFI image.
        # - `CentOS`: CentOS image.
        # - `Windows`: Windows image.
        # - `WindowsCore`: WindowsCore image.
        # - `ContainerOS`: container-optimized image.
        self.image_type = image_type
        # The billing method for nodes in the node pool. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The metadata access configuration for ECS instances.
        # This parameter is currently available only to accounts on the whitelist. Submit a ticket to request access.
        self.instance_metadata_options = instance_metadata_options
        # The instance types.
        # 
        # This parameter is required.
        self.instance_types = instance_types
        # The billing method for public IP addresses. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth for node public IP addresses. Unit: Mbit/s. Valid values: [1,100].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The key pair name. Specify either this parameter or `login_password`.
        # 
        # > For managed node pools, only `key_pair` is supported.
        self.key_pair = key_pair
        # Specifies whether scaled-out ECS instances log on as a non-root user.
        self.login_as_non_root = login_as_non_root
        # The SSH logon password. Specify either this parameter or `key_pair`. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The multi-zone scaling policy for ECS instances in the scaling group. Valid values:
        # 
        # - `PRIORITY`: Scales based on the vSwitches (VSwitchIds.N) that you define. When ECS instances cannot be created in the zone of a higher-priority vSwitch, the system automatically uses the next-priority vSwitch to create ECS instances.
        # 
        # - `COST_OPTIMIZED`: Attempts to create instances in order of ascending vCPU unit price. When the scaling configuration sets the spot billing method for multiple instance types, spot instances are created first. You can use the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when spot instances cannot be created due to insufficient inventory.
        # 
        #   >`COST_OPTIMIZED` takes effect only when the scaling configuration sets multiple instance types or uses spot instances.
        # 
        # - `BALANCE`: Distributes ECS instances evenly across the active zones specified in the scaling group. If the zones become unbalanced due to insufficient inventory, you can call the RebalanceInstances operation to rebalance resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances required by the scaling group. Valid values: [0,1000]. When the number of pay-as-you-go instances is less than this value, pay-as-you-go instances are created first.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the instances that exceed the minimum number of pay-as-you-go instances (`on_demand_base_capacity`). Valid values: [0,100].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration for nodes in the node pool. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`. When `period_unit` is set to Month, valid values for `period`: {1, 2, 3, 6, 12}.
        # 
        # Default value: 1.
        self.period = period
        # The billing period unit for nodes in the node pool. This parameter must be specified when `instance_charge_type` is set to `PrePaid`.
        # 
        # `Month`: Currently, only monthly billing is supported.
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
        # The private node pool configuration.
        self.private_pool_options = private_pool_options
        # The Worker RAM role name.
        # >Notice: Only ACK managed clusters of version 1.22 or later support configuring this parameter when creating a node pool.</notice>
        self.ram_role_name = ram_role_name
        # The list of RDS instances.
        self.rds_instances = rds_instances
        # The resource pool and resource pool policy used when creating instances. Note the following when you set this parameter:
        # This parameter takes effect only when creating pay-as-you-go instances.
        # This parameter cannot be set together with private_pool_options.match_criteria or private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # The scaling group mode. Valid values:
        # 
        # - `release`: standard mode. Scales in or out by creating or releasing ECS instances based on resource usage.
        # - `recycle`: swift mode. Scales in or out by creating, stopping, or starting ECS instances, which improves the speed of subsequent scaling operations. (Stopped instances are not charged for compute resources, but storage fees still apply, except for instances with local disks.)
        # 
        # Default value: `release`.
        self.scaling_policy = scaling_policy
        # The security group ID for the node pool. Specify either this parameter or `security_group_ids`. We recommend that you use `security_group_ids`.
        self.security_group_id = security_group_id
        # The list of security group IDs. Specify either this parameter or `security_group_id`. We recommend that you use `security_group_ids`. When both `security_group_id` and `security_group_ids` are specified, `security_group_ids` takes precedence.
        self.security_group_ids = security_group_ids
        # The number of available instance types. The scaling group creates spot instances across the lowest-cost instance types in a balanced manner. Valid values: [1,10].
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable spot instance supplementation. When enabled, the scaling group attempts to create new instances to replace spot instances that are about to be reclaimed. Valid values:
        # 
        # - `true`: Enables spot instance supplementation.
        # - `false`: Disables spot instance supplementation.
        self.spot_instance_remedy = spot_instance_remedy
        # The market price range configuration for a single spot instance type.
        self.spot_price_limit = spot_price_limit
        # The type of spot instance. Valid values:
        # - NoSpot: non-spot instance.
        # - SpotWithPriceLimit: spot instance with a price limit.
        # - SpotAsPriceGo: system automatically bids at the current market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable burst (performance burst) for the node system cloud disk. Valid values:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disk](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The multiple cloud disk types for the system cloud disk. When a higher-priority cloud disk type is unavailable, the system automatically attempts the next-priority cloud disk type to create the system cloud disk. Valid values:
        # 
        # - cloud: basic cloud disk.
        # - cloud_efficiency: ultra cloud disk.
        # - cloud_ssd: standard SSD.
        # - cloud_essd: ESSD.
        self.system_disk_categories = system_disk_categories
        # The type of the system cloud disk for nodes. Valid values:
        # 
        # - `cloud_efficiency`: ultra cloud disk.
        # - `cloud_ssd`: standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL cloud disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # The encryption algorithm for the node system cloud disk. Valid values: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system cloud disk. Valid values: true: encrypted. false: not encrypted.
        self.system_disk_encrypted = system_disk_encrypted
        # The KMS key ID used by the node system cloud disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system cloud disk for nodes. Applies only to ESSD cloud disks.
        # 
        # - PL0: moderate maximum concurrent I/O performance with relatively stable read/write latency.
        # - PL1: moderate maximum concurrent I/O performance with relatively stable read/write latency.
        # - PL2: high maximum concurrent I/O performance with stable read/write latency.
        # - PL3: ultra-high maximum concurrent I/O performance with extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS for the node system cloud disk. Valid values: 0 to min{50,000, 1000 × capacity - baseline performance}. Baseline performance = min{1,800 + 50 × capacity, 50000}.
        # 
        # This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disk](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system cloud disk for nodes. Unit: GiB.
        # 
        # Valid values: [40,500].
        self.system_disk_size = system_disk_size
        # The tags that are added only to ECS instances.
        # 
        # Tag keys cannot be duplicated and can be up to 128 characters in length. Tag keys and tag values cannot start with "aliyun" or "acs:", or contain "https://" or "http://".
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
        # The spot instance type.
        self.instance_type = instance_type
        # The maximum price per instance.
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
        # The list of private pool IDs, which are elasticity assurance IDs or capacity reservation IDs. Only Target mode private pool IDs can be passed in. Valid values of N: 1 to 20.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy used when creating instances. Resource pools include private pools generated after an elasticity assurance or capacity reservation takes effect, and public pools, for instance startup. Valid values:
        # PrivatePoolFirst: private pool first. When this policy is selected and resource_pool_options.private_pool_ids is specified, the specified private pools are used first. If no private pool is specified or the specified private pool capacity is insufficient, open-type private pools are automatically matched. If no matching private pool is available, public pool resources are used.
        # PrivatePoolOnly: private pool only. When this policy is selected, resource_pool_options.private_pool_ids must be specified. If the specified private pool capacity is insufficient, the instance fails to start.
        # None: no resource pool policy.
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
        # The private node pool ID.
        self.id = id
        # The private node pool type. The private pool capacity option for instance startup. After an elasticity assurance or capacity reservation takes effect, a private pool is generated for instance startup. Valid values:
        # 
        # - `Open`: open mode. Automatically matches open-type private pool capacity. If no matching private pool capacity is available, public pool resources are used for instance startup.
        # 
        # - `Target`: targeted mode. Uses the specified private pool capacity for instance startup. If the specified private pool capacity is unavailable, the instance fails to start.
        # 
        # - `None`: none mode. The instance does not use private pool capacity for startup.
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
        # disabled: Disable nested virtualization.
        # enabled: Enable nested virtualization.
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
        # The node pool name.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group to which the node pool belongs.
        self.resource_group_id = resource_group_id
        # The node pool type. Valid values:
        # 
        # - `ess`: node pool.
        # - `edge`: edge node pool.
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
        # The node component name.
        self.name = name
        # The node component version.
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
    ):
        # The custom node component configuration.
        self.custom_config = custom_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_config is not None:
            result['custom_config'] = self.custom_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_config') is not None:
            self.custom_config = m.get('custom_config')

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
        # Specifies whether to enable node self-healing ECS fault detection.
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Specifies whether to enable automatic repair. This parameter takes effect only when `enable=true`.
        # 
        # - `true`: Enable automatic repair.
        # - `false`: Disable automatic repair.
        self.auto_repair = auto_repair
        # The auto repair node policy.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to enable auto upgrade.
        self.auto_upgrade = auto_upgrade
        # The auto upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically fix CVEs.
        self.auto_vul_fix = auto_vul_fix
        # The auto CVE fix policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable node rotation. Only intelligent managed node pools support this feature, and it is enabled by default. Common node pools do not support this feature.
        self.drift_enabled = drift_enabled
        # Specifies whether to enable the managed node pool. Valid values:
        # 
        # - `true`: Enable the managed node pool.
        # - `false`: Do not enable the managed node pool. Other related configurations take effect only when `enable=true`.
        self.enable = enable
        # The auto upgrade configuration. This parameter takes effect only when `enable=true`.
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
        # 
        # - `true`: Enable auto upgrade.
        # - `false`: Disable auto upgrade.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes. Valid values: [1,1000\\].
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of extra nodes.
        self.surge = surge
        # The percentage of extra nodes. This parameter is mutually exclusive with `surge`.
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
        # Specifies whether to allow node restart.
        self.restart_node = restart_node
        # The vulnerability levels that are allowed for automatic fix, separated by commas.
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
        # Specifies whether to allow automatic kubelet upgrade.
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
        self.max_parallel_repairing_nodes = max_parallel_repairing_nodes
        self.max_unhealthy_nodes_threshold = max_unhealthy_nodes_threshold
        # Specifies whether to allow node restart.
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
        # Specifies whether to install the CloudMonitor agent on ECS nodes. After installation, you can view monitoring information of the created ECS instances in the CloudMonitor console. We recommend that you enable this feature. Valid values:
        # 
        # - `true`: Installs the CloudMonitor agent on ECS nodes.
        # - `false`: Does not install the CloudMonitor agent on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy for nodes. The following two policies are supported for clusters of version 1.12.6 or later:
        # 
        # - `static`: Allows pods with certain resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # - `none`: Enables the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The node labels. Adds labels to the nodes in the Kubernetes cluster.
        self.labels = labels
        # The node name consists of three parts: prefix + node IP + suffix:
        # 
        # - Both the prefix and suffix can consist of one or more parts separated by ".". Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or digit.
        # - The node IP is the full private IP address of the node.
        # 
        # The parameter contains four parts separated by commas. For example, if you pass in the string "customized,aliyun,ip,com" (where "customized" and "ip" are fixed strings, "aliyun" is the prefix, and "com" is the suffix), the node name is: aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # The container runtime. Valid values:
        # - `containerd`: Recommended. Supports all cluster versions.
        # - `Sandboxed-Container.runv`: Sandboxed container. Provides higher isolation. Supports clusters of version 1.24 or earlier.
        # - `docker`: Supports clusters of version 1.22 or earlier.
        # 
        # Default value: `containerd`
        # 
        # This parameter is required.
        self.runtime = runtime
        # The container runtime version.
        # 
        # This parameter is required.
        self.runtime_version = runtime_version
        # The taint configuration.
        self.taints = taints
        # The node custom data.
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
        # **This field is deprecated.**
        # 
        # The network bandwidth of the enhanced edge node pool. Unit: Mbps.
        self.bandwidth = bandwidth
        # **This field is deprecated.**
        # 
        # The instance ID of the Cloud Connect Network (CCN) attached to the enhanced edge node pool.
        self.ccn_id = ccn_id
        # **This field is deprecated.**
        # 
        # The region of the Cloud Connect Network (CCN) instance bound to the enhanced edge node pool.
        self.ccn_region_id = ccn_region_id
        # **This field is deprecated.**
        # 
        # The instance ID of the Cloud Enterprise Network (CEN) attached to the enhanced edge node pool.
        self.cen_id = cen_id
        # **This field is deprecated.**
        # 
        # The purchase duration of the enhanced edge node pool. Unit: months.
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
        # [This field is deprecated]
        # 
        # The peak bandwidth of the EIP. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # [This field is deprecated]
        # 
        # The billing method for the EIP. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-data-transfer.
        # 
        # Default value: PayByBandwidth.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling.
        # 
        # - `true`: Enables auto scaling for the node pool.
        # - `false`: Disables auto scaling. When set to false, other configuration parameters in `auto_scaling` do not take effect.
        # 
        # Default value: `false`.
        # 
        # This parameter is required.
        self.enable = enable
        # [This field is deprecated]
        # 
        # Specifies whether to associate an EIP. Valid values:
        # 
        # - `true`: Associates an EIP.
        # - `false`: Does not associate an EIP.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances in the auto scaling group.
        # 
        # This parameter is required.
        self.max_instances = max_instances
        # The minimum number of instances in the auto scaling group.
        # 
        # This parameter is required.
        self.min_instances = min_instances
        # The auto scaling type, classified by instance type. Valid values:
        # 
        # - `cpu`: regular instance type.
        # - `gpu`: GPU instance type.
        # - `gpushare`: GPU shared type.
        # - `spot`: spot instance type.
        # 
        # Default value: `cpu`.
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

