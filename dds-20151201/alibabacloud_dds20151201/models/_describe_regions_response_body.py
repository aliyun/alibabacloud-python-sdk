# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dds20151201 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: main_models.DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        # The regions.
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
            temp_model = main_models.DescribeRegionsResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        dds_region: List[main_models.DescribeRegionsResponseBodyRegionsDdsRegion] = None,
    ):
        self.dds_region = dds_region

    def validate(self):
        if self.dds_region:
            for v1 in self.dds_region:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DdsRegion'] = []
        if self.dds_region is not None:
            for k1 in self.dds_region:
                result['DdsRegion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dds_region = []
        if m.get('DdsRegion') is not None:
            for k1 in m.get('DdsRegion'):
                temp_model = main_models.DescribeRegionsResponseBodyRegionsDdsRegion()
                self.dds_region.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsDdsRegion(DaraModel):
    def __init__(
        self,
        end_point: str = None,
        region_id: str = None,
        region_name: str = None,
        zones: main_models.DescribeRegionsResponseBodyRegionsDdsRegionZones = None,
    ):
        # The public endpoint of the region.
        # 
        # For example, if the value of the RegionId parameter in the response is cn-hangzhou, the following value is returned for the EndPoint parameter:
        # 
        # *   mongodb.aliyuncs.com
        self.end_point = end_point
        # The region ID.
        self.region_id = region_id
        # The name of the region.
        # 
        # The value of the LocalName parameter is in the language that is specified by the **AcceptLanguage** parameter. For example, if the value of the RegionId parameter in the response is **cn-hangzhou**, the following values are returned for the LocalName parameter:
        # 
        # *   If the value of the **AcceptLanguage** parameter is **zh**, the value **华东1（杭州）** is returned for the LocalName parameter.
        # *   If the value of the **AcceptLanguage** parameter is **en**, the value **China (Hangzhou)** is returned for the LocalName parameter.
        self.region_name = region_name
        # The zones.
        self.zones = zones

    def validate(self):
        if self.zones:
            self.zones.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_point is not None:
            result['EndPoint'] = self.end_point

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.zones is not None:
            result['Zones'] = self.zones.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndPoint') is not None:
            self.end_point = m.get('EndPoint')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('Zones') is not None:
            temp_model = main_models.DescribeRegionsResponseBodyRegionsDdsRegionZones()
            self.zones = temp_model.from_map(m.get('Zones'))

        return self

class DescribeRegionsResponseBodyRegionsDdsRegionZones(DaraModel):
    def __init__(
        self,
        zone: List[main_models.DescribeRegionsResponseBodyRegionsDdsRegionZonesZone] = None,
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
                temp_model = main_models.DescribeRegionsResponseBodyRegionsDdsRegionZonesZone()
                self.zone.append(temp_model.from_map(k1))

        return self

class DescribeRegionsResponseBodyRegionsDdsRegionZonesZone(DaraModel):
    def __init__(
        self,
        vpc_enabled: bool = None,
        zone_id: str = None,
        zone_name: str = None,
    ):
        # Indicates whether a virtual private cloud (VPC) is supported. Valid values:
        # 
        # *   **true**: VPC is supported.
        # *   **false**: VPC is not supported.
        self.vpc_enabled = vpc_enabled
        # The zone ID.
        self.zone_id = zone_id
        # The name of the zone.
        # 
        # The value of the ZoneName parameter is in the language that is specified by the **AcceptLanguage** parameter. For example, if the value of the ZoneId parameter in the response is **cn-hangzhou-h**, the following values are returned for the ZoneName parameter:
        # 
        # *   If the value of the **AcceptLanguage** parameter is **zh**, the value **H** is returned for the ZoneName parameter.
        # *   If the value of the **AcceptLanguage** parameter is **en**, the value **Hangzhou Zone H** is returned for the ZoneName parameter.
        self.zone_name = zone_name

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

        if self.zone_name is not None:
            result['ZoneName'] = self.zone_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcEnabled') is not None:
            self.vpc_enabled = m.get('VpcEnabled')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        if m.get('ZoneName') is not None:
            self.zone_name = m.get('ZoneName')

        return self

