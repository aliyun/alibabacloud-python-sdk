# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNodePoolsResponseBody(DaraModel):
    def __init__(
        self,
        nodepools: List[main_models.DescribeClusterNodePoolsResponseBodyNodepools] = None,
    ):
        # The list of node pools.
        self.nodepools = nodepools

    def validate(self):
        if self.nodepools:
            for v1 in self.nodepools:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['nodepools'] = []
        if self.nodepools is not None:
            for k1 in self.nodepools:
                result['nodepools'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodepools = []
        if m.get('nodepools') is not None:
            for k1 in m.get('nodepools'):
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepools()
                self.nodepools.append(temp_model.from_map(k1))

        return self

class DescribeClusterNodePoolsResponseBodyNodepools(DaraModel):
    def __init__(
        self,
        auto_mode: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsAutoMode = None,
        auto_scaling: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling = None,
        eflo_node_group: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsEfloNodeGroup = None,
        interconnect_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig = None,
        management: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagement = None,
        max_nodes: int = None,
        node_components: List[main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponents] = None,
        node_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig = None,
        nodepool_info: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo = None,
        scaling_group: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup = None,
        status: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsStatus = None,
        tee_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig = None,
    ):
        # The auto mode configuration.
        self.auto_mode = auto_mode
        # The auto scaling configuration.
        self.auto_scaling = auto_scaling
        # The Lingjun node group information.
        self.eflo_node_group = eflo_node_group
        # **[Deprecated]** The network configuration for the edge node pool. This parameter is valid only for node pools whose type is edge.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter takes effect only when type is set to edge. Valid values:
        # 
        # - `basic`: Internet. Nodes in cloud node pool interact with cloud nodes over the Internet. Applications in cloud node pool cannot directly access the internal network of the cloud VPC.
        # - `private`: private network. Nodes in cloud node pool connect the cloud and on-premises networks through Express Connect circuits, VPNs, or CEN, which provides higher cloud-edge communication quality and more effective security protection.
        self.interconnect_mode = interconnect_mode
        # The cluster configuration.
        self.kubernetes_config = kubernetes_config
        # The managed node pool configuration. This configuration takes effect only in professional managed clusters.
        self.management = management
        # The maximum number of nodes that the node pool can accommodate. The value must be greater than or equal to 0. A value of 0 indicates no additional limit, meaning the node pool is only limited by the maximum number of nodes that the entire cluster can accommodate. For edge node pools, this value is usually greater than 0. For ESS node pools and default edge node pools, this value is 0.
        self.max_nodes = max_nodes
        # The list of node components.
        self.node_components = node_components
        # The node configuration.
        self.node_config = node_config
        # The node pool information.
        self.nodepool_info = nodepool_info
        # The scaling group configurations of the node pool.
        self.scaling_group = scaling_group
        # The status of the node pool.
        self.status = status
        # The confidential computing configurations.
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
        if self.status:
            self.status.validate()
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

        if self.eflo_node_group is not None:
            result['eflo_node_group'] = self.eflo_node_group.to_map()

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

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_mode') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsAutoMode()
            self.auto_mode = temp_model.from_map(m.get('auto_mode'))

        if m.get('auto_scaling') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling()
            self.auto_scaling = temp_model.from_map(m.get('auto_scaling'))

        if m.get('eflo_node_group') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsEfloNodeGroup()
            self.eflo_node_group = temp_model.from_map(m.get('eflo_node_group'))

        if m.get('interconnect_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m.get('interconnect_config'))

        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')

        if m.get('kubernetes_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('kubernetes_config'))

        if m.get('management') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagement()
            self.management = temp_model.from_map(m.get('management'))

        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')

        self.node_components = []
        if m.get('node_components') is not None:
            for k1 in m.get('node_components'):
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponents()
                self.node_components.append(temp_model.from_map(k1))

        if m.get('node_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig()
            self.node_config = temp_model.from_map(m.get('node_config'))

        if m.get('nodepool_info') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('nodepool_info'))

        if m.get('scaling_group') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('scaling_group'))

        if m.get('status') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('tee_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig()
            self.tee_config = temp_model.from_map(m.get('tee_config'))

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig(DaraModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        # Specifies whether to enable confidential computing for the cluster. Valid values:
        # - `true`: Enabled.
        # - `false`: Disabled.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsStatus(DaraModel):
    def __init__(
        self,
        failed_nodes: int = None,
        healthy_nodes: int = None,
        initial_nodes: int = None,
        offline_nodes: int = None,
        removing_nodes: int = None,
        serving_nodes: int = None,
        state: str = None,
        total_nodes: int = None,
    ):
        # The number of failed instances.
        self.failed_nodes = failed_nodes
        # The number of healthy instances.
        self.healthy_nodes = healthy_nodes
        # The number of nodes that are being created.
        self.initial_nodes = initial_nodes
        # The number of offline nodes.
        self.offline_nodes = offline_nodes
        # The number of nodes that are being removed.
        self.removing_nodes = removing_nodes
        # The number of nodes in the serving state.
        self.serving_nodes = serving_nodes
        # The state of the node pool. Valid values:
        # - `active`: Active.
        # - `scaling`: Scaling.
        # - `removing`: Removing.
        # - `deleting`: Deleting.
        # - `updating`: Updating.
        self.state = state
        # The number of nodes in the node pool.
        self.total_nodes = total_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.failed_nodes is not None:
            result['failed_nodes'] = self.failed_nodes

        if self.healthy_nodes is not None:
            result['healthy_nodes'] = self.healthy_nodes

        if self.initial_nodes is not None:
            result['initial_nodes'] = self.initial_nodes

        if self.offline_nodes is not None:
            result['offline_nodes'] = self.offline_nodes

        if self.removing_nodes is not None:
            result['removing_nodes'] = self.removing_nodes

        if self.serving_nodes is not None:
            result['serving_nodes'] = self.serving_nodes

        if self.state is not None:
            result['state'] = self.state

        if self.total_nodes is not None:
            result['total_nodes'] = self.total_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('failed_nodes') is not None:
            self.failed_nodes = m.get('failed_nodes')

        if m.get('healthy_nodes') is not None:
            self.healthy_nodes = m.get('healthy_nodes')

        if m.get('initial_nodes') is not None:
            self.initial_nodes = m.get('initial_nodes')

        if m.get('offline_nodes') is not None:
            self.offline_nodes = m.get('offline_nodes')

        if m.get('removing_nodes') is not None:
            self.removing_nodes = m.get('removing_nodes')

        if m.get('serving_nodes') is not None:
            self.serving_nodes = m.get('serving_nodes')

        if m.get('state') is not None:
            self.state = m.get('state')

        if m.get('total_nodes') is not None:
            self.total_nodes = m.get('total_nodes')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cis_enabled: bool = None,
        compensate_with_on_demand: bool = None,
        cpu_options: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupCpuOptions = None,
        data_disks: List[main_models.DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        disk_init: List[main_models.DiskInit] = None,
        enable_high_density_mode: bool = None,
        image_id: str = None,
        image_type: str = None,
        instance_charge_type: str = None,
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
        private_pool_options: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions = None,
        ram_policy: str = None,
        ram_role_name: str = None,
        rds_instances: List[str] = None,
        resource_pool_options: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupResourcePoolOptions = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_hardening_os: bool = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit] = None,
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
        tags: List[main_models.Tag] = None,
        vswitch_ids: List[str] = None,
    ):
        # Specifies whether to enable auto-renewal for nodes. This parameter takes effect only when instance_charge_type is set to PrePaid. Valid values:
        # - true: enables auto-renewal.
        # - false: disables auto-renewal.
        self.auto_renew = auto_renew
        # The auto-renewal duration. Valid values:
        # - If PeriodUnit is set to Week: 1, 2, and 3.
        # - If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        self.auto_renew_period = auto_renew_period
        # **[Deprecated]** Use the security_hardening_os parameter instead.
        self.cis_enabled = cis_enabled
        # Specifies whether to automatically create pay-as-you-spot instances to meet the required number of ECS instances when the multi_az_policy parameter is set to COST_OPTIMIZED and sufficient preemptible instances cannot be created due to price or inventory issues. Valid values:
        # - true: allows the system to automatically create pay-as-you-spot instances.
        # - false: does not allow the system to automatically create pay-as-you-spot instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The CPU-related configuration options.
        self.cpu_options = cpu_options
        # The configurations of the data cloud disks for nodes, such as the disk category and size.
        self.data_disks = data_disks
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The block device initialization configurations.
        self.disk_init = disk_init
        # Specifies whether to enable the high-density cloud disk mode. This mode is supported only when the node pool uses instance types. After this mode is enabled, the total number of system cloud disks and data cloud disks does not exceed the maximum number of high-density cloud disks supported by the instance type.
        self.enable_high_density_mode = enable_high_density_mode
        # The custom image ID. You can call the DescribeKubernetesVersionMetadata operation to query the images supported by the system.
        self.image_id = image_id
        # The operating system image type. Valid values:
        # - AliyunLinux: Alinux2 image.
        # - AliyunLinuxSecurity: Alinux2 UEFI image.
        # - AliyunLinux3: Alinux3 image.
        # - AliyunLinux3Arm64: Alinux3 ARM image.
        # - AliyunLinux3Security: Alinux3 UEFI image.
        # - CentOS: CentOS image.
        # - Windows: Windows image.
        # - WindowsCore: Windows Core image.
        # - ContainerOS: container-optimized image.
        # - AliyunLinux3ContainerOptimized: Alinux3 container-optimized image.
        self.image_type = image_type
        # The billing method of nodes in the node pool. Valid values:
        # - PrePaid: subscription.
        # - PostPaid: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The instance property configurations.
        self.instance_patterns = instance_patterns
        # The list of instance types for nodes. You can select multiple instance types as alternatives. When a node is created, the system attempts to purchase instances starting from the first instance type in the list until the creation succeeds. The final instance type purchased may vary depending on inventory availability.
        self.instance_types = instance_types
        # The billing method of the public IP address for the node. Valid values:
        # - PayByBandwidth: pay-by-bandwidth.
        # - PayByTraffic: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must specify this parameter or login_password.
        # If the node pool is a managed node pool, only key_pair is supported.
        self.key_pair = key_pair
        # Specifies whether to log on to the created ECS instances as a non-root user. Valid values:
        # - true: logs on as a non-root user (ecs-user).
        # - false: logs on as the root user.
        self.login_as_non_root = login_as_non_root
        # The SSH logon password. You must specify this parameter or key_pair. The password must be 8 to 30 characters in length and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # For security reasons, the password is encrypted in the query result.
        self.login_password = login_password
        # The scaling policy for ECS instances in a multi-zone scaling group. Valid values:
        # - `PRIORITY`: scales ECS instances based on the priorities of the vSwitches that you specify in the VSwitchIds.N parameter. If ECS instances cannot be created in the zone of the highest-priority vSwitch, the system automatically uses the next highest-priority vSwitch to create ECS instances.
        # - `COST_OPTIMIZED`: creates ECS instances based on the unit prices of vCPUs in ascending order. When the scaling configuration settings include multiple instance types with the spot instance billing method, the system preferentially creates spot instances. You can use the CompensateWithOnDemand parameter to specify whether to automatically create pay-as-you-go instances when spot instances cannot be created due to inventory shortages or other reasons.
        #   > The `COST_OPTIMIZED` value takes effect only when the scaling configuration settings include multiple instance types or use spot instances.
        # - `BALANCE`: evenly allocates ECS instances across the zones specified in the scaling group. If the distribution of instances becomes unbalanced across zones due to inventory shortages, you can call the [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html) operation to balance the resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances required in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than this value, the system preferentially creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the additional instances that exceed the minimum number of pay-as-you-go instances specified by on_demand_base_capacity. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of the node. This parameter takes effect and is required only when instance_charge_type is set to PrePaid. Valid values:
        # - If period_unit is set to Week: 1, 2, 3, and 4.
        # - If period_unit is set to Month: 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of the node. This parameter is required when instance_charge_type is set to PrePaid. Valid values:
        # - `Month`: uses month as the billing unit.
        # - `Week`: uses week as the billing unit.
        self.period_unit = period_unit
        # **[Deprecated]** The operating system distribution. Valid values:
        # - CentOS
        # - AliyunLinux
        # - Windows
        # - WindowsCore
        self.platform = platform
        # The private pool options.
        self.private_pool_options = private_pool_options
        # **[Deprecated]** Use the ram_role_name parameter instead.
        self.ram_policy = ram_policy
        # The name of the RAM role for worker nodes.
        self.ram_role_name = ram_role_name
        # If ApsaraDB RDS instances are specified, the ECS instances of the cluster nodes are automatically added to the whitelists of the ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The resource pool and resource pool policy used to create instances.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The scaling group pattern. Valid values:
        # - `release`: Standard pattern. The scaling group scales instances by creating and releasing ECS instances based on the requested resource usage.
        # - `recycle`: Swift pattern. The scaling group scales instances by creating, stopping, and starting ECS instances to improve the scaling speed. When an instance is stopped, you are not charged for compute resources, but you are still charged for storage resources. This does not apply to instances with local disks.
        self.scaling_policy = scaling_policy
        # **[Deprecated]** The ID of the security group to which the node pool belongs. If the node pool is associated with multiple security groups, this parameter returns the first value in `security_group_ids`.
        self.security_group_id = security_group_id
        # The list of security group IDs for the node pool.
        self.security_group_ids = security_group_ids
        # Specifies whether to enable Alibaba Cloud OS security hardening. Valid values:
        # - `true`: Enables Alibaba Cloud OS security hardening.
        # - `false`: Does not enable Alibaba Cloud OS security hardening.
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Specifies whether to enable MLPS 2.0 security hardening. You can enable MLPS 2.0 security hardening for nodes only when the system image is Alibaba Cloud Linux 2 or Alibaba Cloud Linux 3. Alibaba Cloud provides baseline check standards and scanning programs for classified protection compliance for Alibaba Cloud Linux 2 and Alibaba Cloud Linux 3 MLPS 2.0 Level 3 images.
        self.soc_enabled = soc_enabled
        # The number of available instance types. The scaling group evenly creates spot instances across multiple instance types with the lowest costs. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable spot instance replenishment. After this feature is enabled, when the scaling group receives a system message indicating that a spot instance will be reclaimed, the scaling group attempts to create a new instance to replace the spot instance to be reclaimed. Valid values:
        # - `true`: Enables spot instance replenishment.
        # - `false`: Does not enable spot instance replenishment.
        self.spot_instance_remedy = spot_instance_remedy
        # The market price range configuration for spot instances.
        self.spot_price_limit = spot_price_limit
        # The type of spot instance. Valid values:
        # - NoSpot: Pay-as-you-go instance.
        # - SpotWithPriceLimit: Sets the maximum price for spot instances.
        # - SpotAsPriceGo: Uses the system automatic bidding, which follows the actual market price.
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable the burst feature for the system disk of the node. Valid values:
        # - true: Enables the burst feature. After this feature is enabled, if a volatile workload faces sudden data read and write pressure, the cloud disk temporarily improves its performance based on the actual workload conditions until the workload returns to a stable state.
        # - false: Does not enable the burst feature.
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The categories of the system disk. If the system disk cannot be created by using the disk category with the highest priority, the system automatically attempts to use the disk category with the next highest priority.
        self.system_disk_categories = system_disk_categories
        # The category of the system disk. Valid values:
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: Standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        self.system_disk_category = system_disk_category
        # The encryption algorithm used for the system disk. Valid value: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # - true: Encrypts the system disk.
        # - false: Does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key used for the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system disk. This parameter takes effect only for ESSDs. The performance level is related to the cloud disk size. For more information, see [ESSD](https://help.aliyun.com/document_detail/122389.html). Valid values:
        # - PL0: Medium concurrent I/O performance and relatively stable read/write latency.
        # - PL1: Medium concurrent I/O performance and relatively stable read/write latency.
        # - PL2: High concurrent I/O performance and stable read/write latency.
        # - PL3: Extremely high concurrent I/O performance and extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS for the system disk. This parameter is configured when the disk category is `cloud_auto`.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk. Unit: GiB. Valid values: 20 to 2048.
        self.system_disk_size = system_disk_size
        # The snapshot policy for the system disk.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # The ECS instance labels.
        self.tags = tags
        # The list of vSwitch IDs.
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

        if self.enable_high_density_mode is not None:
            result['enable_high_density_mode'] = self.enable_high_density_mode

        if self.image_id is not None:
            result['image_id'] = self.image_id

        if self.image_type is not None:
            result['image_type'] = self.image_type

        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type

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

        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy

        if self.ram_role_name is not None:
            result['ram_role_name'] = self.ram_role_name

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.resource_pool_options is not None:
            result['resource_pool_options'] = self.resource_pool_options.to_map()

        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id

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

        if m.get('cpu_options') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupCpuOptions()
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

        if m.get('enable_high_density_mode') is not None:
            self.enable_high_density_mode = m.get('enable_high_density_mode')

        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')

        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')

        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')

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
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('private_pool_options'))

        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')

        if m.get('ram_role_name') is not None:
            self.ram_role_name = m.get('ram_role_name')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('resource_pool_options') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('resource_pool_options'))

        if m.get('scaling_group_id') is not None:
            self.scaling_group_id = m.get('scaling_group_id')

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
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit()
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
                temp_model = main_models.Tag()
                self.tags.append(temp_model.from_map(k1))

        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # The market price range for a single instance.
        # 
        # <props="china">Unit: CNY/hour.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # The list of private pool IDs.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy used to create instances. Valid values:
        # - PrivatePoolFirst: Private pools are used first.
        # - PrivatePoolOnly: Only private pools are used.
        # - None: No resource pool policy is used.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The private pool ID, which is the ID of the elasticity assurance or capacity reservation.
        self.id = id
        # The private pool capacity matching criteria for instance startup. After an elasticity assurance or capacity reservation takes effect, private pool capacity is generated for you to select when you start instances. Valid values:
        # - Open: open mode. The system automatically matches the capacity of an open private pool. If no matching private pool capacity is available, the system uses public pool resources to start the instance. In this mode, you do not need to specify the PrivatePoolOptions.Id parameter.
        # - Target: specified mode. The system uses the capacity of the specified private pool to start the instance. If the specified private pool capacity is unavailable, the instance fails to start. In this mode, you must specify the private pool ID by setting the PrivatePoolOptions.Id parameter.
        # - None: no private pool mode. The system does not use private pool capacity to start the instance.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupCpuOptions(DaraModel):
    def __init__(
        self,
        nested_virtualization: str = None,
    ):
        # Specifies whether to enable nested virtualization. Valid values:
        # - disabled: disables nested virtualization.
        # - enabled: enables nested virtualization.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo(DaraModel):
    def __init__(
        self,
        created: str = None,
        is_default: bool = None,
        name: str = None,
        nodepool_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        type: str = None,
        updated: str = None,
    ):
        # The time when the node pool was created.
        self.created = created
        # Specifies whether the node pool is the default node pool. Typically, a cluster has only one default node pool. Valid values:
        # - true: The node pool is the default node pool.
        # - false: The node pool is not the default node pool.
        self.is_default = is_default
        # The node pool name.
        self.name = name
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The node pool type. Valid values:
        # - `ess`: standard node pool, which includes managed and auto scaling features.
        # - `edge`: edge node pool.
        # - `lingjun`: Lingjun node pool.
        self.type = type
        # The time when the node pool was updated.
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.is_default is not None:
            result['is_default'] = self.is_default

        if self.name is not None:
            result['name'] = self.name

        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id

        if self.region_id is not None:
            result['region_id'] = self.region_id

        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id

        if self.type is not None:
            result['type'] = self.type

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('is_default') is not None:
            self.is_default = m.get('is_default')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')

        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig(DaraModel):
    def __init__(
        self,
        kubelet_configuration: main_models.KubeletConfig = None,
        node_os_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfigNodeOsConfig = None,
    ):
        # The Kubelet parameter settings.
        self.kubelet_configuration = kubelet_configuration
        # The node operating system configuration.
        self.node_os_config = node_os_config

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()
        if self.node_os_config:
            self.node_os_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()

        if self.node_os_config is not None:
            result['node_os_config'] = self.node_os_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = main_models.KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m.get('kubelet_configuration'))

        if m.get('node_os_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfigNodeOsConfig()
            self.node_os_config = temp_model.from_map(m.get('node_os_config'))

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfigNodeOsConfig(DaraModel):
    def __init__(
        self,
        hugepage: main_models.Hugepage = None,
        sysctl: Dict[str, Any] = None,
    ):
        # The Hugepage configuration.
        self.hugepage = hugepage
        # The sysctl kernel parameter settings.
        self.sysctl = sysctl

    def validate(self):
        if self.hugepage:
            self.hugepage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hugepage is not None:
            result['hugepage'] = self.hugepage.to_map()

        if self.sysctl is not None:
            result['sysctl'] = self.sysctl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hugepage') is not None:
            temp_model = main_models.Hugepage()
            self.hugepage = temp_model.from_map(m.get('hugepage'))

        if m.get('sysctl') is not None:
            self.sysctl = m.get('sysctl')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponents(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfig = None,
        config_revision: str = None,
        name: str = None,
        version: str = None,
    ):
        # The node component configuration.
        self.config = config
        # The version number of the custom configuration for the node component.
        self.config_revision = config_revision
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

        if self.config_revision is not None:
            result['config_revision'] = self.config_revision

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('config_revision') is not None:
            self.config_revision = m.get('config_revision')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, Any] = None,
        envs: List[main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfigEnvs] = None,
    ):
        # The custom configuration of the node component.
        self.custom_config = custom_config
        # The environment variables of the node component.
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
                temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfigEnvs()
                self.envs.append(temp_model.from_map(k1))

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsNodeComponentsConfigEnvs(DaraModel):
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

class DescribeClusterNodePoolsResponseBodyNodepoolsManagement(DaraModel):
    def __init__(
        self,
        auto_fault_diagnosis: bool = None,
        auto_repair: bool = None,
        auto_repair_policy: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy = None,
        drift_enabled: bool = None,
        enable: bool = None,
        upgrade_config: main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig = None,
    ):
        # Specifies whether to enable ECS fault detection for node self-healing.
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Specifies whether to enable auto repair. This parameter takes effect only when enable is set to true. Valid values:
        # 
        # - `true`: enables auto repair.
        # - `false`: disables auto repair.
        self.auto_repair = auto_repair
        # The auto repair policy for nodes.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to automatically upgrade nodes. This parameter takes effect only when enable is set to true. Valid values:
        # - true: Auto-upgrade is enabled.
        # - false: Auto-upgrade is disabled.
        self.auto_upgrade = auto_upgrade
        # The auto-upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically fix CVEs. This parameter takes effect only when enable is set to true. Valid values:
        # - true: Automatic CVE fixes are allowed.
        # - false: Automatic CVE fixes are not allowed.
        self.auto_vul_fix = auto_vul_fix
        # The auto CVE fix policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the node rotation capability. This capability is supported only by smart managed node pools and is enabled by default. It is not supported by regular node pools.
        self.drift_enabled = drift_enabled
        # Specifies whether to enable the managed node pool. Valid values:
        # - true: The managed node pool is enabled.
        # - false: The managed node pool is disabled. Other related configurations take effect only when enable is set to true.
        self.enable = enable
        # The auto-upgrade configuration. This configuration takes effect only when enable is set to true.
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
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m.get('auto_repair_policy'))

        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('auto_upgrade_policy') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m.get('auto_upgrade_policy'))

        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')

        if m.get('auto_vul_fix_policy') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m.get('auto_vul_fix_policy'))

        if m.get('drift_enabled') is not None:
            self.drift_enabled = m.get('drift_enabled')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('upgrade_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m.get('upgrade_config'))

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # Specifies whether to enable auto-upgrade. Valid values:
        # - true: Auto-upgrade is enabled.
        # - false: Auto-upgrade is disabled.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes. Valid values: 1 to 1000. Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of surge nodes. This parameter and surge_percentage are mutually exclusive.
        self.surge = surge
        # The percentage of surge nodes. This parameter and surge are mutually exclusive. The number of surge nodes is calculated by multiplying the surge node percentage by the total number of nodes. For example, if the surge node percentage is set to 50% and the total number of nodes is 6, the number of surge nodes generated is 50% × 6 = 3.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        exclude_packages: str = None,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # The packages to be excluded during the vulnerability fix process.
        self.exclude_packages = exclude_packages
        # Specifies whether to allow node restarts. This parameter takes effect only when auto_vul_fix is set to true. Valid values:
        # - true: Node restarts are allowed.
        # - false: Node restarts are not allowed.
        self.restart_node = restart_node
        # The vulnerability levels that are allowed for automatic fixes, separated by commas. Valid values:
        # - asap: High.
        # - later: Medium.
        # - nntf: Low.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # Specifies whether to allow automatic kubelet upgrades. This parameter takes effect only when auto_upgrade is set to true. Valid values:
        # - true: Automatic kubelet upgrades are allowed.
        # - false: Automatic kubelet upgrades are not allowed.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy(DaraModel):
    def __init__(
        self,
        approval_required: bool = None,
        auto_repair_policy_id: str = None,
        max_parallel_repairing_nodes: str = None,
        max_unhealthy_nodes_threshold: str = None,
        restart_node: bool = None,
    ):
        # Specifies whether manual approval is required for node repair.
        self.approval_required = approval_required
        # The ID of the auto-repair policy.
        self.auto_repair_policy_id = auto_repair_policy_id
        # The maximum number or percentage of nodes that can be repaired simultaneously when a large number of abnormal nodes exist in the node pool.
        self.max_parallel_repairing_nodes = max_parallel_repairing_nodes
        # The auto-healing circuit breaker condition. When the number or percentage of faulty nodes exceeds this threshold, auto-healing enters the circuit breaker state and stops initiating new auto-healing repair actions.
        self.max_unhealthy_nodes_threshold = max_unhealthy_nodes_threshold
        # Specifies whether to allow node restarts. This parameter takes effect only when auto_repair is set to true. Valid values:
        # - true: Node restarts are allowed.
        # - false: Node restarts are not allowed.
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

        if self.auto_repair_policy_id is not None:
            result['auto_repair_policy_id'] = self.auto_repair_policy_id

        if self.max_parallel_repairing_nodes is not None:
            result['max_parallel_repairing_nodes'] = self.max_parallel_repairing_nodes

        if self.max_unhealthy_nodes_threshold is not None:
            result['max_unhealthy_nodes_threshold'] = self.max_unhealthy_nodes_threshold

        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approval_required') is not None:
            self.approval_required = m.get('approval_required')

        if m.get('auto_repair_policy_id') is not None:
            self.auto_repair_policy_id = m.get('auto_repair_policy_id')

        if m.get('max_parallel_repairing_nodes') is not None:
            self.max_parallel_repairing_nodes = m.get('max_parallel_repairing_nodes')

        if m.get('max_unhealthy_nodes_threshold') is not None:
            self.max_unhealthy_nodes_threshold = m.get('max_unhealthy_nodes_threshold')

        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig(DaraModel):
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
        # Specifies whether to install the CloudMonitor agent on ECS nodes. After installation, you can view the monitoring information of the created ECS instances in the CloudMonitor console. We recommend that you enable this feature. Valid values:
        # 
        # - `true`: installs the CloudMonitor agent on ECS nodes.
        # - `false`: does not install the CloudMonitor agent on ECS nodes.
        self.cms_enabled = cms_enabled
        # The CPU management policy for nodes. The following two policies are supported when the cluster version is 1.12.6 or later:
        # 
        # - `static`: allows pods with specific resource characteristics on the node to enhance their CPU affinity and exclusivity.
        # - `none`: uses the existing default CPU affinity scheme.
        self.cpu_policy = cpu_policy
        # The node labels.
        self.labels = labels
        # The custom node name.
        # 
        # A node name consists of three parts: prefix + node IP address substring + suffix:
        #  
        # - The prefix and suffix can each consist of one or more parts separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or a digit.
        # - The IP address substring length refers to the number of digits intercepted from the end of the node IP address. Valid values: 5 to 12.
        #  
        # For example, if the node IP address is 192.168.0.55, the specified prefix is aliyun.com, the IP address substring length is 5, and the suffix is test, the node name is aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The pre-custom data of the node pool, which is the script that runs before node initialization. For more information, see [Generate instance user data](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The name of the container runtime. ACK supports the following three container runtimes:
        # 
        # - containerd: recommended. Supported by all cluster versions.
        # - Sandboxed-Container.runv: sandboxed container. Provides higher isolation. Supported by clusters of Kubernetes 1.31 and earlier.
        # - docker: no longer maintained. Supported by clusters of Kubernetes 1.22 and earlier.
        self.runtime = runtime
        # The container runtime version.
        self.runtime_version = runtime_version
        # The taint information of the node. Taints and tolerations work together to prevent pods from being scheduled to inappropriate nodes. For more information, see [Taints and Tolerations](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # Specifies whether the scaled-out nodes are unschedulable. Valid values:
        # 
        # - `true`: unschedulable.
        # 
        # - `false`: schedulable.
        self.unschedulable = unschedulable
        # The custom data of the node pool, which is the script that runs after node initialization. For more information, see [Generate instance user data](https://help.aliyun.com/document_detail/49121.html).
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

class DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig(DaraModel):
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

class DescribeClusterNodePoolsResponseBodyNodepoolsEfloNodeGroup(DaraModel):
    def __init__(
        self,
        auto_attach_enabled: bool = None,
        cluster_id: str = None,
        group_id: str = None,
        worker_ram_role_name: str = None,
    ):
        # Specifies whether to enable auto-attach for the Lingjun node pool. This parameter does not take effect.
        self.auto_attach_enabled = auto_attach_enabled
        # The ID of the Lingjun cluster.
        self.cluster_id = cluster_id
        # The ID of the Lingjun group.
        self.group_id = group_id
        # The name of the worker RAM role used by the Lingjun node pool.
        self.worker_ram_role_name = worker_ram_role_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_attach_enabled is not None:
            result['auto_attach_enabled'] = self.auto_attach_enabled

        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id

        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_attach_enabled') is not None:
            self.auto_attach_enabled = m.get('auto_attach_enabled')

        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')

        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')

        return self

class DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling(DaraModel):
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
        # The peak bandwidth of the elastic IP address (EIP). Valid values: 1 to 100. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # The billing method of the EIP. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-data-transfer.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # 
        # - `true`: enables auto scaling for the node pool. When the capacity planning of the cluster cannot meet the scheduling requirements of application pods, ACK automatically scales node resources based on the configured minimum and maximum number of instances. For clusters of Kubernetes 1.24 and later, node instant elasticity is enabled by default. For clusters earlier than Kubernetes 1.24, node auto scaling is enabled by default. For more information, see [Node auto scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: disables auto scaling. ACK adjusts the number of nodes in the node pool based on the configured expected number of nodes, and always maintains the number of nodes at the expected number.
        # 
        # If this parameter is set to false, other configuration parameters in auto_scaling do not take effect.
        self.enable = enable
        # Specifies whether to associate an EIP. Valid values:
        # 
        # - `true`: associates an EIP.
        # - `false`: does not associate an EIP.
        self.is_bond_eip = is_bond_eip
        # The maximum number of scalable instances in the node pool, excluding existing instances.
        self.max_instances = max_instances
        # The minimum number of scalable instances in the node pool, excluding existing instances.
        self.min_instances = min_instances
        # The auto scaling type, which is categorized by the auto scaling instance type. Valid values:
        # 
        # - `cpu`: regular instance.
        # - `gpu`: GPU-accelerated instance.
        # - `gpushare`: shared GPU instance.
        # - `spot`: spot instance.
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

class DescribeClusterNodePoolsResponseBodyNodepoolsAutoMode(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        # Specifies whether to enable auto mode.
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

