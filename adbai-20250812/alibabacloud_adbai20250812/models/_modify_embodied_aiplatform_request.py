# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class ModifyEmbodiedAIPlatformRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        device_count: str = None,
        platform_name: str = None,
        ray_config: main_models.ModifyEmbodiedAIPlatformRequestRayConfig = None,
        ray_train_config: main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfig = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.device_count = device_count
        # This parameter is required.
        self.platform_name = platform_name
        self.ray_config = ray_config
        self.ray_train_config = ray_train_config
        # This parameter is required.
        self.region_id = region_id
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        if self.ray_config:
            self.ray_config.validate()
        if self.ray_train_config:
            self.ray_train_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()

        if self.ray_train_config is not None:
            result['RayTrainConfig'] = self.ray_train_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RayConfig') is not None:
            temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayConfig()
            self.ray_config = temp_model.from_map(m.get('RayConfig'))

        if m.get('RayTrainConfig') is not None:
            temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfig()
            self.ray_train_config = temp_model.from_map(m.get('RayTrainConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')

        return self

class ModifyEmbodiedAIPlatformRequestRayTrainConfig(DaraModel):
    def __init__(
        self,
        cpu_acu: int = None,
        gpu_specs: List[main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigGpuSpecs] = None,
        terminal_config: main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfig = None,
    ):
        self.cpu_acu = cpu_acu
        self.gpu_specs = gpu_specs
        self.terminal_config = terminal_config

    def validate(self):
        if self.gpu_specs:
            for v1 in self.gpu_specs:
                 if v1:
                    v1.validate()
        if self.terminal_config:
            self.terminal_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_acu is not None:
            result['CpuAcu'] = self.cpu_acu

        result['GpuSpecs'] = []
        if self.gpu_specs is not None:
            for k1 in self.gpu_specs:
                result['GpuSpecs'].append(k1.to_map() if k1 else None)

        if self.terminal_config is not None:
            result['TerminalConfig'] = self.terminal_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuAcu') is not None:
            self.cpu_acu = m.get('CpuAcu')

        self.gpu_specs = []
        if m.get('GpuSpecs') is not None:
            for k1 in m.get('GpuSpecs'):
                temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigGpuSpecs()
                self.gpu_specs.append(temp_model.from_map(k1))

        if m.get('TerminalConfig') is not None:
            temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfig()
            self.terminal_config = temp_model.from_map(m.get('TerminalConfig'))

        return self

class ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfig(DaraModel):
    def __init__(
        self,
        acr_config: main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfigAcrConfig = None,
    ):
        self.acr_config = acr_config

    def validate(self):
        if self.acr_config:
            self.acr_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_config is not None:
            result['AcrConfig'] = self.acr_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcrConfig') is not None:
            temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfigAcrConfig()
            self.acr_config = temp_model.from_map(m.get('AcrConfig'))

        return self

class ModifyEmbodiedAIPlatformRequestRayTrainConfigTerminalConfigAcrConfig(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        namespaces: List[str] = None,
        registry: str = None,
    ):
        self.instance_id = instance_id
        self.namespaces = namespaces
        self.registry = registry

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces

        if self.registry is not None:
            result['Registry'] = self.registry

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')

        if m.get('Registry') is not None:
            self.registry = m.get('Registry')

        return self

class ModifyEmbodiedAIPlatformRequestRayTrainConfigGpuSpecs(DaraModel):
    def __init__(
        self,
        allocate_unit: str = None,
        count: int = None,
        spec_name: str = None,
    ):
        self.allocate_unit = allocate_unit
        self.count = count
        self.spec_name = spec_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_unit is not None:
            result['AllocateUnit'] = self.allocate_unit

        if self.count is not None:
            result['Count'] = self.count

        if self.spec_name is not None:
            result['SpecName'] = self.spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnit') is not None:
            self.allocate_unit = m.get('AllocateUnit')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('SpecName') is not None:
            self.spec_name = m.get('SpecName')

        return self

class ModifyEmbodiedAIPlatformRequestRayConfig(DaraModel):
    def __init__(
        self,
        category: str = None,
        head_spec: str = None,
        worker_groups: List[main_models.ModifyEmbodiedAIPlatformRequestRayConfigWorkerGroups] = None,
    ):
        self.category = category
        self.head_spec = head_spec
        self.worker_groups = worker_groups

    def validate(self):
        if self.worker_groups:
            for v1 in self.worker_groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.head_spec is not None:
            result['HeadSpec'] = self.head_spec

        result['WorkerGroups'] = []
        if self.worker_groups is not None:
            for k1 in self.worker_groups:
                result['WorkerGroups'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('HeadSpec') is not None:
            self.head_spec = m.get('HeadSpec')

        self.worker_groups = []
        if m.get('WorkerGroups') is not None:
            for k1 in m.get('WorkerGroups'):
                temp_model = main_models.ModifyEmbodiedAIPlatformRequestRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k1))

        return self

class ModifyEmbodiedAIPlatformRequestRayConfigWorkerGroups(DaraModel):
    def __init__(
        self,
        allocate_unit: str = None,
        group_name: str = None,
        max_worker_quantity: int = None,
        min_worker_quantity: int = None,
        worker_disk_capacity: str = None,
        worker_spec_name: str = None,
        worker_spec_type: str = None,
    ):
        self.allocate_unit = allocate_unit
        self.group_name = group_name
        self.max_worker_quantity = max_worker_quantity
        self.min_worker_quantity = min_worker_quantity
        self.worker_disk_capacity = worker_disk_capacity
        self.worker_spec_name = worker_spec_name
        self.worker_spec_type = worker_spec_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocate_unit is not None:
            result['AllocateUnit'] = self.allocate_unit

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.max_worker_quantity is not None:
            result['MaxWorkerQuantity'] = self.max_worker_quantity

        if self.min_worker_quantity is not None:
            result['MinWorkerQuantity'] = self.min_worker_quantity

        if self.worker_disk_capacity is not None:
            result['WorkerDiskCapacity'] = self.worker_disk_capacity

        if self.worker_spec_name is not None:
            result['WorkerSpecName'] = self.worker_spec_name

        if self.worker_spec_type is not None:
            result['WorkerSpecType'] = self.worker_spec_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocateUnit') is not None:
            self.allocate_unit = m.get('AllocateUnit')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('MaxWorkerQuantity') is not None:
            self.max_worker_quantity = m.get('MaxWorkerQuantity')

        if m.get('MinWorkerQuantity') is not None:
            self.min_worker_quantity = m.get('MinWorkerQuantity')

        if m.get('WorkerDiskCapacity') is not None:
            self.worker_disk_capacity = m.get('WorkerDiskCapacity')

        if m.get('WorkerSpecName') is not None:
            self.worker_spec_name = m.get('WorkerSpecName')

        if m.get('WorkerSpecType') is not None:
            self.worker_spec_type = m.get('WorkerSpecType')

        return self

