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
        eflo_node_group: main_models.ModifyClusterNodePoolRequestEfloNodeGroup = None,
        kubernetes_config: main_models.ModifyClusterNodePoolRequestKubernetesConfig = None,
        management: main_models.ModifyClusterNodePoolRequestManagement = None,
        nodepool_info: main_models.ModifyClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: main_models.ModifyClusterNodePoolRequestScalingGroup = None,
        tee_config: main_models.ModifyClusterNodePoolRequestTeeConfig = None,
        update_nodes: bool = None,
    ):
        # The auto scaling configuration.
        self.auto_scaling = auto_scaling
        # Specifies whether to enable concurrency.
        self.concurrency = concurrency
        self.eflo_node_group = eflo_node_group
        # The cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # The managed node pool configuration.
        self.management = management
        # The node pool configuration.
        self.nodepool_info = nodepool_info
        # The scaling group configuration of the node pool.
        self.scaling_group = scaling_group
        # The confidential computing cluster configuration.
        self.tee_config = tee_config
        # Synchronously updates node labels and taints.
        self.update_nodes = update_nodes

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.eflo_node_group:
            self.eflo_node_group.validate()
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

        if self.eflo_node_group is not None:
            result['eflo_node_group'] = self.eflo_node_group.to_map()

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

        if m.get('eflo_node_group') is not None:
            temp_model = main_models.ModifyClusterNodePoolRequestEfloNodeGroup()
            self.eflo_node_group = temp_model.from_map(m.get('eflo_node_group'))

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
        # - `true`: enabled.
        # - `false`: disabled.
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
        # Specifies whether to enable auto-renewal for nodes. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # - `true`: Enables auto-renewal.
        # - `false`: Disables auto-renewal.
        # 
        # Default value: `false`.
        self.auto_renew = auto_renew
        # The auto-renewal period for a single renewal cycle. Valid values:
        # - When PeriodUnit=Week: 1, 2, 3.
        # - When PeriodUnit=Month: 1, 2, 3, 6, 12, 24, 36, 48, 60.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        # When `multi_az_policy` is set to `COST_OPTIMIZED`, specifies whether to allow the system to automatically create pay-as-you-go instances if spot instances cannot be created due to price or inventory reasons to meet the required number of ECS instances. Valid values:
        # 
        # - `true`: Allows the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        # - `false`: Does not allow the system to automatically create pay-as-you-go instances to meet the required number of ECS instances.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The node data cloud disk configuration. Valid values: [0,10\\]. You can add up to 10 data cloud disks.
        self.data_disks = data_disks
        # The deployment set ID for ECS instances scaled out by the node pool. This setting takes effect only on incremental nodes. The deployment set of existing nodes is not changed.
        self.deploymentset_id = deploymentset_id
        # The desired number of nodes in the node pool.
        # 
        # The total number of nodes that the node pool should maintain. Configure at least 2 nodes to ensure that cluster components run properly. You can adjust the desired node count to scale the node pool in or out.
        # 
        # If you do not need to create nodes, set this parameter to 0 and manually adjust the node count later.
        self.desired_size = desired_size
        # The block device initialization configuration.
        self.disk_init = disk_init
        # The custom image ID. You can call `DescribeKubernetesVersionMetadata` to query the images supported by the system. The latest system image is used by default.
        self.image_id = image_id
        # The operating system distribution type. Use this field to specify the node operating system. Valid values:
        # 
        # - `AliyunLinux`: Alinux2 image.
        # - `AliyunLinuxSecurity`: Alinux2 UEFI image.
        # - `AliyunLinux3`: Alinux3 image.
        # - `AliyunLinux3Arm64`: Alinux3 ARM image.
        # - `AliyunLinux3Security`: Alinux3 UEFI image.
        # - `CentOS`: CentOS image.
        # - `Windows`: Windows image.
        # - `WindowsCore`: WindowsCore image.
        # - `ContainerOS`: container-optimized image.
        # - `AliyunLinux3ContainerOptimized`: Alinux3 container-optimized image.
        self.image_type = image_type
        # The billing method of nodes in the node pool. Valid values:
        # 
        # - `PrePaid`: subscription.
        # - `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.instance_charge_type = instance_charge_type
        # The instance attribute configuration.
        self.instance_patterns = instance_patterns
        # The list of node instance types. You can select multiple instance types as alternatives. When each node is created, the system attempts to purchase instances starting from the first specification until the creation succeeds. The final purchased instance type may vary depending on inventory availability.
        # 
        # Supported number of instance types: [1,10].
        self.instance_types = instance_types
        # The billing type for public IP addresses. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth for node public IP addresses, in Mbit/s. Valid values: [1,100\\].
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The key pair name. This parameter is mutually exclusive with `login_password`. For managed node pools, only `key_pair` is supported.
        self.key_pair = key_pair
        # The SSH logon password. This parameter is mutually exclusive with `key_pair`. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The multi-zone scaling policy for ECS instances in the scaling group. Valid values:
        # 
        # - `PRIORITY`: Scales based on the vSwitches (VSwitchIds.N) you defined. When ECS instances cannot be created in the zone of a higher-priority vSwitch, the system automatically uses the next-priority vSwitch.
        # 
        # - `COST_OPTIMIZED`: Attempts to create instances in order of lowest vCPU unit price. When the scaling configuration specifies multiple instance types with spot billing method, spot instances are created first. You can use the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when spot instances cannot be created due to insufficient inventory.
        # 
        #   > `COST_OPTIMIZED` takes effect only when the scaling configuration specifies multiple instance types or uses spot instances.
        # 
        # - `BALANCE`: Distributes ECS instances evenly across the zones specified in the scaling group. If zones become unbalanced due to insufficient inventory, you can call the `RebalanceInstances` API operation to rebalance resources. For more information, see [RebalanceInstances](https://help.aliyun.com/document_detail/71516.html).
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances required by the scaling group. Valid values: [0,1000\\]. Pay-as-you-go instances are created first when the number of pay-as-you-go instances is less than this value.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among instances that exceed the minimum pay-as-you-go instance count (`on_demand_base_capacity`). Valid values: [0,100\\].
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of nodes in the node pool. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - When `period_unit=Week`, valid values of `period`: {1, 2, 3, 4}.
        # - When `period_unit=Month`, valid values of `period`: {1, 2, 3, 4, 5, 6, 7, 8, 9, 12, 24, 36, 48, 60}.
        self.period = period
        # The billing period of nodes in the node pool. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # - `Month`: billed on a monthly basis.
        # - `Week`: billed on a weekly basis.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # **This parameter is deprecated.** Use the `image_type` parameter instead.
        # 
        # The operating system platform. Valid values:
        # 
        # - `AliyunLinux`
        # - `CentOS`
        # - `Windows`
        # - `WindowsCore`
        self.platform = platform
        # The private node pool configuration.
        self.private_pool_options = private_pool_options
        # The list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The resource pools and resource pool policy used when creating instances. Note the following when you set this parameter:
        # This parameter takes effect only when creating pay-as-you-go instances.
        # This parameter cannot be set together with private_pool_options.match_criteria or private_pool_options.id.
        self.resource_pool_options = resource_pool_options
        # The scaling group mode. Valid values:
        # 
        # - `release`: standard mode. Scales by creating and releasing ECS instances based on resource usage.
        # - `recycle`: swift mode. Scales by creating, stopping, and starting instances, which improves the speed of subsequent scaling operations. (Compute resources are not charged during the stopped state. Only storage fees are charged, except for local disk instance types.)
        self.scaling_policy = scaling_policy
        # The list of security group IDs.
        self.security_group_ids = security_group_ids
        # The number of available instance types. The scaling group creates spot instances across the lowest-cost instance types in a balanced manner. Valid values: [1,10\\].
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to enable spot instance supplementation. When enabled,
        self.spot_instance_remedy = spot_instance_remedy
        # The spot instance price limit configuration.
        self.spot_price_limit = spot_price_limit
        # The spot instance type. Valid values:
        # 
        # - `NoSpot`: non-spot instance.
        # - `SpotWithPriceLimit`: spot instance with a price limit.
        # - `SpotAsPriceGo`: system automatically bids at the current market price.
        # 
        # For more information, see [Spot instances](https://help.aliyun.com/document_detail/157759.html).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable burst (performance burst) for the node system cloud disk. Valid values:
        # - true: Enabled. When enabled, the cloud disk temporarily boosts performance during sudden data read/write pressure from fluctuating workloads until the workload stabilizes.
        # - false: Disabled.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # The multiple system cloud disk types. When a higher-priority cloud disk type is unavailable, the system automatically attempts the next-priority cloud disk type to create the system cloud disk.
        self.system_disk_categories = system_disk_categories
        # The node system cloud disk type. Valid values:
        # - `cloud_efficiency`: ultra cloud disk.
        # - `cloud_ssd`: standard SSD.
        # - `cloud_essd`: ESSD.
        # - `cloud_auto`: ESSD AutoPL cloud disk.
        # - `cloud_essd_entry`: ESSD Entry cloud disk.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        # The encryption algorithm used by the system cloud disk. Valid values: aes-256.
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # Specifies whether to encrypt the system cloud disk. Valid values:
        # 
        # - true: Encrypted.
        # 
        # - false: Not encrypted.
        self.system_disk_encrypted = system_disk_encrypted
        # The KMS key ID used by the system cloud disk.
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level of the node system cloud disk. This parameter takes effect only for ESSD cloud disks. The performance level is related to the cloud disk size. For more information, see [ESSD cloud disks](https://help.aliyun.com/document_detail/122389.html).
        # - PL0: moderate maximum concurrent I/O performance with relatively stable read/write latency.
        # - PL1: moderate maximum concurrent I/O performance with relatively stable read/write latency.
        # - PL2: high maximum concurrent I/O performance with stable read/write latency.
        # - PL3: ultra-high maximum concurrent I/O performance with extremely stable read/write latency.
        self.system_disk_performance_level = system_disk_performance_level
        # The provisioned read/write IOPS for the node system cloud disk.
        # 
        # Valid values: 0~min{50,000, 1000 × capacity - baseline performance}. Baseline performance = min{1,800 + 50 × capacity, 50000}.
        # 
        # This parameter is supported only when `system_disk_category` is set to `cloud_auto`. For more information, see [ESSD AutoPL cloud disks](https://help.aliyun.com/document_detail/368372.html).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The node system cloud disk size, in GiB.
        # 
        # Valid values: [20,2048\\].
        # 
        # The value must be greater than or equal to max{20, ImageSize}.
        # 
        # Default value: max{40, image size corresponding to the ImageId parameter}.
        self.system_disk_size = system_disk_size
        # The snapshot policy for the system cloud disk.
        self.system_disk_snapshot_policy_id = system_disk_snapshot_policy_id
        # Tags added to ECS instances only.
        # 
        # Tag keys cannot be duplicated and can be up to 128 characters in length. Tag keys and tag values cannot start with "aliyun" or "acs:", or contain "https://" or "http://".
        self.tags = tags
        # The list of vSwitch IDs. Valid values: [1,8\\].
        # 
        # > To ensure high availability, select vSwitches in different zones.
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
        # The spot instance type.
        self.instance_type = instance_type
        # The maximum price per instance.
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
        # The list of private pool IDs, which are the IDs of elasticity assurance or capacity reservation services. Only Target mode private pool IDs can be specified. Valid values of N: 1 to 20.
        self.private_pool_ids = private_pool_ids
        # The resource pool policy used when creating instances. Resource pools include private pools generated after an elasticity assurance or capacity reservation takes effect, and public pools, for instance launching. Valid values:
        # PrivatePoolFirst: private pool first. When this policy is selected, if resouce_pool_options.private_pool_ids is specified, the specified private pools are used first. If no private pool is specified or the specified private pool capacity is insufficient, open private pool capacity is automatically matched. If no matching private pool is available, public pool resources are used.
        # PrivatePoolOnly: private pool only. When this policy is selected, you must specify resouce_pool_options.private_pool_ids. If the specified private pool capacity is insufficient, the instance fails to launch.
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

class ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions(DaraModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The private node pool ID. When `match_criteria` is set to `Target`, you must specify the private pool ID.
        self.id = id
        # The private node pool type. Specifies the private pool capacity option for launching instances. After an elasticity assurance or capacity reservation takes effect, a private pool is generated for instance launching. Valid values:
        # - `Open`: open mode. The system automatically matches open private pool capacity. If no matching private pool capacity is available, public pool resources are used.
        # - `Target`: specified mode. The instance is launched using the specified private pool capacity. If the specified private pool capacity is unavailable, the instance fails to launch.
        # - `None`: not used. The instance does not use private pool capacity.
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
        # The node pool name.
        # 
        # Naming rules: The name must be 1 to 63 characters in length and can contain digits, Chinese characters, letters, and hyphens (-). It cannot start with a hyphen (-).
        self.name = name
        # The resource group ID of the node pool. Instances created by the node pool belong to this resource group.
        # 
        # A resource can belong to only one resource group. You can map resource groups to concepts such as projects, applications, or organizations based on your business scenarios.
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
        # Specifies whether to automatically repair nodes. This parameter takes effect only when `enable=true`.
        # 
        # - `true`: Enables auto repair.
        # 
        # - `false`: Disables auto repair.
        # 
        # Default value: `true`.
        self.auto_repair = auto_repair
        # The auto repair node policy.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to automatically upgrade nodes. This parameter takes effect only when `enable=true`.
        # - `true`: Enables auto upgrade.
        # - `false`: Disables auto upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # The auto upgrade policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether to automatically fix CVE vulnerabilities. This parameter takes effect only when `enable=true`.
        # 
        # - `true`: Allows automatic CVE fixing.
        # - `false`: Does not allow automatic CVE fixing.
        # 
        # Default value: `true`.
        self.auto_vul_fix = auto_vul_fix
        # The auto CVE fix policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the managed node pool. Valid values:
        # 
        # - `true`: Enables the managed node pool.
        # - `false`: Disables the managed node pool. Other related configurations take effect only when `enable=true`.
        # 
        # Default value: `false`.
        self.enable = enable
        # [This field is deprecated] Use the `auto_upgrade` parameter at the upper level instead.
        # 
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
        # [This field is deprecated] Use the `auto_upgrade` parameter at the upper level instead.
        # 
        # Specifies whether to enable auto upgrade:
        # 
        # - true: Enabled.
        # - false: Disabled.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # The maximum number of unavailable nodes.
        # 
        # Valid values: [1,1000\\].
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of extra nodes. This parameter is mutually exclusive with `surge_percentage`.
        # 
        # Nodes become unavailable during an upgrade. You can create extra nodes to compensate for the cluster workload.
        # 
        # > The number of extra nodes should not exceed the current number of nodes.
        self.surge = surge
        # The percentage of extra nodes. This parameter is mutually exclusive with `surge`.
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

class ModifyClusterNodePoolRequestManagementAutoVulFixPolicy(DaraModel):
    def __init__(
        self,
        exclude_packages: str = None,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # Specifies the packages to exclude during vulnerability fixing.
        # 
        # Default value: `kernel`.
        self.exclude_packages = exclude_packages
        # Specifies whether to allow node restart. This parameter takes effect only when `auto_vul_fix=true`. Valid values:
        # - `true`: Allows node restart.
        # - `false`: Does not allow node restart.
        # 
        # Default value: `true`.
        self.restart_node = restart_node
        # The vulnerability levels allowed for automatic fixing, separated by commas. Example: `asap,later`. Supported vulnerability levels:
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

class ModifyClusterNodePoolRequestManagementAutoUpgradePolicy(DaraModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
        auto_upgrade_os: bool = None,
        auto_upgrade_runtime: bool = None,
    ):
        # Specifies whether to allow automatic kubelet upgrade. This parameter takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: Allows automatic kubelet upgrade.
        # - `false`: Does not allow automatic kubelet upgrade.
        # 
        # Default value: `true`.
        self.auto_upgrade_kubelet = auto_upgrade_kubelet
        # Specifies whether to allow automatic operating system upgrade. This parameter takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: Allows automatic operating system upgrade.
        # - `false`: Does not allow automatic operating system upgrade.
        # 
        # Default value: `false`.
        self.auto_upgrade_os = auto_upgrade_os
        # Specifies whether to allow automatic runtime upgrade. This parameter takes effect only when `auto_upgrade=true`. Valid values:
        # - `true`: Allows automatic runtime upgrade.
        # - `false`: Does not allow automatic runtime upgrade.
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
        # Specifies whether node repair requires manual approval.
        self.approval_required = approval_required
        # The auto repair policy ID.
        self.auto_repair_policy_id = auto_repair_policy_id
        # Specifies whether to allow node restart. This parameter takes effect only when `auto_repair=true`. Valid values:
        # 
        # - `true`: Allows node restart.
        # - `false`: Does not allow node restart.
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
        # Specifies whether to install the CloudMonitor agent on ECS nodes. After installation, you can view monitoring information about the created ECS instances in the CloudMonitor console. We recommend that you enable this feature. Valid values:
        # 
        # - `true`: installs the CloudMonitor agent on ECS nodes.
        # - `false`: does not install the CloudMonitor agent on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy for nodes. The following two policies are supported for cluster versions 1.12.6 and later:
        # 
        # - `static`: allows pods with certain resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # - `none`: enables the existing default CPU affinity scheme.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The node labels. Adds labels to Kubernetes cluster nodes. Label definition rules:
        # 
        # - Labels consist of case-sensitive key-value pairs. You can set up to 20 labels.
        # - Label keys cannot be duplicated and can be up to 64 characters in length. Label values can be empty and can be up to 128 characters in length. Neither label keys nor label values can start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # The custom node name parameter. A node name consists of three parts: prefix + node IP + suffix.
        # 
        # Both the prefix and suffix can consist of one or more parts separated by ".". Each part can contain lowercase letters, digits, and hyphens (-). The node name must start and end with a lowercase letter or digit. The node IP is the full private IP address of the node.
        # 
        # The parameter contains four parts separated by commas. For example, if you pass in the string "customized,aliyun,ip,com" (where "customized" and "ip" are fixed strings, "aliyun" is the prefix, and "com" is the suffix), the node name is: aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # The pre-user data for the instance. Before the node joins the cluster, the specified pre-user data script is run. For more information, see [User data scripts](https://help.aliyun.com/document_detail/49121.html).
        self.pre_user_data = pre_user_data
        # The container runtime name. ACK supports the following three container runtimes:
        # 
        # - containerd: recommended. Supported by all cluster versions.
        # - Sandboxed-Container.runv: sandboxed container that provides higher isolation. Supported by cluster versions 1.31 and earlier.
        # - docker: no longer maintained. Supported by cluster versions 1.22 and earlier.
        # 
        # Default value: containerd.
        self.runtime = runtime
        # The container runtime version.
        self.runtime_version = runtime_version
        # The node taint configuration.
        self.taints = taints
        # Specifies whether the nodes added during scale-out are unschedulable.
        # 
        # - true: unschedulable.
        # 
        # - false: schedulable.
        self.unschedulable = unschedulable
        # The instance user data. After the node joins the cluster, the specified user data script is run. For more information, see [User data scripts](https://help.aliyun.com/document_detail/49121.html).
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

class ModifyClusterNodePoolRequestEfloNodeGroup(DaraModel):
    def __init__(
        self,
        auto_attach_enabled: str = None,
    ):
        self.auto_attach_enabled = auto_attach_enabled

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_attach_enabled is not None:
            result['auto_attach_enabled'] = self.auto_attach_enabled

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_attach_enabled') is not None:
            self.auto_attach_enabled = m.get('auto_attach_enabled')

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
        # [This field is deprecated] Use internet_charge_type and internet_max_bandwidth_out instead.
        # The peak EIP bandwidth.
        # 
        # Valid values: [1,100]. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # [This field is deprecated] Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # The EIP billing type. Valid values:
        # 
        # - `PayByBandwidth`: pay-by-bandwidth.
        # - `PayByTraffic`: pay-by-data-transfer.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # 
        # - `true`: Enables auto scaling for the node pool. When the capacity planning of the cluster cannot meet the scheduling requirements of application pods, ACK automatically scales nodes based on the configured minimum and maximum instance counts. Clusters of version 1.24 or later use instant elasticity by default. Clusters of versions earlier than 1.24 use auto scaling by default. For more information, see [Node scaling](https://help.aliyun.com/document_detail/2746785.html).
        # 
        # - `false`: Disables auto scaling. ACK adjusts the number of nodes in the node pool based on the configured desired node count and maintains the node count at the desired value.
        # 
        # When this parameter is set to false, other configuration parameters in `auto_scaling` do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # [This field is deprecated] This field is deprecated. Use internet_charge_type and internet_max_bandwidth_out instead.
        # 
        # - `true`: Associates an EIP.
        # - `false`: Does not associate an EIP.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of instances that can be scaled in the node pool, excluding your existing instances. This parameter takes effect only when `enable=true`.
        # 
        # Valid values: [min_instances, 2000]. Default value: 0.
        self.max_instances = max_instances
        # The minimum number of instances that can be scaled in the node pool, excluding your existing instances. This parameter takes effect only when `enable=true`.
        # 
        # Valid values: [0, max_instances]. Default value: 0.
        # 
        # > - If the minimum number of instances is not 0, the corresponding number of ECS instances are automatically created after the scaling group takes effect.
        # > - Set the maximum number of instances to a value that is not less than the current number of nodes in the node pool. Otherwise, nodes in the node pool are scaled in after the elastic scaling feature takes effect.
        self.min_instances = min_instances
        # The auto scaling type, classified by instance type. Valid values:
        # 
        # - `cpu`: regular instance type.
        # - `gpu`: GPU instance type.
        # - `gpushare`: GPU sharing type.
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

