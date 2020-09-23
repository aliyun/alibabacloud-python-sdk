# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AttachInstancesRequest(TeaModel):
    def __init__(self, instances=None, runtime=None, image_id=None, format_disk=None, keep_instance_name=None,
                 cpu_policy=None, key_pair=None, password=None, is_edge_worker=None, user_data=None, nodepool_id=None,
                 rds_instances=None, tags=None):
        # 待添加的实例列表。
        self.instances = instances      # type: List[str]
        # 容器运行时。
        self.runtime = runtime          # type: AttachInstancesRequestRuntime
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # 是否格式化数据盘。
        self.format_disk = format_disk  # type: bool
        # 是否保留实例名称。
        self.keep_instance_name = keep_instance_name  # type: bool
        # CPU策略。
        self.cpu_policy = cpu_policy    # type: str
        # key_pair名称，与login_password二选一
        self.key_pair = key_pair        # type: str
        # password，与key_pair二选一。
        self.password = password        # type: str
        # 是否为边缘节点。
        self.is_edge_worker = is_edge_worker  # type: bool
        # 用户自定义数据。
        self.user_data = user_data      # type: str
        # 节点池ID，欲将节点添加到哪个节点池中。。
        self.nodepool_id = nodepool_id  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 节点标签。
        self.tags = tags                # type: List[AttachInstancesRequestTags]

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['instances'] = self.instances
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        else:
            result['runtime'] = None
        result['image_id'] = self.image_id
        result['format_disk'] = self.format_disk
        result['keep_instance_name'] = self.keep_instance_name
        result['cpu_policy'] = self.cpu_policy
        result['key_pair'] = self.key_pair
        result['password'] = self.password
        result['is_edge_worker'] = self.is_edge_worker
        result['user_data'] = self.user_data
        result['nodepool_id'] = self.nodepool_id
        result['rds_instances'] = self.rds_instances
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        return result

    def from_map(self, map={}):
        self.instances = map.get('instances')
        if map.get('runtime') is not None:
            temp_model = AttachInstancesRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        else:
            self.runtime = None
        self.image_id = map.get('image_id')
        self.format_disk = map.get('format_disk')
        self.keep_instance_name = map.get('keep_instance_name')
        self.cpu_policy = map.get('cpu_policy')
        self.key_pair = map.get('key_pair')
        self.password = map.get('password')
        self.is_edge_worker = map.get('is_edge_worker')
        self.user_data = map.get('user_data')
        self.nodepool_id = map.get('nodepool_id')
        self.rds_instances = map.get('rds_instances')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = AttachInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        return self


class AttachInstancesRequestRuntime(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器运行时名称。
        self.name = name                # type: str
        # 容器运行时版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.version = map.get('version')
        return self


class AttachInstancesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(self, list=None, task_id=None):
        # 节点信息列表。
        self.list = list                # type: List[AttachInstancesResponseBodyList]
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        else:
            result['list'] = None
        result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = AttachInstancesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        else:
            self.list = None
        self.task_id = map.get('task_id')
        return self


class AttachInstancesResponseBodyList(TeaModel):
    def __init__(self, code=None, instance_id=None, message=None):
        # 状态码。
        self.code = code                # type: str
        # 实例ID。
        self.instance_id = instance_id  # type: str
        # 添加结果描述。
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['code'] = self.code
        result['instanceId'] = self.instance_id
        result['message'] = self.message
        return result

    def from_map(self, map={}):
        self.code = map.get('code')
        self.instance_id = map.get('instanceId')
        self.message = map.get('message')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: AttachInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CancelClusterUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CancelComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, name=None, cluster_type=None, region_id=None, zone_id=None, kubernetes_version=None,
                 deletion_protection=None, runtime=None, vpcid=None, worker_vswitch_ids=None, container_cidr=None, service_cidr=None,
                 node_cidr_mask=None, snat_entry=None, endpoint_public_access=None, ssh_flags=None, rds_instances=None,
                 security_group_id=None, is_enterprise_security_group=None, proxy_mode=None, tags=None, images_id=None,
                 master_instance_charge_type=None, master_period=None, master_period_unit=None, master_auto_renew=None,
                 master_auto_renew_period=None, master_count=None, master_vswitch_ids=None, master_instance_types=None,
                 master_system_disk_category=None, master_system_disk_size=None, worker_instance_charge_type=None, worker_period=None,
                 worker_period_unit=None, worker_auto_renew=None, worker_auto_renew_period=None, num_of_nodes=None,
                 worker_instance_types=None, worker_system_disk_category=None, worker_system_disk_size=None, worker_data_disks=None,
                 os_type=None, key_pair=None, login_password=None, user_data=None, node_port_range=None, cpu_policy=None,
                 taints=None, cloud_monitor_flags=None, addons=None, platform=None, vswitch_ids=None, private_zone=None,
                 profile=None, pod_vswitch_ids=None, disable_rollback=None, timeout_mins=None):
        # 集群名称。
        self.name = name                # type: str
        # 集群类型
        self.cluster_type = cluster_type  # type: str
        # 集群所属地域ID。
        self.region_id = region_id      # type: str
        # 集群所属地域内的可用区ID。
        self.zone_id = zone_id          # type: str
        # 集群版本好。
        self.kubernetes_version = kubernetes_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: str
        # 容器运行时。
        self.runtime = runtime          # type: CreateClusterRequestRuntime
        # 集群使用的VPC。
        self.vpcid = vpcid              # type: str
        # 集群使用的虚拟交换机。
        self.worker_vswitch_ids = worker_vswitch_ids  # type: List[str]
        # POD网络地址段。
        self.container_cidr = container_cidr  # type: str
        # Service网络地址段。
        self.service_cidr = service_cidr  # type: str
        # 节点IP数量，这里通过CIDR来指定。
        self.node_cidr_mask = node_cidr_mask  # type: str
        # 集群是否配置SNAT。
        self.snat_entry = snat_entry    # type: bool
        # 集群是否运行公网访问。
        self.endpoint_public_access = endpoint_public_access  # type: bool
        # 集群是否开启公网SSH登录。
        self.ssh_flags = ssh_flags      # type: bool
        # RDS列表，将该ECS加入到选择的RDS实例的白名单中。。
        self.rds_instances = rds_instances  # type: List[str]
        # 自定义安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 是否自动创建企业安全组，与security_group_id二选一。
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # kube-proxy代理模式。
        self.proxy_mode = proxy_mode    # type: str
        # 集群标签。
        self.tags = tags                # type: List[CreateClusterRequestTags]
        # 自定义镜像ID。
        self.images_id = images_id      # type: str
        # Master节点付费类型。
        self.master_instance_charge_type = master_instance_charge_type  # type: str
        # Master节点包年包月时长，当master_instance_charge_type取值为PrePaid时才生效且为必选值。
        self.master_period = master_period  # type: int
        # Master节点包年包月周期。
        self.master_period_unit = master_period_unit  # type: str
        # Master节点是否自动续费。
        self.master_auto_renew = master_auto_renew  # type: bool
        # Master节点自动续费周期。
        self.master_auto_renew_period = master_auto_renew_period  # type: int
        # Master节点数量。
        self.master_count = master_count  # type: int
        # Master节点交换机ID列表。
        self.master_vswitch_ids = master_vswitch_ids  # type: List[str]
        # Master节点ECS规格类型。
        self.master_instance_types = master_instance_types  # type: List[str]
        # Master节点系统盘类型。
        self.master_system_disk_category = master_system_disk_category  # type: str
        # Master节点系统盘大小。
        self.master_system_disk_size = master_system_disk_size  # type: int
        # Worker节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # Worker节点包年包月周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # Worker节点是否自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # Worker节点自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # Worker节点数量。
        self.num_of_nodes = num_of_nodes  # type: int
        # Worker节点ECS实例类型。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # Worker节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # Worker节点系统盘大小。
        self.worker_system_disk_size = worker_system_disk_size  # type: int
        # Worker节点数据盘配置。
        self.worker_data_disks = worker_data_disks  # type: List[CreateClusterRequestWorkerDataDisks]
        # 操作系统。
        self.os_type = os_type          # type: str
        # key_pair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码，与key_pair二选一。
        self.login_password = login_password  # type: str
        # 节点用户自定义数据。
        self.user_data = user_data      # type: str
        # 节点服务端口范围。
        self.node_port_range = node_port_range  # type: str
        # CPU管理策略。
        self.cpu_policy = cpu_policy    # type: str
        # 污点信息。
        self.taints = taints            # type: List[CreateClusterRequestTaints]
        # 是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 组件信息。
        self.addons = addons            # type: List[CreateClusterRequestAddons]
        # 操作系统发行版。
        self.platform = platform        # type: str
        # 虚拟交换机列表。List长度范围为[1，3]。当集群类型为托管版或标准serverless集群时，该参数必填。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # 是否开启PrivateZone用于服务发现。
        self.private_zone = private_zone  # type: bool
        # 边缘集群标识。
        self.profile = profile          # type: str
        # Pod的虚拟交换机列表，在ENI多网卡模式下，需要传额外的VSwitch ID给addon。
        self.pod_vswitch_ids = pod_vswitch_ids  # type: List[str]
        # 集群创建失败后是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 集群创建超时时间。
        self.timeout_mins = timeout_mins  # type: int

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['cluster_type'] = self.cluster_type
        result['region_id'] = self.region_id
        result['zone_id'] = self.zone_id
        result['kubernetes_version'] = self.kubernetes_version
        result['deletion_protection'] = self.deletion_protection
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        else:
            result['runtime'] = None
        result['vpcid'] = self.vpcid
        result['worker_vswitch_ids'] = self.worker_vswitch_ids
        result['container_cidr'] = self.container_cidr
        result['service_cidr'] = self.service_cidr
        result['node_cidr_mask'] = self.node_cidr_mask
        result['snat_entry'] = self.snat_entry
        result['endpoint_public_access'] = self.endpoint_public_access
        result['ssh_flags'] = self.ssh_flags
        result['rds_instances'] = self.rds_instances
        result['security_group_id'] = self.security_group_id
        result['is_enterprise_security_group'] = self.is_enterprise_security_group
        result['proxy_mode'] = self.proxy_mode
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['images_id'] = self.images_id
        result['master_instance_charge_type'] = self.master_instance_charge_type
        result['master_period'] = self.master_period
        result['master_period_unit'] = self.master_period_unit
        result['master_auto_renew'] = self.master_auto_renew
        result['master_auto_renew_period'] = self.master_auto_renew_period
        result['master_count'] = self.master_count
        result['master_vswitch_ids'] = self.master_vswitch_ids
        result['master_instance_types'] = self.master_instance_types
        result['master_system_disk_category'] = self.master_system_disk_category
        result['master_system_disk_size'] = self.master_system_disk_size
        result['worker_instance_charge_type'] = self.worker_instance_charge_type
        result['worker_period'] = self.worker_period
        result['worker_period_unit'] = self.worker_period_unit
        result['worker_auto_renew'] = self.worker_auto_renew
        result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['num_of_nodes'] = self.num_of_nodes
        result['worker_instance_types'] = self.worker_instance_types
        result['worker_system_disk_category'] = self.worker_system_disk_category
        result['worker_system_disk_size'] = self.worker_system_disk_size
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        else:
            result['worker_data_disks'] = None
        result['os_type'] = self.os_type
        result['key_pair'] = self.key_pair
        result['login_password'] = self.login_password
        result['user_data'] = self.user_data
        result['node_port_range'] = self.node_port_range
        result['cpu_policy'] = self.cpu_policy
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        else:
            result['taints'] = None
        result['cloud_monitor_flags'] = self.cloud_monitor_flags
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        else:
            result['addons'] = None
        result['platform'] = self.platform
        result['vswitch_ids'] = self.vswitch_ids
        result['private_zone'] = self.private_zone
        result['profile'] = self.profile
        result['pod_vswitch_ids'] = self.pod_vswitch_ids
        result['disable_rollback'] = self.disable_rollback
        result['timeout_mins'] = self.timeout_mins
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.cluster_type = map.get('cluster_type')
        self.region_id = map.get('region_id')
        self.zone_id = map.get('zone_id')
        self.kubernetes_version = map.get('kubernetes_version')
        self.deletion_protection = map.get('deletion_protection')
        if map.get('runtime') is not None:
            temp_model = CreateClusterRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        else:
            self.runtime = None
        self.vpcid = map.get('vpcid')
        self.worker_vswitch_ids = map.get('worker_vswitch_ids')
        self.container_cidr = map.get('container_cidr')
        self.service_cidr = map.get('service_cidr')
        self.node_cidr_mask = map.get('node_cidr_mask')
        self.snat_entry = map.get('snat_entry')
        self.endpoint_public_access = map.get('endpoint_public_access')
        self.ssh_flags = map.get('ssh_flags')
        self.rds_instances = map.get('rds_instances')
        self.security_group_id = map.get('security_group_id')
        self.is_enterprise_security_group = map.get('is_enterprise_security_group')
        self.proxy_mode = map.get('proxy_mode')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = CreateClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.images_id = map.get('images_id')
        self.master_instance_charge_type = map.get('master_instance_charge_type')
        self.master_period = map.get('master_period')
        self.master_period_unit = map.get('master_period_unit')
        self.master_auto_renew = map.get('master_auto_renew')
        self.master_auto_renew_period = map.get('master_auto_renew_period')
        self.master_count = map.get('master_count')
        self.master_vswitch_ids = map.get('master_vswitch_ids')
        self.master_instance_types = map.get('master_instance_types')
        self.master_system_disk_category = map.get('master_system_disk_category')
        self.master_system_disk_size = map.get('master_system_disk_size')
        self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        self.worker_period = map.get('worker_period')
        self.worker_period_unit = map.get('worker_period_unit')
        self.worker_auto_renew = map.get('worker_auto_renew')
        self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        self.num_of_nodes = map.get('num_of_nodes')
        self.worker_instance_types = map.get('worker_instance_types')
        self.worker_system_disk_category = map.get('worker_system_disk_category')
        self.worker_system_disk_size = map.get('worker_system_disk_size')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = CreateClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        else:
            self.worker_data_disks = None
        self.os_type = map.get('os_type')
        self.key_pair = map.get('key_pair')
        self.login_password = map.get('login_password')
        self.user_data = map.get('user_data')
        self.node_port_range = map.get('node_port_range')
        self.cpu_policy = map.get('cpu_policy')
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = CreateClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        else:
            self.taints = None
        self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        self.addons = []
        if map.get('addons') is not None:
            for k in map.get('addons'):
                temp_model = CreateClusterRequestAddons()
                self.addons.append(temp_model.from_map(k))
        else:
            self.addons = None
        self.platform = map.get('platform')
        self.vswitch_ids = map.get('vswitch_ids')
        self.private_zone = map.get('private_zone')
        self.profile = map.get('profile')
        self.pod_vswitch_ids = map.get('pod_vswitch_ids')
        self.disable_rollback = map.get('disable_rollback')
        self.timeout_mins = map.get('timeout_mins')
        return self


class CreateClusterRequestRuntime(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器运行时名称。
        self.name = name                # type: str
        # 容器运行时版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.version = map.get('version')
        return self


class CreateClusterRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签key。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class CreateClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, auto_snapshot_policy_id=None, category=None, encrypted=None, size=None):
        # 数据盘是否开启云盘备份。
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str
        # 数据盘类型。
        self.category = category        # type: str
        # 数据盘是否加密。
        self.encrypted = encrypted      # type: str
        # 数据盘大小。
        self.size = size                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        result['category'] = self.category
        result['encrypted'] = self.encrypted
        result['size'] = self.size
        return result

    def from_map(self, map={}):
        self.auto_snapshot_policy_id = map.get('auto_snapshot_policy_id')
        self.category = map.get('category')
        self.encrypted = map.get('encrypted')
        self.size = map.get('size')
        return self


class CreateClusterRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # 调度策略。
        self.effect = effect            # type: str
        # 污点key。
        self.key = key                  # type: str
        # 污点值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['effect'] = self.effect
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.effect = map.get('effect')
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class CreateClusterRequestAddons(TeaModel):
    def __init__(self, config=None, name=None):
        # 组件需要的配置。
        self.config = config            # type: str
        # 组件名称。
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['config'] = self.config
        result['name'] = self.name
        return result

    def from_map(self, map={}):
        self.config = map.get('config')
        self.name = map.get('name')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 请求ID。
        self.request_id = request_id    # type: str
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['request_id'] = self.request_id
        result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.request_id = map.get('request_id')
        self.task_id = map.get('task_id')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class CreateKubernetesTriggerRequest(TeaModel):
    def __init__(self, region_id=None, cluster_id=None, project_id=None, type=None):
        # 地域ID。
        self.region_id = region_id      # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 项目名称。
        self.project_id = project_id    # type: str
        # 触发器类型。
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['RegionId'] = self.region_id
        result['ClusterId'] = self.cluster_id
        result['ProjectId'] = self.project_id
        result['Type'] = self.type
        return result

    def from_map(self, map={}):
        self.region_id = map.get('RegionId')
        self.cluster_id = map.get('ClusterId')
        self.project_id = map.get('ProjectId')
        self.type = map.get('Type')
        return self


class CreateKubernetesTriggerResponseBody(TeaModel):
    def __init__(self, action=None, cluster_id=None, id=None, project_id=None):
        # 触发器行为。
        self.action = action            # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 触发器ID。
        self.id = id                    # type: str
        # 项目名称。
        self.project_id = project_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['action'] = self.action
        result['cluster_id'] = self.cluster_id
        result['id'] = self.id
        result['project_id'] = self.project_id
        return result

    def from_map(self, map={}):
        self.action = map.get('action')
        self.cluster_id = map.get('cluster_id')
        self.id = map.get('id')
        self.project_id = map.get('project_id')
        return self


class CreateKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateKubernetesTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, retain_resources=None):
        # 要保留的资源列表。
        self.retain_resources = retain_resources  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['retain_resources'] = self.retain_resources
        return result

    def from_map(self, map={}):
        self.retain_resources = map.get('retain_resources')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DeleteKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeAddonsRequest(TeaModel):
    def __init__(self, region=None, cluster_type=None):
        # Region ID。
        self.region = region            # type: str
        # 集群类型，默认为kubernetes。
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['region'] = self.region
        result['cluster_type'] = self.cluster_type
        return result

    def from_map(self, map={}):
        self.region = map.get('region')
        self.cluster_type = map.get('cluster_type')
        return self


class DescribeAddonsResponseBody(TeaModel):
    def __init__(self, component_groups=None, standard_components=None):
        # 组件分组信息，例如：存储类组件，网络组件等。
        self.component_groups = component_groups  # type: List[DescribeAddonsResponseBodyComponentGroups]
        # 标准组件信息，包含各个组件的描述信息。
        self.standard_components = standard_components  # type: DescribeAddonsResponseBodyStandardComponents

    def validate(self):
        if self.component_groups:
            for k in self.component_groups:
                if k:
                    k.validate()
        if self.standard_components:
            self.standard_components.validate()

    def to_map(self):
        result = {}
        result['ComponentGroups'] = []
        if self.component_groups is not None:
            for k in self.component_groups:
                result['ComponentGroups'].append(k.to_map() if k else None)
        else:
            result['ComponentGroups'] = None
        if self.standard_components is not None:
            result['StandardComponents'] = self.standard_components.to_map()
        else:
            result['StandardComponents'] = None
        return result

    def from_map(self, map={}):
        self.component_groups = []
        if map.get('ComponentGroups') is not None:
            for k in map.get('ComponentGroups'):
                temp_model = DescribeAddonsResponseBodyComponentGroups()
                self.component_groups.append(temp_model.from_map(k))
        else:
            self.component_groups = None
        if map.get('StandardComponents') is not None:
            temp_model = DescribeAddonsResponseBodyStandardComponents()
            self.standard_components = temp_model.from_map(map['StandardComponents'])
        else:
            self.standard_components = None
        return self


class DescribeAddonsResponseBodyComponentGroupsItems(TeaModel):
    def __init__(self, description=None, disabled=None, name=None, required=None, version=None):
        # 组件描述信息。
        self.description = description  # type: str
        # 是否禁止默认安装。
        self.disabled = disabled        # type: bool
        # 组件名称。
        self.name = name                # type: str
        # 是否为必需组件。
        self.required = required        # type: str
        # 组件版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['description'] = self.description
        result['disabled'] = self.disabled
        result['name'] = self.name
        result['required'] = self.required
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.description = map.get('description')
        self.disabled = map.get('disabled')
        self.name = map.get('name')
        self.required = map.get('required')
        self.version = map.get('version')
        return self


class DescribeAddonsResponseBodyComponentGroups(TeaModel):
    def __init__(self, default=None, group_name=None, items=None):
        # 默认组件组。
        self.default = default          # type: List[str]
        # 组件组名称。
        self.group_name = group_name    # type: str
        # 组件清单。
        self.items = items              # type: List[DescribeAddonsResponseBodyComponentGroupsItems]

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['default'] = self.default
        result['group_name'] = self.group_name
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        else:
            result['items'] = None
        return result

    def from_map(self, map={}):
        self.default = map.get('default')
        self.group_name = map.get('group_name')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = DescribeAddonsResponseBodyComponentGroupsItems()
                self.items.append(temp_model.from_map(k))
        else:
            self.items = None
        return self


class DescribeAddonsResponseBodyStandardComponents(TeaModel):
    def __init__(self, component_name=None):
        # 组件名称。
        self.component_name = component_name  # type: Dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ComponentName'] = self.component_name
        return result

    def from_map(self, map={}):
        self.component_name = map.get('ComponentName')
        return self


class DescribeAddonsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeAddonsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeAddonsResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterAddonUpgradeStatusResponseBody(TeaModel):
    def __init__(self, addon_info=None, can_upgrade=None, template=None):
        # 组件信息。
        self.addon_info = addon_info    # type: DescribeClusterAddonUpgradeStatusResponseBodyAddonInfo
        # 是否能够升级。
        self.can_upgrade = can_upgrade  # type: bool
        # 模板信息，采用base64加密。
        self.template = template        # type: str

    def validate(self):
        if self.addon_info:
            self.addon_info.validate()

    def to_map(self):
        result = {}
        if self.addon_info is not None:
            result['addon_info'] = self.addon_info.to_map()
        else:
            result['addon_info'] = None
        result['can_upgrade'] = self.can_upgrade
        result['template'] = self.template
        return result

    def from_map(self, map={}):
        if map.get('addon_info') is not None:
            temp_model = DescribeClusterAddonUpgradeStatusResponseBodyAddonInfo()
            self.addon_info = temp_model.from_map(map['addon_info'])
        else:
            self.addon_info = None
        self.can_upgrade = map.get('can_upgrade')
        self.template = map.get('template')
        return self


class DescribeClusterAddonUpgradeStatusResponseBodyAddonInfo(TeaModel):
    def __init__(self, category=None, component_name=None, message=None, version=None, yaml=None):
        # Addon类别。
        self.category = category        # type: str
        # 组件名称。
        self.component_name = component_name  # type: str
        # 升级说明信息。
        self.message = message          # type: str
        # 组件版本。
        self.version = version          # type: str
        # 组件配置文件。
        self.yaml = yaml                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['component_name'] = self.component_name
        result['message'] = self.message
        result['version'] = self.version
        result['yaml'] = self.yaml
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.component_name = map.get('component_name')
        self.message = map.get('message')
        self.version = map.get('version')
        self.yaml = map.get('yaml')
        return self


class DescribeClusterAddonUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterAddonUpgradeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterAddonUpgradeStatusResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterAddonsUpgradeStatusRequest(TeaModel):
    def __init__(self, component_ids=None):
        # 组件列表。
        self.component_ids = component_ids  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['componentIds'] = self.component_ids
        return result

    def from_map(self, map={}):
        self.component_ids = map.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class DescribeClusterAddonsVersionResponseBody(TeaModel):
    def __init__(self, addons_name=None):
        # 组件名称。
        self.addons_name = addons_name  # type: Dict[str, dict]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['AddonsName'] = self.addons_name
        return result

    def from_map(self, map={}):
        self.addons_name = map.get('AddonsName')
        return self


class DescribeClusterAddonsVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterAddonsVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterAddonsVersionResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterAttachScriptsRequest(TeaModel):
    def __init__(self, arch=None, options=None):
        # 节点CPU架构,支持amd64、arm、arm64。
        self.arch = arch                # type: str
        # 边缘托管版集群节点的接入配置。
        self.options = options          # type: DescribeClusterAttachScriptsRequestOptions

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = {}
        result['arch'] = self.arch
        if self.options is not None:
            result['options'] = self.options.to_map()
        else:
            result['options'] = None
        return result

    def from_map(self, map={}):
        self.arch = map.get('arch')
        if map.get('options') is not None:
            temp_model = DescribeClusterAttachScriptsRequestOptions()
            self.options = temp_model.from_map(map['options'])
        else:
            self.options = None
        return self


class DescribeClusterAttachScriptsRequestOptions(TeaModel):
    def __init__(self, allowed_cluster_addons=None, enable_iptables=None, flannel_iface=None, gpu_version=None,
                 manage_runtime=None, node_name_override=None, quiet=None):
        # 需要安装的组件列表，默认为空，不安装。
        self.allowed_cluster_addons = allowed_cluster_addons  # type: List[str]
        # 是否开启iptables，默认值true。
        self.enable_iptables = enable_iptables  # type: bool
        # flannel使用的网卡名。默认使用节点默认路由的网卡名。
        self.flannel_iface = flannel_iface  # type: str
        # 表示要接入的节点是否为GPU节点，默认为空。当前支持的GPU版本是Nvidia_Tesla_T4、Nvidia_Tesla_P4、Nvidia_Tesla_P100。
        self.gpu_version = gpu_version  # type: str
        # 是否由edgeadm安装并检测Runtime，默认false。
        self.manage_runtime = manage_runtime  # type: bool
        # 设置节点名。  - ""（默认值，表示使用主机名。） - "*"（表示随机生成6位的字符串。） - "*.XXX"（表示随机生成6位字符串+XXX后缀。）
        self.node_name_override = node_name_override  # type: str
        # 是否使用静默模式安装。
        self.quiet = quiet              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['allowedClusterAddons'] = self.allowed_cluster_addons
        result['enableIptables'] = self.enable_iptables
        result['flannelIface'] = self.flannel_iface
        result['gpuVersion'] = self.gpu_version
        result['manageRuntime'] = self.manage_runtime
        result['nodeNameOverride'] = self.node_name_override
        result['quiet'] = self.quiet
        return result

    def from_map(self, map={}):
        self.allowed_cluster_addons = map.get('allowedClusterAddons')
        self.enable_iptables = map.get('enableIptables')
        self.flannel_iface = map.get('flannelIface')
        self.gpu_version = map.get('gpuVersion')
        self.manage_runtime = map.get('manageRuntime')
        self.node_name_override = map.get('nodeNameOverride')
        self.quiet = map.get('quiet')
        return self


class DescribeClusterAttachScriptsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: str

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['body'] = self.body
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.body = map.get('body')
        return self


class DescribeClusterDetailResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, created=None, current_version=None,
                 deletion_protection=None, docker_version=None, external_loadbalancer_id=None, instance_type=None, meta_data=None,
                 name=None, network_mode=None, region_id=None, resource_group_id=None, security_group_id=None, size=None,
                 state=None, tags=None, updated=None, vpc_id=None, vswitch_cidr=None, vswitch_id=None, zone_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created          # type: str
        # 集群当前K8S版本。
        self.current_version = current_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群内Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingress SLB ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群实例类型。
        self.instance_type = instance_type  # type: str
        # 集群元数据。
        self.meta_data = meta_data      # type: str
        # 集群名称。
        self.name = name                # type: str
        # 集群采用的网络类型，例如：VPC网络。
        self.network_mode = network_mode  # type: str
        # 集群所在地域ID。
        self.region_id = region_id      # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群节点数量。
        self.size = size                # type: int
        # 集群运行状态。
        self.state = state              # type: str
        # 集群标签。
        self.tags = tags                # type: List[DescribeClusterDetailResponseBodyTags]
        # 集群更新时间。
        self.updated = updated          # type: str
        # 集群使用的VPC ID。
        self.vpc_id = vpc_id            # type: str
        # 集群使用的虚拟交换机ID。
        self.vswitch_cidr = vswitch_cidr  # type: str
        # 集群节点使用的虚拟交换机列表。
        self.vswitch_id = vswitch_id    # type: str
        # 集群所在地域内的可用区ID。
        self.zone_id = zone_id          # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['cluster_type'] = self.cluster_type
        result['created'] = self.created
        result['current_version'] = self.current_version
        result['deletion_protection'] = self.deletion_protection
        result['docker_version'] = self.docker_version
        result['external_loadbalancer_id'] = self.external_loadbalancer_id
        result['instance_type'] = self.instance_type
        result['meta_data'] = self.meta_data
        result['name'] = self.name
        result['network_mode'] = self.network_mode
        result['region_id'] = self.region_id
        result['resource_group_id'] = self.resource_group_id
        result['security_group_id'] = self.security_group_id
        result['size'] = self.size
        result['state'] = self.state
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['updated'] = self.updated
        result['vpc_id'] = self.vpc_id
        result['vswitch_cidr'] = self.vswitch_cidr
        result['vswitch_id'] = self.vswitch_id
        result['zone_id'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.cluster_type = map.get('cluster_type')
        self.created = map.get('created')
        self.current_version = map.get('current_version')
        self.deletion_protection = map.get('deletion_protection')
        self.docker_version = map.get('docker_version')
        self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        self.instance_type = map.get('instance_type')
        self.meta_data = map.get('meta_data')
        self.name = map.get('name')
        self.network_mode = map.get('network_mode')
        self.region_id = map.get('region_id')
        self.resource_group_id = map.get('resource_group_id')
        self.security_group_id = map.get('security_group_id')
        self.size = map.get('size')
        self.state = map.get('state')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = DescribeClusterDetailResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.updated = map.get('updated')
        self.vpc_id = map.get('vpc_id')
        self.vswitch_cidr = map.get('vswitch_cidr')
        self.vswitch_id = map.get('vswitch_id')
        self.zone_id = map.get('zone_id')
        return self


class DescribeClusterDetailResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class DescribeClusterDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterDetailResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterLogsResponseBody(TeaModel):
    def __init__(self, id=None, cluster_id=None, cluster_log=None, created=None, log_level=None, updated=None):
        # 日志ID。
        self.id = id                    # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 日志详情。
        self.cluster_log = cluster_log  # type: str
        # 日志创建时间。
        self.created = created          # type: str
        # 日志级别。
        self.log_level = log_level      # type: str
        # 日志更新时间。
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['ID'] = self.id
        result['cluster_id'] = self.cluster_id
        result['cluster_log'] = self.cluster_log
        result['created'] = self.created
        result['log_level'] = self.log_level
        result['updated'] = self.updated
        return result

    def from_map(self, map={}):
        self.id = map.get('ID')
        self.cluster_id = map.get('cluster_id')
        self.cluster_log = map.get('cluster_log')
        self.created = map.get('created')
        self.log_level = map.get('log_level')
        self.updated = map.get('updated')
        return self


class DescribeClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterLogsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterLogsResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterNodesRequest(TeaModel):
    def __init__(self, page_size=None, page_number=None, nodepool_id=None, state=None):
        # 每页展示结果数。
        self.page_size = page_size      # type: str
        # 结果只展示几页。
        self.page_number = page_number  # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 节点状态信息。
        self.state = state              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['pageSize'] = self.page_size
        result['pageNumber'] = self.page_number
        result['nodepool_id'] = self.nodepool_id
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.page_size = map.get('pageSize')
        self.page_number = map.get('pageNumber')
        self.nodepool_id = map.get('nodepool_id')
        self.state = map.get('state')
        return self


class DescribeClusterNodesResponseBody(TeaModel):
    def __init__(self, nodes=None, page=None):
        # 节点信息列表。
        self.nodes = nodes              # type: List[DescribeClusterNodesResponseBodyNodes]
        # 分页信息。
        self.page = page                # type: DescribeClusterNodesResponseBodyPage

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        result = {}
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        else:
            result['nodes'] = None
        if self.page is not None:
            result['page'] = self.page.to_map()
        else:
            result['page'] = None
        return result

    def from_map(self, map={}):
        self.nodes = []
        if map.get('nodes') is not None:
            for k in map.get('nodes'):
                temp_model = DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        else:
            self.nodes = None
        if map.get('page') is not None:
            temp_model = DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(map['page'])
        else:
            self.page = None
        return self


class DescribeClusterNodesResponseBodyNodes(TeaModel):
    def __init__(self, creation_time=None, error_message=None, expired_time=None, host_name=None, image_id=None,
                 instance_charge_type=None, instance_id=None, instance_name=None, instance_role=None, instance_status=None,
                 instance_type=None, instance_type_family=None, ip_address=None, is_aliyun_node=None, node_name=None,
                 node_status=None, nodepool_id=None, source=None, state=None):
        # 节点创建时间。
        self.creation_time = creation_time  # type: str
        # 错误信息说明。
        self.error_message = error_message  # type: str
        # 节点过期时间。
        self.expired_time = expired_time  # type: str
        # 节点主机名。
        self.host_name = host_name      # type: str
        # 节点使用的镜像ID。
        self.image_id = image_id        # type: str
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点实例ID。
        self.instance_id = instance_id  # type: str
        # 节点实例名称。
        self.instance_name = instance_name  # type: str
        # 节点实例角色类型，Master或Worker。
        self.instance_role = instance_role  # type: str
        # 节点实例状态，
        self.instance_status = instance_status  # type: str
        # 节点实例类型。
        self.instance_type = instance_type  # type: str
        # 节点实例所属ECS实例簇名称。
        self.instance_type_family = instance_type_family  # type: str
        # 节点IP地址。
        self.ip_address = ip_address    # type: List[str]
        # 节点是否为aliyun实例。
        self.is_aliyun_node = is_aliyun_node  # type: bool
        # 节点名称，该名称是k8s专用名称。
        self.node_name = node_name      # type: str
        # 节点状态，是否Ready。
        self.node_status = node_status  # type: str
        # 节点所属的节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 节点通过什么方式创建出来的，例如：ROS。
        self.source = source            # type: str
        # ECS运行状态，例如：running。
        self.state = state              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['creation_time'] = self.creation_time
        result['error_message'] = self.error_message
        result['expired_time'] = self.expired_time
        result['host_name'] = self.host_name
        result['image_id'] = self.image_id
        result['instance_charge_type'] = self.instance_charge_type
        result['instance_id'] = self.instance_id
        result['instance_name'] = self.instance_name
        result['instance_role'] = self.instance_role
        result['instance_status'] = self.instance_status
        result['instance_type'] = self.instance_type
        result['instance_type_family'] = self.instance_type_family
        result['ip_address'] = self.ip_address
        result['is_aliyun_node'] = self.is_aliyun_node
        result['node_name'] = self.node_name
        result['node_status'] = self.node_status
        result['nodepool_id'] = self.nodepool_id
        result['source'] = self.source
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.creation_time = map.get('creation_time')
        self.error_message = map.get('error_message')
        self.expired_time = map.get('expired_time')
        self.host_name = map.get('host_name')
        self.image_id = map.get('image_id')
        self.instance_charge_type = map.get('instance_charge_type')
        self.instance_id = map.get('instance_id')
        self.instance_name = map.get('instance_name')
        self.instance_role = map.get('instance_role')
        self.instance_status = map.get('instance_status')
        self.instance_type = map.get('instance_type')
        self.instance_type_family = map.get('instance_type_family')
        self.ip_address = map.get('ip_address')
        self.is_aliyun_node = map.get('is_aliyun_node')
        self.node_name = map.get('node_name')
        self.node_status = map.get('node_status')
        self.nodepool_id = map.get('nodepool_id')
        self.source = map.get('source')
        self.state = map.get('state')
        return self


class DescribeClusterNodesResponseBodyPage(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 总页数。
        self.page_number = page_number  # type: int
        # 单页展示结果数量。
        self.page_size = page_size      # type: int
        # 结果总条数。
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['page_number'] = self.page_number
        result['page_size'] = self.page_size
        result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        self.page_number = map.get('page_number')
        self.page_size = map.get('page_size')
        self.total_count = map.get('total_count')
        return self


class DescribeClusterNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterNodesResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: List[DescribeClusterResourcesResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeClusterResourcesResponseBody()
                self.body.append(temp_model.from_map(k))
        else:
            self.body = None
        return self


class DescribeClusterResourcesResponseBody(TeaModel):
    def __init__(self, cluster_id=None, created=None, instance_id=None, resource_info=None, resource_type=None,
                 state=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 资源创建时间。
        self.created = created          # type: str
        # 资源实例ID。
        self.instance_id = instance_id  # type: str
        # 资源元信息。
        self.resource_info = resource_info  # type: str
        # 资源类型。
        self.resource_type = resource_type  # type: str
        # 资源状态。
        self.state = state              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['created'] = self.created
        result['instance_id'] = self.instance_id
        result['resource_info'] = self.resource_info
        result['resource_type'] = self.resource_type
        result['state'] = self.state
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.created = map.get('created')
        self.instance_id = map.get('instance_id')
        self.resource_info = map.get('resource_info')
        self.resource_type = map.get('resource_type')
        self.state = map.get('state')
        return self


class DescribeClusterUserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # ApiServer是否为内网地址。
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        self.private_ip_address = map.get('PrivateIpAddress')
        return self


class DescribeClusterUserKubeconfigResponseBody(TeaModel):
    def __init__(self, config=None):
        # kubeconfig内容。
        self.config = config            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['config'] = self.config
        return result

    def from_map(self, map={}):
        self.config = map.get('config')
        return self


class DescribeClusterUserKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterUserKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterUserKubeconfigResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClusterV2UserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # 是否为内网访问。
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        self.private_ip_address = map.get('PrivateIpAddress')
        return self


class DescribeClusterV2UserKubeconfigResponseBody(TeaModel):
    def __init__(self, config=None):
        # kubeconfig内容。
        self.config = config            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['config'] = self.config
        return result

    def from_map(self, map={}):
        self.config = map.get('config')
        return self


class DescribeClusterV2UserKubeconfigResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterV2UserKubeconfigResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterV2UserKubeconfigResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(self, name=None, cluster_type=None):
        # 集群名称。
        self.name = name                # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['clusterType'] = self.cluster_type
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.cluster_type = map.get('clusterType')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: List[DescribeClustersResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeClustersResponseBody()
                self.body.append(temp_model.from_map(k))
        else:
            self.body = None
        return self


class DescribeClustersResponseBodyTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class DescribeClustersResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, created=None, current_version=None,
                 data_disk_category=None, data_disk_size=None, deletion_protection=None, docker_version=None,
                 external_loadbalancer_id=None, init_version=None, master_url=None, meta_data=None, name=None, network_mode=None,
                 private_zone=None, profile=None, region_id=None, resource_group_id=None, security_group_id=None, size=None,
                 state=None, subnet_cidr=None, tags=None, updated=None, vpc_id=None, vswitch_cidr=None, vswitch_id=None,
                 worker_ram_role_name=None, zone_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created          # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 节点系统盘类型。
        self.data_disk_category = data_disk_category  # type: str
        # 节点系统盘大小。
        self.data_disk_size = data_disk_size  # type: int
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 容器运行时版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingerss SLB实例的ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群创建时版本。
        self.init_version = init_version  # type: str
        # 集群的endpoint地址。
        self.master_url = master_url    # type: str
        # 集群元数据。
        self.meta_data = meta_data      # type: str
        # 集群名称。
        self.name = name                # type: str
        # 集群使用的网络类型。
        self.network_mode = network_mode  # type: str
        # 集群是否开启Private Zone，默认false。
        self.private_zone = private_zone  # type: bool
        # 集群标识，区分是否为边缘托管版。
        self.profile = profile          # type: str
        # 集群所在地域ID。
        self.region_id = region_id      # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群内实例数量。
        self.size = size                # type: int
        # 集群运行状态。
        self.state = state              # type: str
        # POD网络。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群标签。
        self.tags = tags                # type: List[DescribeClustersResponseBodyTags]
        # 集群更新时间。
        self.updated = updated          # type: str
        # 集群使用的VPC ID。
        self.vpc_id = vpc_id            # type: str
        # 虚拟交换机网络ID。
        self.vswitch_cidr = vswitch_cidr  # type: str
        # 节点使用的Vswitch ID。
        self.vswitch_id = vswitch_id    # type: str
        # 集群Worker节点RAM角色名称。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 集群所在Region内的区域ID。
        self.zone_id = zone_id          # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['cluster_type'] = self.cluster_type
        result['created'] = self.created
        result['current_version'] = self.current_version
        result['data_disk_category'] = self.data_disk_category
        result['data_disk_size'] = self.data_disk_size
        result['deletion_protection'] = self.deletion_protection
        result['docker_version'] = self.docker_version
        result['external_loadbalancer_id'] = self.external_loadbalancer_id
        result['init_version'] = self.init_version
        result['master_url'] = self.master_url
        result['meta_data'] = self.meta_data
        result['name'] = self.name
        result['network_mode'] = self.network_mode
        result['private_zone'] = self.private_zone
        result['profile'] = self.profile
        result['region_id'] = self.region_id
        result['resource_group_id'] = self.resource_group_id
        result['security_group_id'] = self.security_group_id
        result['size'] = self.size
        result['state'] = self.state
        result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['updated'] = self.updated
        result['vpc_id'] = self.vpc_id
        result['vswitch_cidr'] = self.vswitch_cidr
        result['vswitch_id'] = self.vswitch_id
        result['worker_ram_role_name'] = self.worker_ram_role_name
        result['zone_id'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.cluster_type = map.get('cluster_type')
        self.created = map.get('created')
        self.current_version = map.get('current_version')
        self.data_disk_category = map.get('data_disk_category')
        self.data_disk_size = map.get('data_disk_size')
        self.deletion_protection = map.get('deletion_protection')
        self.docker_version = map.get('docker_version')
        self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        self.init_version = map.get('init_version')
        self.master_url = map.get('master_url')
        self.meta_data = map.get('meta_data')
        self.name = map.get('name')
        self.network_mode = map.get('network_mode')
        self.private_zone = map.get('private_zone')
        self.profile = map.get('profile')
        self.region_id = map.get('region_id')
        self.resource_group_id = map.get('resource_group_id')
        self.security_group_id = map.get('security_group_id')
        self.size = map.get('size')
        self.state = map.get('state')
        self.subnet_cidr = map.get('subnet_cidr')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = DescribeClustersResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.updated = map.get('updated')
        self.vpc_id = map.get('vpc_id')
        self.vswitch_cidr = map.get('vswitch_cidr')
        self.vswitch_id = map.get('vswitch_id')
        self.worker_ram_role_name = map.get('worker_ram_role_name')
        self.zone_id = map.get('zone_id')
        return self


class DescribeClustersV1Request(TeaModel):
    def __init__(self, name=None, cluster_type=None, page_size=None, page_number=None):
        # 集群名称。
        self.name = name                # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 单页大小。
        self.page_size = page_size      # type: int
        # 分页数。
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Name'] = self.name
        result['ClusterType'] = self.cluster_type
        result['page_size'] = self.page_size
        result['page_number'] = self.page_number
        return result

    def from_map(self, map={}):
        self.name = map.get('Name')
        self.cluster_type = map.get('ClusterType')
        self.page_size = map.get('page_size')
        self.page_number = map.get('page_number')
        return self


class DescribeClustersV1ResponseBody(TeaModel):
    def __init__(self, clusters=None, page_info=None):
        # 集群详情列表。
        self.clusters = clusters        # type: List[DescribeClustersV1ResponseBodyClusters]
        # 分页信息。
        self.page_info = page_info      # type: DescribeClustersV1ResponseBodyPageInfo

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = {}
        result['clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        else:
            result['clusters'] = None
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        else:
            result['page_info'] = None
        return result

    def from_map(self, map={}):
        self.clusters = []
        if map.get('clusters') is not None:
            for k in map.get('clusters'):
                temp_model = DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        else:
            self.clusters = None
        if map.get('page_info') is not None:
            temp_model = DescribeClustersV1ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(map['page_info'])
        else:
            self.page_info = None
        return self


class DescribeClustersV1ResponseBodyClustersTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签键。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class DescribeClustersV1ResponseBodyClusters(TeaModel):
    def __init__(self, cluster_healthy=None, cluster_id=None, cluster_type=None, created=None, current_version=None,
                 data_disk_category=None, data_disk_size=None, deletion_protection=None, docker_version=None,
                 external_loadbalancer_id=None, init_version=None, master_url=None, meta_data=None, name=None, network_mode=None,
                 node_status=None, private_zone=None, profile=None, region_id=None, resource_group_id=None,
                 security_group_id=None, size=None, state=None, subnet_cidr=None, tags=None, updated=None, vpc_id=None,
                 vswitch_cidr=None, vswitch_id=None, worker_ram_role_name=None, zone_id=None):
        # 集群健康状态。
        self.cluster_healthy = cluster_healthy  # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created          # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 数据盘类型。
        self.data_disk_category = data_disk_category  # type: str
        # 数据盘大小。
        self.data_disk_size = data_disk_size  # type: int
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群使用的Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingress对应的SLB的地址。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群初始化版本。
        self.init_version = init_version  # type: str
        # 集群访问的端点信息。
        self.master_url = master_url    # type: str
        # 集群元数据信息。
        self.meta_data = meta_data      # type: str
        # 集群名称。
        self.name = name                # type: str
        # 集群使用的网络类型，例如：VPC网络。
        self.network_mode = network_mode  # type: str
        # 节点状态。
        self.node_status = node_status  # type: str
        # 集群是否开启Private Zone。
        self.private_zone = private_zone  # type: bool
        # 边缘集群表示，用于区分边缘托管版集群。
        self.profile = profile          # type: str
        # 地域ID。
        self.region_id = region_id      # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 集群安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 集群节点数。
        self.size = size                # type: int
        # 集群运行状态。
        self.state = state              # type: str
        # POD网段地址。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群标签。
        self.tags = tags                # type: List[DescribeClustersV1ResponseBodyClustersTags]
        # 集群更新时间。
        self.updated = updated          # type: str
        # 集群所在的VPC ID。
        self.vpc_id = vpc_id            # type: str
        # 虚拟交换机CIDR。
        self.vswitch_cidr = vswitch_cidr  # type: str
        # 集群使用的虚拟交换ID。
        self.vswitch_id = vswitch_id    # type: str
        # 集群Worker RAM角色。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 可用区ID。
        self.zone_id = zone_id          # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['cluster_healthy'] = self.cluster_healthy
        result['cluster_id'] = self.cluster_id
        result['cluster_type'] = self.cluster_type
        result['created'] = self.created
        result['current_version'] = self.current_version
        result['data_disk_category'] = self.data_disk_category
        result['data_disk_size'] = self.data_disk_size
        result['deletion_protection'] = self.deletion_protection
        result['docker_version'] = self.docker_version
        result['external_loadbalancer_id'] = self.external_loadbalancer_id
        result['init_version'] = self.init_version
        result['master_url'] = self.master_url
        result['meta_data'] = self.meta_data
        result['name'] = self.name
        result['network_mode'] = self.network_mode
        result['node_status'] = self.node_status
        result['private_zone'] = self.private_zone
        result['profile'] = self.profile
        result['region_id'] = self.region_id
        result['resource_group_id'] = self.resource_group_id
        result['security_group_id'] = self.security_group_id
        result['size'] = self.size
        result['state'] = self.state
        result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['updated'] = self.updated
        result['vpc_id'] = self.vpc_id
        result['vswitch_cidr'] = self.vswitch_cidr
        result['vswitch_id'] = self.vswitch_id
        result['worker_ram_role_name'] = self.worker_ram_role_name
        result['zone_id'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.cluster_healthy = map.get('cluster_healthy')
        self.cluster_id = map.get('cluster_id')
        self.cluster_type = map.get('cluster_type')
        self.created = map.get('created')
        self.current_version = map.get('current_version')
        self.data_disk_category = map.get('data_disk_category')
        self.data_disk_size = map.get('data_disk_size')
        self.deletion_protection = map.get('deletion_protection')
        self.docker_version = map.get('docker_version')
        self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        self.init_version = map.get('init_version')
        self.master_url = map.get('master_url')
        self.meta_data = map.get('meta_data')
        self.name = map.get('name')
        self.network_mode = map.get('network_mode')
        self.node_status = map.get('node_status')
        self.private_zone = map.get('private_zone')
        self.profile = map.get('profile')
        self.region_id = map.get('region_id')
        self.resource_group_id = map.get('resource_group_id')
        self.security_group_id = map.get('security_group_id')
        self.size = map.get('size')
        self.state = map.get('state')
        self.subnet_cidr = map.get('subnet_cidr')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = DescribeClustersV1ResponseBodyClustersTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.updated = map.get('updated')
        self.vpc_id = map.get('vpc_id')
        self.vswitch_cidr = map.get('vswitch_cidr')
        self.vswitch_id = map.get('vswitch_id')
        self.worker_ram_role_name = map.get('worker_ram_role_name')
        self.zone_id = map.get('zone_id')
        return self


class DescribeClustersV1ResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 分页总数。
        self.page_number = page_number  # type: int
        # 单页大小。
        self.page_size = page_size      # type: int
        # 结果总条目数。
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['page_number'] = self.page_number
        result['page_size'] = self.page_size
        result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        self.page_number = map.get('page_number')
        self.page_size = map.get('page_size')
        self.total_count = map.get('total_count')
        return self


class DescribeClustersV1Response(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClustersV1ResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClustersV1ResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeExternalAgentResponseBody(TeaModel):
    def __init__(self, config=None):
        # 代理配置。
        self.config = config            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['config'] = self.config
        return result

    def from_map(self, map={}):
        self.config = map.get('config')
        return self


class DescribeExternalAgentResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeExternalAgentResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeExternalAgentResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(self, template_type=None):
        # 模板类型，部署模板类型，目前一共有2种类型，取值为：kubernetes或compose。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['template_type'] = self.template_type
        return result

    def from_map(self, map={}):
        self.template_type = map.get('template_type')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(self, page_info=None, templates=None):
        # 分页信息。
        self.page_info = page_info      # type: DescribeTemplatesResponseBodyPageInfo
        # 模板列表。
        self.templates = templates      # type: List[DescribeTemplatesResponseBodyTemplates]

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        else:
            result['page_info'] = None
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        else:
            result['templates'] = None
        return result

    def from_map(self, map={}):
        if map.get('page_info') is not None:
            temp_model = DescribeTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(map['page_info'])
        else:
            self.page_info = None
        self.templates = []
        if map.get('templates') is not None:
            for k in map.get('templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        else:
            self.templates = None
        return self


class DescribeTemplatesResponseBodyPageInfo(TeaModel):
    def __init__(self, page_number=None, page_size=None, total_count=None):
        # 分页数。
        self.page_number = page_number  # type: int
        # 单页大小。
        self.page_size = page_size      # type: int
        # 结果总数。
        self.total_count = total_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['page_number'] = self.page_number
        result['page_size'] = self.page_size
        result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        self.page_number = map.get('page_number')
        self.page_size = map.get('page_size')
        self.total_count = map.get('total_count')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(self, acl=None, created=None, description=None, id=None, name=None, tags=None, template=None,
                 template_type=None, updated=None):
        # 模板访问权限，取值为：private、pubilc或shared。。
        self.acl = acl                  # type: str
        # 模板创建时间。
        self.created = created          # type: str
        # 模板描述信息。
        self.description = description  # type: str
        # 模板ID。
        self.id = id                    # type: str
        # 模板名称。
        self.name = name                # type: str
        # 模板标签，如果不显式指定了，默认为模板名称。
        self.tags = tags                # type: str
        # 模板详情。
        self.template = template        # type: str
        # 部署模板类型，目前只有kubernetes一种生效。
        self.template_type = template_type  # type: str
        # 模板修改时间。
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['acl'] = self.acl
        result['created'] = self.created
        result['description'] = self.description
        result['id'] = self.id
        result['name'] = self.name
        result['tags'] = self.tags
        result['template'] = self.template
        result['template_type'] = self.template_type
        result['updated'] = self.updated
        return result

    def from_map(self, map={}):
        self.acl = map.get('acl')
        self.created = map.get('created')
        self.description = map.get('description')
        self.id = map.get('id')
        self.name = map.get('name')
        self.tags = map.get('tags')
        self.template = map.get('template')
        self.template_type = map.get('template_type')
        self.updated = map.get('updated')
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeTemplatesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class DescribeUserQuotaResponseBody(TeaModel):
    def __init__(self, amk_cluster_quota=None, ask_cluster_quota=None, cluster_nodepool_quota=None,
                 cluster_quota=None, node_quota=None):
        # 托管版集群配额。
        self.amk_cluster_quota = amk_cluster_quota  # type: int
        # Serverless集群配额。
        self.ask_cluster_quota = ask_cluster_quota  # type: int
        # 集群节点池配额。
        self.cluster_nodepool_quota = cluster_nodepool_quota  # type: int
        # 专有版集群托管版集群的总配额。
        self.cluster_quota = cluster_quota  # type: int
        # 单集群的节点配额。
        self.node_quota = node_quota    # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['amk_cluster_quota'] = self.amk_cluster_quota
        result['ask_cluster_quota'] = self.ask_cluster_quota
        result['cluster_nodepool_quota'] = self.cluster_nodepool_quota
        result['cluster_quota'] = self.cluster_quota
        result['node_quota'] = self.node_quota
        return result

    def from_map(self, map={}):
        self.amk_cluster_quota = map.get('amk_cluster_quota')
        self.ask_cluster_quota = map.get('ask_cluster_quota')
        self.cluster_nodepool_quota = map.get('cluster_nodepool_quota')
        self.cluster_quota = map.get('cluster_quota')
        self.node_quota = map.get('node_quota')
        return self


class DescribeUserQuotaResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeUserQuotaResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeUserQuotaResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetKubernetesTriggerRequest(TeaModel):
    def __init__(self, namespace=None, type=None, name=None):
        # 应用所属命名空间。
        self.namespace = namespace      # type: str
        # 应用类型。
        self.type = type                # type: str
        # 应用名称。
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['Namespace'] = self.namespace
        result['Type'] = self.type
        result['Name'] = self.name
        return result

    def from_map(self, map={}):
        self.namespace = map.get('Namespace')
        self.type = map.get('Type')
        self.name = map.get('Name')
        return self


class GetKubernetesTriggerResponseBody(TeaModel):
    def __init__(self, triggers=None):
        # 触发器详情。
        self.triggers = triggers        # type: List[GetKubernetesTriggerResponseBodyTriggers]

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['triggers'].append(k.to_map() if k else None)
        else:
            result['triggers'] = None
        return result

    def from_map(self, map={}):
        self.triggers = []
        if map.get('triggers') is not None:
            for k in map.get('triggers'):
                temp_model = GetKubernetesTriggerResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        else:
            self.triggers = None
        return self


class GetKubernetesTriggerResponseBodyTriggers(TeaModel):
    def __init__(self, action=None, cluster_id=None, id=None, project_id=None, token=None):
        # 触发器行为。
        self.action = action            # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 触发器ID。
        self.id = id                    # type: str
        # 项目ID，格式为：${namepsce}/${应用名}，
        self.project_id = project_id    # type: str
        # 触发器Token。
        self.token = token              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['action'] = self.action
        result['cluster_id'] = self.cluster_id
        result['id'] = self.id
        result['project_id'] = self.project_id
        result['token'] = self.token
        return result

    def from_map(self, map={}):
        self.action = map.get('action')
        self.cluster_id = map.get('cluster_id')
        self.id = map.get('id')
        self.project_id = map.get('project_id')
        self.token = map.get('token')
        return self


class GetKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetKubernetesTriggerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class GetUpgradeStatusResponseBody(TeaModel):
    def __init__(self, error_message=None, precheck_report_id=None, status=None, upgrade_step=None):
        # 错误信息描述。
        self.error_message = error_message  # type: str
        # 预检查返回ID。
        self.precheck_report_id = precheck_report_id  # type: str
        # 升级状态。
        self.status = status            # type: str
        # 升级任务执行到哪一步了。
        self.upgrade_step = upgrade_step  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['error_message'] = self.error_message
        result['precheck_report_id'] = self.precheck_report_id
        result['status'] = self.status
        result['upgrade_step'] = self.upgrade_step
        return result

    def from_map(self, map={}):
        self.error_message = map.get('error_message')
        self.precheck_report_id = map.get('precheck_report_id')
        self.status = map.get('status')
        self.upgrade_step = map.get('upgrade_step')
        return self


class GetUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: GetUpgradeStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUpgradeStatusResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class InstallClusterAddonsRequest(TeaModel):
    def __init__(self, body=None):
        # Addon列表。
        self.body = body                # type: List[InstallClusterAddonsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = InstallClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        else:
            self.body = None
        return self


class InstallClusterAddonsRequestBody(TeaModel):
    def __init__(self, config=None, disabled=None, name=None, required=None, version=None):
        # Addon配置信息。
        self.config = config            # type: str
        # 是否禁止默认安装。
        self.disabled = disabled        # type: bool
        # Addon名称。
        self.name = name                # type: str
        # 是否默认安装。
        self.required = required        # type: str
        # Addon版本号。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['config'] = self.config
        result['disabled'] = self.disabled
        result['name'] = self.name
        result['required'] = self.required
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.config = map.get('config')
        self.disabled = map.get('disabled')
        self.name = map.get('name')
        self.required = map.get('required')
        self.version = map.get('version')
        return self


class InstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(self, deletion_protection=None, ingress_loadbalancer_id=None, api_server_eip=None,
                 api_server_eip_id=None, resource_group_id=None, ingress_domain_rebinding=None):
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群的Ingress SLB的ID。
        self.ingress_loadbalancer_id = ingress_loadbalancer_id  # type: str
        # 集群是否开启EIP。
        self.api_server_eip = api_server_eip  # type: bool
        # 集群的API Server的EIP ID。
        self.api_server_eip_id = api_server_eip_id  # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 域名是否重新绑定到Ingress的SLB地址。
        self.ingress_domain_rebinding = ingress_domain_rebinding  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['deletion_protection'] = self.deletion_protection
        result['ingress_loadbalancer_id'] = self.ingress_loadbalancer_id
        result['api_server_eip'] = self.api_server_eip
        result['api_server_eip_id'] = self.api_server_eip_id
        result['resource_group_id'] = self.resource_group_id
        result['ingress_domain_rebinding'] = self.ingress_domain_rebinding
        return result

    def from_map(self, map={}):
        self.deletion_protection = map.get('deletion_protection')
        self.ingress_loadbalancer_id = map.get('ingress_loadbalancer_id')
        self.api_server_eip = map.get('api_server_eip')
        self.api_server_eip_id = map.get('api_server_eip_id')
        self.resource_group_id = map.get('resource_group_id')
        self.ingress_domain_rebinding = map.get('ingress_domain_rebinding')
        return self


class ModifyClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 请求ID。
        self.request_id = request_id    # type: str
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['request_id'] = self.request_id
        result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.request_id = map.get('request_id')
        self.task_id = map.get('task_id')
        return self


class ModifyClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ModifyClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ModifyClusterConfigurationRequest(TeaModel):
    def __init__(self, customize_config=None):
        # 自定配置。
        self.customize_config = customize_config  # type: ModifyClusterConfigurationRequestCustomizeConfig

    def validate(self):
        if self.customize_config:
            self.customize_config.validate()

    def to_map(self):
        result = {}
        if self.customize_config is not None:
            result['customize_config'] = self.customize_config.to_map()
        else:
            result['customize_config'] = None
        return result

    def from_map(self, map={}):
        if map.get('customize_config') is not None:
            temp_model = ModifyClusterConfigurationRequestCustomizeConfig()
            self.customize_config = temp_model.from_map(map['customize_config'])
        else:
            self.customize_config = None
        return self


class ModifyClusterConfigurationRequestCustomizeConfigConfigs(TeaModel):
    def __init__(self, key=None, value=None):
        # key。
        self.key = key                  # type: str
        # value。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class ModifyClusterConfigurationRequestCustomizeConfig(TeaModel):
    def __init__(self, configs=None, name=None):
        # 配置集合。
        self.configs = configs          # type: ModifyClusterConfigurationRequestCustomizeConfigConfigs
        # 配置名称。
        self.name = name                # type: str

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = {}
        if self.configs is not None:
            result['configs'] = self.configs.to_map()
        else:
            result['configs'] = None
        result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('configs') is not None:
            temp_model = ModifyClusterConfigurationRequestCustomizeConfigConfigs()
            self.configs = temp_model.from_map(map['configs'])
        else:
            self.configs = None
        self.name = map.get('name')
        return self


class ModifyClusterConfigurationResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class ModifyClusterTagsRequest(TeaModel):
    def __init__(self, body=None):
        # 标签列表。
        self.body = body                # type: List[ModifyClusterTagsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = ModifyClusterTagsRequestBody()
                self.body.append(temp_model.from_map(k))
        else:
            self.body = None
        return self


class ModifyClusterTagsRequestBody(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class ModifyClusterTagsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class PauseComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class RemoveClusterNodesRequest(TeaModel):
    def __init__(self, release_node=None, drain_node=None, nodes=None):
        # 是否同时释放ECS。
        self.release_node = release_node  # type: bool
        # 是否排空节点上的Pod。
        self.drain_node = drain_node    # type: bool
        # 要移除的Node列表。
        self.nodes = nodes              # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['release_node'] = self.release_node
        result['drain_node'] = self.drain_node
        result['nodes'] = self.nodes
        return result

    def from_map(self, map={}):
        self.release_node = map.get('release_node')
        self.drain_node = map.get('drain_node')
        self.nodes = map.get('nodes')
        return self


class RemoveClusterNodesResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class ResumeComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class ScaleClusterRequest(TeaModel):
    def __init__(self, count=None, key_pair=None, login_password=None, worker_data_disk=None,
                 worker_instance_types=None, worker_instance_charge_type=None, worker_period=None, worker_period_unit=None,
                 worker_auto_renew=None, worker_auto_renew_period=None, worker_system_disk_category=None,
                 worker_system_disk_size=None, cloud_monitor_flags=None, cpu_policy=None, disable_rollback=None, vswitch_ids=None,
                 worker_data_disks=None, tags=None, taints=None):
        # 扩容节点数。
        self.count = count              # type: int
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码。和keypair二选一。
        self.login_password = login_password  # type: str
        # 是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # Worker节点ECS规格类型。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # 节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # 节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # 当指定为PrePaid的时候需要指定周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # 节点是否开启Worker节点自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # 自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # 节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # 节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: int
        # 节点是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 节点CPU策略。
        self.cpu_policy = cpu_policy    # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 节点交换机ID列表。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: List[ScaleClusterRequestWorkerDataDisks]
        # 集群标签。
        self.tags = tags                # type: List[ScaleClusterRequestTags]
        # 节点污点标记。
        self.taints = taints            # type: List[ScaleClusterRequestTaints]

    def validate(self):
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['count'] = self.count
        result['key_pair'] = self.key_pair
        result['login_password'] = self.login_password
        result['worker_data_disk'] = self.worker_data_disk
        result['worker_instance_types'] = self.worker_instance_types
        result['worker_instance_charge_type'] = self.worker_instance_charge_type
        result['worker_period'] = self.worker_period
        result['worker_period_unit'] = self.worker_period_unit
        result['worker_auto_renew'] = self.worker_auto_renew
        result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_system_disk_category'] = self.worker_system_disk_category
        result['worker_system_disk_size'] = self.worker_system_disk_size
        result['cloud_monitor_flags'] = self.cloud_monitor_flags
        result['cpu_policy'] = self.cpu_policy
        result['disable_rollback'] = self.disable_rollback
        result['vswitch_ids'] = self.vswitch_ids
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        else:
            result['worker_data_disks'] = None
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        else:
            result['taints'] = None
        return result

    def from_map(self, map={}):
        self.count = map.get('count')
        self.key_pair = map.get('key_pair')
        self.login_password = map.get('login_password')
        self.worker_data_disk = map.get('worker_data_disk')
        self.worker_instance_types = map.get('worker_instance_types')
        self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        self.worker_period = map.get('worker_period')
        self.worker_period_unit = map.get('worker_period_unit')
        self.worker_auto_renew = map.get('worker_auto_renew')
        self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        self.worker_system_disk_category = map.get('worker_system_disk_category')
        self.worker_system_disk_size = map.get('worker_system_disk_size')
        self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        self.cpu_policy = map.get('cpu_policy')
        self.disable_rollback = map.get('disable_rollback')
        self.vswitch_ids = map.get('vswitch_ids')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = ScaleClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        else:
            self.worker_data_disks = None
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ScaleClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = ScaleClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        else:
            self.taints = None
        return self


class ScaleClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, size=None):
        # 数据盘类型。
        self.category = category        # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted      # type: str
        # 数据盘大小。
        self.size = size                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['encrypted'] = self.encrypted
        result['size'] = self.size
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.encrypted = map.get('encrypted')
        self.size = map.get('size')
        return self


class ScaleClusterRequestTags(TeaModel):
    def __init__(self, key=None):
        # 标签值。
        self.key = key                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        return self


class ScaleClusterRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # 污点生效策略。
        self.effect = effect            # type: str
        # 污点键。
        self.key = key                  # type: str
        # 污点值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['effect'] = self.effect
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.effect = map.get('effect')
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class ScaleClusterShrinkRequest(TeaModel):
    def __init__(self, count=None, key_pair=None, login_password=None, worker_data_disk=None,
                 worker_instance_types=None, worker_instance_charge_type=None, worker_period=None, worker_period_unit=None,
                 worker_auto_renew=None, worker_auto_renew_period=None, worker_system_disk_category=None,
                 worker_system_disk_size=None, cloud_monitor_flags=None, cpu_policy=None, disable_rollback=None, vswitch_ids=None,
                 worker_data_disks=None, tags=None, taints_shrink=None):
        # 扩容节点数。
        self.count = count              # type: int
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码。和keypair二选一。
        self.login_password = login_password  # type: str
        # 是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # Worker节点ECS规格类型。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # 节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # 节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # 当指定为PrePaid的时候需要指定周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # 节点是否开启Worker节点自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # 自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # 节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # 节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: int
        # 节点是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 节点CPU策略。
        self.cpu_policy = cpu_policy    # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 节点交换机ID列表。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: List[ScaleClusterShrinkRequestWorkerDataDisks]
        # 集群标签。
        self.tags = tags                # type: List[ScaleClusterShrinkRequestTags]
        # 节点污点标记。
        self.taints_shrink = taints_shrink  # type: str

    def validate(self):
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['count'] = self.count
        result['key_pair'] = self.key_pair
        result['login_password'] = self.login_password
        result['worker_data_disk'] = self.worker_data_disk
        result['worker_instance_types'] = self.worker_instance_types
        result['worker_instance_charge_type'] = self.worker_instance_charge_type
        result['worker_period'] = self.worker_period
        result['worker_period_unit'] = self.worker_period_unit
        result['worker_auto_renew'] = self.worker_auto_renew
        result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_system_disk_category'] = self.worker_system_disk_category
        result['worker_system_disk_size'] = self.worker_system_disk_size
        result['cloud_monitor_flags'] = self.cloud_monitor_flags
        result['cpu_policy'] = self.cpu_policy
        result['disable_rollback'] = self.disable_rollback
        result['vswitch_ids'] = self.vswitch_ids
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        else:
            result['worker_data_disks'] = None
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['taints'] = self.taints_shrink
        return result

    def from_map(self, map={}):
        self.count = map.get('count')
        self.key_pair = map.get('key_pair')
        self.login_password = map.get('login_password')
        self.worker_data_disk = map.get('worker_data_disk')
        self.worker_instance_types = map.get('worker_instance_types')
        self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        self.worker_period = map.get('worker_period')
        self.worker_period_unit = map.get('worker_period_unit')
        self.worker_auto_renew = map.get('worker_auto_renew')
        self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        self.worker_system_disk_category = map.get('worker_system_disk_category')
        self.worker_system_disk_size = map.get('worker_system_disk_size')
        self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        self.cpu_policy = map.get('cpu_policy')
        self.disable_rollback = map.get('disable_rollback')
        self.vswitch_ids = map.get('vswitch_ids')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = ScaleClusterShrinkRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        else:
            self.worker_data_disks = None
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ScaleClusterShrinkRequestTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.taints_shrink = map.get('taints')
        return self


class ScaleClusterShrinkRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, size=None):
        # 数据盘类型。
        self.category = category        # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted      # type: str
        # 数据盘大小。
        self.size = size                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['encrypted'] = self.encrypted
        result['size'] = self.size
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.encrypted = map.get('encrypted')
        self.size = map.get('size')
        return self


class ScaleClusterShrinkRequestTags(TeaModel):
    def __init__(self, key=None):
        # 标签值。
        self.key = key                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        return self


class ScaleClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 请求ID。
        self.request_id = request_id    # type: str
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['request_id'] = self.request_id
        result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.request_id = map.get('request_id')
        self.task_id = map.get('task_id')
        return self


class ScaleClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ScaleClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScaleClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class ScaleOutClusterRequest(TeaModel):
    def __init__(self, count=None, worker_instance_charge_type=None, worker_period=None, worker_period_unit=None,
                 worker_auto_renew=None, worker_auto_renew_period=None, worker_system_disk_category=None,
                 worker_system_disk_size=None, worker_data_disk=None, key_pair=None, login_password=None, cloud_monitor_flags=None,
                 cpu_policy=None, disable_rollback=None, image_id=None, user_data=None, runtime=None, vswitch_ids=None,
                 worker_instance_types=None, rds_instances=None, worker_data_disks=None, tags=None, taints=None):
        # 扩容实例数量。
        self.count = count              # type: int
        # Worker节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # Worker节点预付费周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # Worker节点是否开启自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # Worker节点自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # Worker节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # Worker节点系统盘大小。
        self.worker_system_disk_size = worker_system_disk_size  # type: int
        # Worker节点是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码，和key_pair二选一。
        self.login_password = login_password  # type: str
        # 是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # CPU策略，取值static或者none。
        self.cpu_policy = cpu_policy    # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # 用户自定义数据。
        self.user_data = user_data      # type: str
        # 容器引擎。
        self.runtime = runtime          # type: ScaleOutClusterRequestRuntime
        # 节点交换机ID列表，交换机个数取值范围为1~3。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # Worker节点ECS规格类型代码。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # RDS白名单实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: List[ScaleOutClusterRequestWorkerDataDisks]
        # 节点标签。
        self.tags = tags                # type: List[ScaleOutClusterRequestTags]
        # 节点污点信息。
        self.taints = taints            # type: List[ScaleOutClusterRequestTaints]

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['count'] = self.count
        result['worker_instance_charge_type'] = self.worker_instance_charge_type
        result['worker_period'] = self.worker_period
        result['worker_period_unit'] = self.worker_period_unit
        result['worker_auto_renew'] = self.worker_auto_renew
        result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_system_disk_category'] = self.worker_system_disk_category
        result['worker_system_disk_size'] = self.worker_system_disk_size
        result['worker_data_disk'] = self.worker_data_disk
        result['key_pair'] = self.key_pair
        result['login_password'] = self.login_password
        result['cloud_monitor_flags'] = self.cloud_monitor_flags
        result['cpu_policy'] = self.cpu_policy
        result['disable_rollback'] = self.disable_rollback
        result['image_id'] = self.image_id
        result['user_data'] = self.user_data
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        else:
            result['runtime'] = None
        result['vswitch_ids'] = self.vswitch_ids
        result['worker_instance_types'] = self.worker_instance_types
        result['rds_instances'] = self.rds_instances
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        else:
            result['worker_data_disks'] = None
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        else:
            result['tags'] = None
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        else:
            result['taints'] = None
        return result

    def from_map(self, map={}):
        self.count = map.get('count')
        self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        self.worker_period = map.get('worker_period')
        self.worker_period_unit = map.get('worker_period_unit')
        self.worker_auto_renew = map.get('worker_auto_renew')
        self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        self.worker_system_disk_category = map.get('worker_system_disk_category')
        self.worker_system_disk_size = map.get('worker_system_disk_size')
        self.worker_data_disk = map.get('worker_data_disk')
        self.key_pair = map.get('key_pair')
        self.login_password = map.get('login_password')
        self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        self.cpu_policy = map.get('cpu_policy')
        self.disable_rollback = map.get('disable_rollback')
        self.image_id = map.get('image_id')
        self.user_data = map.get('user_data')
        if map.get('runtime') is not None:
            temp_model = ScaleOutClusterRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        else:
            self.runtime = None
        self.vswitch_ids = map.get('vswitch_ids')
        self.worker_instance_types = map.get('worker_instance_types')
        self.rds_instances = map.get('rds_instances')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = ScaleOutClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        else:
            self.worker_data_disks = None
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ScaleOutClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        else:
            self.tags = None
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = ScaleOutClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        else:
            self.taints = None
        return self


class ScaleOutClusterRequestRuntime(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器引擎名称。
        self.name = name                # type: str
        # 容器引擎版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.version = map.get('version')
        return self


class ScaleOutClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, size=None):
        # 数据盘类型。
        self.category = category        # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted      # type: str
        # 数据盘大小。
        self.size = size                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['category'] = self.category
        result['encrypted'] = self.encrypted
        result['size'] = self.size
        return result

    def from_map(self, map={}):
        self.category = map.get('category')
        self.encrypted = map.get('encrypted')
        self.size = map.get('size')
        return self


class ScaleOutClusterRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class ScaleOutClusterRequestTaints(TeaModel):
    def __init__(self, effect=None, key=None, value=None):
        # 污点生效策略。
        self.effect = effect            # type: str
        # 污点名。
        self.key = key                  # type: str
        # 污点值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['effect'] = self.effect
        result['key'] = self.key
        result['value'] = self.value
        return result

    def from_map(self, map={}):
        self.effect = map.get('effect')
        self.key = map.get('key')
        self.value = map.get('value')
        return self


class ScaleOutClusterResponseBody(TeaModel):
    def __init__(self, cluster_id=None, request_id=None, task_id=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 请求ID。
        self.request_id = request_id    # type: str
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['cluster_id'] = self.cluster_id
        result['request_id'] = self.request_id
        result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.cluster_id = map.get('cluster_id')
        self.request_id = map.get('request_id')
        self.task_id = map.get('task_id')
        return self


class ScaleOutClusterResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ScaleOutClusterResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScaleOutClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
        else:
            self.body = None
        return self


class UnInstallClusterAddonsRequest(TeaModel):
    def __init__(self, addons=None):
        # 卸载组件列表。
        self.addons = addons            # type: List[UnInstallClusterAddonsRequestAddons]

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        else:
            result['addons'] = None
        return result

    def from_map(self, map={}):
        self.addons = []
        if map.get('addons') is not None:
            for k in map.get('addons'):
                temp_model = UnInstallClusterAddonsRequestAddons()
                self.addons.append(temp_model.from_map(k))
        else:
            self.addons = None
        return self


class UnInstallClusterAddonsRequestAddons(TeaModel):
    def __init__(self, name=None):
        # 组件名称。
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        return self


class UnInstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, name=None, template=None, tags=None, description=None, template_type=None):
        # 部署模板名称。
        self.name = name                # type: str
        # 部署模板yaml。
        self.template = template        # type: str
        # 部署模板标签
        self.tags = tags                # type: str
        # 部署模板描述信息。
        self.description = description  # type: str
        # 部署模板类型。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['name'] = self.name
        result['template'] = self.template
        result['tags'] = self.tags
        result['description'] = self.description
        result['template_type'] = self.template_type
        return result

    def from_map(self, map={}):
        self.name = map.get('name')
        self.template = map.get('template')
        self.tags = map.get('tags')
        self.description = map.get('description')
        self.template_type = map.get('template_type')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(self, component_name=None, version=None, next_version=None):
        # 组件名称，集群升级时取值"k8s"。
        self.component_name = component_name  # type: str
        # 当前版本。
        self.version = version          # type: str
        # 目标版本。
        self.next_version = next_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['component_name'] = self.component_name
        result['version'] = self.version
        result['next_version'] = self.next_version
        return result

    def from_map(self, map={}):
        self.component_name = map.get('component_name')
        self.version = map.get('version')
        self.next_version = map.get('next_version')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self


class UpgradeClusterAddonsRequest(TeaModel):
    def __init__(self, body=None):
        # Request body，类型是对象数组。
        self.body = body                # type: List[UpgradeClusterAddonsRequestBody]

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        else:
            result['body'] = None
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = UpgradeClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        else:
            self.body = None
        return self


class UpgradeClusterAddonsRequestBody(TeaModel):
    def __init__(self, component_name=None, next_version=None, version=None):
        # 组件名称。
        self.component_name = component_name  # type: str
        # 可升级版本。
        self.next_version = next_version  # type: str
        # 当前版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        result['component_name'] = self.component_name
        result['next_version'] = self.next_version
        result['version'] = self.version
        return result

    def from_map(self, map={}):
        self.component_name = map.get('component_name')
        self.next_version = map.get('next_version')
        self.version = map.get('version')
        return self


class UpgradeClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        self.headers = map.get('headers')
        return self
