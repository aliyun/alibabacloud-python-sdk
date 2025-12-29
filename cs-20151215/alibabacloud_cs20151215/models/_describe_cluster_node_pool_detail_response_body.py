# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeClusterNodePoolDetailResponseBody(DaraModel):
    def __init__(
        self,
        auto_mode: main_models.DescribeClusterNodePoolDetailResponseBodyAutoMode = None,
        auto_scaling: main_models.DescribeClusterNodePoolDetailResponseBodyAutoScaling = None,
        host_network: bool = None,
        interconnect_config: main_models.DescribeClusterNodePoolDetailResponseBodyInterconnectConfig = None,
        interconnect_mode: str = None,
        intranet: bool = None,
        kubernetes_config: main_models.DescribeClusterNodePoolDetailResponseBodyKubernetesConfig = None,
        management: main_models.DescribeClusterNodePoolDetailResponseBodyManagement = None,
        max_nodes: int = None,
        node_components: List[main_models.DescribeClusterNodePoolDetailResponseBodyNodeComponents] = None,
        node_config: main_models.DescribeClusterNodePoolDetailResponseBodyNodeConfig = None,
        nodepool_info: main_models.DescribeClusterNodePoolDetailResponseBodyNodepoolInfo = None,
        scaling_group: main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroup = None,
        status: main_models.DescribeClusterNodePoolDetailResponseBodyStatus = None,
        tee_config: main_models.DescribeClusterNodePoolDetailResponseBodyTeeConfig = None,
    ):
        self.auto_mode = auto_mode
        # The auto scaling configuration of the node pool.
        self.auto_scaling = auto_scaling
        # Indicates whether the pods in the edge node pool can use the host network.
        # 
        # `true`: sets to host network.
        # 
        # `false`: sets to container network.
        self.host_network = host_network
        # The network configuration of the edge node pool. This parameter takes effect only for edge node pools.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter takes effect only if you set the type parameter of the node pool to edge. Valid values:
        # 
        # `basic`: Internet.
        # 
        # `private`: private network.
        self.interconnect_mode = interconnect_mode
        # Specifies whether all nodes in the edge node pool can communicate with each other at Layer 3.
        # 
        # `true`: The nodes in the edge node pool can communicate with each other at Layer 3.
        # 
        # `false`: The nodes in the edge node pool cannot communicate with each other at Layer 3.
        self.intranet = intranet
        # The configurations of the cluster in which the node pool is deployed.
        self.kubernetes_config = kubernetes_config
        # The configuration of the managed node pool feature.
        self.management = management
        # This parameter is deprecated.
        # 
        # The maximum number of nodes allowed in an edge node pool.
        self.max_nodes = max_nodes
        self.node_components = node_components
        # The node configurations.
        self.node_config = node_config
        # The configuration of the node pool.
        self.nodepool_info = nodepool_info
        # The configurations of the scaling group that is used by the node pool.
        self.scaling_group = scaling_group
        # The status details about the node pool.
        self.status = status
        # The configuration of confidential computing.
        self.tee_config = tee_config

    def validate(self):
        if self.auto_mode:
            self.auto_mode.validate()
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

        if self.status is not None:
            result['status'] = self.status.to_map()

        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_mode') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyAutoMode()
            self.auto_mode = temp_model.from_map(m.get('auto_mode'))

        if m.get('auto_scaling') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyAutoScaling()
            self.auto_scaling = temp_model.from_map(m.get('auto_scaling'))

        if m.get('host_network') is not None:
            self.host_network = m.get('host_network')

        if m.get('interconnect_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m.get('interconnect_config'))

        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')

        if m.get('intranet') is not None:
            self.intranet = m.get('intranet')

        if m.get('kubernetes_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('kubernetes_config'))

        if m.get('management') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyManagement()
            self.management = temp_model.from_map(m.get('management'))

        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')

        self.node_components = []
        if m.get('node_components') is not None:
            for k1 in m.get('node_components'):
                temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyNodeComponents()
                self.node_components.append(temp_model.from_map(k1))

        if m.get('node_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyNodeConfig()
            self.node_config = temp_model.from_map(m.get('node_config'))

        if m.get('nodepool_info') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('nodepool_info'))

        if m.get('scaling_group') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('scaling_group'))

        if m.get('status') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyStatus()
            self.status = temp_model.from_map(m.get('status'))

        if m.get('tee_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyTeeConfig()
            self.tee_config = temp_model.from_map(m.get('tee_config'))

        return self

class DescribeClusterNodePoolDetailResponseBodyTeeConfig(DaraModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        # Indicates whether confidential computing is enabled. Valid values:
        # 
        # *   `true`: Confidential computing is enabled.
        # *   `false`: Confidential computing is disabled.
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

class DescribeClusterNodePoolDetailResponseBodyStatus(DaraModel):
    def __init__(
        self,
        conditions: List[main_models.DescribeClusterNodePoolDetailResponseBodyStatusConditions] = None,
        failed_nodes: int = None,
        healthy_nodes: int = None,
        initial_nodes: int = None,
        offline_nodes: int = None,
        removing_nodes: int = None,
        serving_nodes: int = None,
        state: str = None,
        total_nodes: int = None,
    ):
        self.conditions = conditions
        # The number of failed nodes.
        self.failed_nodes = failed_nodes
        # The number of healthy nodes.
        self.healthy_nodes = healthy_nodes
        # The number of nodes that are being created.
        self.initial_nodes = initial_nodes
        # The number of offline nodes.
        self.offline_nodes = offline_nodes
        # The number of nodes that are being removed.
        self.removing_nodes = removing_nodes
        # The number of running nodes.
        self.serving_nodes = serving_nodes
        # The status of the node pool. Valid values:
        # 
        # *   `active`: The node pool is active.
        # *   `scaling`: The node pool is being scaled.
        # *   `removing`: Nodes are being removed from the node pool.
        # *   `deleting`: The node pool is being deleted.
        # *   `updating`: The node pool is being updated.
        self.state = state
        # The total number of nodes in the node pool.
        self.total_nodes = total_nodes

    def validate(self):
        if self.conditions:
            for v1 in self.conditions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['conditions'] = []
        if self.conditions is not None:
            for k1 in self.conditions:
                result['conditions'].append(k1.to_map() if k1 else None)

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
        self.conditions = []
        if m.get('conditions') is not None:
            for k1 in m.get('conditions'):
                temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyStatusConditions()
                self.conditions.append(temp_model.from_map(k1))

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

class DescribeClusterNodePoolDetailResponseBodyStatusConditions(DaraModel):
    def __init__(
        self,
        last_transition_time: str = None,
        message: str = None,
        reason: str = None,
        status: str = None,
        type: str = None,
    ):
        self.last_transition_time = last_transition_time
        self.message = message
        self.reason = reason
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_transition_time is not None:
            result['last_transition_time'] = self.last_transition_time

        if self.message is not None:
            result['message'] = self.message

        if self.reason is not None:
            result['reason'] = self.reason

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('last_transition_time') is not None:
            self.last_transition_time = m.get('last_transition_time')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('reason') is not None:
            self.reason = m.get('reason')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class DescribeClusterNodePoolDetailResponseBodyScalingGroup(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        cis_enabled: bool = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[main_models.DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
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
        private_pool_options: main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions = None,
        ram_policy: str = None,
        ram_role_name: str = None,
        rds_instances: List[str] = None,
        resource_pool_options: main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupResourcePoolOptions = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        security_hardening_os: bool = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit] = None,
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
        # Indicates whether auto-renewal is enabled for the nodes in the node pool. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: Auto-renewal is enabled.
        # *   `false`: Auto-renewal is disabled.
        self.auto_renew = auto_renew
        # The duration of the auto-renewal. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # If you specify `PeriodUnit=Month`, the valid values are 1, 2, 3, 6, and 12.
        self.auto_renew_period = auto_renew_period
        # [**Deprecated**] Please use the parameter security_hardening_os instead.
        self.cis_enabled = cis_enabled
        # Indicates whether pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created due to reasons such as cost or insufficient inventory. This parameter takes effect when `multi_az_policy` is set to `COST_OPTIMIZED`. Valid values:
        # 
        # *   `true`: Pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        # *   `false`: Pay-as-you-go instances are not automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configurations of the data disks that are attached to the nodes in the node pool. The configurations include the disk category and disk size.
        self.data_disks = data_disks
        # The ID of the deployment set to which the ECS instances in the node pool belong.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The ID of the custom image. You can call the `DescribeKubernetesVersionMetadata` operation to query the images supported by ACK.
        self.image_id = image_id
        # Operating system image type.
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method.
        # *   `PostPaid`: the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        self.instance_metadata_options = instance_metadata_options
        # The instance properties.
        self.instance_patterns = instance_patterns
        # A list of instance types. You can select multiple instance types. When the system needs to create a node, it starts from the first instance type until the node is created. The instance type that is used to create the node varies based on the actual instance stock.
        self.instance_types = instance_types
        # The billing method of the public IP address of the node.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must set this parameter or the `login_password` parameter. You must set `key_pair` if the node pool is a managed node pool.
        self.key_pair = key_pair
        # Whether the popped ECS instance uses a non-root user for login.
        self.login_as_non_root = login_as_non_root
        # The password for SSH logon. You must set this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # For security purposes, the returned password is encrypted.
        self.login_password = login_password
        # The ECS instance scaling policy for a multi-zone scaling group. Valid values:
        # 
        # *   `PRIORITY`: the scaling group is scaled based on the VSwitchIds.N parameter. If an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, Auto Scaling creates the ECS instance in the zone where the vSwitch that has the next highest priority resides.
        # 
        # *   `COST_OPTIMIZED`: ECS instances are created based on the vCPU unit price in ascending order. Preemptible instances are preferably created when preemptible instance types are specified in the scaling configuration. You can set the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when preemptible instances cannot be created due to insufficient resources.
        # 
        #     **
        # 
        #     **Note**The `COST_OPTIMIZED` setting takes effect only when multiple instance types are specified or at least one instance type is specified for preemptible instances.
        # 
        # *   `BALANCE`: ECS instances are evenly distributed across multiple zones specified by the scaling group. If ECS instances become imbalanced among multiple zones due to insufficient inventory, you can call the RebalanceInstances operation of Auto Scaling to balance the instance distribution among zones. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances that must be kept in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferably creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the number specified by `on_demand_base_capacity`. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of worker nodes. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # If `PeriodUnit=Month` is specified, the valid values are 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of the nodes. This parameter is required if `instance_charge_type` is set to `PrePaid`.
        # 
        # Valid value: `Month`.
        self.period_unit = period_unit
        # The release version of the operating system. Valid values:
        # 
        # *   `CentOS`
        # *   `AliyunLinux`
        # *   `Windows`
        # *   `WindowsCore`
        self.platform = platform
        # The configuration of the private node pool.
        self.private_pool_options = private_pool_options
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage ECS instances.
        self.ram_policy = ram_policy
        # Worker RAM role name.
        self.ram_role_name = ram_role_name
        # After you specify the list of RDS instances, the ECS instances in the cluster are automatically added to the whitelist of the RDS instances.
        self.rds_instances = rds_instances
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The scaling mode of the scaling group. Valid values:
        # 
        # *   `release`: the standard mode. ECS instances are created and released based on resource usage.
        # *   `recycle`: the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances that are attached with local disks.
        self.scaling_policy = scaling_policy
        # The ID of the security group to which the node pool is added. If the node pool is added to multiple security groups, the first ID in the value of `security_group_ids` is returned.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the node pool is added.
        self.security_group_ids = security_group_ids
        # Alibaba Cloud OS security hardening. Values:
        # - `true`: Enable Alibaba Cloud OS security hardening. 
        # - `false`: Do not enable Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Indicates whether to enable security reinforcement compliant with the hardening standards. This option is available only when the system image is set to Alibaba Cloud Linux 2 or Alibaba Cloud Linux 3. Alibaba Cloud provides baseline check standards and scanning programs compliant with Grade 3, Version 2.0 of the hardening standards for both Alibaba Cloud Linux 2 and Alibaba Cloud Linux 3 images.
        self.soc_enabled = soc_enabled
        # The number of instance types that are available for creating preemptible instances. Auto Scaling creates preemptible instances of multiple instance types that are available at the lowest cost. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether preemptible instances are supplemented when the number of preemptible instances drops below the specified minimum number. If this parameter is set to true, when the scaling group receives a system message that a preemptible instance is to be reclaimed, the scaling group attempts to create a new instance to replace this instance. Valid values: Valid values:
        # 
        # *   `true`: Supplementation of preemptible instances is enabled.
        # *   `false`: Supplementation of preemptible instances is disabled.
        self.spot_instance_remedy = spot_instance_remedy
        # The bid configurations of preemptible instances.
        self.spot_price_limit = spot_price_limit
        # The type of preemptible instance. Valid values:
        # 
        # *   NoSpot: a non-preemptible instance.
        # *   SpotWithPriceLimit: a preemptible instance that is configured with the highest bid price.
        # *   SpotAsPriceGo: a preemptible instance for which the system automatically bids based on the current market price.
        # 
        # For more information, see [Preemptible instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Indicates whether to enable the burst feature for the system disk. Valid values:
        # 
        # *   true: enables the burst feature for the system disk. The performance burst feature allows ESSD AutoPL disks to burst their performance when spikes in read/write workloads occur and reduce the performance to the baseline level at the end of workload spikes.
        # *   false: does not enable the burst feature for the system disk.
        # 
        # This parameter is effective only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The categories of the system disk for nodes. The system attempts to create system disks of a disk category with a lower priority if the disk category with a higher priority is unavailable. Valid values: Valid values:
        # 
        # *   `cloud`: basic disk.
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: Enterprise SSD (ESSD).
        # *   `cloud_auto`: ESSD AutoPL disk.
        # *   `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_categories = system_disk_categories
        # The system disk type. Valid values:
        # 
        # *   `cloud`: basic disk
        # *   `cloud_efficiency`: ultra disk
        # *   `cloud_ssd`: standard SSD
        # *   `cloud_essd`: Enterprise SSD (ESSD)
        # *   `cloud_auto`: ESSD AutoPL disk
        # *   `cloud_essd_entry`: ESSD Entry disk
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # The encryption algorithm that is used to encrypt the system disk. Set the value to aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values: Valid values:
        # 
        # *   `true`: encrypts the system disk.
        # *   `false`: does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # System disk\\"s KMS key ID.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for enhanced SSDs (ESSDs).
        self.system_disk_performance_level = system_disk_performance_level
        # Pre-configured read and write IOPS for the system disk of the node, configured when the disk type is cloud_auto.
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of a node. Unit: GiB.
        # 
        # Valid values: 20 to 500.
        self.system_disk_size = system_disk_size
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # The labels that you want to add only to ECS instances.
        # 
        # The label key must be unique and cannot exceed 128 characters in length. The label key and value cannot start with aliyun or acs: or contain https:// or http://.
        self.tags = tags
        # The IDs of vSwitches. You can specify 1 to 20 vSwitches.
        # 
        # > We recommend that you select vSwitches in different zones to ensure high availability.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for v1 in self.data_disks:
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

        self.data_disks = []
        if m.get('data_disks') is not None:
            for k1 in m.get('data_disks'):
                temp_model = main_models.DataDisk()
                self.data_disks.append(temp_model.from_map(k1))

        if m.get('deploymentset_id') is not None:
            self.deploymentset_id = m.get('deploymentset_id')

        if m.get('desired_size') is not None:
            self.desired_size = m.get('desired_size')

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
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('private_pool_options'))

        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')

        if m.get('ram_role_name') is not None:
            self.ram_role_name = m.get('ram_role_name')

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('resource_pool_options') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupResourcePoolOptions()
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
                temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit()
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

class DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of the preemptible instances.
        self.instance_type = instance_type
        # The price cap of a preemptible instance of the type.
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

class DescribeClusterNodePoolDetailResponseBodyScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        self.private_pool_ids = private_pool_ids
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

class DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private node pool.
        self.id = id
        # The type of private node pool. This parameter specifies the type of private node pool that you want to use to create instances. A private node pool is generated when an elasticity assurance or a capacity reservation service takes effect. The system selects a private node pool to launch instances. Valid values:
        # 
        # *   `Open`: open private pool. The system selects an open private node pool to launch instances. If no matching open private node pool is available, the resources in the public node pool are used.
        # *   `Target`: specific private pool. The system uses the resources of the specified private node pool to launch instances. If the specified private node pool is unavailable, instances cannot be launched.
        # *   `None`: no private node pool is used. The resources of private node pools are not used to launch the instances.
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

class DescribeClusterNodePoolDetailResponseBodyNodepoolInfo(DaraModel):
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
        # Indicates whether the node pool is a default node pool. A Container Service for Kubernetes (ACK) cluster usually has only one default node pool. Valid values: `true`: The node pool is a default node pool. `false`: The node pool is not a default node pool.
        self.is_default = is_default
        # The name of the node pool.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-).
        self.name = name
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The type of node pool.
        self.type = type
        # The time when the node pool was last updated.
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

class DescribeClusterNodePoolDetailResponseBodyNodeConfig(DaraModel):
    def __init__(
        self,
        kubelet_configuration: main_models.KubeletConfig = None,
        node_os_config: main_models.DescribeClusterNodePoolDetailResponseBodyNodeConfigNodeOsConfig = None,
    ):
        # The configurations of the kubelet.
        self.kubelet_configuration = kubelet_configuration
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
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyNodeConfigNodeOsConfig()
            self.node_os_config = temp_model.from_map(m.get('node_os_config'))

        return self

class DescribeClusterNodePoolDetailResponseBodyNodeConfigNodeOsConfig(DaraModel):
    def __init__(
        self,
        hugepage: main_models.Hugepage = None,
    ):
        self.hugepage = hugepage

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hugepage') is not None:
            temp_model = main_models.Hugepage()
            self.hugepage = temp_model.from_map(m.get('hugepage'))

        return self

class DescribeClusterNodePoolDetailResponseBodyNodeComponents(DaraModel):
    def __init__(
        self,
        config: main_models.DescribeClusterNodePoolDetailResponseBodyNodeComponentsConfig = None,
        name: str = None,
        version: str = None,
    ):
        self.config = config
        self.name = name
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
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyNodeComponentsConfig()
            self.config = temp_model.from_map(m.get('config'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

class DescribeClusterNodePoolDetailResponseBodyNodeComponentsConfig(DaraModel):
    def __init__(
        self,
        custom_config: Dict[str, str] = None,
    ):
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

class DescribeClusterNodePoolDetailResponseBodyManagement(DaraModel):
    def __init__(
        self,
        auto_repair: bool = None,
        auto_repair_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: main_models.DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig = None,
    ):
        # Indicates whether auto repair is enabled. This parameter takes effect only when `enable=true` is specified. Valid values:
        # 
        # *   `true`: Auto repair is enabled.
        # *   `false`: Auto repair is disabled.
        self.auto_repair = auto_repair
        # Automatic repair node policy.
        self.auto_repair_policy = auto_repair_policy
        # Whether to automatically upgrade.
        self.auto_upgrade = auto_upgrade
        # Automatic upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Whether to automatically fix CVEs.
        self.auto_vul_fix = auto_vul_fix
        # Automatically repair CVE policies.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Indicates whether the managed node pool feature is enabled. Valid values:
        # 
        # *   `true`: The managed node pool feature is enabled.
        # *   `false`: The managed node pool feature is disabled. Other parameters in this section take effect only when `enable=true` is specified.
        self.enable = enable
        # The configuration of auto update. The configuration takes effect only when `enable=true` is specified.
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
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')

        if m.get('auto_repair_policy') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m.get('auto_repair_policy'))

        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('auto_upgrade_policy') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m.get('auto_upgrade_policy'))

        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')

        if m.get('auto_vul_fix_policy') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m.get('auto_vul_fix_policy'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('upgrade_config') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m.get('upgrade_config'))

        return self

class DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # Indicates whether auto update is enabled. Valid values:
        # 
        # *   `true`: Auto update is enabled.
        # *   `false`: Auto update is disabled.
        self.auto_upgrade = auto_upgrade
        # The maximum number of nodes that can be in the Unavailable state. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of additional nodes.
        self.surge = surge
        # The percentage of additional nodes to the nodes in the node pool. You must set this parameter or `surge`.
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

class DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        exclude_packages: str = None,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        self.exclude_packages = exclude_packages
        # Whether to allow restarting nodes.
        self.restart_node = restart_node
        # The vulnerability levels allowed for auto-fixing, separated by commas.
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

class DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # Whether to allow automatic upgrading of kubelet.
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

class DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy(DaraModel):
    def __init__(
        self,
        approval_required: bool = None,
        restart_node: bool = None,
    ):
        self.approval_required = approval_required
        # Whether to allow restarting nodes.
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

class DescribeClusterNodePoolDetailResponseBodyKubernetesConfig(DaraModel):
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
        # Indicates whether the CloudMonitor agent is installed on ECS nodes in the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values:
        # 
        # *   `true`: The CloudMonitor agent is installed on ECS nodes.
        # *   `false`: The CloudMonitor agent is not installed on ECS nodes.
        self.cms_enabled = cms_enabled
        # The CPU management policy of the nodes in the node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: indicates that the default CPU affinity is used.
        self.cpu_policy = cpu_policy
        # The labels that you want to add to the nodes in the cluster. You must add labels based on the following rules:
        # 
        # *   A label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   The key must be unique and cannot exceed 64 characters in length. The value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # A custom node name consists of a prefix, an IP substring, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter.
        # *   The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The user-defined script that is executed before nodes are initialized. For more information, see [Generate user-defined data](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The name of the container runtime.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The taints that you want to add to nodes. Taints can be used together with tolerations to prevent pods from being scheduled to specific nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # Whether the expanded node is schedulable.
        self.unschedulable = unschedulable
        # The custom script to be executed after nodes in the node pool are initialized. For more information, see [Generate user-defined data](https://help.aliyun.com/document_detail/49121.html).
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

class DescribeClusterNodePoolDetailResponseBodyInterconnectConfig(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        # The bandwidth of the enhanced edge node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The ID of the Cloud Connect Network (CCN) instance that is associated with the enhanced edge node pool.
        self.ccn_id = ccn_id
        # The region to which the CCN instance that is associated with the enhanced edge node pool belongs.
        self.ccn_region_id = ccn_region_id
        # The ID of the Cloud Enterprise Network (CEN) instance that is associated with the enhanced edge node pool.
        self.cen_id = cen_id
        # The subscription duration of the enhanced edge node pool. The duration is measured in months.
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

class DescribeClusterNodePoolDetailResponseBodyAutoScaling(DaraModel):
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
        # The maximum bandwidth of the elastic IP address (EIP).
        self.eip_bandwidth = eip_bandwidth
        # The metering method of the EIP. Valid values:
        # 
        # *   `PayByBandwidth`: pay-by-bandwidth.
        # *   `PayByTraffic`: pay-by-data-transfer.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Indicates whether auto scaling is enabled. Valid values:
        # 
        # *   `true`: auto scaling is enabled.
        # *   `false`: auto scaling is disabled. If this parameter is set to false, other parameters in the `auto_scaling` section do not take effect.
        self.enable = enable
        # Indicates whether an EIP is associated with the node pool. Valid values:
        # 
        # *   `true`: An EIP is associated with the node pool.
        # *   `false`: No EIP is associated with the node pool.
        self.is_bond_eip = is_bond_eip
        # The maximum number of Elastic Compute Service (ECS) instances that can be created in the node pool.
        self.max_instances = max_instances
        # The minimum number of ECS instances that must be kept in the node pool.
        self.min_instances = min_instances
        # The instance types that can be used for the auto scaling of the node pool. Valid values:
        # 
        # *   `cpu`: regular instance.
        # *   `gpu`: GPU-accelerated instance.
        # *   `gpushare`: shared GPU-accelerated instance.
        # *   `spot`: preemptible instance.
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

class DescribeClusterNodePoolDetailResponseBodyAutoMode(DaraModel):
    def __init__(
        self,
        enable: bool = None,
    ):
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

