# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

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
        # The intelligent managed node pool configurations.
        self.auto_mode = auto_mode
        # The auto scaling configurations.
        self.auto_scaling = auto_scaling
        # [This parameter is deprecated] Use desired_size instead.
        # 
        # The number of nodes in the node pool.
        self.count = count
        # The Lingjun node pool configurations.
        self.eflo_node_group = eflo_node_group
        # Specifies whether to use the host network for the pod network.
        # 
        # - `true`: host network. Pods directly use the network stack of the host and share the IP address and ports with the host.
        # 
        # - `false`: container network. Pods have an independent network stack and do not occupy host network ports.
        self.host_network = host_network
        # [This parameter is deprecated]
        # 
        # The configurations of the edge node pool.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter takes effect only for node pools of the \\`edge\\` type. Valid values:
        # 
        # - `basic`: public network. Nodes in the node pool interact with cloud nodes over the Internet. Applications in the node pool cannot directly access the VPC in the cloud.
        # 
        # - `private`: private network. Nodes in the node pool connect to the cloud over a leased line, VPN, or CEN to achieve higher communication quality and better security.
        self.interconnect_mode = interconnect_mode
        # Specifies whether nodes in the edge node pool can communicate with each other at Layer 3.
        # 
        # - `true`: All nodes in the node pool can communicate with each other at Layer 3.
        # 
        # - `false`: All hosts in the node pool cannot communicate with each other at Layer 3.
        self.intranet = intranet
        # The cluster-related configurations.
        self.kubernetes_config = kubernetes_config
        # The configurations of the managed node pool feature.
        self.management = management
        # [This parameter is deprecated]
        # 
        # The maximum number of nodes that the edge node pool can contain.
        self.max_nodes = max_nodes
        # A list of node components.
        self.node_components = node_components
        # The node configurations.
        self.node_config = node_config
        # The node pool configurations.
        self.nodepool_info = nodepool_info
        # The configurations of the scaling group for the node pool.
        self.scaling_group = scaling_group
        # The configurations of the confidential computing cluster.
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
        # Specifies whether to enable the confidential computing cluster.
        # 
        # - true: Enables confidential computing.
        # 
        # - false: Disables confidential computing.
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
        # Specifies whether to enable auto-renewal for the nodes in the node pool. This parameter takes effect only if \\`instance_charge_type\\` is set to \\`PrePaid\\`. Valid values:
        # 
        # - `true`: enables auto-renewal.
        # 
        # - `false`: disables auto-renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # 
        # - If \\`PeriodUnit\\` is set to \\`Week\\`: 1, 2, and 3.
        # 
        # - If \\`PeriodUnit\\` is set to \\`Month\\`: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # [Deprecated] Use the \\`security_hardening_os\\` parameter instead.
        self.cis_enabled = cis_enabled
        # Specifies whether to automatically create pay-as-you-go instances to meet the instance quantity requirement when \\`multi_az_policy\\` is set to \\`COST_OPTIMIZED\\` and spot instances cannot be created due to issues such as price or insufficient inventory. Valid values:
        # 
        # - `true`: Allows the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        # 
        # - `false`: Does not allow the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The data disk configurations of the nodes in the node pool.
        self.data_disks = data_disks
        # The ID of the deployment set. You can use a deployment set to distribute the ECS instances created in the node pool across different physical servers to ensure high availability and underlying disaster recovery. When you create ECS instances in a deployment set, the instances are launched in the specified region based on the deployment strategy that you set.
        # 
        # >Notice: 
        # 
        # After you select a deployment set, the maximum number of nodes in the node pool is limited. By default, a deployment set supports a maximum of 20 × Number of zones (the number of zones is determined by the vSwitches) nodes. Select a deployment set with sufficient quota to prevent node creation failures.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        # 
        # The total number of nodes that the node pool should maintain. We recommend that you configure at least two nodes to ensure that cluster components run as expected. You can adjust the expected number of nodes to scale out or scale in the node pool.
        # 
        # If you do not need to create nodes, set this parameter to 0. You can manually adjust the number of nodes later.
        self.desired_size = desired_size
        # The block device initialization configurations.
        self.disk_init = disk_init
        # The ID of the custom image. By default, the system-provided image is used.
        self.image_id = image_id
        # The OS image type. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # 
        # - `AliyunLinuxSecurity`: Alinux2 UEFI image.
        # 
        # - `AliyunLinux3`: Alinux3 image.
        # 
        # - `AliyunLinux3Arm64`: Alinux3 ARM image.
        # 
        # - `AliyunLinux3Security`: Alinux3 UEFI image.
        # 
        # - `CentOS`: CentOS image.
        # 
        # - `Windows`: Windows image.
        # 
        # - `WindowsCore`: WindowsCore image.
        # 
        # - `ContainerOS`: Container-Optimized OS.
        # 
        # - `AliyunLinux3ContainerOptimized`: Alinux3 Container-Optimized OS.
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # - `PrePaid`: subscription.
        # 
        # - `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # The ECS instance metadata access configurations.
        self.instance_metadata_options = instance_metadata_options
        # The instance property configurations.
        self.instance_patterns = instance_patterns
        # A list of instance types for the nodes in the node pool. When the system creates nodes in the node pool, it selects an instance type from the list that meets the requirements.
        # 
        # The number of instance types must be in the range of [1, 10].
        # 
        # > For high availability, we recommend that you select multiple instance types.
        # 
        # This parameter is required.
        self.instance_types = instance_types
        # The billing method of the public IP address. Valid values:
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # 
        # - PayByTraffic: pay-by-traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth of the node. Unit: Mbit/s. The value must be in the range of [1, 100].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair that is used for passwordless logon. You must specify one of \\`key_pair\\` and \\`login_password\\`.
        # 
        # > If you select Container-Optimized OS for the node pool, you can use only \\`key_pair\\`.
        self.key_pair = key_pair
        # Specifies whether to log on to the created ECS instances as a non-root user.
        # 
        # - true: Logs on as the ecs-user.
        # 
        # - false: Logs on as the root user.
        self.login_as_non_root = login_as_non_root
        # The SSH logon password. You must specify one of \\`key_pair\\` and \\`login_password\\`. The password must be 8 to 30 characters in length, and contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The scaling policy for the ECS instances in the multi-zone scaling group. Valid values:
        # 
        # - `PRIORITY`: Scales instances based on the vSwitch priority. The system scales instances based on the order of vSwitches that you specify in \\`VSwitchIds.N\\`. If the system fails to create an ECS instance in the zone where the vSwitch with the highest priority resides, it automatically uses the vSwitch with the next highest priority to create the instance.
        # 
        # - `COST_OPTIMIZED`: Creates instances based on the vCPU unit price in ascending order. When multiple instance types are specified and the preemptible instance policy is configured, the system gives priority to creating the lowest-cost instance type. You can also use the \\`CompensateWithOnDemand\\` parameter to specify whether to automatically create pay-as-you-go instances when preemptible instances cannot be created due to insufficient inventory.
        # 
        #   > `COST_OPTIMIZED` takes effect only when multiple instance types are specified or the preemptible instance policy is configured.
        # 
        # - `BALANCE`: Evenly distributes ECS instances across the specified zones. If the distribution of ECS instances becomes unbalanced due to insufficient inventory, you can call the API [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html) operation to balance the resource distribution.
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances that must be included in the scaling group. The value must be in the range of [0, 1000]. If the number of pay-as-you-go instances is less than this value, the system gives priority to creating pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that are created after the minimum number of pay-as-you-go instances (\\`on_demand_base_capacity\\`) is met. The value must be in the range of [0, 100].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of the nodes in the node pool. This parameter is required and takes effect only if \\`instance_charge_type\\` is set to \\`PrePaid\\`.
        # 
        # - If \\`period_unit\\` is set to \\`Week\\`, the valid values of \\`period\\` are 1, 2, 3, and 4.
        # 
        # - If \\`period_unit\\` is set to \\`Month\\`, the valid values of \\`period\\` are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of the nodes in the node pool. This parameter is required and takes effect only if \\`instance_charge_type\\` is set to \\`PrePaid\\`.
        # 
        # - `Month`: The billing cycle is measured in months.
        # 
        # - `Week`: The billing cycle is measured in weeks.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # [This parameter is deprecated] Use the \\`image_type\\` parameter instead.
        # 
        # The OS distribution. Valid values:
        # 
        # - `CentOS`
        # 
        # - `AliyunLinux`
        # 
        # - `Windows`
        # 
        # - `WindowsCore`
        # 
        # Default value: `AliyunLinux`.
        self.platform = platform
        # The private pool configurations.
        self.private_pool_options = private_pool_options
        # The name of the worker RAM role.
        # 
        # - If this parameter is left empty, the default worker RAM role of the cluster is used.
        # 
        # - If this parameter is not empty, the specified RAM role must be a **service role**, and its **trusted service** must be **Elastic Compute Service**. For more information, see [Create a service role](https://help.aliyun.com/document_detail/116800.html). If the specified RAM role is not the default worker RAM role of the cluster, the name of the role cannot start with \\`KubernetesMasterRole-\\` or \\`KubernetesWorkerRole-\\`.
        # 
        # >Notice: 
        # 
        # This parameter is supported only by ACK managed clusters of Kubernetes 1.22 or later.
        self.ram_role_name = ram_role_name
        # A list of RDS instances.
        self.rds_instances = rds_instances
        # The resource pool and policy used to create instances. Note:
        # This parameter takes effect only when you create pay-as-you-go instances.
        # This parameter cannot be set at the same time as \\`private_pool_options.match_criteria\\` and \\`private_pool_options.id\\`.
        self.resource_pool_options = resource_pool_options
        # The scaling mode of the scaling group. Valid values:
        # 
        # - `release`: standard mode. The system creates and releases ECS instances to scale the group.
        # 
        # - `recycle`: accelerated mode. The system creates, stops, and starts ECS instances to scale the group. This improves the scaling speed. When an instance is stopped, its computing resources are not billed, but its storage resources are. This does not apply to instances with local disks.
        # 
        # Default value: `release`.
        self.scaling_policy = scaling_policy
        # The ID of the security group for the node pool. You must specify one of \\`security_group_ids\\` and \\`security_group_id\\`. We recommend that you specify \\`security_group_ids\\`.
        self.security_group_id = security_group_id
        # A list of security group IDs. You must specify one of \\`security_group_ids\\` and \\`security_group_id\\`. We recommend that you specify \\`security_group_ids\\`. If you specify both \\`security_group_id\\` and \\`security_group_ids\\`, \\`security_group_ids\\` takes precedence.
        self.security_group_ids = security_group_ids
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enables Alibaba Cloud OS security hardening.
        # 
        # - `false`: Disables Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Specifies whether to enable MLPS 2.0 security hardening. You can enable MLPS 2.0 security hardening for nodes only when you select Alibaba Cloud Linux 2 or Alibaba Cloud Linux 3 for the OS image. Alibaba Cloud provides baseline check standards and scanning programs for Alibaba Cloud Linux 2 and Alibaba Cloud Linux 3 Level 3 of MLPS 2.0 to ensure classified protection compliance.
        self.soc_enabled = soc_enabled
        # The number of instance types that you can specify. The scaling group creates preemptible instances of multiple instance types that are available at the lowest cost. The value must be in the range of [1, 10].
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable the instance reclaim mode. After this mode is enabled, when the system receives a message that a spot instance is about to be reclaimed, the scaling group attempts to create a new instance to replace the instance that is about to be reclaimed. Valid values:
        # 
        # - `true`: Enables the instance reclaim mode.
        # 
        # - `false`: Disables the instance reclaim mode.
        self.spot_instance_remedy = spot_instance_remedy
        # The configurations of the price range for a single spot instance.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the spot instances. Valid values:
        # 
        # - `NoSpot`: The instance is not a spot instance.
        # 
        # - `SpotWithPriceLimit`: Sets the maximum bid price for the spot instance.
        # 
        # - `SpotAsPriceGo`: The system automatically bids based on the current market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/165053.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable the performance burst feature for the system disk of the node. Valid values:
        # 
        # - true: Yes.
        # 
        # - false: No.
        # 
        # This parameter can be set only when \\`system_disk_category\\` is set to \\`cloud_auto\\`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The types of system disks. If a disk of a high-priority type is unavailable, the system automatically uses a disk of the next priority type to create the system disk.
        self.system_disk_categories = system_disk_categories
        # The type of the system disk of the node. Valid values:
        # 
        # - `cloud_efficiency`: ultra disk.
        # 
        # - `cloud_ssd`: standard SSD.
        # 
        # - `cloud_essd`: ESSD.
        # 
        # - `cloud_auto`: ESSD AutoPL disk.
        # 
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # The encryption algorithm that is used to encrypt the system disk. Valid value: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypts the system disk.
        # 
        # - false: does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key that is used to encrypt the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system disk for each node. This parameter applies only to Enhanced SSD (ESSD) disks. The performance level of an ESSD is determined by its size. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        # 
        # - PL0: A moderate maximum concurrent I/O performance and a relatively stable read/write latency.
        # 
        # - PL1: A moderate maximum concurrent I/O performance and a relatively stable read/write latency.
        # 
        # - PL2: A high maximum concurrent I/O performance and a stable read/write latency.
        # 
        # - PL3: A very high maximum concurrent I/O performance and a very stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS of the system disk of the node.
        # 
        # Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter can be set only when \\`system_disk_category\\` is set to \\`cloud_auto\\`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk of the node. Unit: GiB.
        # 
        # The value must be in the range of [20, 2048].
        self.system_disk_size = system_disk_size
        # The snapshot policy for the system disk.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # The tags that you want to add only to ECS instances.
        # 
        # A tag key cannot be repeated. The tag key can be up to 128 characters in length. The tag key and the tag value cannot start with “aliyun” or “acs:”, and cannot contain “https\\://” or “http\\://”.
        self.tags = tags
        # A list of vSwitch IDs. The number of vSwitch IDs must be in the range of [1, 8].
        # 
        # > For high availability, we recommend that you select vSwitches in different zones.
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
        # The name of the tag.
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

class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # The maximum bid price for a single instance.
        # 
        # <props="intl">
        # 
        # Unit: USD/hour.
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
        # A list of private pool IDs. These are the IDs of elastic assurance services or capacity reservation services. You can only specify the IDs of private pools in Target mode. The number of IDs must be in the range of 1 to 20.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy for instance creation. Resource pools include private pools (generated by elastic assurance or capacity reservation services) and public pools. Valid values:
        # PrivatePoolFirst: Prioritizes private pools. If you specify \\`resouce_pool_options.private_pool_ids\\`, the specified private pools are used first. If no private pool is specified or the specified pools have insufficient capacity, the system automatically tries to use open private pools. If no suitable private pool is found, the public pool is used.
        # PrivatePoolOnly: Uses only private pools. You must specify \\`resouce_pool_options.private_pool_ids\\`. If the specified private pools have insufficient capacity, the instance fails to launch.
        # None: No resource pool policy is used.
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
        # The ID of the private pool. You must specify the private pool ID when \\`match_criteria\\` is set to \\`Target\\`.
        self.id = id
        # The type of the private pool. This parameter specifies the capacity of the private pool that you want to use to launch instances. An elastic assurance service or a capacity reservation service takes effect after it is generated. You can select a capacity type when you launch an instance. Valid values:
        # 
        # - `Open`: Open mode. The system automatically matches the capacity of open private pools. If no matching private pool is found, the instance is launched using public pool resources.
        # 
        # - `Target`: Target mode. The instance is launched using the capacity of the specified private pool. If the capacity of the private pool is unavailable, the instance fails to be launched.
        # 
        # - `None`: The instance is launched without using the capacity of a private pool.
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
        # The name of the node pool.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the resource group. Instances that are created in the node pool belong to this resource group.
        # 
        # A resource can belong to only one resource group. You can map resource groups to concepts such as projects, applications, or organizations based on your business scenarios.
        self.resource_group_id = resource_group_id
        # The type of the node pool. Valid values:
        # 
        # - `ess`: a regular node pool. This type of node pool provides managed features and auto scaling.
        # 
        # - `edge`: an edge node pool.
        # 
        # - `lingjun`: a Lingjun node pool.
        # 
        # - `hybrid`: a hybrid cloud node pool.
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

class CreateClusterNodePoolRequestNodeComponents(DaraModel):
    def __init__(
        self,
        config: main_models.CreateClusterNodePoolRequestNodeComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        # The configurations of the node component.
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
        custom_config: Dict[str, str] = None,
    ):
        # The custom configurations of the node component.
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
        # Specifies whether to enable auto node repair. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
        # 
        # - `true`: Enables auto node repair.
        # 
        # - `false`: Disables auto node repair.
        # 
        # Default value: `true`
        self.auto_repair = auto_repair
        # The auto node repair policy.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to enable auto node upgrade. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
        # 
        # - `true`: Enables auto node upgrade.
        # 
        # - `false`: Disables auto node upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # The auto node upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically fix CVE vulnerabilities. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
        # 
        # - `true`: Automatically fixes CVE vulnerabilities.
        # 
        # - `false`: Does not automatically fix CVE vulnerabilities.
        # 
        # Default value: `true`.
        self.auto_vul_fix = auto_vul_fix
        # The policy for automatically fixing CVE vulnerabilities.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the managed node pool feature. Valid values:
        # 
        # - `true`: Enables the managed node pool feature.
        # 
        # - `false`: Disables the managed node pool feature. If you set this parameter to \\`false\\`, the other parameters of \\`management\\` do not take effect.
        # 
        # Default value: false.
        self.enable = enable
        # [This parameter is deprecated] Use the \\`auto_upgrade\\` parameter instead.
        # 
        # The auto upgrade configurations. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
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
        # [This parameter is deprecated] Use the \\`auto_upgrade\\` parameter instead.
        # 
        # Specifies whether to enable auto upgrade. Valid values:
        # 
        # - `true`: enables auto upgrade.
        # 
        # - `false`: disables auto upgrade.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes.
        # The value must be in the range of [1, 1000].
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of extra nodes. You can specify only one of \\`surge\\` and \\`surge_percentage\\`.
        # 
        # Nodes become unavailable during an upgrade. You can create extra nodes to compensate for the load on the cluster.
        # 
        # > We recommend that the number of extra nodes does not exceed the current number of nodes.
        self.surge = surge
        # The percentage of extra nodes. You can specify only one of \\`surge\\` and \\`surge_percentage\\`.
        # 
        # Number of extra nodes = Percentage of extra nodes × Number of nodes. For example, if you set the percentage of extra nodes to 50% and the number of existing nodes is 6, three extra nodes are created.
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
        # The packages that should be excluded from vulnerability fixing.
        # 
        # Default value: `kernel`.
        self.exclude_packages = exclude_packages
        # Specifies whether to allow node restart. This parameter takes effect only if \\`auto_vul_fix\\` is set to \\`true\\`. Valid values:
        # 
        # - `true`: Allows node restart.
        # 
        # - `false`: Disallows node restart.
        # 
        # Default value: `true`
        self.restart_node = restart_node
        # The vulnerability levels that are allowed to be automatically fixed. Separate multiple levels with commas. Example: `asap,later`. Supported vulnerability levels:
        # 
        # - `asap`: high
        # 
        # - `later`: medium
        # 
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
        # Specifies whether to allow auto kubelet upgrade. This parameter takes effect only if \\`auto_upgrade\\` is set to \\`true\\`. Valid values:
        # 
        # - `true`: Allows auto kubelet upgrade.
        # 
        # - `false`: Disallows auto kubelet upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade_kubelet = auto_upgrade_kubelet
        # Specifies whether to allow auto OS upgrade. This parameter takes effect only if \\`auto_upgrade\\` is set to \\`true\\`. Valid values:
        # 
        # - `true`: Allows auto OS upgrade.
        # 
        # - `false`: Disallows auto OS upgrade.
        # 
        # Default value: `false`.
        self.auto_upgrade_os = auto_upgrade_os
        # Specifies whether to allow auto runtime upgrade. This parameter takes effect only if \\`auto_upgrade\\` is set to \\`true\\`. Valid values:
        # 
        # - `true`: Allows auto runtime upgrade.
        # 
        # - `false`: Disallows auto runtime upgrade.
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
        # Specifies whether manual approval is required for node repair.
        self.approval_required = approval_required
        # Specifies whether to allow node restart. This parameter takes effect only if \\`auto_repair\\` is set to \\`true\\`. Valid values:
        # 
        # - `true`: Allows node restart.
        # 
        # - `false`: Disallows node restart.
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
        # Specifies whether to install Cloud Monitor on the ECS nodes. After Cloud Monitor is installed, you can view the monitoring information of the created ECS instances in the Cloud Monitor console. We recommend that you enable this feature. Valid values:
        # 
        # - `true`: Installs Cloud Monitor on the ECS nodes.
        # 
        # - `false`: Does not install Cloud Monitor on the ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy of the node. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # - `static`: Allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # 
        # - `none`: Enables the default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The labels that you want to add to the nodes in the Kubernetes cluster.
        self.labels = labels
        # The custom node name. If you customize the node name, the node name, ECS instance name, and ECS instance hostname are changed.
        # 
        # > For Windows instances for which custom node names are enabled, the hostname is fixed as the IP address. Hyphens (-) are used to replace periods (.) in the IP address. The hostname does not contain a prefix or a suffix.
        # 
        # A node name consists of a prefix, the node IP address, and a suffix.
        # 
        # - The total length must be 2 to 64 characters. The node name must start and end with a lowercase letter or a digit.
        # 
        # - The prefix and suffix can contain uppercase letters, lowercase letters, digits, hyphens (-), and periods (.). They must start with an uppercase or lowercase letter. They cannot start or end with a hyphen (-) or a period (.). You cannot use consecutive hyphens (-)or periods (.). You cannot use consecutive hyphens (-) or periods (.).
        # 
        # - The prefix is required (due to an ECS limit). The suffix is optional.
        # 
        # - The node IP address is the complete private IP address of the node.
        # 
        # For example, if the node IP address is 192.XX.YY.55, the prefix is aliyun.com, and the suffix is test.
        # 
        # - If the node is a Linux node, the node name, ECS instance name, and ECS instance hostname are all aliyun.com192.XX.YY.55test.
        # 
        # - If the node is a Windows node, the ECS instance hostname is 192-XX-YY-55, and the node name and ECS instance name are both aliyun.com192.XX.YY.55test.
        self.node_name_mode = node_name_mode
        # The pre-join instance user data. The specified user data script is run before the node joins the cluster. For more information, see [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The name of the container runtime. ACK supports the following three container runtimes.
        # 
        # - containerd: We recommend that you use this runtime. It is supported by all cluster versions.
        # 
        # - Sandboxed-Container.runv: a sandboxed container that provides higher isolation. It is supported by clusters of Kubernetes 1.31 or earlier.
        # 
        # - docker: no longer maintained. It is supported by clusters of Kubernetes 1.22 or earlier.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The taint configurations.
        self.taints = taints
        # Specifies whether the scaled-out nodes are unschedulable.
        # 
        # - true: The nodes are unschedulable.
        # 
        # - false: The nodes are schedulable.
        self.unschedulable = unschedulable
        # The instance user data. After the node joins the cluster, the specified user data script is run. For more information, see [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
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
        # [This parameter is deprecated]
        # 
        # The network bandwidth of the enhanced edge node pool. Unit: Mbps.
        self.bandwidth = bandwidth
        # [This parameter is deprecated]
        # 
        # The ID of the CCN instance that is associated with the enhanced edge node pool.
        self.ccn_id = ccn_id
        # [This parameter is deprecated]
        # 
        # The region of the CCN instance that is associated with the enhanced edge node pool.
        self.ccn_region_id = ccn_region_id
        # [This parameter is deprecated]
        # 
        # The ID of the CEN instance that is associated with the enhanced edge node pool.
        self.cen_id = cen_id
        # [This parameter is deprecated]
        # 
        # The subscription duration of the enhanced edge node pool. Unit: months.
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
        # The ID of the Lingjun cluster that you want to associate with the Lingjun node pool when you create the node pool.
        self.cluster_id = cluster_id
        # The ID of the Lingjun group in the Lingjun cluster that you want to associate with the Lingjun node pool when you create the node pool.
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
        # [This parameter is deprecated] Use \\`internet_charge_type\\` and \\`internet_max_bandwidth_out\\` instead.
        # 
        # The peak bandwidth of the EIP. Unit: Mbps.
        self.eip_bandwidth = eip_bandwidth
        # [This parameter is deprecated] Use \\`internet_charge_type\\` and \\`internet_max_bandwidth_out\\` instead.
        # 
        # The billing method of the EIP. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # 
        # - `PayByTraffic`: pay-by-traffic.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # 
        # - `true`: Enables auto scaling for the node pool. If the resources planned for the cluster cannot meet the scheduling requirements of pods, Container Service for Kubernetes (ACK) automatically scales out or scales in nodes based on the configured minimum and maximum numbers of instances. For clusters of Kubernetes 1.24 or later, instant scaling is enabled by default. For clusters of a Kubernetes version earlier than 1.24, node autoscaling is enabled by default. For more information, see [Node scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: Disables auto scaling. ACK adjusts the number of nodes in the node pool based on the value of \\`desired_size\\` to maintain a specific number of nodes.
        # 
        # If you set this parameter to false, other parameters in \\`auto_scaling\\` do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # [This parameter is deprecated] This parameter is deprecated. Use \\`internet_charge_type\\` and \\`internet_max_bandwidth_out\\` instead.
        # 
        # Specifies whether to associate an EIP with the node. Valid values:
        # 
        # - `true`: associates an EIP with the node.
        # 
        # - `false`: does not associate an EIP with the node.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances that can be created in the node pool. This does not include existing instances. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
        # 
        # The value must be in the range of [\\`min_instances\\`, 2000]. Default value: 0.
        self.max_instances = max_instances
        # The minimum number of instances that can be created in the node pool. This does not include existing instances. This parameter takes effect only if \\`enable\\` is set to \\`true\\`.
        # 
        # The value must be in the range of [0, \\`max_instances\\`]. Default value: 0.
        # 
        # > - If the minimum number of instances is not 0, the specified number of ECS instances are automatically created after the scaling group is created.
        # >
        # > - We recommend that you set the maximum number of instances to a value that is not smaller than the current number of nodes in the node pool. Otherwise, nodes in the node pool are scaled in after auto scaling is enabled.
        self.min_instances = min_instances
        # The type of instances that are automatically scaled. This parameter takes effect only if \\`enable\\` is set to \\`true\\`. Valid values:
        # 
        # - `cpu`: regular instance.
        # 
        # - `gpu`: GPU-accelerated instance.
        # 
        # - `gpushare`: shared GPU-accelerated instance.
        # 
        # - `spot`: spot instance.
        # 
        # Default value: `cpu`.
        # >Notice: You cannot change the value of this parameter after the node pool is created.
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
        # Specifies whether to enable the intelligent managed mode.
        # Valid values:
        # 
        # - true: Enables the intelligent managed mode. You can enable this mode only when the intelligent managed mode is enabled for the cluster.
        # 
        # - false: Disables the intelligent managed mode.
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

