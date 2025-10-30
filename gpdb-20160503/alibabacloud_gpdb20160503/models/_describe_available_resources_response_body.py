# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourcesResponseBody(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        request_id: str = None,
        resources: List[main_models.DescribeAvailableResourcesResponseBodyResources] = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The zone ID.
        self.resources = resources

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.DescribeAvailableResourcesResponseBodyResources()
                self.resources.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourcesResponseBodyResources(DaraModel):
    def __init__(
        self,
        supported_engines: List[main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEngines] = None,
        zone_id: str = None,
    ):
        # The available engine version and specifications.
        self.supported_engines = supported_engines
        # The ID of the zone.
        self.zone_id = zone_id

    def validate(self):
        if self.supported_engines:
            for v1 in self.supported_engines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k1 in self.supported_engines:
                result['SupportedEngines'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k1 in m.get('SupportedEngines'):
                temp_model = main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAvailableResourcesResponseBodyResourcesSupportedEngines(DaraModel):
    def __init__(
        self,
        mode: str = None,
        supported_engine_version: str = None,
        supported_instance_classes: List[main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses] = None,
    ):
        # The instance resource type. Valid values:
        # 
        # *   **ecs**: elastic storage mode
        # *   **serverless**: Serverless mode
        self.mode = mode
        # The available engine version.
        self.supported_engine_version = supported_engine_version
        # The available specifications.
        self.supported_instance_classes = supported_instance_classes

    def validate(self):
        if self.supported_instance_classes:
            for v1 in self.supported_instance_classes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mode is not None:
            result['Mode'] = self.mode

        if self.supported_engine_version is not None:
            result['SupportedEngineVersion'] = self.supported_engine_version

        result['SupportedInstanceClasses'] = []
        if self.supported_instance_classes is not None:
            for k1 in self.supported_instance_classes:
                result['SupportedInstanceClasses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('SupportedEngineVersion') is not None:
            self.supported_engine_version = m.get('SupportedEngineVersion')

        self.supported_instance_classes = []
        if m.get('SupportedInstanceClasses') is not None:
            for k1 in m.get('SupportedInstanceClasses'):
                temp_model = main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses()
                self.supported_instance_classes.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClasses(DaraModel):
    def __init__(
        self,
        category: str = None,
        description: str = None,
        display_class: str = None,
        instance_class: str = None,
        node_count: main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount = None,
        storage_size: main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize = None,
        storage_type: str = None,
    ):
        # The instance edition. Valid values:
        # 
        # *   **HighAvailability**: High-availability Edition
        # *   **Basic**: Basic Edition
        self.category = category
        # The description of compute node specifications.
        self.description = description
        # The specifications of each compute node.
        self.display_class = display_class
        # The specifications of each compute node.
        self.instance_class = instance_class
        # Details about the compute nodes.
        self.node_count = node_count
        # Details about the storage capacity of compute nodes.
        self.storage_size = storage_size
        # The storage type. Valid values:
        # 
        # *   **cloud_essd**: enhanced SSD (ESSD)
        # *   **cloud_efficiency**: ultra disk
        # *   **oss**: Object Storage Service (OSS)
        self.storage_type = storage_type

    def validate(self):
        if self.node_count:
            self.node_count.validate()
        if self.storage_size:
            self.storage_size.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.description is not None:
            result['Description'] = self.description

        if self.display_class is not None:
            result['DisplayClass'] = self.display_class

        if self.instance_class is not None:
            result['InstanceClass'] = self.instance_class

        if self.node_count is not None:
            result['NodeCount'] = self.node_count.to_map()

        if self.storage_size is not None:
            result['StorageSize'] = self.storage_size.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DisplayClass') is not None:
            self.display_class = m.get('DisplayClass')

        if m.get('InstanceClass') is not None:
            self.instance_class = m.get('InstanceClass')

        if m.get('NodeCount') is not None:
            temp_model = main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount()
            self.node_count = temp_model.from_map(m.get('NodeCount'))

        if m.get('StorageSize') is not None:
            temp_model = main_models.DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize()
            self.storage_size = temp_model.from_map(m.get('StorageSize'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesStorageSize(DaraModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum storage capacity of each compute node.
        self.max_count = max_count
        # The minimum storage capacity of each compute node.
        self.min_count = min_count
        # The step size for adding storage capacity for compute nodes.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

class DescribeAvailableResourcesResponseBodyResourcesSupportedEnginesSupportedInstanceClassesNodeCount(DaraModel):
    def __init__(
        self,
        max_count: str = None,
        min_count: str = None,
        step: str = None,
    ):
        # The maximum number of compute nodes.
        self.max_count = max_count
        # The minimum number of compute nodes.
        self.min_count = min_count
        # The step size for adding compute nodes.
        # 
        # For example, if the value of this parameter is 4, compute nodes must be added by multiples of 4.
        self.step = step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        if self.min_count is not None:
            result['MinCount'] = self.min_count

        if self.step is not None:
            result['Step'] = self.step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        if m.get('MinCount') is not None:
            self.min_count = m.get('MinCount')

        if m.get('Step') is not None:
            self.step = m.get('Step')

        return self

