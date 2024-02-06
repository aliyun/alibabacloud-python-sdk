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
        version: str = None,
    ):
        self.config = config
        self.disabled = disabled
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
        if self.disabled is not None:
            result['disabled'] = self.disabled
        if self.name is not None:
            result['name'] = self.name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('disabled') is not None:
            self.disabled = m.get('disabled')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DataDisk(TeaModel):
    def __init__(
        self,
        auto_format: bool = None,
        auto_snapshot_policy_id: str = None,
        bursting_enabled: bool = None,
        category: str = None,
        device: str = None,
        disk_name: str = None,
        encrypted: str = None,
        file_system: str = None,
        kms_key_id: str = None,
        mount_target: str = None,
        performance_level: str = None,
        provisioned_iops: int = None,
        size: int = None,
        snapshot_id: str = None,
    ):
        self.auto_format = auto_format
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        self.bursting_enabled = bursting_enabled
        self.category = category
        self.device = device
        self.disk_name = disk_name
        self.encrypted = encrypted
        self.file_system = file_system
        self.kms_key_id = kms_key_id
        self.mount_target = mount_target
        self.performance_level = performance_level
        self.provisioned_iops = provisioned_iops
        self.size = size
        self.snapshot_id = snapshot_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_format is not None:
            result['auto_format'] = self.auto_format
        if self.auto_snapshot_policy_id is not None:
            result['auto_snapshot_policy_id'] = self.auto_snapshot_policy_id
        if self.bursting_enabled is not None:
            result['bursting_enabled'] = self.bursting_enabled
        if self.category is not None:
            result['category'] = self.category
        if self.device is not None:
            result['device'] = self.device
        if self.disk_name is not None:
            result['disk_name'] = self.disk_name
        if self.encrypted is not None:
            result['encrypted'] = self.encrypted
        if self.file_system is not None:
            result['file_system'] = self.file_system
        if self.kms_key_id is not None:
            result['kms_key_id'] = self.kms_key_id
        if self.mount_target is not None:
            result['mount_target'] = self.mount_target
        if self.performance_level is not None:
            result['performance_level'] = self.performance_level
        if self.provisioned_iops is not None:
            result['provisioned_iops'] = self.provisioned_iops
        if self.size is not None:
            result['size'] = self.size
        if self.snapshot_id is not None:
            result['snapshot_id'] = self.snapshot_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_format') is not None:
            self.auto_format = m.get('auto_format')
        if m.get('auto_snapshot_policy_id') is not None:
            self.auto_snapshot_policy_id = m.get('auto_snapshot_policy_id')
        if m.get('bursting_enabled') is not None:
            self.bursting_enabled = m.get('bursting_enabled')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('device') is not None:
            self.device = m.get('device')
        if m.get('disk_name') is not None:
            self.disk_name = m.get('disk_name')
        if m.get('encrypted') is not None:
            self.encrypted = m.get('encrypted')
        if m.get('file_system') is not None:
            self.file_system = m.get('file_system')
        if m.get('kms_key_id') is not None:
            self.kms_key_id = m.get('kms_key_id')
        if m.get('mount_target') is not None:
            self.mount_target = m.get('mount_target')
        if m.get('performance_level') is not None:
            self.performance_level = m.get('performance_level')
        if m.get('provisioned_iops') is not None:
            self.provisioned_iops = m.get('provisioned_iops')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('snapshot_id') is not None:
            self.snapshot_id = m.get('snapshot_id')
        return self


class KubeletConfig(TeaModel):
    def __init__(
        self,
        allowed_unsafe_sysctls: List[str] = None,
        container_log_max_files: int = None,
        container_log_max_size: str = None,
        cpu_manager_policy: str = None,
        event_burst: int = None,
        event_record_qps: int = None,
        eviction_hard: Dict[str, Any] = None,
        eviction_soft: Dict[str, Any] = None,
        eviction_soft_grace_period: Dict[str, Any] = None,
        feature_gates: Dict[str, Any] = None,
        kube_apiburst: int = None,
        kube_apiqps: int = None,
        kube_reserved: Dict[str, Any] = None,
        max_pods: int = None,
        read_only_port: int = None,
        registry_burst: int = None,
        registry_pull_qps: int = None,
        serialize_image_pulls: bool = None,
        system_reserved: Dict[str, Any] = None,
    ):
        self.allowed_unsafe_sysctls = allowed_unsafe_sysctls
        self.container_log_max_files = container_log_max_files
        self.container_log_max_size = container_log_max_size
        self.cpu_manager_policy = cpu_manager_policy
        self.event_burst = event_burst
        self.event_record_qps = event_record_qps
        self.eviction_hard = eviction_hard
        self.eviction_soft = eviction_soft
        self.eviction_soft_grace_period = eviction_soft_grace_period
        self.feature_gates = feature_gates
        self.kube_apiburst = kube_apiburst
        self.kube_apiqps = kube_apiqps
        self.kube_reserved = kube_reserved
        self.max_pods = max_pods
        self.read_only_port = read_only_port
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
        if self.allowed_unsafe_sysctls is not None:
            result['allowedUnsafeSysctls'] = self.allowed_unsafe_sysctls
        if self.container_log_max_files is not None:
            result['containerLogMaxFiles'] = self.container_log_max_files
        if self.container_log_max_size is not None:
            result['containerLogMaxSize'] = self.container_log_max_size
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
        if self.feature_gates is not None:
            result['featureGates'] = self.feature_gates
        if self.kube_apiburst is not None:
            result['kubeAPIBurst'] = self.kube_apiburst
        if self.kube_apiqps is not None:
            result['kubeAPIQPS'] = self.kube_apiqps
        if self.kube_reserved is not None:
            result['kubeReserved'] = self.kube_reserved
        if self.max_pods is not None:
            result['maxPods'] = self.max_pods
        if self.read_only_port is not None:
            result['readOnlyPort'] = self.read_only_port
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
        if m.get('allowedUnsafeSysctls') is not None:
            self.allowed_unsafe_sysctls = m.get('allowedUnsafeSysctls')
        if m.get('containerLogMaxFiles') is not None:
            self.container_log_max_files = m.get('containerLogMaxFiles')
        if m.get('containerLogMaxSize') is not None:
            self.container_log_max_size = m.get('containerLogMaxSize')
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
        if m.get('featureGates') is not None:
            self.feature_gates = m.get('featureGates')
        if m.get('kubeAPIBurst') is not None:
            self.kube_apiburst = m.get('kubeAPIBurst')
        if m.get('kubeAPIQPS') is not None:
            self.kube_apiqps = m.get('kubeAPIQPS')
        if m.get('kubeReserved') is not None:
            self.kube_reserved = m.get('kubeReserved')
        if m.get('maxPods') is not None:
            self.max_pods = m.get('maxPods')
        if m.get('readOnlyPort') is not None:
            self.read_only_port = m.get('readOnlyPort')
        if m.get('registryBurst') is not None:
            self.registry_burst = m.get('registryBurst')
        if m.get('registryPullQPS') is not None:
            self.registry_pull_qps = m.get('registryPullQPS')
        if m.get('serializeImagePulls') is not None:
            self.serialize_image_pulls = m.get('serializeImagePulls')
        if m.get('systemReserved') is not None:
            self.system_reserved = m.get('systemReserved')
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


class NodepoolAutoScaling(TeaModel):
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


class NodepoolInterconnectConfig(TeaModel):
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


class NodepoolKubernetesConfig(TeaModel):
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


class NodepoolManagementAutoRepairPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
    ):
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')
        return self


class NodepoolManagementAutoUpgradePolicy(TeaModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')
        return self


class NodepoolManagementAutoVulFixPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        self.restart_node = restart_node
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class NodepoolManagementUpgradeConfig(TeaModel):
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


class NodepoolManagement(TeaModel):
    def __init__(
        self,
        auto_repair: bool = None,
        auto_repair_policy: NodepoolManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: NodepoolManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: NodepoolManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: NodepoolManagementUpgradeConfig = None,
    ):
        self.auto_repair = auto_repair
        self.auto_repair_policy = auto_repair_policy
        self.auto_upgrade = auto_upgrade
        self.auto_upgrade_policy = auto_upgrade_policy
        self.auto_vul_fix = auto_vul_fix
        self.auto_vul_fix_policy = auto_vul_fix_policy
        self.enable = enable
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = NodepoolManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m['auto_repair_policy'])
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('auto_upgrade_policy') is not None:
            temp_model = NodepoolManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m['auto_upgrade_policy'])
        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')
        if m.get('auto_vul_fix_policy') is not None:
            temp_model = NodepoolManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m['auto_vul_fix_policy'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = NodepoolManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class NodepoolNodeConfig(TeaModel):
    def __init__(
        self,
        kubelet_configuration: KubeletConfig = None,
    ):
        self.kubelet_configuration = kubelet_configuration

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m['kubelet_configuration'])
        return self


class NodepoolNodepoolInfo(TeaModel):
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


class NodepoolScalingGroupPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        self.id = id
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class NodepoolScalingGroupSpotPriceLimit(TeaModel):
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


class NodepoolScalingGroupTags(TeaModel):
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


class NodepoolScalingGroup(TeaModel):
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
        login_as_non_root: bool = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: NodepoolScalingGroupPrivatePoolOptions = None,
        rds_instances: List[str] = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[NodepoolScalingGroupSpotPriceLimit] = None,
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
        tags: List[NodepoolScalingGroupTags] = None,
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
        self.login_as_non_root = login_as_non_root
        self.login_password = login_password
        self.multi_az_policy = multi_az_policy
        self.on_demand_base_capacity = on_demand_base_capacity
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        self.period = period
        self.period_unit = period_unit
        self.platform = platform
        self.private_pool_options = private_pool_options
        self.rds_instances = rds_instances
        self.scaling_policy = scaling_policy
        self.security_group_id = security_group_id
        self.security_group_ids = security_group_ids
        self.spot_instance_pools = spot_instance_pools
        self.spot_instance_remedy = spot_instance_remedy
        self.spot_price_limit = spot_price_limit
        self.spot_strategy = spot_strategy
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        self.system_disk_categories = system_disk_categories
        self.system_disk_category = system_disk_category
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        self.system_disk_encrypted = system_disk_encrypted
        self.system_disk_kms_key_id = system_disk_kms_key_id
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        self.system_disk_size = system_disk_size
        self.tags = tags
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
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
            temp_model = NodepoolScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['private_pool_options'])
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
                temp_model = NodepoolScalingGroupSpotPriceLimit()
                self.spot_price_limit.append(temp_model.from_map(k))
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
            for k in m.get('tags'):
                temp_model = NodepoolScalingGroupTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('vswitch_ids') is not None:
            self.vswitch_ids = m.get('vswitch_ids')
        return self


class NodepoolTeeConfig(TeaModel):
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


class Nodepool(TeaModel):
    def __init__(
        self,
        auto_scaling: NodepoolAutoScaling = None,
        count: int = None,
        interconnect_config: NodepoolInterconnectConfig = None,
        interconnect_mode: str = None,
        kubernetes_config: NodepoolKubernetesConfig = None,
        management: NodepoolManagement = None,
        max_nodes: int = None,
        node_config: NodepoolNodeConfig = None,
        nodepool_info: NodepoolNodepoolInfo = None,
        scaling_group: NodepoolScalingGroup = None,
        tee_config: NodepoolTeeConfig = None,
    ):
        self.auto_scaling = auto_scaling
        self.count = count
        self.interconnect_config = interconnect_config
        self.interconnect_mode = interconnect_mode
        self.kubernetes_config = kubernetes_config
        self.management = management
        self.max_nodes = max_nodes
        self.node_config = node_config
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
        if self.node_config:
            self.node_config.validate()
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
            temp_model = NodepoolAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('interconnect_config') is not None:
            temp_model = NodepoolInterconnectConfig()
            self.interconnect_config = temp_model.from_map(m['interconnect_config'])
        if m.get('interconnect_mode') is not None:
            self.interconnect_mode = m.get('interconnect_mode')
        if m.get('kubernetes_config') is not None:
            temp_model = NodepoolKubernetesConfig()
            self.kubernetes_config = temp_model.from_map(m['kubernetes_config'])
        if m.get('management') is not None:
            temp_model = NodepoolManagement()
            self.management = temp_model.from_map(m['management'])
        if m.get('max_nodes') is not None:
            self.max_nodes = m.get('max_nodes')
        if m.get('node_config') is not None:
            temp_model = NodepoolNodeConfig()
            self.node_config = temp_model.from_map(m['node_config'])
        if m.get('nodepool_info') is not None:
            temp_model = NodepoolNodepoolInfo()
            self.nodepool_info = temp_model.from_map(m['nodepool_info'])
        if m.get('scaling_group') is not None:
            temp_model = NodepoolScalingGroup()
            self.scaling_group = temp_model.from_map(m['scaling_group'])
        if m.get('tee_config') is not None:
            temp_model = NodepoolTeeConfig()
            self.tee_config = temp_model.from_map(m['tee_config'])
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


class StandardComponentsValue(TeaModel):
    def __init__(
        self,
        name: str = None,
        version: str = None,
        description: str = None,
        required: str = None,
        disabled: bool = None,
    ):
        # The name of the component.
        self.name = name
        # The version of the component.
        self.version = version
        # The description of the component.
        self.description = description
        # Indicates whether the component is a required component. Valid values:
        # 
        # *   `true`: The component is required and must be installed when a cluster is created.
        # *   `false`: The component is optional. After a cluster is created, you can go to the `Add-ons` page to install the component.
        self.required = required
        # Indicates whether the automatic installation of the component is disabled. By default, some optional components, such as components for logging and Ingresses, are installed when a cluster is created. You can set this parameter to disable automatic component installation. Valid values:
        # 
        # *   `true`: disables automatic component installation.
        # *   `false`: enables automatic component installation.
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


class QuotasValue(TeaModel):
    def __init__(
        self,
        quota: str = None,
        operation_code: str = None,
        adjustable: bool = None,
        unit: str = None,
    ):
        # The value of the quota. If the quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.quota = quota
        # The quota code.
        self.operation_code = operation_code
        # Indicates whether the quota is adjustable.
        self.adjustable = adjustable
        # The unit.
        self.unit = unit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quota is not None:
            result['quota'] = self.quota
        if self.operation_code is not None:
            result['operation_code'] = self.operation_code
        if self.adjustable is not None:
            result['adjustable'] = self.adjustable
        if self.unit is not None:
            result['unit'] = self.unit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        if m.get('operation_code') is not None:
            self.operation_code = m.get('operation_code')
        if m.get('adjustable') is not None:
            self.adjustable = m.get('adjustable')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
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
        # The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: This policy allows pods with specific resource characteristics on the node to be configured with enhanced CPU affinity and exclusivity.
        # *   `none`: The default CPU affinity is used.
        # 
        # Default value: `none`.
        # 
        # >  This parameter is not supported if you specify the `nodepool_id` parameter.
        self.cpu_policy = cpu_policy
        # Specifies whether to store container data and images on data disks. Valid values:
        # 
        # *   `true`: stores container data and images on data disks.
        # *   `false`: does not store container data or images on data disks.
        # 
        # Default value: `false`.
        # 
        # How a data disk is mounted:
        # 
        # *   If the ECS instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is attached to the ECS instances, the system does not purchase a new data disk.
        # 
        # >  If you choose to store container data and images on data disks and a data disk is already mounted to the ECS instance, the original data on this data disk will be cleared. You can back up the disk to avoid data loss.
        self.format_disk = format_disk
        # The ID of the custom image. If you do not set this parameter, the default system image is used.
        # 
        # > 
        # 
        # *   If you specify a custom image, the custom image is used to deploy the operating systems on the system disks of the nodes.
        # 
        # *   This parameter is not supported after you specify `nodepool_id`.
        self.image_id = image_id
        # The ECS instances to be added.
        self.instances = instances
        # Specifies whether the nodes that you want to add are Edge Node Service (ENS) nodes. Valid values:
        # 
        # *   `true`: The nodes that you want to add are ENS nodes.
        # *   `false`: The nodes that you want to add are not ENS nodes.
        # 
        # Default value: `false`.
        # 
        # >  If the nodes that you want to add are ENS nodes, you must set this parameter to `true`. This allows you to identify these nodes.
        self.is_edge_worker = is_edge_worker
        # Specifies whether to retain the instance name. Valid values:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `true`
        self.keep_instance_name = keep_instance_name
        # The name of the key pair that is used to log on to the ECS instances. You must set key_pair or `login_password`.
        # 
        # >  This parameter is not supported if you specify the `nodepool_id` parameter.
        self.key_pair = key_pair
        # The node pool ID. If you do not set this parameter, the nodes are added to the default node pool.
        self.nodepool_id = nodepool_id
        # The SSH logon password that is used to log on to the ECS instances. You must set login_password or `key_pair`. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. It cannot contain backslashes (\\) or double quotation marks (").
        # 
        # For security considerations, the password is encrypted during data transfer.
        self.password = password
        # A list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The container runtime.
        # 
        # >  This parameter is not supported if you specify the `nodepool_id` parameter.
        self.runtime = runtime
        # The labels that you want to add to nodes. You must add labels based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        # 
        # >  This parameter is not supported if you specify the `nodepool_id` parameter.
        self.tags = tags
        # User-defined data. For more information, see [Generate user data](~~49121~~).
        # 
        # >  This parameter is not supported if you specify the `nodepool_id` parameter.
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
        # The code that indicates the task result.
        self.code = code
        # The ID of the ECS instance.
        self.instance_id = instance_id
        # Indicates whether the ECS instance is successfully added to the ACK cluster.
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
        # The details of the added nodes.
        self.list = list
        # The task ID.
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


class AttachInstancesToNodePoolRequest(TeaModel):
    def __init__(
        self,
        format_disk: bool = None,
        instances: List[str] = None,
        keep_instance_name: bool = None,
        password: str = None,
    ):
        # Specifies whether to store container data and images on data disks. Valid values:
        # 
        # *   `true`: stores container data and images on data disks.
        # *   `false`: does not store container data or images on data disks.
        # 
        # Default value: `false`.
        # 
        # How to mount a data disk:
        # 
        # *   If the ECS instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is attached to the ECS instances, the system does not purchase a new data disk.
        # 
        # > If you choose to store container data and images on a data disk and the data disk is already mounted to the ECS instance, the existing data on the data disk will be cleared. You can back up the disk to avoid data loss.
        self.format_disk = format_disk
        # The IDs of the instances to be added.
        self.instances = instances
        # Specifies whether to retain the instance name. Valid values:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The SSH password that is used to log on to the instance.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.format_disk is not None:
            result['format_disk'] = self.format_disk
        if self.instances is not None:
            result['instances'] = self.instances
        if self.keep_instance_name is not None:
            result['keep_instance_name'] = self.keep_instance_name
        if self.password is not None:
            result['password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('format_disk') is not None:
            self.format_disk = m.get('format_disk')
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('keep_instance_name') is not None:
            self.keep_instance_name = m.get('keep_instance_name')
        if m.get('password') is not None:
            self.password = m.get('password')
        return self


class AttachInstancesToNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
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


class AttachInstancesToNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AttachInstancesToNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = AttachInstancesToNodePoolResponseBody()
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
        pass

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
        pass

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


class CancelOperationPlanResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelOperationPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelOperationPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CancelOperationPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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
        # The operation that you want to perform. Set the value to cancel.
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
        pass

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


class CheckControlPlaneLogEnableResponseBody(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        components: List[str] = None,
        log_project: str = None,
        log_ttl: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the resource belongs.
        self.aliuid = aliuid
        # The control plane components for which log collection is enabled.
        self.components = components
        # The name of the Simple Log Service project that you want to use to store the logs of control plane components.
        # 
        # Default value: k8s-log-$Cluster ID.
        self.log_project = log_project
        # The retention period of the log data stored in the Logstore. Valid values: 1 to 3000. Unit: days.
        # 
        # Default value: 30.
        self.log_ttl = log_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['aliuid'] = self.aliuid
        if self.components is not None:
            result['components'] = self.components
        if self.log_project is not None:
            result['log_project'] = self.log_project
        if self.log_ttl is not None:
            result['log_ttl'] = self.log_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliuid') is not None:
            self.aliuid = m.get('aliuid')
        if m.get('components') is not None:
            self.components = m.get('components')
        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')
        if m.get('log_ttl') is not None:
            self.log_ttl = m.get('log_ttl')
        return self


class CheckControlPlaneLogEnableResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckControlPlaneLogEnableResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = CheckControlPlaneLogEnableResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAutoscalingConfigRequest(TeaModel):
    def __init__(
        self,
        cool_down_duration: str = None,
        daemonset_eviction_for_nodes: bool = None,
        expander: str = None,
        gpu_utilization_threshold: str = None,
        max_graceful_termination_sec: int = None,
        min_replica_count: int = None,
        recycle_node_deletion_enabled: bool = None,
        scale_down_enabled: bool = None,
        scale_up_from_zero: bool = None,
        scan_interval: str = None,
        skip_nodes_with_local_storage: bool = None,
        skip_nodes_with_system_pods: bool = None,
        unneeded_duration: str = None,
        utilization_threshold: str = None,
    ):
        # The waiting time before the auto scaling feature performs a scale-in activity. Only if the resource usage on a node remains below the scale-in threshold within the waiting time, the node is removed after the waiting time ends. Unit: minutes.
        self.cool_down_duration = cool_down_duration
        # Specifies whether to evict DaemonSet pods during scale-in activities. Valid values:
        # 
        # *   `true`: evicts DaemonSet pods.
        # *   `false`: does not evict DaemonSet pods.
        self.daemonset_eviction_for_nodes = daemonset_eviction_for_nodes
        # The node pool scale-out policy. Valid values:
        # 
        # *   `least-waste`: the default policy. If multiple node pools meet the requirement, this policy selects the node pool that will have the least idle resources after the scale-out activity is completed.
        # *   `random`: the random policy. If multiple node pools meet the requirement, this policy selects a random node pool for the scale-out activity.
        # *   `priority`: the priority-based policy If multiple node pools meet the requirement, this policy selects the node pool with the highest priority for the scale-out activity. The priority setting is stored in the ConfigMap named `cluster-autoscaler-priority-expander` in the kube-system namespace. When a scale-out activity is triggered, the policy obtains the node pool priorities from the ConfigMap based on the node pool IDs and then selects the node pool with the highest priority for the scale-out activity.
        self.expander = expander
        # The scale-in threshold of GPU utilization. This threshold specifies the ratio of the GPU resources that are requested by pods to the total GPU resources on the node.
        self.gpu_utilization_threshold = gpu_utilization_threshold
        # The maximum amount of time that the cluster autoscaler waits for pods on the nodes to terminate during scale-in activities. Unit: seconds.
        self.max_graceful_termination_sec = max_graceful_termination_sec
        # The minimum number of pods that must be guaranteed during scale-in activities.
        self.min_replica_count = min_replica_count
        # Specifies whether to delete the corresponding Kubernetes node objects after nodes are removed in swift mode.
        self.recycle_node_deletion_enabled = recycle_node_deletion_enabled
        # Specifies whether to allow node scale-in activities. Valid values:
        # 
        # *   `true`: allows node scale-in activities.
        # *   `false`: does not allow node scale-in activities.
        self.scale_down_enabled = scale_down_enabled
        # Specifies whether the cluster autoscaler performs scale-out activities when the number of ready nodes in the cluster is zero.
        self.scale_up_from_zero = scale_up_from_zero
        # The interval at which the cluster is scanned and evaluated for scaling. Unit: seconds.
        self.scan_interval = scan_interval
        # Specifies whether to allow the cluster autoscaler to scale in nodes that host pods mounted with local storage, such as EmptyDir volumes or HostPath volumes. Valid values:
        # 
        # *   `true`: does not allow the cluster autoscaler to scale in these nodes.
        # *   `false`: allows the cluster autoscaler to scale in these nodes.
        self.skip_nodes_with_local_storage = skip_nodes_with_local_storage
        # Specifies whether to allow the cluster autoscaler to scale in nodes that host pods in the kube-system namespace, excluding DaemonSet pods and mirror pods. Valid values:
        # 
        # *   `true`: does not allow the cluster autoscaler to scale in these nodes.
        # *   `false`: allows the cluster autoscaler to scale in these nodes.
        self.skip_nodes_with_system_pods = skip_nodes_with_system_pods
        # The cooldown period. Newly added nodes can be removed in scale-in activities only after the cooldown period ends. Unit: minutes.
        self.unneeded_duration = unneeded_duration
        # The scale-in threshold. This threshold specifies the ratio of the resources that are requested by pods to the total resources on the node.
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
        if self.daemonset_eviction_for_nodes is not None:
            result['daemonset_eviction_for_nodes'] = self.daemonset_eviction_for_nodes
        if self.expander is not None:
            result['expander'] = self.expander
        if self.gpu_utilization_threshold is not None:
            result['gpu_utilization_threshold'] = self.gpu_utilization_threshold
        if self.max_graceful_termination_sec is not None:
            result['max_graceful_termination_sec'] = self.max_graceful_termination_sec
        if self.min_replica_count is not None:
            result['min_replica_count'] = self.min_replica_count
        if self.recycle_node_deletion_enabled is not None:
            result['recycle_node_deletion_enabled'] = self.recycle_node_deletion_enabled
        if self.scale_down_enabled is not None:
            result['scale_down_enabled'] = self.scale_down_enabled
        if self.scale_up_from_zero is not None:
            result['scale_up_from_zero'] = self.scale_up_from_zero
        if self.scan_interval is not None:
            result['scan_interval'] = self.scan_interval
        if self.skip_nodes_with_local_storage is not None:
            result['skip_nodes_with_local_storage'] = self.skip_nodes_with_local_storage
        if self.skip_nodes_with_system_pods is not None:
            result['skip_nodes_with_system_pods'] = self.skip_nodes_with_system_pods
        if self.unneeded_duration is not None:
            result['unneeded_duration'] = self.unneeded_duration
        if self.utilization_threshold is not None:
            result['utilization_threshold'] = self.utilization_threshold
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cool_down_duration') is not None:
            self.cool_down_duration = m.get('cool_down_duration')
        if m.get('daemonset_eviction_for_nodes') is not None:
            self.daemonset_eviction_for_nodes = m.get('daemonset_eviction_for_nodes')
        if m.get('expander') is not None:
            self.expander = m.get('expander')
        if m.get('gpu_utilization_threshold') is not None:
            self.gpu_utilization_threshold = m.get('gpu_utilization_threshold')
        if m.get('max_graceful_termination_sec') is not None:
            self.max_graceful_termination_sec = m.get('max_graceful_termination_sec')
        if m.get('min_replica_count') is not None:
            self.min_replica_count = m.get('min_replica_count')
        if m.get('recycle_node_deletion_enabled') is not None:
            self.recycle_node_deletion_enabled = m.get('recycle_node_deletion_enabled')
        if m.get('scale_down_enabled') is not None:
            self.scale_down_enabled = m.get('scale_down_enabled')
        if m.get('scale_up_from_zero') is not None:
            self.scale_up_from_zero = m.get('scale_up_from_zero')
        if m.get('scan_interval') is not None:
            self.scan_interval = m.get('scan_interval')
        if m.get('skip_nodes_with_local_storage') is not None:
            self.skip_nodes_with_local_storage = m.get('skip_nodes_with_local_storage')
        if m.get('skip_nodes_with_system_pods') is not None:
            self.skip_nodes_with_system_pods = m.get('skip_nodes_with_system_pods')
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
        pass

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
        # The data disk type.
        self.category = category
        # Specifies whether to encrypt a data disk. Valid values:
        # 
        # *   `true`: encrypts a data disk.
        # *   `false`: does not encrypt a data disk.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # The performance level (PL) of a data disk. This parameter takes effect only on ESSDs. You can specify a higher PL if you increase the size of a data disk. For more information, see [ESSDs](~~122389~~).
        self.performance_level = performance_level
        # The size of the data disk. Valid values: 40 to 32767.
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
        access_control_list: List[str] = None,
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
        ip_stack: str = None,
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
        nodepools: List[Nodepool] = None,
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
        # The network access control list (ACL) of the SLB instance associated with the API server if the cluster is a registered cluster.
        self.access_control_list = access_control_list
        # The components that you want to install in the cluster. When you create a cluster, you can set the `addons` parameter to install specific components.
        # 
        # **Network plug-in**: required. The Flannel and Terway plug-ins are supported. Select one of the plug-ins for the cluster.
        # 
        # *   Specify the Flannel plug-in in the following format: \[{"name":"flannel","config":""}].
        # *   Specify the Terway plug-in in the following format: \[{"name": "terway-eniip","config": ""}].
        # 
        # **Volume plug-in**: required. The `CSI` and `FlexVolume` volume plug-ins are supported.
        # 
        # *   Specify the `CSI` plug-in in the following format: \[{"name":"csi-plugin","config": ""},{"name": "csi-provisioner","config": ""}].
        # *   Specify the `FlexVolume` plug-in in the following format: \[{"name": "flexvolume","config": ""}].
        # 
        # **Simple Log Service component**: optional. We recommend that you enable Simple Log Service. If Simple Log Service is disabled, you cannot use the cluster auditing feature.
        # 
        # *   Use an existing `Simple Log Service project`: \[{"name": "logtail-ds","config": "{"IngressDashboardEnabled":"true","sls_project_name":"your_sls_project_name"}"}].
        # *   To create a `Simple Log Service project`, specify the component in the following format: \[{"name": "logtail-ds","config": "{"IngressDashboardEnabled":"true"}"}].
        # 
        # **Ingress controller**: optional. By default, the `nginx-ingress-controller` component is installed in ACK dedicated clusters.
        # 
        # *   To install nginx-ingress-controller and enable Internet access, specify the Ingress controller in the following format: \[{"name":"nginx-ingress-controller","config":"{"IngressSlbNetworkType":"internet"}"}].
        # *   If you do not want to install nginx-ingress-controller, specify the component in the following format: \[{"name": "nginx-ingress-controller","config": "","disabled": true}].
        # 
        # **Event center**: optional. By default, the event center feature is enabled.
        # 
        # You can use Kubernetes event centers to store and query events, and configure alert rules. You can use the Logstores that are associated with Kubernetes event centers for free within 90 days. For more information, see [Create and use an event center](~~150476~~).
        # 
        # Enable the ack-node-problem-detector component in the following format: \[{"name":"ack-node-problem-detector","config":"{"sls_project_name":"your_sls_project_name"}"}].
        self.addons = addons
        # Service accounts provide identities for pods when pods communicate with the `API server` of the cluster. `api-audiences` are used by the `API server` to check whether the `tokens` of requests are legitimate.`` Separate multiple `audiences` with commas (,).
        # 
        # For more information about `ServiceAccount`, see [Enable service account token volume projection](~~160384~~).
        self.api_audiences = api_audiences
        # The billing method of the cluster.
        self.charge_type = charge_type
        # Specifies whether to enable Center for Internet Security (CIS) reinforcement. For more information, see [CIS reinforcement](~~223744~~).
        # 
        # Valid values:
        # 
        # *   `true`: enables CIS reinforcement.
        # *   `false`: disables CIS reinforcement.
        # 
        # Default value: `false`.
        self.cis_enabled = cis_enabled
        # Specifies whether to install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent.
        # *   `false`: does not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The domain name of the cluster.
        # 
        # The domain name can contain one or more parts that are separated by periods (.). Each part cannot exceed 63 characters in length, and can contain lowercase letters, digits, and hyphens (-). Each part must start and end with a lowercase letter or digit.
        self.cluster_domain = cluster_domain
        # The type of ACK managed cluster. Valid values:
        # 
        # *   `ack.pro.small`: ACK Pro cluster.
        # *   `ack.standard`: ACK Basic cluster.
        # 
        # Default value: `ack.standard`. If you leave this property empty, an ACK Basic cluster.is created.
        # 
        # For more information, see [Overview of ACK Pro clusters](~~173290~~).
        self.cluster_spec = cluster_spec
        # The cluster type. Valid value: ManagedKubernetes. 
        # You can create ACK managed clusters, ACK Serverless clusters, and ACK Edge clusters.
        self.cluster_type = cluster_type
        # The CIDR block of pods. You can specify 10.0.0.0/8, 172.16-31.0.0/12-16, 192.168.0.0/16, or their subnets as the CIDR block of pods. The CIDR block of pods cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after the cluster is created.
        # 
        # For more information about subnetting for ACK clusters, see [Plan CIDR blocks for an ACK cluster that is deployed in a VPC](~~86500~~).
        # 
        # >  This parameter is required if the cluster uses the Flannel plug-in.
        self.container_cidr = container_cidr
        # The list of control plane components for which you want to enable log collection.
        # 
        # By default, the logs of kube-apiserver, kube-controller-manager, and kube-scheduler are collected.
        self.controlplane_log_components = controlplane_log_components
        # The Simple Log Service project that is used to store the logs of control plane components. You can use an existing project or create one. If you choose to create a Simple Log Service project, the created project is named in the `k8s-log-{ClusterID}` format.
        self.controlplane_log_project = controlplane_log_project
        # The retention period of control plane logs in days.
        self.controlplane_log_ttl = controlplane_log_ttl
        # The CPU management policy of the nodes in a node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Specifies custom subject alternative names (SANs) for the API server certificate to accept requests from specified IP addresses or domain names. Multiple IP addresses and domain names are separated by commas (,).
        self.custom_san = custom_san
        # Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the ACK console or by calling API operations. Valid values:
        # 
        # *   `true`: enables deletion protection for the cluster. This way, the cluster cannot be deleted in the ACK console or by calling API operations.
        # *   `false`: disables deletion protection for the cluster. This way, the cluster can be deleted in the ACK console or by calling API operations.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # Specifies whether to perform a rollback if the cluster fails to be created. Valid values:
        # 
        # *   `true`: performs a rollback if the system fails to create the cluster.
        # *   `false`: does not perform a rollback if the system fails to create the cluster.
        # 
        # Default value: `true`.
        self.disable_rollback = disable_rollback
        # Specifies whether to enable the RAM Roles for Service Accounts (RRSA) feature.
        self.enable_rrsa = enable_rrsa
        # The ID of a key that is managed by Key Management Service (KMS). The key is used to encrypt data disks. For more information, see [KMS](~~28935~~).
        # 
        # >  This feature supports only ACK Pro clusters.
        self.encryption_provider_key = encryption_provider_key
        # Specifies whether to enable Internet access for the cluster. You can use an elastic IP address (EIP) to expose the API server. This way, you can access the cluster over the Internet.
        # 
        # *   `true`: enables Internet access.
        # *   `false`: disables Internet access. If you set this parameter to false, the API server cannot be accessed over the Internet.
        # 
        # Default value: `false`.
        self.endpoint_public_access = endpoint_public_access
        # Specifies whether to mount a data disk to a node that is created based on an existing ECS instance. Valid values:
        # 
        # *   `true`: stores the data of containers and images on a data disk. Back up the existing data on the data disk first.
        # *   `false`: does not store the data of containers and images on a data disk.
        # 
        # Default value: `false`.
        # 
        # How to mount a data disk:
        # 
        # *   If an ECS instance has data disks mounted and the file system of the last data disk is not initialized, the system automatically formats the data disk to ext4. Then, the system mounts the data disk to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is attached to the ECS instances, the system does not purchase a new data disk.
        self.format_disk = format_disk
        # Specifies a custom image for nodes. By default, the image provided by ACK is used. You can select a custom image to replace the default image. For more information, see [Custom images](~~146647~~).
        self.image_id = image_id
        # The type of OS distribution that you want to use. To specify the node OS, we recommend that you use this parameter. Valid values:
        # 
        # *   CentOS
        # *   AliyunLinux
        # *   AliyunLinux Qboot
        # *   AliyunLinuxUEFI
        # *   AliyunLinux3
        # *   Windows
        # *   WindowsCore
        # *   AliyunLinux3Arm64
        # *   ContainerOS
        # 
        # Default value: `CentOS`.
        self.image_type = image_type
        # The list of existing ECS instances that are specified as worker nodes for the cluster.
        # 
        # >  This parameter is required when you create worker nodes on existing ECS instances.
        self.instances = instances
        # The cluster IP stack.
        self.ip_stack = ip_stack
        # Specifies whether to create an advanced security group. This parameter takes effect only if `security_group_id` is left empty.
        # 
        # >  To use a basic security group, make sure that the sum of the number of nodes in the cluster and the number of pods that use Terway does not exceed 2,000. Therefore, if the cluster uses Terway, we recommend that you use an advanced security group.
        # 
        # *   `true`: creates an advanced security group.
        # *   `false`: does not create an advanced security group.
        # 
        # Default value: `true`.
        self.is_enterprise_security_group = is_enterprise_security_group
        # Specifies whether to retain the names of existing ECS instances that are used in the cluster. Valid values:
        # 
        # *   `true`: retains the names.
        # *   `false`: does not retain the names. The new names are assigned by the system.
        # 
        # Default value: `true`.
        self.keep_instance_name = keep_instance_name
        # The name of the key pair. You must set this parameter or the `login_password` parameter.
        self.key_pair = key_pair
        # The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used.
        # 
        # You can create clusters of the latest two Kubernetes versions in the ACK console. You can create clusters of earlier Kubernetes versions by calling API operations. For more information about the Kubernetes versions supported by ACK, see [Release notes on Kubernetes versions](~~185269~~).
        self.kubernetes_version = kubernetes_version
        # The specification of the Server Load Balancer (SLB) instance. Valid values:
        # 
        # *   slb.s1.small
        # *   slb.s2.small
        # *   slb.s2.medium
        # *   slb.s3.small
        # *   slb.s3.medium
        # *   slb.s3.large
        # 
        # Default value: `slb.s2.small`.
        self.load_balancer_spec = load_balancer_spec
        # Specifies whether to enable Simple Log Service for the cluster. Set the value to `SLS`. This parameter takes effect only for ACK Serverless clusters.
        self.logging_type = logging_type
        # The password for SSH logon. You must set this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # Specifies whether to enable auto-renewal for master nodes. This parameter takes effect only if `master_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.master_auto_renew = master_auto_renew
        # The auto-renewal period for master nodes after the subscriptions of master nodes expire. This parameter takes effect and is required only if the subscription billing method is selected for master nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.master_auto_renew_period = master_auto_renew_period
        # The number of master nodes. Valid values: `3` and `5`.
        # 
        # Default value: `3`.
        self.master_count = master_count
        # The billing method of master nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.master_instance_charge_type = master_instance_charge_type
        # The Elastic Compute Service (ECS) instance types of master nodes. For more information, see [Overview of instance families](~~25378~~).
        self.master_instance_types = master_instance_types
        # The subscription duration of master nodes. This parameter takes effect and is required only if `master_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.master_period = master_period
        # The billing cycle of master nodes. This parameter is required if master_instance_charge_type is set to `PrePaid`.
        # 
        # Set the value to `Month`. Master nodes are billed only on a monthly basis.
        self.master_period_unit = master_period_unit
        # The type of system disk that you want to use for master nodes. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: ESSD.
        # 
        # Default value: `cloud_ssd`. The default value may vary in different zones.
        self.master_system_disk_category = master_system_disk_category
        # The performance level (PL) of the system disk that you want to use for master nodes. This parameter takes effect only for enhanced SSDs. For more information about the relationship between disk PLs and disk sizes, see [ESSDs](~~122389~~).
        self.master_system_disk_performance_level = master_system_disk_performance_level
        # The size of the system disk that you want to use for master nodes. Valid values: 40 to 500. Unit: GiB.
        # 
        # Default value: `120`.
        self.master_system_disk_size = master_system_disk_size
        # The ID of the automatic snapshot policy that you want to use for the system disks of master nodes.
        self.master_system_disk_snapshot_policy_id = master_system_disk_snapshot_policy_id
        # The IDs of the vSwitches that are specified for master nodes. You can specify up to three vSwitches. We recommend that you specify three vSwitches in different zones to ensure high availability.
        # 
        # The number of vSwitches must be the same as that specified in `master_count` and the same as those specified in `master_vswitch_ids`.
        self.master_vswitch_ids = master_vswitch_ids
        # The cluster name.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.name = name
        # Specifies whether to create a NAT gateway and configure Source Network Address Translation (SNAT) rules when the system creates the ACK Serverless cluster. Valid values:
        # 
        # *   `true`: automatically creates a NAT gateway and configures SNAT rules. This enables Internet access for the VPC in which the cluster is deployed.
        # *   `false`: does not create a NAT gateway or configure SNAT rules. In this case, the cluster in the VPC cannot access the Internet.
        # 
        # Default value: `false`.
        self.nat_gateway = nat_gateway
        # The maximum number of IP addresses that can be assigned to nodes. This number is determined by the node CIDR block. This parameter takes effect only if the cluster uses Flannel as the network plug-in.
        # 
        # Default value: `26`.
        self.node_cidr_mask = node_cidr_mask
        # The name of the custom node.
        # 
        # A custom node name consists of a prefix, an IP substring, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-), and must start and end with a lowercase letter or digit.
        # *   The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the length of the IP address substring is 5, and the suffix is test, the node name will be aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The node port range. Valid values: 30000 to 65535.
        # 
        # Default value: `30000-32767`.
        self.node_port_range = node_port_range
        # The list of node pools.
        self.nodepools = nodepools
        # The number of worker nodes. Valid values: 0 to 100.
        self.num_of_nodes = num_of_nodes
        # The type of OS. Valid values:
        # 
        # *   Windows
        # *   Linux
        # 
        # Default value: `Linux`.
        self.os_type = os_type
        # The subscription duration.
        self.period = period
        # The unit of the subscription duration.
        self.period_unit = period_unit
        # The release version of the operating system. Valid values:
        # 
        # *   CentOS
        # *   AliyunLinux
        # *   QbootAliyunLinux
        # *   Qboot
        # *   Windows
        # *   WindowsCore
        # 
        # Default value: `CentOS`.
        self.platform = platform
        # The list of pod vSwitches. You need to specify at least one pod vSwitch for each node vSwitch and the pod vSwitches must not be the same as the node vSwitches (`vswitch`). We recommend that you specify pod vSwitches whose mask lengths are no greater than 19.
        # 
        # >  The `pod_vswitch_ids` parameter is required if the cluster uses Terway as the network plug-in.
        self.pod_vswitch_ids = pod_vswitch_ids
        # The identifier that indicates whether the cluster is an ACK Edge cluster. To create an ACK Edge cluster, you must set this parameter to `Edge`.
        # 
        # *   `Default`: The cluster is not an ACK Edge cluster.
        # *   `Edge`: The cluster is an ACK Edge cluster.
        self.profile = profile
        # The kube-proxy mode. Valid values:
        # 
        # *   `iptables`: iptables is a mature and stable kube-proxy mode. It uses iptables rules to conduct service discovery and load balancing. The performance of this mode is restricted by the size of the Kubernetes cluster. This mode is suitable for Kubernetes clusters that manage a small number of Services.
        # *   `ipvs`: IPVS is a high-performance kube-proxy mode. It uses Linux Virtual Server (LVS) to conduct service discovery and load balancing. This mode is suitable for clusters that manage a large number of Services. We recommend that you use this mode in scenarios where high-performance load balancing is required.
        # 
        # Default value: `ipvs`.
        self.proxy_mode = proxy_mode
        # The list of ApsaraDB RDS instances. Select the ApsaraDB RDS instances that you want to add to the whitelist. We recommend that you add the CIDR block of pods and CIDR block of nodes to the ApsaraDB RDS instances in the ApsaraDB RDS console. When you set the ApsaraDB RDS instances, you cannot scale out the number of nodes because the instances are not in the Running state.
        self.rds_instances = rds_instances
        # The ID of the region in which you want to deploy the cluster.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs. You can use resource groups to isolate clusters.
        self.resource_group_id = resource_group_id
        # The container runtime. The default container runtime is Docker. containerd and Sandboxed-Container are also supported.
        # 
        # For more information about how to select a proper container runtime, see [Comparison of Docker, containerd, and Sandboxed-Container](~~160313~~).
        self.runtime = runtime
        # The ID of an existing security group. You need to choose between this parameter and the `is_enterprise_security_group` parameter. Cluster nodes are automatically added to the security group.
        self.security_group_id = security_group_id
        # Service accounts provide identities for pods when pods communicate with the `API server` of the cluster. `service-account-issuer` is the issuer of the `serviceaccount token`, which corresponds to the `iss` field in the `token payload`.
        # 
        # For more information about `ServiceAccount`, see [Enable service account token volume projection](~~160384~~).
        self.service_account_issuer = service_account_issuer
        # The CIDR block of Services. Valid values: 10.0.0.0/16-24, 172.16-31.0.0/16-24, and 192.168.0.0/16-24. The CIDR block of Services cannot overlap with the CIDR block of the VPC (10.1.0.0/21) or the CIDR blocks of existing clusters in the VPC. You cannot modify the CIDR block of Services after the cluster is created.
        # 
        # By default, the CIDR block of Services is set to 172.19.0.0/20.
        self.service_cidr = service_cidr
        # The type of service discovery that is implemented in the `ACK Serverless` cluster.
        # 
        # *   `CoreDNS`: a standard service discovery plug-in provided by open source Kubernetes. To use the Domain Name System (DNS) resolution, you must provision pods. By default, two elastic container instances are used. The specification of each instance is 0.25 CPU cores and 512 MiB of memory.
        # *   `PrivateZone`: a DNS resolution service provided by Alibaba Cloud. You must activate Alibaba Cloud DNS PrivateZone before you can use it for service discovery.
        # 
        # By default, this parameter is not specified.
        self.service_discovery_types = service_discovery_types
        # Specifies whether to configure SNAT rules for the VPC where your cluster is deployed. Valid values:
        # 
        # *   `true`: automatically creates a NAT gateway and configures SNAT rules. Set this parameter to `true` if nodes and applications in the cluster need to access the Internet.
        # *   `false`: does not create a NAT gateway or configure SNAT rules. In this case, nodes and applications in the cluster cannot access the Internet.
        # 
        # >  If this feature is disabled when you create the cluster, you can also manually enable this feature after you create the cluster. For more information, see [Manually create a NAT gateway and configure SNAT rules](~~178480~~).
        # 
        # Default value: `true`.
        self.snat_entry = snat_entry
        # Reinforcement based on classified protection. For more information, see [ACK reinforcement based on classified protection](~~196148~~).
        # 
        # Valid values:
        # 
        # *   `true`: enables reinforcement based on classified protection.
        # *   `false`: disables reinforcement based on classified protection.
        # 
        # Default value: `false`.
        self.soc_enabled = soc_enabled
        # Specifies whether to enable SSH logon over the Internet. If this parameter is set to true, you can log on to master nodes in an ACK dedicated cluster over the Internet. This parameter does not take effect in ACK managed clusters.
        # 
        # *   `true`: enables SSH logon over the Internet.
        # *   `false`: disables SSH logon over the Internet.
        # 
        # Default value: `false`.
        self.ssh_flags = ssh_flags
        # The labels that you want to add to nodes. You must add tags based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # The taints of the nodes in the node pool. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, tolerations allow pods to be scheduled to nodes with matching taints. For more information, see [Taints and Tolerations](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # Specifies the timeout period of cluster creation. Unit: minutes.
        # 
        # Default value: `60`.
        self.timeout_mins = timeout_mins
        # The time zone of the cluster.
        self.timezone = timezone
        # The custom certificate authority (CA) certificate used by the cluster.
        self.user_ca = user_ca
        # The user data of nodes.
        self.user_data = user_data
        # The virtual private cloud (VPC) in which you want to deploy the cluster. This parameter is required.
        self.vpcid = vpcid
        # The vSwitches that are specified for nodes in the cluster. This parameter is required when you create a managed Kubernetes cluster that does not contain nodes.
        self.vswitch_ids = vswitch_ids
        # Specifies whether to enable auto-renewal for worker nodes. This parameter takes effect only if `worker_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.worker_auto_renew = worker_auto_renew
        # The auto-renewal period for worker nodes after the subscriptions of worker nodes expire. This parameter takes effect and is required only if the subscription billing method is selected for worker nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        self.worker_auto_renew_period = worker_auto_renew_period
        # The configuration of the data disk that is mounted to worker nodes. The configuration includes disk type and disk size.
        self.worker_data_disks = worker_data_disks
        # The billing method of worker nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: PostPaid.
        self.worker_instance_charge_type = worker_instance_charge_type
        # The instance configurations of worker nodes.
        self.worker_instance_types = worker_instance_types
        # The subscription duration of worker nodes. This parameter takes effect and is required only if `worker_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.worker_period = worker_period
        # The billing cycle of worker nodes. This parameter is required if worker_instance_charge_type is set to `PrePaid`.
        # 
        # Set the value to `Month`. Worker nodes are billed only on a monthly basis.
        self.worker_period_unit = worker_period_unit
        # The category of the system disk that you attach to the worker node. For more information, see [Elastic Block Storage devices](~~63136~~).
        # 
        # Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # 
        # Default value: `cloud_ssd`.
        self.worker_system_disk_category = worker_system_disk_category
        # If the system disk is an ESSD, you can set the PL of the ESSD. For more information, see [ESSDs](~~122389~~).
        # 
        # Valid values:
        # 
        # *   PL0
        # *   PL1
        # *   PL2
        # *   PL3
        self.worker_system_disk_performance_level = worker_system_disk_performance_level
        # The size of the system disk that you want to use for worker nodes. Unit: GiB.
        # 
        # Valid values: 40 to 500.
        # 
        # The value of this parameter must be at least 40 and no less than the image size.
        # 
        # Default value: `120`.
        self.worker_system_disk_size = worker_system_disk_size
        # The ID of the automatic snapshot policy that you want to use for the system disks of worker nodes.
        self.worker_system_disk_snapshot_policy_id = worker_system_disk_snapshot_policy_id
        # The list of vSwitches that are specified for nodes. Each node is allocated a vSwitch.
        # 
        # The `worker_vswitch_ids` parameter is optional but the `vswitch_ids` parameter is required when you create an ACK managed cluster that does not contain nodes.
        self.worker_vswitch_ids = worker_vswitch_ids
        # The ID of the zone in which the cluster is deployed. This parameter takes effect in only ACK Serverless clusters.
        # 
        # When you create an ACK Serverless cluster, you must configure `zone_id` if `vpc_id` and `vswitch_ids` are not configured. This way, the system automatically creates a VPC in the specified zone.
        self.zone_id = zone_id

    def validate(self):
        if self.addons:
            for k in self.addons:
                if k:
                    k.validate()
        if self.nodepools:
            for k in self.nodepools:
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
        if self.access_control_list is not None:
            result['access_control_list'] = self.access_control_list
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
        if self.ip_stack is not None:
            result['ip_stack'] = self.ip_stack
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
        result['nodepools'] = []
        if self.nodepools is not None:
            for k in self.nodepools:
                result['nodepools'].append(k.to_map() if k else None)
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
        if m.get('access_control_list') is not None:
            self.access_control_list = m.get('access_control_list')
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
        if m.get('ip_stack') is not None:
            self.ip_stack = m.get('ip_stack')
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
        self.nodepools = []
        if m.get('nodepools') is not None:
            for k in m.get('nodepools'):
                temp_model = Nodepool()
                self.nodepools.append(temp_model.from_map(k))
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
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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
        # This parameter is deprecated.
        # 
        # The maximum bandwidth of the EIP. Unit: Mbit/s.
        self.eip_bandwidth = eip_bandwidth
        # This parameter is deprecated.
        # 
        # The metering method of the EIP. Valid values:
        # 
        # *   `PayByBandwidth`: pay-by-bandwidth.
        # *   `PayByTraffic`: pay-by-data-transfer.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # 
        # *   `true`: enables auto scaling.
        # *   `false`: disables auto scaling. If you set this parameter to false, other parameters in the `auto_scaling` section do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # This parameter is deprecated.
        # 
        # Specifies whether to associate an elastic IP address (EIP) with the node pool. Valid values:
        # 
        # *   `true`: associates an EIP with the node pool
        # *   `false`: does not associate an EIP with the node pool.
        # 
        # Default value: `false`.
        self.is_bond_eip = is_bond_eip
        # The maximum number of Elastic Compute Service (ECS) instances that can be created in a node pool.
        self.max_instances = max_instances
        # The minimum number of ECS instances that must be kept in a node pool.
        self.min_instances = min_instances
        # The instance types that can be used for the auto scaling of the node pool. Valid values:
        # 
        # *   `cpu`: regular instance.
        # *   `gpu`: GPU-accelerated instance.
        # *   `gpushare`: shared GPU-accelerated instance.
        # *   `spot`: preemptible instance
        # 
        # Default value: `cpu`.
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
        # This parameter is deprecated.
        # 
        # The bandwidth of the enhanced edge node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # This parameter is deprecated.
        # 
        # The ID of the Cloud Connect Network (CCN) instance that is associated with the enhanced edge node pool.
        self.ccn_id = ccn_id
        # This parameter is deprecated.
        # 
        # The region to which the CCN instance that is associated with the enhanced edge node pool belongs.
        self.ccn_region_id = ccn_region_id
        # This parameter is deprecated.
        # 
        # The ID of the Cloud Enterprise Network (CEN) instance that is associated with the enhanced edge node pool.
        self.cen_id = cen_id
        # This parameter is deprecated.
        # 
        # The subscription duration of the enhanced edge node pool. The duration is measured in months.
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
        unschedulable: bool = None,
        user_data: str = None,
    ):
        # Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent on ECS nodes.
        # *   `false`: does not install the CloudMonitor agent on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy of the nodes in a node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The labels that you want to add to the nodes in the cluster.
        self.labels = labels
        # A custom node name consists of a prefix, a node IP address, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter.
        # *   The node IP address in a custom node name is the private IP address of the node.
        # 
        # Set the value in the customized,aliyun,ip,com format. The value consists of four parts that are separated by commas (,). customized and ip are fixed content. aliyun is the prefix and com is the suffix. Example: aliyun.192.168.xxx.xxx.com.
        self.node_name_mode = node_name_mode
        # The container runtime.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The configuration of taints.
        self.taints = taints
        self.unschedulable = unschedulable
        # The user-defined data on nodes.
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
        if m.get('unschedulable') is not None:
            self.unschedulable = m.get('unschedulable')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class CreateClusterNodePoolRequestManagementAutoRepairPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
    ):
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')
        return self


class CreateClusterNodePoolRequestManagementAutoUpgradePolicy(TeaModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')
        return self


class CreateClusterNodePoolRequestManagementAutoVulFixPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        self.restart_node = restart_node
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # Indicates whether auto update is enabled. Valid values:
        # 
        # *   `true`: enables auto upgrade.
        # *   `false`: disables auto update.
        self.auto_upgrade = auto_upgrade
        # The maximum number of nodes that can be in the Unschedulable state. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of nodes that are temporarily added to the node pool during an auto update.
        self.surge = surge
        # The percentage of additional nodes to the nodes in the node pool. You must set this parameter or `surge`.
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
        auto_repair_policy: CreateClusterNodePoolRequestManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: CreateClusterNodePoolRequestManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: CreateClusterNodePoolRequestManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: CreateClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        # Specifies whether to enable auto repair. This parameter takes effect only when you specify `enable=true`. Valid values:
        # 
        # *   `true`: enables auto repair.
        # *   `false`: disables auto repair.
        self.auto_repair = auto_repair
        self.auto_repair_policy = auto_repair_policy
        self.auto_upgrade = auto_upgrade
        self.auto_upgrade_policy = auto_upgrade_policy
        self.auto_vul_fix = auto_vul_fix
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the managed node pool feature. Valid values:
        # 
        # *   `true`: enables the managed node pool feature.
        # *   `false`: disables the managed node pool feature. Other parameters in this section take effect only when you specify enable=true.
        self.enable = enable
        # The configuration of auto update. The configuration takes effect only when you specify `enable=true`.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = CreateClusterNodePoolRequestManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m['auto_repair_policy'])
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('auto_upgrade_policy') is not None:
            temp_model = CreateClusterNodePoolRequestManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m['auto_upgrade_policy'])
        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')
        if m.get('auto_vul_fix_policy') is not None:
            temp_model = CreateClusterNodePoolRequestManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m['auto_vul_fix_policy'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = CreateClusterNodePoolRequestManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class CreateClusterNodePoolRequestNodeConfig(TeaModel):
    def __init__(
        self,
        kubelet_configuration: KubeletConfig = None,
    ):
        self.kubelet_configuration = kubelet_configuration

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m['kubelet_configuration'])
        return self


class CreateClusterNodePoolRequestNodepoolInfo(TeaModel):
    def __init__(
        self,
        name: str = None,
        resource_group_id: str = None,
        type: str = None,
    ):
        # The name of the node pool.
        self.name = name
        # The ID of the resource group to which the node pool belongs.
        self.resource_group_id = resource_group_id
        # The type of node pool. Valid values:
        # 
        # *   `ess`: node pool
        # *   `edge`: edge node pool
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


class CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private node pool.
        self.id = id
        # The type of private node pool. This parameter specifies the type of private pool that you want to use to create instances. A private node pool is generated when an elasticity assurance or a capacity reservation service takes effect. The system selects a private node pool to launch instances. Valid values:
        # 
        # *   `Open`: open private pool. The system selects an open private node pool to launch instances. If no matching open private node pool is available, the resources in the public node pool are used.
        # *   `Target`: specific private pool. The system uses the resources of the specified private node pool to launch instances. If the specified private node pool is unavailable, instances cannot be launched.
        # *   `None`: no private pool is used. The resources of private node pools are not used to launch the instances.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of preemptible instance.
        self.instance_type = instance_type
        # The maximum bid price of a preemptible instance.
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
        # The key of a label.
        self.key = key
        # The value of a label.
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
        cis_enabled: bool = None,
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
        login_as_non_root: bool = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions = None,
        rds_instances: List[str] = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[CreateClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
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
        tags: List[CreateClusterNodePoolRequestScalingGroupTags] = None,
        vswitch_ids: List[str] = None,
    ):
        # Specifies whether to enable auto-renewal for nodes in the node pool. This parameter takes effect only when you set `instance_charge_type` to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.auto_renew = auto_renew
        # The duration of the auto-renewal. This parameter takes effect and is required only when you set instance_charge_type to PrePaid and auto_renew to true. If `PeriodUnit=Month` is configured, the valid values are 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.auto_renew_period = auto_renew_period
        self.cis_enabled = cis_enabled
        # Specifies whether to automatically create pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created due to reasons such as the cost or insufficient inventory. This parameter takes effect when you set `multi_az_policy` to `COST_OPTIMIZED`. Valid values:
        # 
        # *   `true`: automatically creates pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created.
        # *   `false`: does not create pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configuration of the data disks that are mounted to the nodes in the node pool.
        self.data_disks = data_disks
        # The ID of the deployment set to which the ECS instances in the node pool belong.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The ID of a custom image. By default, the image provided by ACK is used.
        self.image_id = image_id
        # The type of OS image. You must set this parameter or `platform`. Valid values:
        # 
        # *   `AliyunLinux`: Alinux2
        # *   `AliyunLinux3`: Alinux3
        # *   `AliyunLinux3Arm64`: Alinux3 ARM
        # *   `AliyunLinuxUEFI`: Alinux2 UEFI
        # *   `CentOS`: CentOS
        # *   `Windows`: Windows
        # *   `WindowsCore`: Windows Core
        # *   `ContainerOS`: ContainerOS
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method.
        # *   `PostPaid`: the pay-as-you-go billing method.
        # 
        # Default value: `PostPaid`.
        self.instance_charge_type = instance_charge_type
        # The instance type of the nodes in the node pool.
        self.instance_types = instance_types
        # The metering method of the public IP address. Valid values:
        # 
        # *   PayByBandwidth: pay-by-bandwidth.
        # *   PayByTraffic: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must set this parameter or the `login_password` parameter.
        # 
        # >  If you want to create a managed node pool, you must set `key_pair`.
        self.key_pair = key_pair
        self.login_as_non_root = login_as_non_root
        # The password for SSH logon. You must set this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The ECS instance scaling policy for a multi-zone scaling group. Valid values:
        # 
        # *   `PRIORITY`: ECS instances are created based on the VSwitchIds.N parameter. If Auto Scaling fails to create ECS instances in the zone of the vSwitch with the highest priority, Auto Scaling attempts to create ECS instances in the zone of the vSwitch with a lower priority.
        # 
        # *   `COST_OPTIMIZED`: ECS instances are created based on the vCPU unit price in ascending order. Preemptible instances are preferably created when preemptible instance types are specified in the scaling configuration. You can set the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when preemptible instances cannot be created due to insufficient resources.
        # 
        #     **\
        # 
        #     **Note** `COST_OPTIMIZED` is valid only when multiple instance types are specified or at least one preemptible instance type is specified.
        # 
        # *   `BALANCE`: ECS instances are evenly distributed across multiple zones specified by the scaling group. If ECS instances become imbalanced among multiple zones due to insufficient inventory, you can call [RebalanceInstances](~~71516~~) of Auto Scaling to balance the instance distribution among zones.
        # 
        # Default value: `PRIORITY`.
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances that must be kept in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferably creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the number specified by `on_demand_base_capacity`. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of the nodes in the node pool. This parameter takes effect and is required only when you set `instance_charge_type` to `PrePaid`. If you set `period_unit` to Month, the valid values of `period` are 1, 2, 3, 6, and 12.
        # 
        # Default value: 1.
        self.period = period
        # The billing cycle of the nodes in the node pool. This parameter is required if you set instance_charge_type to `PrePaid`. A value of Month indicates that the billing cycle is measured in months.
        self.period_unit = period_unit
        # The release version of the operating system. Valid values:
        # 
        # *   `CentOS`
        # *   `AliyunLinux`
        # *   `Windows`
        # *   `WindowsCore`
        # 
        # Default value: `AliyunLinux`.
        self.platform = platform
        # The configuration of the private node pool.
        self.private_pool_options = private_pool_options
        # A list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The scaling mode of the scaling group. Valid values:
        # 
        # *   `release`: the standard mode. ECS instances are created and released based on resource usage.
        # *   `recycle`: the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks.
        # 
        # Default value: `release`.
        self.scaling_policy = scaling_policy
        # Specifies the ID of the security group to which you want to add the node pool. You must set this parameter or `security_group_ids`. We recommend that you set `security_group_ids`.
        self.security_group_id = security_group_id
        # The IDs of security groups to which you want to add the node pool. You must set this parameter or `security_group_id`. We recommend that you set `security_group_ids`. If you set both `security_group_id` and `security_group_ids`, `security_group_ids` is used.
        self.security_group_ids = security_group_ids
        self.soc_enabled = soc_enabled
        # The number of instance types that are available. Auto Scaling creates preemptible instances of multiple instance types that are available at the lowest cost. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to supplement preemptible instances when the number of preemptible instances drops below the specified minimum number. If this parameter is set to true, when the scaling group receives a system message that a preemptible instance is to be reclaimed, the scaling group attempts to create a new instance to replace this instance. Valid values:
        # 
        # *   `true`: enables the supplementation of preemptible instances.
        # *   `false`: disables the supplementation of preemptible instances.
        self.spot_instance_remedy = spot_instance_remedy
        # The instance type of preemptible instance and the maximum bid price.
        self.spot_price_limit = spot_price_limit
        # The bidding policy of preemptible instances. Valid values:
        # 
        # *   `NoSpot`: non-preemptible instance.
        # *   `SpotWithPriceLimit`: specifies the highest bid.
        # *   `SpotAsPriceGo`: automatically submits bids based on the up-to-date market price.
        # 
        # For more information, see [Preemptible instances](~~165053~~).
        self.spot_strategy = spot_strategy
        # Specifies whether to enable the burst feature for system disks. Valid values:
        # 
        # *   true: enables the burst feature.
        # *   false: disables the burst feature.
        # 
        # This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](~~368372~~).
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        self.system_disk_categories = system_disk_categories
        # The type of system disk. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: enhanced SSD.
        # 
        # Default value: `cloud_efficiency`.
        self.system_disk_category = system_disk_category
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        self.system_disk_encrypted = system_disk_encrypted
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for ESSDs.
        # 
        # *   PL0: moderate maximum concurrent I/O performance and low I/O latency
        # *   PL1: moderate maximum concurrent I/O performance and low I/O latency
        # *   PL2: high maximum concurrent I/O performance and low I/O latency
        # *   PL3: ultra-high maximum concurrent I/O performance and ultra-low I/O latency
        self.system_disk_performance_level = system_disk_performance_level
        # The predefined IOPS of a system disk. Valid values: 0 to min{50,000, 1,000 × Capacity - Baseline IOPS}. Baseline IOPS = min{1,800 + 50 × Capacity, 50,000}.
        # 
        # This parameter is supported only when `SystemDiskCategory` is set to `cloud_auto`. For more information, see [ESSD AutoPL disks](~~368372~~).
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of a node. Unit: GiB.
        # 
        # Valid values: 40 to 500.
        self.system_disk_size = system_disk_size
        # The labels that you want to add to the ECS instances.
        # 
        # Each key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://.
        self.tags = tags
        # The vSwitch IDs. Valid values: 1 to 8.
        # 
        # >  To ensure high availability, we recommend that you select vSwitches that reside in different zones.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
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
        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled
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
        if self.rds_instances is not None:
            result['rds_instances'] = self.rds_instances
        if self.scaling_policy is not None:
            result['scaling_policy'] = self.scaling_policy
        if self.security_group_id is not None:
            result['security_group_id'] = self.security_group_id
        if self.security_group_ids is not None:
            result['security_group_ids'] = self.security_group_ids
        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled
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
        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')
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
            temp_model = CreateClusterNodePoolRequestScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['private_pool_options'])
        if m.get('rds_instances') is not None:
            self.rds_instances = m.get('rds_instances')
        if m.get('scaling_policy') is not None:
            self.scaling_policy = m.get('scaling_policy')
        if m.get('security_group_id') is not None:
            self.security_group_id = m.get('security_group_id')
        if m.get('security_group_ids') is not None:
            self.security_group_ids = m.get('security_group_ids')
        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')
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
        # Specifies whether to enable confidential computing for the cluster.
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
        node_config: CreateClusterNodePoolRequestNodeConfig = None,
        nodepool_info: CreateClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: CreateClusterNodePoolRequestScalingGroup = None,
        tee_config: CreateClusterNodePoolRequestTeeConfig = None,
    ):
        # The configuration of auto scaling.
        self.auto_scaling = auto_scaling
        # This parameter is deprecated. Use the desired_size parameter instead.
        # 
        # The number of nodes in the node pool.
        self.count = count
        # This parameter is deprecated.
        # 
        # The configuration of the edge node pool.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. This parameter takes effect only when you set the `type` parameter of the node pool to `edge`. Valid values:
        # 
        # *   `basic`: basic
        # *   `improved`: enhanced
        # *   `private`: dedicated Only Kubernetes 1.22 and later support this parameter.
        self.interconnect_mode = interconnect_mode
        # The configuration of the cluster.
        self.kubernetes_config = kubernetes_config
        # The configuration of the managed node pool feature.
        self.management = management
        # The maximum number of nodes that can be created in the edge node pool. You must specify a value that is equal to or larger than 0. A value of 0 indicates that the number of nodes in the node pool is limited only by the quota of nodes in the cluster. In most cases, this parameter is set to a value larger than 0 for edge node pools. This parameter is set to 0 for node pools of the ess type or default edge node pools.
        self.max_nodes = max_nodes
        self.node_config = node_config
        # The configuration of the node pool.
        self.nodepool_info = nodepool_info
        # The configuration of the scaling group that is used by the node pool.
        self.scaling_group = scaling_group
        # The configuration of confidential computing for the cluster.
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
        if self.node_config:
            self.node_config.validate()
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
        if m.get('node_config') is not None:
            temp_model = CreateClusterNodePoolRequestNodeConfig()
            self.node_config = temp_model.from_map(m['node_config'])
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
        request_id: str = None,
        task_id: str = None,
    ):
        # The node pool ID.
        self.nodepool_id = nodepool_id
        self.request_id = request_id
        # The ID of the task.
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
        # The `hostname` of the cloud-native box.
        # 
        # >  After the cloud-native box is activated, the `hostname` is automatically modified. The `hostname` is prefixed with the model and the prefix is followed by a random string.
        self.hostname = hostname
        # The model of the cloud-native box.
        self.model = model
        # The serial number of the cloud-native box.
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
        # The ID of the cloud-native box.
        self.edge_machine_id = edge_machine_id
        # The request ID.
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
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        self.action = action
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the trigger project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`.
        # 
        # Example: `default/test-app`.
        self.project_id = project_id
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
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
        # The action that the trigger performs. For example, a value of `redeploy` indicates that the trigger redeploys the application.
        self.action = action
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the trigger.
        self.id = id
        # The name of the trigger project.
        self.project_id = project_id
        # The type of trigger.
        # 
        # Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
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
        # The description of the template.
        self.description = description
        # The name of the orchestration template.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-).
        self.name = name
        # The label of the template.
        self.tags = tags
        # The template content in the YAML format.
        self.template = template
        # The type of template. You can set the parameter to a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If you set the parameter to `compose`, the template is not displayed in the console.
        # 
        # We recommend that you set the parameter to `kubernetes`.
        # 
        # Default value: `compose`.
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
        # The ID of the orchestration template.
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
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        self.action = action
        # The cluster ID.
        self.cluster_id = cluster_id
        # The name of the trigger project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`.
        # 
        # Example: `default/test-app`.
        self.project_id = project_id
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
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
        # The action that the trigger performs. For example, a value of `redeploy` indicates that the trigger redeploys the application.
        self.action = action
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The ID of the trigger.
        self.id = id
        # The name of the trigger project.
        self.project_id = project_id
        # The type of trigger. Default value: deployment.
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
        pass

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
        pass

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
        # Specifies whether to retain the Server Load Balancer (SLB) resources that are created by the cluster.
        # 
        # *   `true`: retains the SLB resources that are created by the cluster.
        # *   `false`: does not retain the SLB resources that are created by the cluster.
        # 
        # Default value: `false`.
        self.keep_slb = keep_slb
        # Specifies whether to retain all resources. If you set the parameter to `true`, the `retain_resources` parameter is ignored.
        # 
        # *   `true`: retains all resources.
        # *   `false`: does not retain all resources.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The list of resources. To retain resources when you delete a cluster, you need to specify the IDs of the resources to be retained.
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
        # Specifies whether to retain the Server Load Balancer (SLB) resources that are created by the cluster.
        # 
        # *   `true`: retains the SLB resources that are created by the cluster.
        # *   `false`: does not retain the SLB resources that are created by the cluster.
        # 
        # Default value: `false`.
        self.keep_slb = keep_slb
        # Specifies whether to retain all resources. If you set the parameter to `true`, the `retain_resources` parameter is ignored.
        # 
        # *   `true`: retains all resources.
        # *   `false`: does not retain all resources.
        # 
        # Default value: `false`.
        self.retain_all_resources = retain_all_resources
        # The list of resources. To retain resources when you delete a cluster, you need to specify the IDs of the resources to be retained.
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


class DeleteClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.request_id = request_id
        # The task ID.
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


class DeleteClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DeleteClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteClusterNodepoolRequest(TeaModel):
    def __init__(
        self,
        force: bool = None,
    ):
        # Specifies whether to forcefully delete the node pool.
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
        task_id: str = None,
    ):
        # The request ID.
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
        # Specifies whether to remove all pods from the nodes that you want to remove. Valid values:
        # 
        # *   `true`: removes all pods from the nodes that you want to remove.
        # *   `false`: does not remove pods from the nodes that you want to remove.
        # 
        # Default value: `false`.
        self.drain_node = drain_node
        # The list of nodes to be removed. You need to specify the name of the nodes used in the cluster, for example, `cn-hangzhou.192.168.0.70`.
        self.nodes = nodes
        # Specifies whether to release the Elastic Compute Service (ECS) instances. Valid values:
        # 
        # *   `true`: releases the ECS instances.
        # *   `false`: does not release the ECS instances.
        # 
        # Default value: `false`.
        # 
        # >  You cannot release subscription ECS instances.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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
        # Specifies whether to forcefully delete the cloud-native box. Valid values:
        # 
        # *   `true`: forcefully deletes the cloud-native box.
        # *   `false`: does not forcefully delete the cloud-native box.
        # 
        # Default value: `false`.
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
        pass

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
        pass

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
        # The ID of the policy instance.
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
        # A list of policy instances.
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
        pass

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
        pass

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
        # The action of the policy. Valid values:
        # 
        # *   `deny`: Deployments that match the policy are denied.
        # *   `warn`: Alerts are generated for Deployments that match the policy.
        self.action = action
        # The applicable scope of the policy instance. If you leave this parameter empty, the policy instance is applicable to all namespaces.
        self.namespaces = namespaces
        # The parameters of the policy instance.
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
        # A list of policy instances.
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
        # The time when the workflow was created.
        self.create_time = create_time
        # The duration of the workflow.
        self.duration = duration
        # The end time of the task.
        self.finish_time = finish_time
        # The size of the input data.
        self.input_data_size = input_data_size
        # The name of the workflow.
        self.job_name = job_name
        # The namespace to which the workflow belongs.
        self.job_namespace = job_namespace
        # The size of the output data.
        self.output_data_size = output_data_size
        # The current state of the workflow.
        self.status = status
        # The number of base pairs.
        self.total_bases = total_bases
        # The number of reads.
        self.total_reads = total_reads
        # The user input parameters.
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


class DescribeAddonRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        profile: str = None,
        region_id: str = None,
        version: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.cluster_version = cluster_version
        self.profile = profile
        self.region_id = region_id
        self.version = version

    def validate(self):
        pass

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
        if self.cluster_version is not None:
            result['cluster_version'] = self.cluster_version
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('cluster_version') is not None:
            self.cluster_version = m.get('cluster_version')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeAddonResponseBodyNewerVersions(TeaModel):
    def __init__(
        self,
        minimum_cluster_version: str = None,
        upgradable: bool = None,
        version: str = None,
    ):
        self.minimum_cluster_version = minimum_cluster_version
        self.upgradable = upgradable
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.minimum_cluster_version is not None:
            result['minimum_cluster_version'] = self.minimum_cluster_version
        if self.upgradable is not None:
            result['upgradable'] = self.upgradable
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('minimum_cluster_version') is not None:
            self.minimum_cluster_version = m.get('minimum_cluster_version')
        if m.get('upgradable') is not None:
            self.upgradable = m.get('upgradable')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeAddonResponseBody(TeaModel):
    def __init__(
        self,
        architecture: List[str] = None,
        category: str = None,
        config_schema: str = None,
        install_by_default: bool = None,
        managed: bool = None,
        name: str = None,
        newer_versions: List[DescribeAddonResponseBodyNewerVersions] = None,
        supported_actions: List[str] = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.category = category
        self.config_schema = config_schema
        self.install_by_default = install_by_default
        self.managed = managed
        self.name = name
        self.newer_versions = newer_versions
        self.supported_actions = supported_actions
        self.version = version

    def validate(self):
        if self.newer_versions:
            for k in self.newer_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.category is not None:
            result['category'] = self.category
        if self.config_schema is not None:
            result['config_schema'] = self.config_schema
        if self.install_by_default is not None:
            result['install_by_default'] = self.install_by_default
        if self.managed is not None:
            result['managed'] = self.managed
        if self.name is not None:
            result['name'] = self.name
        result['newer_versions'] = []
        if self.newer_versions is not None:
            for k in self.newer_versions:
                result['newer_versions'].append(k.to_map() if k else None)
        if self.supported_actions is not None:
            result['supported_actions'] = self.supported_actions
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')
        if m.get('install_by_default') is not None:
            self.install_by_default = m.get('install_by_default')
        if m.get('managed') is not None:
            self.managed = m.get('managed')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.newer_versions = []
        if m.get('newer_versions') is not None:
            for k in m.get('newer_versions'):
                temp_model = DescribeAddonResponseBodyNewerVersions()
                self.newer_versions.append(temp_model.from_map(k))
        if m.get('supported_actions') is not None:
            self.supported_actions = m.get('supported_actions')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeAddonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeAddonResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeAddonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeAddonsRequest(TeaModel):
    def __init__(
        self,
        cluster_profile: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        region: str = None,
    ):
        # The type of cluster. Valid values:
        # 
        # *   `Default`: ACK managed cluster
        # *   `Serverless`: ACK Serverless cluster
        # *   `Edge`: ACK Edge cluster
        self.cluster_profile = cluster_profile
        # The edition of the cluster. If you set the cluster type to `ManagedKubernetes`, the following editions are supported:
        # 
        # *   `ack.pro.small`: ACK Pro cluster
        # *   `ack.standard`: ACK Basic cluster
        # 
        # By default, this parameter is left empty. If you leave this parameter empty, clusters are not filtered by edition.
        self.cluster_spec = cluster_spec
        # The type of cluster. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK Pro clusters, ACK Basic clusters, ACK Serverless Pro clusters, ACK Serverless Basic clusters, ACK Edge Pro clusters, and ACK Edge Basic clusters.
        # *   `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The cluster version.
        self.cluster_version = cluster_version
        # The region ID of the cluster.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_profile is not None:
            result['cluster_profile'] = self.cluster_profile
        if self.cluster_spec is not None:
            result['cluster_spec'] = self.cluster_spec
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.cluster_version is not None:
            result['cluster_version'] = self.cluster_version
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_profile') is not None:
            self.cluster_profile = m.get('cluster_profile')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('cluster_version') is not None:
            self.cluster_version = m.get('cluster_version')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class DescribeAddonsResponseBodyComponentGroupsItems(TeaModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the component.
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
        # The name of the component group.
        self.group_name = group_name
        # The names of the components in the component group.
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


class DescribeAddonsResponseBody(TeaModel):
    def __init__(
        self,
        component_groups: List[DescribeAddonsResponseBodyComponentGroups] = None,
        standard_components: Dict[str, StandardComponentsValue] = None,
    ):
        # The list of the returned components.
        self.component_groups = component_groups
        # Standard components.
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


class DescribeClusterAddonInstanceResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        # The configuration of the component.
        self.config = config
        # The name of the component.
        self.name = name
        # The status of the component. Valid values:
        # 
        # *   initial: The component is being installed.
        # *   active: The component is installed.
        # *   unhealthy: The component is in an abnormal state.
        # *   upgrading: The component is being updated.
        # *   updating: The component is being modified.
        # *   deleting: The component is being uninstalled.
        # *   deleted: The component is deleted.
        self.state = state
        # The version of the component.
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
        if self.state is not None:
            result['state'] = self.state
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeClusterAddonInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterAddonInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeClusterAddonInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClusterAddonMetadataResponseBody(TeaModel):
    def __init__(
        self,
        config_schema: str = None,
        name: str = None,
        version: str = None,
    ):
        # The component schema parameters.
        self.config_schema = config_schema
        # The component name.
        self.name = name
        # The component version.
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
        pass

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
        # The list of component names.
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
        # The list of component names.
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
        pass

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
        pass

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
        # The CPU architecture of the node. Valid values: `amd64`, `arm`, and `arm64`.
        # 
        # Default value: `amd64`.
        # 
        # >  This parameter is required if you want to add the existing node to a Container Service for Kubernetes (ACK) Edge cluster.
        self.arch = arch
        # Specifies whether to mount data disks to an existing instance when you add the instance to the cluster. You can add data disks to store container data and images. Valid values:
        # 
        # *   `true`: mounts data disks to the existing instance that you want to add. After a data disk is mounted, the original data on the disk is erased. Back up data before you mount a data disk.
        # *   `false`: does not mount data disks to the existing instance.
        # 
        # Default value: `false`.
        # 
        # How a data disk is mounted:
        # 
        # *   If the Elastic Compute Service (ECS) instances are already mounted with data disks and the file system of the last data disk is not initialized, the system automatically formats this data disk to ext4 and mounts it to /var/lib/docker and /var/lib/kubelet.
        # *   If no data disk is mounted to the ECS instance, the system does not purchase a new data disk.
        self.format_disk = format_disk
        # Specifies whether to retain the name of the existing instance when it is added to the cluster. If you do not retain the instance name, the instance is named in the `worker-k8s-for-cs-<clusterid>` format. Valid values:
        # 
        # *   `true`: retains the instance name.
        # *   `false`: does not retain the instance name.
        # 
        # Default value: `true`
        self.keep_instance_name = keep_instance_name
        # The ID of the node pool to which you want to add an existing node. This parameter allows you to add an existing node to a specified node pool.
        # 
        # >  If you do not specify a node pool ID, the node is added to the default node pool.
        self.nodepool_id = nodepool_id
        # The node configurations for the existing instance that you want to add as a node.
        # 
        # >  This parameter is required if you want to add the existing node to an ACK Edge cluster.
        self.options = options
        # After you specify the list of RDS instances, the ECS instances in the cluster are automatically added to the whitelist of the RDS instances.
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
        pass

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
        parameters: Dict[str, str] = None,
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The edition of the cluster if the cluster is an ACK managed cluster. Valid values:
        # 
        # *   `ack.pro.small`: ACK Pro
        # *   `ack.standard`: ACK Basic
        self.cluster_spec = cluster_spec
        # The type of cluster. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster
        # *   `ManagedKubernetes`: ACK managed cluster
        # *   `Ask`: ACK Serverless cluster
        # *   `ExternalKubernetes`: registered cluster
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.created = created
        # The current Kubernetes version of the cluster. For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](~~185269~~).
        self.current_version = current_version
        # Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the Container Service console or by calling API operations. Valid values:
        # 
        # *   `true`: deletion protection is enabled for the cluster. This way, the cluster cannot be deleted in the Container Service console or by calling API operations.
        # *   `false`: deletion protection is disabled for the cluster. This way, the cluster can be deleted in the Container Service console or by calling API operations.
        self.deletion_protection = deletion_protection
        # The Docker version that is used by the cluster.
        self.docker_version = docker_version
        self.external_loadbalancer_id = external_loadbalancer_id
        # The initial Kubernetes version of the cluster.
        self.init_version = init_version
        # The maintenance window of the cluster. This feature is available only in ACK Pro clusters.
        self.maintenance_window = maintenance_window
        # The endpoints of the cluster, including an internal endpoint and a public endpoint.
        self.master_url = master_url
        # The metadata of the cluster.
        self.meta_data = meta_data
        # The name of the cluster.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.name = name
        self.network_mode = network_mode
        self.next_version = next_version
        # The ROS parameters of the cluster.
        self.parameters = parameters
        self.private_zone = private_zone
        # Indicates the scenario in which the cluster is used. Valid values:
        # 
        # *   `Default`: non-edge computing scenarios
        # *   `Edge`: edge computing scenarios
        self.profile = profile
        # The region ID of the cluster.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # The ID of the security group to which the cluster belongs.
        self.security_group_id = security_group_id
        # The number of nodes in the cluster. Master nodes and worker nodes are included.
        self.size = size
        # The status of the cluster. Valid values:
        # 
        # *   `initial`: The cluster is being created.
        # *   `failed`: The cluster failed to be created.
        # *   `running`: The cluster is running.
        # *   `updating`: The cluster is being updated.
        # *   `updating_failed`: The cluster failed to be updated.
        # *   `scaling`: The cluster is being scaled.
        # *   `waiting`: The cluster is waiting for connection requests.
        # *   `disconnected`: The cluster is disconnected.
        # *   `stopped`: The cluster is stopped.
        # *   `deleting`: The cluster is being deleted.
        # *   `deleted`: The cluster is deleted.
        # *   `delete_failed`: The cluster failed to be deleted.
        self.state = state
        # The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets:
        # 
        # *   10.0.0.0/8
        # *   172.16-31.0.0/12-16
        # *   192.168.0.0/16
        # 
        # The pod CIDR block cannot overlap with the CIDR block of the VPC or the CIDR blocks of the clusters in the VPC.
        # 
        # For more information, see [Plan CIDR blocks for an ACK cluster](~~186964~~).
        self.subnet_cidr = subnet_cidr
        # The resource labels of the cluster.
        self.tags = tags
        # The time when the cluster was updated.
        self.updated = updated
        # The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster.
        self.vpc_id = vpc_id
        # The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability.
        self.vswitch_id = vswitch_id
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage Elastic Compute Service (ECS) instances.
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
        if self.parameters is not None:
            result['parameters'] = self.parameters
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
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
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
        task_id: str = None,
    ):
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 50.
        self.page_size = page_size
        # The ID of the query task.
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
        # The severity level of the event.
        # 
        # Valid values:
        # 
        # *   warning
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   error
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   info
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.level = level
        # The details of the event.
        self.message = message
        # The status of the event.
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
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The description of the event.
        self.data = data
        # The event ID.
        self.event_id = event_id
        # The event source.
        self.source = source
        # The subject related to the event.
        self.subject = subject
        # The time when the event started.
        self.time = time
        # The type of event. Valid values:
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
        # The number of the page to return.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 50. Default value: 50.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The list of events.
        self.events = events
        # The pagination information.
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
        # The ID of the log entry.
        self.id = id
        # The cluster ID.
        self.cluster_id = cluster_id
        # The log content.
        self.cluster_log = cluster_log
        # The time when the log entry was generated.
        self.created = created
        # The time when the log entry was updated.
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
        # The labels of the nodes in the node pool. You can add labels to the nodes in the cluster. You must add labels based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # A custom node name consists of a prefix, an IP substring, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter.
        # *   The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The name of the container runtime.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The taints of the nodes in the node pool. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, tolerations allow pods to be scheduled to nodes with matching taints. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        self.unschedulable = unschedulable
        # The user data of the node pool. For more information, see [Generate user data](~~49121~~).
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
        if m.get('unschedulable') is not None:
            self.unschedulable = m.get('unschedulable')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
    ):
        # 是否允许重启节点。
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy(TeaModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # 是否允许自动升级kubelet。
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')
        return self


class DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig(TeaModel):
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
        auto_repair_policy: DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig = None,
    ):
        # Indicates whether auto repair is enabled. This parameter takes effect only when `enable=true` is specified. Valid values:
        # 
        # *   `true`: Auto repair is enabled.
        # *   `false`: Auto repair is disabled.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m['auto_repair_policy'])
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('auto_upgrade_policy') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m['auto_upgrade_policy'])
        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')
        if m.get('auto_vul_fix_policy') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m['auto_vul_fix_policy'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolDetailResponseBodyNodeConfig(TeaModel):
    def __init__(
        self,
        kubelet_configuration: KubeletConfig = None,
    ):
        # Kubelet参数配置。
        self.kubelet_configuration = kubelet_configuration

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m['kubelet_configuration'])
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


class DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of preemptible instances.
        self.instance_type = instance_type
        # The price limit of a preemptible instance.
        # 
        # Unit: USD/hour.
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
        cis_enabled: bool = None,
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
        login_as_non_root: bool = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions = None,
        ram_policy: str = None,
        rds_instances: List[str] = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[DescribeClusterNodePoolDetailResponseBodyScalingGroupSpotPriceLimit] = None,
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
        tags: List[Tag] = None,
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
        self.cis_enabled = cis_enabled
        # Indicates whether pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created due to reasons such as cost or insufficient inventory. This parameter takes effect when `multi_az_policy` is set to `COST_OPTIMIZED`. Valid values:
        # 
        # *   `true`: Pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        # *   `false`: Pay-as-you-go instances are not automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configurations of the data disks that are attached to the nodes in the node pool. The configurations include the disk type and disk size.
        self.data_disks = data_disks
        # The ID of the deployment set to which the ECS instances in the node pool belong.
        self.deploymentset_id = deploymentset_id
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The ID of the custom image. You can call the `DescribeKubernetesVersionMetadata` operation to query the images supported by ACK.
        self.image_id = image_id
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method.
        # *   `PostPaid`: the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # A list of instance types. You can select multiple instance types. When the system needs to create a node, it starts from the first instance type until the node is created. The instance type that is used to create the node varies based on the actual instance stock.
        self.instance_types = instance_types
        # The billing method of the public IP address of the node.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must set this parameter or the `login_password` parameter. You must set `key_pair` if the node pool is a managed node pool.
        self.key_pair = key_pair
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
        #     **\
        # 
        #     **Note**The `COST_OPTIMIZED` setting takes effect only when multiple instance types are specified or at least one instance type is specified for preemptible instances.
        # 
        # *   `BALANCE`: ECS instances are evenly distributed across multiple zones specified by the scaling group. If ECS instances become imbalanced among multiple zones due to insufficient inventory, you can call the RebalanceInstances operation of Auto Scaling to balance the instance distribution among zones. For more information, see [RebalanceInstances](~~71516~~).
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
        # After you specify the list of RDS instances, the ECS instances in the cluster are automatically added to the whitelist of the RDS instances.
        self.rds_instances = rds_instances
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
        # For more information, see [Preemptible instances](~~157759~~).
        self.spot_strategy = spot_strategy
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        self.system_disk_categories = system_disk_categories
        # The type of system disk. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        self.system_disk_category = system_disk_category
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        self.system_disk_encrypted = system_disk_encrypted
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for enhanced SSDs (ESSDs).
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of a node. Unit: GiB.
        # 
        # Valid values: 20 to 500.
        self.system_disk_size = system_disk_size
        # The labels that you want to add to the ECS instances.
        # 
        # A key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://.
        self.tags = tags
        # The IDs of vSwitches. You can specify 1 to 20 vSwitches.
        # 
        # > We recommend that you select vSwitches in different zones to ensure high availability.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
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
        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled
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
        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled
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
        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')
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
            temp_model = DescribeClusterNodePoolDetailResponseBodyScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['private_pool_options'])
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
        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')
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
        # Indicates whether confidential computing is enabled. Valid values:
        # 
        # *   `true`: Confidential computing is enabled.
        # *   `false`: Confidential computing is disabled.
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
        node_config: DescribeClusterNodePoolDetailResponseBodyNodeConfig = None,
        nodepool_info: DescribeClusterNodePoolDetailResponseBodyNodepoolInfo = None,
        scaling_group: DescribeClusterNodePoolDetailResponseBodyScalingGroup = None,
        status: DescribeClusterNodePoolDetailResponseBodyStatus = None,
        tee_config: DescribeClusterNodePoolDetailResponseBodyTeeConfig = None,
    ):
        # The auto scaling configuration of the node pool.
        self.auto_scaling = auto_scaling
        # The network configuration of the edge node pool. This parameter takes effect only for edge node pools.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. Valid values: basic and enhanced. This parameter takes effect only for edge node pools.
        self.interconnect_mode = interconnect_mode
        # The configuration of the cluster where the node pool is deployed.
        self.kubernetes_config = kubernetes_config
        # The configuration of the managed node pool feature.
        self.management = management
        # The maximum number of nodes that are supported by the edge node pool. The value of this parameter must be equal to or greater than 0. A value of 0 indicates that the number of nodes in the node pool is limited only by the quota of nodes in the cluster. In most cases, this parameter is set to a value larger than 0 for edge node pools. This parameter is set to 0 for node pools whose types are ess or default edge node pools.
        self.max_nodes = max_nodes
        # 节点配置
        self.node_config = node_config
        # The configuration of the node pool.
        self.nodepool_info = nodepool_info
        # The configuration of the scaling group.
        self.scaling_group = scaling_group
        # The status details about the node pool.
        self.status = status
        # The configuration of confidential computing.
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
        if m.get('node_config') is not None:
            temp_model = DescribeClusterNodePoolDetailResponseBodyNodeConfig()
            self.node_config = temp_model.from_map(m['node_config'])
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
        # The maximum bandwidth of the EIP.
        self.eip_bandwidth = eip_bandwidth
        # The metering method of the EIP. Valid values:
        # 
        # *   `PayByBandwidth`: pay-by-bandwidth.
        # *   `PayByTraffic`: pay-by-traffic.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Indicates whether auto scaling is enabled.
        # 
        # *   `true`: Auto scaling is enabled for the node pool.
        # *   `false`: Auto scaling is disabled for the node pool. If you set this parameter to `false`, other parameters in the `auto_scaling` section does not take effect.
        self.enable = enable
        # Indicates whether an EIP is associated with the node pool. Valid values:
        # 
        # *   `true`: An EIP is associated with the node pool.
        # *   `false`: No EIP is associated with the node pool.
        self.is_bond_eip = is_bond_eip
        # The maximum number of Elastic Compute Service (ECS) instances that can be created in the node pool.
        self.max_instances = max_instances
        # The minimum number of ECS instances that must be retained in the node pool.
        self.min_instances = min_instances
        # The instance types that can be used for the auto scaling of a node pool. Valid values:
        # 
        # *   `cpu`: regular instance.
        # *   `gpu`: GPU-accelerated instance.
        # *   `gpushare`: shared GPU-accelerated instance.
        # *   `spot`: preemptible instance.
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
        # This parameter is deprecated.
        # 
        # The bandwidth of the enhanced edge node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # This parameter is deprecated.
        # 
        # The ID of the Cloud Connect Network (CCN) instance that is associated with the enhanced edge node pool.
        self.ccn_id = ccn_id
        # This parameter is deprecated.
        # 
        # The region to which the CCN instance that is with the enhanced edge node pool belongs.
        self.ccn_region_id = ccn_region_id
        # This parameter is deprecated.
        # 
        # The ID of the Cloud Enterprise Network (CEN) instance that is associated with the enhanced edge node pool.
        self.cen_id = cen_id
        # This parameter is deprecated.
        # 
        # The subscription duration of the enhanced edge node pool. The duration is measured in months.
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
        unschedulable: bool = None,
        user_data: str = None,
    ):
        # Indicates whether the CloudMonitor agent is installed on ECS nodes in the cluster. After the CloudMonitor agent is installed, you can view monitoring information about the ECS instances in the CloudMonitor console. Installation is recommended. Valid values:
        # 
        # *   `true`: The CloudMonitor agent is installed on ECS nodes.
        # *   `false`: The CloudMonitor agent is not installed on ECS nodes.
        self.cms_enabled = cms_enabled
        # The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity.
        # *   `none`: indicates that the default CPU affinity is used.
        self.cpu_policy = cpu_policy
        # The labels of the nodes in the node pool. You can add labels to the nodes in the cluster. You must add labels based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add at most 20 labels.
        # *   The key must be unique and cannot exceed 64 characters in length. The value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # A custom node name consists of a prefix, an IP substring, and a suffix.
        # 
        # *   The prefix and suffix can contain multiple parts that are separated by periods (.). Each part can contain lowercase letters, digits, and hyphens (-). A custom node name must start and end with a digit or lowercase letter.
        # *   The IP substring length specifies the number of digits to be truncated from the end of the node IP address. The IP substring length ranges from 5 to 12.
        # 
        # For example, if the node IP address is 192.168.0.55, the prefix is aliyun.com, the IP substring length is 5, and the suffix is test, the node name will be aliyun.com00055test.
        self.node_name_mode = node_name_mode
        # The name of the container runtime.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The taints that you want to add to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, tolerations allow pods to be scheduled to nodes with matching taints. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # 扩容后的节点是否可调度。
        self.unschedulable = unschedulable
        # The user data of the node pool. For more information, see [Generate user-defined data](~~49121~~).
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
        if m.get('unschedulable') is not None:
            self.unschedulable = m.get('unschedulable')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
    ):
        # 是否允许重启节点。
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy(TeaModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # 是否允许自动升级kubelet。
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig(TeaModel):
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
        # The maximum number of nodes that can be in the unschedulable state. Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of additional nodes.
        self.surge = surge
        # The percentage of temporary nodes to the nodes in the node pool. You must set this parameter or `surge`.
        # 
        # The number of extra nodes = The percentage of extra nodes × The number of nodes in the node pool. For example, the percentage of extra nodes is set to 50% and the number of nodes in the node pool is six. The number of extra nodes will be three.
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
        auto_repair_policy: DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig = None,
    ):
        # Indicates whether auto repair is enabled. This parameter takes effect only when `enable=true` is specified. Valid values:
        # 
        # *   `true`: Auto repair is enabled.
        # *   `false`: Auto repair is disabled.
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
        # Indicates whether the managed node pool feature is enabled. Valid values:
        # 
        # *   `true`: The managed node pool feature is enabled.
        # *   `false`: The managed node pool feature is disabled. Other parameters in this section take effect only when `enable=true` is specified.
        self.enable = enable
        # The configuration of auto update. The configuration take effects only when `enable=true` is specified.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m['auto_repair_policy'])
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('auto_upgrade_policy') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m['auto_upgrade_policy'])
        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')
        if m.get('auto_vul_fix_policy') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m['auto_vul_fix_policy'])
        if m.get('enable') is not None:
            self.enable = m.get('enable')
        if m.get('upgrade_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsManagementUpgradeConfig()
            self.upgrade_config = temp_model.from_map(m['upgrade_config'])
        return self


class DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig(TeaModel):
    def __init__(
        self,
        kubelet_configuration: KubeletConfig = None,
    ):
        # The kubelet configuration.
        self.kubelet_configuration = kubelet_configuration

    def validate(self):
        if self.kubelet_configuration:
            self.kubelet_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.kubelet_configuration is not None:
            result['kubelet_configuration'] = self.kubelet_configuration.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('kubelet_configuration') is not None:
            temp_model = KubeletConfig()
            self.kubelet_configuration = temp_model.from_map(m['kubelet_configuration'])
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
        # The time when the node pool was created.
        self.created = created
        # Indicates whether the node pool is a default node pool. A Container Service for Kubernetes (ACK) cluster usually has only one default node pool. Valid values:
        # 
        # *   `true`: The node pool is a default node pool.
        # *   `false`: The node pool is not a default node pool.
        self.is_default = is_default
        # The name of the node pool.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.name = name
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group to which the node pool belongs.
        self.resource_group_id = resource_group_id
        # The type of node pool. Valid values:
        # 
        # *   `edge`: edge node pool
        # *   `ess`: node pool in the cloud.
        self.type = type
        # The time when the node pool was last updated.
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


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The private pool ID. The ID of a private pool is the same as the ID of the elasticity assurance or capacity reservation for which the private pool is generated.
        self.id = id
        # The type of private node pool. This parameter specifies the type of private node pool that you want to use to create instances. A private node pool is generated when an elasticity assurance or a capacity reservation service takes effect. The system selects a private node pool to launch instances. Valid values:
        # 
        # *   `Open`: open private node pool. The system selects an open private node pool to launch instances. If no matching open private node pool is available, the resources in the public node pool are used.
        # *   `Target`: specific private pool. The system uses the resources of the specified private node pool to launch instances. If the specified private node pool is unavailable, instances cannot be started.
        # *   `None`: no private node pool is used. The resources of private node pools are not used to lancuh instances.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of preemptible instances.
        self.instance_type = instance_type
        # The price limit of a single preemptible instance.
        # 
        # Unit: USD/hour.
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
        cis_enabled: bool = None,
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
        login_as_non_root: bool = None,
        login_password: str = None,
        multi_az_policy: str = None,
        on_demand_base_capacity: int = None,
        on_demand_percentage_above_base_capacity: int = None,
        period: int = None,
        period_unit: str = None,
        platform: str = None,
        private_pool_options: DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions = None,
        ram_policy: str = None,
        rds_instances: List[str] = None,
        scaling_group_id: str = None,
        scaling_policy: str = None,
        security_group_id: str = None,
        security_group_ids: List[str] = None,
        soc_enabled: bool = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupSpotPriceLimit] = None,
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
        tags: List[Tag] = None,
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
        # 是否开启CIS加固，仅当系统镜像选择Alibaba Cloud Linux 2或Alibaba Cloud Linux 3时，可为节点开启CIS加固。
        self.cis_enabled = cis_enabled
        # Indicates whether pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created due to reasons such as cost or insufficient inventory. This parameter takes effect when `multi_az_policy` is set to `COST_OPTIMIZED`. Valid values:
        # 
        # *   `true`: Pay-as-you-go instances are automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        # *   `false`: Pay-as-you-go instances are not automatically created to meet the required number of ECS instances if preemptible instances cannot be created.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configurations of the data disks that are attached to the nodes in the node pool. The configurations include the disk type and disk size.
        self.data_disks = data_disks
        # The ID of the deployment set to which the ECS instances in the node pool belong.
        self.deploymentset_id = deploymentset_id
        # You can now specify the desired number of nodes for a node pool.
        self.desired_size = desired_size
        # The ID of the custom image. You can call the `DescribeKubernetesVersionMetadata` operation to query the images supported by ACK.
        self.image_id = image_id
        # 操作系统镜像类型。
        self.image_type = image_type
        # The billing method of the nodes in a node pool. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method.
        # *   `PostPaid`: the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # A list of instance types. You can select multiple instance types. When the system needs to create a node, it starts from the first instance type until the node is created. The actual instance types used to create nodes are subject to inventory availability.
        self.instance_types = instance_types
        # The billing method of the public IP address of the node.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must set this parameter or the `login_password` parameter.
        # 
        # You must set `key_pair` if the node pool is a managed node pool.
        self.key_pair = key_pair
        # 弹出的ECS实例是否使用以非root用户登陆。
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
        #     **\
        # 
        #     **Note** `COST_OPTIMIZED` takes effect only when multiple instance types or preemptible instances are specified in the auto scaling conflagrations.
        # 
        # *   `BALANCE`: ECS instances are evenly distributed across multiple zones specified by the scaling group. If ECS instances become imbalanced among multiple zones due to insufficient inventory, you can call the `RebalanceInstances` operation of Auto Scaling to balance the instance distribution among zones. For more information, see [RebalanceInstances](~~71516~~).
        self.multi_az_policy = multi_az_policy
        # The minimum number of pay-as-you-go instances that must be kept in the scaling group. Valid values: 0 to 1000. If the number of pay-as-you-go instances is less than the value of this parameter, Auto Scaling preferably creates pay-as-you-go instances.
        self.on_demand_base_capacity = on_demand_base_capacity
        # The percentage of pay-as-you-go instances among the extra instances that exceed the number specified by `on_demand_base_capacity`. Valid values: 0 to 100.
        self.on_demand_percentage_above_base_capacity = on_demand_percentage_above_base_capacity
        # The subscription duration of worker nodes. This parameter takes effect and is required only when `instance_charge_type` is set to `PrePaid`.
        # 
        # If `PeriodUnit=Month` is specified, the valid values are 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        self.period = period
        # The billing cycle of the nodes. This parameter takes effect only when `instance_charge_type` is set to `PrePaid`.
        # 
        # Valid value: `Month`
        self.period_unit = period_unit
        # The release version of the operating system. Valid values:
        # 
        # *   `CentOS`
        # *   `AliyunLinux`
        # *   `Windows`
        # *   `WindowsCore`
        self.platform = platform
        # The private node pool options.
        self.private_pool_options = private_pool_options
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes that are created on Elastic Compute Service (ECS) instances.
        self.ram_policy = ram_policy
        # After you specify a list of ApsaraDB RDS instances, the ECS instances in the cluster are automatically added to the whitelists of the ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The ID of the scaling group.
        self.scaling_group_id = scaling_group_id
        # The scaling mode of the scaling group. Valid values:
        # 
        # *   `release`: the standard mode. ECS instances are created and released based on resource usage.
        # *   `recycle`: the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances attached with local disks.
        self.scaling_policy = scaling_policy
        # The ID of the security group to which the node pool is added. If the node pool is added to multiple security groups, the first ID in the value of `security_group_ids` is returned.
        self.security_group_id = security_group_id
        # The IDs of the security groups to which the node pool is added.
        self.security_group_ids = security_group_ids
        # 是否开启等保加固，仅当系统镜像选择Alibaba Cloud Linux 2或Alibaba Cloud Linux 3时，可为节点开启等保加固。阿里云为Alibaba Cloud Linux 2和Alibaba Cloud Linux 3等保2.0三级版镜像提供等保合规的基线检查标准和扫描程序。
        self.soc_enabled = soc_enabled
        # The number of instance types that are available for creating preemptible instances. Auto Scaling creates preemptible instances of multiple instance types that are available at the lowest cost. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Indicates whether preemptible instances are supplemented when the number of preemptible instances drops below the specified minimum number. If this parameter is set to true, when the scaling group receives a system message that a preemptible instance is to be reclaimed, the scaling group attempts to create a new instance to replace this instance. Valid values:
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
        # For more information, see [Preemptible instances](~~157759~~).
        self.spot_strategy = spot_strategy
        # 节点系统盘是否开启Burst（性能突发），磁盘类型为cloud_auto时配置。
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        # 系统盘的多磁盘类型。当无法使用高优先级的磁盘类型时，自动尝试下一优先级的磁盘类型创建系统盘。取值范围：cloud：普通云盘。cloud_efficiency：高效云盘。cloud_ssd：SSD云盘。cloud_essd：ESSD云盘。
        self.system_disk_categories = system_disk_categories
        # The type of system disk. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        self.system_disk_category = system_disk_category
        # 系统盘采用的加密算法。取值范围：aes-256。
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        # 是否加密系统盘。取值范围：true：加密。false：不加密。
        self.system_disk_encrypted = system_disk_encrypted
        # 系统盘使用的KMS密钥ID。
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for enhanced SSDs (ESSDs).
        self.system_disk_performance_level = system_disk_performance_level
        # 节点系统盘预配置的读写IOPS，磁盘类型为cloud_auto时配置。
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of a node. Unit: GiB.
        # 
        # Valid values: 20 to 500
        self.system_disk_size = system_disk_size
        # The labels that you want to add to the ECS instances.
        # 
        # The key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://.
        self.tags = tags
        # The vSwitch IDs. You can specify 1 to 20 vSwitches.
        # 
        # >  To ensure high availability, we recommend that you select vSwitches in different zones.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
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
        if self.cis_enabled is not None:
            result['cis_enabled'] = self.cis_enabled
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
        if self.soc_enabled is not None:
            result['soc_enabled'] = self.soc_enabled
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
        if m.get('cis_enabled') is not None:
            self.cis_enabled = m.get('cis_enabled')
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
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['private_pool_options'])
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
        if m.get('soc_enabled') is not None:
            self.soc_enabled = m.get('soc_enabled')
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
        # Indicates whether confidential computing is enabled. Valid values:
        # 
        # *   `true`: Confidential computing is enabled.
        # *   `false`: Confidential computing is disabled.
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
        node_config: DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig = None,
        nodepool_info: DescribeClusterNodePoolsResponseBodyNodepoolsNodepoolInfo = None,
        scaling_group: DescribeClusterNodePoolsResponseBodyNodepoolsScalingGroup = None,
        status: DescribeClusterNodePoolsResponseBodyNodepoolsStatus = None,
        tee_config: DescribeClusterNodePoolsResponseBodyNodepoolsTeeConfig = None,
    ):
        # The configurations about auto scaling.
        self.auto_scaling = auto_scaling
        # This parameter is deprecated.
        # 
        # The network configuration of the edge node pool. This parameter takes effect only for edge node pools.
        self.interconnect_config = interconnect_config
        # The network type of the edge node pool. basic: basic edge node pools. dedicated: dedicated edge node pools. This parameter takes effect only for edge node pools.
        self.interconnect_mode = interconnect_mode
        # The configurations of the cluster where the node pool is deployed.
        self.kubernetes_config = kubernetes_config
        # The configurations of managed node pools. Managed node pools are available only in professional managed Kubernetes clusters.
        self.management = management
        # The maximum number of nodes that are supported by the edge node pool. The value of this parameter must be equal to or greater than 0. A value of 0 indicates that the number of nodes in the node pool is limited only by the quota of nodes in the cluster. In most cases, this parameter is set to a value larger than 0 for edge node pools. This parameter is set to 0 for node pools whose types are ess or default edge node pools.
        self.max_nodes = max_nodes
        # The configurations of nodes.
        self.node_config = node_config
        # The information about the node pool.
        self.nodepool_info = nodepool_info
        # The configuration of the scaling group.
        self.scaling_group = scaling_group
        # The status details about the node pool.
        self.status = status
        # The configurations of confidential computing.
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
        if m.get('node_config') is not None:
            temp_model = DescribeClusterNodePoolsResponseBodyNodepoolsNodeConfig()
            self.node_config = temp_model.from_map(m['node_config'])
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
        # A list of node pools.
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
        # The IDs of the nodes that you want to query. Separate multiple node IDs with commas (,).
        self.instance_ids = instance_ids
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 100.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The node state that you want to use to filter nodes. Valid values:
        # 
        # *   `all`: query nodes in the following four states.
        # *   `running`: query nodes in the running state.
        # *   `removing`: query nodes that are being removed.
        # *   `initial`: query nodes that are being initialized.
        # *   `failed`: query nodes that fail to be created.
        # 
        # Default value: `all`.
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
        # The time when the node was created.
        self.creation_time = creation_time
        # The error message generated when the node was created.
        self.error_message = error_message
        # The expiration date of the node.
        self.expired_time = expired_time
        # The name of the host.
        self.host_name = host_name
        # The ID of the system image that is used by the node.
        self.image_id = image_id
        # The billing method of the node. Valid values:
        # 
        # *   `PrePaid`: the subscription billing method. If the value is PrePaid, make sure that you have a sufficient balance or credit in your account. Otherwise, an `InvalidPayMethod` error is returned.
        # *   `PostPaid`: the pay-as-you-go billing method.
        self.instance_charge_type = instance_charge_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The name of the instance on which the node is deployed.
        self.instance_name = instance_name
        # The role of the node. Valid values:
        # 
        # *   Master: master node
        # *   Worker: worker node
        self.instance_role = instance_role
        # The status of the node.
        self.instance_status = instance_status
        # The type of the node.
        self.instance_type = instance_type
        # The ECS instance family of the node.
        self.instance_type_family = instance_type_family
        # The IP address of the node.
        self.ip_address = ip_address
        # Indicates whether the instance on which the node is deployed is provided by Alibaba Cloud. Valid values:
        # 
        # *   `true`: The instance is provided by Alibaba Cloud.
        # *   `false`: The instance is not provided by Alibaba Cloud.
        self.is_aliyun_node = is_aliyun_node
        # The name of the node. This name is the identifier of the node in the cluster.
        self.node_name = node_name
        # Indicates whether the node is ready. Valid values:
        # 
        # *   `Ready`: The node is ready.
        # *   `NotReady`: The node is not ready.
        # *   `Unknown`: The status of the node is unknown.
        # *   `Offline`: The node is offline.
        self.node_status = node_status
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # Indicates how the node is initialized. A node can be manually created or created by using Resource Orchestration Service (ROS).
        self.source = source
        # The type of preemptible instance. Valid values:
        # 
        # *   NoSpot: a non-preemptible instance.
        # *   SpotWithPriceLimit: a preemptible instance that is configured with the highest bid price.
        # *   SpotAsPriceGo: a preemptible instance for which the system automatically bids based on the current market price.
        self.spot_strategy = spot_strategy
        # The status of the node. Valid values:
        # 
        # *   `pending`: The node is being created.
        # *   `running`: The node is running.
        # *   `starting`: The node is being started.
        # *   `stopping`: The node is being stopped.
        # *   `stopped`: The node is stopped.
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The details of the nodes in the cluster.
        self.nodes = nodes
        # The pagination information.
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


class DescribeClusterResourcesResponseBodyDependencies(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        resource_type: str = None,
        instance_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.resource_type = resource_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
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
        dependencies: List[DescribeClusterResourcesResponseBodyDependencies] = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The time when the resource was created.
        self.created = created
        # The resource ID.
        self.instance_id = instance_id
        # The information about the resource. For more information about how to query the source information about a resource, see [ListStackResources](~~133836~~).
        self.resource_info = resource_info
        # The resource type.
        self.resource_type = resource_type
        # The resource status. Valid values:
        # 
        # *   `CREATE_COMPLETE`: The resource is created.
        # *   `CREATE_FAILED`: The resource failed to be created.
        # *   `CREATE_IN_PROGRESS`: The resource is being created.
        # *   `DELETE_FAILED`: The resource failed to be deleted.
        # *   `DELETE_IN_PROGRESS`: The resource is being deleted.
        # *   `ROLLBACK_COMPLETE`: The resource is rolled back.
        # *   `ROLLBACK_FAILED`: The resource failed to be rolled back.
        # *   `ROLLBACK_IN_PROGRESS`: The resource is being rolled back.
        self.state = state
        # Indicates whether the resource is created by Container Service for Kubernetes (ACK). Valid values:
        # 
        # *   1: The resource is created by ACK.
        # *   0: The resource is an existing resource.
        self.auto_create = auto_create
        self.dependencies = dependencies

    def validate(self):
        if self.dependencies:
            for k in self.dependencies:
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
        result['dependencies'] = []
        if self.dependencies is not None:
            for k in self.dependencies:
                result['dependencies'].append(k.to_map() if k else None)
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
        self.dependencies = []
        if m.get('dependencies') is not None:
            for k in m.get('dependencies'):
                temp_model = DescribeClusterResourcesResponseBodyDependencies()
                self.dependencies.append(temp_model.from_map(k))
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


class DescribeClusterTasksRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('page_number') is not None:
            self.page_number = m.get('page_number')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        return self


class DescribeClusterTasksResponseBodyPageInfo(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of the page returned.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The error code returned.
        self.code = code
        # The error message returned.
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
        # The time when the task was created.
        self.created = created
        # The error returned for the task.
        self.error = error
        # The status of the task.
        self.state = state
        # The task ID.
        self.task_id = task_id
        # The type of task.
        self.task_type = task_type
        # The time when the task was updated.
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
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id
        # The information about the tasks.
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
        # Specifies whether to obtain the kubeconfig file that is used to connect to the cluster over the internal network. Valid values:
        # 
        # *   `true`: obtains the kubeconfig file that is used to connect to the master instance over the internal network.
        # *   `false`: obtains the kubeconfig file that is used to connect to the master instance over the Internet.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address
        # The validity period of a temporary kubeconfig file. Unit: minutes. Valid values: 15 to 4320 (3 days).
        # 
        # >  If you do not specify this parameter, the system specifies a longer validity period. The validity period is returned in the `expiration` parameter.
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
        # The kubeconfig file of the cluster. For more information about the content of the kubeconfig file, see [Configure cluster credentials](~~86494~~).
        self.config = config
        # The validity period of the kubeconfig file. The value is the UTC time displayed in RFC3339 format.
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


class DescribeClusterVulsResponseBodyVulRecords(TeaModel):
    def __init__(
        self,
        cve_list: List[str] = None,
        necessity: str = None,
        node_count: int = None,
        nodepool_id: str = None,
        nodepool_name: str = None,
        vul_alias_name: str = None,
        vul_name: str = None,
        vul_type: str = None,
    ):
        # The CVE list.
        self.cve_list = cve_list
        # The severity level of the vulnerability.
        # 
        # Valid values:
        # 
        # *   nntf
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     low
        # 
        #     <!-- -->
        # 
        # *   later
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     medium
        # 
        #     <!-- -->
        # 
        # *   asap
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     high
        # 
        #     <!-- -->
        self.necessity = necessity
        # The number of nodes that have the vulnerability.
        self.node_count = node_count
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The name of the node pool.
        self.nodepool_name = nodepool_name
        # The alias of the vulnerability.
        self.vul_alias_name = vul_alias_name
        # The name of the vulnerability.
        self.vul_name = vul_name
        # The type of vulnerability.
        # 
        # Valid values:
        # 
        # *   app
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     application vulnerabilities
        # 
        #     <!-- -->
        # 
        # *   sca
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     application vulnerabilities (software component analysis)
        # 
        #     <!-- -->
        # 
        # *   cve
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Linux vulnerabilities
        # 
        #     <!-- -->
        # 
        # *   cms
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Web-CMS vulnerabilities
        # 
        #     <!-- -->
        # 
        # *   sys
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     Windows vulnerabilities
        # 
        #     <!-- -->
        # 
        # *   emg
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     emergency vulnerabilities
        # 
        #     <!-- -->
        self.vul_type = vul_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cve_list is not None:
            result['cve_list'] = self.cve_list
        if self.necessity is not None:
            result['necessity'] = self.necessity
        if self.node_count is not None:
            result['node_count'] = self.node_count
        if self.nodepool_id is not None:
            result['nodepool_id'] = self.nodepool_id
        if self.nodepool_name is not None:
            result['nodepool_name'] = self.nodepool_name
        if self.vul_alias_name is not None:
            result['vul_alias_name'] = self.vul_alias_name
        if self.vul_name is not None:
            result['vul_name'] = self.vul_name
        if self.vul_type is not None:
            result['vul_type'] = self.vul_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cve_list') is not None:
            self.cve_list = m.get('cve_list')
        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')
        if m.get('node_count') is not None:
            self.node_count = m.get('node_count')
        if m.get('nodepool_id') is not None:
            self.nodepool_id = m.get('nodepool_id')
        if m.get('nodepool_name') is not None:
            self.nodepool_name = m.get('nodepool_name')
        if m.get('vul_alias_name') is not None:
            self.vul_alias_name = m.get('vul_alias_name')
        if m.get('vul_name') is not None:
            self.vul_name = m.get('vul_name')
        if m.get('vul_type') is not None:
            self.vul_type = m.get('vul_type')
        return self


class DescribeClusterVulsResponseBody(TeaModel):
    def __init__(
        self,
        vul_records: List[DescribeClusterVulsResponseBodyVulRecords] = None,
    ):
        # An array of vulnerabilities.
        self.vul_records = vul_records

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vul_records = []
        if m.get('vul_records') is not None:
            for k in m.get('vul_records'):
                temp_model = DescribeClusterVulsResponseBodyVulRecords()
                self.vul_records.append(temp_model.from_map(k))
        return self


class DescribeClusterVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeClusterVulsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeClusterVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        name: str = None,
    ):
        # The cluster type.
        self.cluster_type = cluster_type
        # The cluster name based on which the system performs fuzzy searches among the clusters that belong to the current Alibaba Cloud account.
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
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        profile: str = None,
        region_id: str = None,
    ):
        # 集群ID。
        self.cluster_id = cluster_id
        # The cluster type, which is available only when the cluster type is set to `ManagedKubernetes`. Valid values:
        # 
        # *   `ack.pro.small`: ACK Pro cluster
        # *   `ack.standard`: ACK Basic cluster
        # 
        # By default, this parameter is left empty, which means that ACK clusters are not filtered by this parameter.
        self.cluster_spec = cluster_spec
        # The cluster type. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster.
        # *   `ManagedKubernetes`: ACK managed cluster. ACK managed clusters include ACK Pro clusters, ACK Basic clusters, ACK Serverless Pro clusters, ACK Serverless Basic clusters, ACK Edge Pro clusters, and ACK Edge Basic clusters.
        # *   `ExternalKubernetes`: registered cluster.
        self.cluster_type = cluster_type
        # The cluster name.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.name = name
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The identifier of the cluster. Valid values when the cluster_type parameter is set to `ManagedKubernetes`:
        # 
        # *   `Default`: ACK managed cluster
        # *   `Serverless`: ACK Serverless cluster
        # *   `Edge`: ACK Edge cluster
        # 
        # Valid values when the cluster_type parameter is set to `Ask`:
        # 
        # `ask.v2`: ACK Serverless cluster
        # 
        # By default, this parameter is left empty. If you leave this parameter empty, ACK clusters are not filtered by identifier.
        self.profile = profile
        # The region ID of the clusters. You can use this parameter to query all clusters in the specified region.
        self.region_id = region_id

    def validate(self):
        pass

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
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The type of ACK managed cluster. This parameter is available only for ACK managed clusters. Valid values:
        # 
        # *   `ack.pro.small`: ACK Pro cluster
        # *   `ack.standard`: ACK Basic cluster
        self.cluster_spec = cluster_spec
        # The cluster type. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster
        # *   `ManagedKubernetes`: ACK managed cluster
        # *   `Ask`: ACK Serverless cluster
        # *   `ExternalKubernetes`: registered cluster
        self.cluster_type = cluster_type
        # The time when the cluster was created.
        self.created = created
        # The Kubernetes version of the cluster.
        self.current_version = current_version
        # Indicates whether deletion protection is enabled for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the ACK console or by calling API operations. Valid values:
        # 
        # *   `true`: Deletion protection is enabled for the cluster. The cluster cannot be deleted in the ACK console or by calling API operations.
        # *   `false`: Deletion protection is disabled for the cluster. The cluster can be deleted in the ACK console or by calling API operations.
        self.deletion_protection = deletion_protection
        # The Docker version that is used by the cluster.
        self.docker_version = docker_version
        # The ID of the Server Load Balancer (SLB) instance that is used by the Ingress of the cluster.
        # 
        # The default SLB specification is slb.s1.small, which belongs to the high-performance instance type.
        self.external_loadbalancer_id = external_loadbalancer_id
        # The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the versions of open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not specify this parameter, the latest Kubernetes version is used.
        # 
        # You can create clusters of the latest two Kubernetes versions in the ACK console. You can call the corresponding ACK API operation to create clusters of other Kubernetes versions. For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](~~185269~~).
        self.init_version = init_version
        # The maintenance window of the cluster. This feature is available only for ACK Pro clusters.
        self.maintenance_window = maintenance_window
        # The endpoint of the cluster API server, including an internal endpoint and a public endpoint.
        self.master_url = master_url
        # The metadata of the cluster.
        self.meta_data = meta_data
        # The cluster name.
        # 
        # The name must be 1 to 63 characters in length and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.name = name
        # The network mode of the cluster. Valid values:
        # 
        # *   `classic`: classic network
        # *   `vpc`: virtual private cloud (VPC)
        # *   `overlay`: overlay network
        # *   `calico`: network powered by Calico.
        self.network_mode = network_mode
        # The Kubernetes version to which the cluster can be updated.
        self.next_version = next_version
        # Indicates whether Alibaba Cloud DNS PrivateZone is enabled. Valid values:
        # 
        # *   `true`: Alibaba Cloud DNS PrivateZone is enabled.
        # *   `false`: Alibaba Cloud DNS PrivateZone is disabled.
        self.private_zone = private_zone
        # The cluster identifier. Valid values:
        # 
        # *   `Edge`: The cluster is an ACK Edge cluster.
        # *   `Default`: The cluster is not an ACK Edge cluster.
        self.profile = profile
        # The region ID of the cluster.
        self.region_id = region_id
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # The ID of the security group to which the instances of the cluster belong.
        self.security_group_id = security_group_id
        # The number of nodes in the cluster, including master nodes and worker nodes.
        self.size = size
        # The status of the cluster. Valid values:
        # 
        # *   `initial`: The cluster is being created.
        # *   `failed`: The cluster failed to be created.
        # *   `running`: The cluster is running.
        # *   `updating`: The cluster is being updated.
        # *   `updating_failed`: The cluster failed to be updated.
        # *   `scaling`: The cluster is being scaled.
        # *   `stopped`: The cluster is stopped.
        # *   `deleting`: The cluster is being deleted.
        # *   `deleted`: The cluster is deleted.
        # *   `delete_failed`: The cluster failed to be deleted.
        self.state = state
        # The pod CIDR block. It must be a valid and private CIDR block, and must be one of the following CIDR blocks or their subnets:
        # 
        # *   10.0.0.0/8
        # *   172.16-31.0.0/12-16
        # *   192.168.0.0/16
        # 
        # The CIDR block of pods cannot overlap with the CIDR block of the VPC in which the cluster is deployed and the CIDR blocks of existing clusters in the VPC. You cannot modify the pod CIDR block after the cluster is created.
        # 
        # For more information, see [Plan CIDR blocks for an ACK cluster](~~86500~~).
        self.subnet_cidr = subnet_cidr
        # The resource labels of the cluster.
        self.tags = tags
        # The time when the cluster was updated.
        self.updated = updated
        # The ID of the VPC where the cluster is deployed. This parameter is required when you create a cluster.
        self.vpc_id = vpc_id
        # The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability.
        self.vswitch_id = vswitch_id
        # The name of the worker Resource Access Management (RAM) role. The RAM role is assigned to the worker nodes of the cluster to allow the worker nodes to manage Elastic Compute Service (ECS) instances.
        self.worker_ram_role_name = worker_ram_role_name
        # The zone ID.
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The details of the clusters.
        self.clusters = clusters
        # The pagination information.
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
        # The activation progress list.
        self.logs = logs
        # The activation progress.
        self.progress = progress
        # The request ID.
        self.request_id = request_id
        # The activation status.
        self.state = state
        # The activation step.
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
        # The number of vCores.
        self.cpu = cpu
        # The CPU architecture.
        self.cpu_arch = cpu_arch
        # The time when the cloud-native box was created.
        self.created = created
        # The description of the cloud-native box.
        self.description = description
        # Indicates whether the cloud-native box model manages the Docker runtime.
        self.manage_runtime = manage_runtime
        # The memory. Unit: GB.
        self.memory = memory
        # The model of the cloud-native box.
        self.model = model
        # The ID of the cloud-native box.
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
        # The cloud-native box models.
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
        # The device name.
        self.device_name = device_name
        # The model of the cloud-native box.
        self.model = model
        # Product Key
        self.product_key = product_key
        # Request ID
        self.request_id = request_id
        # The serial number of the cloud-native box.
        self.sn = sn
        # Token
        self.token = token
        # The tunnel endpoint.
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
        # The `hostname` of the cloud-native box.
        self.hostname = hostname
        # The lifecycle status.
        self.life_state = life_state
        # The type of cloud-native box.
        self.model = model
        # The status of the cloud-native box. Valid values:
        # 
        # *   `offline`
        # *   `online`
        self.online_state = online_state
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
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
        # The time when the cloud-native box was activated.
        self.active_time = active_time
        # The time when the cloud-native box was created.
        self.created = created
        # The device ID.
        self.edge_machine_id = edge_machine_id
        # The `hostname` of the cloud-native box.
        self.hostname = hostname
        # The lifecycle of the cloud-native box.
        self.life_state = life_state
        # The model of the cloud-native box.
        self.model = model
        # The machine name.
        self.name = name
        # The status of the cloud-native box.
        self.online_state = online_state
        # The serial number.
        self.sn = sn
        # The time when the cloud-native box was last updated.
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
        # The page number.
        # 
        # Default value: 1.
        self.page_number = page_number
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The total number of pages returned.
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
        # The list of cloud-native boxes.
        self.edge_machines = edge_machines
        # The paging information.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The event type. Valid values:
        # 
        # *   `cluster_create`: cluster creation.
        # *   `cluster_scaleout`: cluster scale-out.
        # *   `cluster_attach`: node addition.
        # *   `cluster_delete`: cluster deletion.
        # *   `cluster_upgrade`: cluster upgrades.
        # *   `cluster_migrate`: cluster migration.
        # *   `cluster_node_delete`: node removal.
        # *   `cluster_node_drain`: node draining.
        # *   `cluster_modify`: cluster modifications.
        # *   `cluster_configuration_modify`: modifications of control plane configurations.
        # *   `cluster_addon_install`: component installation.
        # *   `cluster_addon_upgrade`: component updates.
        # *   `cluster_addon_uninstall`: component uninstallation.
        # *   `runtime_upgrade`: runtime updates.
        # *   `nodepool_upgrade`: node pool upgrades.
        # *   `nodepool_update`: node pool updates.
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
        # The severity level of the event.
        self.level = level
        # The details of the event.
        self.message = message
        # The status of the event.
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
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The description of the event.
        self.data = data
        # The event ID.
        self.event_id = event_id
        # The source of the event.
        self.source = source
        # The subject of the event.
        self.subject = subject
        # The time when the event started.
        self.time = time
        # The event type. Valid values:
        # 
        # *   `cluster_create`: cluster creation.
        # *   `cluster_scaleout`: cluster scale-out.
        # *   `cluster_attach`: node addition.
        # *   `cluster_delete`: cluster deletion.
        # *   `cluster_upgrade`: cluster upgrades.
        # *   `cluster_migrate`: cluster migration.
        # *   `cluster_node_delete`: node removal.
        # *   `cluster_node_drain`: node draining.
        # *   `cluster_modify`: cluster modifications.
        # *   `cluster_configuration_modify`: modifications of control plane configurations.
        # *   `cluster_addon_install`: component installation.
        # *   `cluster_addon_upgrade`: component updates.
        # *   `cluster_addon_uninstall`: component uninstallation.
        # *   `runtime_upgrade`: runtime updates.
        # *   `nodepool_upgrade`: node pool upgrades.
        # *   `nodepool_update`: node pool updates.
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The details of the event.
        self.events = events
        # The pagination information.
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
        agent_mode: str = None,
        private_ip_address: str = None,
    ):
        # The permission mode of the agent. Valid values:
        # 
        # admin: the admin mode, which provides full permissions. restricted: the restricted mode, which provides partial permissions. Default value: admin.
        self.agent_mode = agent_mode
        # Specifies whether to obtain the credentials that are used to access the cluster over the internal network.
        # 
        # *   `true`: obtains the credentials that are used to access the cluster over the internal network.
        # *   `false`: obtains the credentials that are used to access the cluster over the Internet.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_mode is not None:
            result['AgentMode'] = self.agent_mode
        if self.private_ip_address is not None:
            result['PrivateIpAddress'] = self.private_ip_address
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentMode') is not None:
            self.agent_mode = m.get('AgentMode')
        if m.get('PrivateIpAddress') is not None:
            self.private_ip_address = m.get('PrivateIpAddress')
        return self


class DescribeExternalAgentResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
    ):
        # The agent configurations in the YAML format.
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
        mode: str = None,
        profile: str = None,
        region: str = None,
        runtime: str = None,
    ):
        # The cluster type that you want to use. Valid values:
        # 
        # *   `Kubernetes`: ACK dedicated cluster
        # *   `ManagedKubernetes`: ACK managed cluster
        # *   `ExternalKubernetes`: registered cluster
        self.cluster_type = cluster_type
        # The Kubernetes version of the cluster. The Kubernetes versions supported by ACK are the same as the Kubernetes versions supported by open source Kubernetes. We recommend that you specify the latest Kubernetes version. If you do not set this parameter, the latest Kubernetes version is used.
        # 
        # You can create ACK clusters of the latest two Kubernetes versions in the ACK console. You can call the specific ACK API operation to create clusters of other Kubernetes versions. For more information about the Kubernetes versions supported by ACK, see [Release notes for Kubernetes versions](~~185269~~).
        self.kubernetes_version = kubernetes_version
        # The query mode. Valid values:
        # 
        # *   `supported`: queries all supported versions.
        # *   `creatable`: queries only versions that allow you to create clusters.
        # 
        # If you specify `KubernetesVersion`, this parameter does not take effect.
        # 
        # Default value: creatable.
        self.mode = mode
        # The scenario where clusters are used. Valid values:
        # 
        # *   `Default`: non-edge computing scenarios
        # *   `Edge`: edge computing scenarios
        # *   `Serverless`: serverless scenarios.
        # 
        # Default value: `Default`.
        self.profile = profile
        # The region ID of the cluster.
        self.region = region
        # The container runtime type that you want to use. You can specify a runtime type to query only OS images that support the runtime type. Valid values:
        # 
        # *   `docker`: Docker
        # *   `containerd`: containerd
        # *   `Sandboxed-Container.runv`: Sandboxed-Container
        # 
        # If you specify a runtime type, only the OS images that support the specified runtime type are returned.
        # 
        # Otherwise, all OS images are returned.
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
        if self.mode is not None:
            result['Mode'] = self.mode
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
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
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
        architecture: str = None,
    ):
        # The image ID.
        self.image_id = image_id
        # The image name.
        self.image_name = image_name
        # The OS platform. Valid values:
        # 
        # *   `AliyunLinux`
        # *   `CentOS`
        # *   `Windows`
        # *   `WindowsCore`
        self.platform = platform
        # The version of the image.
        self.os_version = os_version
        # The type of OS distribution that you want to use. To specify the node OS, we recommend that you use this parameter. Valid values:
        # 
        # *   `CentOS`
        # *   `AliyunLinux`
        # *   `AliyunLinux Qboot`
        # *   `AliyunLinuxUEFI`
        # *   `AliyunLinux3`
        # *   `Windows`
        # *   `WindowsCore`
        # *   `AliyunLinux3Arm64`
        # *   `ContainerOS`
        self.image_type = image_type
        # The type of operating system. Examples:
        # 
        # *   `Windows`
        # *   `Linux`
        self.os_type = os_type
        # The type of image. Valid values:
        # 
        # *   `system`: public image
        # *   `self`: custom image
        # *   `others`: shared image from other Alibaba Cloud accounts
        # *   `marketplace`: image from the marketplace
        self.image_category = image_category
        # The architecture of the image.
        self.architecture = architecture

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
        if self.architecture is not None:
            result['architecture'] = self.architecture
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
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        return self


class DescribeKubernetesVersionMetadataResponseBody(TeaModel):
    def __init__(
        self,
        capabilities: Dict[str, Any] = None,
        images: List[DescribeKubernetesVersionMetadataResponseBodyImages] = None,
        meta_data: Dict[str, Any] = None,
        runtimes: List[Runtime] = None,
        version: str = None,
        release_date: str = None,
        expiration_date: str = None,
        creatable: bool = None,
    ):
        # Features of the queried Kubernetes version.
        self.capabilities = capabilities
        # The OS images that are returned.
        self.images = images
        # The metadata of the Kubernetes version.
        self.meta_data = meta_data
        # Details of the supported container runtimes.
        self.runtimes = runtimes
        # The Kubernetes version that is supported by ACK. For more information, see [Release notes for Kubernetes versions](~~185269~~).
        self.version = version
        # The release date of the Kubernetes version.
        self.release_date = release_date
        # The expiration date of the Kubernetes version.
        self.expiration_date = expiration_date
        # Indicates whether you can create clusters that run the Kubernetes version.
        self.creatable = creatable

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
        if self.release_date is not None:
            result['release_date'] = self.release_date
        if self.expiration_date is not None:
            result['expiration_date'] = self.expiration_date
        if self.creatable is not None:
            result['creatable'] = self.creatable
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
        if m.get('release_date') is not None:
            self.release_date = m.get('release_date')
        if m.get('expiration_date') is not None:
            self.expiration_date = m.get('expiration_date')
        if m.get('creatable') is not None:
            self.creatable = m.get('creatable')
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


class DescribeNodePoolVulsRequest(TeaModel):
    def __init__(
        self,
        necessity: str = None,
    ):
        # The priority to fix the vulnerability. Separate multiple priorities with commas (,). Valid values:
        # 
        # *   `asap`: high
        # *   `later`: medium
        # *   `nntf`: low
        self.necessity = necessity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.necessity is not None:
            result['necessity'] = self.necessity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('necessity') is not None:
            self.necessity = m.get('necessity')
        return self


class DescribeNodePoolVulsResponseBodyVulRecordsVulList(TeaModel):
    def __init__(
        self,
        alias_name: str = None,
        cve_list: List[str] = None,
        name: str = None,
        necessity: str = None,
    ):
        # The alias of the vulnerability.
        self.alias_name = alias_name
        # A list of CVE names corresponding to the vulnerabilities.
        self.cve_list = cve_list
        # The name of the vulnerability.
        self.name = name
        # The severity level of the vulnerability.
        # 
        # Valid values:
        # 
        # *   nntf
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     You can ignore the vulnerability
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   later
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     You can fix the vulnerability later
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   asap
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     You need to fix the vulnerability at the earliest opportunity
        # 
        #     <!-- -->
        # 
        #     .
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
        node_name: str = None,
        vul_list: List[DescribeNodePoolVulsResponseBodyVulRecordsVulList] = None,
    ):
        # The node ID.
        self.instance_id = instance_id
        # The node name. This name is the identifier of the node in the cluster.
        self.node_name = node_name
        # A list of vulnerabilities.
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
        if self.node_name is not None:
            result['node_name'] = self.node_name
        result['vul_list'] = []
        if self.vul_list is not None:
            for k in self.vul_list:
                result['vul_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('node_name') is not None:
            self.node_name = m.get('node_name')
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
        # The node pool vulnerabilities.
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
        pass

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
        # The action of the policy. Valid values:
        # 
        # *   `enforce`: blocks deployments that match the policy.
        # *   `inform`: generates alerts for deployments that match the policy.
        self.action = action
        # The type of the policy.
        self.category = category
        # The description of the policy.
        self.description = description
        # Indicates whether the policy is deleted. Valid values:
        # 
        # *   0: The policy is not deleted.
        # *   1: The policy is deleted.
        self.is_deleted = is_deleted
        # The name of the policy.
        self.name = name
        # Indicates whether parameters are required. Valid values:
        # 
        # *   0: Parameters are required.
        # *   1: Parameters are optional.
        self.no_config = no_config
        # The severity level of the policy.
        self.severity = severity
        # The content of the policy.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The policy type.
        self.constraint_kind = constraint_kind
        # The message that appears when an event is generated by a policy.
        self.msg = msg
        # The resource type.
        self.resource_kind = resource_kind
        # The resource name.
        self.resource_name = resource_name
        # The namespace to which the resource belongs.
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
        # The number of audit log entries.
        self.count = count
        # The audit log content.
        self.log = log
        # The status of the query. Valid values:
        # 
        # *   `Complete`: The query succeeded and the complete query result is returned.
        # *   `Incomplete`: The query succeeded but the query result is incomplete. To obtain the complete query result, you must repeat the request.
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
        # The number of policies that are enabled.
        self.enabled_count = enabled_count
        # The severity level of the policy.
        self.severity = severity
        # The total number of policies of the severity level.
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
        # The severity level of the policy.
        self.severity = severity
        # The number of blocking events that are triggered.
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
        # The severity level of the policy.
        self.severity = severity
        # The number of alerting events that are triggered.
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
        # Details about the blocking events that are triggered by the policies of each severity level.
        self.deny = deny
        # Details about the alerting events that are triggered by the policies of each severity level.
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
        # The policy description.
        self.policy_description = policy_description
        # The policy name.
        self.policy_name = policy_name
        # The severity level of the policy.
        self.severity = severity
        # The total number of blocking events that are triggered by the policy.
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
        # The policy description.
        self.policy_description = policy_description
        # The policy name.
        self.policy_name = policy_name
        # The severity level of the policy.
        self.severity = severity
        # The total number of alerting events that are triggered by the policy.
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
        # Details about the blocking events that are triggered by each policy.
        self.deny = deny
        # Details about the alerting events that are triggered by the policies of each severity level.
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
        # The audit logs of the policies in the cluster.
        self.admit_log = admit_log
        # Details about the policies of different severity levels that are enabled for the cluster.
        self.on_state = on_state
        # Details about the blocking and alerting events that are triggered by policies of different severity levels.
        self.total_violations = total_violations
        # Details about the blocking and alerting events that are triggered by different policies.
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
        # The name of the policy instance that you want to query.
        self.instance_name = instance_name
        # The name of the policy that you want to query.
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
        # The UID of the Alibaba Cloud account that is used to deploy the policy instance.
        self.ali_uid = ali_uid
        # The ID of the cluster.
        self.cluster_id = cluster_id
        # The name of the policy instance.
        self.instance_name = instance_name
        # The name of the policy.
        self.policy_name = policy_name
        # The type of policy.
        self.policy_category = policy_category
        # The description of the policy template.
        self.policy_description = policy_description
        # The parameters of the policy instance.
        self.policy_parameters = policy_parameters
        # The severity level of the policy instance.
        self.policy_severity = policy_severity
        # The applicable scope of the policy instance.
        # 
        # A value of \* indicates all namespaces in the cluster. This is the default value.
        # 
        # Multiple namespaces are separated by commas (,).
        self.policy_scope = policy_scope
        # The action of the policy. Valid values:
        # 
        # *   `deny`: Deployments that match the policy are denied.
        # *   `warn`: Alerts are generated for deployments that match the policy.
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
        # The policy type.
        self.policy_category = policy_category
        # The description of the policy.
        self.policy_description = policy_description
        # The number of policy instances that are deployed. If this parameter is empty, no policy instance is deployed.
        self.policy_instances_count = policy_instances_count
        # The name of the policy.
        self.policy_name = policy_name
        # The severity level of the policy.
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
        # Information about the number of policy instances of each severity level.
        self.instances_severity_count = instances_severity_count
        # Details about policy instances of different types.
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


class DescribeSubaccountK8sClusterUserConfigRequest(TeaModel):
    def __init__(
        self,
        private_ip_address: bool = None,
        temporary_duration_minutes: int = None,
    ):
        # Specifies whether to obtain the kubeconfig file used to connect to the cluster over the internal network. Valid values:
        # 
        # *   `true`: Obtain the kubeconfig file used to connect to the cluster over the internal network.
        # *   `false`: Obtain the kubeconfig file used to connect to the cluster over the Internet.
        # 
        # Default value: `false`.
        self.private_ip_address = private_ip_address
        # The validity period of the temporary kubeconfig file. Unit: minutes.
        # 
        # Valid values: 15 to 4320 (three days).
        # 
        # > If you leave this parameter empty, the system sets a longer validity period and returns the value in the expiration parameter of the response.
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


class DescribeSubaccountK8sClusterUserConfigResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        expiration: str = None,
    ):
        # The cluster kubeconfig file. For more information about the content of the kubeconfig file, see [Configure cluster credentials](~~86494~~).
        self.config = config
        # The expiration date of the kubeconfig file. The value is the UTC time displayed in RFC3339 format.
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


class DescribeSubaccountK8sClusterUserConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeSubaccountK8sClusterUserConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = DescribeSubaccountK8sClusterUserConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInfoResponseBodyError(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
    ):
        # The error code returned.
        self.code = code
        # The error message returned.
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
        # The action of the event.
        self.action = action
        # The severity level of the event.
        self.level = level
        # The message about the event.
        self.message = message
        # The cause of the event.
        self.reason = reason
        # The source of the event.
        self.source = source
        # The timestamp when the event was generated.
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
        # The end time of the stage.
        self.end_time = end_time
        # The message about the stage.
        self.message = message
        # The output generated at the stage.
        self.outputs = outputs
        # The start time of the stage.
        self.start_time = start_time
        # The status of the stage.
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
        # The ID of the object.
        self.id = id
        # The type of the object.
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
        # The resources that are managed by the task. For a scale-out task, the value of this parameter is the ID of the instance that is added by the task.
        self.data = data
        # The status of the scale-out task. Valid values:
        # 
        # *   `success`: The scale-out task is successful.
        # *   `success`: The scale-out task failed.
        # *   `initial`: The scale-out task is being initialized.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The time when the task was created.
        self.created = created
        # The current stage of the task.
        self.current_stage = current_stage
        # The error returned for the task.
        self.error = error
        # The event generated by the task.
        self.events = events
        # The task parameters.
        self.parameters = parameters
        # Detailed information about the stage of the task.
        self.stages = stages
        # The status of the task. Valid values:
        # 
        # *   `running`: The task is running.
        # *   `failed`: The task failed.
        # *   `success`: The task is complete.
        self.state = state
        # The object of the task.
        self.target = target
        # The task ID.
        self.task_id = task_id
        # The execution details of the task.
        self.task_result = task_result
        # The task type. A value of `cluster_scaleout` indicates a scale-out task.
        self.task_type = task_type
        # The time when the task was updated.
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
        # The type of template. The value can be a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. Container Service for Swarm is deprecated.
        # *   If the value of the parameter is not `kubernetes`, the template is not displayed on the Templates page in the console. We recommend that you set the parameter to `kubernetes`.
        # 
        # Default value: `kubernetes`.
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
        # The ID of the template. When you update a template, a new template ID is generated.
        self.id = id
        # The access control policy of the template.
        self.acl = acl
        # The name of the template.
        self.name = name
        # The template content in the YAML format.
        self.template = template
        # The type of template. The value can be a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. Container Service for Swarm is deprecated.
        # *   If the value of the parameter is not `kubernetes`, the template is not displayed on the Templates page in the console. We recommend that you set the parameter to `kubernetes`.
        # 
        # Default value: `kubernetes`.
        self.template_type = template_type
        # The description of the template.
        self.description = description
        # The label of the template.
        self.tags = tags
        # The unique ID of the template. The value remains unchanged after the template is updated.
        self.template_with_hist_id = template_with_hist_id
        # The time when the template was created.
        self.created = created
        # The time when the template was updated.
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
        # The page number.
        # 
        # Default value: 1.
        self.page_num = page_num
        # The number of entries per page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The type of template. This parameter can be set to a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If you set the parameter to `compose`, the template is not displayed on the Templates page in the console.
        # 
        # Default value: `kubernetes`.
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
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
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
        # The access control policy of the template. Valid values:
        # 
        # *   `private`: The template is private.
        # *   `public`: The template is public.
        # *   `shared`: The template can be shared.
        # 
        # Default value: `private`.
        self.acl = acl
        # The time when the template was created.
        self.created = created
        # The description of the template.
        self.description = description
        # The ID of the template.
        self.id = id
        # The name of the template.
        self.name = name
        # The label of the template. By default, the value is the name of the template.
        self.tags = tags
        # The template content in the YAML format.
        self.template = template
        # The type of template. This parameter can be set to a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. However, Container Service for Swarm is deprecated.
        self.template_type = template_type
        # The ID of the parent template. The value of `template_with_hist_id` is the same for each template version. This allows you to manage different template versions.
        self.template_with_hist_id = template_with_hist_id
        # The time when the template was updated.
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
        # The pagination information.
        self.page_info = page_info
        # The list of returned templates.
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
        # The application name.
        self.name = name
        # The namespace to which the application belongs.
        self.namespace = namespace
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        # 
        # If you do not set this parameter, triggers are not filtered by type.
        self.type = type
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        # 
        # If you do not specify this parameter, triggers are not filtered by action.
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
        # The ID of the trigger.
        self.id = id
        # The name of the trigger.
        self.name = name
        # The ID of the associated cluster.
        self.cluster_id = cluster_id
        # The name of the project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`. Example: default/test-app.
        self.project_id = project_id
        # The type of trigger.
        # 
        # Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        self.type = type
        # The action that the trigger performs. The value is set to redeploy.
        # 
        # `redeploy`: redeploys the resource specified by project_id.
        self.action = action
        # The token information.
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


class DescribeUserClusterNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[str] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        pass

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
        # The authorization setting. Valid values:
        # 
        # *   `{cluster_id}` is returned if the permissions are scoped to a cluster.
        # *   `{cluster_id}/{namespace}` is returned if the permissions are scoped to a namespace of a cluster.
        # *   `all-clusters` is returned if the permissions are scoped to all clusters.
        self.resource_id = resource_id
        # The authorization type. Valid values:
        # 
        # *   `cluster`: indicates that the permissions are scoped to a cluster.
        # *   `namespace`: indicates that the permissions are scoped to a namespace of a cluster.
        # *   `console`: indicates that the permissions are scoped to all clusters. This value was displayed only in the console.
        self.resource_type = resource_type
        # The name of the custom role. If a custom role is assigned, the value is the name of the assigned custom role.
        self.role_name = role_name
        # The type of predefined role. Valid values:
        # 
        # *   `admin`: administrator
        # *   `ops`: O\&M engineer
        # *   `dev`: developer
        # *   `restricted`: restricted user
        # *   `custom`: custom role
        self.role_type = role_type
        # Indicates whether the permissions are granted to the cluster owner.
        # 
        # *   `0`: indicates that the permissions are not granted to the cluster owner.
        # *   `1`: indicates that the permissions are granted to the cluster owner. The cluster owner is the administrator.
        self.is_owner = is_owner
        # Indicates whether the permissions are granted to the RAM role. Valid values:
        # 
        # *   `0`: indicates that the permissions are not granted to the RAM role.
        # *   `1`: indicates that the permissions are granted to the RAM role.
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


class DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota(TeaModel):
    def __init__(
        self,
        bandwidth: int = None,
        count: int = None,
        period: int = None,
    ):
        # The maximum bandwidth of each enhanced node pool. Unit: Mbit/s.
        self.bandwidth = bandwidth
        # The quota of enhanced edge node pools that belong to an Alibaba Cloud account.
        self.count = count
        # The maximum subscription duration of an enhanced edge node pool. Unit: months.
        # 
        # > You can ignore this parameter because enhanced edge node pools are pay-as-you-go resources.
        self.period = period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bandwidth is not None:
            result['bandwidth'] = self.bandwidth
        if self.count is not None:
            result['count'] = self.count
        if self.period is not None:
            result['period'] = self.period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bandwidth') is not None:
            self.bandwidth = m.get('bandwidth')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('period') is not None:
            self.period = m.get('period')
        return self


class DescribeUserQuotaResponseBody(TeaModel):
    def __init__(
        self,
        amk_cluster_quota: int = None,
        ask_cluster_quota: int = None,
        cluster_nodepool_quota: int = None,
        cluster_quota: int = None,
        edge_improved_nodepool_quota: DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota = None,
        node_quota: int = None,
        quotas: Dict[str, QuotasValue] = None,
    ):
        # The quota of Container Service for Kubernetes (ACK) managed clusters. Default value: 20. If the default quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.amk_cluster_quota = amk_cluster_quota
        # The quota of ACK Serverless clusters. Default value: 20. If the default quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.ask_cluster_quota = ask_cluster_quota
        # The quota of node pools in an ACK cluster. Default value: 20. If the default quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.cluster_nodepool_quota = cluster_nodepool_quota
        # The quota of clusters that belong to an Alibaba Cloud account. Default value: 50. If the default quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.cluster_quota = cluster_quota
        # The quota of enhanced edge node pools.
        self.edge_improved_nodepool_quota = edge_improved_nodepool_quota
        # The quota of nodes in an ACK cluster. Default value: 100. If the default quota limit is reached, submit an application in the [Quota Center console](https://quotas.console.aliyun.com/products/csk/quotas) to increase the quota.
        self.node_quota = node_quota
        # Information about the new quota.
        self.quotas = quotas

    def validate(self):
        if self.edge_improved_nodepool_quota:
            self.edge_improved_nodepool_quota.validate()
        if self.quotas:
            for v in self.quotas.values():
                if v:
                    v.validate()

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
        if self.edge_improved_nodepool_quota is not None:
            result['edge_improved_nodepool_quota'] = self.edge_improved_nodepool_quota.to_map()
        if self.node_quota is not None:
            result['node_quota'] = self.node_quota
        result['quotas'] = {}
        if self.quotas is not None:
            for k, v in self.quotas.items():
                result['quotas'][k] = v.to_map()
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
        if m.get('edge_improved_nodepool_quota') is not None:
            temp_model = DescribeUserQuotaResponseBodyEdgeImprovedNodepoolQuota()
            self.edge_improved_nodepool_quota = temp_model.from_map(m['edge_improved_nodepool_quota'])
        if m.get('node_quota') is not None:
            self.node_quota = m.get('node_quota')
        self.quotas = {}
        if m.get('quotas') is not None:
            for k, v in m.get('quotas').items():
                temp_model = QuotasValue()
                self.quotas[k] = temp_model.from_map(v)
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The time when the workflow was created.
        self.create_time = create_time
        # The name of the workflow.
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
        # The list of jobs.
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
        # The timeout period of sessions. Unit: seconds.
        self.expired = expired
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The options that you want to configure.
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
        # The ID of the cloud-native box.
        self.edge_machine_id = edge_machine_id
        # The request ID.
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
        # The maximum number of nodes that can be patched in parallel. The minimum value is 1. The maximum value equals the number of nodes in the node pool.
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
        auto_restart: bool = None,
        nodes: List[str] = None,
        rollout_policy: FixNodePoolVulsRequestRolloutPolicy = None,
        vuls: List[str] = None,
    ):
        self.auto_restart = auto_restart
        # The names of the nodes to be patched.
        self.nodes = nodes
        # The batch patching policy.
        self.rollout_policy = rollout_policy
        # The list of vulnerabilities.
        self.vuls = vuls

    def validate(self):
        if self.rollout_policy:
            self.rollout_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_restart is not None:
            result['auto_restart'] = self.auto_restart
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.rollout_policy is not None:
            result['rollout_policy'] = self.rollout_policy.to_map()
        if self.vuls is not None:
            result['vuls'] = self.vuls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_restart') is not None:
            self.auto_restart = m.get('auto_restart')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('rollout_policy') is not None:
            temp_model = FixNodePoolVulsRequestRolloutPolicy()
            self.rollout_policy = temp_model.from_map(m['rollout_policy'])
        if m.get('vuls') is not None:
            self.vuls = m.get('vuls')
        return self


class FixNodePoolVulsResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # The ID of the CVE patching task.
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


class GetClusterAddonInstanceResponseBodyLogging(TeaModel):
    def __init__(
        self,
        capable: bool = None,
        enabled: bool = None,
        log_project: str = None,
        logstore: str = None,
    ):
        self.capable = capable
        self.enabled = enabled
        self.log_project = log_project
        self.logstore = logstore

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.capable is not None:
            result['capable'] = self.capable
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.log_project is not None:
            result['log_project'] = self.log_project
        if self.logstore is not None:
            result['logstore'] = self.logstore
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('capable') is not None:
            self.capable = m.get('capable')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')
        if m.get('logstore') is not None:
            self.logstore = m.get('logstore')
        return self


class GetClusterAddonInstanceResponseBody(TeaModel):
    def __init__(
        self,
        config: str = None,
        logging: GetClusterAddonInstanceResponseBodyLogging = None,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        self.config = config
        self.logging = logging
        self.name = name
        self.state = state
        self.version = version

    def validate(self):
        if self.logging:
            self.logging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config
        if self.logging is not None:
            result['logging'] = self.logging.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.state is not None:
            result['state'] = self.state
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')
        if m.get('logging') is not None:
            temp_model = GetClusterAddonInstanceResponseBodyLogging()
            self.logging = temp_model.from_map(m['logging'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetClusterAddonInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterAddonInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetClusterAddonInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterCheckResponseBody(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        check_items: Dict[str, List[Dict[str, Any]]] = None,
        created_at: str = None,
        finished_at: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        # Id of the request
        self.check_id = check_id
        # The list of check items.
        self.check_items = check_items
        # The time when the cluster check task was created.
        self.created_at = created_at
        # The time when the cluster check task was completed.
        self.finished_at = finished_at
        # The message that indicates the status of the cluster check task.
        self.message = message
        # The status of the cluster check.
        self.status = status
        # The check method.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['check_id'] = self.check_id
        if self.check_items is not None:
            result['check_items'] = self.check_items
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.finished_at is not None:
            result['finished_at'] = self.finished_at
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_id') is not None:
            self.check_id = m.get('check_id')
        if m.get('check_items') is not None:
            self.check_items = m.get('check_items')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('finished_at') is not None:
            self.finished_at = m.get('finished_at')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetClusterCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterCheckResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = GetClusterCheckResponseBody()
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
        # The application name.
        self.name = name
        # The namespace name.
        self.namespace = namespace
        # The type of trigger. Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        # 
        # If you do not set this parameter, triggers are not filtered by type.
        self.type = type
        # The action that the trigger performs. Set the value to redeploy.
        # 
        # `redeploy`: redeploys the resources specified by `project_id`.
        # 
        # If you do not specify this parameter, triggers are not filtered by action.
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
        # The ID of the trigger.
        self.id = id
        # The name of the trigger.
        self.name = name
        # The ID of the associated cluster.
        self.cluster_id = cluster_id
        # The name of the project.
        # 
        # The name consists of the namespace where the application is deployed and the name of the application. The format is `${namespace}/${name}`. Example: default/test-app.
        self.project_id = project_id
        # The type of trigger.
        # 
        # Valid values:
        # 
        # *   `deployment`: performs actions on Deployments.
        # *   `application`: performs actions on applications that are deployed in Application Center.
        # 
        # Default value: `deployment`.
        self.type = type
        # The action that the trigger performs. The value is set to redeploy.
        # 
        # `redeploy`: redeploys the resource specified by project_id.
        self.action = action
        # Token
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
        # The description of the update task.
        self.message = message
        # The status of the update task. Valid values:
        # 
        # *   `running`: The update task is being executed.
        # *   `Success`: The update task is successfully executed.
        # *   `Failed`: The update task failed.
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
        # The error message returned during the update.
        self.error_message = error_message
        # The ID of the precheck report.
        self.precheck_report_id = precheck_report_id
        # The status of the update. Valid values:
        # 
        # *   `success`: The update is successful.
        # *   `fail`: The update failed.
        # *   `pause`: The update is paused.
        # *   `running`: The update is in progress.
        self.status = status
        # The current phase of the update. Valid values:
        # 
        # *   `not_start`: The update is not started.
        # *   `prechecking`: The precheck is in progress.
        # *   `upgrading`: The cluster is being updated.
        # *   `pause`: The update is paused.
        # *   `success`: The update is successful.
        self.upgrade_step = upgrade_step
        # The details of the update task.
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
        # The ID of the cluster that you want to manage.
        # 
        # *   When the `role_type` parameter is set to `all-clusters`, this parameter is set to an empty string.
        self.cluster = cluster
        # Specifies whether to perform a custom authorization. To perform a custom authorization, set `role_name` to a custom cluster role.
        self.is_custom = is_custom
        # Specifies whether the permissions are granted to a RAM role.
        self.is_ram_role = is_ram_role
        # The namespace to which the permissions are scoped. This parameter is required only if you set role_type to namespace.
        self.namespace = namespace
        # The predefined role name. Valid values:
        # 
        # *   `admin`: administrator
        # *   `ops`: O\&M engineer
        # *   `dev`: developer
        # *   `restricted`: restricted user
        # *   The custom cluster role.
        self.role_name = role_name
        # The authorization type. Valid values:
        # 
        # *   `cluster`: indicates that the permissions are scoped to a cluster.
        # *   `namespace`: specifies that the permissions are scoped to a namespace of a cluster.
        # *   `all-clusters`: specifies that the permissions are scoped to all clusters.
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
        # The request body.
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
        pass

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
        # The custom component settings that you want to use. The value is a JSON string.
        self.config = config
        # The component name.
        self.name = name
        # The component version.
        # 
        # >  You can call the [DescribeClusterAddonsVersion](~~197434~~) operation to query the version of a component.
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
        # The request body.
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
        pass

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


class ListAddonsRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_spec: str = None,
        cluster_type: str = None,
        cluster_version: str = None,
        profile: str = None,
        region_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_spec = cluster_spec
        self.cluster_type = cluster_type
        self.cluster_version = cluster_version
        self.profile = profile
        self.region_id = region_id

    def validate(self):
        pass

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
        if self.cluster_version is not None:
            result['cluster_version'] = self.cluster_version
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['region_id'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_spec') is not None:
            self.cluster_spec = m.get('cluster_spec')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('cluster_version') is not None:
            self.cluster_version = m.get('cluster_version')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        return self


class ListAddonsResponseBodyAddons(TeaModel):
    def __init__(
        self,
        architecture: List[str] = None,
        category: str = None,
        config_schema: str = None,
        install_by_default: bool = None,
        managed: bool = None,
        name: str = None,
        supported_actions: List[str] = None,
        version: str = None,
    ):
        self.architecture = architecture
        self.category = category
        self.config_schema = config_schema
        self.install_by_default = install_by_default
        self.managed = managed
        self.name = name
        self.supported_actions = supported_actions
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['architecture'] = self.architecture
        if self.category is not None:
            result['category'] = self.category
        if self.config_schema is not None:
            result['config_schema'] = self.config_schema
        if self.install_by_default is not None:
            result['install_by_default'] = self.install_by_default
        if self.managed is not None:
            result['managed'] = self.managed
        if self.name is not None:
            result['name'] = self.name
        if self.supported_actions is not None:
            result['supported_actions'] = self.supported_actions
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('architecture') is not None:
            self.architecture = m.get('architecture')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('config_schema') is not None:
            self.config_schema = m.get('config_schema')
        if m.get('install_by_default') is not None:
            self.install_by_default = m.get('install_by_default')
        if m.get('managed') is not None:
            self.managed = m.get('managed')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('supported_actions') is not None:
            self.supported_actions = m.get('supported_actions')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListAddonsResponseBody(TeaModel):
    def __init__(
        self,
        addons: List[ListAddonsResponseBodyAddons] = None,
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
                temp_model = ListAddonsResponseBodyAddons()
                self.addons.append(temp_model.from_map(k))
        return self


class ListAddonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddonsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListAddonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterAddonInstancesResponseBodyAddons(TeaModel):
    def __init__(
        self,
        name: str = None,
        state: str = None,
        version: str = None,
    ):
        self.name = name
        self.state = state
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
        if self.state is not None:
            result['state'] = self.state
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListClusterAddonInstancesResponseBody(TeaModel):
    def __init__(
        self,
        addons: List[ListClusterAddonInstancesResponseBodyAddons] = None,
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
                temp_model = ListClusterAddonInstancesResponseBodyAddons()
                self.addons.append(temp_model.from_map(k))
        return self


class ListClusterAddonInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterAddonInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListClusterAddonInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterChecksRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # The check method.
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


class ListClusterChecksResponseBodyChecks(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        created_at: str = None,
        finished_at: str = None,
        message: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the cluster check task.
        self.check_id = check_id
        # The time when the cluster check task was created.
        self.created_at = created_at
        # The time when the cluster check task was completed.
        self.finished_at = finished_at
        # The message that indicates the status of the cluster check task.
        self.message = message
        # The status of the cluster check.
        self.status = status
        # The check method.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['check_id'] = self.check_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.finished_at is not None:
            result['finished_at'] = self.finished_at
        if self.message is not None:
            result['message'] = self.message
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_id') is not None:
            self.check_id = m.get('check_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('finished_at') is not None:
            self.finished_at = m.get('finished_at')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListClusterChecksResponseBody(TeaModel):
    def __init__(
        self,
        checks: List[ListClusterChecksResponseBodyChecks] = None,
    ):
        # The list of check items.
        self.checks = checks

    def validate(self):
        if self.checks:
            for k in self.checks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['checks'] = []
        if self.checks is not None:
            for k in self.checks:
                result['checks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.checks = []
        if m.get('checks') is not None:
            for k in m.get('checks'):
                temp_model = ListClusterChecksResponseBodyChecks()
                self.checks.append(temp_model.from_map(k))
        return self


class ListClusterChecksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterChecksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListClusterChecksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationPlansRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
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
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListOperationPlansResponseBodyPlans(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        created: str = None,
        end_time: str = None,
        plan_id: str = None,
        start_time: str = None,
        state: str = None,
        target_id: str = None,
        target_type: str = None,
        type: str = None,
    ):
        self.cluster_id = cluster_id
        self.created = created
        self.end_time = end_time
        self.plan_id = plan_id
        self.start_time = start_time
        self.state = state
        self.target_id = target_id
        self.target_type = target_type
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
        if self.created is not None:
            result['created'] = self.created
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.plan_id is not None:
            result['plan_id'] = self.plan_id
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.state is not None:
            result['state'] = self.state
        if self.target_id is not None:
            result['target_id'] = self.target_id
        if self.target_type is not None:
            result['target_type'] = self.target_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('plan_id') is not None:
            self.plan_id = m.get('plan_id')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('target_id') is not None:
            self.target_id = m.get('target_id')
        if m.get('target_type') is not None:
            self.target_type = m.get('target_type')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListOperationPlansResponseBody(TeaModel):
    def __init__(
        self,
        plans: List[ListOperationPlansResponseBodyPlans] = None,
    ):
        self.plans = plans

    def validate(self):
        if self.plans:
            for k in self.plans:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['plans'] = []
        if self.plans is not None:
            for k in self.plans:
                result['plans'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.plans = []
        if m.get('plans') is not None:
            for k in m.get('plans'):
                temp_model = ListOperationPlansResponseBodyPlans()
                self.plans.append(temp_model.from_map(k))
        return self


class ListOperationPlansResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListOperationPlansResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ListOperationPlansResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The list of cluster IDs.
        self.resource_ids = resource_ids
        # The resource type. Set the value to `CLUSTER`.
        self.resource_type = resource_type
        # The list of labels that you want to query. You can specify at most 20 labels.
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
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID.
        self.region_id = region_id
        # The list of cluster IDs.
        self.resource_ids_shrink = resource_ids_shrink
        # The resource type. Set the value to `CLUSTER`.
        self.resource_type = resource_type
        # The list of labels that you want to query. You can specify at most 20 labels.
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
        # The ID of the resource.
        self.resource_id = resource_id
        # The type of the resource. For more information, see [Labels](~~110425~~).
        self.resource_type = resource_type
        # The key of the label.
        self.tag_key = tag_key
        # The value of the label.
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
        # The resource and label.
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
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The details of the queried labels and resources.
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
        # The endpoint of the OSS bucket.
        self.oss_bucket_endpoint = oss_bucket_endpoint
        # The name of the Object Storage Service (OSS) bucket.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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


class ModifyClusterRequestOperationPolicyClusterAutoUpgrade(TeaModel):
    def __init__(
        self,
        channel: str = None,
        enabled: bool = None,
    ):
        self.channel = channel
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class ModifyClusterRequestOperationPolicy(TeaModel):
    def __init__(
        self,
        cluster_auto_upgrade: ModifyClusterRequestOperationPolicyClusterAutoUpgrade = None,
    ):
        self.cluster_auto_upgrade = cluster_auto_upgrade

    def validate(self):
        if self.cluster_auto_upgrade:
            self.cluster_auto_upgrade.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_auto_upgrade is not None:
            result['cluster_auto_upgrade'] = self.cluster_auto_upgrade.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_auto_upgrade') is not None:
            temp_model = ModifyClusterRequestOperationPolicyClusterAutoUpgrade()
            self.cluster_auto_upgrade = temp_model.from_map(m['cluster_auto_upgrade'])
        return self


class ModifyClusterRequestSystemEventsLogging(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        logging_project: str = None,
    ):
        # 是否开启系统事件存储。
        self.enabled = enabled
        # 系统事件存储的LogProject名称。
        self.logging_project = logging_project

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.logging_project is not None:
            result['logging_project'] = self.logging_project
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('logging_project') is not None:
            self.logging_project = m.get('logging_project')
        return self


class ModifyClusterRequest(TeaModel):
    def __init__(
        self,
        access_control_list: List[str] = None,
        api_server_eip: bool = None,
        api_server_eip_id: str = None,
        cluster_name: str = None,
        deletion_protection: bool = None,
        enable_rrsa: bool = None,
        ingress_domain_rebinding: bool = None,
        ingress_loadbalancer_id: str = None,
        instance_deletion_protection: bool = None,
        maintenance_window: MaintenanceWindow = None,
        operation_policy: ModifyClusterRequestOperationPolicy = None,
        resource_group_id: str = None,
        system_events_logging: ModifyClusterRequestSystemEventsLogging = None,
    ):
        # The network access control list (ACL) of the SLB instance associated with the API server if the cluster is a registered cluster.
        self.access_control_list = access_control_list
        # Specifies whether to associate an elastic IP address (EIP) with the cluster API server. This enables Internet access for the cluster. Valid values:
        # 
        # *   `true`: associates an EIP with the cluster API server.
        # *   `false`: does not associate an EIP with the cluster API server.
        self.api_server_eip = api_server_eip
        # The ID of the EIP that you want to associate with the cluster API server. The parameter takes effect only if `api_server_eip` is set to `true`.
        self.api_server_eip_id = api_server_eip_id
        # The cluster name.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). The name cannot start with a hyphen (-).
        self.cluster_name = cluster_name
        # Specifies whether to enable deletion protection for the cluster. If deletion protection is enabled, the cluster cannot be deleted in the ACK console or by calling API operations. Valid values:
        # 
        # *   `true`: enables deletion protection for the cluster. This way, the cluster cannot be deleted in the ACK console or by calling API operations.
        # *   `false`: disables deletion protection for the cluster. This way, the cluster can be deleted in the ACK console or by calling API operations.
        # 
        # Default value: `false`.
        self.deletion_protection = deletion_protection
        # Specifies whether to enable the RAM Roles for Service Accounts (RRSA) feature. Valid values:
        # 
        # *   `true`: enables the RRSA feature.
        # *   `false`: disables the RRSA feature.
        self.enable_rrsa = enable_rrsa
        # Specifies whether to remap the test domain name of the cluster. Valid values:
        # 
        # *   `true`: remaps the test domain name of the cluster.
        # *   `false`: does not remap the test domain name of the cluster.
        # 
        # Default value: `false`.
        self.ingress_domain_rebinding = ingress_domain_rebinding
        # The ID of the Server Load Balancer (SLB) instance that is associated with the cluster.
        self.ingress_loadbalancer_id = ingress_loadbalancer_id
        # Specifies whether to enable deletion protection for the instances in the cluster. If deletion protection is enabled, the instances in the cluster cannot be deleted in the console or by calling the API. Valid values:
        # 
        # *   `true`: enables deletion protection for the instances in the cluster. You cannot delete the instances in the cluster in the console or by calling the API.
        # *   `false`: disables deletion protection for the instances in the cluster. You can delete the instances in the cluster in the console or by calling the API.
        # 
        # Default value: `false`.
        self.instance_deletion_protection = instance_deletion_protection
        # The maintenance window of the cluster. This parameter takes effect only in ACK Pro clusters.
        self.maintenance_window = maintenance_window
        self.operation_policy = operation_policy
        # The ID of the resource group to which the cluster belongs.
        self.resource_group_id = resource_group_id
        # 系统事件存储配置。
        self.system_events_logging = system_events_logging

    def validate(self):
        if self.maintenance_window:
            self.maintenance_window.validate()
        if self.operation_policy:
            self.operation_policy.validate()
        if self.system_events_logging:
            self.system_events_logging.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_control_list is not None:
            result['access_control_list'] = self.access_control_list
        if self.api_server_eip is not None:
            result['api_server_eip'] = self.api_server_eip
        if self.api_server_eip_id is not None:
            result['api_server_eip_id'] = self.api_server_eip_id
        if self.cluster_name is not None:
            result['cluster_name'] = self.cluster_name
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
        if self.operation_policy is not None:
            result['operation_policy'] = self.operation_policy.to_map()
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.system_events_logging is not None:
            result['system_events_logging'] = self.system_events_logging.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_control_list') is not None:
            self.access_control_list = m.get('access_control_list')
        if m.get('api_server_eip') is not None:
            self.api_server_eip = m.get('api_server_eip')
        if m.get('api_server_eip_id') is not None:
            self.api_server_eip_id = m.get('api_server_eip_id')
        if m.get('cluster_name') is not None:
            self.cluster_name = m.get('cluster_name')
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
        if m.get('operation_policy') is not None:
            temp_model = ModifyClusterRequestOperationPolicy()
            self.operation_policy = temp_model.from_map(m['operation_policy'])
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('system_events_logging') is not None:
            temp_model = ModifyClusterRequestSystemEventsLogging()
            self.system_events_logging = temp_model.from_map(m['system_events_logging'])
        return self


class ModifyClusterResponseBody(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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
        # The custom parameter settings that you want to use.
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
        pass

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
        # The name of the configuration item.
        self.key = key
        # The value of the configuration item.
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
        # The custom configuration.
        self.configs = configs
        # The name of the component.
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
        # The custom configuration.
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
        pass

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
        # The maximum bandwidth of the elastic IP address (EIP).
        self.eip_bandwidth = eip_bandwidth
        # The metering method of the EIP. Valid values:
        # 
        # *   `PayByBandwidth`: pay-by-bandwidth.
        # *   `PayByTraffic`: pay-by-data-transfer.
        # 
        # Default value: `PayByBandwidth`.
        self.eip_internet_charge_type = eip_internet_charge_type
        # Specifies whether to enable auto scaling. Valid values:
        # 
        # *   `true`: enables auto scaling for the node pool.
        # *   `false`: disables auto scaling for the node pool. If you set this parameter to false, other parameters in the `auto_scaling` section do not take effect.
        # 
        # Default value: `false`.
        self.enable = enable
        # Specifies whether to associate an EIP with the node pool. Valid values:
        # 
        # *   `true`: associates an EIP with the node pool.
        # *   `false`: does not associate an EIP with the node pool.
        # 
        # Default value: `false`.
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
        # *   `spot`: preemptible instance
        # 
        # Default value: `cpu`.
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
        unschedulable: bool = None,
        user_data: str = None,
    ):
        # Specifies whether to install the CloudMonitor agent on ECS nodes. After the CloudMonitor agent is installed on ECS nodes, you can view monitoring information about the instances in the CloudMonitor console. We recommend that you install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent on ECS nodes.
        # *   `false`: does not install the CloudMonitor agent on ECS nodes.
        # 
        # Default value: `false`.
        self.cms_enabled = cms_enabled
        # The CPU management policy of the nodes in the node pool. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: allows pods with specific resource characteristics on the node to be granted enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # The labels of the nodes in the node pool. You can add labels to the nodes in the cluster. You must add labels based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add at most 20 labels.
        # *   The key must be unique and cannot exceed 64 characters in length. The value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with `aliyun`, `acs:`, `https://`, or `http://`. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.labels = labels
        # The name of the container runtime.
        self.runtime = runtime
        # The version of the container runtime.
        self.runtime_version = runtime_version
        # The configurations of node taints.
        self.taints = taints
        self.unschedulable = unschedulable
        # The user-defined data of the node pool. For more information, see [Prepare user data](~~49121~~).
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
        if m.get('unschedulable') is not None:
            self.unschedulable = m.get('unschedulable')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        return self


class ModifyClusterNodePoolRequestManagementAutoRepairPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
    ):
        # Specifies whether ACK is allowed to automatically restart nodes after patching CVE vulnerabilities. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.restart_node = restart_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.restart_node is not None:
            result['restart_node'] = self.restart_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('restart_node') is not None:
            self.restart_node = m.get('restart_node')
        return self


class ModifyClusterNodePoolRequestManagementAutoUpgradePolicy(TeaModel):
    def __init__(
        self,
        auto_upgrade_kubelet: bool = None,
    ):
        # Specifies whether ACK is allowed to automatically update the kubelet. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.auto_upgrade_kubelet = auto_upgrade_kubelet

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_upgrade_kubelet is not None:
            result['auto_upgrade_kubelet'] = self.auto_upgrade_kubelet
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_upgrade_kubelet') is not None:
            self.auto_upgrade_kubelet = m.get('auto_upgrade_kubelet')
        return self


class ModifyClusterNodePoolRequestManagementAutoVulFixPolicy(TeaModel):
    def __init__(
        self,
        restart_node: bool = None,
        vul_level: str = None,
    ):
        # Specifies whether ACK is allowed to automatically restart nodes after patching CVE vulnerabilities. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.restart_node = restart_node
        # The severity levels of vulnerabilities that ACK is allowed to automatically patch. Multiple severity levels are separated by commas (,).
        self.vul_level = vul_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestManagementUpgradeConfig(TeaModel):
    def __init__(
        self,
        auto_upgrade: bool = None,
        max_unavailable: int = None,
        surge: int = None,
        surge_percentage: int = None,
    ):
        # Specifies whether to enable auto update.
        # 
        # *   true: enables auto update.
        # *   false: disables auto update.
        # 
        # Default value: `true`.
        self.auto_upgrade = auto_upgrade
        # The maximum number of nodes that can be in the Unavailable state.
        # 
        # Valid values: 1 to 1000.
        # 
        # Default value: 1.
        self.max_unavailable = max_unavailable
        # The number of nodes that are temporarily added to the node pool during an auto update. Additional nodes are used to host the workloads of nodes that are being updated.
        # 
        # >  We recommend that you set the number of additional nodes to a value that does not exceed the current number of existing nodes.
        self.surge = surge
        # The percentage of additional nodes to the nodes in the node pool. You must set this parameter or `surge`.
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
        auto_repair_policy: ModifyClusterNodePoolRequestManagementAutoRepairPolicy = None,
        auto_upgrade: bool = None,
        auto_upgrade_policy: ModifyClusterNodePoolRequestManagementAutoUpgradePolicy = None,
        auto_vul_fix: bool = None,
        auto_vul_fix_policy: ModifyClusterNodePoolRequestManagementAutoVulFixPolicy = None,
        enable: bool = None,
        upgrade_config: ModifyClusterNodePoolRequestManagementUpgradeConfig = None,
    ):
        # Specifies whether to enable auto repair. This parameter takes effect only when you specify `enable=true`. Valid values:
        # 
        # *   `true`: enables auto repair.
        # *   `false`: disables auto repair.
        # 
        # Default value: `true`.
        self.auto_repair = auto_repair
        # The auto node repair policy.
        self.auto_repair_policy = auto_repair_policy
        # Specifies whether to enable auto update. Valid values:
        # 
        # *   `true`: enables auto update.
        # *   `false`: disables auto update.
        self.auto_upgrade = auto_upgrade
        # The auto update policy.
        self.auto_upgrade_policy = auto_upgrade_policy
        # Specifies whether ACK is allowed to automatically patch CVE vulnerabilities. Valid values:
        # 
        # *   `true`: yes
        # *   `false`: no
        self.auto_vul_fix = auto_vul_fix
        # The auto CVE patching policy.
        self.auto_vul_fix_policy = auto_vul_fix_policy
        # Specifies whether to enable the managed node pool feature. Valid values:
        # 
        # *   `true`: enables the managed node pool feature.
        # *   `false`: disables the managed node pool feature. Other parameters in this section take effect only when `enable=true` is specified.
        # 
        # Default value: `false`.
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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
            temp_model = ModifyClusterNodePoolRequestManagementAutoRepairPolicy()
            self.auto_repair_policy = temp_model.from_map(m['auto_repair_policy'])
        if m.get('auto_upgrade') is not None:
            self.auto_upgrade = m.get('auto_upgrade')
        if m.get('auto_upgrade_policy') is not None:
            temp_model = ModifyClusterNodePoolRequestManagementAutoUpgradePolicy()
            self.auto_upgrade_policy = temp_model.from_map(m['auto_upgrade_policy'])
        if m.get('auto_vul_fix') is not None:
            self.auto_vul_fix = m.get('auto_vul_fix')
        if m.get('auto_vul_fix_policy') is not None:
            temp_model = ModifyClusterNodePoolRequestManagementAutoVulFixPolicy()
            self.auto_vul_fix_policy = temp_model.from_map(m['auto_vul_fix_policy'])
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
        # The name of the node pool.
        # 
        # The name must be 1 to 63 characters in length, and can contain digits, letters, and hyphens (-). It cannot start with a hyphen (-).
        self.name = name
        # The ID of the resource group to which the node pool belongs.
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


class ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions(TeaModel):
    def __init__(
        self,
        id: str = None,
        match_criteria: str = None,
    ):
        # The ID of the private node pool.
        self.id = id
        # The type of private node pool. This parameter specifies the type of private node pool that you want to use to create instances. A private node pool is generated when an elasticity assurance or a capacity reservation service takes effect. The system selects a private node pool to launch instances. Valid values:
        # 
        # *   `Open`: specifies an open private node pool. The system selects an open private node pool to launch instances. If no matching open private node pool is available, the resources in the public node pool are used.
        # *   `Target`: specifies a private node pool. The system uses the resources of the specified private node pool to launch instances. If the specified private node pool is unavailable, instances cannot be launched.
        # *   `None`: no private node pool is used. The resources of private node pools are not used to launch the instances.
        self.match_criteria = match_criteria

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit(TeaModel):
    def __init__(
        self,
        instance_type: str = None,
        price_limit: str = None,
    ):
        # The instance type of preemptible instances.
        self.instance_type = instance_type
        # The maximum bid price of a preemptible instance.
        # 
        # Unit: USD/hour.
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
        private_pool_options: ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions = None,
        rds_instances: List[str] = None,
        scaling_policy: str = None,
        spot_instance_pools: int = None,
        spot_instance_remedy: bool = None,
        spot_price_limit: List[ModifyClusterNodePoolRequestScalingGroupSpotPriceLimit] = None,
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
        tags: List[Tag] = None,
        vswitch_ids: List[str] = None,
    ):
        # Specifies whether to enable auto-renewal for the nodes in the node pool. This parameter takes effect only when you set `instance_charge_type` to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.auto_renew = auto_renew
        # The duration of the auto-renewal. This parameter takes effect and is required only when you set `instance_charge_type` to `PrePaid`.
        # 
        # If you specify `PeriodUnit=Month`, the valid values are 1, 2, 3, 6, and 12.
        self.auto_renew_period = auto_renew_period
        # Specifies whether to automatically create pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created due to reasons such as the cost or insufficient inventory. This parameter takes effect when you set `multi_az_policy` to `COST_OPTIMIZED`. Valid values:
        # 
        # *   `true`: automatically creates pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created.
        # *   `false`: does not create pay-as-you-go instances to meet the required number of ECS instances if preemptible instances cannot be created.
        self.compensate_with_on_demand = compensate_with_on_demand
        # The configurations of the data disks that are mounted to the nodes in the node pool. You can mount 0 to 10 data disks. You can mount at most 10 data disks to the nodes in the node pool.
        self.data_disks = data_disks
        # The expected number of nodes in the node pool.
        self.desired_size = desired_size
        # The ID of the custom image. You can call the `DescribeKubernetesVersionMetadata` operation to query the supported images. By default, the latest image is used.
        self.image_id = image_id
        self.image_type = image_type
        # The billing method of the nodes in the node pool. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go.
        # 
        # Default value: `PostPaid`.
        self.instance_charge_type = instance_charge_type
        # A list of instance types. You can select multiple instance types. When the system needs to create a node, it starts from the first instance type until the node is created. The instance type that is used to create the node varies based on the actual instance stock.
        self.instance_types = instance_types
        # The metering method of the public IP address. Valid values:
        # 
        # *   `PayByBandwidth`: pay-by-bandwidth.
        # *   `PayByTraffic`: pay-by-data-transfer.
        self.internet_charge_type = internet_charge_type
        # The maximum outbound bandwidth of the public IP address of the node. Unit: Mbit/s. Valid values: 1 to 100.
        self.internet_max_bandwidth_out = internet_max_bandwidth_out
        # The name of the key pair. You must set this parameter or the `login_password` parameter. You must set `key_pair` if the node pool is a managed node pool.
        self.key_pair = key_pair
        # The password for SSH logon. You must set this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # The ECS instance scaling policy for a multi-zone scaling group. Valid values:
        # 
        # *   `PRIORITY`: The scaling group is scaled based on the VSwitchIds.N parameter. If an ECS instance cannot be created in the zone where the vSwitch that has the highest priority resides, Auto Scaling creates the ECS instance in the zone where the vSwitch that has the next highest priority resides.
        # 
        # *   `COST_OPTIMIZED`: ECS instances are created based on the vCPU unit price in ascending order. Preemptible instances are preferably created when preemptible instance types are specified in the scaling configuration. You can set the `CompensateWithOnDemand` parameter to specify whether to automatically create pay-as-you-go instances when preemptible instances cannot be created due to insufficient resources.
        # 
        #     **\
        # 
        #     **Note** `COST_OPTIMIZED` is valid only when multiple instance types are specified or at least one preemptible instance type is specified.
        # 
        # *   `BALANCE`: ECS instances are evenly distributed across multiple zones specified by the scaling group. If ECS instances become imbalanced among multiple zones due to insufficient inventory, you can call the `RebalanceInstances` operation of Auto Scaling to balance the instance distribution among zones. For more information, see [RebalanceInstances](~~71516~~).
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
        # The billing cycle of the nodes in the node pool. This parameter is required if you set `instance_charge_type` to `PrePaid`.
        # 
        # The billing cycle is measured only in months.
        # 
        # Default value: `Month`.
        self.period_unit = period_unit
        # The operating system. Valid values:
        # 
        # *   `AliyunLinux`
        # *   `CentOS`
        # *   `Windows`
        # *   `WindowsCore`
        self.platform = platform
        # The configuration of the private node pool.
        self.private_pool_options = private_pool_options
        # A list of ApsaraDB RDS instances.
        self.rds_instances = rds_instances
        # The scaling mode of the scaling group. Valid values:
        # 
        # *   `release`: the standard mode. ECS instances are created and released based on resource usage.
        # *   `recycle`: the swift mode. ECS instances are created, stopped, or started during scaling events. This reduces the time required for the next scale-out event. When the instance is stopped, you are charged only for the storage service. This does not apply to ECS instances that are attached with local disks.
        self.scaling_policy = scaling_policy
        # The number of instance types that are available for creating preemptible instances. Auto Scaling creates preemptible instances of multiple instance types that are available at the lowest cost. Valid values: 1 to 10.
        self.spot_instance_pools = spot_instance_pools
        # Specifies whether to supplement preemptible instances. If this parameter is set to true, when the scaling group receives a system message that a preemptible instance is to be reclaimed, the scaling group attempts to create a new instance to replace this instance. Valid values:
        # 
        # *   `true`: enables the supplementation of preemptible instances.
        # *   `false`: disables the supplementation of preemptible instances.
        self.spot_instance_remedy = spot_instance_remedy
        # The bid configurations of preemptible instances.
        self.spot_price_limit = spot_price_limit
        # The bidding policy of preemptible instances. Valid values:
        # 
        # *   `NoSpot`: non-preemptible instance.
        # *   `SpotWithPriceLimit`: specifies the highest bid for the preemptible instance.
        # *   `SpotAsPriceGo`: automatically submits bids based on the up-to-date market price.
        # 
        # For more information, see [Preemptible instances](~~157759~~).
        self.spot_strategy = spot_strategy
        self.system_disk_bursting_enabled = system_disk_bursting_enabled
        self.system_disk_categories = system_disk_categories
        # The type of system disk. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # 
        # Default value: `cloud_ssd`.
        self.system_disk_category = system_disk_category
        self.system_disk_encrypt_algorithm = system_disk_encrypt_algorithm
        self.system_disk_encrypted = system_disk_encrypted
        self.system_disk_kms_key_id = system_disk_kms_key_id
        # The performance level (PL) of the system disk that you want to use for the node. This parameter takes effect only for enhanced SSDs. You can specify a higher PL if you increase the size of the system disk. For more information, see [ESSDs](~~122389~~).
        self.system_disk_performance_level = system_disk_performance_level
        self.system_disk_provisioned_iops = system_disk_provisioned_iops
        # The system disk size of a node. Unit: GiB.
        # 
        # Valid values: 20 to 500.
        # 
        # The value of this parameter must be at least 20 and greater than or equal to the size of the specified image.
        # 
        # The default value is the greater one between 40 and the image size.
        self.system_disk_size = system_disk_size
        # The labels that you want to add to the ECS instances.
        # 
        # The key must be unique and cannot exceed 128 characters in length. Neither keys nor values can start with aliyun or acs:. Neither keys nor values can contain https:// or http://.
        self.tags = tags
        # The vSwitch IDs. You can specify 1 to 20 vSwitches.
        # 
        # >  To ensure high availability, we recommend that you select vSwitches in different zones.
        self.vswitch_ids = vswitch_ids

    def validate(self):
        if self.data_disks:
            for k in self.data_disks:
                if k:
                    k.validate()
        if self.private_pool_options:
            self.private_pool_options.validate()
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
        if self.private_pool_options is not None:
            result['private_pool_options'] = self.private_pool_options.to_map()
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
        if m.get('private_pool_options') is not None:
            temp_model = ModifyClusterNodePoolRequestScalingGroupPrivatePoolOptions()
            self.private_pool_options = temp_model.from_map(m['private_pool_options'])
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
        # Specifies whether to enable confidential computing for the cluster. Valid values:
        # 
        # *   `true`: enables confidential computing for the cluster.
        # *   `false`: disables confidential computing for the cluster.
        # 
        # Default value: `false`.
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
        concurrency: bool = None,
        kubernetes_config: ModifyClusterNodePoolRequestKubernetesConfig = None,
        management: ModifyClusterNodePoolRequestManagement = None,
        nodepool_info: ModifyClusterNodePoolRequestNodepoolInfo = None,
        scaling_group: ModifyClusterNodePoolRequestScalingGroup = None,
        tee_config: ModifyClusterNodePoolRequestTeeConfig = None,
        update_nodes: bool = None,
    ):
        # The configuration of auto scaling.
        self.auto_scaling = auto_scaling
        self.concurrency = concurrency
        # The configuration of the cluster where the node pool is deployed.
        self.kubernetes_config = kubernetes_config
        # The configuration of the managed node pool feature.
        self.management = management
        # The configurations of the node pool.
        self.nodepool_info = nodepool_info
        # The configurations of the scaling group.
        self.scaling_group = scaling_group
        # The configurations about confidential computing for the cluster.
        self.tee_config = tee_config
        # Specifies whether to update node information, such as labels and taints.
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
            temp_model = ModifyClusterNodePoolRequestAutoScaling()
            self.auto_scaling = temp_model.from_map(m['auto_scaling'])
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
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
        request_id: str = None,
        task_id: str = None,
    ):
        # The node pool ID.
        self.nodepool_id = nodepool_id
        self.request_id = request_id
        # The task ID.
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
        # The data of the labels that you want to modify.
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
        pass

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


class ModifyNodePoolNodeConfigRequestRollingPolicy(TeaModel):
    def __init__(
        self,
        max_parallelism: int = None,
    ):
        # The maximum number of nodes in the Unschedulable state.
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
        kubelet_config: KubeletConfig = None,
        rolling_policy: ModifyNodePoolNodeConfigRequestRollingPolicy = None,
    ):
        # The kubelet configuration.
        self.kubelet_config = kubelet_config
        # The rotation configuration.
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
            temp_model = KubeletConfig()
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
        # The node pool ID.
        self.nodepool_id = nodepool_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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
        # The action of the policy. Valid values:
        # 
        # *   `deny`: Deployments that match the policy are denied.
        # *   `warn`: Alerts are generated for deployments that match the policy.
        self.action = action
        # The ID of the policy instance.
        self.instance_name = instance_name
        # The namespaces to which the policy is applied. The policy is applied to all namespaces if this parameter is left empty.
        self.namespaces = namespaces
        # The parameters of the policy instance. For more information, see [Predefined security policies of ACK](~~359819~~).
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
        # The list of policy instances that are updated.
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
        # The type of ACK service that you want to activate. Valid values:
        # 
        # *   `propayasgo`: ACK Pro
        # *   `edgepayasgo`: ACK Edge
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
        # The ID of the order.
        self.order_id = order_id
        # The request ID.
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
        pass

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
        pass

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
        pass

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
        # Specifies whether to evict all pods from the nodes that you want to remove.
        self.drain_node = drain_node
        # The list of nodes to be removed.
        self.nodes = nodes
        # Specifies whether to release the Elastic Compute Service (ECS) instances when they are removed from the cluster.
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
        pass

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


class RemoveNodePoolNodesRequest(TeaModel):
    def __init__(
        self,
        concurrency: bool = None,
        drain_node: bool = None,
        instance_ids: List[str] = None,
        nodes: List[str] = None,
        release_node: bool = None,
    ):
        # 是否并发移除。
        self.concurrency = concurrency
        # Specifies whether to drain the nodes that you want to remove. Valid values:
        # 
        # *   true: drain the nodes that you want to remove.
        # *   false: do not drain the nodes that you want to remove.
        self.drain_node = drain_node
        # A list of instances that you want to remove.
        self.instance_ids = instance_ids
        # A list of nodes that you want to remove.
        self.nodes = nodes
        # Specifies whether to release the nodes after they are removed. Valid values:
        # 
        # *   true: release the nodes after they are removed.
        # *   false: do not release the nodes after they are removed.
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.instance_ids is not None:
            result['instance_ids'] = self.instance_ids
        if self.nodes is not None:
            result['nodes'] = self.nodes
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('instance_ids') is not None:
            self.instance_ids = m.get('instance_ids')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class RemoveNodePoolNodesShrinkRequest(TeaModel):
    def __init__(
        self,
        concurrency: bool = None,
        drain_node: bool = None,
        instance_ids_shrink: str = None,
        nodes_shrink: str = None,
        release_node: bool = None,
    ):
        # 是否并发移除。
        self.concurrency = concurrency
        # Specifies whether to drain the nodes that you want to remove. Valid values:
        # 
        # *   true: drain the nodes that you want to remove.
        # *   false: do not drain the nodes that you want to remove.
        self.drain_node = drain_node
        # A list of instances that you want to remove.
        self.instance_ids_shrink = instance_ids_shrink
        # A list of nodes that you want to remove.
        self.nodes_shrink = nodes_shrink
        # Specifies whether to release the nodes after they are removed. Valid values:
        # 
        # *   true: release the nodes after they are removed.
        # *   false: do not release the nodes after they are removed.
        self.release_node = release_node

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrency is not None:
            result['concurrency'] = self.concurrency
        if self.drain_node is not None:
            result['drain_node'] = self.drain_node
        if self.instance_ids_shrink is not None:
            result['instance_ids'] = self.instance_ids_shrink
        if self.nodes_shrink is not None:
            result['nodes'] = self.nodes_shrink
        if self.release_node is not None:
            result['release_node'] = self.release_node
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('concurrency') is not None:
            self.concurrency = m.get('concurrency')
        if m.get('drain_node') is not None:
            self.drain_node = m.get('drain_node')
        if m.get('instance_ids') is not None:
            self.instance_ids_shrink = m.get('instance_ids')
        if m.get('nodes') is not None:
            self.nodes_shrink = m.get('nodes')
        if m.get('release_node') is not None:
            self.release_node = m.get('release_node')
        return self


class RemoveNodePoolNodesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
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


class RemoveNodePoolNodesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveNodePoolNodesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RemoveNodePoolNodesResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        pass

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
        auto_restart: bool = None,
        nodes: List[str] = None,
    ):
        self.auto_restart = auto_restart
        # The list of nodes. If you do not specify nodes, all nodes in the node pool are selected.
        self.nodes = nodes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_restart is not None:
            result['auto_restart'] = self.auto_restart
        if self.nodes is not None:
            result['nodes'] = self.nodes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_restart') is not None:
            self.auto_restart = m.get('auto_restart')
        if m.get('nodes') is not None:
            self.nodes = m.get('nodes')
        return self


class RepairClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The ID of the task.
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
        pass

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
        pass

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
        pass

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


class RunClusterCheckRequest(TeaModel):
    def __init__(
        self,
        options: Dict[str, str] = None,
        type: str = None,
    ):
        # The cluster check items.
        self.options = options
        # The check method.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.options is not None:
            result['options'] = self.options
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('options') is not None:
            self.options = m.get('options')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class RunClusterCheckResponseBody(TeaModel):
    def __init__(
        self,
        check_id: str = None,
        request_id: str = None,
    ):
        # The ID of the cluster check task.
        self.check_id = check_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_id is not None:
            result['check_id'] = self.check_id
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_id') is not None:
            self.check_id = m.get('check_id')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class RunClusterCheckResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunClusterCheckResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = RunClusterCheckResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        # The number of worker nodes that you want to add. You can add at most 500 nodes in one API call. The maximum number of nodes that can be added is limited by the quota of nodes in the cluster.
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
        # The task ID.
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
        # The ID of an automatic snapshot policy. Automatic backup is performed for a disk based on the specified automatic snapshot policy.
        # 
        # By default, this parameter is empty. This indicates that automatic backup is disabled.
        self.auto_snapshot_policy_id = auto_snapshot_policy_id
        # The data disk type.
        self.category = category
        # Specifies whether to encrypt the data disks. Valid values:
        # 
        # *   `true`: encrypts data disks.
        # *   `false`: does not encrypt data disks.
        # 
        # Default value: `false`.
        self.encrypted = encrypted
        # The size of the data disk. Valid values: 40 to 32767.
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
        # Specifies whether to install the CloudMonitor agent. Valid values:
        # 
        # *   `true`: installs the CloudMonitor agent.
        # *   `false`: does not install the CloudMonitor agent.
        # 
        # Default value: `false`.
        self.cloud_monitor_flags = cloud_monitor_flags
        # The number of worker nodes that you want to add.
        self.count = count
        # The CPU management policy. The following policies are supported if the Kubernetes version of the cluster is 1.12.6 or later.
        # 
        # *   `static`: This policy allows pods with specific resource characteristics on the node to be granted with enhanced CPU affinity and exclusivity.
        # *   `none`: specifies that the default CPU affinity is used.
        # 
        # Default value: `none`.
        self.cpu_policy = cpu_policy
        # Specifies a custom image for nodes. By default, the image provided by ACK is used. You can select a custom image to replace the default image. For more information, see [Custom images](~~146647~~).
        self.image_id = image_id
        # The name of the key pair. You must set this parameter or the `login_password` parameter.
        self.key_pair = key_pair
        # The password for SSH logon. You must set this parameter or the `key_pair` parameter. The password must be 8 to 30 characters in length, and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters.
        self.login_password = login_password
        # After you specify the list of RDS instances, the ECS instances in the cluster are automatically added to the whitelist of the RDS instances.
        self.rds_instances = rds_instances
        # The container runtime.
        self.runtime = runtime
        # The labels that you want to add to nodes. You must add labels based on the following rules:
        # 
        # *   Each label is a case-sensitive key-value pair. You can add up to 20 labels.
        # *   A key must be unique and cannot exceed 64 characters in length. A value can be empty and cannot exceed 128 characters in length. Keys and values cannot start with aliyun, acs:, https://, or http://. For more information, see [Labels and Selectors](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/#syntax-and-character-set).
        self.tags = tags
        # The taints that you want to add to nodes. Taints are added to nodes to prevent pods from being scheduled to inappropriate nodes. However, tolerations allow pods to be scheduled to nodes with matching taints. For more information, see [taint-and-toleration](https://kubernetes.io/zh/docs/concepts/scheduling-eviction/taint-and-toleration/).
        self.taints = taints
        # The user data of the node pool. For more information, see [Generate user-defined data](~~49121~~).
        self.user_data = user_data
        # The IDs of the vSwitches. You can select one to three vSwitches when you create a cluster. We recommend that you select vSwitches in different zones to ensure high availability.
        self.vswitch_ids = vswitch_ids
        # Specifies whether to enable auto-renewal for worker nodes. This parameter takes effect only if `worker_instance_charge_type` is set to `PrePaid`. Valid values:
        # 
        # *   `true`: enables auto-renewal.
        # *   `false`: disables auto-renewal.
        # 
        # Default value: `true`.
        self.worker_auto_renew = worker_auto_renew
        # The auto-renewal period for worker nodes after the subscriptions of worker nodes expire. This parameter takes effect and is required only if the subscription billing method is selected for worker nodes.
        # 
        # Valid values: 1, 2, 3, 6, and 12.
        # 
        # Default value: `1`.
        self.worker_auto_renew_period = worker_auto_renew_period
        # The configuration of the data disk that is mounted to worker nodes. The configuration includes the disk type and disk size.
        self.worker_data_disks = worker_data_disks
        # The billing method of worker nodes. Valid values:
        # 
        # *   `PrePaid`: subscription.
        # *   `PostPaid`: pay-as-you-go
        # 
        # Default value: `PostPaid`
        self.worker_instance_charge_type = worker_instance_charge_type
        # The instance configurations of worker nodes.
        self.worker_instance_types = worker_instance_types
        # The subscription duration of worker nodes. This parameter takes effect and is required only if `worker_instance_charge_type` is set to `PrePaid`.
        # 
        # Valid values: 1, 2, 3, 6, 12, 24, 36, 48, and 60.
        # 
        # Default value: 1.
        self.worker_period = worker_period
        # The billing cycle of worker nodes. This parameter is required if worker_instance_charge_type is set to `PrePaid`.
        # 
        # Set the value to `Month`. Worker nodes are billed only on a monthly basis.
        self.worker_period_unit = worker_period_unit
        # The type of system disk that you want to use for worker nodes. Valid values:
        # 
        # *   `cloud_efficiency`: ultra disk.
        # *   `cloud_ssd`: standard SSD.
        # *   `cloud_essd`: enhanced SSD (ESSD).
        # 
        # Default value: `cloud_ssd`.
        self.worker_system_disk_category = worker_system_disk_category
        # The size of the system disk that you want to use for worker nodes. Unit: GiB.
        # 
        # Valid values: 40 to 500.
        # 
        # Default value: `120`.
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
        # The cluster ID.
        self.cluster_id = cluster_id
        # The request ID.
        self.request_id = request_id
        # The task ID.
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


class ScanClusterVulsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
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


class ScanClusterVulsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanClusterVulsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = ScanClusterVulsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAlertResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        status: bool = None,
    ):
        # The message returned.
        self.msg = msg
        # The status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class StartAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAlertResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = StartAlertResponseBody()
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
        # The name of the output BAM file.
        self.mapping_bam_out_filename = mapping_bam_out_filename
        # The output path of the Binary Alignment Map (BAM) file.
        self.mapping_bam_out_path = mapping_bam_out_path
        # The name of the OSS bucket that stores the data of the mapping workflow.
        self.mapping_bucket_name = mapping_bucket_name
        # The name of the first FASTQ file of the mapping workflow.
        self.mapping_fastq_first_filename = mapping_fastq_first_filename
        # The path of the FASTQ files of the mapping workflow.
        self.mapping_fastq_path = mapping_fastq_path
        # The name of the second FASTQ file of the mapping workflow.
        self.mapping_fastq_second_filename = mapping_fastq_second_filename
        # Specifies whether to mark duplicate values.
        self.mapping_is_mark_dup = mapping_is_mark_dup
        # The region where the Object Storage Service (OSS) bucket that stores the data of the mapping workflow is deployed.
        self.mapping_oss_region = mapping_oss_region
        # The path of the reference files of the mapping workflow.
        self.mapping_reference_path = mapping_reference_path
        # The type of service-level agreement (SLA). Valid values:
        # 
        # *   s: the silver level (S-level). It requires 1 extra minute to process every 1.5 billion base pairs beyond the limit of 90 billion base pairs.
        # *   g: the gold level (G-level). It requires 1 extra minute to process every 2 billion base pairs beyond the limit of 90 billion base pairs.
        # *   p: the platinum level (P-level). It requires 1 extra minute to process every 3 billion base pairs beyond the limit of 90 billion base pairs.
        self.service = service
        # The name of the OSS bucket that stores the data of the WGS workflow.
        self.wgs_bucket_name = wgs_bucket_name
        # The name of the first FASTQ file of the WGS workflow.
        self.wgs_fastq_first_filename = wgs_fastq_first_filename
        # The path of the FASTQ files of the WGS workflow.
        self.wgs_fastq_path = wgs_fastq_path
        # The name of the second FASTQ file of the WGS workflow.
        self.wgs_fastq_second_filename = wgs_fastq_second_filename
        # The region where the OSS bucket that stores the data of the whole genome sequencing (WGS) workflow is deployed.
        self.wgs_oss_region = wgs_oss_region
        # The path of the reference files of the WGS workflow.
        self.wgs_reference_path = wgs_reference_path
        # The name of the output VCF file.
        self.wgs_vcf_out_filename = wgs_vcf_out_filename
        # The output path of the Variant Call Format (VCF) file.
        self.wgs_vcf_out_path = wgs_vcf_out_path
        # The type of workflow. Valid values: wgs and mapping.
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
        # The name of the workflow.
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


class StopAlertResponseBody(TeaModel):
    def __init__(
        self,
        msg: str = None,
        status: bool = None,
    ):
        # The error message returned if the call fails.
        self.msg = msg
        # The operation result. Valid values:
        # 
        # *   True: The operation is successful.
        # *   False: The operation failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class StopAlertResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StopAlertResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = StopAlertResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SyncClusterNodePoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class SyncClusterNodePoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SyncClusterNodePoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = SyncClusterNodePoolResponseBody()
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
        # The region ID of the resource.
        self.region_id = region_id
        # The IDs of the resources that you want to label.
        self.resource_ids = resource_ids
        # The type of resource that you want to label. Set the value to `CLUSTER`.
        self.resource_type = resource_type
        # The labels that you want to add to the resources in key-value pairs. You can add up to 20 labels. Note:
        # 
        # *   A value cannot be empty and can contain up to 128 characters.
        # *   A key or value must not start with `aliyun` or `acs:`.
        # *   A key or value must not contain `http://` or `https://`.
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
        # The request ID.
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
        cleanup_cloud_resources: bool = None,
        name: str = None,
    ):
        # Whether to clean up cloud resources.
        self.cleanup_cloud_resources = cleanup_cloud_resources
        # The component name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cleanup_cloud_resources is not None:
            result['cleanup_cloud_resources'] = self.cleanup_cloud_resources
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cleanup_cloud_resources') is not None:
            self.cleanup_cloud_resources = m.get('cleanup_cloud_resources')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UnInstallClusterAddonsRequest(TeaModel):
    def __init__(
        self,
        addons: List[UnInstallClusterAddonsRequestAddons] = None,
    ):
        # The list of components that you want to uninstall. The list is an array.
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
        pass

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
        # Specifies whether to remove all custom labels. This parameter takes effect only when `tag_keys` is left empty. Valid values:
        # 
        # *   `true`: Remove all custom labels.
        # *   `false`: Do not remove all custom labels.
        self.all = all
        # The region ID of the resources.
        self.region_id = region_id
        # The list of resource IDs.
        self.resource_ids = resource_ids
        # The type of resource. Set the value to `CLUSTER`.
        self.resource_type = resource_type
        # The list of keys of the labels that you want to remove.
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


class UntagResourcesShrinkRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_ids_shrink: str = None,
        resource_type: str = None,
        tag_keys_shrink: str = None,
    ):
        # Specifies whether to remove all custom labels. This parameter takes effect only when `tag_keys` is left empty. Valid values:
        # 
        # *   `true`: Remove all custom labels.
        # *   `false`: Do not remove all custom labels.
        self.all = all
        # The region ID of the resources.
        self.region_id = region_id
        # The list of resource IDs.
        self.resource_ids_shrink = resource_ids_shrink
        # The type of resource. Set the value to `CLUSTER`.
        self.resource_type = resource_type
        # The list of keys of the labels that you want to remove.
        self.tag_keys_shrink = tag_keys_shrink

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
        if self.resource_ids_shrink is not None:
            result['resource_ids'] = self.resource_ids_shrink
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.tag_keys_shrink is not None:
            result['tag_keys'] = self.tag_keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('resource_ids') is not None:
            self.resource_ids_shrink = m.get('resource_ids')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('tag_keys') is not None:
            self.tag_keys_shrink = m.get('tag_keys')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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
        pass

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


class UpdateControlPlaneLogRequest(TeaModel):
    def __init__(
        self,
        aliuid: str = None,
        components: List[str] = None,
        log_project: str = None,
        log_ttl: str = None,
    ):
        # The ID of the Alibaba Cloud account.
        self.aliuid = aliuid
        # The control plane components for which you want to enable log collection.
        self.components = components
        # The name of the Simple Log Service project that you want to use to store the logs of control plane components.
        # 
        # Default value: k8s-log-$Cluster ID.
        self.log_project = log_project
        # The retention period of the log data stored in the Logstore. Valid values: 1 to 3000. Unit: days.
        # 
        # Default value: 30.
        self.log_ttl = log_ttl

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['aliuid'] = self.aliuid
        if self.components is not None:
            result['components'] = self.components
        if self.log_project is not None:
            result['log_project'] = self.log_project
        if self.log_ttl is not None:
            result['log_ttl'] = self.log_ttl
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliuid') is not None:
            self.aliuid = m.get('aliuid')
        if m.get('components') is not None:
            self.components = m.get('components')
        if m.get('log_project') is not None:
            self.log_project = m.get('log_project')
        if m.get('log_ttl') is not None:
            self.log_ttl = m.get('log_ttl')
        return self


class UpdateControlPlaneLogResponseBody(TeaModel):
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


class UpdateControlPlaneLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateControlPlaneLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpdateControlPlaneLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateK8sClusterUserConfigExpireRequest(TeaModel):
    def __init__(
        self,
        expire_hour: int = None,
        user: str = None,
    ):
        # The validity period of the kubeconfig file. Unit: hours.
        # 
        # > The value of expire_hour must be greater than 0 and equal to or smaller than 876000 (100 years).
        self.expire_hour = expire_hour
        # The user ID.
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
        pass

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
        # The description of the template.
        self.description = description
        # The name of the template.
        self.name = name
        # The label of the template.
        self.tags = tags
        # The YAML content of the template.
        self.template = template
        # The type of template. This parameter can be set to a custom value.
        # 
        # *   If the parameter is set to `kubernetes`, the template is displayed on the Templates page in the console.
        # *   If the parameter is set to `compose`, the template is displayed on the Container Service - Swarm page in the console. Container Service for Swarm is deprecated.
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
        pass

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
        master_only: bool = None,
        next_version: str = None,
        version: str = None,
    ):
        # The name of the component. Set the value to `k8s`.
        self.component_name = component_name
        # Specifies whether to update only master nodes. Valid values:
        # 
        # *   true: update only master nodes.
        # *   false: update master and worker nodes.
        self.master_only = master_only
        # The Kubernetes version to which the cluster can be updated.
        self.next_version = next_version
        # The current Kubernetes version of the cluster. For more information, see [Kubernetes versions](~~185269~~).
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
        if self.master_only is not None:
            result['master_only'] = self.master_only
        if self.next_version is not None:
            result['next_version'] = self.next_version
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('component_name') is not None:
            self.component_name = m.get('component_name')
        if m.get('master_only') is not None:
            self.master_only = m.get('master_only')
        if m.get('next_version') is not None:
            self.next_version = m.get('next_version')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterResponseBody(TeaModel):
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


class UpgradeClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeClusterResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeClusterAddonsRequestBody(TeaModel):
    def __init__(
        self,
        component_name: str = None,
        config: str = None,
        next_version: str = None,
        policy: str = None,
        version: str = None,
    ):
        # The name of the component.
        self.component_name = component_name
        # The custom component settings that you want to use. The value is a JSON string.
        self.config = config
        # The version to which the component can be updated. You can call the `DescribeClusterAddonsVersion` operation to query the version to which the component can be updated.
        self.next_version = next_version
        # The update policy. Valid values:
        # 
        # *   overwrite
        # *   canary
        self.policy = policy
        # The current version of the component.
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
        if self.policy is not None:
            result['policy'] = self.policy
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
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UpgradeClusterAddonsRequest(TeaModel):
    def __init__(
        self,
        body: List[UpgradeClusterAddonsRequestBody] = None,
    ):
        # The request parameters.
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
        pass

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


class UpgradeClusterNodepoolRequest(TeaModel):
    def __init__(
        self,
        image_id: str = None,
        kubernetes_version: str = None,
        runtime_type: str = None,
        runtime_version: str = None,
        use_replace: bool = None,
    ):
        # The ID of the OS image that is used by the nodes.
        self.image_id = image_id
        # The Kubernetes version that is used by the nodes.
        self.kubernetes_version = kubernetes_version
        # The runtime type. Valid values: containerd and docker.
        self.runtime_type = runtime_type
        # The version of the container runtime that is used by the nodes.
        self.runtime_version = runtime_version
        self.use_replace = use_replace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_id is not None:
            result['image_id'] = self.image_id
        if self.kubernetes_version is not None:
            result['kubernetes_version'] = self.kubernetes_version
        if self.runtime_type is not None:
            result['runtime_type'] = self.runtime_type
        if self.runtime_version is not None:
            result['runtime_version'] = self.runtime_version
        if self.use_replace is not None:
            result['use_replace'] = self.use_replace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_id') is not None:
            self.image_id = m.get('image_id')
        if m.get('kubernetes_version') is not None:
            self.kubernetes_version = m.get('kubernetes_version')
        if m.get('runtime_type') is not None:
            self.runtime_type = m.get('runtime_type')
        if m.get('runtime_version') is not None:
            self.runtime_version = m.get('runtime_version')
        if m.get('use_replace') is not None:
            self.use_replace = m.get('use_replace')
        return self


class UpgradeClusterNodepoolResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class UpgradeClusterNodepoolResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeClusterNodepoolResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
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
            temp_model = UpgradeClusterNodepoolResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


