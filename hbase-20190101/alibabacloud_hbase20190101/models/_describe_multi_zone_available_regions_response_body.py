# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbase20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeMultiZoneAvailableRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Regions') is not None:
            temp_model = main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeMultiZoneAvailableRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region: List[main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion] = None,
    ):
        self.region = region

    def validate(self):
        if self.region:
            for v1 in self.region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Region'] = []
        if self.region is not None:
            for k1 in self.region:
                result['Region'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.region = []
        if m.get('Region') is not None:
            for k1 in m.get('Region'):
                temp_model = main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k1))

        return self

class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegion(DaraModel):
    def __init__(
        self,
        available_combines: main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines = None,
        local_name: str = None,
        region_endpoint: str = None,
        region_id: str = None,
    ):
        self.available_combines = available_combines
        self.local_name = local_name
        self.region_endpoint = region_endpoint
        self.region_id = region_id

    def validate(self):
        if self.available_combines:
            self.available_combines.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.available_combines is not None:
            result['AvailableCombines'] = self.available_combines.to_map()

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvailableCombines') is not None:
            temp_model = main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines()
            self.available_combines = temp_model.from_map(m.get('AvailableCombines'))

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombines(DaraModel):
    def __init__(
        self,
        available_combine: List[main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine] = None,
    ):
        self.available_combine = available_combine

    def validate(self):
        if self.available_combine:
            for v1 in self.available_combine:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AvailableCombine'] = []
        if self.available_combine is not None:
            for k1 in self.available_combine:
                result['AvailableCombine'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.available_combine = []
        if m.get('AvailableCombine') is not None:
            for k1 in m.get('AvailableCombine'):
                temp_model = main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine()
                self.available_combine.append(temp_model.from_map(k1))

        return self

class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombine(DaraModel):
    def __init__(
        self,
        id: str = None,
        zones: main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones = None,
    ):
        self.id = id
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeMultiZoneAvailableRegionsResponseBodyRegionsRegionAvailableCombinesAvailableCombineZones(DaraModel):
    def __init__(
        self,
        zone: List[str] = None,
    ):
        self.zone = zone

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.zone is not None:
            result['Zone'] = self.zone

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Zone') is not None:
            self.zone = m.get('Zone')

        return self

