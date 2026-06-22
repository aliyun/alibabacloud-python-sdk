# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class AckConfig(DaraModel):
    def __init__(
        self,
        ack_instance_id: str = None,
        custom_annotations: List[main_models.Tag] = None,
        custom_labels: List[main_models.Tag] = None,
        data_disk_size: int = None,
        data_disk_storage_class: str = None,
        limit_cpu: float = None,
        limit_memory: float = None,
        mount_host_cgroup: bool = None,
        namespace: str = None,
        node_affinity: str = None,
        node_selectors: List[main_models.Tag] = None,
        pod_affinity: str = None,
        pod_anti_affinity: str = None,
        pre_start_command: List[str] = None,
        pvcs: List[main_models.AckConfigPvcs] = None,
        request_cpu: float = None,
        request_memory: float = None,
        tolerations: List[main_models.Toleration] = None,
        volume_mounts: List[main_models.AckConfigVolumeMounts] = None,
        volumes: List[main_models.AckConfigVolumes] = None,
    ):
        # ack集群id
        self.ack_instance_id = ack_instance_id
        self.custom_annotations = custom_annotations
        self.custom_labels = custom_labels
        self.data_disk_size = data_disk_size
        self.data_disk_storage_class = data_disk_storage_class
        # Pod的CPU限制值。
        self.limit_cpu = limit_cpu
        # Pod的内存限制值。
        self.limit_memory = limit_memory
        self.mount_host_cgroup = mount_host_cgroup
        # ack 命名空间
        self.namespace = namespace
        self.node_affinity = node_affinity
        # ack的节点标签限制
        self.node_selectors = node_selectors
        self.pod_affinity = pod_affinity
        self.pod_anti_affinity = pod_anti_affinity
        self.pre_start_command = pre_start_command
        self.pvcs = pvcs
        # Pod的CPU请求值
        self.request_cpu = request_cpu
        # Pod的内存请求值。
        self.request_memory = request_memory
        # ack的节点污点容忍
        self.tolerations = tolerations
        self.volume_mounts = volume_mounts
        self.volumes = volumes

    def validate(self):
        if self.custom_annotations:
            for v1 in self.custom_annotations:
                 if v1:
                    v1.validate()
        if self.custom_labels:
            for v1 in self.custom_labels:
                 if v1:
                    v1.validate()
        if self.node_selectors:
            for v1 in self.node_selectors:
                 if v1:
                    v1.validate()
        if self.pvcs:
            for v1 in self.pvcs:
                 if v1:
                    v1.validate()
        if self.tolerations:
            for v1 in self.tolerations:
                 if v1:
                    v1.validate()
        if self.volume_mounts:
            for v1 in self.volume_mounts:
                 if v1:
                    v1.validate()
        if self.volumes:
            for v1 in self.volumes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ack_instance_id is not None:
            result['AckInstanceId'] = self.ack_instance_id

        result['CustomAnnotations'] = []
        if self.custom_annotations is not None:
            for k1 in self.custom_annotations:
                result['CustomAnnotations'].append(k1.to_map() if k1 else None)

        result['CustomLabels'] = []
        if self.custom_labels is not None:
            for k1 in self.custom_labels:
                result['CustomLabels'].append(k1.to_map() if k1 else None)

        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.data_disk_storage_class is not None:
            result['DataDiskStorageClass'] = self.data_disk_storage_class

        if self.limit_cpu is not None:
            result['LimitCpu'] = self.limit_cpu

        if self.limit_memory is not None:
            result['LimitMemory'] = self.limit_memory

        if self.mount_host_cgroup is not None:
            result['MountHostCgroup'] = self.mount_host_cgroup

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.node_affinity is not None:
            result['NodeAffinity'] = self.node_affinity

        result['NodeSelectors'] = []
        if self.node_selectors is not None:
            for k1 in self.node_selectors:
                result['NodeSelectors'].append(k1.to_map() if k1 else None)

        if self.pod_affinity is not None:
            result['PodAffinity'] = self.pod_affinity

        if self.pod_anti_affinity is not None:
            result['PodAntiAffinity'] = self.pod_anti_affinity

        if self.pre_start_command is not None:
            result['PreStartCommand'] = self.pre_start_command

        result['Pvcs'] = []
        if self.pvcs is not None:
            for k1 in self.pvcs:
                result['Pvcs'].append(k1.to_map() if k1 else None)

        if self.request_cpu is not None:
            result['RequestCpu'] = self.request_cpu

        if self.request_memory is not None:
            result['RequestMemory'] = self.request_memory

        result['Tolerations'] = []
        if self.tolerations is not None:
            for k1 in self.tolerations:
                result['Tolerations'].append(k1.to_map() if k1 else None)

        result['VolumeMounts'] = []
        if self.volume_mounts is not None:
            for k1 in self.volume_mounts:
                result['VolumeMounts'].append(k1.to_map() if k1 else None)

        result['Volumes'] = []
        if self.volumes is not None:
            for k1 in self.volumes:
                result['Volumes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AckInstanceId') is not None:
            self.ack_instance_id = m.get('AckInstanceId')

        self.custom_annotations = []
        if m.get('CustomAnnotations') is not None:
            for k1 in m.get('CustomAnnotations'):
                temp_model = main_models.Tag()
                self.custom_annotations.append(temp_model.from_map(k1))

        self.custom_labels = []
        if m.get('CustomLabels') is not None:
            for k1 in m.get('CustomLabels'):
                temp_model = main_models.Tag()
                self.custom_labels.append(temp_model.from_map(k1))

        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DataDiskStorageClass') is not None:
            self.data_disk_storage_class = m.get('DataDiskStorageClass')

        if m.get('LimitCpu') is not None:
            self.limit_cpu = m.get('LimitCpu')

        if m.get('LimitMemory') is not None:
            self.limit_memory = m.get('LimitMemory')

        if m.get('MountHostCgroup') is not None:
            self.mount_host_cgroup = m.get('MountHostCgroup')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NodeAffinity') is not None:
            self.node_affinity = m.get('NodeAffinity')

        self.node_selectors = []
        if m.get('NodeSelectors') is not None:
            for k1 in m.get('NodeSelectors'):
                temp_model = main_models.Tag()
                self.node_selectors.append(temp_model.from_map(k1))

        if m.get('PodAffinity') is not None:
            self.pod_affinity = m.get('PodAffinity')

        if m.get('PodAntiAffinity') is not None:
            self.pod_anti_affinity = m.get('PodAntiAffinity')

        if m.get('PreStartCommand') is not None:
            self.pre_start_command = m.get('PreStartCommand')

        self.pvcs = []
        if m.get('Pvcs') is not None:
            for k1 in m.get('Pvcs'):
                temp_model = main_models.AckConfigPvcs()
                self.pvcs.append(temp_model.from_map(k1))

        if m.get('RequestCpu') is not None:
            self.request_cpu = m.get('RequestCpu')

        if m.get('RequestMemory') is not None:
            self.request_memory = m.get('RequestMemory')

        self.tolerations = []
        if m.get('Tolerations') is not None:
            for k1 in m.get('Tolerations'):
                temp_model = main_models.Toleration()
                self.tolerations.append(temp_model.from_map(k1))

        self.volume_mounts = []
        if m.get('VolumeMounts') is not None:
            for k1 in m.get('VolumeMounts'):
                temp_model = main_models.AckConfigVolumeMounts()
                self.volume_mounts.append(temp_model.from_map(k1))

        self.volumes = []
        if m.get('Volumes') is not None:
            for k1 in m.get('Volumes'):
                temp_model = main_models.AckConfigVolumes()
                self.volumes.append(temp_model.from_map(k1))

        return self

class AckConfigVolumes(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
        type: str = None,
    ):
        self.name = name
        self.path = path
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class AckConfigVolumeMounts(DaraModel):
    def __init__(
        self,
        name: str = None,
        path: str = None,
    ):
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self



class AckConfigPvcs(DaraModel):
    def __init__(
        self,
        data_disk_size: int = None,
        data_disk_storage_class: str = None,
        name: str = None,
        path: str = None,
    ):
        self.data_disk_size = data_disk_size
        self.data_disk_storage_class = data_disk_storage_class
        self.name = name
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_disk_size is not None:
            result['DataDiskSize'] = self.data_disk_size

        if self.data_disk_storage_class is not None:
            result['DataDiskStorageClass'] = self.data_disk_storage_class

        if self.name is not None:
            result['Name'] = self.name

        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataDiskSize') is not None:
            self.data_disk_size = m.get('DataDiskSize')

        if m.get('DataDiskStorageClass') is not None:
            self.data_disk_storage_class = m.get('DataDiskStorageClass')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

