# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableResourceResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: main_models.DescribeAvailableResourceResponseBodyAvailableZones = None,
        request_id: str = None,
    ):
        self.available_zones = available_zones
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            self.available_zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_zones is not None:
            result['AvailableZones'] = self.available_zones.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableZones') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZones()
            self.available_zones = temp_model.from_map(m.get('AvailableZones'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableResourceResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        available_zone: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone] = None,
    ):
        self.available_zone = available_zone

    def validate(self):
        if self.available_zone:
            for v1 in self.available_zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZone'] = []
        if self.available_zone is not None:
            for k1 in self.available_zone:
                result['AvailableZone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zone = []
        if m.get('AvailableZone') is not None:
            for k1 in m.get('AvailableZone'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone()
                self.available_zone.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZone(DaraModel):
    def __init__(
        self,
        master_resources: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources = None,
        region_id: str = None,
        supported_engines: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines = None,
        zone_id: str = None,
    ):
        self.master_resources = master_resources
        self.region_id = region_id
        self.supported_engines = supported_engines
        self.zone_id = zone_id

    def validate(self):
        if self.master_resources:
            self.master_resources.validate()
        if self.supported_engines:
            self.supported_engines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.master_resources is not None:
            result['MasterResources'] = self.master_resources.to_map()

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.supported_engines is not None:
            result['SupportedEngines'] = self.supported_engines.to_map()

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MasterResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources()
            self.master_resources = temp_model.from_map(m.get('MasterResources'))

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportedEngines') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines()
            self.supported_engines = temp_model.from_map(m.get('SupportedEngines'))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEngines(DaraModel):
    def __init__(
        self,
        supported_engine: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine] = None,
    ):
        self.supported_engine = supported_engine

    def validate(self):
        if self.supported_engine:
            for v1 in self.supported_engine:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedEngine'] = []
        if self.supported_engine is not None:
            for k1 in self.supported_engine:
                result['SupportedEngine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine = []
        if m.get('SupportedEngine') is not None:
            for k1 in m.get('SupportedEngine'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine()
                self.supported_engine.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngine(DaraModel):
    def __init__(
        self,
        engine: str = None,
        supported_engine_versions: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions = None,
    ):
        self.engine = engine
        self.supported_engine_versions = supported_engine_versions

    def validate(self):
        if self.supported_engine_versions:
            self.supported_engine_versions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        if self.supported_engine_versions is not None:
            result['SupportedEngineVersions'] = self.supported_engine_versions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('SupportedEngineVersions') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions()
            self.supported_engine_versions = temp_model.from_map(m.get('SupportedEngineVersions'))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersions(DaraModel):
    def __init__(
        self,
        supported_engine_version: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion] = None,
    ):
        self.supported_engine_version = supported_engine_version

    def validate(self):
        if self.supported_engine_version:
            for v1 in self.supported_engine_version:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedEngineVersion'] = []
        if self.supported_engine_version is not None:
            for k1 in self.supported_engine_version:
                result['SupportedEngineVersion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_engine_version = []
        if m.get('SupportedEngineVersion') is not None:
            for k1 in m.get('SupportedEngineVersion'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion()
                self.supported_engine_version.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersion(DaraModel):
    def __init__(
        self,
        supported_categories: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories = None,
        version: str = None,
    ):
        self.supported_categories = supported_categories
        self.version = version

    def validate(self):
        if self.supported_categories:
            self.supported_categories.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.supported_categories is not None:
            result['SupportedCategories'] = self.supported_categories.to_map()

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SupportedCategories') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories()
            self.supported_categories = temp_model.from_map(m.get('SupportedCategories'))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategories(DaraModel):
    def __init__(
        self,
        supported_categories: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories] = None,
    ):
        self.supported_categories = supported_categories

    def validate(self):
        if self.supported_categories:
            for v1 in self.supported_categories:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedCategories'] = []
        if self.supported_categories is not None:
            for k1 in self.supported_categories:
                result['SupportedCategories'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_categories = []
        if m.get('SupportedCategories') is not None:
            for k1 in m.get('SupportedCategories'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories()
                self.supported_categories.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategories(DaraModel):
    def __init__(
        self,
        category: str = None,
        supported_storage_types: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes = None,
    ):
        self.category = category
        self.supported_storage_types = supported_storage_types

    def validate(self):
        if self.supported_storage_types:
            self.supported_storage_types.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.supported_storage_types is not None:
            result['SupportedStorageTypes'] = self.supported_storage_types.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('SupportedStorageTypes') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes()
            self.supported_storage_types = temp_model.from_map(m.get('SupportedStorageTypes'))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypes(DaraModel):
    def __init__(
        self,
        supported_storage_type: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType] = None,
    ):
        self.supported_storage_type = supported_storage_type

    def validate(self):
        if self.supported_storage_type:
            for v1 in self.supported_storage_type:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedStorageType'] = []
        if self.supported_storage_type is not None:
            for k1 in self.supported_storage_type:
                result['SupportedStorageType'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_storage_type = []
        if m.get('SupportedStorageType') is not None:
            for k1 in m.get('SupportedStorageType'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType()
                self.supported_storage_type.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageType(DaraModel):
    def __init__(
        self,
        core_resources: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources = None,
        storage_type: str = None,
    ):
        self.core_resources = core_resources
        self.storage_type = storage_type

    def validate(self):
        if self.core_resources:
            self.core_resources.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.core_resources is not None:
            result['CoreResources'] = self.core_resources.to_map()

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CoreResources') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources()
            self.core_resources = temp_model.from_map(m.get('CoreResources'))

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResources(DaraModel):
    def __init__(
        self,
        core_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource] = None,
    ):
        self.core_resource = core_resource

    def validate(self):
        if self.core_resource:
            for v1 in self.core_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CoreResource'] = []
        if self.core_resource is not None:
            for k1 in self.core_resource:
                result['CoreResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.core_resource = []
        if m.get('CoreResource') is not None:
            for k1 in m.get('CoreResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource()
                self.core_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResource(DaraModel):
    def __init__(
        self,
        dbinstance_storage_range: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange = None,
        instance_type: str = None,
        instance_type_detail: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail = None,
        max_core_count: int = None,
    ):
        self.dbinstance_storage_range = dbinstance_storage_range
        self.instance_type = instance_type
        self.instance_type_detail = instance_type_detail
        self.max_core_count = max_core_count

    def validate(self):
        if self.dbinstance_storage_range:
            self.dbinstance_storage_range.validate()
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_storage_range is not None:
            result['DBInstanceStorageRange'] = self.dbinstance_storage_range.to_map()

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()

        if self.max_core_count is not None:
            result['MaxCoreCount'] = self.max_core_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceStorageRange') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange()
            self.dbinstance_storage_range = temp_model.from_map(m.get('DBInstanceStorageRange'))

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeDetail') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m.get('InstanceTypeDetail'))

        if m.get('MaxCoreCount') is not None:
            self.max_core_count = m.get('MaxCoreCount')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceInstanceTypeDetail(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.mem is not None:
            result['Mem'] = self.mem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneSupportedEnginesSupportedEngineSupportedEngineVersionsSupportedEngineVersionSupportedCategoriesSupportedCategoriesSupportedStorageTypesSupportedStorageTypeCoreResourcesCoreResourceDBInstanceStorageRange(DaraModel):
    def __init__(
        self,
        max_size: int = None,
        min_size: int = None,
        step_size: int = None,
    ):
        self.max_size = max_size
        self.min_size = min_size
        self.step_size = step_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_size is not None:
            result['MaxSize'] = self.max_size

        if self.min_size is not None:
            result['MinSize'] = self.min_size

        if self.step_size is not None:
            result['StepSize'] = self.step_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxSize') is not None:
            self.max_size = m.get('MaxSize')

        if m.get('MinSize') is not None:
            self.min_size = m.get('MinSize')

        if m.get('StepSize') is not None:
            self.step_size = m.get('StepSize')

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResources(DaraModel):
    def __init__(
        self,
        master_resource: List[main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource] = None,
    ):
        self.master_resource = master_resource

    def validate(self):
        if self.master_resource:
            for v1 in self.master_resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MasterResource'] = []
        if self.master_resource is not None:
            for k1 in self.master_resource:
                result['MasterResource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.master_resource = []
        if m.get('MasterResource') is not None:
            for k1 in m.get('MasterResource'):
                temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource()
                self.master_resource.append(temp_model.from_map(k1))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResource(DaraModel):
    def __init__(
        self,
        instance_type: str = None,
        instance_type_detail: main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail = None,
    ):
        self.instance_type = instance_type
        self.instance_type_detail = instance_type_detail

    def validate(self):
        if self.instance_type_detail:
            self.instance_type_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.instance_type_detail is not None:
            result['InstanceTypeDetail'] = self.instance_type_detail.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('InstanceTypeDetail') is not None:
            temp_model = main_models.DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail()
            self.instance_type_detail = temp_model.from_map(m.get('InstanceTypeDetail'))

        return self

class DescribeAvailableResourceResponseBodyAvailableZonesAvailableZoneMasterResourcesMasterResourceInstanceTypeDetail(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        mem: int = None,
    ):
        self.cpu = cpu
        self.mem = mem

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['Cpu'] = self.cpu

        if self.mem is not None:
            result['Mem'] = self.mem

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cpu') is not None:
            self.cpu = m.get('Cpu')

        if m.get('Mem') is not None:
            self.mem = m.get('Mem')

        return self

