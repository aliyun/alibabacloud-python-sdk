# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class JobSpec(DaraModel):
    def __init__(
        self,
        assign_node_spec: main_models.AssignNodeSpec = None,
        auto_scaling_spec: main_models.AutoScalingSpec = None,
        ecs_spec: str = None,
        extra_pod_spec: main_models.ExtraPodSpec = None,
        image: str = None,
        image_config: main_models.ImageConfig = None,
        is_cheif: bool = None,
        is_chief: bool = None,
        local_mount_specs: List[main_models.LocalMountSpec] = None,
        pod_count: int = None,
        resource_config: main_models.ResourceConfig = None,
        restart_policy: str = None,
        service_spec: main_models.ServiceSpec = None,
        spot_spec: main_models.SpotSpec = None,
        startup_dependencies: List[main_models.StartupDependency] = None,
        system_disk: main_models.SystemDisk = None,
        type: str = None,
        use_spot_instance: bool = None,
    ):
        self.assign_node_spec = assign_node_spec
        self.auto_scaling_spec = auto_scaling_spec
        self.ecs_spec = ecs_spec
        self.extra_pod_spec = extra_pod_spec
        self.image = image
        self.image_config = image_config
        self.is_cheif = is_cheif
        self.is_chief = is_chief
        self.local_mount_specs = local_mount_specs
        self.pod_count = pod_count
        self.resource_config = resource_config
        self.restart_policy = restart_policy
        self.service_spec = service_spec
        self.spot_spec = spot_spec
        self.startup_dependencies = startup_dependencies
        self.system_disk = system_disk
        self.type = type
        self.use_spot_instance = use_spot_instance

    def validate(self):
        if self.assign_node_spec:
            self.assign_node_spec.validate()
        if self.auto_scaling_spec:
            self.auto_scaling_spec.validate()
        if self.extra_pod_spec:
            self.extra_pod_spec.validate()
        if self.image_config:
            self.image_config.validate()
        if self.local_mount_specs:
            for v1 in self.local_mount_specs:
                 if v1:
                    v1.validate()
        if self.resource_config:
            self.resource_config.validate()
        if self.service_spec:
            self.service_spec.validate()
        if self.spot_spec:
            self.spot_spec.validate()
        if self.startup_dependencies:
            for v1 in self.startup_dependencies:
                 if v1:
                    v1.validate()
        if self.system_disk:
            self.system_disk.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_node_spec is not None:
            result['AssignNodeSpec'] = self.assign_node_spec.to_map()

        if self.auto_scaling_spec is not None:
            result['AutoScalingSpec'] = self.auto_scaling_spec.to_map()

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec

        if self.extra_pod_spec is not None:
            result['ExtraPodSpec'] = self.extra_pod_spec.to_map()

        if self.image is not None:
            result['Image'] = self.image

        if self.image_config is not None:
            result['ImageConfig'] = self.image_config.to_map()

        if self.is_cheif is not None:
            result['IsCheif'] = self.is_cheif

        if self.is_chief is not None:
            result['IsChief'] = self.is_chief

        result['LocalMountSpecs'] = []
        if self.local_mount_specs is not None:
            for k1 in self.local_mount_specs:
                result['LocalMountSpecs'].append(k1.to_map() if k1 else None)

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.resource_config is not None:
            result['ResourceConfig'] = self.resource_config.to_map()

        if self.restart_policy is not None:
            result['RestartPolicy'] = self.restart_policy

        if self.service_spec is not None:
            result['ServiceSpec'] = self.service_spec.to_map()

        if self.spot_spec is not None:
            result['SpotSpec'] = self.spot_spec.to_map()

        result['StartupDependencies'] = []
        if self.startup_dependencies is not None:
            for k1 in self.startup_dependencies:
                result['StartupDependencies'].append(k1.to_map() if k1 else None)

        if self.system_disk is not None:
            result['SystemDisk'] = self.system_disk.to_map()

        if self.type is not None:
            result['Type'] = self.type

        if self.use_spot_instance is not None:
            result['UseSpotInstance'] = self.use_spot_instance

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignNodeSpec') is not None:
            temp_model = main_models.AssignNodeSpec()
            self.assign_node_spec = temp_model.from_map(m.get('AssignNodeSpec'))

        if m.get('AutoScalingSpec') is not None:
            temp_model = main_models.AutoScalingSpec()
            self.auto_scaling_spec = temp_model.from_map(m.get('AutoScalingSpec'))

        if m.get('EcsSpec') is not None:
            self.ecs_spec = m.get('EcsSpec')

        if m.get('ExtraPodSpec') is not None:
            temp_model = main_models.ExtraPodSpec()
            self.extra_pod_spec = temp_model.from_map(m.get('ExtraPodSpec'))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageConfig') is not None:
            temp_model = main_models.ImageConfig()
            self.image_config = temp_model.from_map(m.get('ImageConfig'))

        if m.get('IsCheif') is not None:
            self.is_cheif = m.get('IsCheif')

        if m.get('IsChief') is not None:
            self.is_chief = m.get('IsChief')

        self.local_mount_specs = []
        if m.get('LocalMountSpecs') is not None:
            for k1 in m.get('LocalMountSpecs'):
                temp_model = main_models.LocalMountSpec()
                self.local_mount_specs.append(temp_model.from_map(k1))

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('ResourceConfig') is not None:
            temp_model = main_models.ResourceConfig()
            self.resource_config = temp_model.from_map(m.get('ResourceConfig'))

        if m.get('RestartPolicy') is not None:
            self.restart_policy = m.get('RestartPolicy')

        if m.get('ServiceSpec') is not None:
            temp_model = main_models.ServiceSpec()
            self.service_spec = temp_model.from_map(m.get('ServiceSpec'))

        if m.get('SpotSpec') is not None:
            temp_model = main_models.SpotSpec()
            self.spot_spec = temp_model.from_map(m.get('SpotSpec'))

        self.startup_dependencies = []
        if m.get('StartupDependencies') is not None:
            for k1 in m.get('StartupDependencies'):
                temp_model = main_models.StartupDependency()
                self.startup_dependencies.append(temp_model.from_map(k1))

        if m.get('SystemDisk') is not None:
            temp_model = main_models.SystemDisk()
            self.system_disk = temp_model.from_map(m.get('SystemDisk'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UseSpotInstance') is not None:
            self.use_spot_instance = m.get('UseSpotInstance')

        return self

