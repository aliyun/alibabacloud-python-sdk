# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeAvailableZonesResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[main_models.DescribeAvailableZonesResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        # The available zones in the region.
        self.available_zones = available_zones
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.available_zones:
            for v1 in self.available_zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableZones'] = []
        if self.available_zones is not None:
            for k1 in self.available_zones:
                result['AvailableZones'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_zones = []
        if m.get('AvailableZones') is not None:
            for k1 in m.get('AvailableZones'):
                temp_model = main_models.DescribeAvailableZonesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAvailableZonesResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        supported_engines: List[main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEngines] = None,
        zone_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The database engines that are available for purchase.
        self.supported_engines = supported_engines
        # The zone ID.
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
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['SupportedEngines'] = []
        if self.supported_engines is not None:
            for k1 in self.supported_engines:
                result['SupportedEngines'].append(k1.to_map() if k1 else None)

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.supported_engines = []
        if m.get('SupportedEngines') is not None:
            for k1 in m.get('SupportedEngines'):
                temp_model = main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeAvailableZonesResponseBodyAvailableZonesSupportedEngines(DaraModel):
    def __init__(
        self,
        engine: str = None,
        supported_engine_versions: List[main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersions] = None,
    ):
        # The database engine of the instance.
        self.engine = engine
        # The database engine versions that are available for purchase.
        self.supported_engine_versions = supported_engine_versions

    def validate(self):
        if self.supported_engine_versions:
            for v1 in self.supported_engine_versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['Engine'] = self.engine

        result['SupportedEngineVersions'] = []
        if self.supported_engine_versions is not None:
            for k1 in self.supported_engine_versions:
                result['SupportedEngineVersions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        self.supported_engine_versions = []
        if m.get('SupportedEngineVersions') is not None:
            for k1 in m.get('SupportedEngineVersions'):
                temp_model = main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersions()
                self.supported_engine_versions.append(temp_model.from_map(k1))

        return self

class DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersions(DaraModel):
    def __init__(
        self,
        supported_categorys: List[main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys] = None,
        version: str = None,
    ):
        # The RDS editions that are available that are available for purchase.
        self.supported_categorys = supported_categorys
        # The database engine version.
        self.version = version

    def validate(self):
        if self.supported_categorys:
            for v1 in self.supported_categorys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SupportedCategorys'] = []
        if self.supported_categorys is not None:
            for k1 in self.supported_categorys:
                result['SupportedCategorys'].append(k1.to_map() if k1 else None)

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.supported_categorys = []
        if m.get('SupportedCategorys') is not None:
            for k1 in m.get('SupportedCategorys'):
                temp_model = main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys()
                self.supported_categorys.append(temp_model.from_map(k1))

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorys(DaraModel):
    def __init__(
        self,
        category: str = None,
        supported_storage_types: List[main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes] = None,
    ):
        # The RDS edition of the instance.
        self.category = category
        # The storage types that are available for purchase.
        self.supported_storage_types = supported_storage_types

    def validate(self):
        if self.supported_storage_types:
            for v1 in self.supported_storage_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        result['SupportedStorageTypes'] = []
        if self.supported_storage_types is not None:
            for k1 in self.supported_storage_types:
                result['SupportedStorageTypes'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        self.supported_storage_types = []
        if m.get('SupportedStorageTypes') is not None:
            for k1 in m.get('SupportedStorageTypes'):
                temp_model = main_models.DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes()
                self.supported_storage_types.append(temp_model.from_map(k1))

        return self

class DescribeAvailableZonesResponseBodyAvailableZonesSupportedEnginesSupportedEngineVersionsSupportedCategorysSupportedStorageTypes(DaraModel):
    def __init__(
        self,
        storage_type: str = None,
    ):
        # The storage type of the instance.
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

