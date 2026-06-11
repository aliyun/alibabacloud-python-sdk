# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class ModifyClusterNodePoolRequest(DaraModel):
    def __init__(
        self,
        auto_scaling: main_models.ModifyClusterNodePoolRequestAutoScaling = None,
        concurrency: bool = None,
        kubernetes_config: main_models.ModifyClusterNodePoolRequestKubernetesConfig = None,
        management: main_models.ModifyClusterNodePoolRequestManagement = None,
        nodepool_info: main_models.ModifyClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: main_models.ModifyClusterNodePoolRequestScalingGroup = None,
        tee_config: main_models.ModifyClusterNodePoolRequestTeeConfig = None,
        update_nodes: bool = None,
    ):
        # The auto scaling configurations.
        self.auto_scaling = auto_scaling
        # Specifies whether to run the task in parallel.
        self.concurrency = concurrency
        # The Kubernetes-related configurations.
        self.kubernetes_config = kubernetes_config
        # The configurations of the managed node pool.
        self.management = management
        # The node pool configurations.
        self.nodepool_info = nodepool_info
        # The configurations of the node pool scaling group.
        self.scaling_group = scaling_group
        # The configurations of the Kubernetes cluster for confidential computing.
        self.tee_config = tee_config
        # Synchronously updates node labels and taints.
        self.update_nodes = update_nodes

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.management:
            self.management.validate()
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

        if self.concurrency is not None:
            result['concurrency'] = self.concurrency

        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()

        if self.management is not None:
            result['management'] = self.management.to_map()

        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()

        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()

        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()

        if self.update_nodes is not None:
            result['update_nodes'] = self.update_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_scaling') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m.get('auto_scaling'))

        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')

        if m.get('kubernetes_config') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m.get('kubernetes_config'))

        if m.get('management') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m.get('management'))

        if m.get('nodepool_info') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m.get('nodepool_info'))

        if m.get('scaling_group') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m.get('scaling_group'))

        if m.get('tee_config') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m.get('tee_config'))

        if m.get('update_nodes') is not None:
            self.update_nodes = m.get('update_nodes')

        return self

class ModifyClusterNodePoolRequestTeeConfig(DaraModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        # Specifies whether to enable the confidential computing cluster. Valid values:
        # 
        # - `true`: enables the cluster.
        # 
        # - `false`: disables the cluster.
        # 
        # Default value: `false`.
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

class ModifyClusterNodePoolRequestScalingGroup(DaraModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[main_models.DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        disk_init: List[main_models.DiskInit] = None,
        image_id: str = None,
        image_type: str = None,
        instance_charge_type: str = None,
        instance_patterns: List[main_models.InstancePatterns] = None,
        instance_types: List[str] = None,
        internet_charge_type: str = None,
        internet_max_bandwidth_out: int = None,
        key_pair: str = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: main_models.ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions = None,
        rds_instances: List[str] = None,
        resource_pool_options: main_models.ModifyClusterNodePoolRequestScalingGroupResourcePoolOptions = None,
        scaling_policy: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[main_models.ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
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
        # Specifies whether to enable auto-renewal for the nodes. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Auto-renewal is enabled.
        # 
        # - `false`: Auto-renewal is disabled.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # The auto-renewal period. Valid values:
        # 
        # - If PeriodUnit=Week, valid values are 1, 2, and 3.
        # 
        # - If PeriodUnit=Month, valid values are 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # If `multi_az_policy` is set to `COST_OPTIMIZED`, this parameter specifies whether to allow the system to automatically create pay-as-you-go instances to meet the required number of ECS instances when spot instances cannot be created due to reasons such as price and stock. Valid values:
        # 
        # - `true`: allows the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        # 
        # - `false`: does not allow the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The data disk configurations of the node. You can specify 0 to 10 data disks.
        self.data_disks = data_disks
        # The ID of the deployment set to which the ECS instances in the node pool belong. This parameter is valid only for incremental nodes. The deployment sets of existing nodes are not changed.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        # 
        # The total number of nodes that the node pool should maintain. We recommend that you configure at least two nodes to ensure that the cluster components run as expected. You can adjust the expected number of nodes to scale in or scale out the node pool.
        # 
        # If you do not need to create nodes, set this parameter to 0. You can manually adjust the number of nodes later.
        self.desired_size = desired_size
        # The block device initialization configuration.
        self.disk_init = disk_init
        # The ID of the custom image. You can call `DescribeKubernetesVersionMetadata` to query the images that are supported by the system. By default, the latest image is used.
        self.image_id = image_id
        # The distribution of the operating system. We recommend that you use this parameter to specify the operating system of the nodes. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # 
        # - `AliyunLinuxSecurity`: Alinux2 image with UEFI.
        # 
        # - `AliyunLinux3`: Alinux3 image.
        # 
        # - `AliyunLinux3Arm64`: Alinux3 image for ARM.
        # 
        # - `AliyunLinux3Security`: Alinux3 image with UEFI.
        # 
        # - `CentOS`: CentOS image.
        # 
        # - `Windows`: Windows image.
        # 
        # - `WindowsCore`: WindowsCore image.
        # 
        # - `ContainerOS`: container-optimized image.
        # 
        # - `AliyunLinux3ContainerOptimized`: container-optimized Alinux3 image.
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # - `PrePaid`: subscription
        # 
        # - `PostPaid`: pay-as-you-go
        # 
        # Default value: `PostPaid`.
        self.instance_charge_type = instance_charge_type
        # The instance attribute configurations.
        self.instance_patterns = instance_patterns
        # A list of node instance types. You can specify multiple instance types as alternatives. When a node is created, the system attempts to purchase the instance types in the order they are specified until one is successfully purchased. The final instance type that is purchased may vary depending on the stock.
        # 
        # You can specify 1 to 10 instance types.
        self.instance_types = instance_types
        # The billing method of the public IP address. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # 
        # - `PayByTraffic`: pay-by-traffic.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: [1, 100].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must specify key_pair or `login_password`. For managed node pools, you can specify only `key_pair`.
        self.key_pair = key_pair
        # The SSH logon password. You must specify key_pair or `login_password`. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The scaling policy for ECS instances in a multi-zone scaling group. Valid values:
        # 
        # - `PRIORITY`: The system scales ECS instances based on the vSwitch priority. The vSwitch priority is specified by the VSwitchIds.N parameter. If the system fails to create an ECS instance in the zone where the vSwitch with the highest priority resides, it attempts to create the ECS instance in the zone where the vSwitch with the next highest priority resides.
        # 
        # - `COST_OPTIMIZED`: The system creates ECS instances of the instance type that has the lowest vCPU price. When the scaling configuration is set to create multiple instance types and the billing method is set to preemptible, the system preferentially creates preemptible instances. You can also use the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when the system fails to create preemptible instances due to insufficient stock.
        # 
        #   > The `COST_OPTIMIZED` policy is valid only when multiple instance types are specified or preemptible instances are selected in the scaling configuration.
        # 
        # - `BALANCE`: The system evenly distributes ECS instances across the zones that are specified in the scaling group. If the distribution of ECS instances becomes unbalanced due to insufficient stock, you can call the `RebalanceInstances` operation to rebalance the distribution. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html) .
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of on-demand instances that must be contained in the scaling group. Valid values: [0, 1000]. When the number of on-demand instances is less than this value, on-demand instances are preferentially created.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of on-demand instances among the instances that exceed the minimum number of on-demand instances (`on_demand_base_capacity`). Valid values: [0, 100].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of the nodes in the node pool. This parameter is required and takes effect only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - If `period_unit=Week`, valid values of `period` are {1, 2, 3, 4}.
        # 
        # - If `period_unit=Month`, valid values of `period` are {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 60}.
        self.period = period
        # The billing cycle of the nodes in the node pool. This parameter is required and takes effect only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - `Month`: billed by month.
        # 
        # - `Week`: billed by week.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # This parameter is deprecated. Use the `image_type` parameter instead.
        # 
        # The OS platform. Valid values:
        # 
        # - `AliyunLinux`
        # 
        # - `CentOS`
        # 
        # - `Windows`
        # 
        # - `WindowsCore`
        self.platform = platform
        # The private node pool configurations.
        self.private_pool_options = private_pool_options
        # A list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The resource pool and resource pool policy that are used when you create an instance. If you specify this parameter, note the following points:
        # This parameter is valid only when you create pay-as-you-go instances.
        # This parameter cannot be specified at the same time as private_pool_options.match_criteria and private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # The scaling mode of the scaling group. Valid values:
        # 
        # - `release`: standard mode. This mode creates and releases ECS instances to perform scaling.
        # 
        # - `recycle`: fast mode. This mode creates, stops, and starts ECS instances to perform scaling. This improves scaling speed. When an instance is stopped, its computing resources are not billed, but its storage resources are. This does not apply to instance types with local disks.
        self.scaling_policy = scaling_policy
        # A list of security group IDs.
        self.security_group_ids = security_group_ids
        # The number of available instance types. The scaling group creates spot instances of multiple instance types that are provided at the lowest cost. Valid values: [1, 10].
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable the feature of supplementing spot instances. If this feature is enabled, the scaling group attempts to create a new instance to replace a spot instance that is reclaimed. Valid values:
        # 
        # - `true`: enables the feature of supplementing spot instances.
        # 
        # - `false`: disables the feature of supplementing spot instances.
        self.spot_instance_remedy = spot_instance_remedy
        # The price range for the spot instance.
        self.spot_price_limit = spot_price_limit
        # The bidding policy for the spot instance. Valid values:
        # 
        # - `NoSpot`: The instance is not a spot instance.
        # 
        # - `SpotWithPriceLimit`: The instance is a spot instance for which you can specify the maximum hourly price.
        # 
        # - `SpotAsPriceGo`: The system automatically bids for the instance. The bid is based on the market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable the performance burst feature for the system disk. Valid values:
        # 
        # - true: enables the performance burst feature. If your business fluctuates and is subject to unexpected data read and write pressure, the cloud disk temporarily improves its performance until your business returns to a stable state.
        # 
        # - false: disables the performance burst feature.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The multi-disk type of the system disk. If a disk of a higher priority disk type cannot be used, the system automatically tries the next priority disk type to create the system disk.
        self.system_disk_categories = system_disk_categories
        # The type of the system disk. Valid values:
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
        # The encryption algorithm that is used for the system disk. Valid value: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system disk. Valid values:
        # 
        # - true: encrypts the system disk.
        # 
        # - false: does not encrypt the system disk.
        self.system_disk_encrypted = system_disk_encrypted
        # The ID of the KMS key that is used to encrypt the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the system disk. This parameter is valid only for ESSD disks. The performance level of a disk is related to its size. For more information, see [ESSDs](https://help.aliyun.com/document_detail/122389.html).
        # 
        # - PL0: The maximum concurrent I/O performance is moderate and the read/write latency is relatively stable.
        # 
        # - PL1: The maximum concurrent I/O performance is moderate and the read/write latency is relatively stable.
        # 
        # - PL2: The maximum concurrent I/O performance is high and the read/write latency is stable.
        # 
        # - PL3: The maximum concurrent I/O performance is very high and the read/write latency is very stable.
        self.system_disk_performance_level = system_disk_performance_level
        # The pre-configured read/write IOPS of the system disk.
        # 
        # Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The size of the system disk. Unit: GiB.
        # 
        # Valid values: [20, 2048].
        # 
        # The value of this parameter must be greater than or equal to max{20, ImageSize}.
        # 
        # Default value: max{40, The size of the image that corresponds to the ImageId parameter}.
        self.system_disk_size = system_disk_size
        # The snapshot policy for the system disk.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # The tags that you want to add only to ECS instances.
        # 
        # Tag keys cannot be repeated. A tag key can be up to 128 characters in length. Tag keys and tag values cannot start with "aliyun" or "acs:" and cannot contain "https\\://" or "http\\://".
        self.tags = tags
        # A list of vSwitch IDs. You can specify 1 to 8 vSwitch IDs.
        # 
        # > For high availability, select vSwitches in different zones.
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

        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances

        if self.resource_pool_options is not None:
            result['resource_pool_options'] = self.resource_pool_options.to_map()

        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy

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
            temp_model = main_models.ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m.get('private_pool_options'))

        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')

        if m.get('resource_pool_options') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestScalingGroupResourcePoolOptions()
            self.resource_pool_options = temp_model.from_map(m.get('resource_pool_options'))

        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')

        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')

        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')

        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')

        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k1 in m.get('spot_price_limit'):
                temp_model = main_models.ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit()
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

class ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of the spot instance.
        self.instance_type = instance_type
        # The maximum price of a single instance.
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

class ModifyClusterNodePoolRequestScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # A list of private pool IDs. The IDs of elastic assurance services or capacity reservation services. You can specify only the IDs of private pools in Target mode. You can specify 1 to 20 IDs.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy that is used when you create an instance. Resource pools include private pools that are generated after elastic assurance services or capacity reservation services take effect, and public pools. You can select a resource pool when you start an instance. Valid values:
        # PrivatePoolFirst: Private pool first. If you select this policy and specify resouce_pool_options.private_pool_ids, the specified private pool is used first. If you do not specify a private pool or the capacity of the specified private pool is insufficient, the system automatically matches a private pool in Open mode. If no matching private pool is found, a public pool is used to create the instance.
        # PrivatePoolOnly: Private pool only. If you select this policy, you must specify resouce_pool_options.private_pool_ids. If the capacity of the specified private pool is insufficient, the instance fails to be started.
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

class ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private node pool. If `match_criteria` is set to `Target`, you must specify the ID of the private pool.
        self.id = id
        # The type of the private node pool. This parameter specifies the private pool capacity option for instance startup. After an elastic assurance service or a capacity reservation service takes effect, it generates a private pool of capacity for instance startup. Valid values:
        # 
        # - `Open`: Open mode. The system automatically matches the capacity of private pools in Open mode. If no matching private pool is found, the instance is started using public pool resources.
        # 
        # - `Target`: Specified mode. The instance is started using the capacity of a specified private pool. If the capacity of the specified private pool is unavailable, the instance fails to be started.
        # 
        # - `None`: The instance is started without using the capacity of a private pool.
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

class ModifyClusterNodePoolRequestNodepoolInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
    ):
        # The name of the node pool.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-).
        self.name = name
        # The ID of the resource group for the node pool. Instances created in the node pool belong to this resource group.
        # 
        # A resource can belong to only one resource group. You can use resource groups to categorize resources by project, application, or organization.
        self.resource_group_id = resource_group_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')

        return self

class ModifyClusterNodePoolRequestManagement(DaraModel):
    def __init__(
        self,
        auto_fault_diagnosis: bool = None,
        auto_repair: bool = None,
        auto_repair_policy: main_models.ModifyClusterNodePoolRequestManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: main_models.ModifyClusterNodePoolRequestManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: main_models.ModifyClusterNodePoolRequestManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: main_models.ModifyClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # Specifies whether to enable auto node repair. This parameter takes effect only when enable is set to `true`.
        # 
        # - `true`: Auto repair is enabled.
        # 
        # - `false`: Auto repair is disabled.
        # 
        # Default value: `true`
        self.auto_repair = auto_repair
        # The auto node repair policy.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to enable auto node upgrade. This parameter takes effect only when enable is set to `true`.
        # 
        # - `true`: enables auto upgrade.
        # 
        # - `false`: disables auto upgrade.
        # 
        # Default value: `true`
        self.auto_upgrade = auto_upgrade
        # The auto upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically fix CVE vulnerabilities. This parameter takes effect only when enable is set to `true`.
        # 
        # - `true`: allows automatic CVE fixing.
        # 
        # - `false`: disallows automatic CVE fixing.
        # 
        # Default value: `true`.
        self.auto_vul_fix = auto_vul_fix
        # The policy for automatically fixing CVE vulnerabilities.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the managed node pool. Valid values:
        # 
        # - `true`: Enables the managed node pool.
        # 
        # - `false`: Disables the managed node pool. Other related configurations are ignored.
        # 
        # Default value: `false`.
        self.enable = enable
        # This parameter is deprecated. Use the `auto_upgrade` parameter at the upper level instead.
        # 
        # The auto upgrade configurations. This parameter takes effect only when enable is set to `true`.
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
            temp_model = main_models.ModifyClusterNodePoolRequestManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m.get('auto_repair_policy'))

        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')

        if m.get('auto_upgrade_policy') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m.get('auto_upgrade_policy'))

        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')

        if m.get('auto_vul_fix_policy') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m.get('auto_vul_fix_policy'))

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('upgrade_config') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m.get('upgrade_config'))

        return self

class ModifyClusterNodePoolRequestManagementUpgradeConfig(DaraModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # This parameter is deprecated. Use the `auto_upgrade` parameter at the upper level instead.
        # 
        # Specifies whether to enable auto upgrade:
        # 
        # - true: enables auto upgrade.
        # 
        # - false: disables auto upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes.
        # 
        # Valid values: [1, 1000]
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of extra nodes. You can specify only one of surge and `surge_percentage`.
        # 
        # Nodes may become unavailable during an upgrade. You can create extra nodes to ensure service continuity.
        # 
        # > The number of extra nodes must not exceed the current number of nodes.
        self.surge = surge
        # The percentage of extra nodes. You can specify only one of surge and `surge_percentage`.
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

class ModifyClusterNodePoolRequestManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        exclude_packages: str = None,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # The packages that should be excluded during vulnerability fixing.
        # 
        # Default value: `kernel`.
        self.exclude_packages = exclude_packages
        # Specifies whether to allow node restart. This parameter takes effect only when auto_vul_fix is set to `true`. Valid values:
        # 
        # - `true`: allows node restart.
        # 
        # - `false`: disallows node restart.
        # 
        # Default value: `true`
        self.restart_node = restart_node
        # The vulnerability levels that are allowed to be automatically fixed. The value is a comma-separated list. Example: `asap,later`. Supported vulnerability levels:
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

class ModifyClusterNodePoolRequestManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
        auto_upgrade_os: bool = None,
        auto_upgrade_runtime: bool = None,
    ):
        # Specifies whether to allow auto kubelet upgrade. This parameter takes effect only when auto_upgrade is set to `true`. Valid values:
        # 
        # - `true`: allows auto kubelet upgrade.
        # 
        # - `false`: disallows auto kubelet upgrade.
        # 
        # Default value: `true`
        self.auto_upgrade_kubelet = auto_upgrade_kubelet
        # Specifies whether to allow auto operating system upgrade. This parameter takes effect only when auto_upgrade is set to `true`. Valid values:
        # 
        # - `true`: allows auto operating system upgrade.
        # 
        # - `false`: disallows auto operating system upgrade.
        # 
        # Default value: `false`.
        self.auto_upgrade_os = auto_upgrade_os
        # Specifies whether to allow auto runtime upgrade. This parameter takes effect only when auto_upgrade is set to `true`. Valid values:
        # 
        # - `true`: allows auto runtime upgrade.
        # 
        # - `false`: disallows auto runtime upgrade.
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

class ModifyClusterNodePoolRequestManagementAutoRepairPolicy(DaraModel):
    def __init__(
        self,
        approval_required: bool = None,
        auto_repair_policy_id: str = None,
        restart_node: bool = None,
    ):
        # Specifies whether manual approval is required for node repair.
        self.approval_required = approval_required
        # The ID of the auto repair policy.
        self.auto_repair_policy_id = auto_repair_policy_id
        # Specifies whether to allow node restart. This parameter takes effect only when auto_repair is set to `true`. Valid values:
        # 
        # - `true`: allows node restart.
        # 
        # - `false`: disallows node restart.
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

class ModifyClusterNodePoolRequestKubernetesConfig(DaraModel):
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
        # - `true`: installs Cloud Monitor on ECS nodes.
        # 
        # - `false`: does not install Cloud Monitor on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy of the node. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later:
        # 
        # - `static`: allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity.
        # 
        # - `none`: indicates that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The labels that you want to add to the nodes. The following rules apply:
        # 
        # - A label is a case-sensitive key-value pair. You can add up to 20 labels.
        # 
        # - The key must be unique and can be up to 64 characters in length. The value can be empty and can be up to 128 characters in length. The key and the value cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # The custom node name parameter. A node name consists of three parts: a prefix, the node IP address, and a suffix.
        # 
        # The prefix and suffix can contain one or more parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or a digit. The node IP address is the complete private IP address of the node.
        # 
        # The parameter consists of four parts that are separated by commas. For example, if you pass the "customized,aliyun,ip,com" string (where "customized" and "ip" are fixed strings, "aliyun" is the prefix, and "com" is the suffix), the node name is aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # The pre-customized instance data. Before a node is added to the cluster, the specified pre-customized instance data script is run. For more information, see [User data](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The name of the container runtime. ACK supports the following three container runtimes.
        # 
        # - containerd: We recommend that you use this runtime. It is supported by all cluster versions.
        # 
        # - Sandboxed-Container.runv: a sandboxed container that provides higher isolation. It is supported by clusters of Kubernetes 1.31 and earlier.
        # 
        # - docker: This runtime is no longer maintained. It is supported by clusters of Kubernetes 1.22 and earlier.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The node taint configurations.
        self.taints = taints
        # Specifies whether the scaled-out nodes are unschedulable.
        # 
        # - true: The nodes are unschedulable.
        # 
        # - false: The nodes are schedulable.
        self.unschedulable = unschedulable
        # The instance user data. After a node is added to the cluster, the specified user data script is run. For more information, see [User data](https://help.aliyun.com/document_detail/49121.html).
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

class ModifyClusterNodePoolRequestAutoScaling(DaraModel):
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
        # This parameter is deprecated. Use internet_charge_type and internet_max_bandwidth_out instead.
        # The peak bandwidth of the EIP.
        # 
        # Valid values: [1, 100]. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # This parameter is deprecated. Use internet_charge_type and internet_max_bandwidth_out instead.
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
        # - `true`: Enables auto scaling for the node pool. If the resources in the cluster do not meet the scheduling requirements of application pods, ACK automatically scales the nodes based on the configured minimum and maximum numbers of instances. For clusters of Kubernetes 1.24 or later, instant elasticity is enabled by default. For clusters of a Kubernetes version earlier than 1.24, node autoscaling is enabled by default. For more information, see [Node scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: Disables auto scaling. ACK adjusts the number of nodes in the node pool to the value of \\`desired_size\\` and keeps the number of nodes unchanged.
        # 
        # If this parameter is set to false, other parameters in `auto_scaling` do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # This parameter is deprecated. Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # - `true`: associates an EIP.
        # 
        # - `false`: does not associate an EIP.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances that can be created in the node pool. This parameter does not include existing instances. This parameter takes effect only when `enable=true`.
        # 
        # Valid values: [min_instances, 2000]. Default value: 0.
        self.max_instances = max_instances
        # The minimum number of instances that can be created in the node pool. This parameter does not include existing instances. This parameter takes effect only when `enable=true`.
        # 
        # Valid values: [0, max_instances]. Default value: 0.
        # 
        # > - If the minimum number of instances is not 0, the specified number of ECS instances are automatically created after the scaling group is created.
        # >
        # > - Set the maximum number of instances to a value that is not smaller than the current number of nodes in the node pool. Otherwise, a scale-in event is triggered after auto scaling is enabled.
        self.min_instances = min_instances
        # The type of auto scaling. This parameter is specified based on the instance type. Valid values:
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

