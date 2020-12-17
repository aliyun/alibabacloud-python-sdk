# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
try:
    from typing import List, Dict, Any
except ImportError:
    pass


class Taint(TeaModel):
    def __init__(self, key=None, value=None, effect=None):
        # key值。
        self.key = key                  # type: str
        # value值。
        self.value = value              # type: str
        # 污点生效策略。
        self.effect = effect            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        return self


class DataDisk(TeaModel):
    def __init__(self, category=None, size=None, encrypted=None, auto_snapshot_policy_id=None):
        # 数据盘类型
        self.category = category        # type: str
        # 数据盘大小，取值范围：40～32767
        self.size = size                # type: int
        # 是否对数据盘加密。
        self.encrypted = encrypted      # type: str
        # 开启云盘备份时的自动备份策略。
        self.auto_snapshot_policy_id = auto_snapshot_policy_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.size is not None:
            result['size'] = self.size
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('encrypted') is not None:
            self.encrypted = map.get('encrypted')
        if map.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = map.get('auto_snapshot_policy_id')
        return self


class DataDisks(TeaModel):
    def __init__(self, category=None, size=None, encrypted=None):
        # 数据盘类型。取值cloud,cloud-ssd等
        self.category = category        # type: str
        # 数据盘大小。最小值40，单位：GiB
        self.size = size                # type: int
        # 是否对数据盘加密。默认值：false。
        self.encrypted = encrypted      # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.size is not None:
            result['size'] = self.size
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('encrypted') is not None:
            self.encrypted = map.get('encrypted')
        return self


class Runtimes(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器运行时名称。
        self.name = name                # type: str
        # 容器运行时版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class Addon(TeaModel):
    def __init__(self, name=None, config=None, disabled=None):
        # 插件名称。
        self.name = name                # type: str
        # 插件配置参数。
        self.config = config            # type: str
        # 是否禁止默认安装。true | false。
        self.disabled = disabled        # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.config is not None:
            result['config'] = self.config
        if self.disabled is not None:
            result['disabled'] = self.disabled
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('config') is not None:
            self.config = map.get('config')
        if map.get('disabled') is not None:
            self.disabled = map.get('disabled')
        return self


class MaintenanceWindow(TeaModel):
    def __init__(self, enable=None, maintenance_time=None, duration=None, weekly_period=None):
        # 是否开启维护窗口。默认值false。
        self.enable = enable            # type: bool
        # 维护起始时间。Golang标准时间格式"15:04:05Z"。
        self.maintenance_time = maintenance_time  # type: str
        # 维护时长。取值范围1～24，单位为小时。 默认值：3h。
        self.duration = duration        # type: str
        # 维护周期。取值范围为:Monday~Sunday，多个值用逗号分隔。 默认值：Thursday。
        self.weekly_period = weekly_period  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.maintenance_time is not None:
            result['maintenance_time'] = self.maintenance_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.weekly_period is not None:
            result['weekly_period'] = self.weekly_period
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('maintenance_time') is not None:
            self.maintenance_time = map.get('maintenance_time')
        if map.get('duration') is not None:
            self.duration = map.get('duration')
        if map.get('weekly_period') is not None:
            self.weekly_period = map.get('weekly_period')
        return self


class Runtime(TeaModel):
    def __init__(self, name=None, version=None):
        # 容器运行时名称
        self.name = name                # type: str
        # 容器运行时版本
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class Taints(TeaModel):
    def __init__(self, key=None, value=None, effect=None):
        # 污点名。
        self.key = key                  # type: str
        # 污点值。
        self.value = value              # type: str
        # 污点生效策略。
        self.effect = effect            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        if self.effect is not None:
            result['effect'] = self.effect
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        return self


class Tag(TeaModel):
    def __init__(self, key=None, value=None):
        # key值。
        self.key = key                  # type: str
        # value值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class Tags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签名。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, resource_ids=None, tags=None, next_token=None):
        # 集群ID列表。
        self.resource_ids = resource_ids  # type: List[str]
        # 按标签查找。
        self.tags = tags                # type: List[ListTagResourcesRequestTags]
        # 下一次查询Token。
        self.next_token = next_token    # type: str

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['next_token'] = self.next_token
        return result

    def from_map(self, map={}):
        if map.get('resource_ids') is not None:
            self.resource_ids = map.get('resource_ids')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ListTagResourcesRequestTags()
                self.tags.append(temp_model.from_map(k))
        if map.get('next_token') is not None:
            self.next_token = map.get('next_token')
        return self


class ListTagResourcesRequestTags(TeaModel):
    def __init__(self, key=None, value=None):
        # 标签key。
        self.key = key                  # type: str
        # 标签值。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # 下一个查询token。
        self.next_token = next_token    # type: str
        # 请求ID。
        self.request_id = request_id    # type: str
        # 资源标签列表。
        self.tag_resources = tag_resources  # type: ListTagResourcesResponseBodyTagResources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        result = {}
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.tag_resources is not None:
            result['tag_resources'] = self.tag_resources.to_map()
        return result

    def from_map(self, map={}):
        if map.get('next_token') is not None:
            self.next_token = map.get('next_token')
        if map.get('request_id') is not None:
            self.request_id = map.get('request_id')
        if map.get('tag_resources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(map['tag_resources'])
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(self, tag_key=None, tag_value=None, resource_id=None, resource_type=None):
        # 标签key。
        self.tag_key = tag_key          # type: str
        # 标签值。
        self.tag_value = tag_value      # type: str
        # 资源ID。
        self.resource_id = resource_id  # type: str
        # 资源类型。
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        return result

    def from_map(self, map={}):
        if map.get('tag_key') is not None:
            self.tag_key = map.get('tag_key')
        if map.get('tag_value') is not None:
            self.tag_value = map.get('tag_value')
        if map.get('resource_id') is not None:
            self.resource_id = map.get('resource_id')
        if map.get('resource_type') is not None:
            self.resource_type = map.get('resource_type')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, tag_resource=None):
        # 资源标签。
        self.tag_resource = tag_resource  # type: List[ListTagResourcesResponseBodyTagResourcesTagResource]

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['tag_resource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['tag_resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.tag_resource = []
        if map.get('tag_resource') is not None:
            for k in map.get('tag_resource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(self, api_server_eip=None, api_server_eip_id=None, deletion_protection=None,
                 instance_deletion_protection=None, ingress_domain_rebinding=None, ingress_loadbalancer_id=None, resource_group_id=None,
                 maintenance_window=None):
        # 集群是否绑定EIP，用于公网访问API Server。 true | false
        self.api_server_eip = api_server_eip  # type: bool
        # 集群API Server 公网连接端点。
        self.api_server_eip_id = api_server_eip_id  # type: str
        # 集群是否开启删除保护。默认值false。
        self.deletion_protection = deletion_protection  # type: bool
        # 实例删除保护，防止通过控制台或API误删除释放节点。
        self.instance_deletion_protection = instance_deletion_protection  # type: bool
        # 域名是否重新绑定到Ingress的SLB地址。
        self.ingress_domain_rebinding = ingress_domain_rebinding  # type: str
        # 集群的Ingress SLB的ID。
        self.ingress_loadbalancer_id = ingress_loadbalancer_id  # type: str
        # 集群资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()

    def to_map(self):
        result = {}
        if self.api_server_eip is not None:
            result['api_server_eip'] = self.api_server_eip
        if self.api_server_eip_id is not None:
            result['api_server_eip_id'] = self.api_server_eip_id
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.instance_deletion_protection is not None:
            result['instance_deletion_protection'] = self.instance_deletion_protection
        if self.ingress_domain_rebinding is not None:
            result['ingress_domain_rebinding'] = self.ingress_domain_rebinding
        if self.ingress_loadbalancer_id is not None:
            result['ingress_loadbalancer_id'] = self.ingress_loadbalancer_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        return result

    def from_map(self, map={}):
        if map.get('api_server_eip') is not None:
            self.api_server_eip = map.get('api_server_eip')
        if map.get('api_server_eip_id') is not None:
            self.api_server_eip_id = map.get('api_server_eip_id')
        if map.get('deletion_protection') is not None:
            self.deletion_protection = map.get('deletion_protection')
        if map.get('instance_deletion_protection') is not None:
            self.instance_deletion_protection = map.get('instance_deletion_protection')
        if map.get('ingress_domain_rebinding') is not None:
            self.ingress_domain_rebinding = map.get('ingress_domain_rebinding')
        if map.get('ingress_loadbalancer_id') is not None:
            self.ingress_loadbalancer_id = map.get('ingress_loadbalancer_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(map['maintenance_window'])
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('request_id') is not None:
            self.request_id = map.get('request_id')
        if map.get('task_id') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        if self.arch is not None:
            result['arch'] = self.arch
        if self.options is not None:
            result['options'] = self.options.to_map()
        return result

    def from_map(self, map={}):
        if map.get('arch') is not None:
            self.arch = map.get('arch')
        if map.get('options') is not None:
            temp_model = DescribeClusterAttachScriptsRequestOptions()
            self.options = temp_model.from_map(map['options'])
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
        if self.allowed_cluster_addons is not None:
            result['allowedClusterAddons'] = self.allowed_cluster_addons
        if self.enable_iptables is not None:
            result['enableIptables'] = self.enable_iptables
        if self.flannel_iface is not None:
            result['flannelIface'] = self.flannel_iface
        if self.gpu_version is not None:
            result['gpuVersion'] = self.gpu_version
        if self.manage_runtime is not None:
            result['manageRuntime'] = self.manage_runtime
        if self.node_name_override is not None:
            result['nodeNameOverride'] = self.node_name_override
        if self.quiet is not None:
            result['quiet'] = self.quiet
        return result

    def from_map(self, map={}):
        if map.get('allowedClusterAddons') is not None:
            self.allowed_cluster_addons = map.get('allowedClusterAddons')
        if map.get('enableIptables') is not None:
            self.enable_iptables = map.get('enableIptables')
        if map.get('flannelIface') is not None:
            self.flannel_iface = map.get('flannelIface')
        if map.get('gpuVersion') is not None:
            self.gpu_version = map.get('gpuVersion')
        if map.get('manageRuntime') is not None:
            self.manage_runtime = map.get('manageRuntime')
        if map.get('nodeNameOverride') is not None:
            self.node_name_override = map.get('nodeNameOverride')
        if map.get('quiet') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            self.body = map.get('body')
        return self


class DescribeKubernetesVersionMetadataRequest(TeaModel):
    def __init__(self, region=None, cluster_type=None, multi_az=None, kubernetes_version=None, profile=None):
        # 地域ID。
        self.region = region            # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 是否查询多可用区。
        self.multi_az = multi_az        # type: bool
        # 要查询的版本，如果为空则查所有版本。
        self.kubernetes_version = kubernetes_version  # type: str
        # 边缘集群标识，用于区分边缘集群，取值：Default或Edge。
        self.profile = profile          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.region is not None:
            result['Region'] = self.region
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.multi_az is not None:
            result['MultiAZ'] = self.multi_az
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        if self.profile is not None:
            result['Profile'] = self.profile
        return result

    def from_map(self, map={}):
        if map.get('Region') is not None:
            self.region = map.get('Region')
        if map.get('ClusterType') is not None:
            self.cluster_type = map.get('ClusterType')
        if map.get('MultiAZ') is not None:
            self.multi_az = map.get('MultiAZ')
        if map.get('KubernetesVersion') is not None:
            self.kubernetes_version = map.get('KubernetesVersion')
        if map.get('Profile') is not None:
            self.profile = map.get('Profile')
        return self


class DescribeKubernetesVersionMetadataResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: List[DescribeKubernetesVersionMetadataResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeKubernetesVersionMetadataResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeKubernetesVersionMetadataResponseBodyImages(TeaModel):
    def __init__(self, image_id=None, image_name=None, platform=None, os_version=None, image_type=None, os_type=None,
                 image_category=None):
        # 镜像ID。	
        self.image_id = image_id        # type: str
        # 镜像名称。	
        self.image_name = image_name    # type: str
        # 操作系统发行版。取值范围： CentOS,AliyunLinux,Windows,WindowsCore。
        self.platform = platform        # type: str
        # 镜像版本。
        self.os_version = os_version    # type: str
        # 镜像类型。	
        self.image_type = image_type    # type: str
        # 操作系统发行版本号。
        self.os_type = os_type          # type: str
        # 镜像分类
        self.image_category = image_category  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.image_name is not None:
            result['image_name'] = self.image_name
        if self.platform is not None:
            result['platform'] = self.platform
        if self.os_version is not None:
            result['os_version'] = self.os_version
        if self.image_type is not None:
            result['image_type'] = self.image_type
        if self.os_type is not None:
            result['os_type'] = self.os_type
        if self.image_category is not None:
            result['image_category'] = self.image_category
        return result

    def from_map(self, map={}):
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('image_name') is not None:
            self.image_name = map.get('image_name')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('os_version') is not None:
            self.os_version = map.get('os_version')
        if map.get('image_type') is not None:
            self.image_type = map.get('image_type')
        if map.get('os_type') is not None:
            self.os_type = map.get('os_type')
        if map.get('image_category') is not None:
            self.image_category = map.get('image_category')
        return self


class DescribeKubernetesVersionMetadataResponseBody(TeaModel):
    def __init__(self, capabilities=None, images=None, meta_data=None, runtimes=None, version=None, multi_az=None):
        # Kubernetes版本特性。	
        self.capabilities = capabilities  # type: Dict[str, Any]
        # ECS系统镜像列表。	
        self.images = images            # type: List[DescribeKubernetesVersionMetadataResponseBodyImages]
        # Kubernetes版本元数据信息。	
        self.meta_data = meta_data      # type: Dict[str, Any]
        # 容器运行时详情。	
        self.runtimes = runtimes        # type: List[Runtimes]
        # Kubernetes版本。	
        self.version = version          # type: str
        # 是否为多可用区。
        self.multi_az = multi_az        # type: str

    def validate(self):
        if self.images:
            for k in self.images:
                if k:
                    k.validate()
        if self.runtimes:
            for k in self.runtimes:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.capabilities is not None:
            result['capabilities'] = self.capabilities
        result['images'] = []
        if self.images is not None:
            for k in self.images:
                result['images'].append(k.to_map() if k else None)
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        result['runtimes'] = []
        if self.runtimes is not None:
            for k in self.runtimes:
                result['runtimes'].append(k.to_map() if k else None)
        if self.version is not None:
            result['version'] = self.version
        if self.multi_az is not None:
            result['multi_az'] = self.multi_az
        return result

    def from_map(self, map={}):
        if map.get('capabilities') is not None:
            self.capabilities = map.get('capabilities')
        self.images = []
        if map.get('images') is not None:
            for k in map.get('images'):
                temp_model = DescribeKubernetesVersionMetadataResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if map.get('meta_data') is not None:
            self.meta_data = map.get('meta_data')
        self.runtimes = []
        if map.get('runtimes') is not None:
            for k in map.get('runtimes'):
                temp_model = Runtimes()
                self.runtimes.append(temp_model.from_map(k))
        if map.get('version') is not None:
            self.version = map.get('version')
        if map.get('multi_az') is not None:
            self.multi_az = map.get('multi_az')
        return self


class DescribeClusterLogsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: List[DescribeClusterLogsResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeClusterLogsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClusterLogsResponseBody(TeaModel):
    def __init__(self, id=None, cluster_id=None, cluster_log=None, created=None, log_level=None, updated=None):
        # 日志ID。
        self.id = id                    # type: int
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群日志。
        self.cluster_log = cluster_log  # type: str
        # 日志创建时间。
        self.created = created          # type: str
        # 日志等级。
        self.log_level = log_level      # type: str
        # 日志更新时间。
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.id is not None:
            result['ID'] = self.id
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_log is not None:
            result['cluster_log'] = self.cluster_log
        if self.created is not None:
            result['created'] = self.created
        if self.log_level is not None:
            result['log_level'] = self.log_level
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, map={}):
        if map.get('ID') is not None:
            self.id = map.get('ID')
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('cluster_log') is not None:
            self.cluster_log = map.get('cluster_log')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('log_level') is not None:
            self.log_level = map.get('log_level')
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        return self


class CreateKubernetesTriggerRequest(TeaModel):
    def __init__(self, action=None, cluster_id=None, project_id=None, region_id=None, type=None):
        # 触发器行为。
        self.action = action            # type: str
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 项目名称。
        self.project_id = project_id    # type: str
        # 地域ID。
        self.region_id = region_id      # type: str
        # 触发器类型。
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.action is not None:
            result['Action'] = self.action
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('Action') is not None:
            self.action = map.get('Action')
        if map.get('ClusterId') is not None:
            self.cluster_id = map.get('ClusterId')
        if map.get('ProjectId') is not None:
            self.project_id = map.get('ProjectId')
        if map.get('RegionId') is not None:
            self.region_id = map.get('RegionId')
        if map.get('Type') is not None:
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
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        return result

    def from_map(self, map={}):
        if map.get('action') is not None:
            self.action = map.get('action')
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('project_id') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeClusterDetailResponseBody(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, created=None, init_version=None, current_version=None,
                 next_version=None, deletion_protection=None, docker_version=None, external_loadbalancer_id=None,
                 meta_data=None, name=None, network_mode=None, region_id=None, resource_group_id=None, security_group_id=None,
                 size=None, state=None, tags=None, updated=None, vpc_id=None, vswitch_id=None, subnet_cidr=None,
                 zone_id=None, master_url=None, private_zone=None, profile=None, cluster_spec=None,
                 worker_ram_role_name=None, maintenance_window=None, parameters=None, outputs=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群创建时间。
        self.created = created          # type: str
        # 集群初始化版本。
        self.init_version = init_version  # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 集群可升级版本。
        self.next_version = next_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群内Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群Ingress LB实例ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
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
        self.tags = tags                # type: List[Tags]
        # 集群更新时间。
        self.updated = updated          # type: str
        # 集群使用的VPC ID。
        self.vpc_id = vpc_id            # type: str
        # 集群节点使用的虚拟交换机列表。
        self.vswitch_id = vswitch_id    # type: str
        # Pod网络地址段，必须是有效的私有网段，即以下网段及其子网：10.0.0.0/8，172.16-31.0.0/12-16，192.168.0.0/16。不能与 VPC 及VPC 内已有 Kubernetes 集群使用的网段重复，创建成功后不能修改。  有关集群网络规划，请参见：[VPC下 Kubernetes 的网络地址段规划](https://help.aliyun.com/document_detail/～～86500～～)。
        self.subnet_cidr = subnet_cidr  # type: str
        # 集群所在地域内的可用区ID。
        self.zone_id = zone_id          # type: str
        # 集群访问地址。
        self.master_url = master_url    # type: str
        # 集群是否启用用PrivateZone。  true：启用 false：不启用 默认值：false。
        self.private_zone = private_zone  # type: bool
        # 面向场景时的集群类型。  Default：非边缘场景集群。 Edge：边缘场景集群。
        self.profile = profile          # type: str
        # 托管版集群类型，面向托管集群。  ack.pro.small：专业托管集群。 ack.standard ：标准托管集群。
        self.cluster_spec = cluster_spec  # type: str
        # Worker节点RAM角色名称。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow
        # 创建集群参数。
        self.parameters = parameters    # type: Dict[str, Any]
        # 集群创建的资源列表。
        self.outputs = outputs          # type: List[DescribeClusterDetailResponseBodyOutputs]

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.outputs:
            for k in self.outputs:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.parameters is not None:
            result['parameters'] = self.parameters
        result['outputs'] = []
        if self.outputs is not None:
            for k in self.outputs:
                result['outputs'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('init_version') is not None:
            self.init_version = map.get('init_version')
        if map.get('current_version') is not None:
            self.current_version = map.get('current_version')
        if map.get('next_version') is not None:
            self.next_version = map.get('next_version')
        if map.get('deletion_protection') is not None:
            self.deletion_protection = map.get('deletion_protection')
        if map.get('docker_version') is not None:
            self.docker_version = map.get('docker_version')
        if map.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        if map.get('meta_data') is not None:
            self.meta_data = map.get('meta_data')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('network_mode') is not None:
            self.network_mode = map.get('network_mode')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('state') is not None:
            self.state = map.get('state')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = Tags()
                self.tags.append(temp_model.from_map(k))
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        if map.get('vpc_id') is not None:
            self.vpc_id = map.get('vpc_id')
        if map.get('vswitch_id') is not None:
            self.vswitch_id = map.get('vswitch_id')
        if map.get('subnet_cidr') is not None:
            self.subnet_cidr = map.get('subnet_cidr')
        if map.get('zone_id') is not None:
            self.zone_id = map.get('zone_id')
        if map.get('master_url') is not None:
            self.master_url = map.get('master_url')
        if map.get('private_zone') is not None:
            self.private_zone = map.get('private_zone')
        if map.get('profile') is not None:
            self.profile = map.get('profile')
        if map.get('cluster_spec') is not None:
            self.cluster_spec = map.get('cluster_spec')
        if map.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = map.get('worker_ram_role_name')
        if map.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(map['maintenance_window'])
        if map.get('parameters') is not None:
            self.parameters = map.get('parameters')
        self.outputs = []
        if map.get('outputs') is not None:
            for k in map.get('outputs'):
                temp_model = DescribeClusterDetailResponseBodyOutputs()
                self.outputs.append(temp_model.from_map(k))
        return self


class DescribeClusterDetailResponseBodyOutputs(TeaModel):
    def __init__(self, output_key=None, output_value=None, description=None):
        # 资源ID。
        self.output_key = output_key    # type: str
        # 资源名称。
        self.output_value = output_value  # type: str
        # 资源描述。
        self.description = description  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.output_key is not None:
            result['OutputKey'] = self.output_key
        if self.output_value is not None:
            result['OutputValue'] = self.output_value
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, map={}):
        if map.get('OutputKey') is not None:
            self.output_key = map.get('OutputKey')
        if map.get('OutputValue') is not None:
            self.output_value = map.get('OutputValue')
        if map.get('Description') is not None:
            self.description = map.get('Description')
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterDetailResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class PauseComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
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
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('clusterType') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeClustersResponseBody()
                self.body.append(temp_model.from_map(k))
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
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.data_disk_category is not None:
            result['data_disk_category'] = self.data_disk_category
        if self.data_disk_size is not None:
            result['data_disk_size'] = self.data_disk_size
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_cidr is not None:
            result['vswitch_cidr'] = self.vswitch_cidr
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('current_version') is not None:
            self.current_version = map.get('current_version')
        if map.get('data_disk_category') is not None:
            self.data_disk_category = map.get('data_disk_category')
        if map.get('data_disk_size') is not None:
            self.data_disk_size = map.get('data_disk_size')
        if map.get('deletion_protection') is not None:
            self.deletion_protection = map.get('deletion_protection')
        if map.get('docker_version') is not None:
            self.docker_version = map.get('docker_version')
        if map.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        if map.get('init_version') is not None:
            self.init_version = map.get('init_version')
        if map.get('master_url') is not None:
            self.master_url = map.get('master_url')
        if map.get('meta_data') is not None:
            self.meta_data = map.get('meta_data')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('network_mode') is not None:
            self.network_mode = map.get('network_mode')
        if map.get('private_zone') is not None:
            self.private_zone = map.get('private_zone')
        if map.get('profile') is not None:
            self.profile = map.get('profile')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('subnet_cidr') is not None:
            self.subnet_cidr = map.get('subnet_cidr')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = DescribeClustersResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        if map.get('vpc_id') is not None:
            self.vpc_id = map.get('vpc_id')
        if map.get('vswitch_cidr') is not None:
            self.vswitch_cidr = map.get('vswitch_cidr')
        if map.get('vswitch_id') is not None:
            self.vswitch_id = map.get('vswitch_id')
        if map.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = map.get('worker_ram_role_name')
        if map.get('zone_id') is not None:
            self.zone_id = map.get('zone_id')
        return self


class ModifyClusterNodePoolRequest(TeaModel):
    def __init__(self, auto_scaling=None, kubernetes_config=None, nodepool_info=None, scaling_group=None,
                 tee_config=None, management=None, update_nodes=None):
        # 自动伸缩节点池配置。
        self.auto_scaling = auto_scaling  # type: ModifyClusterNodePoolRequestAutoScaling
        # 集群配置。
        self.kubernetes_config = kubernetes_config  # type: ModifyClusterNodePoolRequestKubernetesConfig
        # 节点池配置。
        self.nodepool_info = nodepool_info  # type: ModifyClusterNodePoolRequestNodepoolInfo
        # 扩容组配置。
        self.scaling_group = scaling_group  # type: ModifyClusterNodePoolRequestScalingGroup
        # 加密计算配置。
        self.tee_config = tee_config    # type: ModifyClusterNodePoolRequestTeeConfig
        # 托管版节点池配置。
        self.management = management    # type: ModifyClusterNodePoolRequestManagement
        # 是否同步更新节点标签及污点。
        self.update_nodes = update_nodes  # type: bool

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()
        if self.management:
            self.management.validate()

    def to_map(self):
        result = {}
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.update_nodes is not None:
            result['update_nodes'] = self.update_nodes
        return result

    def from_map(self, map={}):
        if map.get('auto_scaling') is not None:
            temp_model = ModifyClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(map['auto_scaling'])
        if map.get('kubernetes_config') is not None:
            temp_model = ModifyClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(map['kubernetes_config'])
        if map.get('nodepool_info') is not None:
            temp_model = ModifyClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(map['nodepool_info'])
        if map.get('scaling_group') is not None:
            temp_model = ModifyClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(map['scaling_group'])
        if map.get('tee_config') is not None:
            temp_model = ModifyClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(map['tee_config'])
        if map.get('management') is not None:
            temp_model = ModifyClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(map['management'])
        if map.get('update_nodes') is not None:
            self.update_nodes = map.get('update_nodes')
        return self


class ModifyClusterNodePoolRequestAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # 带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: int
        # EIP计费类型。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 是否开启自动伸缩。
        self.enable = enable            # type: bool
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: int
        # 最小实例数。
        self.min_instances = min_instances  # type: int
        # 自动伸缩节点类型。
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('eip_bandwidth') is not None:
            self.eip_bandwidth = map.get('eip_bandwidth')
        if map.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = map.get('eip_internet_charge_type')
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('is_bond_eip') is not None:
            self.is_bond_eip = map.get('is_bond_eip')
        if map.get('max_instances') is not None:
            self.max_instances = map.get('max_instances')
        if map.get('min_instances') is not None:
            self.min_instances = map.get('min_instances')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class ModifyClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控。
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略。
        self.cpu_policy = cpu_policy    # type: str
        # 节点标签。
        self.labels = labels            # type: List[Tags]
        # 容器运行时。
        self.runtime = runtime          # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点配置。
        self.taints = taints            # type: List[Taints]
        # 实例自定义数据。
        self.user_data = user_data      # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, map={}):
        if map.get('cms_enabled') is not None:
            self.cms_enabled = map.get('cms_enabled')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                temp_model = Tags()
                self.labels.append(temp_model.from_map(k))
        if map.get('runtime') is not None:
            self.runtime = map.get('runtime')
        if map.get('runtime_version') is not None:
            self.runtime_version = map.get('runtime_version')
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = Taints()
                self.taints.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        return self


class ModifyClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(self, name=None, resource_group_id=None):
        # 节点池名称。
        self.name = name                # type: str
        # 资源组ID。
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        return self


class ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, map={}):
        if map.get('instance_type') is not None:
            self.instance_type = map.get('instance_type')
        if map.get('price_limit') is not None:
            self.price_limit = map.get('price_limit')
        return self


class ModifyClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(self, data_disks=None, instance_charge_type=None, period=None, period_unit=None, auto_renew=None,
                 auto_renew_period=None, platform=None, image_id=None, spot_strategy=None, spot_price_limit=None, instance_types=None,
                 key_pair=None, login_password=None, rds_instances=None, scaling_policy=None, system_disk_category=None,
                 system_disk_size=None, tags=None, vswitch_ids=None):
        # 数据盘配置。
        self.data_disks = data_disks    # type: List[DataDisks]
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 包年包月时长
        self.period = period            # type: int
        # 付费周期
        self.period_unit = period_unit  # type: str
        # 节点池节点是启用自动续费
        self.auto_renew = auto_renew    # type: bool
        # 节点池节点自动续费周期
        self.auto_renew_period = auto_renew_period  # type: int
        # 操作系统发行版。
        self.platform = platform        # type: str
        # 自定义镜像
        self.image_id = image_id        # type: str
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 抢占实例价格上限配置
        self.spot_price_limit = spot_price_limit  # type: List[ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit]
        # 节点实例规格。
        self.instance_types = instance_types  # type: List[str]
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码，和key_pari二选一。
        self.login_password = login_password  # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 扩容策略。
        self.scaling_policy = scaling_policy  # type: str
        # 节点系统盘类型。
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘大小。
        self.system_disk_size = system_disk_size  # type: int
        # ECS标签。
        self.tags = tags                # type: List[Tags]
        # 节点使用的虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: List[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.platform is not None:
            result['platform'] = self.platform
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, map={}):
        self.data_disks = []
        if map.get('data_disks') is not None:
            for k in map.get('data_disks'):
                temp_model = DataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if map.get('instance_charge_type') is not None:
            self.instance_charge_type = map.get('instance_charge_type')
        if map.get('period') is not None:
            self.period = map.get('period')
        if map.get('period_unit') is not None:
            self.period_unit = map.get('period_unit')
        if map.get('auto_renew') is not None:
            self.auto_renew = map.get('auto_renew')
        if map.get('auto_renew_period') is not None:
            self.auto_renew_period = map.get('auto_renew_period')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('spot_strategy') is not None:
            self.spot_strategy = map.get('spot_strategy')
        self.spot_price_limit = []
        if map.get('spot_price_limit') is not None:
            for k in map.get('spot_price_limit'):
                temp_model = ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if map.get('instance_types') is not None:
            self.instance_types = map.get('instance_types')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('scaling_policy') is not None:
            self.scaling_policy = map.get('scaling_policy')
        if map.get('system_disk_category') is not None:
            self.system_disk_category = map.get('system_disk_category')
        if map.get('system_disk_size') is not None:
            self.system_disk_size = map.get('system_disk_size')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = Tags()
                self.tags.append(temp_model.from_map(k))
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        return self


class ModifyClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable    # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, map={}):
        if map.get('tee_enable') is not None:
            self.tee_enable = map.get('tee_enable')
        return self


class ModifyClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, surge=None, surge_percentage=None, max_unavailable=None):
        # 是否启用自动升级，自修复。
        self.auto_upgrade = auto_upgrade  # type: bool
        # 额外节点数量。
        self.surge = surge              # type: int
        # 额外节点比例， 和surge 二选一。
        self.surge_percentage = surge_percentage  # type: int
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        return result

    def from_map(self, map={}):
        if map.get('auto_upgrade') is not None:
            self.auto_upgrade = map.get('auto_upgrade')
        if map.get('surge') is not None:
            self.surge = map.get('surge')
        if map.get('surge_percentage') is not None:
            self.surge_percentage = map.get('surge_percentage')
        if map.get('max_unavailable') is not None:
            self.max_unavailable = map.get('max_unavailable')
        return self


class ModifyClusterNodePoolRequestManagement(TeaModel):
    def __init__(self, enable=None, auto_repair=None, upgrade_config=None):
        # 是否启用托管节点池。
        self.enable = enable            # type: bool
        # 是否开启自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: ModifyClusterNodePoolRequestManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('auto_repair') is not None:
            self.auto_repair = map.get('auto_repair')
        if map.get('upgrade_config') is not None:
            temp_model = ModifyClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(map['upgrade_config'])
        return self


class ModifyClusterNodePoolResponseBody(TeaModel):
    def __init__(self, task_id=None, nodepool_id=None):
        # 任务ID。
        self.task_id = task_id          # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        return result

    def from_map(self, map={}):
        if map.get('task_id') is not None:
            self.task_id = map.get('task_id')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        return self


class ModifyClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ModifyClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ModifyClusterNodePoolResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ResumeUpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class ScaleClusterNodePoolRequest(TeaModel):
    def __init__(self, count=None):
        # 扩容节点数量
        self.count = count              # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, map={}):
        if map.get('count') is not None:
            self.count = map.get('count')
        return self


class ScaleClusterNodePoolResponseBody(TeaModel):
    def __init__(self, task_id=None):
        # 任务ID。
        self.task_id = task_id          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('task_id') is not None:
            self.task_id = map.get('task_id')
        return self


class ScaleClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: ScaleClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScaleClusterNodePoolResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeClusterNodePoolDetailResponseBody(TeaModel):
    def __init__(self, auto_scaling=None, kubernetes_config=None, nodepool_info=None, scaling_group=None,
                 status=None, tee_config=None, management=None):
        # 节点池自动伸缩信息。
        self.auto_scaling = auto_scaling  # type: DescribeClusterNodePoolDetailResponseBodyAutoScaling
        # 节点池所属集群配置。
        self.kubernetes_config = kubernetes_config  # type: DescribeClusterNodePoolDetailResponseBodyKubernetesConfig
        # 节点池详情。
        self.nodepool_info = nodepool_info  # type: DescribeClusterNodePoolDetailResponseBodyNodepoolInfo
        # 节点池扩容组信息。
        self.scaling_group = scaling_group  # type: DescribeClusterNodePoolDetailResponseBodyScalingGroup
        # 节点池状态。
        self.status = status            # type: DescribeClusterNodePoolDetailResponseBodyStatus
        # 加密计算节点池信息。
        self.tee_config = tee_config    # type: DescribeClusterNodePoolDetailResponseBodyTeeConfig
        # 托管版节点池配置。
        self.management = management    # type: DescribeClusterNodePoolDetailResponseBodyManagement

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()
        if self.management:
            self.management.validate()

    def to_map(self):
        result = {}
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        return result

    def from_map(self, map={}):
        if map.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyAutoScaling()
            self.auto_scaling = temp_model.from_map(map['auto_scaling'])
        if map.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(map['kubernetes_config'])
        if map.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyNodepoolInfo()
            self.nodepool_info = temp_model.from_map(map['nodepool_info'])
        if map.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroup()
            self.scaling_group = temp_model.from_map(map['scaling_group'])
        if map.get('status') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyStatus()
            self.status = temp_model.from_map(map['status'])
        if map.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyTeeConfig()
            self.tee_config = temp_model.from_map(map['tee_config'])
        if map.get('management') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagement()
            self.management = temp_model.from_map(map['management'])
        return self


class DescribeClusterNodePoolDetailResponseBodyAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, eip_internet_charge_type=None, enable=None, is_bond_eip=None,
                 max_instances=None, min_instances=None, type=None):
        # EIP带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: int
        # EIP实例付费类型。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 是否启用自动伸缩。
        self.enable = enable            # type: bool
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: int
        # 最小实例数。
        self.min_instances = min_instances  # type: int
        # 扩容组类型
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('eip_bandwidth') is not None:
            self.eip_bandwidth = map.get('eip_bandwidth')
        if map.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = map.get('eip_internet_charge_type')
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('is_bond_eip') is not None:
            self.is_bond_eip = map.get('is_bond_eip')
        if map.get('max_instances') is not None:
            self.max_instances = map.get('max_instances')
        if map.get('min_instances') is not None:
            self.min_instances = map.get('min_instances')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class DescribeClusterNodePoolDetailResponseBodyKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略
        self.cpu_policy = cpu_policy    # type: str
        # 节点标签。
        self.labels = labels            # type: List[Tags]
        # 容器运行时
        self.runtime = runtime          # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点配置。
        self.taints = taints            # type: List[Taints]
        # 节点自定义数据
        self.user_data = user_data      # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, map={}):
        if map.get('cms_enabled') is not None:
            self.cms_enabled = map.get('cms_enabled')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                temp_model = Tags()
                self.labels.append(temp_model.from_map(k))
        if map.get('runtime') is not None:
            self.runtime = map.get('runtime')
        if map.get('runtime_version') is not None:
            self.runtime_version = map.get('runtime_version')
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = Taints()
                self.taints.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        return self


class DescribeClusterNodePoolDetailResponseBodyNodepoolInfo(TeaModel):
    def __init__(self, created=None, is_default=None, name=None, nodepool_id=None, region_id=None,
                 resource_group_id=None, type=None, updated=None):
        # 节点池创建时间。
        self.created = created          # type: str
        # 是否为默认节点池。
        self.is_default = is_default    # type: bool
        # 节点池名称。
        self.name = name                # type: str
        # 节点池ID。
        self.nodepool_id = nodepool_id  # type: str
        # 节点池所属地域ID。
        self.region_id = region_id      # type: str
        # 节点池所属资源组ID。
        self.resource_group_id = resource_group_id  # type: str
        # 节点池类型。
        self.type = type                # type: str
        # 节点池更新时间。
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('is_default') is not None:
            self.is_default = map.get('is_default')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        return self


class DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格。
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, map={}):
        if map.get('instance_type') is not None:
            self.instance_type = map.get('instance_type')
        if map.get('price_limit') is not None:
            self.price_limit = map.get('price_limit')
        return self


class DescribeClusterNodePoolDetailResponseBodyScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, data_disks=None, image_id=None,
                 instance_charge_type=None, instance_types=None, multi_az_policy=None, period=None, period_unit=None, platform=None,
                 ram_policy=None, spot_strategy=None, spot_price_limit=None, rds_instances=None, scaling_group_id=None,
                 scaling_policy=None, security_group_id=None, system_disk_category=None, system_disk_size=None, tags=None,
                 vswitch_ids=None, login_password=None, key_pair=None):
        # 节点是否开启自动续费。
        self.auto_renew = auto_renew    # type: bool
        # 节点自动续费周期。
        self.auto_renew_period = auto_renew_period  # type: int
        # 数据盘配置。
        self.data_disks = data_disks    # type: List[DataDisks]
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # 节点付费类型。
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点ECS规格类型。
        self.instance_types = instance_types  # type: List[str]
        # 多可用区策略。
        self.multi_az_policy = multi_az_policy  # type: str
        # 节点包年包月时长。
        self.period = period            # type: int
        # 节点付费周期。
        self.period_unit = period_unit  # type: str
        # 操作系统发行版。取值： CentOS，AliyunLinux，Windows，WindowsCore。
        self.platform = platform        # type: str
        # 节点RAM 角色名称。
        self.ram_policy = ram_policy    # type: str
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 抢占式实例价格上限配置。
        self.spot_price_limit = spot_price_limit  # type: List[DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit]
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 扩容组ID。
        self.scaling_group_id = scaling_group_id  # type: str
        # 扩容策略。
        self.scaling_policy = scaling_policy  # type: str
        # 节点所属安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 系统盘类型
        self.system_disk_category = system_disk_category  # type: str
        # 系统盘大小
        self.system_disk_size = system_disk_size  # type: int
        # ECS标签
        self.tags = tags                # type: List[Tags]
        # 虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # 登录密码
        self.login_password = login_password  # type: str
        # 密钥对名称
        self.key_pair = key_pair        # type: str

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        return result

    def from_map(self, map={}):
        if map.get('auto_renew') is not None:
            self.auto_renew = map.get('auto_renew')
        if map.get('auto_renew_period') is not None:
            self.auto_renew_period = map.get('auto_renew_period')
        self.data_disks = []
        if map.get('data_disks') is not None:
            for k in map.get('data_disks'):
                temp_model = DataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instance_charge_type') is not None:
            self.instance_charge_type = map.get('instance_charge_type')
        if map.get('instance_types') is not None:
            self.instance_types = map.get('instance_types')
        if map.get('multi_az_policy') is not None:
            self.multi_az_policy = map.get('multi_az_policy')
        if map.get('period') is not None:
            self.period = map.get('period')
        if map.get('period_unit') is not None:
            self.period_unit = map.get('period_unit')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('ram_policy') is not None:
            self.ram_policy = map.get('ram_policy')
        if map.get('spot_strategy') is not None:
            self.spot_strategy = map.get('spot_strategy')
        self.spot_price_limit = []
        if map.get('spot_price_limit') is not None:
            for k in map.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('scaling_group_id') is not None:
            self.scaling_group_id = map.get('scaling_group_id')
        if map.get('scaling_policy') is not None:
            self.scaling_policy = map.get('scaling_policy')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('system_disk_category') is not None:
            self.system_disk_category = map.get('system_disk_category')
        if map.get('system_disk_size') is not None:
            self.system_disk_size = map.get('system_disk_size')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = Tags()
                self.tags.append(temp_model.from_map(k))
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        return self


class DescribeClusterNodePoolDetailResponseBodyStatus(TeaModel):
    def __init__(self, failed_nodes=None, healthy_nodes=None, initial_nodes=None, offline_nodes=None,
                 removing_nodes=None, serving_nodes=None, state=None, total_nodes=None):
        # 失败节点数。
        self.failed_nodes = failed_nodes  # type: int
        # 处于健康状态节点数。
        self.healthy_nodes = healthy_nodes  # type: int
        # 正在初始化节点数。
        self.initial_nodes = initial_nodes  # type: int
        # 离线节点数量。
        self.offline_nodes = offline_nodes  # type: int
        # 正在被移除节点数。
        self.removing_nodes = removing_nodes  # type: int
        # 工作节点数量。
        self.serving_nodes = serving_nodes  # type: int
        # 节点池状态。
        self.state = state              # type: str
        # 总节点数。
        self.total_nodes = total_nodes  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('failed_nodes') is not None:
            self.failed_nodes = map.get('failed_nodes')
        if map.get('healthy_nodes') is not None:
            self.healthy_nodes = map.get('healthy_nodes')
        if map.get('initial_nodes') is not None:
            self.initial_nodes = map.get('initial_nodes')
        if map.get('offline_nodes') is not None:
            self.offline_nodes = map.get('offline_nodes')
        if map.get('removing_nodes') is not None:
            self.removing_nodes = map.get('removing_nodes')
        if map.get('serving_nodes') is not None:
            self.serving_nodes = map.get('serving_nodes')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('total_nodes') is not None:
            self.total_nodes = map.get('total_nodes')
        return self


class DescribeClusterNodePoolDetailResponseBodyTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable    # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, map={}):
        if map.get('tee_enable') is not None:
            self.tee_enable = map.get('tee_enable')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, surge=None, surge_percentage=None, max_unavailable=None):
        # 是否启用自动升级，自修复。
        self.auto_upgrade = auto_upgrade  # type: bool
        # 额外节点数量。
        self.surge = surge              # type: int
        # 额外节点比例， 和surge 二选一。
        self.surge_percentage = surge_percentage  # type: int
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        return result

    def from_map(self, map={}):
        if map.get('auto_upgrade') is not None:
            self.auto_upgrade = map.get('auto_upgrade')
        if map.get('surge') is not None:
            self.surge = map.get('surge')
        if map.get('surge_percentage') is not None:
            self.surge_percentage = map.get('surge_percentage')
        if map.get('max_unavailable') is not None:
            self.max_unavailable = map.get('max_unavailable')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagement(TeaModel):
    def __init__(self, enable=None, auto_repair=None, upgrade_config=None):
        # 是否开启托管版节点池。
        self.enable = enable            # type: bool
        # 自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('auto_repair') is not None:
            self.auto_repair = map.get('auto_repair')
        if map.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(map['upgrade_config'])
        return self


class DescribeClusterNodePoolDetailResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterNodePoolDetailResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateClusterNodePoolRequest(TeaModel):
    def __init__(self, auto_scaling=None, kubernetes_config=None, nodepool_info=None, scaling_group=None,
                 tee_config=None, management=None, count=None):
        # 自动伸缩节点池配置。
        self.auto_scaling = auto_scaling  # type: CreateClusterNodePoolRequestAutoScaling
        # 集群配置
        self.kubernetes_config = kubernetes_config  # type: CreateClusterNodePoolRequestKubernetesConfig
        # 节点池配置
        self.nodepool_info = nodepool_info  # type: CreateClusterNodePoolRequestNodepoolInfo
        # 伸缩组配置
        self.scaling_group = scaling_group  # type: CreateClusterNodePoolRequestScalingGroup
        # 加密计算节点池配置。
        self.tee_config = tee_config    # type: CreateClusterNodePoolRequestTeeConfig
        # 托管节点池配置。
        self.management = management    # type: CreateClusterNodePoolRequestManagement
        # 节点数量。
        self.count = count              # type: int

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()
        if self.management:
            self.management.validate()

    def to_map(self):
        result = {}
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, map={}):
        if map.get('auto_scaling') is not None:
            temp_model = CreateClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(map['auto_scaling'])
        if map.get('kubernetes_config') is not None:
            temp_model = CreateClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(map['kubernetes_config'])
        if map.get('nodepool_info') is not None:
            temp_model = CreateClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(map['nodepool_info'])
        if map.get('scaling_group') is not None:
            temp_model = CreateClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(map['scaling_group'])
        if map.get('tee_config') is not None:
            temp_model = CreateClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(map['tee_config'])
        if map.get('management') is not None:
            temp_model = CreateClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(map['management'])
        if map.get('count') is not None:
            self.count = map.get('count')
        return self


class CreateClusterNodePoolRequestAutoScaling(TeaModel):
    def __init__(self, enable=None, max_instances=None, min_instances=None, type=None, is_bond_eip=None,
                 eip_internet_charge_type=None, eip_bandwidth=None):
        # 是否开启自动伸缩。
        self.enable = enable            # type: bool
        # 最大实例数。
        self.max_instances = max_instances  # type: int
        # 最小实例数。
        self.min_instances = min_instances  # type: int
        # 扩容节点类型。
        self.type = type                # type: str
        # 是否绑定EIP。
        self.is_bond_eip = is_bond_eip  # type: bool
        # EIP实例规格。
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 带宽峰值。
        self.eip_bandwidth = eip_bandwidth  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('max_instances') is not None:
            self.max_instances = map.get('max_instances')
        if map.get('min_instances') is not None:
            self.min_instances = map.get('min_instances')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('is_bond_eip') is not None:
            self.is_bond_eip = map.get('is_bond_eip')
        if map.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = map.get('eip_internet_charge_type')
        if map.get('eip_bandwidth') is not None:
            self.eip_bandwidth = map.get('eip_bandwidth')
        return self


class CreateClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控。
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略。
        self.cpu_policy = cpu_policy    # type: str
        # 节点标签。
        self.labels = labels            # type: List[Tags]
        # 容器运行时。
        self.runtime = runtime          # type: str
        # 容器运行时版本。
        self.runtime_version = runtime_version  # type: str
        # 污点信息。
        self.taints = taints            # type: List[Taints]
        # 节点自定义数据。
        self.user_data = user_data      # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, map={}):
        if map.get('cms_enabled') is not None:
            self.cms_enabled = map.get('cms_enabled')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                temp_model = Tags()
                self.labels.append(temp_model.from_map(k))
        if map.get('runtime') is not None:
            self.runtime = map.get('runtime')
        if map.get('runtime_version') is not None:
            self.runtime_version = map.get('runtime_version')
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = Taints()
                self.taints.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        return self


class CreateClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(self, name=None, resource_group_id=None):
        # 节点池名称
        self.name = name                # type: str
        # 资源组ID。
        self.resource_group_id = resource_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        return self


class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占实例规格。
        self.instance_type = instance_type  # type: str
        # 抢占实例单价。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, map={}):
        if map.get('instance_type') is not None:
            self.instance_type = map.get('instance_type')
        if map.get('price_limit') is not None:
            self.price_limit = map.get('price_limit')
        return self


class CreateClusterNodePoolRequestScalingGroupTags(TeaModel):
    def __init__(self, key=None, value=None):
        # key
        self.key = key                  # type: str
        # value
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class CreateClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, data_disks=None, image_id=None,
                 instance_charge_type=None, instance_types=None, key_pair=None, login_password=None, period=None, period_unit=None,
                 platform=None, rds_instances=None, spot_strategy=None, spot_price_limit=None, scaling_policy=None,
                 security_group_id=None, system_disk_category=None, system_disk_size=None, tags=None, vswitch_ids=None):
        # 节点是否开启自动续费
        self.auto_renew = auto_renew    # type: bool
        # 节点自动续费周期
        self.auto_renew_period = auto_renew_period  # type: int
        # 数据盘配置。
        self.data_disks = data_disks    # type: List[DataDisks]
        # 自定义镜像。
        self.image_id = image_id        # type: str
        # 节点付费类型
        self.instance_charge_type = instance_charge_type  # type: str
        # 实例规格。
        self.instance_types = instance_types  # type: List[str]
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码。
        self.login_password = login_password  # type: str
        # 节点包年包月时长。
        self.period = period            # type: int
        # 节点包年包月周期。
        self.period_unit = period_unit  # type: str
        # 操作系统发行版
        self.platform = platform        # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 抢占实例价格上限配置。
        self.spot_price_limit = spot_price_limit  # type: List[CreateClusterNodePoolRequestScalingGroupSpotPriceLimit]
        # 自动伸缩。
        self.scaling_policy = scaling_policy  # type: str
        # 安全组ID。
        self.security_group_id = security_group_id  # type: str
        # 节点系统盘类型。
        self.system_disk_category = system_disk_category  # type: str
        # 节点系统盘大小。
        self.system_disk_size = system_disk_size  # type: int
        # ECS标签
        self.tags = tags                # type: List[CreateClusterNodePoolRequestScalingGroupTags]
        # 虚拟交换机ID。
        self.vswitch_ids = vswitch_ids  # type: List[str]

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        return result

    def from_map(self, map={}):
        if map.get('auto_renew') is not None:
            self.auto_renew = map.get('auto_renew')
        if map.get('auto_renew_period') is not None:
            self.auto_renew_period = map.get('auto_renew_period')
        self.data_disks = []
        if map.get('data_disks') is not None:
            for k in map.get('data_disks'):
                temp_model = DataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instance_charge_type') is not None:
            self.instance_charge_type = map.get('instance_charge_type')
        if map.get('instance_types') is not None:
            self.instance_types = map.get('instance_types')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('period') is not None:
            self.period = map.get('period')
        if map.get('period_unit') is not None:
            self.period_unit = map.get('period_unit')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('spot_strategy') is not None:
            self.spot_strategy = map.get('spot_strategy')
        self.spot_price_limit = []
        if map.get('spot_price_limit') is not None:
            for k in map.get('spot_price_limit'):
                temp_model = CreateClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if map.get('scaling_policy') is not None:
            self.scaling_policy = map.get('scaling_policy')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('system_disk_category') is not None:
            self.system_disk_category = map.get('system_disk_category')
        if map.get('system_disk_size') is not None:
            self.system_disk_size = map.get('system_disk_size')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = CreateClusterNodePoolRequestScalingGroupTags()
                self.tags.append(temp_model.from_map(k))
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        return self


class CreateClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池。
        self.tee_enable = tee_enable    # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, map={}):
        if map.get('tee_enable') is not None:
            self.tee_enable = map.get('tee_enable')
        return self


class CreateClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, surge=None, surge_percentage=None, max_unavailable=None):
        # 是否启用自动升级
        self.auto_upgrade = auto_upgrade  # type: bool
        # 额外节点数量。
        self.surge = surge              # type: int
        # 额外节点比例。和surge二选一。
        self.surge_percentage = surge_percentage  # type: int
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        return result

    def from_map(self, map={}):
        if map.get('auto_upgrade') is not None:
            self.auto_upgrade = map.get('auto_upgrade')
        if map.get('surge') is not None:
            self.surge = map.get('surge')
        if map.get('surge_percentage') is not None:
            self.surge_percentage = map.get('surge_percentage')
        if map.get('max_unavailable') is not None:
            self.max_unavailable = map.get('max_unavailable')
        return self


class CreateClusterNodePoolRequestManagement(TeaModel):
    def __init__(self, enable=None, auto_repair=None, upgrade_config=None):
        # 是否启用托管节点池。
        self.enable = enable            # type: bool
        # 是否启用自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 自动升级配置。
        self.upgrade_config = upgrade_config  # type: CreateClusterNodePoolRequestManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('auto_repair') is not None:
            self.auto_repair = map.get('auto_repair')
        if map.get('upgrade_config') is not None:
            temp_model = CreateClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(map['upgrade_config'])
        return self


class CreateClusterNodePoolResponseBody(TeaModel):
    def __init__(self, nodepool_id=None):
        # 节点池ID
        self.nodepool_id = nodepool_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        return result

    def from_map(self, map={}):
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        return self


class CreateClusterNodePoolResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateClusterNodePoolResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateClusterNodePoolResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeClusterUserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # ApiServer是否为内网地址。
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        if map.get('PrivateIpAddress') is not None:
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
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, map={}):
        if map.get('config') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterUserKubeconfigResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ScaleClusterRequest(TeaModel):
    def __init__(self, cloud_monitor_flags=None, count=None, cpu_policy=None, disable_rollback=None, key_pair=None,
                 login_password=None, tags=None, taints=None, vswitch_ids=None, worker_auto_renew=None,
                 worker_auto_renew_period=None, worker_data_disk=None, worker_data_disks=None, worker_instance_charge_type=None,
                 worker_instance_types=None, worker_period=None, worker_period_unit=None, worker_system_disk_category=None,
                 worker_system_disk_size=None):
        # 节点是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 扩容节点数。
        self.count = count              # type: int
        # 节点CPU策略。
        self.cpu_policy = cpu_policy    # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码。和keypair二选一。
        self.login_password = login_password  # type: str
        # 集群标签。
        self.tags = tags                # type: List[ScaleClusterRequestTags]
        # 节点污点标记。
        self.taints = taints            # type: List[ScaleClusterRequestTaints]
        # 节点交换机ID列表。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # 节点是否开启Worker节点自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # 自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # 是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: List[ScaleClusterRequestWorkerDataDisks]
        # 节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点ECS规格类型。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # 节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # 当指定为PrePaid的时候需要指定周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # 节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # 节点系统盘大小
        self.worker_system_disk_size = worker_system_disk_size  # type: int

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        if self.worker_data_disk is not None:
            result['worker_data_disk'] = self.worker_data_disk
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        return result

    def from_map(self, map={}):
        if map.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        if map.get('disable_rollback') is not None:
            self.disable_rollback = map.get('disable_rollback')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ScaleClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = ScaleClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        if map.get('worker_auto_renew') is not None:
            self.worker_auto_renew = map.get('worker_auto_renew')
        if map.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        if map.get('worker_data_disk') is not None:
            self.worker_data_disk = map.get('worker_data_disk')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = ScaleClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if map.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        if map.get('worker_instance_types') is not None:
            self.worker_instance_types = map.get('worker_instance_types')
        if map.get('worker_period') is not None:
            self.worker_period = map.get('worker_period')
        if map.get('worker_period_unit') is not None:
            self.worker_period_unit = map.get('worker_period_unit')
        if map.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = map.get('worker_system_disk_category')
        if map.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = map.get('worker_system_disk_size')
        return self


class ScaleClusterRequestTags(TeaModel):
    def __init__(self, key=None):
        # 标签值。
        self.key = key                  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
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
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
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
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('encrypted') is not None:
            self.encrypted = map.get('encrypted')
        if map.get('size') is not None:
            self.size = map.get('size')
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('request_id') is not None:
            self.request_id = map.get('request_id')
        if map.get('task_id') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScaleClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        if self.can_upgrade is not None:
            result['can_upgrade'] = self.can_upgrade
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, map={}):
        if map.get('addon_info') is not None:
            temp_model = DescribeClusterAddonUpgradeStatusResponseBodyAddonInfo()
            self.addon_info = temp_model.from_map(map['addon_info'])
        if map.get('can_upgrade') is not None:
            self.can_upgrade = map.get('can_upgrade')
        if map.get('template') is not None:
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
        if self.category is not None:
            result['category'] = self.category
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.message is not None:
            result['message'] = self.message
        if self.version is not None:
            result['version'] = self.version
        if self.yaml is not None:
            result['yaml'] = self.yaml
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('component_name') is not None:
            self.component_name = map.get('component_name')
        if map.get('message') is not None:
            self.message = map.get('message')
        if map.get('version') is not None:
            self.version = map.get('version')
        if map.get('yaml') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterAddonUpgradeStatusResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        if self.region is not None:
            result['region'] = self.region
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        return result

    def from_map(self, map={}):
        if map.get('region') is not None:
            self.region = map.get('region')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        return self


class DescribeAddonsResponseBody(TeaModel):
    def __init__(self, component_groups=None, standard_components=None):
        # 组件分组信息，例如：存储类组件，网络组件等。
        self.component_groups = component_groups  # type: List[DescribeAddonsResponseBodyComponentGroups]
        # 标准组件信息，包含各个组件的描述信息。
        self.standard_components = standard_components  # type: Dict[str, StandardComponentsValue]

    def validate(self):
        if self.component_groups:
            for k in self.component_groups:
                if k:
                    k.validate()
        if self.standard_components:
            for v in self.standard_components.values():
                if v:
                    v.validate()

    def to_map(self):
        result = {}
        result['ComponentGroups'] = []
        if self.component_groups is not None:
            for k in self.component_groups:
                result['ComponentGroups'].append(k.to_map() if k else None)
        result['StandardComponents'] = {}
        if self.standard_components is not None:
            for k, v in self.standard_components.items():
                result['StandardComponents'][k] = v.to_map()
        return result

    def from_map(self, map={}):
        self.component_groups = []
        if map.get('ComponentGroups') is not None:
            for k in map.get('ComponentGroups'):
                temp_model = DescribeAddonsResponseBodyComponentGroups()
                self.component_groups.append(temp_model.from_map(k))
        self.standard_components = {}
        if map.get('StandardComponents') is not None:
            for k, v in map.get('StandardComponents').items():
                temp_model = StandardComponentsValue()
                self.standard_components[k] = temp_model.from_map(v)
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
        if self.description is not None:
            result['description'] = self.description
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('disabled') is not None:
            self.disabled = map.get('disabled')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('required') is not None:
            self.required = map.get('required')
        if map.get('version') is not None:
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
        if self.default is not None:
            result['default'] = self.default
        if self.group_name is not None:
            result['group_name'] = self.group_name
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('default') is not None:
            self.default = map.get('default')
        if map.get('group_name') is not None:
            self.group_name = map.get('group_name')
        self.items = []
        if map.get('items') is not None:
            for k in map.get('items'):
                temp_model = DescribeAddonsResponseBodyComponentGroupsItems()
                self.items.append(temp_model.from_map(k))
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeAddonsResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CreateClusterRequest(TeaModel):
    def __init__(self, addons=None, cloud_monitor_flags=None, cluster_type=None, container_cidr=None,
                 cpu_policy=None, deletion_protection=None, disable_rollback=None, endpoint_public_access=None,
                 format_disk=None, image_id=None, instances=None, is_enterprise_security_group=None, keep_instance_name=None,
                 key_pair=None, kubernetes_version=None, login_password=None, master_auto_renew=None,
                 master_auto_renew_period=None, master_count=None, master_instance_charge_type=None, master_instance_types=None,
                 master_period=None, master_period_unit=None, master_system_disk_category=None, master_system_disk_size=None,
                 master_vswitch_ids=None, name=None, node_cidr_mask=None, node_port_range=None, num_of_nodes=None, os_type=None,
                 platform=None, pod_vswitch_ids=None, private_zone=None, profile=None, proxy_mode=None, rds_instances=None,
                 region_id=None, runtime=None, security_group_id=None, service_cidr=None, snat_entry=None, ssh_flags=None,
                 tags=None, taints=None, timeout_mins=None, user_data=None, vpcid=None, vswitch_ids=None,
                 worker_auto_renew=None, worker_auto_renew_period=None, worker_data_disks=None, worker_instance_charge_type=None,
                 worker_instance_types=None, worker_period=None, worker_period_unit=None, worker_system_disk_category=None,
                 worker_system_disk_size=None, worker_vswitch_ids=None, zone_id=None):
        # 组件信息。
        self.addons = addons            # type: List[CreateClusterRequestAddons]
        # 是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 集群类型
        self.cluster_type = cluster_type  # type: str
        # POD网络地址段。
        self.container_cidr = container_cidr  # type: str
        # CPU管理策略。
        self.cpu_policy = cpu_policy    # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群创建失败后是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 集群是否运行公网访问。
        self.endpoint_public_access = endpoint_public_access  # type: bool
        # 是否进行数据盘挂载
        self.format_disk = format_disk  # type: bool
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # 已有实例列表。
        self.instances = instances      # type: List[str]
        # 是否自动创建企业安全组，与security_group_id二选一。
        self.is_enterprise_security_group = is_enterprise_security_group  # type: bool
        # 是否保留实例名称。
        self.keep_instance_name = keep_instance_name  # type: bool
        # key_pair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # 集群版本好。
        self.kubernetes_version = kubernetes_version  # type: str
        # SSH登录密码，与key_pair二选一。
        self.login_password = login_password  # type: str
        # Master节点是否自动续费。
        self.master_auto_renew = master_auto_renew  # type: bool
        # Master节点自动续费周期。
        self.master_auto_renew_period = master_auto_renew_period  # type: int
        # Master节点数量。
        self.master_count = master_count  # type: int
        # Master节点付费类型。
        self.master_instance_charge_type = master_instance_charge_type  # type: str
        # Master节点ECS规格类型。
        self.master_instance_types = master_instance_types  # type: List[str]
        # Master节点包年包月时长，当master_instance_charge_type取值为PrePaid时才生效且为必选值。
        self.master_period = master_period  # type: int
        # Master节点包年包月周期。
        self.master_period_unit = master_period_unit  # type: str
        # Master节点系统盘类型。
        self.master_system_disk_category = master_system_disk_category  # type: str
        # Master节点系统盘大小。
        self.master_system_disk_size = master_system_disk_size  # type: int
        # Master节点交换机ID列表。
        self.master_vswitch_ids = master_vswitch_ids  # type: List[str]
        # 集群名称。
        self.name = name                # type: str
        # 节点IP数量，这里通过CIDR来指定。
        self.node_cidr_mask = node_cidr_mask  # type: str
        # 节点服务端口范围。
        self.node_port_range = node_port_range  # type: str
        # Worker节点数量。
        self.num_of_nodes = num_of_nodes  # type: int
        # 操作系统。
        self.os_type = os_type          # type: str
        # 操作系统发行版。
        self.platform = platform        # type: str
        # Pod的虚拟交换机列表，在ENI多网卡模式下，需要传额外的VSwitch ID给addon。
        self.pod_vswitch_ids = pod_vswitch_ids  # type: List[str]
        # 是否开启PrivateZone用于服务发现。
        self.private_zone = private_zone  # type: bool
        # 边缘集群标识。
        self.profile = profile          # type: str
        # kube-proxy代理模式。
        self.proxy_mode = proxy_mode    # type: str
        # RDS列表，将该ECS加入到选择的RDS实例的白名单中。。
        self.rds_instances = rds_instances  # type: List[str]
        # 集群所属地域ID。
        self.region_id = region_id      # type: str
        # 容器运行时。
        self.runtime = runtime          # type: CreateClusterRequestRuntime
        # 自定义安全组ID。
        self.security_group_id = security_group_id  # type: str
        # Service网络地址段。
        self.service_cidr = service_cidr  # type: str
        # 集群是否配置SNAT。
        self.snat_entry = snat_entry    # type: bool
        # 集群是否开启公网SSH登录。
        self.ssh_flags = ssh_flags      # type: bool
        # 集群标签。
        self.tags = tags                # type: List[CreateClusterRequestTags]
        # 污点信息。
        self.taints = taints            # type: List[CreateClusterRequestTaints]
        # 集群创建超时时间。
        self.timeout_mins = timeout_mins  # type: int
        # 节点用户自定义数据。
        self.user_data = user_data      # type: str
        # 集群使用的VPC。
        self.vpcid = vpcid              # type: str
        # 虚拟交换机列表。List长度范围为[1，3]。当集群类型为托管版或标准serverless集群时，该参数必填。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # Worker节点是否自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # Worker节点自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # Worker节点数据盘配置。
        self.worker_data_disks = worker_data_disks  # type: List[CreateClusterRequestWorkerDataDisks]
        # Worker节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点ECS实例类型。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # Worker节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # Worker节点包年包月周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # Worker节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # Worker节点系统盘大小。
        self.worker_system_disk_size = worker_system_disk_size  # type: int
        # 集群使用的虚拟交换机。
        self.worker_vswitch_ids = worker_vswitch_ids  # type: List[str]
        # 集群所属地域内的可用区ID。
        self.zone_id = zone_id          # type: str

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.container_cidr is not None:
            result['container_cidr'] = self.container_cidr
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.endpoint_public_access is not None:
            result['endpoint_public_access'] = self.endpoint_public_access
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instances is not None:
            result['instances'] = self.instances
        if self.is_enterprise_security_group is not None:
            result['is_enterprise_security_group'] = self.is_enterprise_security_group
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.kubernetes_version is not None:
            result['kubernetes_version'] = self.kubernetes_version
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.master_auto_renew is not None:
            result['master_auto_renew'] = self.master_auto_renew
        if self.master_auto_renew_period is not None:
            result['master_auto_renew_period'] = self.master_auto_renew_period
        if self.master_count is not None:
            result['master_count'] = self.master_count
        if self.master_instance_charge_type is not None:
            result['master_instance_charge_type'] = self.master_instance_charge_type
        if self.master_instance_types is not None:
            result['master_instance_types'] = self.master_instance_types
        if self.master_period is not None:
            result['master_period'] = self.master_period
        if self.master_period_unit is not None:
            result['master_period_unit'] = self.master_period_unit
        if self.master_system_disk_category is not None:
            result['master_system_disk_category'] = self.master_system_disk_category
        if self.master_system_disk_size is not None:
            result['master_system_disk_size'] = self.master_system_disk_size
        if self.master_vswitch_ids is not None:
            result['master_vswitch_ids'] = self.master_vswitch_ids
        if self.name is not None:
            result['name'] = self.name
        if self.node_cidr_mask is not None:
            result['node_cidr_mask'] = self.node_cidr_mask
        if self.node_port_range is not None:
            result['node_port_range'] = self.node_port_range
        if self.num_of_nodes is not None:
            result['num_of_nodes'] = self.num_of_nodes
        if self.os_type is not None:
            result['os_type'] = self.os_type
        if self.platform is not None:
            result['platform'] = self.platform
        if self.pod_vswitch_ids is not None:
            result['pod_vswitch_ids'] = self.pod_vswitch_ids
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr
        if self.snat_entry is not None:
            result['snat_entry'] = self.snat_entry
        if self.ssh_flags is not None:
            result['ssh_flags'] = self.ssh_flags
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.timeout_mins is not None:
            result['timeout_mins'] = self.timeout_mins
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.vpcid is not None:
            result['vpcid'] = self.vpcid
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        if self.worker_vswitch_ids is not None:
            result['worker_vswitch_ids'] = self.worker_vswitch_ids
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, map={}):
        self.addons = []
        if map.get('addons') is not None:
            for k in map.get('addons'):
                temp_model = CreateClusterRequestAddons()
                self.addons.append(temp_model.from_map(k))
        if map.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        if map.get('container_cidr') is not None:
            self.container_cidr = map.get('container_cidr')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        if map.get('deletion_protection') is not None:
            self.deletion_protection = map.get('deletion_protection')
        if map.get('disable_rollback') is not None:
            self.disable_rollback = map.get('disable_rollback')
        if map.get('endpoint_public_access') is not None:
            self.endpoint_public_access = map.get('endpoint_public_access')
        if map.get('format_disk') is not None:
            self.format_disk = map.get('format_disk')
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instances') is not None:
            self.instances = map.get('instances')
        if map.get('is_enterprise_security_group') is not None:
            self.is_enterprise_security_group = map.get('is_enterprise_security_group')
        if map.get('keep_instance_name') is not None:
            self.keep_instance_name = map.get('keep_instance_name')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('kubernetes_version') is not None:
            self.kubernetes_version = map.get('kubernetes_version')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('master_auto_renew') is not None:
            self.master_auto_renew = map.get('master_auto_renew')
        if map.get('master_auto_renew_period') is not None:
            self.master_auto_renew_period = map.get('master_auto_renew_period')
        if map.get('master_count') is not None:
            self.master_count = map.get('master_count')
        if map.get('master_instance_charge_type') is not None:
            self.master_instance_charge_type = map.get('master_instance_charge_type')
        if map.get('master_instance_types') is not None:
            self.master_instance_types = map.get('master_instance_types')
        if map.get('master_period') is not None:
            self.master_period = map.get('master_period')
        if map.get('master_period_unit') is not None:
            self.master_period_unit = map.get('master_period_unit')
        if map.get('master_system_disk_category') is not None:
            self.master_system_disk_category = map.get('master_system_disk_category')
        if map.get('master_system_disk_size') is not None:
            self.master_system_disk_size = map.get('master_system_disk_size')
        if map.get('master_vswitch_ids') is not None:
            self.master_vswitch_ids = map.get('master_vswitch_ids')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('node_cidr_mask') is not None:
            self.node_cidr_mask = map.get('node_cidr_mask')
        if map.get('node_port_range') is not None:
            self.node_port_range = map.get('node_port_range')
        if map.get('num_of_nodes') is not None:
            self.num_of_nodes = map.get('num_of_nodes')
        if map.get('os_type') is not None:
            self.os_type = map.get('os_type')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('pod_vswitch_ids') is not None:
            self.pod_vswitch_ids = map.get('pod_vswitch_ids')
        if map.get('private_zone') is not None:
            self.private_zone = map.get('private_zone')
        if map.get('profile') is not None:
            self.profile = map.get('profile')
        if map.get('proxy_mode') is not None:
            self.proxy_mode = map.get('proxy_mode')
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('runtime') is not None:
            temp_model = CreateClusterRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('service_cidr') is not None:
            self.service_cidr = map.get('service_cidr')
        if map.get('snat_entry') is not None:
            self.snat_entry = map.get('snat_entry')
        if map.get('ssh_flags') is not None:
            self.ssh_flags = map.get('ssh_flags')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = CreateClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = CreateClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if map.get('timeout_mins') is not None:
            self.timeout_mins = map.get('timeout_mins')
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('vpcid') is not None:
            self.vpcid = map.get('vpcid')
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        if map.get('worker_auto_renew') is not None:
            self.worker_auto_renew = map.get('worker_auto_renew')
        if map.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = CreateClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if map.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        if map.get('worker_instance_types') is not None:
            self.worker_instance_types = map.get('worker_instance_types')
        if map.get('worker_period') is not None:
            self.worker_period = map.get('worker_period')
        if map.get('worker_period_unit') is not None:
            self.worker_period_unit = map.get('worker_period_unit')
        if map.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = map.get('worker_system_disk_category')
        if map.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = map.get('worker_system_disk_size')
        if map.get('worker_vswitch_ids') is not None:
            self.worker_vswitch_ids = map.get('worker_vswitch_ids')
        if map.get('zone_id') is not None:
            self.zone_id = map.get('zone_id')
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
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('config') is not None:
            self.config = map.get('config')
        if map.get('name') is not None:
            self.name = map.get('name')
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
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('version') is not None:
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
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
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
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
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
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, map={}):
        if map.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = map.get('auto_snapshot_policy_id')
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('encrypted') is not None:
            self.encrypted = map.get('encrypted')
        if map.get('size') is not None:
            self.size = map.get('size')
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('request_id') is not None:
            self.request_id = map.get('request_id')
        if map.get('task_id') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(self, component_name=None, next_version=None, version=None):
        # 组件名称，集群升级时取值"k8s"。
        self.component_name = component_name  # type: str
        # 目标版本。
        self.next_version = next_version  # type: str
        # 当前版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('component_name') is not None:
            self.component_name = map.get('component_name')
        if map.get('next_version') is not None:
            self.next_version = map.get('next_version')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class AttachInstancesRequest(TeaModel):
    def __init__(self, cpu_policy=None, format_disk=None, image_id=None, instances=None, is_edge_worker=None,
                 keep_instance_name=None, key_pair=None, nodepool_id=None, password=None, rds_instances=None, runtime=None, tags=None,
                 user_data=None):
        # CPU策略。
        self.cpu_policy = cpu_policy    # type: str
        # 是否格式化数据盘。
        self.format_disk = format_disk  # type: bool
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # 待添加的实例列表。
        self.instances = instances      # type: List[str]
        # 是否为边缘节点。
        self.is_edge_worker = is_edge_worker  # type: bool
        # 是否保留实例名称。
        self.keep_instance_name = keep_instance_name  # type: bool
        # key_pair名称，与login_password二选一
        self.key_pair = key_pair        # type: str
        # 节点池ID，欲将节点添加到哪个节点池中。。
        self.nodepool_id = nodepool_id  # type: str
        # password，与key_pair二选一。
        self.password = password        # type: str
        # RDS实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 容器运行时。
        self.runtime = runtime          # type: AttachInstancesRequestRuntime
        # 节点标签。
        self.tags = tags                # type: List[AttachInstancesRequestTags]
        # 用户自定义数据。
        self.user_data = user_data      # type: str

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instances is not None:
            result['instances'] = self.instances
        if self.is_edge_worker is not None:
            result['is_edge_worker'] = self.is_edge_worker
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.password is not None:
            result['password'] = self.password
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, map={}):
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        if map.get('format_disk') is not None:
            self.format_disk = map.get('format_disk')
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instances') is not None:
            self.instances = map.get('instances')
        if map.get('is_edge_worker') is not None:
            self.is_edge_worker = map.get('is_edge_worker')
        if map.get('keep_instance_name') is not None:
            self.keep_instance_name = map.get('keep_instance_name')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        if map.get('password') is not None:
            self.password = map.get('password')
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('runtime') is not None:
            temp_model = AttachInstancesRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = AttachInstancesRequestTags()
                self.tags.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
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
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('version') is not None:
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
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
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
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        self.list = []
        if map.get('list') is not None:
            for k in map.get('list'):
                temp_model = AttachInstancesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if map.get('task_id') is not None:
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
        if self.code is not None:
            result['code'] = self.code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('code') is not None:
            self.code = map.get('code')
        if map.get('instanceId') is not None:
            self.instance_id = map.get('instanceId')
        if map.get('message') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(self, template_type=None):
        # 模板类型，部署模板类型，目前一共有2种类型，取值为：kubernetes或compose。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, map={}):
        if map.get('template_type') is not None:
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
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('page_info') is not None:
            temp_model = DescribeTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(map['page_info'])
        self.templates = []
        if map.get('templates') is not None:
            for k in map.get('templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
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
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        if map.get('page_number') is not None:
            self.page_number = map.get('page_number')
        if map.get('page_size') is not None:
            self.page_size = map.get('page_size')
        if map.get('total_count') is not None:
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
        if self.acl is not None:
            result['acl'] = self.acl
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, map={}):
        if map.get('acl') is not None:
            self.acl = map.get('acl')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('tags') is not None:
            self.tags = map.get('tags')
        if map.get('template') is not None:
            self.template = map.get('template')
        if map.get('template_type') is not None:
            self.template_type = map.get('template_type')
        if map.get('updated') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class PauseClusterUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeTemplateAttributeResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: List[DescribeTemplateAttributeResponseBody]

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeTemplateAttributeResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeTemplateAttributeResponseBody(TeaModel):
    def __init__(self, acl=None, created=None, description=None, id=None, name=None, template=None,
                 template_hash_code_version=None, template_type=None, template_with_hist_id=None, updated=None):
        # 编排模板权限。取值：private，public，shared。	
        self.acl = acl                  # type: str
        # 编排模板创建时间。	
        self.created = created          # type: str
        # 编排模板描述。	
        self.description = description  # type: str
        # 编排模板ID，模板每次修改，这个ID都会改变。	
        self.id = id                    # type: str
        # 编排模板名称。	
        self.name = name                # type: str
        # 编排模板内容。	
        self.template = template        # type: str
        # 编排模板ID，该ID主要用于应用中心。	
        self.template_hash_code_version = template_hash_code_version  # type: str
        # 编排模板类型，取值：kubernetes。	
        self.template_type = template_type  # type: str
        # 编排模板ID，该ID唯一不随更新而改变。	
        self.template_with_hist_id = template_with_hist_id  # type: str
        # 编排模板修改时间。	
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.acl is not None:
            result['acl'] = self.acl
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.template is not None:
            result['template'] = self.template
        if self.template_hash_code_version is not None:
            result['template_hash_code_version'] = self.template_hash_code_version
        if self.template_type is not None:
            result['template_type'] = self.template_type
        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, map={}):
        if map.get('acl') is not None:
            self.acl = map.get('acl')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('template') is not None:
            self.template = map.get('template')
        if map.get('template_hash_code_version') is not None:
            self.template_hash_code_version = map.get('template_hash_code_version')
        if map.get('template_type') is not None:
            self.template_type = map.get('template_type')
        if map.get('template_with_hist_id') is not None:
            self.template_with_hist_id = map.get('template_with_hist_id')
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(self, name=None, template=None, tags=None, template_type=None):
        self.name = name                # type: str
        self.template = template        # type: str
        self.tags = tags                # type: str
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.template is not None:
            result['template'] = self.template
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('template') is not None:
            self.template = map.get('template')
        if map.get('tags') is not None:
            self.tags = map.get('tags')
        if map.get('template_type') is not None:
            self.template_type = map.get('template_type')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(self, template_id=None):
        self.template_id = template_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, map={}):
        if map.get('template_id') is not None:
            self.template_id = map.get('template_id')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: CreateTemplateResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('pageSize') is not None:
            self.page_size = map.get('pageSize')
        if map.get('pageNumber') is not None:
            self.page_number = map.get('pageNumber')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        if map.get('state') is not None:
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
        if self.page is not None:
            result['page'] = self.page.to_map()
        return result

    def from_map(self, map={}):
        self.nodes = []
        if map.get('nodes') is not None:
            for k in map.get('nodes'):
                temp_model = DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if map.get('page') is not None:
            temp_model = DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(map['page'])
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
        if self.creation_time is not None:
            result['creation_time'] = self.creation_time
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.expired_time is not None:
            result['expired_time'] = self.expired_time
        if self.host_name is not None:
            result['host_name'] = self.host_name
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.instance_role is not None:
            result['instance_role'] = self.instance_role
        if self.instance_status is not None:
            result['instance_status'] = self.instance_status
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.instance_type_family is not None:
            result['instance_type_family'] = self.instance_type_family
        if self.ip_address is not None:
            result['ip_address'] = self.ip_address
        if self.is_aliyun_node is not None:
            result['is_aliyun_node'] = self.is_aliyun_node
        if self.node_name is not None:
            result['node_name'] = self.node_name
        if self.node_status is not None:
            result['node_status'] = self.node_status
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.source is not None:
            result['source'] = self.source
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('creation_time') is not None:
            self.creation_time = map.get('creation_time')
        if map.get('error_message') is not None:
            self.error_message = map.get('error_message')
        if map.get('expired_time') is not None:
            self.expired_time = map.get('expired_time')
        if map.get('host_name') is not None:
            self.host_name = map.get('host_name')
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instance_charge_type') is not None:
            self.instance_charge_type = map.get('instance_charge_type')
        if map.get('instance_id') is not None:
            self.instance_id = map.get('instance_id')
        if map.get('instance_name') is not None:
            self.instance_name = map.get('instance_name')
        if map.get('instance_role') is not None:
            self.instance_role = map.get('instance_role')
        if map.get('instance_status') is not None:
            self.instance_status = map.get('instance_status')
        if map.get('instance_type') is not None:
            self.instance_type = map.get('instance_type')
        if map.get('instance_type_family') is not None:
            self.instance_type_family = map.get('instance_type_family')
        if map.get('ip_address') is not None:
            self.ip_address = map.get('ip_address')
        if map.get('is_aliyun_node') is not None:
            self.is_aliyun_node = map.get('is_aliyun_node')
        if map.get('node_name') is not None:
            self.node_name = map.get('node_name')
        if map.get('node_status') is not None:
            self.node_status = map.get('node_status')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        if map.get('source') is not None:
            self.source = map.get('source')
        if map.get('state') is not None:
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
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        if map.get('page_number') is not None:
            self.page_number = map.get('page_number')
        if map.get('page_size') is not None:
            self.page_size = map.get('page_size')
        if map.get('total_count') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterNodesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(self, retain_all_resources=None, keep_slb=None, retain_resources=None):
        # 是否保留所有资源,如果设置了该值，将会忽略retain_resources。  true：保留 false：不保留 默认值：fase。
        self.retain_all_resources = retain_all_resources  # type: bool
        # 是否保留SLB。  true：保留 false：不保留 默认值：false。
        self.keep_slb = keep_slb        # type: bool
        # 要保留的资源列表。
        self.retain_resources = retain_resources  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources
        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb
        if self.retain_resources is not None:
            result['retain_resources'] = self.retain_resources
        return result

    def from_map(self, map={}):
        if map.get('retain_all_resources') is not None:
            self.retain_all_resources = map.get('retain_all_resources')
        if map.get('keep_slb') is not None:
            self.keep_slb = map.get('keep_slb')
        if map.get('retain_resources') is not None:
            self.retain_resources = map.get('retain_resources')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class CancelComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeClusterAddonsVersionResponseBody(TeaModel):
    def __init__(self, addons_version=None):
        # 组件信息详情。
        self.addons_version = addons_version  # type: Dict[str, AddonsVersionValue]

    def validate(self):
        if self.addons_version:
            for v in self.addons_version.values():
                if v:
                    v.validate()

    def to_map(self):
        result = {}
        result['AddonsVersion'] = {}
        if self.addons_version is not None:
            for k, v in self.addons_version.items():
                result['AddonsVersion'][k] = v.to_map()
        return result

    def from_map(self, map={}):
        self.addons_version = {}
        if map.get('AddonsVersion') is not None:
            for k, v in map.get('AddonsVersion').items():
                temp_model = AddonsVersionValue()
                self.addons_version[k] = temp_model.from_map(v)
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterAddonsVersionResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeExternalAgentRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # 是否获取内网访问凭据。  true：获取内网连接凭据 false：获取公网连接凭据 默认值：false。
        self.private_ip_address = private_ip_address  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        if map.get('PrivateIpAddress') is not None:
            self.private_ip_address = map.get('PrivateIpAddress')
        return self


class DescribeExternalAgentResponseBody(TeaModel):
    def __init__(self, config=None):
        # 代理配置。
        self.config = config            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, map={}):
        if map.get('config') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeExternalAgentResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        return result

    def from_map(self, map={}):
        self.addons = []
        if map.get('addons') is not None:
            for k in map.get('addons'):
                temp_model = UnInstallClusterAddonsRequestAddons()
                self.addons.append(temp_model.from_map(k))
        return self


class UnInstallClusterAddonsRequestAddons(TeaModel):
    def __init__(self, name=None):
        # 组件名称。
        self.name = name                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        return self


class UnInstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class ResumeComponentUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeClustersV1Request(TeaModel):
    def __init__(self, name=None, cluster_type=None, page_size=None, page_number=None):
        # 通过集群名称进行模糊查询。
        self.name = name                # type: str
        # 集群类型。  Kubernetes: 专有版集群。 ManagedKubernetes：托管版集群。 Ask：Serverless集群。 ExternalKubernetes：注册集群。 ServiceMesh：ASM集群。
        self.cluster_type = cluster_type  # type: str
        # 单页大小。
        self.page_size = page_size      # type: int
        # 分页数。
        self.page_number = page_number  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.page_number is not None:
            result['page_number'] = self.page_number
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        if map.get('page_size') is not None:
            self.page_size = map.get('page_size')
        if map.get('page_number') is not None:
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
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, map={}):
        self.clusters = []
        if map.get('clusters') is not None:
            for k in map.get('clusters'):
                temp_model = DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if map.get('page_info') is not None:
            temp_model = DescribeClustersV1ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(map['page_info'])
        return self


class DescribeClustersV1ResponseBodyClusters(TeaModel):
    def __init__(self, cluster_id=None, cluster_type=None, created=None, init_version=None, current_version=None,
                 next_version=None, deletion_protection=None, docker_version=None, external_loadbalancer_id=None,
                 master_url=None, meta_data=None, name=None, network_mode=None, private_zone=None, profile=None, region_id=None,
                 resource_group_id=None, security_group_id=None, size=None, state=None, subnet_cidr=None, tags=None, updated=None,
                 vpc_id=None, vswitch_id=None, worker_ram_role_name=None, zone_id=None, cluster_spec=None,
                 maintenance_window=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 集群类型。
        self.cluster_type = cluster_type  # type: str
        # 集群初始化时间。
        self.created = created          # type: str
        # 集群初始化版本。
        self.init_version = init_version  # type: str
        # 集群当前版本。
        self.current_version = current_version  # type: str
        # 集群可升级版本。
        self.next_version = next_version  # type: str
        # 集群是否开启删除保护。
        self.deletion_protection = deletion_protection  # type: bool
        # 集群使用的Docker版本。
        self.docker_version = docker_version  # type: str
        # 集群负载均衡服务的ID。
        self.external_loadbalancer_id = external_loadbalancer_id  # type: str
        # 集群访问地址列表。
        self.master_url = master_url    # type: str
        # 集群元数据信息。
        self.meta_data = meta_data      # type: str
        # 集群名称。
        self.name = name                # type: str
        # 集群使用的网络类型，例如：VPC网络。
        self.network_mode = network_mode  # type: str
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
        self.tags = tags                # type: List[Tags]
        # 集群更新时间。
        self.updated = updated          # type: str
        # 集群所在的VPC ID。
        self.vpc_id = vpc_id            # type: str
        # 集群使用的虚拟交换ID。
        self.vswitch_id = vswitch_id    # type: str
        # 集群Worker RAM角色。
        self.worker_ram_role_name = worker_ram_role_name  # type: str
        # 可用区ID。
        self.zone_id = zone_id          # type: str
        # 托管版集群类型，面向托管集群。 • ack.pro.small：专业托管集群。 • ack.standard ：标准托管集群。
        self.cluster_spec = cluster_spec  # type: str
        self.maintenance_window = maintenance_window  # type: MaintenanceWindow

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.maintenance_window:
            self.maintenance_window.validate()

    def to_map(self):
        result = {}
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.private_zone is not None:
            result['private_zone'] = self.private_zone
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.size is not None:
            result['size'] = self.size
        if self.state is not None:
            result['state'] = self.state
        if self.subnet_cidr is not None:
            result['subnet_cidr'] = self.subnet_cidr
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.updated is not None:
            result['updated'] = self.updated
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        if self.vswitch_id is not None:
            result['vswitch_id'] = self.vswitch_id
        if self.worker_ram_role_name is not None:
            result['worker_ram_role_name'] = self.worker_ram_role_name
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('cluster_type') is not None:
            self.cluster_type = map.get('cluster_type')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('init_version') is not None:
            self.init_version = map.get('init_version')
        if map.get('current_version') is not None:
            self.current_version = map.get('current_version')
        if map.get('next_version') is not None:
            self.next_version = map.get('next_version')
        if map.get('deletion_protection') is not None:
            self.deletion_protection = map.get('deletion_protection')
        if map.get('docker_version') is not None:
            self.docker_version = map.get('docker_version')
        if map.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = map.get('external_loadbalancer_id')
        if map.get('master_url') is not None:
            self.master_url = map.get('master_url')
        if map.get('meta_data') is not None:
            self.meta_data = map.get('meta_data')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('network_mode') is not None:
            self.network_mode = map.get('network_mode')
        if map.get('private_zone') is not None:
            self.private_zone = map.get('private_zone')
        if map.get('profile') is not None:
            self.profile = map.get('profile')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('size') is not None:
            self.size = map.get('size')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('subnet_cidr') is not None:
            self.subnet_cidr = map.get('subnet_cidr')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = Tags()
                self.tags.append(temp_model.from_map(k))
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        if map.get('vpc_id') is not None:
            self.vpc_id = map.get('vpc_id')
        if map.get('vswitch_id') is not None:
            self.vswitch_id = map.get('vswitch_id')
        if map.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = map.get('worker_ram_role_name')
        if map.get('zone_id') is not None:
            self.zone_id = map.get('zone_id')
        if map.get('cluster_spec') is not None:
            self.cluster_spec = map.get('cluster_spec')
        if map.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(map['maintenance_window'])
        return self


class DescribeClustersV1ResponseBodyPageInfo(TeaModel):
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
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, map={}):
        if map.get('page_number') is not None:
            self.page_number = map.get('page_number')
        if map.get('page_size') is not None:
            self.page_size = map.get('page_size')
        if map.get('total_count') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClustersV1ResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ModifyClusterConfigurationRequest(TeaModel):
    def __init__(self, configs=None, name=None):
        # 配置集合。
        self.configs = configs          # type: ModifyClusterConfigurationRequestConfigs
        # 配置名称。
        self.name = name                # type: str

    def validate(self):
        if self.configs:
            self.configs.validate()

    def to_map(self):
        result = {}
        if self.configs is not None:
            result['configs'] = self.configs.to_map()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('configs') is not None:
            temp_model = ModifyClusterConfigurationRequestConfigs()
            self.configs = temp_model.from_map(map['configs'])
        if map.get('name') is not None:
            self.name = map.get('name')
        return self


class ModifyClusterConfigurationRequestConfigs(TeaModel):
    def __init__(self, key=None, value=None):
        # key。
        self.key = key                  # type: str
        # value。
        self.value = value              # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class ModifyClusterConfigurationResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeTaskInfoResponseBody(TeaModel):
    def __init__(self, cluster_id=None, task_id=None, created=None, updated=None, state=None, task_type=None,
                 task_result=None):
        # 集群ID。
        self.cluster_id = cluster_id    # type: str
        # 任务ID。
        self.task_id = task_id          # type: str
        # 任务创建时间。
        self.created = created          # type: str
        # 任务更新时间。
        self.updated = updated          # type: str
        # 任务当前状态。
        self.state = state              # type: str
        # 当前任务类型。
        self.task_type = task_type      # type: str
        # 任务执行详情。
        self.task_result = task_result  # type: List[DescribeTaskInfoResponseBodyTaskResult]

    def validate(self):
        if self.task_result:
            for k in self.task_result:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        if self.state is not None:
            result['state'] = self.state
        if self.task_type is not None:
            result['task_type'] = self.task_type
        result['task_result'] = []
        if self.task_result is not None:
            for k in self.task_result:
                result['task_result'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('task_id') is not None:
            self.task_id = map.get('task_id')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('task_type') is not None:
            self.task_type = map.get('task_type')
        self.task_result = []
        if map.get('task_result') is not None:
            for k in map.get('task_result'):
                temp_model = DescribeTaskInfoResponseBodyTaskResult()
                self.task_result.append(temp_model.from_map(k))
        return self


class DescribeTaskInfoResponseBodyTaskResult(TeaModel):
    def __init__(self, data=None, status=None):
        # 操作的资源，例如：实例ID。
        self.data = data                # type: str
        # 资源的状态。
        self.status = status            # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, map={}):
        if map.get('data') is not None:
            self.data = map.get('data')
        if map.get('status') is not None:
            self.status = map.get('status')
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeTaskInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeTaskInfoResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class CancelClusterUpgradeResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(self, description=None, name=None, tags=None, template=None, template_type=None):
        # 部署模板描述信息。
        self.description = description  # type: str
        # 部署模板名称。
        self.name = name                # type: str
        # 部署模板标签
        self.tags = tags                # type: str
        # 部署模板yaml。
        self.template = template        # type: str
        # 部署模板类型。
        self.template_type = template_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, map={}):
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('tags') is not None:
            self.tags = map.get('tags')
        if map.get('template') is not None:
            self.template = map.get('template')
        if map.get('template_type') is not None:
            self.template_type = map.get('template_type')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
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
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = UpgradeClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
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
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('component_name') is not None:
            self.component_name = map.get('component_name')
        if map.get('next_version') is not None:
            self.next_version = map.get('next_version')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class UpgradeClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DeleteKubernetesTriggerResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
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
        if self.amk_cluster_quota is not None:
            result['amk_cluster_quota'] = self.amk_cluster_quota
        if self.ask_cluster_quota is not None:
            result['ask_cluster_quota'] = self.ask_cluster_quota
        if self.cluster_nodepool_quota is not None:
            result['cluster_nodepool_quota'] = self.cluster_nodepool_quota
        if self.cluster_quota is not None:
            result['cluster_quota'] = self.cluster_quota
        if self.node_quota is not None:
            result['node_quota'] = self.node_quota
        return result

    def from_map(self, map={}):
        if map.get('amk_cluster_quota') is not None:
            self.amk_cluster_quota = map.get('amk_cluster_quota')
        if map.get('ask_cluster_quota') is not None:
            self.ask_cluster_quota = map.get('ask_cluster_quota')
        if map.get('cluster_nodepool_quota') is not None:
            self.cluster_nodepool_quota = map.get('cluster_nodepool_quota')
        if map.get('cluster_quota') is not None:
            self.cluster_quota = map.get('cluster_quota')
        if map.get('node_quota') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeUserQuotaResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DeleteClusterNodepoolResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeClusterAddonsUpgradeStatusRequest(TeaModel):
    def __init__(self, component_ids=None):
        # 组件列表。
        self.component_ids = component_ids  # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.component_ids is not None:
            result['componentIds'] = self.component_ids
        return result

    def from_map(self, map={}):
        if map.get('componentIds') is not None:
            self.component_ids = map.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
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
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = InstallClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
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
        if self.config is not None:
            result['config'] = self.config
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('config') is not None:
            self.config = map.get('config')
        if map.get('disabled') is not None:
            self.disabled = map.get('disabled')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('required') is not None:
            self.required = map.get('required')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class InstallClusterAddonsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        return self


class DescribeClusterNodePoolsResponseBody(TeaModel):
    def __init__(self, nodepools=None):
        # 节点池列表。	
        self.nodepools = nodepools      # type: List[DescribeClusterNodePoolsResponseBodyNodepools]

    def validate(self):
        if self.nodepools:
            for k in self.nodepools:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        result['nodepools'] = []
        if self.nodepools is not None:
            for k in self.nodepools:
                result['nodepools'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        self.nodepools = []
        if map.get('nodepools') is not None:
            for k in map.get('nodepools'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepools()
                self.nodepools.append(temp_model.from_map(k))
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling(TeaModel):
    def __init__(self, eip_bandwidth=None, is_bond_eip=None, eip_internet_charge_type=None, enable=None,
                 max_instances=None, min_instances=None, type=None):
        # EIP带宽峰值
        self.eip_bandwidth = eip_bandwidth  # type: int
        # 是否绑定EIP
        self.is_bond_eip = is_bond_eip  # type: bool
        # EIP实例计费方式
        self.eip_internet_charge_type = eip_internet_charge_type  # type: str
        # 自动伸缩。	
        self.enable = enable            # type: bool
        # 最大节点数	
        self.max_instances = max_instances  # type: int
        # 最小节点数	
        self.min_instances = min_instances  # type: int
        # 扩容组类型。
        self.type = type                # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.eip_bandwidth is not None:
            result['eip_bandwidth'] = self.eip_bandwidth
        if self.is_bond_eip is not None:
            result['is_bond_eip'] = self.is_bond_eip
        if self.eip_internet_charge_type is not None:
            result['eip_internet_charge_type'] = self.eip_internet_charge_type
        if self.enable is not None:
            result['enable'] = self.enable
        if self.max_instances is not None:
            result['max_instances'] = self.max_instances
        if self.min_instances is not None:
            result['min_instances'] = self.min_instances
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, map={}):
        if map.get('eip_bandwidth') is not None:
            self.eip_bandwidth = map.get('eip_bandwidth')
        if map.get('is_bond_eip') is not None:
            self.is_bond_eip = map.get('is_bond_eip')
        if map.get('eip_internet_charge_type') is not None:
            self.eip_internet_charge_type = map.get('eip_internet_charge_type')
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('max_instances') is not None:
            self.max_instances = map.get('max_instances')
        if map.get('min_instances') is not None:
            self.min_instances = map.get('min_instances')
        if map.get('type') is not None:
            self.type = map.get('type')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig(TeaModel):
    def __init__(self, cms_enabled=None, cpu_policy=None, labels=None, runtime=None, runtime_version=None,
                 taints=None, user_data=None):
        # 是否开启云监控	
        self.cms_enabled = cms_enabled  # type: bool
        # CPU管理策略	
        self.cpu_policy = cpu_policy    # type: str
        # ECS标签。	
        self.labels = labels            # type: List[Tags]
        # 容器运行时	
        self.runtime = runtime          # type: str
        # 容器运行时版本	
        self.runtime_version = runtime_version  # type: str
        # 污点配置
        self.taints = taints            # type: List[Taints]
        # 节点自定义数据
        self.user_data = user_data      # type: str

    def validate(self):
        if self.labels:
            for k in self.labels:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.runtime is not None:
            result['runtime'] = self.runtime
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        return result

    def from_map(self, map={}):
        if map.get('cms_enabled') is not None:
            self.cms_enabled = map.get('cms_enabled')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        self.labels = []
        if map.get('labels') is not None:
            for k in map.get('labels'):
                temp_model = Tags()
                self.labels.append(temp_model.from_map(k))
        if map.get('runtime') is not None:
            self.runtime = map.get('runtime')
        if map.get('runtime_version') is not None:
            self.runtime_version = map.get('runtime_version')
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = Taints()
                self.taints.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo(TeaModel):
    def __init__(self, created=None, is_default=None, name=None, nodepool_id=None, region_id=None,
                 resource_group_id=None, type=None, updated=None):
        # 节点池创建时间
        self.created = created          # type: str
        # 是否为默认节点池
        self.is_default = is_default    # type: bool
        # 节点池名称
        self.name = name                # type: str
        # 节点池ID
        self.nodepool_id = nodepool_id  # type: str
        # 节点池所在地域ID。
        self.region_id = region_id      # type: str
        # 资源组ID
        self.resource_group_id = resource_group_id  # type: str
        # 节点池类型
        self.type = type                # type: str
        # 节点池更新时间
        self.updated = updated          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('is_default') is not None:
            self.is_default = map.get('is_default')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('nodepool_id') is not None:
            self.nodepool_id = map.get('nodepool_id')
        if map.get('region_id') is not None:
            self.region_id = map.get('region_id')
        if map.get('resource_group_id') is not None:
            self.resource_group_id = map.get('resource_group_id')
        if map.get('type') is not None:
            self.type = map.get('type')
        if map.get('updated') is not None:
            self.updated = map.get('updated')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit(TeaModel):
    def __init__(self, instance_type=None, price_limit=None):
        # 抢占式实例规格。
        self.instance_type = instance_type  # type: str
        # 单台实例上限价格，单位：元/小时。
        self.price_limit = price_limit  # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.price_limit is not None:
            result['price_limit'] = self.price_limit
        return result

    def from_map(self, map={}):
        if map.get('instance_type') is not None:
            self.instance_type = map.get('instance_type')
        if map.get('price_limit') is not None:
            self.price_limit = map.get('price_limit')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup(TeaModel):
    def __init__(self, auto_renew=None, auto_renew_period=None, data_disks=None, image_id=None,
                 instance_charge_type=None, instance_types=None, multi_az_policy=None, period=None, period_unit=None, platform=None,
                 ram_policy=None, spot_strategy=None, spot_price_limit=None, rds_instances=None, scaling_group_id=None,
                 scaling_policy=None, security_group_id=None, system_disk_category=None, system_disk_size=None, tags=None,
                 vswitch_ids=None, login_password=None, key_pair=None):
        # 自动续费	
        self.auto_renew = auto_renew    # type: bool
        # 自动付费时长	
        self.auto_renew_period = auto_renew_period  # type: int
        # 数据盘配置	
        self.data_disks = data_disks    # type: List[DataDisks]
        # 镜像ID	
        self.image_id = image_id        # type: str
        # 节点付费类型	
        self.instance_charge_type = instance_charge_type  # type: str
        # 节点类型	
        self.instance_types = instance_types  # type: List[str]
        # 多可用去策略	
        self.multi_az_policy = multi_az_policy  # type: str
        # 包年包月时长	
        self.period = period            # type: int
        # 自动付费周期	
        self.period_unit = period_unit  # type: str
        # 操作系统发行版。取值： CentOS，AliyunLinux，Windows，WindowsCore。
        self.platform = platform        # type: str
        # RAM 角色名称	
        self.ram_policy = ram_policy    # type: str
        # 抢占式实例类型
        self.spot_strategy = spot_strategy  # type: str
        # 抢占实例价格上限配置。
        self.spot_price_limit = spot_price_limit  # type: List[DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit]
        # RDS列表	
        self.rds_instances = rds_instances  # type: List[str]
        # 扩容组ID	
        self.scaling_group_id = scaling_group_id  # type: str
        # 扩容节点策略	
        self.scaling_policy = scaling_policy  # type: str
        # 安全组ID。	
        self.security_group_id = security_group_id  # type: str
        # 系统盘类型。	
        self.system_disk_category = system_disk_category  # type: str
        # 系统盘大小	
        self.system_disk_size = system_disk_size  # type: int
        # 节点标签	
        self.tags = tags                # type: List[Tags]
        # 虚拟交换机ID。	
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # 登录密码，返回结果是加密的。
        self.login_password = login_password  # type: str
        # 密钥对名称，和login_password二选一。
        self.key_pair = key_pair        # type: str

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.spot_price_limit:
            for k in self.spot_price_limit:
                if k:
                    k.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
        if self.instance_types is not None:
            result['instance_types'] = self.instance_types
        if self.multi_az_policy is not None:
            result['multi_az_policy'] = self.multi_az_policy
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        return result

    def from_map(self, map={}):
        if map.get('auto_renew') is not None:
            self.auto_renew = map.get('auto_renew')
        if map.get('auto_renew_period') is not None:
            self.auto_renew_period = map.get('auto_renew_period')
        self.data_disks = []
        if map.get('data_disks') is not None:
            for k in map.get('data_disks'):
                temp_model = DataDisks()
                self.data_disks.append(temp_model.from_map(k))
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('instance_charge_type') is not None:
            self.instance_charge_type = map.get('instance_charge_type')
        if map.get('instance_types') is not None:
            self.instance_types = map.get('instance_types')
        if map.get('multi_az_policy') is not None:
            self.multi_az_policy = map.get('multi_az_policy')
        if map.get('period') is not None:
            self.period = map.get('period')
        if map.get('period_unit') is not None:
            self.period_unit = map.get('period_unit')
        if map.get('platform') is not None:
            self.platform = map.get('platform')
        if map.get('ram_policy') is not None:
            self.ram_policy = map.get('ram_policy')
        if map.get('spot_strategy') is not None:
            self.spot_strategy = map.get('spot_strategy')
        self.spot_price_limit = []
        if map.get('spot_price_limit') is not None:
            for k in map.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('scaling_group_id') is not None:
            self.scaling_group_id = map.get('scaling_group_id')
        if map.get('scaling_policy') is not None:
            self.scaling_policy = map.get('scaling_policy')
        if map.get('security_group_id') is not None:
            self.security_group_id = map.get('security_group_id')
        if map.get('system_disk_category') is not None:
            self.system_disk_category = map.get('system_disk_category')
        if map.get('system_disk_size') is not None:
            self.system_disk_size = map.get('system_disk_size')
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = Tags()
                self.tags.append(temp_model.from_map(k))
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsStatus(TeaModel):
    def __init__(self, failed_nodes=None, healthy_nodes=None, initial_nodes=None, offline_nodes=None,
                 removing_nodes=None, serving_nodes=None, state=None, total_nodes=None):
        # 失败的节点数	
        self.failed_nodes = failed_nodes  # type: int
        # 处于健康状态的节点数	
        self.healthy_nodes = healthy_nodes  # type: int
        # 正在创建的节点数	
        self.initial_nodes = initial_nodes  # type: int
        # 离线节点数	
        self.offline_nodes = offline_nodes  # type: int
        # 真在被移除的节点数。	
        self.removing_nodes = removing_nodes  # type: int
        # 正在工作节点数	
        self.serving_nodes = serving_nodes  # type: int
        # 节点池状态	
        self.state = state              # type: str
        # 节点总数	
        self.total_nodes = total_nodes  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
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

    def from_map(self, map={}):
        if map.get('failed_nodes') is not None:
            self.failed_nodes = map.get('failed_nodes')
        if map.get('healthy_nodes') is not None:
            self.healthy_nodes = map.get('healthy_nodes')
        if map.get('initial_nodes') is not None:
            self.initial_nodes = map.get('initial_nodes')
        if map.get('offline_nodes') is not None:
            self.offline_nodes = map.get('offline_nodes')
        if map.get('removing_nodes') is not None:
            self.removing_nodes = map.get('removing_nodes')
        if map.get('serving_nodes') is not None:
            self.serving_nodes = map.get('serving_nodes')
        if map.get('state') is not None:
            self.state = map.get('state')
        if map.get('total_nodes') is not None:
            self.total_nodes = map.get('total_nodes')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig(TeaModel):
    def __init__(self, tee_enable=None):
        # 是否为加密计算节点池	
        self.tee_enable = tee_enable    # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, map={}):
        if map.get('tee_enable') is not None:
            self.tee_enable = map.get('tee_enable')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig(TeaModel):
    def __init__(self, auto_upgrade=None, surge=None, surge_percentage=None, max_unavailable=None):
        # 是否启用自动升级，自修复。
        self.auto_upgrade = auto_upgrade  # type: bool
        # 额外节点数量。
        self.surge = surge              # type: int
        # 额外节点比例， 和surge 二选一。
        self.surge_percentage = surge_percentage  # type: int
        # 最大不可用节点数量。
        self.max_unavailable = max_unavailable  # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.auto_upgrade is not None:
            result['auto_upgrade'] = self.auto_upgrade
        if self.surge is not None:
            result['surge'] = self.surge
        if self.surge_percentage is not None:
            result['surge_percentage'] = self.surge_percentage
        if self.max_unavailable is not None:
            result['max_unavailable'] = self.max_unavailable
        return result

    def from_map(self, map={}):
        if map.get('auto_upgrade') is not None:
            self.auto_upgrade = map.get('auto_upgrade')
        if map.get('surge') is not None:
            self.surge = map.get('surge')
        if map.get('surge_percentage') is not None:
            self.surge_percentage = map.get('surge_percentage')
        if map.get('max_unavailable') is not None:
            self.max_unavailable = map.get('max_unavailable')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagement(TeaModel):
    def __init__(self, enable=None, auto_repair=None, upgrade_config=None):
        # 是否开启托管版节点池。
        self.enable = enable            # type: bool
        # 是否启用自动修复。
        self.auto_repair = auto_repair  # type: bool
        # 是否启用自动修复。
        self.upgrade_config = upgrade_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        result = {}
        if self.enable is not None:
            result['enable'] = self.enable
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, map={}):
        if map.get('enable') is not None:
            self.enable = map.get('enable')
        if map.get('auto_repair') is not None:
            self.auto_repair = map.get('auto_repair')
        if map.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(map['upgrade_config'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepools(TeaModel):
    def __init__(self, auto_scaling=None, kubernetes_config=None, nodepool_info=None, scaling_group=None,
                 status=None, tee_config=None, management=None):
        # 自动伸缩配置详情。
        self.auto_scaling = auto_scaling  # type: DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling
        # 集群配置信息。
        self.kubernetes_config = kubernetes_config  # type: DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig
        # 节点池配置详情。
        self.nodepool_info = nodepool_info  # type: DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo
        # 扩容组配置详情。
        self.scaling_group = scaling_group  # type: DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup
        # 节点池状态详情。
        self.status = status            # type: DescribeClusterNodePoolsResponseBodyNodepoolsStatus
        # 加密计算配置详情。
        self.tee_config = tee_config    # type: DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig
        # 托管节点池配置。
        self.management = management    # type: DescribeClusterNodePoolsResponseBodyNodepoolsManagement

    def validate(self):
        if self.auto_scaling:
            self.auto_scaling.validate()
        if self.kubernetes_config:
            self.kubernetes_config.validate()
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()
        if self.management:
            self.management.validate()

    def to_map(self):
        result = {}
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
        if self.kubernetes_config is not None:
            result['kubernetes_config'] = self.kubernetes_config.to_map()
        if self.nodepool_info is not None:
            result['nodepool_info'] = self.nodepool_info.to_map()
        if self.scaling_group is not None:
            result['scaling_group'] = self.scaling_group.to_map()
        if self.status is not None:
            result['status'] = self.status.to_map()
        if self.tee_config is not None:
            result['tee_config'] = self.tee_config.to_map()
        if self.management is not None:
            result['management'] = self.management.to_map()
        return result

    def from_map(self, map={}):
        if map.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling()
            self.auto_scaling = temp_model.from_map(map['auto_scaling'])
        if map.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(map['kubernetes_config'])
        if map.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo()
            self.nodepool_info = temp_model.from_map(map['nodepool_info'])
        if map.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup()
            self.scaling_group = temp_model.from_map(map['scaling_group'])
        if map.get('status') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsStatus()
            self.status = temp_model.from_map(map['status'])
        if map.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig()
            self.tee_config = temp_model.from_map(map['tee_config'])
        if map.get('management') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagement()
            self.management = temp_model.from_map(map['management'])
        return self


class DescribeClusterNodePoolsResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DescribeClusterNodePoolsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterNodePoolsResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class DescribeClusterV2UserKubeconfigRequest(TeaModel):
    def __init__(self, private_ip_address=None):
        # 是否为内网访问。
        self.private_ip_address = private_ip_address  # type: bool

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, map={}):
        if map.get('PrivateIpAddress') is not None:
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
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, map={}):
        if map.get('config') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DescribeClusterV2UserKubeconfigResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class ScaleOutClusterRequest(TeaModel):
    def __init__(self, cloud_monitor_flags=None, count=None, cpu_policy=None, disable_rollback=None, image_id=None,
                 key_pair=None, login_password=None, rds_instances=None, runtime=None, tags=None, taints=None, user_data=None,
                 vswitch_ids=None, worker_auto_renew=None, worker_auto_renew_period=None, worker_data_disk=None,
                 worker_data_disks=None, worker_instance_charge_type=None, worker_instance_types=None, worker_period=None,
                 worker_period_unit=None, worker_system_disk_category=None, worker_system_disk_size=None):
        # 是否安装云监控插件。
        self.cloud_monitor_flags = cloud_monitor_flags  # type: bool
        # 扩容实例数量。
        self.count = count              # type: int
        # CPU策略，取值static或者none。
        self.cpu_policy = cpu_policy    # type: str
        # 失败是否回滚。
        self.disable_rollback = disable_rollback  # type: bool
        # 自定义镜像ID。
        self.image_id = image_id        # type: str
        # keypair名称，和login_password二选一。
        self.key_pair = key_pair        # type: str
        # SSH登录密码，和key_pair二选一。
        self.login_password = login_password  # type: str
        # RDS白名单实例列表。
        self.rds_instances = rds_instances  # type: List[str]
        # 容器引擎。
        self.runtime = runtime          # type: ScaleOutClusterRequestRuntime
        # 节点标签。
        self.tags = tags                # type: List[ScaleOutClusterRequestTags]
        # 节点污点信息。
        self.taints = taints            # type: List[ScaleOutClusterRequestTaints]
        # 用户自定义数据。
        self.user_data = user_data      # type: str
        # 节点交换机ID列表，交换机个数取值范围为1~3。
        self.vswitch_ids = vswitch_ids  # type: List[str]
        # Worker节点是否开启自动续费。
        self.worker_auto_renew = worker_auto_renew  # type: bool
        # Worker节点自动续费周期。
        self.worker_auto_renew_period = worker_auto_renew_period  # type: int
        # Worker节点是否挂载数据盘。
        self.worker_data_disk = worker_data_disk  # type: bool
        # Worker数据盘类型、大小等配置的组合。
        self.worker_data_disks = worker_data_disks  # type: List[ScaleOutClusterRequestWorkerDataDisks]
        # Worker节点付费类型。
        self.worker_instance_charge_type = worker_instance_charge_type  # type: str
        # Worker节点ECS规格类型代码。
        self.worker_instance_types = worker_instance_types  # type: List[str]
        # Worker节点包年包月时长。
        self.worker_period = worker_period  # type: int
        # Worker节点预付费周期。
        self.worker_period_unit = worker_period_unit  # type: str
        # Worker节点系统盘类型。
        self.worker_system_disk_category = worker_system_disk_category  # type: str
        # Worker节点系统盘大小。
        self.worker_system_disk_size = worker_system_disk_size  # type: int

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.taints:
            for k in self.taints:
                if k:
                    k.validate()
        if self.worker_data_disks:
            for k in self.worker_data_disks:
                if k:
                    k.validate()

    def to_map(self):
        result = {}
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.key_pair is not None:
            result['key_pair'] = self.key_pair
        if self.login_password is not None:
            result['login_password'] = self.login_password
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        result['taints'] = []
        if self.taints is not None:
            for k in self.taints:
                result['taints'].append(k.to_map() if k else None)
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.vswitch_ids is not None:
            result['vswitch_ids'] = self.vswitch_ids
        if self.worker_auto_renew is not None:
            result['worker_auto_renew'] = self.worker_auto_renew
        if self.worker_auto_renew_period is not None:
            result['worker_auto_renew_period'] = self.worker_auto_renew_period
        if self.worker_data_disk is not None:
            result['worker_data_disk'] = self.worker_data_disk
        result['worker_data_disks'] = []
        if self.worker_data_disks is not None:
            for k in self.worker_data_disks:
                result['worker_data_disks'].append(k.to_map() if k else None)
        if self.worker_instance_charge_type is not None:
            result['worker_instance_charge_type'] = self.worker_instance_charge_type
        if self.worker_instance_types is not None:
            result['worker_instance_types'] = self.worker_instance_types
        if self.worker_period is not None:
            result['worker_period'] = self.worker_period
        if self.worker_period_unit is not None:
            result['worker_period_unit'] = self.worker_period_unit
        if self.worker_system_disk_category is not None:
            result['worker_system_disk_category'] = self.worker_system_disk_category
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        return result

    def from_map(self, map={}):
        if map.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = map.get('cloud_monitor_flags')
        if map.get('count') is not None:
            self.count = map.get('count')
        if map.get('cpu_policy') is not None:
            self.cpu_policy = map.get('cpu_policy')
        if map.get('disable_rollback') is not None:
            self.disable_rollback = map.get('disable_rollback')
        if map.get('image_id') is not None:
            self.image_id = map.get('image_id')
        if map.get('key_pair') is not None:
            self.key_pair = map.get('key_pair')
        if map.get('login_password') is not None:
            self.login_password = map.get('login_password')
        if map.get('rds_instances') is not None:
            self.rds_instances = map.get('rds_instances')
        if map.get('runtime') is not None:
            temp_model = ScaleOutClusterRequestRuntime()
            self.runtime = temp_model.from_map(map['runtime'])
        self.tags = []
        if map.get('tags') is not None:
            for k in map.get('tags'):
                temp_model = ScaleOutClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if map.get('taints') is not None:
            for k in map.get('taints'):
                temp_model = ScaleOutClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if map.get('user_data') is not None:
            self.user_data = map.get('user_data')
        if map.get('vswitch_ids') is not None:
            self.vswitch_ids = map.get('vswitch_ids')
        if map.get('worker_auto_renew') is not None:
            self.worker_auto_renew = map.get('worker_auto_renew')
        if map.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = map.get('worker_auto_renew_period')
        if map.get('worker_data_disk') is not None:
            self.worker_data_disk = map.get('worker_data_disk')
        self.worker_data_disks = []
        if map.get('worker_data_disks') is not None:
            for k in map.get('worker_data_disks'):
                temp_model = ScaleOutClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if map.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = map.get('worker_instance_charge_type')
        if map.get('worker_instance_types') is not None:
            self.worker_instance_types = map.get('worker_instance_types')
        if map.get('worker_period') is not None:
            self.worker_period = map.get('worker_period')
        if map.get('worker_period_unit') is not None:
            self.worker_period_unit = map.get('worker_period_unit')
        if map.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = map.get('worker_system_disk_category')
        if map.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = map.get('worker_system_disk_size')
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
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('version') is not None:
            self.version = map.get('version')
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
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
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
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('effect') is not None:
            self.effect = map.get('effect')
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class ScaleOutClusterRequestWorkerDataDisks(TeaModel):
    def __init__(self, category=None, encrypted=None, size=None):
        # 数据盘类型。
        self.category = category        # type: str
        # 是否对数据盘加密。
        self.encrypted = encrypted      # type: str
        # 数据盘大小。
        self.size = size                # type: int

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, map={}):
        if map.get('category') is not None:
            self.category = map.get('category')
        if map.get('encrypted') is not None:
            self.encrypted = map.get('encrypted')
        if map.get('size') is not None:
            self.size = map.get('size')
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('request_id') is not None:
            self.request_id = map.get('request_id')
        if map.get('task_id') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = ScaleOutClusterResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        return result

    def from_map(self, map={}):
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = ModifyClusterTagsRequestBody()
                self.body.append(temp_model.from_map(k))
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
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, map={}):
        if map.get('key') is not None:
            self.key = map.get('key')
        if map.get('value') is not None:
            self.value = map.get('value')
        return self


class ModifyClusterTagsResponse(TeaModel):
    def __init__(self, headers=None):
        self.headers = headers          # type: Dict[str, str]

    def validate(self):
        self.validate_required(self.headers, 'headers')

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, map={}):
        if map.get('Namespace') is not None:
            self.namespace = map.get('Namespace')
        if map.get('Type') is not None:
            self.type = map.get('Type')
        if map.get('Name') is not None:
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
        return result

    def from_map(self, map={}):
        self.triggers = []
        if map.get('triggers') is not None:
            for k in map.get('triggers'):
                temp_model = GetKubernetesTriggerResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
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
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, map={}):
        if map.get('action') is not None:
            self.action = map.get('action')
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('id') is not None:
            self.id = map.get('id')
        if map.get('project_id') is not None:
            self.project_id = map.get('project_id')
        if map.get('token') is not None:
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class GetUpgradeStatusResponseBody(TeaModel):
    def __init__(self, error_message=None, precheck_report_id=None, status=None, upgrade_step=None,
                 upgrade_task=None):
        # 错误信息描述。
        self.error_message = error_message  # type: str
        # 预检查返回ID。
        self.precheck_report_id = precheck_report_id  # type: str
        # 升级状态。
        self.status = status            # type: str
        # 升级任务执行到哪一步了。
        self.upgrade_step = upgrade_step  # type: str
        # 升级任务详情。
        self.upgrade_task = upgrade_task  # type: GetUpgradeStatusResponseBodyUpgradeTask

    def validate(self):
        if self.upgrade_task:
            self.upgrade_task.validate()

    def to_map(self):
        result = {}
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.precheck_report_id is not None:
            result['precheck_report_id'] = self.precheck_report_id
        if self.status is not None:
            result['status'] = self.status
        if self.upgrade_step is not None:
            result['upgrade_step'] = self.upgrade_step
        if self.upgrade_task is not None:
            result['upgrade_task'] = self.upgrade_task.to_map()
        return result

    def from_map(self, map={}):
        if map.get('error_message') is not None:
            self.error_message = map.get('error_message')
        if map.get('precheck_report_id') is not None:
            self.precheck_report_id = map.get('precheck_report_id')
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('upgrade_step') is not None:
            self.upgrade_step = map.get('upgrade_step')
        if map.get('upgrade_task') is not None:
            temp_model = GetUpgradeStatusResponseBodyUpgradeTask()
            self.upgrade_task = temp_model.from_map(map['upgrade_task'])
        return self


class GetUpgradeStatusResponseBodyUpgradeTask(TeaModel):
    def __init__(self, status=None, message=None):
        # 任务状态：  emptry、running、success、failed
        self.status = status            # type: str
        # 任务描述信息。
        self.message = message          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.status is not None:
            result['status'] = self.status
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, map={}):
        if map.get('status') is not None:
            self.status = map.get('status')
        if map.get('message') is not None:
            self.message = map.get('message')
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
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = GetUpgradeStatusResponseBody()
            self.body = temp_model.from_map(map['body'])
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
        if self.headers is not None:
            result['headers'] = self.headers
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        self.body = []
        if map.get('body') is not None:
            for k in map.get('body'):
                temp_model = DescribeClusterResourcesResponseBody()
                self.body.append(temp_model.from_map(k))
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
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created is not None:
            result['created'] = self.created
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.resource_info is not None:
            result['resource_info'] = self.resource_info
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, map={}):
        if map.get('cluster_id') is not None:
            self.cluster_id = map.get('cluster_id')
        if map.get('created') is not None:
            self.created = map.get('created')
        if map.get('instance_id') is not None:
            self.instance_id = map.get('instance_id')
        if map.get('resource_info') is not None:
            self.resource_info = map.get('resource_info')
        if map.get('resource_type') is not None:
            self.resource_type = map.get('resource_type')
        if map.get('state') is not None:
            self.state = map.get('state')
        return self


class DeleteClusterNodesRequest(TeaModel):
    def __init__(self, drain_node=None, release_node=None, nodes=None):
        # 是否自动排空节点上的Pod。
        self.drain_node = drain_node    # type: bool
        # 是否同时释放 ECS
        self.release_node = release_node  # type: bool
        # 移除节点列表。
        self.nodes = nodes              # type: List[str]

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.release_node is not None:
            result['release_node'] = self.release_node
        if self.nodes is not None:
            result['nodes'] = self.nodes
        return result

    def from_map(self, map={}):
        if map.get('drain_node') is not None:
            self.drain_node = map.get('drain_node')
        if map.get('release_node') is not None:
            self.release_node = map.get('release_node')
        if map.get('nodes') is not None:
            self.nodes = map.get('nodes')
        return self


class DeleteClusterNodesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # 请求ID。
        self.request_id = request_id    # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, map={}):
        if map.get('requestId') is not None:
            self.request_id = map.get('requestId')
        return self


class DeleteClusterNodesResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers          # type: Dict[str, str]
        self.body = body                # type: DeleteClusterNodesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        result = {}
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, map={}):
        if map.get('headers') is not None:
            self.headers = map.get('headers')
        if map.get('body') is not None:
            temp_model = DeleteClusterNodesResponseBody()
            self.body = temp_model.from_map(map['body'])
        return self


class StandardComponentsValue(TeaModel):
    def __init__(self, description=None, disabled=None, name=None, required=None, version=None):
        # 标准组件信息，包含各个组件的描述信息。
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
        if self.description is not None:
            result['description'] = self.description
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        if self.required is not None:
            result['required'] = self.required
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('disabled') is not None:
            self.disabled = map.get('disabled')
        if map.get('name') is not None:
            self.name = map.get('name')
        if map.get('required') is not None:
            self.required = map.get('required')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self


class AddonsVersionValue(TeaModel):
    def __init__(self, can_upgrade=None, changed=None, component_name=None, description=None, message=None,
                 next_version=None, required=None, template=None, version=None):
        # 组件是否可升级
        self.can_upgrade = can_upgrade  # type: bool
        # 组件是否升级过。
        self.changed = changed          # type: str
        # 组件名称。
        self.component_name = component_name  # type: str
        # 组件说明信息。
        self.description = description  # type: str
        # 是否可升级的额外说明信息。
        self.message = message          # type: str
        # 组件下一个可升级版本。
        self.next_version = next_version  # type: str
        # 组件是否为必需组件
        self.required = required        # type: bool
        # 组件最新模板内容。
        self.template = template        # type: str
        # 组件当前版本。
        self.version = version          # type: str

    def validate(self):
        pass

    def to_map(self):
        result = {}
        if self.can_upgrade is not None:
            result['can_upgrade'] = self.can_upgrade
        if self.changed is not None:
            result['changed'] = self.changed
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.description is not None:
            result['description'] = self.description
        if self.message is not None:
            result['message'] = self.message
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.required is not None:
            result['required'] = self.required
        if self.template is not None:
            result['template'] = self.template
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, map={}):
        if map.get('can_upgrade') is not None:
            self.can_upgrade = map.get('can_upgrade')
        if map.get('changed') is not None:
            self.changed = map.get('changed')
        if map.get('component_name') is not None:
            self.component_name = map.get('component_name')
        if map.get('description') is not None:
            self.description = map.get('description')
        if map.get('message') is not None:
            self.message = map.get('message')
        if map.get('next_version') is not None:
            self.next_version = map.get('next_version')
        if map.get('required') is not None:
            self.required = map.get('required')
        if map.get('template') is not None:
            self.template = map.get('template')
        if map.get('version') is not None:
            self.version = map.get('version')
        return self
