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
        # Auto scaling configuration.
        self.auto_scaling = auto_scaling
        # Whether to run concurrently.
        self.concurrency = concurrency
        # Cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # Managed node pool configuration.
        self.management = management
        # Node pool configuration.
        self.nodepool_info = nodepool_info
        # Node pool scaling group configuration.
        self.scaling_group = scaling_group
        # Confidential computing cluster configuration.
        self.tee_config = tee_config
        # Synchronously update node labels and taints.
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
        # Whether to enable confidential computing cluster. Valid values:
        # 
        # - `true`: Enable.
        # - `false`: Disable.
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
        # Whether to enable auto renewal for nodes. Only takes effect when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enable auto renewal.
        # - `false`: Disable auto renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # Duration of each auto renewal. Valid values:
        # - When PeriodUnit=Week: 1, 2, 3.
        # - When PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # When `multi_az_policy` is set to `COST_OPTIMIZED`, whether to allow automatically creating pay-as-you-go instances to meet ECS instance count requirements when sufficient preemptible instances cannot be created due to price, inventory, or other reasons. Valid values:
        # 
        # - `true`: Allow automatically creating pay-as-you-go instances to meet ECS instance count requirements.
        # - `false`: Do not allow automatically creating pay-as-you-go instances to meet ECS instance count requirements.
        self.compensate_with_on_demand = compensate_with_on_demand
        # Node data disk configuration. Valid values: [0,10\\]. You can add up to 10 data disks.
        self.data_disks = data_disks
        # The deployment set that the ECS instances created by the node pool belong to. Only takes effect for incremental nodes; the deployment set of existing nodes will not be changed.
        self.deploymentset_id = deploymentset_id
        # Desired number of nodes in the node pool.
        # 
        # The total number of nodes that the node pool should maintain. It is recommended to configure at least 2 nodes to ensure cluster components run normally. You can scale the node pool in or out by adjusting the desired node count.
        # 
        # If you do not need to create nodes, you can set this to 0 and manually adjust it later to add nodes.
        self.desired_size = desired_size
        # Block device initialization configuration.
        self.disk_init = disk_init
        # Custom image ID. You can query system-supported images through `DescribeKubernetesVersionMetadata`. The latest system image is used by default.
        self.image_id = image_id
        # Operating system distribution type. It is recommended to use this field to specify the node operating system. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # - `AliyunLinuxSecurity`: Alinux2 image UEFI version.
        # - `AliyunLinux3`: Alinux3 image.
        # - `AliyunLinux3Arm64`: Alinux3 image ARM version.
        # - `AliyunLinux3Security`: Alinux3 image UEFI version.
        # - `CentOS`: CentOS image.
        # - `Windows`: Windows image.
        # - `WindowsCore`: WindowsCore image.
        # - `ContainerOS`: Container-optimized image.
        # - `AliyunLinux3ContainerOptimized`: Alinux3 image container-optimized version.
        self.image_type = image_type
        # Billing type for node pool nodes. Valid values:
        # 
        # - `PrePaid`: Subscription.
        # - `PostPaid`: Pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.instance_charge_type = instance_charge_type
        # Instance attribute configuration.
        self.instance_patterns = instance_patterns
        # List of node instance types. You can select multiple instance types as alternatives. When creating each node, the system attempts to purchase starting from the first type until successful. The final purchased instance type may vary depending on inventory.
        # 
        # Supported number of instance types: [1,10].
        self.instance_types = instance_types
        # Public IP billing type. Valid values:
        # 
        # - `PayByBandwidth`: Pay by fixed bandwidth.
        # - `PayByTraffic`: Pay by traffic usage.
        self.internet_charge_type = internet_charge_type
        # Maximum outbound bandwidth for node public IP, in Mbps (Mega bit per second). Valid values: [1,100\\].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # Key pair name. Mutually exclusive with `login_password`. When the node pool is a managed node pool, only `key_pair` is supported.
        self.key_pair = key_pair
        # SSH login password. Mutually exclusive with `key_pair`. Password must be 8 to 30 characters and contain at least three of the following: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # Multi-AZ scaling group ECS instance scaling policy. Valid values:
        # 
        # - `PRIORITY`: Scale based on the vSwitches (VSwitchIds.N) you defined. When ECS instances cannot be created in the availability zone of the higher-priority vSwitch, the next priority vSwitch is automatically used to create ECS instances.
        # 
        # - `COST_OPTIMIZED`: Create instances by trying from the lowest vCPU unit price. When the scaling configuration has set preemptible billing with multiple instance types, preemptible instances are created preferentially. You can further use the `CompensateWithOnDemand` parameter to specify whether to automatically try creating pay-as-you-go instances when preemptible instances cannot be created due to inventory or other reasons.
        # 
        #   > `COST_OPTIMIZED` only takes effect when the scaling configuration has set multiple instance types or selected preemptible instances.
        # 
        # - `BALANCE`: Evenly distribute ECS instances across multiple availability zones specified by the scaling group. If the zones become unbalanced due to insufficient inventory or other reasons, you can use the API `RebalanceInstances` to rebalance resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # Minimum number of pay-as-you-go instances required by the scaling group. Valid values: [0,1000\\]. Pay-as-you-go instances are created preferentially when the number of pay-as-you-go instances is less than this value.
        self.on_demand_base_capacity = on_demand_base_capacity
        # After the scaling group meets the minimum pay-as-you-go instance requirement (`on_demand_base_capacity`), the proportion of pay-as-you-go instances among the excess instances. Valid values: [0,100\\].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # Subscription duration for node pool nodes. Only takes effect when `instance_charge_type` is set to `PrePaid`, and is required.
        # 
        # - When `period_unit=Week`, valid values for `period`: {1, 2, 3, 4}.
        # - When `period_unit=Month`, valid values for `period`: {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 60}.
        self.period = period
        # Billing cycle for node pool nodes. Only takes effect when `instance_charge_type` is set to `PrePaid`, and is required.
        # 
        # - `Month`: Billed by month.
        # - `Week`: Billed by week.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # [This field is deprecated] Please use the `image_type` parameter instead.
        # 
        # Operating system platform. Valid values:
        # 
        # - `AliyunLinux`
        # - `CentOS`
        # - `Windows`
        # - `WindowsCore`
        self.platform = platform
        # Private node pool configuration.
        self.private_pool_options = private_pool_options
        # RDS instance list.
        self.rds_instances = rds_instances
        # Resource pool and resource pool policy used when creating instances. Note the following when setting this parameter:
        # This parameter only takes effect when creating pay-as-you-go instances.
        # This parameter cannot be set together with private_pool_options.match_criteria or private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # Scaling group mode. Valid values:
        # 
        # - `release`: Standard mode. Scale by creating and releasing ECS instances based on resource usage.
        # - `recycle`: Swift mode. Scale by creating, stopping, and starting instances to improve subsequent scaling speed (compute resources are not charged during shutdown, only storage fees apply, except for local disk instance types).
        self.scaling_policy = scaling_policy
        # List of security group IDs.
        self.security_group_ids = security_group_ids
        # Number of available instance types. The scaling group creates preemptible instances evenly across the lowest-cost instance types. Valid values: [1,10\\].
        self.spot_instance_pools = spot_instance_pools
        # Whether to enable supplementing preemptible instances. When enabled, the scaling group attempts to create new instances to replace preemptible instances that are about to be reclaimed upon receiving a system notification. Valid values:
        # 
        # - `true`: Enable supplementing preemptible instances.
        # - `false`: Disable supplementing preemptible instances.
        self.spot_instance_remedy = spot_instance_remedy
        # Preemptible instance market price range configuration.
        self.spot_price_limit = spot_price_limit
        # Preemptible instance type. Valid values:
        # 
        # - `NoSpot`: Non-preemptible instance.
        # - `SpotWithPriceLimit`: Set a maximum price for the preemptible instance.
        # - `SpotAsPriceGo`: System automatically bids, following the current market price.
        # 
        # For more information, see [Preemptible instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Whether to enable burst (performance burst) for the node system disk. Valid values:
        # - true: Enable. When enabled, cloud disks can temporarily boost performance based on actual business conditions when facing sudden data read/write pressure from volatile workloads, until the business returns to a steady state.
        # - false: Disable.
        # 
        # Only supported when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # Multiple disk types for the system disk. When the higher-priority disk type is unavailable, the system automatically tries the next priority disk type to create the system disk.
        self.system_disk_categories = system_disk_categories
        # Node system disk type. Valid values:
        # - `cloud_efficiency`: Ultra disk.
        # - `cloud_ssd`: SSD disk.
        # - `cloud_essd`: ESSD disk.
        # - `cloud_auto`: ESSD AutoPL disk.
        # - `cloud_essd_entry`: ESSD Entry disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # Encryption algorithm used for the system disk. Valid values: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Whether to encrypt the system disk. Valid values:
        # 
        # - true: Encrypt.
        # 
        # - false: Do not encrypt.
        self.system_disk_encrypted = system_disk_encrypted
        # KMS key ID used for the system disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # Node system disk performance level. Only takes effect for ESSD disks. The performance level is related to the disk size. For more information, see [ESSD disks](https://help.aliyun.com/document_detail/122389.html).
        # - PL0: Medium concurrent extreme I/O performance, relatively stable read/write latency.
        # - PL1: Medium concurrent extreme I/O performance, relatively stable read/write latency.
        # - PL2: High concurrent extreme I/O performance, stable read/write latency.
        # - PL3: Extremely high concurrent extreme I/O performance, extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # Provisioned read/write IOPS for the node system disk.
        # 
        # Valid values: 0~min{50,000, 1000\\*capacity-baseline performance}. Baseline performance=min{1,800+50\\*capacity, 50000}.
        # 
        # Only supported when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # Node system disk size, in GiB.
        # 
        # Valid values: [20,2048\\].
        # 
        # The value of this parameter must be greater than or equal to max{20, ImageSize}.
        # 
        # Default value: max{40, image size corresponding to the ImageId parameter}.
        self.system_disk_size = system_disk_size
        # System disk snapshot policy.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # Tags added only to ECS instances.
        # 
        # Tag keys cannot be duplicated and can be up to 128 characters. Tag keys and tag values cannot start with "aliyun" or "acs:", or contain "https://" or "http://".
        self.tags = tags
        # List of vSwitch IDs. Valid values: [1,8\\].
        # 
        # > To ensure high availability, it is recommended to select vSwitches in different availability zones.
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
        # Preemptible instance type.
        self.instance_type = instance_type
        # Maximum price per instance.
        # 
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

class ModifyClusterNodePoolRequestScalingGroupResourcePoolOptions(DaraModel):
    def __init__(
        self,
        private_pool_ids: List[str] = None,
        strategy: str = None,
    ):
        # List of private pool IDs, i.e., Elasticity Assurance IDs or Capacity Reservation IDs. Only Target mode private pool IDs can be passed. Valid values for N: 1~20.
        self.private_pool_ids = private_pool_ids
        # Resource pool policy used when creating instances. Resource pools include private pools generated after Elasticity Assurance or Capacity Reservation takes effect, as well as public pools, for instance launch selection. Valid values:
        # PrivatePoolFirst: Private pool first. When specified private_pool_ids are set, the specified private pools are used preferentially. If no private pool is specified or the specified private pool capacity is insufficient, open-type private pools are automatically matched. If no matching private pool is available, public pool resources are used to create instances.
        # PrivatePoolOnly: Private pool only. private_pool_ids must be specified. If the specified private pool capacity is insufficient, instance launch fails.
        # None: Do not use resource pool policy.
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
        # Private node pool ID. When `match_criteria` is `Target`, you need to further specify the private pool ID.
        self.id = id
        # Private node pool type. Private pool capacity option for instance launch. After an Elasticity Assurance or Capacity Reservation takes effect, a private pool capacity is generated for instance launch selection. Valid values:
        # - `Open`: Open mode. Automatically matches open-type private pool capacity. If no matching private pool capacity is available, public pool resources are used for launch.
        # - `Target`: Targeted mode. Uses specified private pool capacity to launch instances. If the private pool capacity is unavailable, instance launch fails.
        # - `None`: Do not use mode. Instance launch will not use private pool capacity.
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
        # Node pool name.
        # 
        # Naming rules: The name can contain digits, Chinese characters, English letters, or hyphens (-), must be 1 to 63 characters in length, and cannot start with a hyphen (-).
        self.name = name
        # The resource group ID of the node pool. Instances created by the node pool will belong to this resource group.
        # 
        # A resource can only belong to one resource group. Depending on different business scenarios, you can map a resource group to concepts such as projects, applications, or organizations.
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
        # Whether to automatically repair nodes. Only takes effect when `enable=true`.
        # 
        # - `true`: Auto repair.
        # 
        # - `false`: Do not auto repair.
        # 
        # Default value: `true`.
        self.auto_repair = auto_repair
        # Auto repair node policy.
        self.auto_repair_policy = auto_repair_policy
        # Whether to automatically upgrade nodes. Only takes effect when `enable=true`.
        # - `true`: Enable auto upgrade.
        # - `false`: Disable auto upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # Auto upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Whether to automatically fix CVE vulnerabilities. Only takes effect when `enable=true`.
        # 
        # - `true`: Allow automatic CVE fixing.
        # - `false`: Do not allow automatic CVE fixing.
        # 
        # Default value: `true`.
        self.auto_vul_fix = auto_vul_fix
        # Auto CVE fix policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Whether to enable managed node pool. Valid values:
        # 
        # - `true`: Enable managed node pool.
        # - `false`: Disable managed node pool. Other related configurations only take effect when `enable=true`.
        # 
        # Default value: `false`.
        self.enable = enable
        # [This field is deprecated] Please use the `auto_upgrade` parameter at the parent level instead.
        # 
        # Auto upgrade configuration. Only takes effect when `enable=true`.
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
        # [This field is deprecated] Please use the `auto_upgrade` parameter at the parent level instead.
        # 
        # Whether to enable auto upgrade:
        # 
        # - true: Enable.
        # - false: Disable.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # Maximum number of unavailable nodes.
        # 
        # Valid values: [1,1000\\]
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # Number of extra nodes. Mutually exclusive with `surge_percentage`.
        # 
        # During upgrade, nodes will be unavailable. You can create extra nodes to compensate for the cluster workload.
        # 
        # > It is recommended that the number of extra nodes does not exceed the current number of nodes.
        self.surge = surge
        # Percentage of extra nodes. Mutually exclusive with `surge`.
        # 
        # Number of extra nodes = percentage of extra nodes × number of nodes. For example, if the percentage of extra nodes is set to 50% and there are 6 existing nodes, the number of extra nodes = 50% × 6, which produces 3 extra nodes.
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
        # Specifies the packages to be excluded during vulnerability fix.
        # 
        # Default value: `kernel`.
        self.exclude_packages = exclude_packages
        # Whether to allow restarting nodes. Only takes effect when `auto_vul_fix=true`. Valid values:
        # - `true`: Allow restarting nodes.
        # - `false`: Do not allow restarting nodes.
        # 
        # Default value: `true`.
        self.restart_node = restart_node
        # Vulnerability levels allowed for automatic fixing, separated by commas. For example: `asap,later`. Supported vulnerability levels:
        # 
        # - `asap`: High
        # - `later`: Medium
        # - `nntf`: Low
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
        # Whether to allow auto upgrading kubelet. Only takes effect when `auto_upgrade=true`. Valid values:
        # - `true`: Allow auto upgrading kubelet.
        # - `false`: Do not allow auto upgrading kubelet.
        # 
        # Default value: `true`.
        self.auto_upgrade_kubelet = auto_upgrade_kubelet
        # Whether to allow auto upgrading the operating system. Only takes effect when `auto_upgrade=true`. Valid values:
        # - `true`: Allow auto upgrading the operating system.
        # - `false`: Do not allow auto upgrading the operating system.
        # 
        # Default value: `false`.
        self.auto_upgrade_os = auto_upgrade_os
        # Whether to allow auto upgrading the runtime. Only takes effect when `auto_upgrade=true`. Valid values:
        # - `true`: Allow auto upgrading the runtime.
        # - `false`: Do not allow auto upgrading the runtime.
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
        # Whether node repair requires manual approval.
        self.approval_required = approval_required
        # Auto repair policy ID.
        self.auto_repair_policy_id = auto_repair_policy_id
        # Whether to allow restarting nodes. Only takes effect when `auto_repair=true`. Valid values:
        # 
        # - `true`: Allow restarting nodes.
        # - `false`: Do not allow restarting nodes.
        # 
        # Default value: `true`.
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
        # Whether to install CloudMonitor on ECS nodes. After installation, you can view monitoring information of the created ECS instances in the CloudMonitor console. Recommended to enable. Valid values:
        # 
        # - `true`: Install CloudMonitor on ECS nodes.
        # - `false`: Do not install CloudMonitor on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # Node CPU management policy. Supported when the cluster version is 1.12.6 or above:
        # 
        # - `static`: Allows enhancing CPU affinity and exclusivity for Pods with certain resource characteristics on the node.
        # - `none`: Enables the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Node labels. Add labels to Kubernetes cluster nodes. Label definition rules:
        # 
        # - Labels are case-sensitive key-value pairs. You can set up to 20 labels.
        # - Label keys cannot be duplicated and can be up to 64 characters. Label values can be empty and up to 128 characters. Label keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # Custom node name parameter. The node name consists of three parts: prefix + node IP + suffix.
        # 
        # Both the prefix and suffix can consist of one or more parts separated by ".". Each part can use lowercase letters, digits, and "-". The node name must start and end with a lowercase letter or digit. The node IP is the complete private IP address of the node.
        # 
        # The parameter includes four parts separated by commas. For example, passing "customized,aliyun,ip,com" (where "customized" and "ip" are fixed strings, aliyun is the prefix, and com is the suffix), the node name will be: aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # Instance pre-custom data. Before the node joins the cluster, the specified instance pre-custom data script will be run. See [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # Container runtime name. ACK supports the following three container runtimes:
        # 
        # - containerd: Recommended. Supports all cluster versions.
        # - Sandboxed-Container.runv: Sandboxed container, providing higher isolation. Supports clusters with version 1.31 and below.
        # - docker: Maintenance discontinued. Supports clusters with version 1.22 and below.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # Container runtime version.
        self.runtime_version = runtime_version
        # Node taint configuration.
        self.taints = taints
        # Whether the node is unschedulable after scaling out.
        # 
        # - true: Unschedulable.
        # 
        # - false: Schedulable.
        self.unschedulable = unschedulable
        # Instance custom data. After the node joins the cluster, the specified instance custom data script will be run. See [User-Data scripts](https://help.aliyun.com/document_detail/49121.html).
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
        # [This field is deprecated] Please use internet_charge_type and internet_max_bandwidth_out instead.
        # EIP peak bandwidth.
        # 
        # Valid values: [1,100]. Unit: Mbps.
        self.eip_bandwidth = eip_bandwidth
        # [This field is deprecated] Please use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # EIP billing type. Valid values:
        # 
        # - `PayByBandwidth`: Pay by fixed bandwidth.
        # - `PayByTraffic`: Pay by traffic usage.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Whether to enable auto scaling. Valid values:
        # 
        # - `true`: Enable node pool auto scaling. When the cluster\\"s capacity planning cannot meet application Pod scheduling requirements, ACK automatically scales node resources based on the configured minimum and maximum instance counts. Clusters with version 1.24 and above enable instant node elasticity by default;
        # clusters with versions below 1.24 enable node auto scaling by default. For more information, see [Node Scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: Disable auto scaling. ACK adjusts the number of nodes in the node pool according to the configured desired node count, always maintaining the node count at the desired number.
        # 
        # When the value is false, other configuration parameters in `auto_scaling` will not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # [This field is deprecated] This field is deprecated. Please use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # - `true`: Bindpublic EIP.
        # - `false`: Do not bind EIP.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of scalable instances in the node pool, excluding your existing instances. Only takes effect when `enable=true`.
        # 
        # Valid values: [min_instances, 2000]. Default value: 0.
        self.max_instances = max_instances
        # The minimum number of scalable instances in the node pool, excluding your existing instances. Only takes effect when `enable=true`.
        # 
        # Valid values: [0, max_instances]. Default value: 0.
        # 
        # > - When the minimum number of instances is not 0, the corresponding number of ECS instances will be automatically created after the scaling group takes effect.
        # > - It is recommended that the configured maximum number of instances is not less than the current number of nodes in the node pool. Otherwise, the elastic scaling function will directly cause the node pool to scale in after taking effect.
        self.min_instances = min_instances
        # Auto scaling type, classified by auto scaling instance type. Valid values:
        # 
        # - `cpu`: Regular instance type.
        # - `gpu`: GPU instance type.
        # - `gpushare`: GPU sharing type.
        # - `spot`: Preemptible instance type.
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

