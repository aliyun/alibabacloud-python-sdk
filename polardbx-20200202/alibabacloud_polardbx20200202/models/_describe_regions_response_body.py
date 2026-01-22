# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        error_code: int = None,
        message: str = None,
        regions: main_models.DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.error_code = error_code
        self.message = message
        self.regions = regions
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Regions') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region: List[main_models.DescribeRegionsResponseBodyRegionsRegion] = None,
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
                temp_model = main_models.DescribeRegionsResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsRegion(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        support_polarx_10: bool = None,
        support_polarx_20: bool = None,
        zones: main_models.DescribeRegionsResponseBodyRegionsRegionZones = None,
    ):
        self.region_id = region_id
        self.support_polarx_10 = support_polarx_10
        self.support_polarx_20 = support_polarx_20
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_polarx_10 is not None:
            result['SupportPolarx10'] = self.support_polarx_10

        if self.support_polarx_20 is not None:
            result['SupportPolarx20'] = self.support_polarx_20

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportPolarx10') is not None:
            self.support_polarx_10 = m.get('SupportPolarx10')

        if m.get('SupportPolarx20') is not None:
            self.support_polarx_20 = m.get('SupportPolarx20')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegionsRegionZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeRegionsResponseBodyRegionsRegionZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.DescribeRegionsResponseBodyRegionsRegionZonesZone] = None,
    ):
        self.zone = zone

    def validate(self):
        if self.zone:
            for v1 in self.zone:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Zone'] = []
        if self.zone is not None:
            for k1 in self.zone:
                result['Zone'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.zone = []
        if m.get('Zone') is not None:
            for k1 in m.get('Zone'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionsRegionZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsRegionZonesZone(DaraModel):
    def __init__(
        self,
        vpc_enabled: bool = None,
        zone_id: str = None,
    ):
        self.vpc_enabled = vpc_enabled
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_enabled is not None:
            result['VpcEnabled'] = self.vpc_enabled

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

