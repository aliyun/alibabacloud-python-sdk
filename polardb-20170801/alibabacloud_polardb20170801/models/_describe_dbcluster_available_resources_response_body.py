# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeDBClusterAvailableResourcesResponseBody(DaraModel):
    def __init__(
        self,
        available_zones: List[main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZones] = None,
        request_id: str = None,
    ):
        # The available zones of the cluster.
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
                temp_model = main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZones()
                self.available_zones.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDBClusterAvailableResourcesResponseBodyAvailableZones(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        supported_engines: List[main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines] = None,
        zone_id: str = None,
    ):
        # The region ID of the cluster.
        self.region_id = region_id
        # The database engines that the available resources support.
        self.supported_engines = supported_engines
        # The zone ID of the cluster.
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
                temp_model = main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines()
                self.supported_engines.append(temp_model.from_map(k1))

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEngines(DaraModel):
    def __init__(
        self,
        available_resources: List[main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources] = None,
        engine: str = None,
    ):
        # The available resources.
        self.available_resources = available_resources
        # The version of the database engine.
        self.engine = engine

    def validate(self):
        if self.available_resources:
            for v1 in self.available_resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableResources'] = []
        if self.available_resources is not None:
            for k1 in self.available_resources:
                result['AvailableResources'].append(k1.to_map() if k1 else None)

        if self.engine is not None:
            result['Engine'] = self.engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_resources = []
        if m.get('AvailableResources') is not None:
            for k1 in m.get('AvailableResources'):
                temp_model = main_models.DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources()
                self.available_resources.append(temp_model.from_map(k1))

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        return self

class DescribeDBClusterAvailableResourcesResponseBodyAvailableZonesSupportedEnginesAvailableResources(DaraModel):
    def __init__(
        self,
        category: str = None,
        dbnode_class: str = None,
    ):
        # The edition of the cluster. Valid values:
        # 
        # *   **Normal**: Cluster Edition.
        # *   **Basic**: Single Node Edition.
        # *   **ArchiveNormal**: X-Engine.
        # *   **NormalMultimaster**: Multi-master Cluster (Database/Table) Edition.
        # *   **SENormal**: Standard Edition.
        # 
        # >- Only PolarDB for MySQL supports Single Node Edition.
        # >- Only PolarDB for MySQL 8.0 supports X-Engine Edition and Multi-master Cluster (Database/Table) Edition.
        self.category = category
        # The specifications of the node.
        self.dbnode_class = dbnode_class

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.dbnode_class is not None:
            result['DBNodeClass'] = self.dbnode_class

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('DBNodeClass') is not None:
            self.dbnode_class = m.get('DBNodeClass')

        return self

