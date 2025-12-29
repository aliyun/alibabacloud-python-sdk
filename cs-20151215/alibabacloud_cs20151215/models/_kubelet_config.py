# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class KubeletConfig(DaraModel):
    def __init__(
        self,
        allowed_unsafe_sysctls: List[str] = None,
        cluster_dns: List[str] = None,
        container_log_max_files: int = None,
        container_log_max_size: str = None,
        container_log_max_workers: int = None,
        container_log_monitor_interval: str = None,
        cpu_cfsquota: bool = None,
        cpu_cfsquota_period: str = None,
        cpu_manager_policy: str = None,
        event_burst: int = None,
        event_record_qps: int = None,
        eviction_hard: Dict[str, Any] = None,
        eviction_soft: Dict[str, Any] = None,
        eviction_soft_grace_period: Dict[str, Any] = None,
        feature_gates: Dict[str, Any] = None,
        image_gchigh_threshold_percent: int = None,
        image_gclow_threshold_percent: int = None,
        kube_apiburst: int = None,
        kube_apiqps: int = None,
        kube_reserved: Dict[str, Any] = None,
        max_pods: int = None,
        memory_manager_policy: str = None,
        pod_pids_limit: int = None,
        read_only_port: int = None,
        registry_burst: int = None,
        registry_pull_qps: int = None,
        reserved_memory: List[main_models.KubeletConfigReservedMemory] = None,
        serialize_image_pulls: bool = None,
        server_tlsbootstrap: bool = None,
        system_reserved: Dict[str, Any] = None,
        topology_manager_policy: str = None,
        tracing: main_models.KubeletConfigTracing = None,
    ):
        self.allowed_unsafe_sysctls = allowed_unsafe_sysctls
        self.cluster_dns = cluster_dns
        self.container_log_max_files = container_log_max_files
        self.container_log_max_size = container_log_max_size
        self.container_log_max_workers = container_log_max_workers
        self.container_log_monitor_interval = container_log_monitor_interval
        self.cpu_cfsquota = cpu_cfsquota
        self.cpu_cfsquota_period = cpu_cfsquota_period
        self.cpu_manager_policy = cpu_manager_policy
        self.event_burst = event_burst
        self.event_record_qps = event_record_qps
        self.eviction_hard = eviction_hard
        self.eviction_soft = eviction_soft
        self.eviction_soft_grace_period = eviction_soft_grace_period
        self.feature_gates = feature_gates
        self.image_gchigh_threshold_percent = image_gchigh_threshold_percent
        self.image_gclow_threshold_percent = image_gclow_threshold_percent
        self.kube_apiburst = kube_apiburst
        self.kube_apiqps = kube_apiqps
        self.kube_reserved = kube_reserved
        self.max_pods = max_pods
        self.memory_manager_policy = memory_manager_policy
        self.pod_pids_limit = pod_pids_limit
        self.read_only_port = read_only_port
        self.registry_burst = registry_burst
        self.registry_pull_qps = registry_pull_qps
        self.reserved_memory = reserved_memory
        self.serialize_image_pulls = serialize_image_pulls
        self.server_tlsbootstrap = server_tlsbootstrap
        self.system_reserved = system_reserved
        self.topology_manager_policy = topology_manager_policy
        self.tracing = tracing

    def validate(self):
        if self.reserved_memory:
            for v1 in self.reserved_memory:
                 if v1:
                    v1.validate()
        if self.tracing:
            self.tracing.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_unsafe_sysctls is not None:
            result['allowedUnsafeSysctls'] = self.allowed_unsafe_sysctls

        if self.cluster_dns is not None:
            result['clusterDNS'] = self.cluster_dns

        if self.container_log_max_files is not None:
            result['containerLogMaxFiles'] = self.container_log_max_files

        if self.container_log_max_size is not None:
            result['containerLogMaxSize'] = self.container_log_max_size

        if self.container_log_max_workers is not None:
            result['containerLogMaxWorkers'] = self.container_log_max_workers

        if self.container_log_monitor_interval is not None:
            result['containerLogMonitorInterval'] = self.container_log_monitor_interval

        if self.cpu_cfsquota is not None:
            result['cpuCFSQuota'] = self.cpu_cfsquota

        if self.cpu_cfsquota_period is not None:
            result['cpuCFSQuotaPeriod'] = self.cpu_cfsquota_period

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

        if self.image_gchigh_threshold_percent is not None:
            result['imageGCHighThresholdPercent'] = self.image_gchigh_threshold_percent

        if self.image_gclow_threshold_percent is not None:
            result['imageGCLowThresholdPercent'] = self.image_gclow_threshold_percent

        if self.kube_apiburst is not None:
            result['kubeAPIBurst'] = self.kube_apiburst

        if self.kube_apiqps is not None:
            result['kubeAPIQPS'] = self.kube_apiqps

        if self.kube_reserved is not None:
            result['kubeReserved'] = self.kube_reserved

        if self.max_pods is not None:
            result['maxPods'] = self.max_pods

        if self.memory_manager_policy is not None:
            result['memoryManagerPolicy'] = self.memory_manager_policy

        if self.pod_pids_limit is not None:
            result['podPidsLimit'] = self.pod_pids_limit

        if self.read_only_port is not None:
            result['readOnlyPort'] = self.read_only_port

        if self.registry_burst is not None:
            result['registryBurst'] = self.registry_burst

        if self.registry_pull_qps is not None:
            result['registryPullQPS'] = self.registry_pull_qps

        result['reservedMemory'] = []
        if self.reserved_memory is not None:
            for k1 in self.reserved_memory:
                result['reservedMemory'].append(k1.to_map() if k1 else None)

        if self.serialize_image_pulls is not None:
            result['serializeImagePulls'] = self.serialize_image_pulls

        if self.server_tlsbootstrap is not None:
            result['serverTLSBootstrap'] = self.server_tlsbootstrap

        if self.system_reserved is not None:
            result['systemReserved'] = self.system_reserved

        if self.topology_manager_policy is not None:
            result['topologyManagerPolicy'] = self.topology_manager_policy

        if self.tracing is not None:
            result['tracing'] = self.tracing.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowedUnsafeSysctls') is not None:
            self.allowed_unsafe_sysctls = m.get('allowedUnsafeSysctls')

        if m.get('clusterDNS') is not None:
            self.cluster_dns = m.get('clusterDNS')

        if m.get('containerLogMaxFiles') is not None:
            self.container_log_max_files = m.get('containerLogMaxFiles')

        if m.get('containerLogMaxSize') is not None:
            self.container_log_max_size = m.get('containerLogMaxSize')

        if m.get('containerLogMaxWorkers') is not None:
            self.container_log_max_workers = m.get('containerLogMaxWorkers')

        if m.get('containerLogMonitorInterval') is not None:
            self.container_log_monitor_interval = m.get('containerLogMonitorInterval')

        if m.get('cpuCFSQuota') is not None:
            self.cpu_cfsquota = m.get('cpuCFSQuota')

        if m.get('cpuCFSQuotaPeriod') is not None:
            self.cpu_cfsquota_period = m.get('cpuCFSQuotaPeriod')

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

        if m.get('imageGCHighThresholdPercent') is not None:
            self.image_gchigh_threshold_percent = m.get('imageGCHighThresholdPercent')

        if m.get('imageGCLowThresholdPercent') is not None:
            self.image_gclow_threshold_percent = m.get('imageGCLowThresholdPercent')

        if m.get('kubeAPIBurst') is not None:
            self.kube_apiburst = m.get('kubeAPIBurst')

        if m.get('kubeAPIQPS') is not None:
            self.kube_apiqps = m.get('kubeAPIQPS')

        if m.get('kubeReserved') is not None:
            self.kube_reserved = m.get('kubeReserved')

        if m.get('maxPods') is not None:
            self.max_pods = m.get('maxPods')

        if m.get('memoryManagerPolicy') is not None:
            self.memory_manager_policy = m.get('memoryManagerPolicy')

        if m.get('podPidsLimit') is not None:
            self.pod_pids_limit = m.get('podPidsLimit')

        if m.get('readOnlyPort') is not None:
            self.read_only_port = m.get('readOnlyPort')

        if m.get('registryBurst') is not None:
            self.registry_burst = m.get('registryBurst')

        if m.get('registryPullQPS') is not None:
            self.registry_pull_qps = m.get('registryPullQPS')

        self.reserved_memory = []
        if m.get('reservedMemory') is not None:
            for k1 in m.get('reservedMemory'):
                temp_model = main_models.KubeletConfigReservedMemory()
                self.reserved_memory.append(temp_model.from_map(k1))

        if m.get('serializeImagePulls') is not None:
            self.serialize_image_pulls = m.get('serializeImagePulls')

        if m.get('serverTLSBootstrap') is not None:
            self.server_tlsbootstrap = m.get('serverTLSBootstrap')

        if m.get('systemReserved') is not None:
            self.system_reserved = m.get('systemReserved')

        if m.get('topologyManagerPolicy') is not None:
            self.topology_manager_policy = m.get('topologyManagerPolicy')

        if m.get('tracing') is not None:
            temp_model = main_models.KubeletConfigTracing()
            self.tracing = temp_model.from_map(m.get('tracing'))

        return self

class KubeletConfigTracing(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        sampling_rate_per_million: int = None,
    ):
        self.endpoint = endpoint
        self.sampling_rate_per_million = sampling_rate_per_million

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint

        if self.sampling_rate_per_million is not None:
            result['samplingRatePerMillion'] = self.sampling_rate_per_million

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')

        if m.get('samplingRatePerMillion') is not None:
            self.sampling_rate_per_million = m.get('samplingRatePerMillion')

        return self



class KubeletConfigReservedMemory(DaraModel):
    def __init__(
        self,
        limits: Dict[str, Any] = None,
        numa_node: int = None,
    ):
        self.limits = limits
        self.numa_node = numa_node

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limits is not None:
            result['limits'] = self.limits

        if self.numa_node is not None:
            result['numaNode'] = self.numa_node

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limits') is not None:
            self.limits = m.get('limits')

        if m.get('numaNode') is not None:
            self.numa_node = m.get('numaNode')

        return self

