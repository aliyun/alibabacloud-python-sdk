# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class CreateClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        auto_mode: main_models.CreateClusterNodePoolRequestAutoMode = None,
        auto_scaling: main_models.CreateClusterNodePoolRequestAutoScaling = None,
        count: int = None,
        eflo_node_group: main_models.CreateClusterNodePoolRequestEfloNodeGroup = None,
        host_network: bool = None,
        interconnect_config: main_models.CreateClusterNodePoolRequestInterconnectConfig = None,
        interconnect_mode: str = None,
        intranet: bool = None,
        kubernetes_config: main_models.CreateClusterNodePoolRequestKubernetesConfig = None,
        management: main_models.CreateClusterNodePoolRequestManagement = None,
        max_nodes: int = None,
        node_components: List[main_models.CreateClusterNodePoolRequestNodeComponents] = None,
        node_config: main_models.CreateClusterNodePoolRequestNodeConfig = None,
        nodepool_info: main_models.CreateClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: main_models.CreateClusterNodePoolRequestScalingGroup = None,
        tee_config: main_models.CreateClusterNodePoolRequestTeeConfig = None,
    ):
        # Node pool intelligent managed configuration.
        self.auto_mode = auto_mode
        # Auto scaling configuration.
        self.auto_scaling = auto_scaling
        # [Deprecated] Use desired_size instead.
        # 
        # Number of nodes in the node pool.
        self.count = count
        # Lingjun node pool configuration.
        self.eflo_node_group = eflo_node_group
        # Whether the Pod network mode uses host network mode.
        # - `true`: host network. Pods directly use the host network stack, sharing the IP address and ports with the host.
        # - `false`: container network. Pods have an independent network stack and do not occupy host network ports.
        self.host_network = host_network
        # [Deprecated]
        # 
        # Edge node pool configuration.
        self.interconnect_config = interconnect_config
        # Network type of the edge node pool. This parameter takes effect only for node pools of `edge` type. Valid values:
        # 
        # - `basic`: public network. Nodes in the node pool communicate with cloud nodes over the public network. Applications in the node pool cannot directly access the cloud VPC internal network.
        # - `private`: private network. Nodes in the node pool connect cloud and on-premises networks through Express Connect, VPN, or CEN, providing higher cloud-edge communication quality and more effective security.
        self.interconnect_mode = interconnect_mode
        # Whether nodes in the edge node pool have Layer 3 network connectivity.
        # - `true`: connected. All nodes in this node pool have Layer 3 network connectivity.
        # - `false`: not connected. All hosts in this node pool do not have Layer 3 network connectivity.
        self.intranet = intranet
        # Cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # Node pool managed feature configuration.
        self.management = management
        # [Deprecated]
        # 
        # Maximum number of nodes allowed in the edge node pool.
        self.max_nodes = max_nodes
        # Node component list.
        self.node_components = node_components
        # Node configuration.
        self.node_config = node_config
        # Node pool configuration.
        self.nodepool_info = nodepool_info
        # Node pool scaling group configuration.
        self.scaling_group = scaling_group
        # Confidential computing cluster configuration.
        self.tee_config = tee_config

    def validate(self):
        if self.auto_mode:
            self.auto_mode.validate()
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.eflo_node_group:
            self.eflo_node_group.validate()
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
        if self.auto_mode is not None:
            result['auto_mode'] = self.auto_mode.to_map()

        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()

        if self.count is not None:
            result['count'] = self.count

        if self.eflo_node_group is not None:
            result['eflo_node_group'] = self.eflo_node_group.to_map()

        if self.host_network is not None:
            result['host_network'] = self.host_network

        if self.interconnect_config is not None:
            result['interconnect_config'] = self.interconnect_config.to_map()

        if self.interconnect_mode is not None:
            result['interconnect_mode'] = self.interconnect_mode

        if self.intranet is not None:
            result['intranet'] = self.intranet

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
        if m.get('auto_mode') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestAutoMode()
            self.auto_mode = temp_model.from_map(m.get('auto_mode'))

        if m.get('auto_scaling') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m.get('auto_scaling'))

        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('eflo_node_group') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestEfloNodeGroup()
            self.eflo_node_group = temp_model.from_map(m.get('eflo_node_group'))

        if m.get('host_network') is not None:
            self.host_network = m.get('host_network')

        if m.get('interconnect_config') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m.get('interconnect_config'))

        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')

        if m.get('intranet') is not None:
            self.intranet = m.get('intranet')

        if m.get('kubernetes_config') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('kubernetes_config'))

        if m.get('management') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m.get('management'))

        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')

        self.node_components = []
        if m.get('node_components') is not None:
            for k1 in m.get('node_components'):
                temp_model = main_models.CreateClusterNodePoolRequestNodeComponents()
                self.node_components.append(temp_model.from_map(k1))

        if m.get('node_config') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestNodeConfig()
            self.node_config = temp_model.from_map(m.get('node_config'))

        if m.get('nodepool_info') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('nodepool_info'))

        if m.get('scaling_group') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('scaling_group'))

        if m.get('tee_config') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m.get('tee_config'))

        return self

class CreateClusterNodePoolRequestTeeConfig(DaraModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        # Whether to enable confidential computing for the cluster.
        # 
        # - true: enable confidential computing.
        # 
        # - false: disable confidential computing.
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

class CreateClusterNodePoolRequestScalingGroup(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cis_enabled: bool = None,
        compensate_with_on_demand: bool = None,
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
        private_pool_options: main_models.CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions = None,
        ram_role_name: str = None,
        rds_instances: List[str] = None,
        resource_pool_options: main_models.CreateClusterNodePoolRequestScalingGroupResourcePoolOptions = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_hardening_os: bool = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[main_models.CreateClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
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
        system_disk_snapshot_policy_id: str = None,
        tags: List[main_models.CreateClusterNodePoolRequestScalingGroupTags] = None,
        vswitch_ids: List[str] = None,
    ):
        # Whether to enable auto-renewal for nodes in the node pool. Takes effect only when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: enable auto-renewal.
        # - `false`: disable auto-renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # Duration of each auto-renewal. Valid values:
        # - When PeriodUnit=Week: 1, 2, 3.
        # - When PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # [Deprecated] Use the security_hardening_os parameter instead.
        self.cis_enabled = cis_enabled
        # When `multi_az_policy` is set to `COST_OPTIMIZED`, whether to allow automatic creation of pay-as-you-go instances to meet the required number of ECS instances when preemptible instances cannot be created due to price or inventory constraints. Valid values:
        # 
        # - `true`: allow automatic creation of pay-as-you-go instances.
        # - `false`: do not allow automatic creation of pay-as-you-go instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # Data disk configuration for nodes in the node pool.
        self.data_disks = data_disks
        # Deployment set ID. You can use a deployment set to distribute ECS instances created by the node pool across different physical servers to ensure high availability and disaster recovery capabilities. When creating ECS instances in a deployment set, instances are distributed across the specified region based on the pre-configured deployment policy.
        # 
        # 
        # >Notice: After a deployment set is selected, the maximum number of nodes in the node pool is limited. The default upper limit for nodes in a deployment set is 20 × number of zones (the number of zones is determined by vSwitches). Choose carefully and ensure sufficient quota in the deployment set to avoid node creation failures.
        self.deploymentset_id = deploymentset_id
        # Desired number of nodes in the node pool.
        # 
        # The total number of nodes that the node pool should maintain. We recommend configuring at least 2 nodes to ensure proper running of cluster components. You can scale in or out the node pool by adjusting the desired node count.
        # 
        # If no nodes need to be created, set this to 0 and manually adjust the node count later.
        self.desired_size = desired_size
        # Block device initialization configuration.
        self.disk_init = disk_init
        # Custom image ID. The system-provided image is used by default.
        self.image_id = image_id
        # OS image type. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # - `AliyunLinuxSecurity`: Alinux2 image UEFI version.
        # - `AliyunLinux3`: Alinux3 image.
        # - `AliyunLinux3Arm64`: Alinux3 image ARM version.
        # - `AliyunLinux3Security`: Alinux3 image UEFI version.
        # - `CentOS`: CentOS image.
        # - `Windows`: Windows image.
        # - `WindowsCore`: WindowsCore image.
        # - `ContainerOS`: container-optimized image.
        # - `AliyunLinux3ContainerOptimized`: Alinux3 container-optimized image.
        self.image_type = image_type
        # Billing method for nodes in the node pool. Valid values:
        #  
        # - `PrePaid`: subscription instance.
        # 
        # - `PostPaid`: pay-as-you-go instance.
        # 
        # Default value: `PostPaid`.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # ECS instance metadata access configuration.
        self.instance_metadata_options = instance_metadata_options
        # Instance attribute configuration.
        self.instance_patterns = instance_patterns
        # List of node instance types for the node pool. When the node pool scales out, instance types that meet the requirements are selected from the specified list to create instances.
        # 
        # Supported number of instance types: [1,10]
        # 
        # 
        # > To ensure high availability, we recommend that you select multiple instance types.
        # 
        # This parameter is required.
        self.instance_types = instance_types
        # Public IP billing method. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-traffic.
        self.internet_charge_type = internet_charge_type
        # Maximum outbound public bandwidth for nodes. Unit: Mbps (Megabits per second). Valid values: [1,100\\].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Key pair name for passwordless login. Mutually exclusive with `login_password`.
        # 
        # > If the node pool uses the ContainerOS operating system, only `key_pair` is supported.
        self.key_pair = key_pair
        # Whether the created ECS instances use a non-root user for login.
        #  
        # - true: log on as a non-root user (ecs-user).
        # 
        # - false: log on as the root user.
        self.login_as_non_root = login_as_non_root
        # SSH login password. Mutually exclusive with `key_pair`. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # Multi-zone scaling group ECS instance scaling policy. Valid values:
        # 
        # - `PRIORITY`: scales based on the vSwitches (VSwitchIds.N) you defined. When ECS instances cannot be created in the zone of a higher-priority vSwitch, the next-priority vSwitch is automatically used.
        # 
        # - `COST_OPTIMIZED`: attempts to create instances from lowest to highest vCPU unit price. When multiple instance types with preemptible billing are configured, preemptible instances are created first. You can use the `CompensateWithOnDemand` parameter to specify whether to automatically attempt creating pay-as-you-go instances when preemptible instances cannot be created due to insufficient inventory.
        # 
        #   > `COST_OPTIMIZED` takes effect only when multiple instance types or preemptible instances are configured.
        # 
        # - `BALANCE`: evenly distributes ECS instances across the multiple zones specified in the scaling group. If zones become unbalanced due to insufficient inventory, you can use the API [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html) to rebalance resources.
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # Minimum number of pay-as-you-go instances required by the scaling group. Valid values: [0,1000\\]. When the number of pay-as-you-go instances is less than this value, pay-as-you-go instances are created first.
        self.on_demand_base_capacity = on_demand_base_capacity
        # Percentage of pay-as-you-go instances among the excess instances after the scaling group meets the minimum pay-as-you-go instance requirement (`on_demand_base_capacity`). Valid values: [0,100\\].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # Subscription duration for nodes in the node pool. Takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - When `period_unit=Week`, valid values of `period`: {1, 2, 3, 4}.
        # - When `period_unit=Month`, valid values of `period`: {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 60}.
        self.period = period
        # Billing period unit for nodes in the node pool. Takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - `Month`: billed on a monthly basis.
        # - `Week`: billed on a weekly basis.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # [Deprecated] Use the `image_type` parameter instead.
        # 
        # OS distribution. Valid values:
        # - `CentOS`
        # - `AliyunLinux`
        # - `Windows`
        # - `WindowsCore`
        # 
        # Default value: `AliyunLinux`.
        self.platform = platform
        # Private pool configuration.
        self.private_pool_options = private_pool_options
        # Worker RAM role name.
        # 
        # * When left empty, the default Worker RAM role created by the cluster is used.
        # * When specified, the RAM role must be a **normal service role**, and its **trusted service** must be set to **Elastic Compute Service**. For more information, see [Create a normal service role](https://help.aliyun.com/document_detail/116800.html). When the specified RAM role is not the default Worker RAM role created by the cluster, the role name cannot start with `KubernetesMasterRole-` or `KubernetesWorkerRole-`.
        # 
        # >Notice: This parameter is supported only for ACK managed clusters of version 1.22 or later.
        self.ram_role_name = ram_role_name
        # RDS instance list.
        self.rds_instances = rds_instances
        # Resource pool and resource pool policy used when creating instances. Note the following when you set this parameter:
        # This parameter takes effect only when creating pay-as-you-go instances.
        # This parameter cannot be set together with private_pool_options.match_criteria or private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # Scaling group mode. Valid values:
        # 
        # - `release`: standard mode. Scales by creating and releasing ECS instances based on resource usage.
        # - `recycle`: rapid mode. Scales by creating, stopping, and starting ECS instances, improving the speed of subsequent scaling (compute resources are not charged when stopped, only storage fees are charged, except for local disk instance types).
        # 
        # Default value: `release`.
        self.scaling_policy = scaling_policy
        # Security group ID for the node pool. Mutually exclusive with `security_group_ids`. We recommend using `security_group_ids`.
        self.security_group_id = security_group_id
        # List of security group IDs. Mutually exclusive with `security_group_id`. We recommend using `security_group_ids`. When both `security_group_id` and `security_group_ids` are specified, `security_group_ids` takes priority.
        self.security_group_ids = security_group_ids
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: enable Alibaba Cloud OS security hardening.
        # - `false`: disable Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Whether to enable China classified protection of cybersecurity (China MLPS) hardening. China MLPS hardening can be enabled for nodes only when the system image is set to Alibaba Cloud Linux 2 or Alibaba Cloud Linux 3. Alibaba Cloud provides China MLPS 2.0 Level III baseline check standards and scanning programs for Alibaba Cloud Linux 2 and Alibaba Cloud Linux 3 images.
        self.soc_enabled = soc_enabled
        # Number of available instance types. The scaling group creates preemptible instances in a balanced manner among the lowest-cost instance types. Valid values: [1,10\\].
        self.spot_instance_pools = spot_instance_pools
        # Whether to enable supplementing preemptible instances. When enabled, the scaling group attempts to create new instances to replace preemptible instances that are about to be reclaimed. Valid values:
        # 
        # - `true`: enable supplementing preemptible instances.
        # - `false`: disable supplementing preemptible instances.
        self.spot_instance_remedy = spot_instance_remedy
        # Market price range configuration for a single preemptible instance type.
        self.spot_price_limit = spot_price_limit
        # Preemptible instance type. Valid values:
        # 
        # - `NoSpot`: non-preemptible instance.
        # 
        # - `SpotWithPriceLimit`: set a maximum price for preemptible instances.
        # 
        # - `SpotAsPriceGo`: the system automatically bids at the current market price.
        # 
        # For more information, see [Preemptible instances](https://help.aliyun.com/document_detail/165053.html).
        self.spot_strategy = spot_strategy
        # Whether to enable burst (performance bursting) for the node system disk. Valid values:
        # - true: enable.
        # - false: disable.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Multiple disk types for the system disk. When a higher-priority disk type is unavailable, the next-priority disk type is automatically used to create the system disk.
        self.system_disk_categories = system_disk_categories
        # Node system disk type. Valid values:
        # - `cloud_efficiency`: ultra disk.
        # - `cloud_ssd`: standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # Encryption algorithm used by the system disk. Valid values: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypt.
        # 
        # - false: do not encrypt.
        self.system_disk_encrypted = system_disk_encrypted
        # KMS key ID used by the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # Node system disk performance level. Only applicable to ESSD disks. The performance level is related to disk size. For more information, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # - PL0: moderate peak concurrent I/O performance with relatively stable read/write latency.
        # - PL1: moderate peak concurrent I/O performance with relatively stable read/write latency.
        # - PL2: high peak concurrent I/O performance with stable read/write latency.
        # - PL3: ultra-high peak concurrent I/O performance with extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # Pre-configured read/write IOPS for the node system disk.
        # 
        # Valid values: 0 to min{50,000, 1000\\*capacity - baseline performance}. Baseline performance = min{1,800+50\\*capacity, 50000}.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # Node system disk size. Unit: GiB.
        # 
        # Valid values: [20,2048\\].
        self.system_disk_size = system_disk_size
        # System disk snapshot policy.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # Tags added only to ECS instances.
        # 
        # Tag keys cannot be duplicated and can be up to 128 characters in length. Tag keys and tag values cannot start with “aliyun” or “acs:”, or contain “https://” or “http://”.
        self.tags = tags
        # List of vSwitch IDs. Valid values: [1,8\\].
        # 
        # > To ensure high availability, we recommend that you select vSwitches in different zones.
        # 
        # This parameter is required.
        self.vswitch_ids = vswitch_ids

    def validate(self):
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

        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled

        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand

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

        if self.security_hardening_os is not None:
            result['security_hardening_os'] = self.security_hardening_os

        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled

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

        if self.system_disk_snapshot_policy_id is not None:
            result['system_disk_snapshot_policy_id'] = self.system_disk_snapshot_policy_id

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

        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')

        if m.get('compensate_with_on_demand') is not None:
            self.compensate_with_on_demand = m.get('compensate_with_on_demand')

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
            temp_model = main_models.CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('private_pool_options'))

        if m.get('ram_role_name') is not None:
            self.ram_role_name = m.get('ram_role_name')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('resource_pool_options') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestScalingGroupResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('resource_pool_options'))

        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')

        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')

        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')

        if m.get('security_hardening_os') is not None:
            self.security_hardening_os = m.get('security_hardening_os')

        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')

        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')

        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')

        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k1 in m.get('spot_price_limit'):
                temp_model = main_models.CreateClusterNodePoolRequestScalingGroupSpotPriceLimit()
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

        if m.get('system_disk_snapshot_policy_id') is not None:
            self.system_disk_snapshot_policy_id = m.get('system_disk_snapshot_policy_id')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.CreateClusterNodePoolRequestScalingGroupTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        return self

class CreateClusterNodePoolRequestScalingGroupTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
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

class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # Preemptible instance type.
        self.instance_type = instance_type
        # Maximum price per instance.
        # <props="china">Unit: CNY/hour.
        # 
        # 
        # 
        # <props="intl">Unit: USD/hour.
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

class CreateClusterNodePoolRequestScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # List of private pool IDs, i.e., Elasticity Assurance IDs or Capacity Reservation IDs. Only Target mode private pool IDs can be passed. Valid values of N: 1 to 20.
        self.private_pool_ids = private_pool_ids
        # Resource pool policy used when creating instances. Resource pools include private pools generated after Elasticity Assurance or Capacity Reservation takes effect, and public pools, for instance startup selection. Valid values:
        # PrivatePoolFirst: private pool first. When this policy is selected and resouce_pool_options.private_pool_ids is specified, the specified private pools are used first. If no private pool is specified or the specified private pool capacity is insufficient, open-type private pools are automatically matched. If no eligible private pool is available, public pools are used to create instances.
        # PrivatePoolOnly: private pool only. When this policy is selected, resouce_pool_options.private_pool_ids must be specified. If the specified private pool capacity is insufficient, instance creation fails.
        # None: do not use resource pool policy.
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

class CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # Private pool ID. When `match_criteria` is set to `Target`, you must further specify the private pool ID.
        self.id = id
        # Private pool type. Private pool capacity option for instance startup. After an Elasticity Assurance or Capacity Reservation takes effect, private pool capacity is generated for instance startup. Valid values:
        # - `Open`: open mode. Automatically matches open-type private pool capacity. If no eligible private pool capacity is available, public pool resources are used.
        # - `Target`: targeted mode. Uses the specified private pool capacity to launch instances. If the specified capacity is unavailable, instance creation fails.
        # - `None`: do not use mode. Instances will not use private pool capacity.
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

class CreateClusterNodePoolRequestNodepoolInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # Node pool name.
        # 
        # This parameter is required.
        self.name = name
        # Resource group ID of the node pool. Instances created by the node pool will belong to this resource group.
        # 
        # A resource can only belong to one resource group. Based on different business scenarios, you can map resource groups to concepts such as projects, applications, or organizations.
        self.resource_group_id = resource_group_id
        # Node pool type. Valid values:
        # 
        # - `ess`: standard node pool (includes managed and auto scaling features).
        # - `edge`: edge node pool.
        # - `lingjun`: Lingjun node pool.
        # - `hybrid`: hybrid cloud node pool.
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

class CreateClusterNodePoolRequestNodeConfig(DaraModel):
    def __init__(
        self,
        kubelet_configuration: main_models.KubeletConfig = None,
    ):
        # Kubelet parameter configuration.
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

class CreateClusterNodePoolRequestNodeComponents(DaraModel):
    def __init__(
        self,
        config: main_models.CreateClusterNodePoolRequestNodeComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        # Node component configuration.
        self.config = config
        # Node component name.
        self.name = name
        # Node component version.
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
            temp_model = main_models.CreateClusterNodePoolRequestNodeComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class CreateClusterNodePoolRequestNodeComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
    ):
        # Node component custom configuration.
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

class CreateClusterNodePoolRequestManagement(DaraModel):
    def __init__(
        self,
        auto_fault_diagnosis: bool = None,
        auto_repair: bool = None,
        auto_repair_policy: main_models.CreateClusterNodePoolRequestManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.CreateClusterNodePoolRequestManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.CreateClusterNodePoolRequestManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: main_models.CreateClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Whether to automatically repair nodes. Takes effect only when `enable=true`.
        # 
        # - `true`: auto repair
        # 
        # - `false`: no auto repair
        # 
        # Default value: `true`
        self.auto_repair = auto_repair
        # Auto repair node policy.
        self.auto_repair_policy = auto_repair_policy
        # Whether to automatically upgrade nodes. Takes effect only when `enable=true`.
        # - `true`: enable auto upgrade.
        # - `false`: disable auto upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # Auto node upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Whether to automatically fix CVE vulnerabilities. Takes effect only when `enable=true`.
        # 
        # - `true`: allow automatic CVE fixing.
        # - `false`: do not allow automatic CVE fixing.
        # 
        # Default value: `true`.
        self.auto_vul_fix = auto_vul_fix
        # Auto CVE fix policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Whether to enable the managed feature for the node pool. Valid values:
        # 
        # - `true`: enable the managed feature.
        # 
        # - `false`: disable the managed feature. Other related configurations take effect only when enable=true.
        # 
        # Default value: false.
        self.enable = enable
        # [Deprecated] Use the `auto_upgrade` parameter at the parent level instead.
        # 
        # Auto upgrade configuration. Takes effect only when `enable=true`.
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
            temp_model = main_models.CreateClusterNodePoolRequestManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m.get('auto_repair_policy'))

        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('auto_upgrade_policy') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m.get('auto_upgrade_policy'))

        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')

        if m.get('auto_vul_fix_policy') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m.get('auto_vul_fix_policy'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('upgrade_config') is not None:
            temp_model = main_models.CreateClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m.get('upgrade_config'))

        return self

class CreateClusterNodePoolRequestManagementUpgradeConfig(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # [Deprecated] Use the `auto_upgrade` parameter at the parent level instead.
        # 
        # Whether to enable auto upgrade. Valid values:
        # 
        # - `true`: enable auto upgrade.
        # 
        # - `false`: disable auto upgrade.
        self.auto_upgrade = auto_upgrade
        # Maximum number of unavailable nodes.
        # Valid values: [1,1000\\]
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # Number of extra nodes. Mutually exclusive with `surge_percentage`.
        # 
        # Nodes become unavailable during upgrade. You can create extra nodes to compensate for the cluster workload.
        # 
        # > It is recommended that the number of extra nodes does not exceed the current number of nodes.
        self.surge = surge
        # Percentage of extra nodes. Mutually exclusive with `surge`.
        # 
        # Number of extra nodes = percentage of extra nodes × number of nodes. For example, if the percentage is set to 50% and there are 6 existing nodes, the number of extra nodes = 50% × 6 = 3.
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

class CreateClusterNodePoolRequestManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        exclude_packages: str = None,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # Packages to exclude during vulnerability patching.
        # 
        # Default value: `kernel`.
        self.exclude_packages = exclude_packages
        # Whether to allow node restart. Takes effect only when `auto_vul_fix=true`. Valid values:
        # - `true`: allow node restart
        # - `false`: do not allow node restart
        # 
        # Default value: `true`
        self.restart_node = restart_node
        # Vulnerability levels allowed for automatic fixing, separated by commas, for example: `asap,later`. Supported vulnerability levels:
        # 
        # - `asap`: high
        # - `later`: medium
        # - `nntf`: low
        # 
        # Default value: `asap`.
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_packages is not None:
            result['exclude_packages'] = self.exclude_packages

        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        if self.vul_level is not None:
            result['vul_level'] = self.vul_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exclude_packages') is not None:
            self.exclude_packages = m.get('exclude_packages')

        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')

        if m.get('vul_level') is not None:
            self.vul_level = m.get('vul_level')

        return self

class CreateClusterNodePoolRequestManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
        auto_upgrade_os: bool = None,
        auto_upgrade_runtime: bool = None,
    ):
        # Whether to allow automatic kubelet upgrade. Takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: allow automatic kubelet upgrade.
        # - `false`: do not allow automatic kubelet upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade_kubelet = auto_upgrade_kubelet
        # Whether to allow automatic OS upgrade. Takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: allow automatic OS upgrade.
        # - `false`: do not allow automatic OS upgrade.
        # 
        # 
        # Default value: `false`.
        self.auto_upgrade_os = auto_upgrade_os
        # Whether to allow automatic runtime upgrade. Takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: allow automatic runtime upgrade.
        # - `false`: do not allow automatic runtime upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade_runtime = auto_upgrade_runtime

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet

        if self.auto_upgrade_os is not None:
            result['auto_upgrade_os'] = self.auto_upgrade_os

        if self.auto_upgrade_runtime is not None:
            result['auto_upgrade_runtime'] = self.auto_upgrade_runtime

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')

        if m.get('auto_upgrade_os') is not None:
            self.auto_upgrade_os = m.get('auto_upgrade_os')

        if m.get('auto_upgrade_runtime') is not None:
            self.auto_upgrade_runtime = m.get('auto_upgrade_runtime')

        return self

class CreateClusterNodePoolRequestManagementAutoRepairPolicy(DaraModel):
    def __init__(
        self,
        approval_required: bool = None,
        restart_node: bool = None,
    ):
        # Whether node repair requires manual approval.
        self.approval_required = approval_required
        # Whether to allow node restart. Takes effect only when `auto_repair=true`. Valid values:
        # 
        # - `true`: allow node restart
        # - `false`: do not allow node restart
        # 
        # Default value: `true`
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.approval_required is not None:
            result['approval_required'] = self.approval_required

        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approval_required') is not None:
            self.approval_required = m.get('approval_required')

        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')

        return self

class CreateClusterNodePoolRequestKubernetesConfig(DaraModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[main_models.Tag] = None,
        node_name_mode: str = None,
        pre_user_data: str = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[main_models.Taint] = None,
        unschedulable: bool = None,
        user_data: str = None,
    ):
        # Whether to install CloudMonitor on ECS nodes. After installation, you can view monitoring information for created ECS instances in the CloudMonitor console. We recommend enabling this. Valid values:
        # 
        # - `true`: install CloudMonitor on ECS nodes.
        # 
        # - `false`: do not install CloudMonitor on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # Node CPU management policy. The following two policies are supported when the cluster version is 1.12.6 or later:
        # 
        # - `static`: allows enhanced CPU affinity and exclusivity for Pods with certain resource characteristics on the node.
        # - `none`: enables the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Node labels. Add labels to Kubernetes cluster nodes.
        self.labels = labels
        # Custom node name. After setting a custom node name, the node name, ECS instance name, and ECS instance hostname are all changed accordingly.
        # > For Windows instances with custom node names enabled, the hostname is fixed to the IP address with "-" replacing "." in the IP address, and does not include the prefix or suffix. 
        # 
        # A node name consists of three parts: prefix, node IP address, and suffix:
        # 
        # - Total length: 2 to 64 characters. The node name must start and end with a lowercase letter or digit.
        # 
        # - The prefix and suffix can contain uppercase and lowercase letters, digits, hyphens (-), and periods (.). They must start with a letter and cannot start or end with a hyphen (-) or period (.). Consecutive hyphens (-) or periods (.) are not allowed.
        # - The prefix is required (ECS restriction) and the suffix is optional.
        # - The node IP is the complete private IP address of the node.
        # 
        # Example: If the node IP address is 192.XX.YY.55, the prefix is aliyun.com, and the suffix is test:
        # 
        # - For Linux nodes, the node name, ECS instance name, and ECS instance hostname are all aliyun.com192.XX.YY.55test.
        # 
        # - For Windows nodes, the ECS instance hostname is 192-XX-YY-55, and the node name and ECS instance name are both aliyun.com192.XX.YY.55test.
        self.node_name_mode = node_name_mode
        # Instance pre-custom data. Before a node joins the cluster, the specified instance pre-custom data script is run. For more information, see [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # Container runtime name. ACK supports the following three container runtimes.
        # 
        # - containerd: recommended, supported by all cluster versions.
        # - Sandboxed-Container.runv: sandboxed container with higher isolation, supported by clusters of version 1.31 or earlier.
        # - docker: no longer maintained, supported by clusters of version 1.22 or earlier.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # Container runtime version.
        self.runtime_version = runtime_version
        # Taint configuration.
        self.taints = taints
        # Whether scaled-out nodes are unschedulable.
        # 
        # - true: unschedulable.
        # 
        # - false: schedulable.
        self.unschedulable = unschedulable
        # Instance custom data. After a node joins the cluster, the specified instance custom data script is run. For more information, see [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
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

        if self.pre_user_data is not None:
            result['pre_user_data'] = self.pre_user_data

        if self.runtime is not None:
            result['runtime'] = self.runtime

        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version

        result['taints'] = []
        if self.taints is not None:
            for k1 in self.taints:
                result['taints'].append(k1.to_map() if k1 else None)

        if self.unschedulable is not None:
            result['unschedulable'] = self.unschedulable

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

        if m.get('pre_user_data') is not None:
            self.pre_user_data = m.get('pre_user_data')

        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')

        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')

        self.taints = []
        if m.get('taints') is not None:
            for k1 in m.get('taints'):
                temp_model = main_models.Taint()
                self.taints.append(temp_model.from_map(k1))

        if m.get('unschedulable') is not None:
            self.unschedulable = m.get('unschedulable')

        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')

        return self

class CreateClusterNodePoolRequestInterconnectConfig(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        # [Deprecated]
        # 
        # Network bandwidth of the enhanced edge node pool. Unit: Mbps.
        self.bandwidth = bandwidth
        # [Deprecated]
        # 
        # CCN instance ID (CCN ID) bound to the enhanced edge node pool.
        self.ccn_id = ccn_id
        # [Deprecated]
        # 
        # Region of the CCN instance bound to the enhanced edge node pool.
        self.ccn_region_id = ccn_region_id
        # [Deprecated]
        # 
        # CEN instance ID (CEN ID) bound to the enhanced edge node pool.
        self.cen_id = cen_id
        # [Deprecated]
        # 
        # Subscription duration of the enhanced edge node pool. Unit: months.
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

class CreateClusterNodePoolRequestEfloNodeGroup(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        group_id: str = None,
    ):
        # Lingjun cluster ID to associate when creating a Lingjun node pool.
        self.cluster_id = cluster_id
        # Lingjun group ID of the Lingjun cluster to associate when creating a Lingjun node pool.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.group_id is not None:
            result['group_id'] = self.group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        return self

class CreateClusterNodePoolRequestAutoScaling(DaraModel):
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
        # [Deprecated] Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # Maximum EIP bandwidth. Unit: Mbps.
        self.eip_bandwidth = eip_bandwidth
        # [Deprecated] Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # EIP billing method. Valid values:
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-traffic.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Whether to enable auto scaling. Valid values:
        # 
        # - `true`: enables auto scaling for the node pool. When cluster capacity cannot meet Pod scheduling requirements, ACK automatically scales node resources based on the configured minimum and maximum instance counts. Clusters of version 1.24 or later enable instant node scaling by default;
        # clusters of versions earlier than 1.24 enable node auto scaling by default. For more information, see [Node scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: disables auto scaling. ACK adjusts the number of nodes in the node pool based on the configured desired node count, always maintaining the node count at the desired number.
        # 
        # When this parameter is set to false, other configuration parameters in `auto_scaling` do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # [Deprecated] This field is deprecated. Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # Whether to bind an EIP. Valid values:
        # 
        # - `true`: bind an EIP.
        # 
        # - `false`: do not bind an EIP.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # Maximum number of instances that can be scaled in the node pool, excluding existing instances. Takes effect only when `enable=true`.
        # 
        # Valid values: [min_instances, 2000]. Default value: 0.
        self.max_instances = max_instances
        # Minimum number of instances that can be scaled in the node pool, excluding existing instances. Takes effect only when `enable=true`.
        # 
        # Valid values: [0, max_instances]. Default value: 0.
        # 
        # > - When the minimum number of instances is not 0, the corresponding number of ECS instances will be automatically created after the scaling group takes effect.
        # > - It is recommended that the maximum number of instances is not smaller than the current number of nodes in the node pool. Otherwise, nodes in the node pool will be directly scaled in after auto scaling takes effect.
        self.min_instances = min_instances
        # Auto scaling instance type. Takes effect only when `enable=true`. Valid values:
        # 
        # - `cpu`: standard instance type.
        # 
        # - `gpu`: GPU instance type.
        # 
        # - `gpushare`: GPU sharing type.
        # 
        # - `spot`: preemptible instance type.
        # 
        # Default value: `cpu`.
        # >Notice: This field cannot be modified after the node pool is created.
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

class CreateClusterNodePoolRequestAutoMode(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Whether to enable intelligent managed mode.
        # Valid values:
        # - true: enable intelligent managed mode. Can only be enabled when the cluster has intelligent managed mode enabled.
        # - false: disable intelligent managed mode.
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable is not None:
            result['enable'] = self.enable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable') is not None:
            self.enable = m.get('enable')

        return self

