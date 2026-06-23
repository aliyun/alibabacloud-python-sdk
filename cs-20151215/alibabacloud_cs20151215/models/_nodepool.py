# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

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
        # The auto scaling configuration of the node pool.
        self.auto_scaling = auto_scaling
        # [This field is deprecated. Use desired_size instead.]
        # 
        # The number of nodes in the node pool.
        self.count = count
        # [This field is deprecated.]
        # 
        # The edge node pool configuration.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This value is valid only for node pools whose `type` is `edge`. Valid values:
        # 
        # - `basic`: basic.
        # - `private`: dedicated. Supported in version 1.22 and later.
        self.interconnect_mode = interconnect_mode
        # The cluster-related configuration.
        self.kubernetes_config = kubernetes_config
        # The managed node pool configuration.
        self.management = management
        # The maximum number of nodes allowed in the edge node pool. This parameter must be greater than or equal to 0. A value of 0 indicates no additional limit. The node pool is limited only by the maximum number of nodes that the cluster can contain. Edge node pools typically have a value greater than 0. ESS-type node pools and default edge-type node pools have a value of 0.
        self.max_nodes = max_nodes
        # The list of node components.
        self.node_components = node_components
        # The node configuration.
        self.node_config = node_config
        # The node pool configuration.
        self.nodepool_info = nodepool_info
        # The scaling group configuration of the node pool.
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
        # 是否为加密计算节点池。
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
        # 节点池是否开启自动续费，当`instance_charge_type`取值为`PrePaid`时才生效，取值：
        # 
        # - `true`：自动续费。
        # - `false`：不自动续费。
        # 
        # 默认值：`true`。
        self.auto_renew = auto_renew
        # 节点池自动续费周期。当`instance_charge_type`取值为`PrePaid`时才生效，且为必选值。
        # 
        # 当`PeriodUnit=Month`时，取值范围：{1, 2, 3, 6, 12}。
        # 
        # 默认值：1。
        self.auto_renew_period = auto_renew_period
        # 当`multi_az_policy`取值为`COST_OPTIMIZED`时，如果因价格、库存等原因无法创建足够的抢占式实例，是否允许自动尝试创建按量实例满足ECS实例数量要求。取值：
        # 
        # - `true`：允许自动尝试创建按量实例满足ECS实例数量要求。
        # - `false`：不允许自动尝试创建按量实例满足ECS实例数量要求。
        self.compensate_with_on_demand = compensate_with_on_demand
        # 节点池节点数据盘配置。
        self.data_disks = data_disks
        # 部署集ID。
        self.deploymentset_id = deploymentset_id
        # 节点池期望节点数量。
        self.desired_size = desired_size
        # 块设备初始化配置。
        self.disk_init = disk_init
        # 自定义镜像ID，默认使用系统提供的镜像。
        self.image_id = image_id
        # 操作系统镜像类型，和platform参数二选一，取值范围：
        # 
        # - `AliyunLinux`：Alinux2镜像。
        # - `AliyunLinux3`：Alinux3镜像。
        # - `AliyunLinux3Arm64`：Alinux3镜像ARM版。
        # - `AliyunLinuxUEFI`：Alinux2镜像UEFI版。
        # - `CentOS`：CentOS镜像。
        # - `Windows`：Windows镜像。
        # - `WindowsCore`：WindowsCore镜像。
        # - `ContainerOS`：容器优化镜像。
        self.image_type = image_type
        # 节点池节点付费类型，取值：
        # 
        # - `PrePaid`：预付费。
        # - `PostPaid`：按量付费。
        # 
        # 默认值：`PostPaid`。
        # 
        # This parameter is required.
        self.instance_charge_type = instance_charge_type
        # ECS 实例的元数据访问配置。
        # 目前仅白名单开放，需提交工单申请。
        self.instance_metadata_options = instance_metadata_options
        # 实例规格。
        # 
        # This parameter is required.
        self.instance_types = instance_types
        # 公网IP收费类型。取值：
        # 
        # - `PayByBandwidth`：按固定带宽计费。
        # - `PayByTraffic`：按使用流量计费。
        self.internet_charge_type = internet_charge_type
        # 节点公网IP出带宽最大值，单位为Mbps（Mega bit per second），取值范围：[1,100]
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # 密钥对名称，和`login_password`二选一。
        # 
        # > 如果创建托管节点池，则只支持`key_pair`。
        self.key_pair = key_pair
        # 弹出的ECS实例是否使用以非root用户登录。
        self.login_as_non_root = login_as_non_root
        # SSH登录密码，和`key_pair`二选一。密码规则为8~30个字符，且至少同时包含三项（大小写字母、数字和特殊符号）。
        self.login_password = login_password
        # 多可用区伸缩组ECS实例扩缩容策略。取值：
        # 
        # - `PRIORITY`：根据您定义的虚拟交换机（VSwitchIds.N）扩缩容。当优先级较高的虚拟交换机所在可用区无法创建ECS实例时，自动使用下一优先级的虚拟交换机创建ECS实例。
        # 
        # - `COST_OPTIMIZED`：按vCPU单价从低到高进行尝试创建。当伸缩配置设置了抢占式计费方式的多实例规格时，优先创建对应抢占式实例。您可以继续通过`CompensateWithOnDemand`参数指定当抢占式实例由于库存等原因无法创建时，是否自动尝试以按量付费的方式创建。
        # 
        #   >`COST_OPTIMIZED`仅在伸缩配置设置了多实例规格或者选用了抢占式实例的情况下生效。
        # 
        # - `BALANCE`：在伸缩组指定的多可用区之间均匀分配ECS实例。如果由于库存不足等原因可用区之间变得不平衡，您可以通过API RebalanceInstances平衡资源。更多信息，请参见[RebalanceInstances](https://help.aliyun.com/document_detail/71516.html)。
        # 
        # 默认值：`PRIORITY`。
        self.multi_az_policy = multi_az_policy
        # 伸缩组所需要按量实例个数的最小值，取值范围：[0,1000]。当按量实例个数少于该值时，将优先创建按量实例。
        self.on_demand_base_capacity = on_demand_base_capacity
        # 伸缩组满足最小按量实例数（`on_demand_base_capacity`）要求后，超出的实例中按量实例应占的比例。取值范围：[0,100]。
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # 节点池节点包年包月时长，当`instance_charge_type`取值为`PrePaid`时才生效且为必选值，取值范围：`period_unit`取值为Month时，`period`取值范围：{ 1, 2, 3, 6, 12}。
        # 
        # 默认值：1。
        self.period = period
        # 节点池节点付费周期，当`instance_charge_type`取值为`PrePaid`时需要指定周期。
        # 
        # `Month`：目前只支持以月为单位。
        self.period_unit = period_unit
        # 操作系统发行版。取值：
        # 
        # - `CentOS`
        # - `AliyunLinux`
        # - `Windows`
        # - `WindowsCore`
        # 
        # 默认值：`AliyunLinux`。
        self.platform = platform
        # 私有节点池配置。
        self.private_pool_options = private_pool_options
        # Worker RAM角色名称。
        # >Notice: 仅1.22及以上版本的ACK托管集群支持在创建节点池时配置该参数
        self.ram_role_name = ram_role_name
        # RDS实例列表。
        self.rds_instances = rds_instances
        # 创建实例时使用的资源池及资源池策略。当您设置该参数后，需要注意：
        # 该参数只在创建按量付费实例时生效。
        # 该参数不能与private_pool_options.match_criteria、private_pool_options.id同时设置。
        self.resource_pool_options = resource_pool_options
        # 伸缩组模式，取值：
        # 
        # - `release`：标准模式，根据申请资源值的使用量，通过创建、释放ECS的方式进行伸缩。
        # - `recycle`：极速模式，通过创建、停机、启动的方式进行伸缩，提高再次伸缩的速度（停机时计算资源不收费，只收取存储费用，本地盘机型除外）。
        # 
        # 默认值：`release`。
        self.scaling_policy = scaling_policy
        # 节点池安全组ID，与`security_group_ids`二选一，推荐使用`security_group_ids`。
        self.security_group_id = security_group_id
        # 安全组ID列表，与`security_group_id`二选一，推荐使用`security_group_ids`，当同时指定`security_group_id`和`security_group_ids`将优先使用`security_group_ids`。
        self.security_group_ids = security_group_ids
        # 指定可用实例规格的个数，伸缩组将按成本最低的多个规格均衡创建抢占式实例。取值范围：[1,10]。
        self.spot_instance_pools = spot_instance_pools
        # 是否开启补齐抢占式实例。开启后，当收到抢占式实例将被回收的系统消息时，伸缩组将尝试创建新的实例，替换掉将被回收的抢占式实例。取值：
        # 
        # - `true`：开启补齐抢占式实例。
        # - `false`：不开启补齐抢占式实例。
        self.spot_instance_remedy = spot_instance_remedy
        # 当前单台抢占式实例规格市场价格区间配置。
        self.spot_price_limit = spot_price_limit
        # 抢占式实例类型，取值：
        # - NoSpot：非抢占式实例。
        # - SpotWithPriceLimit：设置抢占实例价格上限。
        # - SpotAsPriceGo：系统自动出价，跟随当前市场实际价格。
        # 
        # 更多信息，请参见[抢占式实例](https://help.aliyun.com/document_detail/157759.html)。
        self.spot_strategy = spot_strategy
        # 节点系统盘是否开启Burst（性能突发）。 取值：
        # 
        # - true：是。
        # - false：否。
        # 
        # 当`SystemDiskCategory`取值为`cloud_auto`时才支持设置该参数。更多信息，请参见[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)。
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # 系统盘的多磁盘类型。当无法使用高优先级的磁盘类型时，自动尝试下一优先级的磁盘类型创建系统盘。取值范围：
        # 
        # - cloud：普通云盘。
        # - cloud_efficiency：高效云盘。
        # - cloud_ssd：SSD云盘。
        # - cloud_essd：ESSD云盘。
        self.system_disk_categories = system_disk_categories
        # 节点系统盘类型，取值：
        # 
        # - `cloud_efficiency`：高效云盘。
        # - `cloud_ssd`：SSD云盘。
        # - `cloud_essd`：ESSD云盘。
        # - `cloud_auto`：ESSD AutoPL云盘。
        # - `cloud_essd_entry`：ESSD Entry云盘。
        # 
        # 默认值：`cloud_efficiency`。
        self.system_disk_category = system_disk_category
        # 节点系统盘采用的加密算法。取值范围：aes-256。
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # 是否加密系统盘。取值范围：true：加密。false：不加密。
        self.system_disk_encrypted = system_disk_encrypted
        # 节点系统盘使用的KMS密钥ID。
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # 节点系统盘磁盘性能，只对ESSD磁盘生效。
        # 
        # - PL0：并发极限I/O性能中等，读写时延较为稳定。
        # - PL1：并发极限I/O性能中等，读写时延较为稳定。
        # - PL2：并发极限I/O性能较高，读写时延稳定。
        # - PL3：并发极限I/O性能极高，读写时延极稳定。
        self.system_disk_performance_level = system_disk_performance_level
        # 节点系统盘预配置的读写IOPS。可能值：0~min{50,000, 1000\\*容量-基准性能}。 基准性能=min{1,800+50\\*容量, 50000}。
        # 
        # 当`SystemDiskCategory`为`cloud_auto`时才支持设置该参数。更多信息，请参见[ESSD AutoPL云盘](https://help.aliyun.com/document_detail/368372.html)。
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # 节点系统盘大小，单位：GiB。
        # 
        # 取值范围：[40,500]。
        self.system_disk_size = system_disk_size
        # 仅为ECS实例添加标签。
        # 
        # 标签键不可以重复，最大长度为128个字符；标签键和标签值都不能以“aliyun”、“acs:”开头，或包含“https://”、“http://”。
        self.tags = tags
        # 虚拟交换机ID。
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
        # 标签的名称。
        self.key = key
        # 标签值。
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
        # 抢占式实例规格。
        self.instance_type = instance_type
        # 单台实例上限价格。
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
        # 私有池 ID列表。即弹性保障服务 ID 或容量预定服务 ID。该参数只能传入 Target 模式私有池 ID。N 的取值范围：1~20。
        self.private_pool_ids = private_pool_ids
        # 创建实例时使用的资源池策略。资源池包括弹性保障服务或容量预定服务生效后生成的私有池以及公共池，供实例启动时选择。取值范围：
        # PrivatePoolFirst：私有池优先。选择此种策略时， 当指定了 resource_pool_options.private_pool_ids，优先使用指定的私有池。如果未指定私有池或指定的私有池容量不足，将自动匹配开放类型的私有池。如果没有符合条件的私有池，则使用公共池创建实例。
        # PrivatePoolOnly：仅限私有池。选择此种策略时，必须指定 resource_pool_options.private_pool_ids。如果指定的私有池容量不足，则实例会启动失败。
        # None：不使用资源池策略。
        # 默认值：None。
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
        # 私有节点池ID。
        self.id = id
        # 私有节点池类型，实例启动的私有池容量选项。弹性保障服务或容量预定服务在生效后会生成私有池容量，供实例启动时选择。取值：
        # 
        # - `Open`：开放模式。将自动匹配开放类型的私有池容量。如果没有符合条件的私有池容量，则使用公共池资源启动。
        # 
        # - `Target`：指定模式。使用指定的私有池容量启动实例，如果该私有池容量不可用，则实例会启动失败。
        # 
        # - `None`：不使用模式。实例启动将不使用私有池容量。
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

class NodepoolNodepoolInfo(DaraModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # 节点池名称。
        # 
        # This parameter is required.
        self.name = name
        # 节点池所在资源ID。
        self.resource_group_id = resource_group_id
        # 节点池类型，取值范围：
        # 
        # - `ess`：节点池。
        # - `edge`：边缘节点池。
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
        # Kubelet参数配置。
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
        # 节点组件配置。
        self.config = config
        # 节点组件名称。
        self.name = name
        # 节点组件版本
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
        custom_config: Dict[str, str] = None,
    ):
        # 节点组件自定义配置。
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
        enable: bool = None,
        upgrade_config: main_models.NodepoolManagementUpgradeConfig = None,
    ):
        self.auto_fault_diagnosis = auto_fault_diagnosis
        # 自动修复，仅当`enable=true`时生效。
        # 
        # - `true`：自动修复。
        # - `false`：不自动修复。
        self.auto_repair = auto_repair
        # 自动修复节点策略。
        self.auto_repair_policy = auto_repair_policy
        # 是否自动升级。
        self.auto_upgrade = auto_upgrade
        # 自动升级策略。
        self.auto_upgrade_policy = auto_upgrade_policy
        # 是否自动修复CVE。
        self.auto_vul_fix = auto_vul_fix
        # 自动修复CVE策略。
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # 是否开启托管版节点池，取值：
        # 
        # - `true`：开启托管节点池。
        # - `false`：不开启托管节点池，只有当`enable=true`时，其他相关配置才生效。
        self.enable = enable
        # 自动升级配置，仅当`enable=true`时生效。
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
        # 是否启用自动升级，取值：
        # 
        # - `true`：启用自动升级。
        # - `false`：不启用自动升级。
        self.auto_upgrade = auto_upgrade
        # 最大不可用节点数量，取值范围：[1,1000\\]。
        # 
        # 默认值：1。
        self.max_unavailable = max_unavailable
        # 额外节点数量。
        self.surge = surge
        # 额外节点比例，和`surge`二选一。
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
        # 是否允许重启节点。
        self.restart_node = restart_node
        # 允许自动修复的漏洞级别，以逗号分隔。
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
        # 是否允许自动升级kubelet。
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
        restart_node: bool = None,
    ):
        # 是否允许重启节点。
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        # 是否在ECS节点上安装云监控，安装后可以在云监控控制台查看所创建ECS实例的监控信息，推荐开启。取值：
        # 
        # - `true`：在ECS节点上安装云监控。
        # - `false`：不在ECS节点上安装云监控。
        # 
        # 默认值：`false`。
        self.cms_enabled = cms_enabled
        # 节点CPU管理策略。当集群版本在1.12.6及以上时支持以下两种策略：
        # 
        # - `static`：允许为节点上具有某些资源特征Pod增强其CPU亲和性和独占性。
        # - `none`：表示启用现有的默认CPU亲和性方案。
        # 
        # 默认值：`none`。
        self.cpu_policy = cpu_policy
        # 节点标签，为Kubernetes集群节点添加标签。
        self.labels = labels
        # 节点名称由三部分组成：前缀 + 节点 IP + 后缀：
        # 
        # - 前缀和后缀均可由“.”分隔的一个或多个部分构成，每个部分可以使用小写字母、数字和“-”，节点名称首尾必须为小写字母和数字；
        # - 节点 IP为完整的节点私网 IP 地址；
        # 
        # 传参包含四个部分，由逗号分隔，例如：参数传入"customized,aliyun,ip,com"字符串（其中“customized”和"ip"为固定的字符串，aliyun为前缀，com为后缀），则节点的名称为：aliyun.192.168.xxx.xxx.com。
        self.node_name_mode = node_name_mode
        # 容器运行时。取值：
        # - `containerd`：推荐使用，支持所有集群版本。
        # - `Sandboxed-Container.runv`：安全沙箱容器，提供更高的隔离性，支持1.24版本及以下集群。
        # - `docker`：支持1.22版本及以下集群。
        # 
        # 默认值：`containerd`
        # 
        # This parameter is required.
        self.runtime = runtime
        # 容器运行时版本。
        # 
        # This parameter is required.
        self.runtime_version = runtime_version
        # 污点配置。
        self.taints = taints
        # 节点自定义数据。
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
        # 【该字段已废弃】
        # 
        # 边缘增强型节点池的网络带宽，单位：Mbps。
        self.bandwidth = bandwidth
        # 【该字段已废弃】
        # 
        # 边缘增强型节点池绑定的云连接网实例ID(CCNID)。
        self.ccn_id = ccn_id
        # 【该字段已废弃】
        # 
        # 边缘增强型节点池绑定的云连接网实例所属的地域。
        self.ccn_region_id = ccn_region_id
        # 【该字段已废弃】
        # 
        # 边缘增强型节点池绑定的云企业网实例ID(CENID)。
        self.cen_id = cen_id
        # 【该字段已废弃】
        # 
        # 边缘增强型节点池的购买时长，单位：月。
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
        # 【该字段已废弃】
        # 
        # EIP带宽峰值。单位：Mbps。
        self.eip_bandwidth = eip_bandwidth
        # 【该字段已废弃】
        # 
        # EIP计费类型，取值：
        # 
        # - `PayByBandwidth`：按固定带宽计费。
        # - `PayByTraffic`：按使用流量计费。
        # 
        # 默认值：PayByBandwidth。
        self.eip_internet_charge_type = eip_internet_charge_type
        # 是否启用自动伸缩。
        # 
        # - `true`：开启节点池自动伸缩功能。
        # - `false`：不开启自动伸缩，当取值为false时，`auto_scaling`内的其他配置参数将不生效。
        # 
        # 默认值：`false`。
        # 
        # This parameter is required.
        self.enable = enable
        # 【该字段已废弃】
        # 
        # 是否绑定EIP，取值：
        # 
        # - `true`：绑定EIP。
        # - `false`：不绑定EIP。
        # 
        # 默认值：`false`。
        self.is_bond_eip = is_bond_eip
        # 自动伸缩组最大实例数。
        # 
        # This parameter is required.
        self.max_instances = max_instances
        # 自动伸缩组最小实例数。
        # 
        # This parameter is required.
        self.min_instances = min_instances
        # 自动伸缩类型，按照自动伸缩实例类型划分。取值：
        # 
        # - `cpu`：普通实例型。
        # - `gpu`：GPU实例型。
        # - `gpushare`：GPU共享型。
        # - `spot`：抢占式实例型。
        # 
        # 默认值：`cpu`。
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

