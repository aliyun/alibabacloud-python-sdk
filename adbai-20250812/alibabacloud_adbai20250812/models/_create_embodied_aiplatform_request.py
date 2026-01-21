# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adbai20250812 import models as main_models
from darabonba.model import DaraModel

class CreateEmbodiedAIPlatformRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        platform_name: str = None,
        ray_config: main_models.CreateEmbodiedAIPlatformRequestRayConfig = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.platform_name = platform_name
        self.ray_config = ray_config
        # This parameter is required.
        self.region_id = region_id
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        if self.ray_config:
            self.ray_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.ray_config is not None:
            result['RayConfig'] = self.ray_config.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RayConfig') is not None:
            temp_model = main_models.CreateEmbodiedAIPlatformRequestRayConfig()
            self.ray_config = temp_model.from_map(m.get('RayConfig'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')

        return self

class CreateEmbodiedAIPlatformRequestRayConfig(DaraModel):
    def __init__(
        self,
        category: str = None,
        head_spec: str = None,
        worker_groups: List[main_models.CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups] = None,
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
                temp_model = main_models.CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups()
                self.worker_groups.append(temp_model.from_map(k1))

        return self

class CreateEmbodiedAIPlatformRequestRayConfigWorkerGroups(DaraModel):
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

