# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class Addon(TeaModel):
    def __init__(
        self,
        config: str = None,
        disabled: bool = None,
        name: str = None,
    ):
        self.config = config
        self.disabled = disabled
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DataDisk(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        category: str = None,
        encrypted: str = None,
        performance_level: str = None,
        size: int = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.category = category
        self.encrypted = encrypted
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.performance_level is not None:
            result['performance_level'] = self.performance_level
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class MaintenanceWindow(TeaModel):
    def __init__(
        self,
        duration: str = None,
        enable: bool = None,
        maintenance_time: str = None,
        weekly_period: str = None,
    ):
        self.duration = duration
        self.enable = enable
        self.maintenance_time = maintenance_time
        self.weekly_period = weekly_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.enable is not None:
            result['enable'] = self.enable
        if self.maintenance_time is not None:
            result['maintenance_time'] = self.maintenance_time
        if self.weekly_period is not None:
            result['weekly_period'] = self.weekly_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('maintenance_time') is not None:
            self.maintenance_time = m.get('maintenance_time')
        if m.get('weekly_period') is not None:
            self.weekly_period = m.get('weekly_period')
        return self


class Runtime(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
    ):
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class Tag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class Taint(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class AttachInstancesRequest(TeaModel):
    def __init__(
        self,
        cpu_policy: str = None,
        format_disk: bool = None,
        image_id: str = None,
        instances: List[str] = None,
        is_edge_worker: bool = None,
        keep_instance_name: bool = None,
        key_pair: str = None,
        nodepool_id: str = None,
        password: str = None,
        rds_instances: List[str] = None,
        runtime: Runtime = None,
        tags: List[Tag] = None,
        user_data: str = None,
    ):
        self.cpu_policy = cpu_policy
        self.format_disk = format_disk
        self.image_id = image_id
        self.instances = instances
        self.is_edge_worker = is_edge_worker
        self.keep_instance_name = keep_instance_name
        self.key_pair = key_pair
        self.nodepool_id = nodepool_id
        self.password = password
        self.rds_instances = rds_instances
        self.runtime = runtime
        self.tags = tags
        self.user_data = user_data

    def validate(self):
        if self.runtime:
            self.runtime.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('is_edge_worker') is not None:
            self.is_edge_worker = m.get('is_edge_worker')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('password') is not None:
            self.password = m.get('password')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class AttachInstancesResponseBodyList(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
    ):
        self.code = code
        self.instance_id = instance_id
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class AttachInstancesResponseBody(TeaModel):
    def __init__(
        self,
        list: List[AttachInstancesResponseBodyList] = None,
        task_id: str = None,
    ):
        self.list = list
        self.task_id = task_id

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['list'] = []
        if self.list is not None:
            for k in self.list:
                result['list'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.list = []
        if m.get('list') is not None:
            for k in m.get('list'):
                temp_model = AttachInstancesResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class AttachInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AttachInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelClusterUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CancelComponentUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CancelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CancelWorkflowRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
    ):
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class CancelWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateAutoscalingConfigRequest(TeaModel):
    def __init__(
        self,
        cool_down_duration: str = None,
        expander: str = None,
        gpu_utilization_threshold: str = None,
        scale_down_enabled: bool = None,
        scan_interval: str = None,
        unneeded_duration: str = None,
        utilization_threshold: str = None,
    ):
        self.cool_down_duration = cool_down_duration
        self.expander = expander
        self.gpu_utilization_threshold = gpu_utilization_threshold
        self.scale_down_enabled = scale_down_enabled
        self.scan_interval = scan_interval
        self.unneeded_duration = unneeded_duration
        self.utilization_threshold = utilization_threshold

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cool_down_duration is not None:
            result['cool_down_duration'] = self.cool_down_duration
        if self.expander is not None:
            result['expander'] = self.expander
        if self.gpu_utilization_threshold is not None:
            result['gpu_utilization_threshold'] = self.gpu_utilization_threshold
        if self.scale_down_enabled is not None:
            result['scale_down_enabled'] = self.scale_down_enabled
        if self.scan_interval is not None:
            result['scan_interval'] = self.scan_interval
        if self.unneeded_duration is not None:
            result['unneeded_duration'] = self.unneeded_duration
        if self.utilization_threshold is not None:
            result['utilization_threshold'] = self.utilization_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cool_down_duration') is not None:
            self.cool_down_duration = m.get('cool_down_duration')
        if m.get('expander') is not None:
            self.expander = m.get('expander')
        if m.get('gpu_utilization_threshold') is not None:
            self.gpu_utilization_threshold = m.get('gpu_utilization_threshold')
        if m.get('scale_down_enabled') is not None:
            self.scale_down_enabled = m.get('scale_down_enabled')
        if m.get('scan_interval') is not None:
            self.scan_interval = m.get('scan_interval')
        if m.get('unneeded_duration') is not None:
            self.unneeded_duration = m.get('unneeded_duration')
        if m.get('utilization_threshold') is not None:
            self.utilization_threshold = m.get('utilization_threshold')
        return self


class CreateAutoscalingConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateClusterRequestWorkerDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        encrypted: str = None,
        performance_level: str = None,
        size: str = None,
    ):
        self.category = category
        self.encrypted = encrypted
        self.performance_level = performance_level
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.performance_level is not None:
            result['performance_level'] = self.performance_level
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class CreateClusterRequest(TeaModel):
    def __init__(
        self,
        addons: List[Addon] = None,
        api_audiences: str = None,
        charge_type: str = None,
        cis_enabled: bool = None,
        cloud_monitor_flags: bool = None,
        cluster_domain: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        container_cidr: str = None,
        controlplane_log_components: List[str] = None,
        controlplane_log_project: str = None,
        controlplane_log_ttl: str = None,
        cpu_policy: str = None,
        custom_san: str = None,
        deletion_protection: bool = None,
        disable_rollback: bool = None,
        enable_rrsa: bool = None,
        encryption_provider_key: str = None,
        endpoint_public_access: bool = None,
        format_disk: bool = None,
        image_id: str = None,
        image_type: str = None,
        instances: List[str] = None,
        is_enterprise_security_group: bool = None,
        keep_instance_name: bool = None,
        key_pair: str = None,
        kubernetes_version: str = None,
        load_balancer_spec: str = None,
        logging_type: str = None,
        login_password: str = None,
        master_auto_renew: bool = None,
        master_auto_renew_period: int = None,
        master_count: int = None,
        master_instance_charge_type: str = None,
        master_instance_types: List[str] = None,
        master_period: int = None,
        master_period_unit: str = None,
        master_system_disk_category: str = None,
        master_system_disk_performance_level: str = None,
        master_system_disk_size: int = None,
        master_system_disk_snapshot_policy_id: str = None,
        master_vswitch_ids: List[str] = None,
        name: str = None,
        nat_gateway: bool = None,
        node_cidr_mask: str = None,
        node_name_mode: str = None,
        node_port_range: str = None,
        num_of_nodes: int = None,
        os_type: str = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        pod_vswitch_ids: List[str] = None,
        profile: str = None,
        proxy_mode: str = None,
        rds_instances: List[str] = None,
        region_id: str = None,
        resource_group_id: str = None,
        runtime: Runtime = None,
        security_group_id: str = None,
        service_account_issuer: str = None,
        service_cidr: str = None,
        service_discovery_types: List[str] = None,
        snat_entry: bool = None,
        soc_enabled: bool = None,
        ssh_flags: bool = None,
        tags: List[Tag] = None,
        taints: List[Taint] = None,
        timeout_mins: int = None,
        timezone: str = None,
        user_ca: str = None,
        user_data: str = None,
        vpcid: str = None,
        vswitch_ids: List[str] = None,
        worker_auto_renew: bool = None,
        worker_auto_renew_period: int = None,
        worker_data_disks: List[CreateClusterRequestWorkerDataDisks] = None,
        worker_instance_charge_type: str = None,
        worker_instance_types: List[str] = None,
        worker_period: int = None,
        worker_period_unit: str = None,
        worker_system_disk_category: str = None,
        worker_system_disk_performance_level: str = None,
        worker_system_disk_size: int = None,
        worker_system_disk_snapshot_policy_id: str = None,
        worker_vswitch_ids: List[str] = None,
        zone_id: str = None,
    ):
        self.addons = addons
        self.api_audiences = api_audiences
        self.charge_type = charge_type
        self.cis_enabled = cis_enabled
        self.cloud_monitor_flags = cloud_monitor_flags
        self.cluster_domain = cluster_domain
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.container_cidr = container_cidr
        self.controlplane_log_components = controlplane_log_components
        self.controlplane_log_project = controlplane_log_project
        self.controlplane_log_ttl = controlplane_log_ttl
        self.cpu_policy = cpu_policy
        self.custom_san = custom_san
        self.deletion_protection = deletion_protection
        self.disable_rollback = disable_rollback
        self.enable_rrsa = enable_rrsa
        self.encryption_provider_key = encryption_provider_key
        self.endpoint_public_access = endpoint_public_access
        self.format_disk = format_disk
        self.image_id = image_id
        self.image_type = image_type
        self.instances = instances
        self.is_enterprise_security_group = is_enterprise_security_group
        self.keep_instance_name = keep_instance_name
        self.key_pair = key_pair
        self.kubernetes_version = kubernetes_version
        self.load_balancer_spec = load_balancer_spec
        self.logging_type = logging_type
        self.login_password = login_password
        self.master_auto_renew = master_auto_renew
        self.master_auto_renew_period = master_auto_renew_period
        self.master_count = master_count
        self.master_instance_charge_type = master_instance_charge_type
        self.master_instance_types = master_instance_types
        self.master_period = master_period
        self.master_period_unit = master_period_unit
        self.master_system_disk_category = master_system_disk_category
        self.master_system_disk_performance_level = master_system_disk_performance_level
        self.master_system_disk_size = master_system_disk_size
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        self.master_vswitch_ids = master_vswitch_ids
        self.name = name
        self.nat_gateway = nat_gateway
        self.node_cidr_mask = node_cidr_mask
        self.node_name_mode = node_name_mode
        self.node_port_range = node_port_range
        self.num_of_nodes = num_of_nodes
        self.os_type = os_type
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.pod_vswitch_ids = pod_vswitch_ids
        self.profile = profile
        self.proxy_mode = proxy_mode
        self.rds_instances = rds_instances
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.runtime = runtime
        self.security_group_id = security_group_id
        self.service_account_issuer = service_account_issuer
        self.service_cidr = service_cidr
        self.service_discovery_types = service_discovery_types
        self.snat_entry = snat_entry
        self.soc_enabled = soc_enabled
        self.ssh_flags = ssh_flags
        self.tags = tags
        self.taints = taints
        self.timeout_mins = timeout_mins
        self.timezone = timezone
        self.user_ca = user_ca
        self.user_data = user_data
        self.vpcid = vpcid
        self.vswitch_ids = vswitch_ids
        self.worker_auto_renew = worker_auto_renew
        self.worker_auto_renew_period = worker_auto_renew_period
        self.worker_data_disks = worker_data_disks
        self.worker_instance_charge_type = worker_instance_charge_type
        self.worker_instance_types = worker_instance_types
        self.worker_period = worker_period
        self.worker_period_unit = worker_period_unit
        self.worker_system_disk_category = worker_system_disk_category
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        self.worker_system_disk_size = worker_system_disk_size
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        self.worker_vswitch_ids = worker_vswitch_ids
        self.zone_id = zone_id

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        if self.api_audiences is not None:
            result['api_audiences'] = self.api_audiences
        if self.charge_type is not None:
            result['charge_type'] = self.charge_type
        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.cluster_domain is not None:
            result['cluster_domain'] = self.cluster_domain
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.container_cidr is not None:
            result['container_cidr'] = self.container_cidr
        if self.controlplane_log_components is not None:
            result['controlplane_log_components'] = self.controlplane_log_components
        if self.controlplane_log_project is not None:
            result['controlplane_log_project'] = self.controlplane_log_project
        if self.controlplane_log_ttl is not None:
            result['controlplane_log_ttl'] = self.controlplane_log_ttl
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        if self.custom_san is not None:
            result['custom_san'] = self.custom_san
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.disable_rollback is not None:
            result['disable_rollback'] = self.disable_rollback
        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa
        if self.encryption_provider_key is not None:
            result['encryption_provider_key'] = self.encryption_provider_key
        if self.endpoint_public_access is not None:
            result['endpoint_public_access'] = self.endpoint_public_access
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.image_type is not None:
            result['image_type'] = self.image_type
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
        if self.load_balancer_spec is not None:
            result['load_balancer_spec'] = self.load_balancer_spec
        if self.logging_type is not None:
            result['logging_type'] = self.logging_type
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
        if self.master_system_disk_performance_level is not None:
            result['master_system_disk_performance_level'] = self.master_system_disk_performance_level
        if self.master_system_disk_size is not None:
            result['master_system_disk_size'] = self.master_system_disk_size
        if self.master_system_disk_snapshot_policy_id is not None:
            result['master_system_disk_snapshot_policy_id'] = self.master_system_disk_snapshot_policy_id
        if self.master_vswitch_ids is not None:
            result['master_vswitch_ids'] = self.master_vswitch_ids
        if self.name is not None:
            result['name'] = self.name
        if self.nat_gateway is not None:
            result['nat_gateway'] = self.nat_gateway
        if self.node_cidr_mask is not None:
            result['node_cidr_mask'] = self.node_cidr_mask
        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode
        if self.node_port_range is not None:
            result['node_port_range'] = self.node_port_range
        if self.num_of_nodes is not None:
            result['num_of_nodes'] = self.num_of_nodes
        if self.os_type is not None:
            result['os_type'] = self.os_type
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.platform is not None:
            result['platform'] = self.platform
        if self.pod_vswitch_ids is not None:
            result['pod_vswitch_ids'] = self.pod_vswitch_ids
        if self.profile is not None:
            result['profile'] = self.profile
        if self.proxy_mode is not None:
            result['proxy_mode'] = self.proxy_mode
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.runtime is not None:
            result['runtime'] = self.runtime.to_map()
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.service_account_issuer is not None:
            result['service_account_issuer'] = self.service_account_issuer
        if self.service_cidr is not None:
            result['service_cidr'] = self.service_cidr
        if self.service_discovery_types is not None:
            result['service_discovery_types'] = self.service_discovery_types
        if self.snat_entry is not None:
            result['snat_entry'] = self.snat_entry
        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled
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
        if self.timezone is not None:
            result['timezone'] = self.timezone
        if self.user_ca is not None:
            result['user_ca'] = self.user_ca
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
        if self.worker_system_disk_performance_level is not None:
            result['worker_system_disk_performance_level'] = self.worker_system_disk_performance_level
        if self.worker_system_disk_size is not None:
            result['worker_system_disk_size'] = self.worker_system_disk_size
        if self.worker_system_disk_snapshot_policy_id is not None:
            result['worker_system_disk_snapshot_policy_id'] = self.worker_system_disk_snapshot_policy_id
        if self.worker_vswitch_ids is not None:
            result['worker_vswitch_ids'] = self.worker_vswitch_ids
        if self.zone_id is not None:
            result['zone_id'] = self.zone_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('addons') is not None:
            for k in m.get('addons'):
                temp_model = Addon()
                self.addons.append(temp_model.from_map(k))
        if m.get('api_audiences') is not None:
            self.api_audiences = m.get('api_audiences')
        if m.get('charge_type') is not None:
            self.charge_type = m.get('charge_type')
        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('cluster_domain') is not None:
            self.cluster_domain = m.get('cluster_domain')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('container_cidr') is not None:
            self.container_cidr = m.get('container_cidr')
        if m.get('controlplane_log_components') is not None:
            self.controlplane_log_components = m.get('controlplane_log_components')
        if m.get('controlplane_log_project') is not None:
            self.controlplane_log_project = m.get('controlplane_log_project')
        if m.get('controlplane_log_ttl') is not None:
            self.controlplane_log_ttl = m.get('controlplane_log_ttl')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('custom_san') is not None:
            self.custom_san = m.get('custom_san')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('disable_rollback') is not None:
            self.disable_rollback = m.get('disable_rollback')
        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')
        if m.get('encryption_provider_key') is not None:
            self.encryption_provider_key = m.get('encryption_provider_key')
        if m.get('endpoint_public_access') is not None:
            self.endpoint_public_access = m.get('endpoint_public_access')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('is_enterprise_security_group') is not None:
            self.is_enterprise_security_group = m.get('is_enterprise_security_group')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('kubernetes_version') is not None:
            self.kubernetes_version = m.get('kubernetes_version')
        if m.get('load_balancer_spec') is not None:
            self.load_balancer_spec = m.get('load_balancer_spec')
        if m.get('logging_type') is not None:
            self.logging_type = m.get('logging_type')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('master_auto_renew') is not None:
            self.master_auto_renew = m.get('master_auto_renew')
        if m.get('master_auto_renew_period') is not None:
            self.master_auto_renew_period = m.get('master_auto_renew_period')
        if m.get('master_count') is not None:
            self.master_count = m.get('master_count')
        if m.get('master_instance_charge_type') is not None:
            self.master_instance_charge_type = m.get('master_instance_charge_type')
        if m.get('master_instance_types') is not None:
            self.master_instance_types = m.get('master_instance_types')
        if m.get('master_period') is not None:
            self.master_period = m.get('master_period')
        if m.get('master_period_unit') is not None:
            self.master_period_unit = m.get('master_period_unit')
        if m.get('master_system_disk_category') is not None:
            self.master_system_disk_category = m.get('master_system_disk_category')
        if m.get('master_system_disk_performance_level') is not None:
            self.master_system_disk_performance_level = m.get('master_system_disk_performance_level')
        if m.get('master_system_disk_size') is not None:
            self.master_system_disk_size = m.get('master_system_disk_size')
        if m.get('master_system_disk_snapshot_policy_id') is not None:
            self.master_system_disk_snapshot_policy_id = m.get('master_system_disk_snapshot_policy_id')
        if m.get('master_vswitch_ids') is not None:
            self.master_vswitch_ids = m.get('master_vswitch_ids')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nat_gateway') is not None:
            self.nat_gateway = m.get('nat_gateway')
        if m.get('node_cidr_mask') is not None:
            self.node_cidr_mask = m.get('node_cidr_mask')
        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')
        if m.get('node_port_range') is not None:
            self.node_port_range = m.get('node_port_range')
        if m.get('num_of_nodes') is not None:
            self.num_of_nodes = m.get('num_of_nodes')
        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('pod_vswitch_ids') is not None:
            self.pod_vswitch_ids = m.get('pod_vswitch_ids')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('proxy_mode') is not None:
            self.proxy_mode = m.get('proxy_mode')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('service_account_issuer') is not None:
            self.service_account_issuer = m.get('service_account_issuer')
        if m.get('service_cidr') is not None:
            self.service_cidr = m.get('service_cidr')
        if m.get('service_discovery_types') is not None:
            self.service_discovery_types = m.get('service_discovery_types')
        if m.get('snat_entry') is not None:
            self.snat_entry = m.get('snat_entry')
        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')
        if m.get('ssh_flags') is not None:
            self.ssh_flags = m.get('ssh_flags')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('timeout_mins') is not None:
            self.timeout_mins = m.get('timeout_mins')
        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')
        if m.get('user_ca') is not None:
            self.user_ca = m.get('user_ca')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('vpcid') is not None:
            self.vpcid = m.get('vpcid')
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = CreateClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_performance_level') is not None:
            self.worker_system_disk_performance_level = m.get('worker_system_disk_performance_level')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        if m.get('worker_system_disk_snapshot_policy_id') is not None:
            self.worker_system_disk_snapshot_policy_id = m.get('worker_system_disk_snapshot_policy_id')
        if m.get('worker_vswitch_ids') is not None:
            self.worker_vswitch_ids = m.get('worker_vswitch_ids')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class CreateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CreateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateClusterNodePoolRequestAutoScaling(TeaModel):
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
        self.eip_bandwidth = eip_bandwidth
        self.eip_internet_charge_type = eip_internet_charge_type
        self.enable = enable
        self.is_bond_eip = is_bond_eip
        self.max_instances = max_instances
        self.min_instances = min_instances
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestInterconnectConfig(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        self.bandwidth = bandwidth
        self.ccn_id = ccn_id
        self.ccn_region_id = ccn_region_id
        self.cen_id = cen_id
        self.improved_period = improved_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[Tag] = None,
        node_name_mode: str = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[Taint] = None,
        user_data: str = None,
    ):
        self.cms_enabled = cms_enabled
        self.cpu_policy = cpu_policy
        self.labels = labels
        self.node_name_mode = node_name_mode
        self.runtime = runtime
        self.runtime_version = runtime_version
        self.taints = taints
        self.user_data = user_data

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class CreateClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        self.auto_upgrade = auto_upgrade
        self.max_unavailable = max_unavailable
        self.surge = surge
        self.surge_percentage = surge_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestManagement(TeaModel):
    def __init__(
        self,
        auto_repair: bool = None,
        enable: bool = None,
        upgrade_config: CreateClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        self.auto_repair = auto_repair
        self.enable = enable
        self.upgrade_config = upgrade_config

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = CreateClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class CreateClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        self.name = name
        self.resource_group_id = resource_group_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestScalingGroupTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        image_id: str = None,
        image_type: str = None,
        instance_charge_type: str = None,
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
        rds_instances: List[str] = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[CreateClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        tags: List[CreateClusterNodePoolRequestScalingGroupTags] = None,
        vswitch_ids: List[str] = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.compensate_with_on_demand = compensate_with_on_demand
        self.data_disks = data_disks
        self.deploymentset_id = deploymentset_id
        self.desired_size = desired_size
        self.image_id = image_id
        self.image_type = image_type
        self.instance_charge_type = instance_charge_type
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair = key_pair
        self.login_password = login_password
        self.multi_az_policy = multi_az_policy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.rds_instances = rds_instances
        self.scaling_policy = scaling_policy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.vswitch_ids = vswitch_ids

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
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
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
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
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
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
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
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
            for k in m.get('spot_price_limit'):
                temp_model = CreateClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateClusterNodePoolRequestScalingGroupTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class CreateClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        self.tee_enable = tee_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class CreateClusterNodePoolRequest(TeaModel):
    def __init__(
        self,
        auto_scaling: CreateClusterNodePoolRequestAutoScaling = None,
        count: int = None,
        interconnect_config: CreateClusterNodePoolRequestInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: CreateClusterNodePoolRequestKubernetesConfig = None,
        management: CreateClusterNodePoolRequestManagement = None,
        max_nodes: int = None,
        nodepool_info: CreateClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: CreateClusterNodePoolRequestScalingGroup = None,
        tee_config: CreateClusterNodePoolRequestTeeConfig = None,
    ):
        self.auto_scaling = auto_scaling
        self.count = count
        self.interconnect_config = interconnect_config
        self.interconnect_mode = interconnect_mode
        self.kubernetes_config = kubernetes_config
        self.management = management
        self.max_nodes = max_nodes
        self.nodepool_info = nodepool_info
        self.scaling_group = scaling_group
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
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('interconnect_config') is not None:
            temp_model = CreateClusterNodePoolRequestInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = CreateClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = CreateClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = CreateClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = CreateClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('tee_config') is not None:
            temp_model = CreateClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class CreateClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        nodepool_id: str = None,
    ):
        self.nodepool_id = nodepool_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        return self


class CreateClusterNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateClusterNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateEdgeMachineRequest(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        model: str = None,
        sn: str = None,
    ):
        self.hostname = hostname
        self.model = model
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.model is not None:
            result['model'] = self.model
        if self.sn is not None:
            result['sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        return self


class CreateEdgeMachineResponseBody(TeaModel):
    def __init__(
        self,
        edge_machine_id: str = None,
        request_id: str = None,
    ):
        self.edge_machine_id = edge_machine_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class CreateEdgeMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateEdgeMachineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateEdgeMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateKubernetesTriggerRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateKubernetesTriggerResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.id = id
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateKubernetesTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateKubernetesTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateKubernetesTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tags: str = None,
        template: str = None,
        template_type: str = None,
    ):
        self.description = description
        self.name = name
        self.tags = tags
        self.template = template
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTemplateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTriggerRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTriggerResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        cluster_id: str = None,
        id: str = None,
        project_id: str = None,
        type: str = None,
    ):
        self.action = action
        self.cluster_id = cluster_id
        self.id = id
        self.project_id = project_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.id is not None:
            result['id'] = self.id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlertContactResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteAlertContactGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteClusterRequest(TeaModel):
    def __init__(
        self,
        keep_slb: bool = None,
        retain_all_resources: bool = None,
        retain_resources: List[str] = None,
    ):
        self.keep_slb = keep_slb
        self.retain_all_resources = retain_all_resources
        self.retain_resources = retain_resources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb
        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources
        if self.retain_resources is not None:
            result['retain_resources'] = self.retain_resources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')
        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')
        if m.get('retain_resources') is not None:
            self.retain_resources = m.get('retain_resources')
        return self


class DeleteClusterShrinkRequest(TeaModel):
    def __init__(
        self,
        keep_slb: bool = None,
        retain_all_resources: bool = None,
        retain_resources_shrink: str = None,
    ):
        self.keep_slb = keep_slb
        self.retain_all_resources = retain_all_resources
        self.retain_resources_shrink = retain_resources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_slb is not None:
            result['keep_slb'] = self.keep_slb
        if self.retain_all_resources is not None:
            result['retain_all_resources'] = self.retain_all_resources
        if self.retain_resources_shrink is not None:
            result['retain_resources'] = self.retain_resources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_slb') is not None:
            self.keep_slb = m.get('keep_slb')
        if m.get('retain_all_resources') is not None:
            self.retain_all_resources = m.get('retain_all_resources')
        if m.get('retain_resources') is not None:
            self.retain_resources_shrink = m.get('retain_resources')
        return self


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteClusterNodepoolRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class DeleteClusterNodepoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class DeleteClusterNodepoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterNodepoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterNodepoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterNodesRequest(TeaModel):
    def __init__(
        self,
        drain_node: bool = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        self.drain_node = drain_node
        self.nodes = nodes
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class DeleteClusterNodesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class DeleteClusterNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEdgeMachineRequest(TeaModel):
    def __init__(
        self,
        force: str = None,
    ):
        self.force = force

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force is not None:
            result['force'] = self.force
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force') is not None:
            self.force = m.get('force')
        return self


class DeleteEdgeMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteKubernetesTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeletePolicyInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
    ):
        self.instance_name = instance_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        return self


class DeletePolicyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[str] = None,
    ):
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class DeletePolicyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeletePolicyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeletePolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeployPolicyInstanceRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        namespaces: List[str] = None,
        parameters: Dict[str, Any] = None,
    ):
        self.action = action
        self.namespaces = namespaces
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.namespaces is not None:
            result['namespaces'] = self.namespaces
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class DeployPolicyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[str] = None,
    ):
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class DeployPolicyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeployPolicyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeployPolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescirbeWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        duration: str = None,
        finish_time: str = None,
        input_data_size: str = None,
        job_name: str = None,
        job_namespace: str = None,
        output_data_size: str = None,
        status: str = None,
        total_bases: str = None,
        total_reads: str = None,
        user_input_data: str = None,
    ):
        self.create_time = create_time
        self.duration = duration
        self.finish_time = finish_time
        self.input_data_size = input_data_size
        self.job_name = job_name
        self.job_namespace = job_namespace
        self.output_data_size = output_data_size
        self.status = status
        self.total_bases = total_bases
        self.total_reads = total_reads
        self.user_input_data = user_input_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.duration is not None:
            result['duration'] = self.duration
        if self.finish_time is not None:
            result['finish_time'] = self.finish_time
        if self.input_data_size is not None:
            result['input_data_size'] = self.input_data_size
        if self.job_name is not None:
            result['job_name'] = self.job_name
        if self.job_namespace is not None:
            result['job_namespace'] = self.job_namespace
        if self.output_data_size is not None:
            result['output_data_size'] = self.output_data_size
        if self.status is not None:
            result['status'] = self.status
        if self.total_bases is not None:
            result['total_bases'] = self.total_bases
        if self.total_reads is not None:
            result['total_reads'] = self.total_reads
        if self.user_input_data is not None:
            result['user_input_data'] = self.user_input_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('finish_time') is not None:
            self.finish_time = m.get('finish_time')
        if m.get('input_data_size') is not None:
            self.input_data_size = m.get('input_data_size')
        if m.get('job_name') is not None:
            self.job_name = m.get('job_name')
        if m.get('job_namespace') is not None:
            self.job_namespace = m.get('job_namespace')
        if m.get('output_data_size') is not None:
            self.output_data_size = m.get('output_data_size')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_bases') is not None:
            self.total_bases = m.get('total_bases')
        if m.get('total_reads') is not None:
            self.total_reads = m.get('total_reads')
        if m.get('user_input_data') is not None:
            self.user_input_data = m.get('user_input_data')
        return self


class DescirbeWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescirbeWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescirbeWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddonsRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        region: str = None,
    ):
        self.cluster_type = cluster_type
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class DescribeAddonsResponseBodyComponentGroupsItems(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeAddonsResponseBodyComponentGroups(TeaModel):
    def __init__(
        self,
        group_name: str = None,
        items: List[DescribeAddonsResponseBodyComponentGroupsItems] = None,
    ):
        self.group_name = group_name
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_name is not None:
            result['group_name'] = self.group_name
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = DescribeAddonsResponseBodyComponentGroupsItems()
                self.items.append(temp_model.from_map(k))
        return self


class StandardComponentsValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        description: str = None,
        required: str = None,
        disabled: bool = None,
    ):
        self.name = name
        self.version = version
        self.description = description
        self.required = required
        self.disabled = disabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        if self.description is not None:
            result['description'] = self.description
        if self.required is not None:
            result['required'] = self.required
        if self.disabled is not None:
            result['disabled'] = self.disabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('required') is not None:
            self.required = m.get('required')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        return self


class DescribeAddonsResponseBody(TeaModel):
    def __init__(
        self,
        component_groups: List[DescribeAddonsResponseBodyComponentGroups] = None,
        standard_components: Dict[str, StandardComponentsValue] = None,
    ):
        self.component_groups = component_groups
        self.standard_components = standard_components

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentGroups'] = []
        if self.component_groups is not None:
            for k in self.component_groups:
                result['ComponentGroups'].append(k.to_map() if k else None)
        result['StandardComponents'] = {}
        if self.standard_components is not None:
            for k, v in self.standard_components.items():
                result['StandardComponents'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_groups = []
        if m.get('ComponentGroups') is not None:
            for k in m.get('ComponentGroups'):
                temp_model = DescribeAddonsResponseBodyComponentGroups()
                self.component_groups.append(temp_model.from_map(k))
        self.standard_components = {}
        if m.get('StandardComponents') is not None:
            for k, v in m.get('StandardComponents').items():
                temp_model = StandardComponentsValue()
                self.standard_components[k] = temp_model.from_map(v)
        return self


class DescribeAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddonsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeAddonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAddonMetadataResponseBody(TeaModel):
    def __init__(
        self,
        config_schema: str = None,
        name: str = None,
        version: str = None,
    ):
        self.config_schema = config_schema
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config_schema is not None:
            result['config_schema'] = self.config_schema
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeClusterAddonMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterAddonMetadataResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterAddonMetadataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAddonUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAddonsUpgradeStatusRequest(TeaModel):
    def __init__(
        self,
        component_ids: List[str] = None,
    ):
        self.component_ids = component_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_ids is not None:
            result['componentIds'] = self.component_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids = m.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        component_ids_shrink: str = None,
    ):
        self.component_ids_shrink = component_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_ids_shrink is not None:
            result['componentIds'] = self.component_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentIds') is not None:
            self.component_ids_shrink = m.get('componentIds')
        return self


class DescribeClusterAddonsUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAddonsVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterAttachScriptsRequest(TeaModel):
    def __init__(
        self,
        arch: str = None,
        format_disk: bool = None,
        keep_instance_name: bool = None,
        nodepool_id: str = None,
        options: str = None,
        rds_instances: List[str] = None,
    ):
        self.arch = arch
        self.format_disk = format_disk
        self.keep_instance_name = keep_instance_name
        self.nodepool_id = nodepool_id
        self.options = options
        self.rds_instances = rds_instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.arch is not None:
            result['arch'] = self.arch
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.options is not None:
            result['options'] = self.options
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('arch') is not None:
            self.arch = m.get('arch')
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        return self


class DescribeClusterAttachScriptsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: str = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribeClusterDetailResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        created: str = None,
        current_version: str = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        init_version: str = None,
        maintenance_window: MaintenanceWindow = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        next_version: str = None,
        private_zone: bool = None,
        profile: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        size: int = None,
        state: str = None,
        subnet_cidr: str = None,
        tags: List[Tag] = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        worker_ram_role_name: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.created = created
        self.current_version = current_version
        self.deletion_protection = deletion_protection
        self.docker_version = docker_version
        self.external_loadbalancer_id = external_loadbalancer_id
        self.init_version = init_version
        self.maintenance_window = maintenance_window
        self.master_url = master_url
        self.meta_data = meta_data
        self.name = name
        self.network_mode = network_mode
        self.next_version = next_version
        self.private_zone = private_zone
        self.profile = profile
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.size = size
        self.state = state
        self.subnet_cidr = subnet_cidr
        self.tags = tags
        self.updated = updated
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.worker_ram_role_name = worker_ram_role_name
        self.zone_id = zone_id

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.next_version is not None:
            result['next_version'] = self.next_version
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClusterDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterEventsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        task_id: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class DescribeClusterEventsResponseBodyEventsData(TeaModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        reason: str = None,
    ):
        self.level = level
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class DescribeClusterEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: DescribeClusterEventsResponseBodyEventsData = None,
        event_id: str = None,
        source: str = None,
        subject: str = None,
        time: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.data = data
        self.event_id = event_id
        self.source = source
        self.subject = subject
        self.time = time
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.event_id is not None:
            result['event_id'] = self.event_id
        if self.source is not None:
            result['source'] = self.source
        if self.subject is not None:
            result['subject'] = self.subject
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('data') is not None:
            temp_model = DescribeClusterEventsResponseBodyEventsData()
            self.data = temp_model.from_map(m['data'])
        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeClusterEventsResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClusterEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeClusterEventsResponseBodyEvents] = None,
        page_info: DescribeClusterEventsResponseBodyPageInfo = None,
    ):
        self.events = events
        self.page_info = page_info

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = DescribeClusterEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeClusterEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeClusterEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterLogsResponseBody(TeaModel):
    def __init__(
        self,
        id: int = None,
        cluster_id: str = None,
        cluster_log: str = None,
        created: str = None,
        updated: str = None,
    ):
        self.id = id
        self.cluster_id = cluster_id
        self.cluster_log = cluster_log
        self.created = created
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['ID'] = self.id
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_log is not None:
            result['cluster_log'] = self.cluster_log
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ID') is not None:
            self.id = m.get('ID')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_log') is not None:
            self.cluster_log = m.get('cluster_log')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeClusterLogsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeClusterLogsResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClusterLogsResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClusterNodePoolDetailResponseBodyAutoScaling(TeaModel):
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
        self.eip_bandwidth = eip_bandwidth
        self.eip_internet_charge_type = eip_internet_charge_type
        self.enable = enable
        self.is_bond_eip = is_bond_eip
        self.max_instances = max_instances
        self.min_instances = min_instances
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyInterconnectConfig(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        self.bandwidth = bandwidth
        self.ccn_id = ccn_id
        self.ccn_region_id = ccn_region_id
        self.cen_id = cen_id
        self.improved_period = improved_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyKubernetesConfig(TeaModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[Tag] = None,
        node_name_mode: str = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[Taint] = None,
        user_data: str = None,
    ):
        self.cms_enabled = cms_enabled
        self.cpu_policy = cpu_policy
        self.labels = labels
        self.node_name_mode = node_name_mode
        self.runtime = runtime
        self.runtime_version = runtime_version
        self.taints = taints
        self.user_data = user_data

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        self.auto_upgrade = auto_upgrade
        self.max_unavailable = max_unavailable
        self.surge = surge
        self.surge_percentage = surge_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyManagement(TeaModel):
    def __init__(
        self,
        auto_repair: bool = None,
        enable: bool = None,
        upgrade_config: DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig = None,
    ):
        self.auto_repair = auto_repair
        self.enable = enable
        self.upgrade_config = upgrade_config

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolDetailResponseBodyNodepoolInfo(TeaModel):
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
        self.created = created
        self.is_default = is_default
        self.name = name
        self.nodepool_id = nodepool_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.type = type
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyScalingGroup(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        image_id: str = None,
        instance_charge_type: str = None,
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
        ram_policy: str = None,
        rds_instances: List[str] = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit] = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        tags: List[Tag] = None,
        vswitch_ids: List[str] = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.compensate_with_on_demand = compensate_with_on_demand
        self.data_disks = data_disks
        self.deploymentset_id = deploymentset_id
        self.desired_size = desired_size
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair = key_pair
        self.login_password = login_password
        self.multi_az_policy = multi_az_policy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.ram_policy = ram_policy
        self.rds_instances = rds_instances
        self.scaling_group_id = scaling_group_id
        self.scaling_policy = scaling_policy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.vswitch_ids = vswitch_ids

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.deploymentset_id is not None:
            result['deploymentset_id'] = self.deploymentset_id
        if self.desired_size is not None:
            result['desired_size'] = self.desired_size
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
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
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
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
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('deploymentset_id') is not None:
            self.deploymentset_id = m.get('deploymentset_id')
        if m.get('desired_size') is not None:
            self.desired_size = m.get('desired_size')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
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
        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_group_id') is not None:
            self.scaling_group_id = m.get('scaling_group_id')
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
            for k in m.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class DescribeClusterNodePoolDetailResponseBodyStatus(TeaModel):
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
        self.failed_nodes = failed_nodes
        self.healthy_nodes = healthy_nodes
        self.initial_nodes = initial_nodes
        self.offline_nodes = offline_nodes
        self.removing_nodes = removing_nodes
        self.serving_nodes = serving_nodes
        self.state = state
        self.total_nodes = total_nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyTeeConfig(TeaModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        self.tee_enable = tee_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class DescribeClusterNodePoolDetailResponseBody(TeaModel):
    def __init__(
        self,
        auto_scaling: DescribeClusterNodePoolDetailResponseBodyAutoScaling = None,
        interconnect_config: DescribeClusterNodePoolDetailResponseBodyInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: DescribeClusterNodePoolDetailResponseBodyKubernetesConfig = None,
        management: DescribeClusterNodePoolDetailResponseBodyManagement = None,
        max_nodes: int = None,
        nodepool_info: DescribeClusterNodePoolDetailResponseBodyNodepoolInfo = None,
        scaling_group: DescribeClusterNodePoolDetailResponseBodyScalingGroup = None,
        status: DescribeClusterNodePoolDetailResponseBodyStatus = None,
        tee_config: DescribeClusterNodePoolDetailResponseBodyTeeConfig = None,
    ):
        self.auto_scaling = auto_scaling
        self.interconnect_config = interconnect_config
        self.interconnect_mode = interconnect_mode
        self.kubernetes_config = kubernetes_config
        self.management = management
        self.max_nodes = max_nodes
        self.nodepool_info = nodepool_info
        self.scaling_group = scaling_group
        self.status = status
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
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
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
        if m.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('interconnect_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('status') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class DescribeClusterNodePoolDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterNodePoolDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling(TeaModel):
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
        self.eip_bandwidth = eip_bandwidth
        self.eip_internet_charge_type = eip_internet_charge_type
        self.enable = enable
        self.is_bond_eip = is_bond_eip
        self.max_instances = max_instances
        self.min_instances = min_instances
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        ccn_id: str = None,
        ccn_region_id: str = None,
        cen_id: str = None,
        improved_period: str = None,
    ):
        self.bandwidth = bandwidth
        self.ccn_id = ccn_id
        self.ccn_region_id = ccn_region_id
        self.cen_id = cen_id
        self.improved_period = improved_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig(TeaModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[Tag] = None,
        node_name_mode: str = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[Taint] = None,
        user_data: str = None,
    ):
        self.cms_enabled = cms_enabled
        self.cpu_policy = cpu_policy
        self.labels = labels
        self.node_name_mode = node_name_mode
        self.runtime = runtime
        self.runtime_version = runtime_version
        self.taints = taints
        self.user_data = user_data

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cms_enabled is not None:
            result['cms_enabled'] = self.cms_enabled
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
        result['labels'] = []
        if self.labels is not None:
            for k in self.labels:
                result['labels'].append(k.to_map() if k else None)
        if self.node_name_mode is not None:
            result['node_name_mode'] = self.node_name_mode
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('node_name_mode') is not None:
            self.node_name_mode = m.get('node_name_mode')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        self.auto_upgrade = auto_upgrade
        self.max_unavailable = max_unavailable
        self.surge = surge
        self.surge_percentage = surge_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsManagement(TeaModel):
    def __init__(
        self,
        auto_repair: bool = None,
        enable: bool = None,
        upgrade_config: DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig = None,
    ):
        self.auto_repair = auto_repair
        self.enable = enable
        self.upgrade_config = upgrade_config

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo(TeaModel):
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
        self.created = created
        self.is_default = is_default
        self.name = name
        self.nodepool_id = nodepool_id
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.type = type
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[DataDisk] = None,
        deploymentset_id: str = None,
        desired_size: int = None,
        image_id: str = None,
        instance_charge_type: str = None,
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
        ram_policy: str = None,
        rds_instances: List[str] = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit] = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        tags: List[Tag] = None,
        vswitch_ids: List[str] = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.compensate_with_on_demand = compensate_with_on_demand
        self.data_disks = data_disks
        self.deploymentset_id = deploymentset_id
        self.desired_size = desired_size
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair = key_pair
        self.login_password = login_password
        self.multi_az_policy = multi_az_policy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.ram_policy = ram_policy
        self.rds_instances = rds_instances
        self.scaling_group_id = scaling_group_id
        self.scaling_policy = scaling_policy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.vswitch_ids = vswitch_ids

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.deploymentset_id is not None:
            result['deploymentset_id'] = self.deploymentset_id
        if self.desired_size is not None:
            result['desired_size'] = self.desired_size
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
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
        if self.ram_policy is not None:
            result['ram_policy'] = self.ram_policy
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_group_id is not None:
            result['scaling_group_id'] = self.scaling_group_id
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
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('deploymentset_id') is not None:
            self.deploymentset_id = m.get('deploymentset_id')
        if m.get('desired_size') is not None:
            self.desired_size = m.get('desired_size')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
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
        if m.get('ram_policy') is not None:
            self.ram_policy = m.get('ram_policy')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_group_id') is not None:
            self.scaling_group_id = m.get('scaling_group_id')
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
            for k in m.get('spot_price_limit'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsStatus(TeaModel):
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
        self.failed_nodes = failed_nodes
        self.healthy_nodes = healthy_nodes
        self.initial_nodes = initial_nodes
        self.offline_nodes = offline_nodes
        self.removing_nodes = removing_nodes
        self.serving_nodes = serving_nodes
        self.state = state
        self.total_nodes = total_nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig(TeaModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        self.tee_enable = tee_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class DescribeClusterNodePoolsResponseBodyNodepools(TeaModel):
    def __init__(
        self,
        auto_scaling: DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling = None,
        interconnect_config: DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig = None,
        management: DescribeClusterNodePoolsResponseBodyNodepoolsManagement = None,
        max_nodes: int = None,
        nodepool_info: DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo = None,
        scaling_group: DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup = None,
        status: DescribeClusterNodePoolsResponseBodyNodepoolsStatus = None,
        tee_config: DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig = None,
    ):
        self.auto_scaling = auto_scaling
        self.interconnect_config = interconnect_config
        self.interconnect_mode = interconnect_mode
        self.kubernetes_config = kubernetes_config
        self.management = management
        self.max_nodes = max_nodes
        self.nodepool_info = nodepool_info
        self.scaling_group = scaling_group
        self.status = status
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
        if self.nodepool_info:
            self.nodepool_info.validate()
        if self.scaling_group:
            self.scaling_group.validate()
        if self.status:
            self.status.validate()
        if self.tee_config:
            self.tee_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
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
        if m.get('auto_scaling') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('interconnect_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('nodepool_info') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('status') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsStatus()
            self.status = temp_model.from_map(m['status'])
        if m.get('tee_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        return self


class DescribeClusterNodePoolsResponseBody(TeaModel):
    def __init__(
        self,
        nodepools: List[DescribeClusterNodePoolsResponseBodyNodepools] = None,
    ):
        self.nodepools = nodepools

    def validate(self):
        if self.nodepools:
            for k in self.nodepools:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['nodepools'] = []
        if self.nodepools is not None:
            for k in self.nodepools:
                result['nodepools'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodepools = []
        if m.get('nodepools') is not None:
            for k in m.get('nodepools'):
                temp_model = DescribeClusterNodePoolsResponseBodyNodepools()
                self.nodepools.append(temp_model.from_map(k))
        return self


class DescribeClusterNodePoolsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterNodePoolsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterNodePoolsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterNodesRequest(TeaModel):
    def __init__(
        self,
        instance_ids: str = None,
        nodepool_id: str = None,
        page_number: str = None,
        page_size: str = None,
        state: str = None,
    ):
        self.instance_ids = instance_ids
        self.nodepool_id = nodepool_id
        self.page_number = page_number
        self.page_size = page_size
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeClusterNodesResponseBodyNodes(TeaModel):
    def __init__(
        self,
        creation_time: str = None,
        error_message: str = None,
        expired_time: str = None,
        host_name: str = None,
        image_id: str = None,
        instance_charge_type: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_role: str = None,
        instance_status: str = None,
        instance_type: str = None,
        instance_type_family: str = None,
        ip_address: List[str] = None,
        is_aliyun_node: bool = None,
        node_name: str = None,
        node_status: str = None,
        nodepool_id: str = None,
        source: str = None,
        spot_strategy: str = None,
        state: str = None,
    ):
        self.creation_time = creation_time
        self.error_message = error_message
        self.expired_time = expired_time
        self.host_name = host_name
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_role = instance_role
        self.instance_status = instance_status
        self.instance_type = instance_type
        self.instance_type_family = instance_type_family
        self.ip_address = ip_address
        self.is_aliyun_node = is_aliyun_node
        self.node_name = node_name
        self.node_status = node_status
        self.nodepool_id = nodepool_id
        self.source = source
        self.spot_strategy = spot_strategy
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creation_time') is not None:
            self.creation_time = m.get('creation_time')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('expired_time') is not None:
            self.expired_time = m.get('expired_time')
        if m.get('host_name') is not None:
            self.host_name = m.get('host_name')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('instance_role') is not None:
            self.instance_role = m.get('instance_role')
        if m.get('instance_status') is not None:
            self.instance_status = m.get('instance_status')
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('instance_type_family') is not None:
            self.instance_type_family = m.get('instance_type_family')
        if m.get('ip_address') is not None:
            self.ip_address = m.get('ip_address')
        if m.get('is_aliyun_node') is not None:
            self.is_aliyun_node = m.get('is_aliyun_node')
        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')
        if m.get('node_status') is not None:
            self.node_status = m.get('node_status')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeClusterNodesResponseBodyPage(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClusterNodesResponseBody(TeaModel):
    def __init__(
        self,
        nodes: List[DescribeClusterNodesResponseBodyNodes] = None,
        page: DescribeClusterNodesResponseBodyPage = None,
    ):
        self.nodes = nodes
        self.page = page

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['nodes'].append(k.to_map() if k else None)
        if self.page is not None:
            result['page'] = self.page.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.nodes = []
        if m.get('nodes') is not None:
            for k in m.get('nodes'):
                temp_model = DescribeClusterNodesResponseBodyNodes()
                self.nodes.append(temp_model.from_map(k))
        if m.get('page') is not None:
            temp_model = DescribeClusterNodesResponseBodyPage()
            self.page = temp_model.from_map(m['page'])
        return self


class DescribeClusterNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterResourcesResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created: str = None,
        instance_id: str = None,
        resource_info: str = None,
        resource_type: str = None,
        state: str = None,
        auto_create: int = None,
    ):
        self.cluster_id = cluster_id
        self.created = created
        self.instance_id = instance_id
        self.resource_info = resource_info
        self.resource_type = resource_type
        self.state = state
        self.auto_create = auto_create

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.auto_create is not None:
            result['auto_create'] = self.auto_create
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('resource_info') is not None:
            self.resource_info = m.get('resource_info')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('auto_create') is not None:
            self.auto_create = m.get('auto_create')
        return self


class DescribeClusterResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeClusterResourcesResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClusterResourcesResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClusterTasksResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClusterTasksResponseBodyTasksError(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeClusterTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        created: str = None,
        error: DescribeClusterTasksResponseBodyTasksError = None,
        state: str = None,
        task_id: str = None,
        task_type: str = None,
        updated: str = None,
    ):
        self.created = created
        self.error = error
        self.state = state
        self.task_id = task_id
        self.task_type = task_type
        self.updated = updated

    def validate(self):
        if self.error:
            self.error.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created is not None:
            result['created'] = self.created
        if self.error is not None:
            result['error'] = self.error.to_map()
        if self.state is not None:
            result['state'] = self.state
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.task_type is not None:
            result['task_type'] = self.task_type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('error') is not None:
            temp_model = DescribeClusterTasksResponseBodyTasksError()
            self.error = temp_model.from_map(m['error'])
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('task_type') is not None:
            self.task_type = m.get('task_type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeClusterTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeClusterTasksResponseBodyPageInfo = None,
        request_id: str = None,
        tasks: List[DescribeClusterTasksResponseBodyTasks] = None,
    ):
        self.page_info = page_info
        self.request_id = request_id
        self.tasks = tasks

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_info') is not None:
            temp_model = DescribeClusterTasksResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = DescribeClusterTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        return self


class DescribeClusterTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterUserKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        temporary_duration_minutes: int = None,
    ):
        self.private_ip_address = private_ip_address
        self.temporary_duration_minutes = temporary_duration_minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        if self.temporary_duration_minutes is not None:
            result['TemporaryDurationMinutes'] = self.temporary_duration_minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        if m.get('TemporaryDurationMinutes') is not None:
            self.temporary_duration_minutes = m.get('TemporaryDurationMinutes')
        return self


class DescribeClusterUserKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        expiration: str = None,
    ):
        self.config = config
        self.expiration = expiration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.expiration is not None:
            result['expiration'] = self.expiration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        return self


class DescribeClusterUserKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterUserKubeconfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterUserKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterV2UserKubeconfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
    ):
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeClusterV2UserKubeconfigResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class DescribeClusterV2UserKubeconfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterV2UserKubeconfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClusterV2UserKubeconfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        name: str = None,
    ):
        self.cluster_type = cluster_type
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DescribeClustersResponseBodyTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClustersResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        created: str = None,
        current_version: str = None,
        data_disk_category: str = None,
        data_disk_size: int = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        init_version: str = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        private_zone: bool = None,
        profile: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        size: int = None,
        state: str = None,
        subnet_cidr: str = None,
        tags: List[DescribeClustersResponseBodyTags] = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_cidr: str = None,
        vswitch_id: str = None,
        worker_ram_role_name: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.created = created
        self.current_version = current_version
        self.data_disk_category = data_disk_category
        self.data_disk_size = data_disk_size
        self.deletion_protection = deletion_protection
        self.docker_version = docker_version
        self.external_loadbalancer_id = external_loadbalancer_id
        self.init_version = init_version
        self.master_url = master_url
        self.meta_data = meta_data
        self.name = name
        self.network_mode = network_mode
        self.private_zone = private_zone
        self.profile = profile
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.size = size
        self.state = state
        self.subnet_cidr = subnet_cidr
        self.tags = tags
        self.updated = updated
        self.vpc_id = vpc_id
        self.vswitch_cidr = vswitch_cidr
        self.vswitch_id = vswitch_id
        self.worker_ram_role_name = worker_ram_role_name
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('data_disk_category') is not None:
            self.data_disk_category = m.get('data_disk_category')
        if m.get('data_disk_size') is not None:
            self.data_disk_size = m.get('data_disk_size')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = DescribeClustersResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_cidr') is not None:
            self.vswitch_cidr = m.get('vswitch_cidr')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeClustersResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeClustersResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeClustersV1Request(TeaModel):
    def __init__(
        self,
        cluster_spec: str = None,
        cluster_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        profile: str = None,
        region_id: str = None,
    ):
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.name = name
        self.page_number = page_number
        self.page_size = page_size
        self.profile = profile
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.name is not None:
            result['name'] = self.name
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class DescribeClustersV1ResponseBodyClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        created: str = None,
        current_version: str = None,
        deletion_protection: bool = None,
        docker_version: str = None,
        external_loadbalancer_id: str = None,
        init_version: str = None,
        maintenance_window: MaintenanceWindow = None,
        master_url: str = None,
        meta_data: str = None,
        name: str = None,
        network_mode: str = None,
        next_version: str = None,
        private_zone: bool = None,
        profile: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        security_group_id: str = None,
        size: int = None,
        state: str = None,
        subnet_cidr: str = None,
        tags: List[Tag] = None,
        updated: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        worker_ram_role_name: str = None,
        zone_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.created = created
        self.current_version = current_version
        self.deletion_protection = deletion_protection
        self.docker_version = docker_version
        self.external_loadbalancer_id = external_loadbalancer_id
        self.init_version = init_version
        self.maintenance_window = maintenance_window
        self.master_url = master_url
        self.meta_data = meta_data
        self.name = name
        self.network_mode = network_mode
        self.next_version = next_version
        self.private_zone = private_zone
        self.profile = profile
        self.region_id = region_id
        self.resource_group_id = resource_group_id
        self.security_group_id = security_group_id
        self.size = size
        self.state = state
        self.subnet_cidr = subnet_cidr
        self.tags = tags
        self.updated = updated
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.worker_ram_role_name = worker_ram_role_name
        self.zone_id = zone_id

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created is not None:
            result['created'] = self.created
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.docker_version is not None:
            result['docker_version'] = self.docker_version
        if self.external_loadbalancer_id is not None:
            result['external_loadbalancer_id'] = self.external_loadbalancer_id
        if self.init_version is not None:
            result['init_version'] = self.init_version
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta_data is not None:
            result['meta_data'] = self.meta_data
        if self.name is not None:
            result['name'] = self.name
        if self.network_mode is not None:
            result['network_mode'] = self.network_mode
        if self.next_version is not None:
            result['next_version'] = self.next_version
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('docker_version') is not None:
            self.docker_version = m.get('docker_version')
        if m.get('external_loadbalancer_id') is not None:
            self.external_loadbalancer_id = m.get('external_loadbalancer_id')
        if m.get('init_version') is not None:
            self.init_version = m.get('init_version')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('network_mode') is not None:
            self.network_mode = m.get('network_mode')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('private_zone') is not None:
            self.private_zone = m.get('private_zone')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('subnet_cidr') is not None:
            self.subnet_cidr = m.get('subnet_cidr')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        if m.get('vswitch_id') is not None:
            self.vswitch_id = m.get('vswitch_id')
        if m.get('worker_ram_role_name') is not None:
            self.worker_ram_role_name = m.get('worker_ram_role_name')
        if m.get('zone_id') is not None:
            self.zone_id = m.get('zone_id')
        return self


class DescribeClustersV1ResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeClustersV1ResponseBody(TeaModel):
    def __init__(
        self,
        clusters: List[DescribeClustersV1ResponseBodyClusters] = None,
        page_info: DescribeClustersV1ResponseBodyPageInfo = None,
    ):
        self.clusters = clusters
        self.page_info = page_info

    def validate(self):
        if self.clusters:
            for k in self.clusters:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['clusters'] = []
        if self.clusters is not None:
            for k in self.clusters:
                result['clusters'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.clusters = []
        if m.get('clusters') is not None:
            for k in m.get('clusters'):
                temp_model = DescribeClustersV1ResponseBodyClusters()
                self.clusters.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeClustersV1ResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeClustersV1Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClustersV1ResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeClustersV1ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineActiveProcessResponseBody(TeaModel):
    def __init__(
        self,
        logs: str = None,
        progress: int = None,
        request_id: str = None,
        state: str = None,
        step: str = None,
    ):
        self.logs = logs
        self.progress = progress
        self.request_id = request_id
        self.state = state
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.logs is not None:
            result['logs'] = self.logs
        if self.progress is not None:
            result['progress'] = self.progress
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.state is not None:
            result['state'] = self.state
        if self.step is not None:
            result['step'] = self.step
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('logs') is not None:
            self.logs = m.get('logs')
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('step') is not None:
            self.step = m.get('step')
        return self


class DescribeEdgeMachineActiveProcessResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdgeMachineActiveProcessResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEdgeMachineActiveProcessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineModelsResponseBodyModels(TeaModel):
    def __init__(
        self,
        cpu: int = None,
        cpu_arch: str = None,
        created: str = None,
        description: str = None,
        manage_runtime: int = None,
        memory: int = None,
        model: str = None,
        model_id: str = None,
    ):
        self.cpu = cpu
        self.cpu_arch = cpu_arch
        self.created = created
        self.description = description
        self.manage_runtime = manage_runtime
        self.memory = memory
        self.model = model
        self.model_id = model_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.cpu_arch is not None:
            result['cpu_arch'] = self.cpu_arch
        if self.created is not None:
            result['created'] = self.created
        if self.description is not None:
            result['description'] = self.description
        if self.manage_runtime is not None:
            result['manage_runtime'] = self.manage_runtime
        if self.memory is not None:
            result['memory'] = self.memory
        if self.model is not None:
            result['model'] = self.model
        if self.model_id is not None:
            result['model_id'] = self.model_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('cpu_arch') is not None:
            self.cpu_arch = m.get('cpu_arch')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('manage_runtime') is not None:
            self.manage_runtime = m.get('manage_runtime')
        if m.get('memory') is not None:
            self.memory = m.get('memory')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('model_id') is not None:
            self.model_id = m.get('model_id')
        return self


class DescribeEdgeMachineModelsResponseBody(TeaModel):
    def __init__(
        self,
        models: List[DescribeEdgeMachineModelsResponseBodyModels] = None,
    ):
        self.models = models

    def validate(self):
        if self.models:
            for k in self.models:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['models'] = []
        if self.models is not None:
            for k in self.models:
                result['models'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.models = []
        if m.get('models') is not None:
            for k in m.get('models'):
                temp_model = DescribeEdgeMachineModelsResponseBodyModels()
                self.models.append(temp_model.from_map(k))
        return self


class DescribeEdgeMachineModelsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdgeMachineModelsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEdgeMachineModelsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachineTunnelConfigDetailResponseBody(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        model: str = None,
        product_key: str = None,
        request_id: str = None,
        sn: str = None,
        token: str = None,
        tunnel_endpoint: str = None,
    ):
        self.device_name = device_name
        self.model = model
        self.product_key = product_key
        self.request_id = request_id
        self.sn = sn
        self.token = token
        self.tunnel_endpoint = tunnel_endpoint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.model is not None:
            result['model'] = self.model
        if self.product_key is not None:
            result['product_key'] = self.product_key
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.sn is not None:
            result['sn'] = self.sn
        if self.token is not None:
            result['token'] = self.token
        if self.tunnel_endpoint is not None:
            result['tunnel_endpoint'] = self.tunnel_endpoint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('product_key') is not None:
            self.product_key = m.get('product_key')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('tunnel_endpoint') is not None:
            self.tunnel_endpoint = m.get('tunnel_endpoint')
        return self


class DescribeEdgeMachineTunnelConfigDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdgeMachineTunnelConfigDetailResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEdgeMachineTunnelConfigDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEdgeMachinesRequest(TeaModel):
    def __init__(
        self,
        hostname: str = None,
        life_state: str = None,
        model: str = None,
        online_state: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.hostname = hostname
        self.life_state = life_state
        self.model = model
        self.online_state = online_state
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.life_state is not None:
            result['life_state'] = self.life_state
        if self.model is not None:
            result['model'] = self.model
        if self.online_state is not None:
            result['online_state'] = self.online_state
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('life_state') is not None:
            self.life_state = m.get('life_state')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('online_state') is not None:
            self.online_state = m.get('online_state')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class DescribeEdgeMachinesResponseBodyEdgeMachines(TeaModel):
    def __init__(
        self,
        active_time: str = None,
        created: str = None,
        edge_machine_id: str = None,
        hostname: str = None,
        life_state: str = None,
        model: str = None,
        name: str = None,
        online_state: str = None,
        sn: str = None,
        updated: str = None,
    ):
        self.active_time = active_time
        self.created = created
        self.edge_machine_id = edge_machine_id
        self.hostname = hostname
        self.life_state = life_state
        self.model = model
        self.name = name
        self.online_state = online_state
        self.sn = sn
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_time is not None:
            result['active_time'] = self.active_time
        if self.created is not None:
            result['created'] = self.created
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.hostname is not None:
            result['hostname'] = self.hostname
        if self.life_state is not None:
            result['life_state'] = self.life_state
        if self.model is not None:
            result['model'] = self.model
        if self.name is not None:
            result['name'] = self.name
        if self.online_state is not None:
            result['online_state'] = self.online_state
        if self.sn is not None:
            result['sn'] = self.sn
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('active_time') is not None:
            self.active_time = m.get('active_time')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('hostname') is not None:
            self.hostname = m.get('hostname')
        if m.get('life_state') is not None:
            self.life_state = m.get('life_state')
        if m.get('model') is not None:
            self.model = m.get('model')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('online_state') is not None:
            self.online_state = m.get('online_state')
        if m.get('sn') is not None:
            self.sn = m.get('sn')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeEdgeMachinesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeEdgeMachinesResponseBody(TeaModel):
    def __init__(
        self,
        edge_machines: List[DescribeEdgeMachinesResponseBodyEdgeMachines] = None,
        page_info: DescribeEdgeMachinesResponseBodyPageInfo = None,
    ):
        self.edge_machines = edge_machines
        self.page_info = page_info

    def validate(self):
        if self.edge_machines:
            for k in self.edge_machines:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['edge_machines'] = []
        if self.edge_machines is not None:
            for k in self.edge_machines:
                result['edge_machines'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.edge_machines = []
        if m.get('edge_machines') is not None:
            for k in m.get('edge_machines'):
                temp_model = DescribeEdgeMachinesResponseBodyEdgeMachines()
                self.edge_machines.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeEdgeMachinesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeEdgeMachinesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEdgeMachinesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEdgeMachinesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeEventsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeEventsResponseBodyEventsData(TeaModel):
    def __init__(
        self,
        level: str = None,
        message: str = None,
        reason: str = None,
    ):
        self.level = level
        self.message = message
        self.reason = reason

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        return self


class DescribeEventsResponseBodyEvents(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        data: DescribeEventsResponseBodyEventsData = None,
        event_id: str = None,
        source: str = None,
        subject: str = None,
        time: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.data = data
        self.event_id = event_id
        self.source = source
        self.subject = subject
        self.time = time
        self.type = type

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.event_id is not None:
            result['event_id'] = self.event_id
        if self.source is not None:
            result['source'] = self.source
        if self.subject is not None:
            result['subject'] = self.subject
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('data') is not None:
            temp_model = DescribeEventsResponseBodyEventsData()
            self.data = temp_model.from_map(m['data'])
        if m.get('event_id') is not None:
            self.event_id = m.get('event_id')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeEventsResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeEventsResponseBody(TeaModel):
    def __init__(
        self,
        events: List[DescribeEventsResponseBodyEvents] = None,
        page_info: DescribeEventsResponseBodyPageInfo = None,
    ):
        self.events = events
        self.page_info = page_info

    def validate(self):
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = DescribeEventsResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('page_info') is not None:
            temp_model = DescribeEventsResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        return self


class DescribeEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeEventsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeExternalAgentRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: str = None,
    ):
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeExternalAgentResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class DescribeExternalAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeExternalAgentResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeExternalAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeKubernetesVersionMetadataRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        kubernetes_version: str = None,
        profile: str = None,
        region: str = None,
        runtime: str = None,
    ):
        self.cluster_type = cluster_type
        self.kubernetes_version = kubernetes_version
        self.profile = profile
        self.region = region
        self.runtime = runtime

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type
        if self.kubernetes_version is not None:
            result['KubernetesVersion'] = self.kubernetes_version
        if self.profile is not None:
            result['Profile'] = self.profile
        if self.region is not None:
            result['Region'] = self.region
        if self.runtime is not None:
            result['runtime'] = self.runtime
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')
        if m.get('KubernetesVersion') is not None:
            self.kubernetes_version = m.get('KubernetesVersion')
        if m.get('Profile') is not None:
            self.profile = m.get('Profile')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        return self


class DescribeKubernetesVersionMetadataResponseBodyImages(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        image_name: str = None,
        platform: str = None,
        os_version: str = None,
        image_type: str = None,
        os_type: str = None,
        image_category: str = None,
    ):
        self.image_id = image_id
        self.image_name = image_name
        self.platform = platform
        self.os_version = os_version
        self.image_type = image_type
        self.os_type = os_type
        self.image_category = image_category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('image_name') is not None:
            self.image_name = m.get('image_name')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        if m.get('os_version') is not None:
            self.os_version = m.get('os_version')
        if m.get('image_type') is not None:
            self.image_type = m.get('image_type')
        if m.get('os_type') is not None:
            self.os_type = m.get('os_type')
        if m.get('image_category') is not None:
            self.image_category = m.get('image_category')
        return self


class DescribeKubernetesVersionMetadataResponseBody(TeaModel):
    def __init__(
        self,
        capabilities: Dict[str, Any] = None,
        images: List[DescribeKubernetesVersionMetadataResponseBodyImages] = None,
        meta_data: Dict[str, Any] = None,
        runtimes: List[Runtime] = None,
        version: str = None,
        multi_az: str = None,
    ):
        self.capabilities = capabilities
        self.images = images
        self.meta_data = meta_data
        self.runtimes = runtimes
        self.version = version
        self.multi_az = multi_az

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capabilities') is not None:
            self.capabilities = m.get('capabilities')
        self.images = []
        if m.get('images') is not None:
            for k in m.get('images'):
                temp_model = DescribeKubernetesVersionMetadataResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('meta_data') is not None:
            self.meta_data = m.get('meta_data')
        self.runtimes = []
        if m.get('runtimes') is not None:
            for k in m.get('runtimes'):
                temp_model = Runtime()
                self.runtimes.append(temp_model.from_map(k))
        if m.get('version') is not None:
            self.version = m.get('version')
        if m.get('multi_az') is not None:
            self.multi_az = m.get('multi_az')
        return self


class DescribeKubernetesVersionMetadataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeKubernetesVersionMetadataResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeKubernetesVersionMetadataResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeNodePoolVulsResponseBodyVulRecordsVulList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        cve_list: List[str] = None,
        name: str = None,
        necessity: str = None,
    ):
        self.alias_name = alias_name
        self.cve_list = cve_list
        self.name = name
        self.necessity = necessity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias_name is not None:
            result['alias_name'] = self.alias_name
        if self.cve_list is not None:
            result['cve_list'] = self.cve_list
        if self.name is not None:
            result['name'] = self.name
        if self.necessity is not None:
            result['necessity'] = self.necessity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alias_name') is not None:
            self.alias_name = m.get('alias_name')
        if m.get('cve_list') is not None:
            self.cve_list = m.get('cve_list')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')
        return self


class DescribeNodePoolVulsResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        vul_list: List[DescribeNodePoolVulsResponseBodyVulRecordsVulList] = None,
    ):
        self.instance_id = instance_id
        self.vul_list = vul_list

    def validate(self):
        if self.vul_list:
            for k in self.vul_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        result['vul_list'] = []
        if self.vul_list is not None:
            for k in self.vul_list:
                result['vul_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        self.vul_list = []
        if m.get('vul_list') is not None:
            for k in m.get('vul_list'):
                temp_model = DescribeNodePoolVulsResponseBodyVulRecordsVulList()
                self.vul_list.append(temp_model.from_map(k))
        return self


class DescribeNodePoolVulsResponseBody(TeaModel):
    def __init__(
        self,
        vul_records: List[DescribeNodePoolVulsResponseBodyVulRecords] = None,
        vuls_fix_service_purchased: bool = None,
    ):
        self.vul_records = vul_records
        self.vuls_fix_service_purchased = vuls_fix_service_purchased

    def validate(self):
        if self.vul_records:
            for k in self.vul_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['vul_records'] = []
        if self.vul_records is not None:
            for k in self.vul_records:
                result['vul_records'].append(k.to_map() if k else None)
        if self.vuls_fix_service_purchased is not None:
            result['vuls_fix_service_purchased'] = self.vuls_fix_service_purchased
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vul_records = []
        if m.get('vul_records') is not None:
            for k in m.get('vul_records'):
                temp_model = DescribeNodePoolVulsResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        if m.get('vuls_fix_service_purchased') is not None:
            self.vuls_fix_service_purchased = m.get('vuls_fix_service_purchased')
        return self


class DescribeNodePoolVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeNodePoolVulsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeNodePoolVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePoliciesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: dict = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            self.body = m.get('body')
        return self


class DescribePolicyDetailsResponseBody(TeaModel):
    def __init__(
        self,
        action: str = None,
        category: str = None,
        description: str = None,
        is_deleted: int = None,
        name: str = None,
        no_config: int = None,
        severity: str = None,
        template: str = None,
    ):
        self.action = action
        self.category = category
        self.description = description
        self.is_deleted = is_deleted
        self.name = name
        self.no_config = no_config
        self.severity = severity
        self.template = template

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.category is not None:
            result['category'] = self.category
        if self.description is not None:
            result['description'] = self.description
        if self.is_deleted is not None:
            result['is_deleted'] = self.is_deleted
        if self.name is not None:
            result['name'] = self.name
        if self.no_config is not None:
            result['no_config'] = self.no_config
        if self.severity is not None:
            result['severity'] = self.severity
        if self.template is not None:
            result['template'] = self.template
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('is_deleted') is not None:
            self.is_deleted = m.get('is_deleted')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('no_config') is not None:
            self.no_config = m.get('no_config')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('template') is not None:
            self.template = m.get('template')
        return self


class DescribePolicyDetailsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyDetailsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyDetailsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        constraint_kind: str = None,
        msg: str = None,
        resource_kind: str = None,
        resource_name: str = None,
        resource_namespace: str = None,
    ):
        self.cluster_id = cluster_id
        self.constraint_kind = constraint_kind
        self.msg = msg
        self.resource_kind = resource_kind
        self.resource_name = resource_name
        self.resource_namespace = resource_namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.constraint_kind is not None:
            result['constraint_kind'] = self.constraint_kind
        if self.msg is not None:
            result['msg'] = self.msg
        if self.resource_kind is not None:
            result['resource_kind'] = self.resource_kind
        if self.resource_name is not None:
            result['resource_name'] = self.resource_name
        if self.resource_namespace is not None:
            result['resource_namespace'] = self.resource_namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('constraint_kind') is not None:
            self.constraint_kind = m.get('constraint_kind')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('resource_kind') is not None:
            self.resource_kind = m.get('resource_kind')
        if m.get('resource_name') is not None:
            self.resource_name = m.get('resource_name')
        if m.get('resource_namespace') is not None:
            self.resource_namespace = m.get('resource_namespace')
        return self


class DescribePolicyGovernanceInClusterResponseBodyAdmitLog(TeaModel):
    def __init__(
        self,
        count: int = None,
        log: DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog = None,
        progress: str = None,
    ):
        self.count = count
        self.log = log
        self.progress = progress

    def validate(self):
        if self.log:
            self.log.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.log is not None:
            result['log'] = self.log.to_map()
        if self.progress is not None:
            result['progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('log') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyAdmitLogLog()
            self.log = temp_model.from_map(m['log'])
        if m.get('progress') is not None:
            self.progress = m.get('progress')
        return self


class DescribePolicyGovernanceInClusterResponseBodyOnState(TeaModel):
    def __init__(
        self,
        enabled_count: int = None,
        severity: str = None,
        total: int = None,
    ):
        self.enabled_count = enabled_count
        self.severity = severity
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled_count is not None:
            result['enabled_count'] = self.enabled_count
        if self.severity is not None:
            result['severity'] = self.severity
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled_count') is not None:
            self.enabled_count = m.get('enabled_count')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny(TeaModel):
    def __init__(
        self,
        severity: str = None,
        violations: int = None,
    ):
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn(TeaModel):
    def __init__(
        self,
        severity: str = None,
        violations: int = None,
    ):
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyTotalViolations(TeaModel):
    def __init__(
        self,
        deny: DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny = None,
        warn: DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn = None,
    ):
        self.deny = deny
        self.warn = warn

    def validate(self):
        if self.deny:
            self.deny.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny is not None:
            result['deny'] = self.deny.to_map()
        if self.warn is not None:
            result['warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deny') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolationsDeny()
            self.deny = temp_model.from_map(m['deny'])
        if m.get('warn') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolationsWarn()
            self.warn = temp_model.from_map(m['warn'])
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolationsDeny(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        severity: str = None,
        violations: int = None,
    ):
        self.policy_description = policy_description
        self.policy_name = policy_name
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolationsWarn(TeaModel):
    def __init__(
        self,
        policy_description: str = None,
        policy_name: str = None,
        severity: str = None,
        violations: int = None,
    ):
        self.policy_description = policy_description
        self.policy_name = policy_name
        self.severity = severity
        self.violations = violations

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_description is not None:
            result['policyDescription'] = self.policy_description
        if self.policy_name is not None:
            result['policyName'] = self.policy_name
        if self.severity is not None:
            result['severity'] = self.severity
        if self.violations is not None:
            result['violations'] = self.violations
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policyDescription') is not None:
            self.policy_description = m.get('policyDescription')
        if m.get('policyName') is not None:
            self.policy_name = m.get('policyName')
        if m.get('severity') is not None:
            self.severity = m.get('severity')
        if m.get('violations') is not None:
            self.violations = m.get('violations')
        return self


class DescribePolicyGovernanceInClusterResponseBodyViolations(TeaModel):
    def __init__(
        self,
        deny: DescribePolicyGovernanceInClusterResponseBodyViolationsDeny = None,
        warn: DescribePolicyGovernanceInClusterResponseBodyViolationsWarn = None,
    ):
        self.deny = deny
        self.warn = warn

    def validate(self):
        if self.deny:
            self.deny.validate()
        if self.warn:
            self.warn.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny is not None:
            result['deny'] = self.deny.to_map()
        if self.warn is not None:
            result['warn'] = self.warn.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('deny') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolationsDeny()
            self.deny = temp_model.from_map(m['deny'])
        if m.get('warn') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolationsWarn()
            self.warn = temp_model.from_map(m['warn'])
        return self


class DescribePolicyGovernanceInClusterResponseBody(TeaModel):
    def __init__(
        self,
        admit_log: DescribePolicyGovernanceInClusterResponseBodyAdmitLog = None,
        on_state: List[DescribePolicyGovernanceInClusterResponseBodyOnState] = None,
        total_violations: DescribePolicyGovernanceInClusterResponseBodyTotalViolations = None,
        violations: DescribePolicyGovernanceInClusterResponseBodyViolations = None,
    ):
        self.admit_log = admit_log
        self.on_state = on_state
        self.total_violations = total_violations
        self.violations = violations

    def validate(self):
        if self.admit_log:
            self.admit_log.validate()
        if self.on_state:
            for k in self.on_state:
                if k:
                    k.validate()
        if self.total_violations:
            self.total_violations.validate()
        if self.violations:
            self.violations.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.admit_log is not None:
            result['admit_log'] = self.admit_log.to_map()
        result['on_state'] = []
        if self.on_state is not None:
            for k in self.on_state:
                result['on_state'].append(k.to_map() if k else None)
        if self.total_violations is not None:
            result['totalViolations'] = self.total_violations.to_map()
        if self.violations is not None:
            result['violations'] = self.violations.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('admit_log') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyAdmitLog()
            self.admit_log = temp_model.from_map(m['admit_log'])
        self.on_state = []
        if m.get('on_state') is not None:
            for k in m.get('on_state'):
                temp_model = DescribePolicyGovernanceInClusterResponseBodyOnState()
                self.on_state.append(temp_model.from_map(k))
        if m.get('totalViolations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyTotalViolations()
            self.total_violations = temp_model.from_map(m['totalViolations'])
        if m.get('violations') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBodyViolations()
            self.violations = temp_model.from_map(m['violations'])
        return self


class DescribePolicyGovernanceInClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyGovernanceInClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyGovernanceInClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribePolicyInstancesRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        policy_name: str = None,
    ):
        self.instance_name = instance_name
        self.policy_name = policy_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        return self


class DescribePolicyInstancesResponseBody(TeaModel):
    def __init__(
        self,
        ali_uid: str = None,
        cluster_id: str = None,
        instance_name: str = None,
        policy_name: str = None,
        policy_category: str = None,
        policy_description: str = None,
        policy_parameters: str = None,
        policy_severity: str = None,
        policy_scope: str = None,
        policy_action: str = None,
    ):
        self.ali_uid = ali_uid
        self.cluster_id = cluster_id
        self.instance_name = instance_name
        self.policy_name = policy_name
        self.policy_category = policy_category
        self.policy_description = policy_description
        self.policy_parameters = policy_parameters
        self.policy_severity = policy_severity
        self.policy_scope = policy_scope
        self.policy_action = policy_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['ali_uid'] = self.ali_uid
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        if self.policy_category is not None:
            result['policy_category'] = self.policy_category
        if self.policy_description is not None:
            result['policy_description'] = self.policy_description
        if self.policy_parameters is not None:
            result['policy_parameters'] = self.policy_parameters
        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity
        if self.policy_scope is not None:
            result['policy_scope'] = self.policy_scope
        if self.policy_action is not None:
            result['policy_action'] = self.policy_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ali_uid') is not None:
            self.ali_uid = m.get('ali_uid')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')
        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')
        if m.get('policy_parameters') is not None:
            self.policy_parameters = m.get('policy_parameters')
        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')
        if m.get('policy_scope') is not None:
            self.policy_scope = m.get('policy_scope')
        if m.get('policy_action') is not None:
            self.policy_action = m.get('policy_action')
        return self


class DescribePolicyInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribePolicyInstancesResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribePolicyInstancesResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribePolicyInstancesStatusResponseBodyPolicyInstances(TeaModel):
    def __init__(
        self,
        policy_category: str = None,
        policy_description: str = None,
        policy_instances_count: int = None,
        policy_name: str = None,
        policy_severity: str = None,
    ):
        self.policy_category = policy_category
        self.policy_description = policy_description
        self.policy_instances_count = policy_instances_count
        self.policy_name = policy_name
        self.policy_severity = policy_severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.policy_category is not None:
            result['policy_category'] = self.policy_category
        if self.policy_description is not None:
            result['policy_description'] = self.policy_description
        if self.policy_instances_count is not None:
            result['policy_instances_count'] = self.policy_instances_count
        if self.policy_name is not None:
            result['policy_name'] = self.policy_name
        if self.policy_severity is not None:
            result['policy_severity'] = self.policy_severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('policy_category') is not None:
            self.policy_category = m.get('policy_category')
        if m.get('policy_description') is not None:
            self.policy_description = m.get('policy_description')
        if m.get('policy_instances_count') is not None:
            self.policy_instances_count = m.get('policy_instances_count')
        if m.get('policy_name') is not None:
            self.policy_name = m.get('policy_name')
        if m.get('policy_severity') is not None:
            self.policy_severity = m.get('policy_severity')
        return self


class DescribePolicyInstancesStatusResponseBody(TeaModel):
    def __init__(
        self,
        instances_severity_count: Dict[str, Any] = None,
        policy_instances: List[DescribePolicyInstancesStatusResponseBodyPolicyInstances] = None,
    ):
        self.instances_severity_count = instances_severity_count
        self.policy_instances = policy_instances

    def validate(self):
        if self.policy_instances:
            for k in self.policy_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances_severity_count is not None:
            result['instances_severity_count'] = self.instances_severity_count
        result['policy_instances'] = []
        if self.policy_instances is not None:
            for k in self.policy_instances:
                result['policy_instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances_severity_count') is not None:
            self.instances_severity_count = m.get('instances_severity_count')
        self.policy_instances = []
        if m.get('policy_instances') is not None:
            for k in m.get('policy_instances'):
                temp_model = DescribePolicyInstancesStatusResponseBodyPolicyInstances()
                self.policy_instances.append(temp_model.from_map(k))
        return self


class DescribePolicyInstancesStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribePolicyInstancesStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribePolicyInstancesStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInfoResponseBodyError(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class DescribeTaskInfoResponseBodyEvents(TeaModel):
    def __init__(
        self,
        action: str = None,
        level: str = None,
        message: str = None,
        reason: str = None,
        source: str = None,
        timestamp: str = None,
    ):
        self.action = action
        self.level = level
        self.message = message
        self.reason = reason
        self.source = source
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.level is not None:
            result['level'] = self.level
        if self.message is not None:
            result['message'] = self.message
        if self.reason is not None:
            result['reason'] = self.reason
        if self.source is not None:
            result['source'] = self.source
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        return self


class DescribeTaskInfoResponseBodyStages(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        message: str = None,
        outputs: Dict[str, Any] = None,
        start_time: str = None,
        state: str = None,
    ):
        self.end_time = end_time
        self.message = message
        self.outputs = outputs
        self.start_time = start_time
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.message is not None:
            result['message'] = self.message
        if self.outputs is not None:
            result['outputs'] = self.outputs
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('outputs') is not None:
            self.outputs = m.get('outputs')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class DescribeTaskInfoResponseBodyTarget(TeaModel):
    def __init__(
        self,
        id: str = None,
        type: str = None,
    ):
        self.id = id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class DescribeTaskInfoResponseBodyTaskResult(TeaModel):
    def __init__(
        self,
        data: str = None,
        status: str = None,
    ):
        self.data = data
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class DescribeTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created: str = None,
        current_stage: str = None,
        error: DescribeTaskInfoResponseBodyError = None,
        events: List[DescribeTaskInfoResponseBodyEvents] = None,
        parameters: Dict[str, Any] = None,
        stages: List[DescribeTaskInfoResponseBodyStages] = None,
        state: str = None,
        target: DescribeTaskInfoResponseBodyTarget = None,
        task_id: str = None,
        task_result: List[DescribeTaskInfoResponseBodyTaskResult] = None,
        task_type: str = None,
        updated: str = None,
    ):
        self.cluster_id = cluster_id
        self.created = created
        self.current_stage = current_stage
        self.error = error
        self.events = events
        self.parameters = parameters
        self.stages = stages
        self.state = state
        self.target = target
        self.task_id = task_id
        self.task_result = task_result
        self.task_type = task_type
        self.updated = updated

    def validate(self):
        if self.error:
            self.error.validate()
        if self.events:
            for k in self.events:
                if k:
                    k.validate()
        if self.stages:
            for k in self.stages:
                if k:
                    k.validate()
        if self.target:
            self.target.validate()
        if self.task_result:
            for k in self.task_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created is not None:
            result['created'] = self.created
        if self.current_stage is not None:
            result['current_stage'] = self.current_stage
        if self.error is not None:
            result['error'] = self.error.to_map()
        result['events'] = []
        if self.events is not None:
            for k in self.events:
                result['events'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['parameters'] = self.parameters
        result['stages'] = []
        if self.stages is not None:
            for k in self.stages:
                result['stages'].append(k.to_map() if k else None)
        if self.state is not None:
            result['state'] = self.state
        if self.target is not None:
            result['target'] = self.target.to_map()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        result['task_result'] = []
        if self.task_result is not None:
            for k in self.task_result:
                result['task_result'].append(k.to_map() if k else None)
        if self.task_type is not None:
            result['task_type'] = self.task_type
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('current_stage') is not None:
            self.current_stage = m.get('current_stage')
        if m.get('error') is not None:
            temp_model = DescribeTaskInfoResponseBodyError()
            self.error = temp_model.from_map(m['error'])
        self.events = []
        if m.get('events') is not None:
            for k in m.get('events'):
                temp_model = DescribeTaskInfoResponseBodyEvents()
                self.events.append(temp_model.from_map(k))
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        self.stages = []
        if m.get('stages') is not None:
            for k in m.get('stages'):
                temp_model = DescribeTaskInfoResponseBodyStages()
                self.stages.append(temp_model.from_map(k))
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('target') is not None:
            temp_model = DescribeTaskInfoResponseBodyTarget()
            self.target = temp_model.from_map(m['target'])
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        self.task_result = []
        if m.get('task_result') is not None:
            for k in m.get('task_result'):
                temp_model = DescribeTaskInfoResponseBodyTaskResult()
                self.task_result.append(temp_model.from_map(k))
        if m.get('task_type') is not None:
            self.task_type = m.get('task_type')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskInfoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTemplateAttributeRequest(TeaModel):
    def __init__(
        self,
        template_type: str = None,
    ):
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class DescribeTemplateAttributeResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        acl: str = None,
        name: str = None,
        template: str = None,
        template_type: str = None,
        description: str = None,
        tags: str = None,
        template_with_hist_id: str = None,
        created: str = None,
        updated: str = None,
    ):
        self.id = id
        self.acl = acl
        self.name = name
        self.template = template
        self.template_type = template_type
        self.description = description
        self.tags = tags
        self.template_with_hist_id = template_with_hist_id
        self.created = created
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.acl is not None:
            result['acl'] = self.acl
        if self.name is not None:
            result['name'] = self.name
        if self.template is not None:
            result['template'] = self.template
        if self.template_type is not None:
            result['template_type'] = self.template_type
        if self.description is not None:
            result['description'] = self.description
        if self.tags is not None:
            result['tags'] = self.tags
        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id
        if self.created is not None:
            result['created'] = self.created
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTemplateAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeTemplateAttributeResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeTemplateAttributeResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        template_type: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['page_num'] = self.page_num
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.template_type is not None:
            result['template_type'] = self.template_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_num') is not None:
            self.page_num = m.get('page_num')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class DescribeTemplatesResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['page_number'] = self.page_number
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class DescribeTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        acl: str = None,
        created: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        tags: str = None,
        template: str = None,
        template_type: str = None,
        template_with_hist_id: str = None,
        updated: str = None,
    ):
        self.acl = acl
        self.created = created
        self.description = description
        self.id = id
        self.name = name
        self.tags = tags
        self.template = template
        self.template_type = template_type
        self.template_with_hist_id = template_with_hist_id
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
        if self.template_with_hist_id is not None:
            result['template_with_hist_id'] = self.template_with_hist_id
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        if m.get('template_with_hist_id') is not None:
            self.template_with_hist_id = m.get('template_with_hist_id')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class DescribeTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        page_info: DescribeTemplatesResponseBodyPageInfo = None,
        templates: List[DescribeTemplatesResponseBodyTemplates] = None,
    ):
        self.page_info = page_info
        self.templates = templates

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_info is not None:
            result['page_info'] = self.page_info.to_map()
        result['templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_info') is not None:
            temp_model = DescribeTemplatesResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m['page_info'])
        self.templates = []
        if m.get('templates') is not None:
            for k in m.get('templates'):
                temp_model = DescribeTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class DescribeTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTemplatesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTriggerRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        type: str = None,
        action: str = None,
    ):
        self.name = name
        self.namespace = namespace
        self.type = type
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class DescribeTriggerResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
        action: str = None,
        token: str = None,
    ):
        self.id = id
        self.name = name
        self.cluster_id = cluster_id
        self.project_id = project_id
        self.type = type
        self.action = action
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class DescribeTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeTriggerResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeTriggerResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeUserPermissionResponseBody(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        role_name: str = None,
        role_type: str = None,
        is_owner: int = None,
        is_ram_role: int = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.role_name = role_name
        self.role_type = role_type
        self.is_owner = is_owner
        self.is_ram_role = is_ram_role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.role_name is not None:
            result['role_name'] = self.role_name
        if self.role_type is not None:
            result['role_type'] = self.role_type
        if self.is_owner is not None:
            result['is_owner'] = self.is_owner
        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')
        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')
        if m.get('is_owner') is not None:
            self.is_owner = m.get('is_owner')
        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')
        return self


class DescribeUserPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[DescribeUserPermissionResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = DescribeUserPermissionResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class DescribeUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        amk_cluster_quota: int = None,
        ask_cluster_quota: int = None,
        cluster_nodepool_quota: int = None,
        cluster_quota: int = None,
        node_quota: int = None,
    ):
        self.amk_cluster_quota = amk_cluster_quota
        self.ask_cluster_quota = ask_cluster_quota
        self.cluster_nodepool_quota = cluster_nodepool_quota
        self.cluster_quota = cluster_quota
        self.node_quota = node_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amk_cluster_quota') is not None:
            self.amk_cluster_quota = m.get('amk_cluster_quota')
        if m.get('ask_cluster_quota') is not None:
            self.ask_cluster_quota = m.get('ask_cluster_quota')
        if m.get('cluster_nodepool_quota') is not None:
            self.cluster_nodepool_quota = m.get('cluster_nodepool_quota')
        if m.get('cluster_quota') is not None:
            self.cluster_quota = m.get('cluster_quota')
        if m.get('node_quota') is not None:
            self.node_quota = m.get('node_quota')
        return self


class DescribeUserQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeUserQuotaResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeUserQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        create_time: str = None,
        job_name: str = None,
    ):
        self.cluster_id = cluster_id
        self.create_time = create_time
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.create_time is not None:
            result['create_time'] = self.create_time
        if self.job_name is not None:
            result['job_name'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('create_time') is not None:
            self.create_time = m.get('create_time')
        if m.get('job_name') is not None:
            self.job_name = m.get('job_name')
        return self


class DescribeWorkflowsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[DescribeWorkflowsResponseBodyJobs] = None,
    ):
        self.jobs = jobs

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = DescribeWorkflowsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        return self


class DescribeWorkflowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWorkflowsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkflowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EdgeClusterAddEdgeMachineRequest(TeaModel):
    def __init__(
        self,
        expired: int = None,
        nodepool_id: str = None,
        options: str = None,
    ):
        self.expired = expired
        self.nodepool_id = nodepool_id
        self.options = options

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired is not None:
            result['expired'] = self.expired
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.options is not None:
            result['options'] = self.options
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('options') is not None:
            self.options = m.get('options')
        return self


class EdgeClusterAddEdgeMachineResponseBody(TeaModel):
    def __init__(
        self,
        edge_machine_id: str = None,
        request_id: str = None,
    ):
        self.edge_machine_id = edge_machine_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.edge_machine_id is not None:
            result['edge_machine_id'] = self.edge_machine_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('edge_machine_id') is not None:
            self.edge_machine_id = m.get('edge_machine_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class EdgeClusterAddEdgeMachineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EdgeClusterAddEdgeMachineResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EdgeClusterAddEdgeMachineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FixNodePoolVulsRequestRolloutPolicy(TeaModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        self.max_parallelism = max_parallelism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')
        return self


class FixNodePoolVulsRequest(TeaModel):
    def __init__(
        self,
        nodes: List[str] = None,
        rollout_policy: FixNodePoolVulsRequestRolloutPolicy = None,
        vul_list: List[str] = None,
    ):
        self.nodes = nodes
        self.rollout_policy = rollout_policy
        self.vul_list = vul_list

    def validate(self):
        if self.rollout_policy:
            self.rollout_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.rollout_policy is not None:
            result['rollout_policy'] = self.rollout_policy.to_map()
        if self.vul_list is not None:
            result['vul_list'] = self.vul_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('rollout_policy') is not None:
            temp_model = FixNodePoolVulsRequestRolloutPolicy()
            self.rollout_policy = temp_model.from_map(m['rollout_policy'])
        if m.get('vul_list') is not None:
            self.vul_list = m.get('vul_list')
        return self


class FixNodePoolVulsResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class FixNodePoolVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FixNodePoolVulsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = FixNodePoolVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetKubernetesTriggerRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        type: str = None,
        action: str = None,
    ):
        self.name = name
        self.namespace = namespace
        self.type = type
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.type is not None:
            result['Type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class GetKubernetesTriggerResponseBody(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        cluster_id: str = None,
        project_id: str = None,
        type: str = None,
        action: str = None,
        token: str = None,
    ):
        self.id = id
        self.name = name
        self.cluster_id = cluster_id
        self.project_id = project_id
        self.type = type
        self.action = action
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.project_id is not None:
            result['project_id'] = self.project_id
        if self.type is not None:
            result['type'] = self.type
        if self.action is not None:
            result['action'] = self.action
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('project_id') is not None:
            self.project_id = m.get('project_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class GetKubernetesTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[GetKubernetesTriggerResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GetKubernetesTriggerResponseBody()
                self.body.append(temp_model.from_map(k))
        return self


class GetUpgradeStatusResponseBodyUpgradeTask(TeaModel):
    def __init__(
        self,
        message: str = None,
        status: str = None,
    ):
        self.message = message
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetUpgradeStatusResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        precheck_report_id: str = None,
        status: str = None,
        upgrade_step: str = None,
        upgrade_task: GetUpgradeStatusResponseBodyUpgradeTask = None,
    ):
        self.error_message = error_message
        self.precheck_report_id = precheck_report_id
        self.status = status
        self.upgrade_step = upgrade_step
        self.upgrade_task = upgrade_task

    def validate(self):
        if self.upgrade_task:
            self.upgrade_task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('precheck_report_id') is not None:
            self.precheck_report_id = m.get('precheck_report_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('upgrade_step') is not None:
            self.upgrade_step = m.get('upgrade_step')
        if m.get('upgrade_task') is not None:
            temp_model = GetUpgradeStatusResponseBodyUpgradeTask()
            self.upgrade_task = temp_model.from_map(m['upgrade_task'])
        return self


class GetUpgradeStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUpgradeStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetUpgradeStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GrantPermissionsRequestBody(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        is_custom: bool = None,
        is_ram_role: bool = None,
        namespace: str = None,
        role_name: str = None,
        role_type: str = None,
    ):
        self.cluster = cluster
        self.is_custom = is_custom
        self.is_ram_role = is_ram_role
        self.namespace = namespace
        self.role_name = role_name
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.is_custom is not None:
            result['is_custom'] = self.is_custom
        if self.is_ram_role is not None:
            result['is_ram_role'] = self.is_ram_role
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.role_name is not None:
            result['role_name'] = self.role_name
        if self.role_type is not None:
            result['role_type'] = self.role_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('is_custom') is not None:
            self.is_custom = m.get('is_custom')
        if m.get('is_ram_role') is not None:
            self.is_ram_role = m.get('is_ram_role')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('role_name') is not None:
            self.role_name = m.get('role_name')
        if m.get('role_type') is not None:
            self.role_type = m.get('role_type')
        return self


class GrantPermissionsRequest(TeaModel):
    def __init__(
        self,
        body: List[GrantPermissionsRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = GrantPermissionsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class GrantPermissionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class InstallClusterAddonsRequestBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        self.config = config
        self.name = name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class InstallClusterAddonsRequest(TeaModel):
    def __init__(
        self,
        body: List[InstallClusterAddonsRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = InstallClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class InstallClusterAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[Tag] = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tags_shrink: str = None,
    ):
        self.next_token = next_token
        self.region_id = region_id
        self.resource_ids_shrink = resource_ids_shrink
        self.resource_type = resource_type
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids_shrink is not None:
            result['resource_ids'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids_shrink = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['resource_id'] = self.resource_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resource_id') is not None:
            self.resource_id = m.get('resource_id')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')
        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tag_resource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['tag_resource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('tag_resource') is not None:
            for k in m.get('tag_resource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        self.next_token = next_token
        self.request_id = request_id
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['next_token'] = self.next_token
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.tag_resources is not None:
            result['tag_resources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_token') is not None:
            self.next_token = m.get('next_token')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('tag_resources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['tag_resources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MigrateClusterRequest(TeaModel):
    def __init__(
        self,
        oss_bucket_endpoint: str = None,
        oss_bucket_name: str = None,
    ):
        self.oss_bucket_endpoint = oss_bucket_endpoint
        self.oss_bucket_name = oss_bucket_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_bucket_endpoint is not None:
            result['oss_bucket_endpoint'] = self.oss_bucket_endpoint
        if self.oss_bucket_name is not None:
            result['oss_bucket_name'] = self.oss_bucket_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('oss_bucket_endpoint') is not None:
            self.oss_bucket_endpoint = m.get('oss_bucket_endpoint')
        if m.get('oss_bucket_name') is not None:
            self.oss_bucket_name = m.get('oss_bucket_name')
        return self


class MigrateClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class MigrateClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MigrateClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = MigrateClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(
        self,
        api_server_eip: bool = None,
        api_server_eip_id: str = None,
        deletion_protection: bool = None,
        enable_rrsa: bool = None,
        ingress_domain_rebinding: str = None,
        ingress_loadbalancer_id: str = None,
        instance_deletion_protection: bool = None,
        maintenance_window: MaintenanceWindow = None,
        resource_group_id: str = None,
    ):
        self.api_server_eip = api_server_eip
        self.api_server_eip_id = api_server_eip_id
        self.deletion_protection = deletion_protection
        self.enable_rrsa = enable_rrsa
        self.ingress_domain_rebinding = ingress_domain_rebinding
        self.ingress_loadbalancer_id = ingress_loadbalancer_id
        self.instance_deletion_protection = instance_deletion_protection
        self.maintenance_window = maintenance_window
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_server_eip is not None:
            result['api_server_eip'] = self.api_server_eip
        if self.api_server_eip_id is not None:
            result['api_server_eip_id'] = self.api_server_eip_id
        if self.deletion_protection is not None:
            result['deletion_protection'] = self.deletion_protection
        if self.enable_rrsa is not None:
            result['enable_rrsa'] = self.enable_rrsa
        if self.ingress_domain_rebinding is not None:
            result['ingress_domain_rebinding'] = self.ingress_domain_rebinding
        if self.ingress_loadbalancer_id is not None:
            result['ingress_loadbalancer_id'] = self.ingress_loadbalancer_id
        if self.instance_deletion_protection is not None:
            result['instance_deletion_protection'] = self.instance_deletion_protection
        if self.maintenance_window is not None:
            result['maintenance_window'] = self.maintenance_window.to_map()
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('api_server_eip') is not None:
            self.api_server_eip = m.get('api_server_eip')
        if m.get('api_server_eip_id') is not None:
            self.api_server_eip_id = m.get('api_server_eip_id')
        if m.get('deletion_protection') is not None:
            self.deletion_protection = m.get('deletion_protection')
        if m.get('enable_rrsa') is not None:
            self.enable_rrsa = m.get('enable_rrsa')
        if m.get('ingress_domain_rebinding') is not None:
            self.ingress_domain_rebinding = m.get('ingress_domain_rebinding')
        if m.get('ingress_loadbalancer_id') is not None:
            self.ingress_loadbalancer_id = m.get('ingress_loadbalancer_id')
        if m.get('instance_deletion_protection') is not None:
            self.instance_deletion_protection = m.get('instance_deletion_protection')
        if m.get('maintenance_window') is not None:
            temp_model = MaintenanceWindow()
            self.maintenance_window = temp_model.from_map(m['maintenance_window'])
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        return self


class ModifyClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ModifyClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterAddonRequest(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        self.config = config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        return self


class ModifyClusterAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ModifyClusterConfigurationRequestCustomizeConfigConfigs(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterConfigurationRequestCustomizeConfig(TeaModel):
    def __init__(
        self,
        configs: List[ModifyClusterConfigurationRequestCustomizeConfigConfigs] = None,
        name: str = None,
    ):
        self.configs = configs
        self.name = name

    def validate(self):
        if self.configs:
            for k in self.configs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['configs'] = []
        if self.configs is not None:
            for k in self.configs:
                result['configs'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.configs = []
        if m.get('configs') is not None:
            for k in m.get('configs'):
                temp_model = ModifyClusterConfigurationRequestCustomizeConfigConfigs()
                self.configs.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class ModifyClusterConfigurationRequest(TeaModel):
    def __init__(
        self,
        customize_config: List[ModifyClusterConfigurationRequestCustomizeConfig] = None,
    ):
        self.customize_config = customize_config

    def validate(self):
        if self.customize_config:
            for k in self.customize_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['customize_config'] = []
        if self.customize_config is not None:
            for k in self.customize_config:
                result['customize_config'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customize_config = []
        if m.get('customize_config') is not None:
            for k in m.get('customize_config'):
                temp_model = ModifyClusterConfigurationRequestCustomizeConfig()
                self.customize_config.append(temp_model.from_map(k))
        return self


class ModifyClusterConfigurationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ModifyClusterNodePoolRequestAutoScaling(TeaModel):
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
        self.eip_bandwidth = eip_bandwidth
        self.eip_internet_charge_type = eip_internet_charge_type
        self.enable = enable
        self.is_bond_eip = is_bond_eip
        self.max_instances = max_instances
        self.min_instances = min_instances
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestKubernetesConfig(TeaModel):
    def __init__(
        self,
        cms_enabled: bool = None,
        cpu_policy: str = None,
        labels: List[Tag] = None,
        runtime: str = None,
        runtime_version: str = None,
        taints: List[Taint] = None,
        user_data: str = None,
    ):
        self.cms_enabled = cms_enabled
        self.cpu_policy = cpu_policy
        self.labels = labels
        self.runtime = runtime
        self.runtime_version = runtime_version
        self.taints = taints
        self.user_data = user_data

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cms_enabled') is not None:
            self.cms_enabled = m.get('cms_enabled')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        self.labels = []
        if m.get('labels') is not None:
            for k in m.get('labels'):
                temp_model = Tag()
                self.labels.append(temp_model.from_map(k))
        if m.get('runtime') is not None:
            self.runtime = m.get('runtime')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class ModifyClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        self.auto_upgrade = auto_upgrade
        self.max_unavailable = max_unavailable
        self.surge = surge
        self.surge_percentage = surge_percentage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestManagement(TeaModel):
    def __init__(
        self,
        auto_repair: bool = None,
        enable: bool = None,
        upgrade_config: ModifyClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        self.auto_repair = auto_repair
        self.enable = enable
        self.upgrade_config = upgrade_config

    def validate(self):
        if self.upgrade_config:
            self.upgrade_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_repair is not None:
            result['auto_repair'] = self.auto_repair
        if self.enable is not None:
            result['enable'] = self.enable
        if self.upgrade_config is not None:
            result['upgrade_config'] = self.upgrade_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_repair') is not None:
            self.auto_repair = m.get('auto_repair')
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = ModifyClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class ModifyClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
    ):
        self.name = name
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        self.instance_type = instance_type
        self.price_limit = price_limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestScalingGroup(TeaModel):
    def __init__(
        self,
        auto_renew: bool = None,
        auto_renew_period: int = None,
        compensate_with_on_demand: bool = None,
        data_disks: List[DataDisk] = None,
        desired_size: int = None,
        image_id: str = None,
        instance_charge_type: str = None,
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
        rds_instances: List[str] = None,
        scaling_policy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
        spot_strategy: str = None,
        system_disk_category: str = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        tags: List[Tag] = None,
        vswitch_ids: List[str] = None,
    ):
        self.auto_renew = auto_renew
        self.auto_renew_period = auto_renew_period
        self.compensate_with_on_demand = compensate_with_on_demand
        self.data_disks = data_disks
        self.desired_size = desired_size
        self.image_id = image_id
        self.instance_charge_type = instance_charge_type
        self.instance_types = instance_types
        self.internet_charge_type = internet_charge_type
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        self.key_pair = key_pair
        self.login_password = login_password
        self.multi_az_policy = multi_az_policy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.rds_instances = rds_instances
        self.scaling_policy = scaling_policy
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_category = system_disk_category
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.vswitch_ids = vswitch_ids

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.auto_renew_period is not None:
            result['auto_renew_period'] = self.auto_renew_period
        if self.compensate_with_on_demand is not None:
            result['compensate_with_on_demand'] = self.compensate_with_on_demand
        result['data_disks'] = []
        if self.data_disks is not None:
            for k in self.data_disks:
                result['data_disks'].append(k.to_map() if k else None)
        if self.desired_size is not None:
            result['desired_size'] = self.desired_size
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.instance_charge_type is not None:
            result['instance_charge_type'] = self.instance_charge_type
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
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.spot_instance_pools is not None:
            result['spot_instance_pools'] = self.spot_instance_pools
        if self.spot_instance_remedy is not None:
            result['spot_instance_remedy'] = self.spot_instance_remedy
        result['spot_price_limit'] = []
        if self.spot_price_limit is not None:
            for k in self.spot_price_limit:
                result['spot_price_limit'].append(k.to_map() if k else None)
        if self.spot_strategy is not None:
            result['spot_strategy'] = self.spot_strategy
        if self.system_disk_category is not None:
            result['system_disk_category'] = self.system_disk_category
        if self.system_disk_performance_level is not None:
            result['system_disk_performance_level'] = self.system_disk_performance_level
        if self.system_disk_size is not None:
            result['system_disk_size'] = self.system_disk_size
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
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
            for k in m.get('data_disks'):
                temp_model = DataDisk()
                self.data_disks.append(temp_model.from_map(k))
        if m.get('desired_size') is not None:
            self.desired_size = m.get('desired_size')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('instance_charge_type') is not None:
            self.instance_charge_type = m.get('instance_charge_type')
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
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('spot_instance_pools') is not None:
            self.spot_instance_pools = m.get('spot_instance_pools')
        if m.get('spot_instance_remedy') is not None:
            self.spot_instance_remedy = m.get('spot_instance_remedy')
        self.spot_price_limit = []
        if m.get('spot_price_limit') is not None:
            for k in m.get('spot_price_limit'):
                temp_model = ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
        if m.get('spot_strategy') is not None:
            self.spot_strategy = m.get('spot_strategy')
        if m.get('system_disk_category') is not None:
            self.system_disk_category = m.get('system_disk_category')
        if m.get('system_disk_performance_level') is not None:
            self.system_disk_performance_level = m.get('system_disk_performance_level')
        if m.get('system_disk_size') is not None:
            self.system_disk_size = m.get('system_disk_size')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class ModifyClusterNodePoolRequestTeeConfig(TeaModel):
    def __init__(
        self,
        tee_enable: bool = None,
    ):
        self.tee_enable = tee_enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tee_enable is not None:
            result['tee_enable'] = self.tee_enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tee_enable') is not None:
            self.tee_enable = m.get('tee_enable')
        return self


class ModifyClusterNodePoolRequest(TeaModel):
    def __init__(
        self,
        auto_scaling: ModifyClusterNodePoolRequestAutoScaling = None,
        kubernetes_config: ModifyClusterNodePoolRequestKubernetesConfig = None,
        management: ModifyClusterNodePoolRequestManagement = None,
        nodepool_info: ModifyClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: ModifyClusterNodePoolRequestScalingGroup = None,
        tee_config: ModifyClusterNodePoolRequestTeeConfig = None,
        update_nodes: bool = None,
    ):
        self.auto_scaling = auto_scaling
        self.kubernetes_config = kubernetes_config
        self.management = management
        self.nodepool_info = nodepool_info
        self.scaling_group = scaling_group
        self.tee_config = tee_config
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_scaling is not None:
            result['auto_scaling'] = self.auto_scaling.to_map()
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
            temp_model = ModifyClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('kubernetes_config') is not None:
            temp_model = ModifyClusterNodePoolRequestKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = ModifyClusterNodePoolRequestManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('nodepool_info') is not None:
            temp_model = ModifyClusterNodePoolRequestNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = ModifyClusterNodePoolRequestScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('tee_config') is not None:
            temp_model = ModifyClusterNodePoolRequestTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
        if m.get('update_nodes') is not None:
            self.update_nodes = m.get('update_nodes')
        return self


class ModifyClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        nodepool_id: str = None,
        task_id: str = None,
    ):
        self.nodepool_id = nodepool_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ModifyClusterNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyClusterNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyClusterTagsRequest(TeaModel):
    def __init__(
        self,
        body: List[Tag] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = Tag()
                self.body.append(temp_model.from_map(k))
        return self


class ModifyClusterTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ModifyNodePoolNodeConfigRequestKubeletConfig(TeaModel):
    def __init__(
        self,
        cpu_manager_policy: str = None,
        event_burst: int = None,
        event_record_qps: int = None,
        eviction_hard: Dict[str, Any] = None,
        eviction_soft: Dict[str, Any] = None,
        eviction_soft_grace_period: Dict[str, Any] = None,
        kube_apiburst: int = None,
        kube_apiqps: int = None,
        kube_reserved: Dict[str, Any] = None,
        registry_burst: int = None,
        registry_pull_qps: int = None,
        serialize_image_pulls: bool = None,
        system_reserved: Dict[str, Any] = None,
    ):
        self.cpu_manager_policy = cpu_manager_policy
        self.event_burst = event_burst
        self.event_record_qps = event_record_qps
        self.eviction_hard = eviction_hard
        self.eviction_soft = eviction_soft
        self.eviction_soft_grace_period = eviction_soft_grace_period
        self.kube_apiburst = kube_apiburst
        self.kube_apiqps = kube_apiqps
        self.kube_reserved = kube_reserved
        self.registry_burst = registry_burst
        self.registry_pull_qps = registry_pull_qps
        self.serialize_image_pulls = serialize_image_pulls
        self.system_reserved = system_reserved

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cpu_manager_policy is not None:
            result['cpuManagerPolicy'] = self.cpu_manager_policy
        if self.event_burst is not None:
            result['eventBurst'] = self.event_burst
        if self.event_record_qps is not None:
            result['eventRecordQPS'] = self.event_record_qps
        if self.eviction_hard is not None:
            result['evictionHard'] = self.eviction_hard
        if self.eviction_soft is not None:
            result['evictionSoft'] = self.eviction_soft
        if self.eviction_soft_grace_period is not None:
            result['evictionSoftGracePeriod'] = self.eviction_soft_grace_period
        if self.kube_apiburst is not None:
            result['kubeAPIBurst'] = self.kube_apiburst
        if self.kube_apiqps is not None:
            result['kubeAPIQPS'] = self.kube_apiqps
        if self.kube_reserved is not None:
            result['kubeReserved'] = self.kube_reserved
        if self.registry_burst is not None:
            result['registryBurst'] = self.registry_burst
        if self.registry_pull_qps is not None:
            result['registryPullQPS'] = self.registry_pull_qps
        if self.serialize_image_pulls is not None:
            result['serializeImagePulls'] = self.serialize_image_pulls
        if self.system_reserved is not None:
            result['systemReserved'] = self.system_reserved
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cpuManagerPolicy') is not None:
            self.cpu_manager_policy = m.get('cpuManagerPolicy')
        if m.get('eventBurst') is not None:
            self.event_burst = m.get('eventBurst')
        if m.get('eventRecordQPS') is not None:
            self.event_record_qps = m.get('eventRecordQPS')
        if m.get('evictionHard') is not None:
            self.eviction_hard = m.get('evictionHard')
        if m.get('evictionSoft') is not None:
            self.eviction_soft = m.get('evictionSoft')
        if m.get('evictionSoftGracePeriod') is not None:
            self.eviction_soft_grace_period = m.get('evictionSoftGracePeriod')
        if m.get('kubeAPIBurst') is not None:
            self.kube_apiburst = m.get('kubeAPIBurst')
        if m.get('kubeAPIQPS') is not None:
            self.kube_apiqps = m.get('kubeAPIQPS')
        if m.get('kubeReserved') is not None:
            self.kube_reserved = m.get('kubeReserved')
        if m.get('registryBurst') is not None:
            self.registry_burst = m.get('registryBurst')
        if m.get('registryPullQPS') is not None:
            self.registry_pull_qps = m.get('registryPullQPS')
        if m.get('serializeImagePulls') is not None:
            self.serialize_image_pulls = m.get('serializeImagePulls')
        if m.get('systemReserved') is not None:
            self.system_reserved = m.get('systemReserved')
        return self


class ModifyNodePoolNodeConfigRequestRollingPolicy(TeaModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        self.max_parallelism = max_parallelism

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_parallelism is not None:
            result['max_parallelism'] = self.max_parallelism
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('max_parallelism') is not None:
            self.max_parallelism = m.get('max_parallelism')
        return self


class ModifyNodePoolNodeConfigRequest(TeaModel):
    def __init__(
        self,
        kubelet_config: ModifyNodePoolNodeConfigRequestKubeletConfig = None,
        rolling_policy: ModifyNodePoolNodeConfigRequestRollingPolicy = None,
    ):
        self.kubelet_config = kubelet_config
        self.rolling_policy = rolling_policy

    def validate(self):
        if self.kubelet_config:
            self.kubelet_config.validate()
        if self.rolling_policy:
            self.rolling_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubelet_config is not None:
            result['kubelet_config'] = self.kubelet_config.to_map()
        if self.rolling_policy is not None:
            result['rolling_policy'] = self.rolling_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_config') is not None:
            temp_model = ModifyNodePoolNodeConfigRequestKubeletConfig()
            self.kubelet_config = temp_model.from_map(m['kubelet_config'])
        if m.get('rolling_policy') is not None:
            temp_model = ModifyNodePoolNodeConfigRequestRollingPolicy()
            self.rolling_policy = temp_model.from_map(m['rolling_policy'])
        return self


class ModifyNodePoolNodeConfigResponseBody(TeaModel):
    def __init__(
        self,
        nodepool_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.nodepool_id = nodepool_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ModifyNodePoolNodeConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyNodePoolNodeConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyNodePoolNodeConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyPolicyInstanceRequest(TeaModel):
    def __init__(
        self,
        action: str = None,
        instance_name: str = None,
        namespaces: List[str] = None,
        parameters: Dict[str, Any] = None,
    ):
        self.action = action
        self.instance_name = instance_name
        self.namespaces = namespaces
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.namespaces is not None:
            result['namespaces'] = self.namespaces
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('namespaces') is not None:
            self.namespaces = m.get('namespaces')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ModifyPolicyInstanceResponseBody(TeaModel):
    def __init__(
        self,
        instances: List[str] = None,
    ):
        self.instances = instances

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        return self


class ModifyPolicyInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ModifyPolicyInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ModifyPolicyInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OpenAckServiceRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class OpenAckServiceResponseBody(TeaModel):
    def __init__(
        self,
        order_id: str = None,
        request_id: str = None,
    ):
        self.order_id = order_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.order_id is not None:
            result['order_id'] = self.order_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class OpenAckServiceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OpenAckServiceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OpenAckServiceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PauseClusterUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PauseComponentUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PauseTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RemoveClusterNodesRequest(TeaModel):
    def __init__(
        self,
        drain_node: bool = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        self.drain_node = drain_node
        self.nodes = nodes
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class RemoveClusterNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RemoveWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RepairClusterNodePoolRequest(TeaModel):
    def __init__(
        self,
        nodes: List[str] = None,
    ):
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nodes is not None:
            result['nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        return self


class RepairClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class RepairClusterNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RepairClusterNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RepairClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResumeComponentUpgradeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ResumeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ResumeUpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ScaleClusterRequestTags(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class ScaleClusterRequestTaints(TeaModel):
    def __init__(
        self,
        effect: str = None,
        key: str = None,
        value: str = None,
    ):
        self.effect = effect
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ScaleClusterRequestWorkerDataDisks(TeaModel):
    def __init__(
        self,
        category: str = None,
        encrypted: str = None,
        size: str = None,
    ):
        self.category = category
        self.encrypted = encrypted
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ScaleClusterRequest(TeaModel):
    def __init__(
        self,
        cloud_monitor_flags: bool = None,
        count: int = None,
        cpu_policy: str = None,
        disable_rollback: bool = None,
        key_pair: str = None,
        login_password: str = None,
        tags: List[ScaleClusterRequestTags] = None,
        taints: List[ScaleClusterRequestTaints] = None,
        vswitch_ids: List[str] = None,
        worker_auto_renew: bool = None,
        worker_auto_renew_period: int = None,
        worker_data_disk: bool = None,
        worker_data_disks: List[ScaleClusterRequestWorkerDataDisks] = None,
        worker_instance_charge_type: str = None,
        worker_instance_types: List[str] = None,
        worker_period: int = None,
        worker_period_unit: str = None,
        worker_system_disk_category: str = None,
        worker_system_disk_size: int = None,
    ):
        self.cloud_monitor_flags = cloud_monitor_flags
        self.count = count
        self.cpu_policy = cpu_policy
        self.disable_rollback = disable_rollback
        self.key_pair = key_pair
        self.login_password = login_password
        self.tags = tags
        self.taints = taints
        self.vswitch_ids = vswitch_ids
        self.worker_auto_renew = worker_auto_renew
        self.worker_auto_renew_period = worker_auto_renew_period
        self.worker_data_disk = worker_data_disk
        self.worker_data_disks = worker_data_disks
        self.worker_instance_charge_type = worker_instance_charge_type
        self.worker_instance_types = worker_instance_types
        self.worker_period = worker_period
        self.worker_period_unit = worker_period_unit
        self.worker_system_disk_category = worker_system_disk_category
        self.worker_system_disk_size = worker_system_disk_size

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('disable_rollback') is not None:
            self.disable_rollback = m.get('disable_rollback')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ScaleClusterRequestTags()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = ScaleClusterRequestTaints()
                self.taints.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        if m.get('worker_data_disk') is not None:
            self.worker_data_disk = m.get('worker_data_disk')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = ScaleClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        return self


class ScaleClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleClusterNodePoolRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class ScaleClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleClusterNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleClusterNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleClusterNodePoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScaleOutClusterRequestWorkerDataDisks(TeaModel):
    def __init__(
        self,
        auto_snapshot_policy_id: str = None,
        category: str = None,
        encrypted: str = None,
        size: str = None,
    ):
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.category = category
        self.encrypted = encrypted
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.category is not None:
            result['category'] = self.category
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ScaleOutClusterRequest(TeaModel):
    def __init__(
        self,
        cloud_monitor_flags: bool = None,
        count: int = None,
        cpu_policy: str = None,
        image_id: str = None,
        key_pair: str = None,
        login_password: str = None,
        rds_instances: List[str] = None,
        runtime: Runtime = None,
        tags: List[Tag] = None,
        taints: List[Taint] = None,
        user_data: str = None,
        vswitch_ids: List[str] = None,
        worker_auto_renew: bool = None,
        worker_auto_renew_period: int = None,
        worker_data_disks: List[ScaleOutClusterRequestWorkerDataDisks] = None,
        worker_instance_charge_type: str = None,
        worker_instance_types: List[str] = None,
        worker_period: int = None,
        worker_period_unit: str = None,
        worker_system_disk_category: str = None,
        worker_system_disk_size: int = None,
    ):
        self.cloud_monitor_flags = cloud_monitor_flags
        self.count = count
        self.cpu_policy = cpu_policy
        self.image_id = image_id
        self.key_pair = key_pair
        self.login_password = login_password
        self.rds_instances = rds_instances
        self.runtime = runtime
        self.tags = tags
        self.taints = taints
        self.user_data = user_data
        self.vswitch_ids = vswitch_ids
        self.worker_auto_renew = worker_auto_renew
        self.worker_auto_renew_period = worker_auto_renew_period
        self.worker_data_disks = worker_data_disks
        self.worker_instance_charge_type = worker_instance_charge_type
        self.worker_instance_types = worker_instance_types
        self.worker_period = worker_period
        self.worker_period_unit = worker_period_unit
        self.worker_system_disk_category = worker_system_disk_category
        self.worker_system_disk_size = worker_system_disk_size

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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cloud_monitor_flags is not None:
            result['cloud_monitor_flags'] = self.cloud_monitor_flags
        if self.count is not None:
            result['count'] = self.count
        if self.cpu_policy is not None:
            result['cpu_policy'] = self.cpu_policy
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cloud_monitor_flags') is not None:
            self.cloud_monitor_flags = m.get('cloud_monitor_flags')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cpu_policy') is not None:
            self.cpu_policy = m.get('cpu_policy')
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('key_pair') is not None:
            self.key_pair = m.get('key_pair')
        if m.get('login_password') is not None:
            self.login_password = m.get('login_password')
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('runtime') is not None:
            temp_model = Runtime()
            self.runtime = temp_model.from_map(m['runtime'])
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        self.taints = []
        if m.get('taints') is not None:
            for k in m.get('taints'):
                temp_model = Taint()
                self.taints.append(temp_model.from_map(k))
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        if m.get('worker_auto_renew') is not None:
            self.worker_auto_renew = m.get('worker_auto_renew')
        if m.get('worker_auto_renew_period') is not None:
            self.worker_auto_renew_period = m.get('worker_auto_renew_period')
        self.worker_data_disks = []
        if m.get('worker_data_disks') is not None:
            for k in m.get('worker_data_disks'):
                temp_model = ScaleOutClusterRequestWorkerDataDisks()
                self.worker_data_disks.append(temp_model.from_map(k))
        if m.get('worker_instance_charge_type') is not None:
            self.worker_instance_charge_type = m.get('worker_instance_charge_type')
        if m.get('worker_instance_types') is not None:
            self.worker_instance_types = m.get('worker_instance_types')
        if m.get('worker_period') is not None:
            self.worker_period = m.get('worker_period')
        if m.get('worker_period_unit') is not None:
            self.worker_period_unit = m.get('worker_period_unit')
        if m.get('worker_system_disk_category') is not None:
            self.worker_system_disk_category = m.get('worker_system_disk_category')
        if m.get('worker_system_disk_size') is not None:
            self.worker_system_disk_size = m.get('worker_system_disk_size')
        return self


class ScaleOutClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class ScaleOutClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScaleOutClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ScaleOutClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartWorkflowRequest(TeaModel):
    def __init__(
        self,
        mapping_bam_out_filename: str = None,
        mapping_bam_out_path: str = None,
        mapping_bucket_name: str = None,
        mapping_fastq_first_filename: str = None,
        mapping_fastq_path: str = None,
        mapping_fastq_second_filename: str = None,
        mapping_is_mark_dup: str = None,
        mapping_oss_region: str = None,
        mapping_reference_path: str = None,
        service: str = None,
        wgs_bucket_name: str = None,
        wgs_fastq_first_filename: str = None,
        wgs_fastq_path: str = None,
        wgs_fastq_second_filename: str = None,
        wgs_oss_region: str = None,
        wgs_reference_path: str = None,
        wgs_vcf_out_filename: str = None,
        wgs_vcf_out_path: str = None,
        workflow_type: str = None,
    ):
        self.mapping_bam_out_filename = mapping_bam_out_filename
        self.mapping_bam_out_path = mapping_bam_out_path
        self.mapping_bucket_name = mapping_bucket_name
        self.mapping_fastq_first_filename = mapping_fastq_first_filename
        self.mapping_fastq_path = mapping_fastq_path
        self.mapping_fastq_second_filename = mapping_fastq_second_filename
        self.mapping_is_mark_dup = mapping_is_mark_dup
        self.mapping_oss_region = mapping_oss_region
        self.mapping_reference_path = mapping_reference_path
        self.service = service
        self.wgs_bucket_name = wgs_bucket_name
        self.wgs_fastq_first_filename = wgs_fastq_first_filename
        self.wgs_fastq_path = wgs_fastq_path
        self.wgs_fastq_second_filename = wgs_fastq_second_filename
        self.wgs_oss_region = wgs_oss_region
        self.wgs_reference_path = wgs_reference_path
        self.wgs_vcf_out_filename = wgs_vcf_out_filename
        self.wgs_vcf_out_path = wgs_vcf_out_path
        self.workflow_type = workflow_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mapping_bam_out_filename is not None:
            result['mapping_bam_out_filename'] = self.mapping_bam_out_filename
        if self.mapping_bam_out_path is not None:
            result['mapping_bam_out_path'] = self.mapping_bam_out_path
        if self.mapping_bucket_name is not None:
            result['mapping_bucket_name'] = self.mapping_bucket_name
        if self.mapping_fastq_first_filename is not None:
            result['mapping_fastq_first_filename'] = self.mapping_fastq_first_filename
        if self.mapping_fastq_path is not None:
            result['mapping_fastq_path'] = self.mapping_fastq_path
        if self.mapping_fastq_second_filename is not None:
            result['mapping_fastq_second_filename'] = self.mapping_fastq_second_filename
        if self.mapping_is_mark_dup is not None:
            result['mapping_is_mark_dup'] = self.mapping_is_mark_dup
        if self.mapping_oss_region is not None:
            result['mapping_oss_region'] = self.mapping_oss_region
        if self.mapping_reference_path is not None:
            result['mapping_reference_path'] = self.mapping_reference_path
        if self.service is not None:
            result['service'] = self.service
        if self.wgs_bucket_name is not None:
            result['wgs_bucket_name'] = self.wgs_bucket_name
        if self.wgs_fastq_first_filename is not None:
            result['wgs_fastq_first_filename'] = self.wgs_fastq_first_filename
        if self.wgs_fastq_path is not None:
            result['wgs_fastq_path'] = self.wgs_fastq_path
        if self.wgs_fastq_second_filename is not None:
            result['wgs_fastq_second_filename'] = self.wgs_fastq_second_filename
        if self.wgs_oss_region is not None:
            result['wgs_oss_region'] = self.wgs_oss_region
        if self.wgs_reference_path is not None:
            result['wgs_reference_path'] = self.wgs_reference_path
        if self.wgs_vcf_out_filename is not None:
            result['wgs_vcf_out_filename'] = self.wgs_vcf_out_filename
        if self.wgs_vcf_out_path is not None:
            result['wgs_vcf_out_path'] = self.wgs_vcf_out_path
        if self.workflow_type is not None:
            result['workflow_type'] = self.workflow_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mapping_bam_out_filename') is not None:
            self.mapping_bam_out_filename = m.get('mapping_bam_out_filename')
        if m.get('mapping_bam_out_path') is not None:
            self.mapping_bam_out_path = m.get('mapping_bam_out_path')
        if m.get('mapping_bucket_name') is not None:
            self.mapping_bucket_name = m.get('mapping_bucket_name')
        if m.get('mapping_fastq_first_filename') is not None:
            self.mapping_fastq_first_filename = m.get('mapping_fastq_first_filename')
        if m.get('mapping_fastq_path') is not None:
            self.mapping_fastq_path = m.get('mapping_fastq_path')
        if m.get('mapping_fastq_second_filename') is not None:
            self.mapping_fastq_second_filename = m.get('mapping_fastq_second_filename')
        if m.get('mapping_is_mark_dup') is not None:
            self.mapping_is_mark_dup = m.get('mapping_is_mark_dup')
        if m.get('mapping_oss_region') is not None:
            self.mapping_oss_region = m.get('mapping_oss_region')
        if m.get('mapping_reference_path') is not None:
            self.mapping_reference_path = m.get('mapping_reference_path')
        if m.get('service') is not None:
            self.service = m.get('service')
        if m.get('wgs_bucket_name') is not None:
            self.wgs_bucket_name = m.get('wgs_bucket_name')
        if m.get('wgs_fastq_first_filename') is not None:
            self.wgs_fastq_first_filename = m.get('wgs_fastq_first_filename')
        if m.get('wgs_fastq_path') is not None:
            self.wgs_fastq_path = m.get('wgs_fastq_path')
        if m.get('wgs_fastq_second_filename') is not None:
            self.wgs_fastq_second_filename = m.get('wgs_fastq_second_filename')
        if m.get('wgs_oss_region') is not None:
            self.wgs_oss_region = m.get('wgs_oss_region')
        if m.get('wgs_reference_path') is not None:
            self.wgs_reference_path = m.get('wgs_reference_path')
        if m.get('wgs_vcf_out_filename') is not None:
            self.wgs_vcf_out_filename = m.get('wgs_vcf_out_filename')
        if m.get('wgs_vcf_out_path') is not None:
            self.wgs_vcf_out_path = m.get('wgs_vcf_out_path')
        if m.get('workflow_type') is not None:
            self.workflow_type = m.get('workflow_type')
        return self


class StartWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        job_name: str = None,
    ):
        self.job_name = job_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_name is not None:
            result['JobName'] = self.job_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')
        return self


class StartWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = StartWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tags: List[Tag] = None,
    ):
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = Tag()
                self.tags.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnInstallClusterAddonsRequestAddons(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UnInstallClusterAddonsRequest(TeaModel):
    def __init__(
        self,
        addons: List[UnInstallClusterAddonsRequestAddons] = None,
    ):
        self.addons = addons

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['addons'] = []
        if self.addons is not None:
            for k in self.addons:
                result['addons'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.addons = []
        if m.get('addons') is not None:
            for k in m.get('addons'):
                temp_model = UnInstallClusterAddonsRequestAddons()
                self.addons.append(temp_model.from_map(k))
        return self


class UnInstallClusterAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
        tag_keys: List[str] = None,
    ):
        self.all = all
        self.region_id = region_id
        self.resource_ids = resource_ids
        self.resource_type = resource_type
        self.tag_keys = tag_keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['all'] = self.all
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.resource_ids is not None:
            result['resource_ids'] = self.resource_ids
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tag_keys is not None:
            result['tag_keys'] = self.tag_keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tag_keys') is not None:
            self.tag_keys = m.get('tag_keys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateContactGroupForAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateK8sClusterUserConfigExpireRequest(TeaModel):
    def __init__(
        self,
        expire_hour: int = None,
        user: str = None,
    ):
        self.expire_hour = expire_hour
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_hour is not None:
            result['expire_hour'] = self.expire_hour
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire_hour') is not None:
            self.expire_hour = m.get('expire_hour')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class UpdateK8sClusterUserConfigExpireResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        tags: str = None,
        template: str = None,
        template_type: str = None,
    ):
        self.description = description
        self.name = name
        self.tags = tags
        self.template = template
        self.template_type = template_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('tags') is not None:
            self.tags = m.get('tags')
        if m.get('template') is not None:
            self.template = m.get('template')
        if m.get('template_type') is not None:
            self.template_type = m.get('template_type')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpgradeClusterRequest(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        next_version: str = None,
        version: str = None,
    ):
        self.component_name = component_name
        self.next_version = next_version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpgradeClusterAddonsRequestBody(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        config: str = None,
        next_version: str = None,
        version: str = None,
    ):
        self.component_name = component_name
        self.config = config
        self.next_version = next_version
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_name is not None:
            result['component_name'] = self.component_name
        if self.config is not None:
            result['config'] = self.config
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterAddonsRequest(TeaModel):
    def __init__(
        self,
        body: List[UpgradeClusterAddonsRequestBody] = None,
    ):
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = UpgradeClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k))
        return self


class UpgradeClusterAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


