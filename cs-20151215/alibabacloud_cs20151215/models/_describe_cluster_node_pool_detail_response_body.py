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
        eflo_node_group: main_models.DescribeClusterNodePoolDetailResponseBodyEfloNodeGroup = None,
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
        # The smart hosting configurations.
        self.auto_mode = auto_mode
        # The configurations of the node pool that is configured for automatic scaling.
        self.auto_scaling = auto_scaling
        self.eflo_node_group = eflo_node_group
        # Indicates whether the pod network uses the host network mode.
        # 
        # - `true`: host network. Pods directly use the host\\"s network stack and share IP addresses and ports with the host.
        # 
        # - `false`: container network. Pods have an independent network stack and do not use host network ports.
        self.host_network = host_network
        # [This parameter is deprecated]
        # 
        # The network configurations of the edge node pool. This parameter is valid only for edge node pools.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter is valid only for `edge` node pools. Valid values:
        # 
        # - `basic`: public network. The nodes in the node pool interact with cloud nodes over the Internet. Applications in the node pool cannot directly access the VPC in the cloud.
        # 
        # - `private`: dedicated network. The nodes in the node pool connect to the cloud network through leased lines, VPNs, or CEN. This provides higher communication quality between the cloud and the edge and offers more effective security.
        self.interconnect_mode = interconnect_mode
        # Indicates whether nodes in the edge node pool have Layer 3 network connectivity.
        # 
        # - `true`: connected. All nodes in this node pool have Layer 3 network connectivity.
        # 
        # - `false`: not connected. All hosts in this node pool do not have Layer 3 network connectivity.
        self.intranet = intranet
        # The cluster-related configurations.
        self.kubernetes_config = kubernetes_config
        # The configurations of the managed node pool.
        self.management = management
        # [This parameter is deprecated]
        # 
        # The maximum number of nodes that the edge node pool can contain.
        self.max_nodes = max_nodes
        # The list of node components.
        self.node_components = node_components
        # The node configurations.
        self.node_config = node_config
        # The node pool configurations.
        self.nodepool_info = nodepool_info
        # The configurations of the scaling group for the node pool.
        self.scaling_group = scaling_group
        # The status of the node pool.
        self.status = status
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

        if m.get('eflo_node_group') is not None:
            temp_model = main_models.DescribeClusterNodePoolDetailResponseBodyEfloNodeGroup()
            self.eflo_node_group = temp_model.from_map(m.get('eflo_node_group'))

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
        # Indicates whether to enable the confidential computing cluster. Valid values:
        # 
        # - `true`: Enables the confidential computing cluster.
        # 
        # - `false`: Disables the confidential computing cluster.
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
        # The current status of the node pool. This parameter indicates the status of the node pool from different dimensions.
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
        # The number of nodes that are in service.
        self.serving_nodes = serving_nodes
        # The state of the node pool. Valid values:
        # 
        # - `active`: The node pool is active.
        # 
        # - `scaling`: The node pool is being scaled.
        # 
        # - `removing`: Nodes are being removed.
        # 
        # - `deleting`: The node pool is being deleted.
        # 
        # - `updating`: The node pool is being updated.
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
        # The time of the last status transition.
        self.last_transition_time = last_transition_time
        # The detailed information.
        self.message = message
        # The reason.
        self.reason = reason
        # The status.
        self.status = status
        # The type.
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
        # Indicates whether to enable auto-renewal for the nodes. This parameter takes effect only if instance_charge_type is set to PrePaid. Valid values:
        # 
        # - `true`: Auto-renewal is enabled.
        # 
        # - `false`: Auto-renewal is disabled.
        self.auto_renew = auto_renew
        # The duration of each auto-renewal. Valid values:
        # 
        # - If PeriodUnit is set to Week: 1, 2, and 3.
        # 
        # - If PeriodUnit is set to Month: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        self.auto_renew_period = auto_renew_period
        # [This parameter is deprecated] Use the security_hardening_os parameter instead.
        self.cis_enabled = cis_enabled
        # If multi_az_policy is set to COST_OPTIMIZED, this parameter specifies whether to allow the system to automatically create on-demand instances to meet the required number of ECS instances when it is not possible to create a sufficient number of spot instances due to price or stock issues. Valid values:
        # 
        # - `true`: Allows the system to automatically create on-demand instances to meet the required number of ECS instances.
        # 
        # - `false`: Does not allow the system to automatically create on-demand instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The combination of the configurations, such as the type and size, of the data disks of the nodes.
        self.data_disks = data_disks
        # The deployment set ID.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The configurations for block device initialization.
        self.disk_init = disk_init
        # The custom image ID.
        self.image_id = image_id
        # The OS image type.
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
        # - `ContainerOS`: Container-optimized image.
        # 
        # - `AliyunLinux3ContainerOptimized`: Alinux3 container-optimized image.
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # - `PrePaid`: subscription.
        # 
        # - `PostPaid`: pay-as-you-go.
        self.instance_charge_type = instance_charge_type
        # The configurations for accessing the metadata of ECS instances.
        self.instance_metadata_options = instance_metadata_options
        # The instance attribute configurations.
        self.instance_patterns = instance_patterns
        # The list of node instance types.
        self.instance_types = instance_types
        # The billing method for the public IP address of the nodes.
        # 
        # - PayByBandwidth: pay-by-bandwidth.
        # 
        # - PayByTraffic: pay-by-traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound public bandwidth of the nodes. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must specify either this parameter or login_password. When the node pool is a managed node pool, only key_pair is supported.
        self.key_pair = key_pair
        # Indicates whether to log on to the created ECS instances as a non-root user.
        # 
        # - true: Logs on as a non-root user (ecs-user).
        # 
        # - false: Logs on as the root user.
        self.login_as_non_root = login_as_non_root
        # The SSH logon password. You must specify either this parameter or key_pair. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        # 
        # For security reasons, the password is encrypted in the query result.
        self.login_password = login_password
        # The scaling policy for the ECS instances in the multi-zone scaling group. Valid values:
        # 
        # - `PRIORITY`: Scales instances based on the vSwitches that you define (VSwitchIds.N). If the ECS instances cannot be created in the zone of the vSwitch with a higher priority, the system automatically uses the vSwitch with the next priority to create the instances.
        # 
        # - `COST_OPTIMIZED`: Attempts to create instances at the lowest vCPU unit price. If multiple instance types are specified for the scaling configuration and the preemption policy is configured, the system preferentially creates the corresponding spot instances. You can also use the `CompensateWithOnDemand` parameter to specify whether to automatically try to create on-demand instances when spot instances cannot be created due to reasons such as stock shortages.
        # 
        #   > `COST_OPTIMIZED` takes effect only when multiple instance types are specified or spot instances are used for the scaling configuration.
        # 
        # - `BALANCE`: Evenly distributes ECS instances across the specified zones of the scaling group. If the distribution of ECS instances becomes unbalanced between zones due to stock shortages, you can call the API RebalanceInstances operation to balance the resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html) .
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of on-demand instances that the scaling group must contain. Valid values: 0 to 1000. If the number of on-demand instances is less than this value, on-demand instances are preferentially created.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of on-demand instances among the instances that exceed the minimum number of on-demand instances (on_demand_base_capacity). Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of the nodes. This parameter is required and takes effect only if instance_charge_type is set to PrePaid.
        # 
        # - If period_unit is set to Week, the valid values of period are 1, 2, 3, and 4.
        # 
        # - If period_unit is set to Month, the valid values of period are 1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of the nodes. This parameter is required if instance_charge_type is set to PrePaid.
        # 
        # - `Month`: The billing cycle is measured in months.
        # 
        # - `Week`: The billing cycle is measured in weeks.
        self.period_unit = period_unit
        # The OS distribution. Valid values:
        # 
        # - `CentOS`
        # 
        # - `AliyunLinux`
        # 
        # - `Windows`
        # 
        # - `WindowsCore`
        self.platform = platform
        # The private node pool configurations.
        self.private_pool_options = private_pool_options
        # [This parameter is deprecated] Use ram_role_name instead.
        self.ram_policy = ram_policy
        # The name of the worker RAM role.
        self.ram_role_name = ram_role_name
        # If you specify a list of RDS instances, the ECS nodes of the cluster are automatically added to the RDS instance whitelist.
        self.rds_instances = rds_instances
        # The resource pool and resource pool policy used when creating instances.
        self.resource_pool_options = resource_pool_options
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The scaling group mode. Valid values:
        # 
        # - `release`: standard mode. Instances are created and released based on the resource usage.
        # 
        # - `recycle`: fast mode. Instances are created, stopped, and started to accelerate scaling. Compute resources are not billed when instances are stopped, but storage resources are. This does not apply to instances with local disks.
        self.scaling_policy = scaling_policy
        # The security group ID of the node pool. If the node pool is associated with multiple security groups, this is the first value in security_group_ids.
        self.security_group_id = security_group_id
        # The list of security group IDs for the node pool.
        self.security_group_ids = security_group_ids
        # Alibaba Cloud OS security hardening. Valid values:
        # 
        # - `true`: Enables Alibaba Cloud OS security hardening.
        # 
        # - `false`: Disables Alibaba Cloud OS security hardening.
        # 
        # Default value: `false`.
        self.security_hardening_os = security_hardening_os
        # Indicates whether to enable classified protection compliance. You can enable classified protection compliance for nodes only when you select Alibaba Cloud Linux 2 or Alibaba Cloud Linux 3 as the OS image. Alibaba Cloud provides baseline check standards and scanning programs for MLPS 2.0 Level 3-compliant Alibaba Cloud Linux 2 and Alibaba Cloud Linux 3 images.
        self.soc_enabled = soc_enabled
        # The number of available instance types. The scaling group creates spot instances of multiple types that have the lowest costs in a balanced manner. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether to enable the feature of supplementing spot instances. If this feature is enabled, the scaling group attempts to create a new instance to replace a spot instance that is reclaimed. Valid values:
        # 
        # - `true`: Enables the feature of supplementing spot instances.
        # 
        # - `false`: Disables the feature of supplementing spot instances.
        self.spot_instance_remedy = spot_instance_remedy
        # The configurations of the price range for spot instances.
        self.spot_price_limit = spot_price_limit
        # The preemption policy for the spot instances. Valid values:
        # 
        # - NoSpot: The instances are not spot instances.
        # 
        # - SpotWithPriceLimit: Sets the maximum price for a spot instance.
        # 
        # - SpotAsPriceGo: The system automatically places bids based on the market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Indicates whether to enable performance burst for the system disk of the nodes. Valid values:
        # 
        # - true: Enables performance burst. If you enable this feature, the cloud disk can temporarily improve its performance to handle sudden data read and write pressure when the business is unstable.
        # 
        # - false: Disables performance burst.
        # 
        # This parameter can be set only when system_disk_category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The types of system disks. When a disk of a high-priority type is not available, the system automatically tries the next-priority disk type to create the system disk.
        self.system_disk_categories = system_disk_categories
        # The type of the system disk of the nodes. Valid values:
        # 
        # - `cloud_efficiency`: ultra disk.
        # 
        # - `cloud_ssd`: standard SSD.
        # 
        # - `cloud_essd`: Enhanced SSD (ESSD).
        # 
        # - `cloud_auto`: ESSD AutoPL disk.
        # 
        # - `cloud_essd_entry`: ESSD Entry disk.
        self.system_disk_category = system_disk_category
        # The encryption algorithm that is used for the system disk. Valid value: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Indicates whether to encrypt the system disk. Valid values:
        # 
        # - `true`: Encrypts the system disk.
        # 
        # - `false`: Does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key that is used to encrypt the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system disk of the nodes. This parameter is valid only for ESSDs. The disk performance level is related to the disk size. For more information, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # - PL0: The I/O performance is moderate and the read/write latency is stable.
        # 
        # - PL1: The I/O performance is moderate and the read/write latency is stable.
        # 
        # - PL2: The I/O performance is high and the read/write latency is stable.
        # 
        # - PL3: The I/O performance is very high and the read/write latency is very stable.
        self.system_disk_performance_level = system_disk_performance_level
        # The pre-configured read and write IOPS of the system disk of the nodes.
        # 
        # Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter can be set only when system_disk_category is set to cloud_auto. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk of the nodes. Unit: GiB.
        # 
        # Valid values: 20 to 2048.
        self.system_disk_size = system_disk_size
        # The system disk snapshot policy
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # The ECS instance tags.
        self.tags = tags
        # The list of vSwitch IDs.
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
        # The spot instance type.
        self.instance_type = instance_type
        # The price of a single instance.
        # 
        # <props="china">
        # 
        # Unit: CNY/hour.
        # 
        # 
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

class DescribeClusterNodePoolDetailResponseBodyScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # The list of private pool IDs.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy used when creating instances. Valid values: PrivatePoolFirst: The private pool is used first. PrivatePoolOnly: Only the private pool is used. None: No resource pool policy is used.
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
        # The private node pool ID.
        self.id = id
        # The type of the private node pool. This parameter specifies the capacity option for the private pool that is used to start instances. After an elastic assurance service or a capacity reservation service takes effect, a private pool is generated. You can select the private pool to start instances. Valid values:
        # 
        # - `Open`: The system automatically matches the capacity of an open private pool. If no matching private pool is found, the system uses public resources.
        # 
        # - `Target`: The system uses the capacity of a specified private pool to start the instance. If the capacity of the specified private pool is unavailable, the instance fails to start.
        # 
        # - `None`: The system does not use the capacity of a private pool.
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
        # Indicates whether the node pool is the default node pool. A cluster usually has only one default node pool. Valid values:
        # 
        # - `true`: the default node pool.
        # 
        # - `false`: not the default node pool.
        self.is_default = is_default
        # The name of the node pool.
        self.name = name
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The region ID.
        self.region_id = region_id
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The type of the node pool.
        # 
        # - `ess`: a regular node pool. It includes the features of managed node pools and automatic scaling.
        # 
        # - `edge`: an edge node pool.
        # 
        # - `lingjun`: a Lingjun node pool.
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
        # The Kubelet parameter settings.
        self.kubelet_configuration = kubelet_configuration
        # The node OS configurations.
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
        # The Hugepage configurations.
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

class DescribeClusterNodePoolDetailResponseBodyManagement(DaraModel):
    def __init__(
        self,
        auto_fault_diagnosis: bool = None,
        auto_repair: bool = None,
        auto_repair_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: main_models.DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig = None,
    ):
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Indicates whether to enable auto repair. This parameter takes effect only if enable is set to true.
        # 
        # - `true`: Auto repair is enabled.
        # 
        # - `false`: Auto repair is disabled.
        self.auto_repair = auto_repair
        # The policy for automatic node repair.
        self.auto_repair_policy = auto_repair_policy
        # Indicates whether to enable automatic node upgrades. This parameter takes effect only if enable is set to true.
        # 
        # - `true`: Automatic upgrades are enabled.
        # 
        # - `false`: Automatic upgrades are disabled.
        self.auto_upgrade = auto_upgrade
        # The policy for automatic upgrades.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Indicates whether to automatically fix CVEs. This parameter takes effect only if enable is set to true.
        # 
        # - `true`: CVEs are automatically fixed.
        # 
        # - `false`: CVEs are not automatically fixed.
        self.auto_vul_fix = auto_vul_fix
        # The policy for automatically fixing CVEs.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Indicates whether to enable the managed node pool feature. Valid values:
        # 
        # - `true`: Enables the managed node pool feature.
        # 
        # - `false`: Disables the managed node pool feature. Other parameters in this section take effect only if this parameter is set to true.
        self.enable = enable
        # The automatic upgrade configurations. This parameter takes effect only if enable is set to true.
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
        # Indicates whether to enable automatic upgrades. Valid values:
        # 
        # - `true`: Automatic upgrades are enabled.
        # 
        # - `false`: Automatic upgrades are disabled.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of extra nodes. You can specify only one of surge and surge_percentage.
        self.surge = surge
        # The percentage of extra nodes. You can specify only one of surge and surge_percentage.
        # 
        # The number of extra nodes = Percentage of extra nodes × Number of nodes. For example, if you set the percentage of extra nodes to 50% and the number of existing nodes is 6, the number of extra nodes is 3 (50% × 6).
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
        # The packages that should be excluded during CVE fixing.
        self.exclude_packages = exclude_packages
        # Indicates whether to allow node restart. This parameter takes effect only if auto_vul_fix is set to true. Valid values:
        # 
        # - `true`: Nodes can be restarted.
        # 
        # - `false`: Nodes cannot be restarted.
        self.restart_node = restart_node
        # The levels of CVEs that are allowed to be automatically fixed. The levels are separated by commas.
        # 
        # - `asap`: high
        # 
        # - `later`: medium
        # 
        # - `nntf`: low
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
        # Indicates whether to allow automatic kubelet upgrades. This parameter takes effect only if auto_upgrade is set to true. Valid values:
        # 
        # - `true`: Automatic kubelet upgrades are allowed.
        # 
        # - `false`: Automatic kubelet upgrades are not allowed.
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
        auto_repair_policy_id: str = None,
        restart_node: bool = None,
    ):
        # Indicates whether manual approval is required for node repair.
        self.approval_required = approval_required
        # The ID of the auto repair policy
        self.auto_repair_policy_id = auto_repair_policy_id
        # Indicates whether to allow node restart. This parameter takes effect only if auto_repair is set to true.
        # 
        # - `true`: Nodes can be restarted.
        # 
        # - `false`: Nodes cannot be restarted.
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

        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('approval_required') is not None:
            self.approval_required = m.get('approval_required')

        if m.get('auto_repair_policy_id') is not None:
            self.auto_repair_policy_id = m.get('auto_repair_policy_id')

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
        # Indicates whether to install Cloud Monitor on the ECS nodes. After you install Cloud Monitor, you can view the monitoring information of the created ECS instances in the Cloud Monitor console. We recommend that you enable this feature. Valid values:
        # 
        # - `true`: Installs Cloud Monitor on the ECS nodes.
        # 
        # - `false`: Does not install Cloud Monitor on the ECS nodes.
        self.cms_enabled = cms_enabled
        # The CPU management policy for the nodes. The following policies are supported for clusters of Kubernetes 1.12.6 and later:
        # 
        # - `static`: Allows pods with specific resource characteristics on a node to have enhanced CPU affinity and exclusivity.
        # 
        # - `none`: Enables the default CPU affinity scheme.
        self.cpu_policy = cpu_policy
        # The node labels.
        self.labels = labels
        # The custom node name.
        # 
        # A node name consists of a prefix, the IP address of the node, and a suffix:
        # 
        # - The prefix and suffix can consist of one or more parts separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or a digit.
        # 
        # - The IP address segment length indicates the number of digits to be truncated from the end of the node IP address. Valid values: 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the IP address segment length is 5, and the suffix is test, the node name is aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The pre-custom data of the node pool. The script is run before the node is initialized. For more information, see [Generate instance user data](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The name of the container runtime. ACK supports the following container runtimes.
        # 
        # - containerd: recommended. It is supported by all cluster versions.
        # 
        # - Sandboxed-Container.runv: a sandboxed container that provides higher isolation. It is supported by clusters of Kubernetes 1.31 and earlier.
        # 
        # - docker: no longer maintained. It is supported by clusters of Kubernetes 1.22 and earlier.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The node taints. Taints work with tolerations to prevent pods from being scheduled to unsuitable nodes. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # Indicates whether the scaled-out nodes are unschedulable.
        # 
        # - true: The nodes are unschedulable.
        # 
        # - false: The nodes are schedulable.
        self.unschedulable = unschedulable
        # The custom data of the node pool. The script is run after the node is initialized. For more information, see [Generate instance user data](https://help.aliyun.com/document_detail/49121.html).
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
        # [This parameter is deprecated]
        # 
        # The network bandwidth of the enhanced edge node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # [This parameter is deprecated]
        # 
        # The ID of the CCN instance that is associated with the enhanced edge node pool.
        self.ccn_id = ccn_id
        # [This parameter is deprecated]
        # 
        # The region where the CCN instance that is associated with the enhanced edge node pool resides.
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

class DescribeClusterNodePoolDetailResponseBodyEfloNodeGroup(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        group_id: str = None,
    ):
        self.cluster_id = cluster_id
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
        # The peak EIP bandwidth.
        # 
        # Valid values: 1 to 100. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # The billing method of the EIP. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # 
        # - `PayByTraffic`: pay-by-traffic.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Indicates whether to enable automatic scaling. Valid values:
        # 
        # - `true`: enables automatic scaling for the node pool. If the resources of the cluster cannot meet the scheduling requirements of pods, ACK automatically scales out or in nodes based on the configured minimum and maximum numbers of instances. For clusters of Kubernetes 1.24 or later, node elastic scaling is enabled by default. For clusters of a Kubernetes version earlier than 1.24, node autoscaling is enabled by default. For more information, see [Node scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: disables automatic scaling. ACK adjusts the number of nodes in the node pool to the expected number of nodes. The number of nodes is always the same as the expected number of nodes.
        # 
        # If this parameter is set to false, other parameters in auto_scaling do not take effect.
        self.enable = enable
        # Indicates whether to associate an EIP with the node pool. Valid values:
        # 
        # - `true`: Associates an EIP with the node pool.
        # 
        # - `false`: Does not associate an EIP with the node pool.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances that can be created in the node pool. This value does not include the existing instances.
        self.max_instances = max_instances
        # The minimum number of instances that can be created in the node pool. This value does not include the existing instances.
        self.min_instances = min_instances
        # The type of automatic scaling that is configured for the node pool. This parameter is specified based on the instance type for automatic scaling. Valid values:
        # 
        # - `cpu`: regular instances.
        # 
        # - `gpu`: GPU-accelerated instances.
        # 
        # - `gpushare`: shared GPU-accelerated instances.
        # 
        # - `spot`: spot instances.
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
        # Indicates whether to enable the feature.
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

