# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class ExtraPodSpec(DaraModel):
    def __init__(
        self,
        init_containers: List[main_models.ContainerSpec] = None,
        lifecycle: main_models.Lifecycle = None,
        pod_annotations: Dict[str, str] = None,
        pod_labels: Dict[str, str] = None,
        shared_volume_mount_paths: List[str] = None,
        side_car_containers: List[main_models.ContainerSpec] = None,
    ):
        self.init_containers = init_containers
        self.lifecycle = lifecycle
        self.pod_annotations = pod_annotations
        self.pod_labels = pod_labels
        self.shared_volume_mount_paths = shared_volume_mount_paths
        self.side_car_containers = side_car_containers

    def validate(self):
        if self.init_containers:
            for v1 in self.init_containers:
                 if v1:
                    v1.validate()
        if self.lifecycle:
            self.lifecycle.validate()
        if self.side_car_containers:
            for v1 in self.side_car_containers:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InitContainers'] = []
        if self.init_containers is not None:
            for k1 in self.init_containers:
                result['InitContainers'].append(k1.to_map() if k1 else None)

        if self.lifecycle is not None:
            result['Lifecycle'] = self.lifecycle.to_map()

        if self.pod_annotations is not None:
            result['PodAnnotations'] = self.pod_annotations

        if self.pod_labels is not None:
            result['PodLabels'] = self.pod_labels

        if self.shared_volume_mount_paths is not None:
            result['SharedVolumeMountPaths'] = self.shared_volume_mount_paths

        result['SideCarContainers'] = []
        if self.side_car_containers is not None:
            for k1 in self.side_car_containers:
                result['SideCarContainers'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.init_containers = []
        if m.get('InitContainers') is not None:
            for k1 in m.get('InitContainers'):
                temp_model = main_models.ContainerSpec()
                self.init_containers.append(temp_model.from_map(k1))

        if m.get('Lifecycle') is not None:
            temp_model = main_models.Lifecycle()
            self.lifecycle = temp_model.from_map(m.get('Lifecycle'))

        if m.get('PodAnnotations') is not None:
            self.pod_annotations = m.get('PodAnnotations')

        if m.get('PodLabels') is not None:
            self.pod_labels = m.get('PodLabels')

        if m.get('SharedVolumeMountPaths') is not None:
            self.shared_volume_mount_paths = m.get('SharedVolumeMountPaths')

        self.side_car_containers = []
        if m.get('SideCarContainers') is not None:
            for k1 in m.get('SideCarContainers'):
                temp_model = main_models.ContainerSpec()
                self.side_car_containers.append(temp_model.from_map(k1))

        return self

