# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionInfosResponseBody(DaraModel):
    def __init__(
        self,
        regions: main_models.DescribeRegionInfosResponseBodyRegions = None,
        request_id: str = None,
    ):
        # A list of regions.
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
            temp_model = main_models.DescribeRegionInfosResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeRegionInfosResponseBodyRegions(DaraModel):
    def __init__(
        self,
        rdsregion: List[main_models.DescribeRegionInfosResponseBodyRegionsRDSRegion] = None,
    ):
        self.rdsregion = rdsregion

    def validate(self):
        if self.rdsregion:
            for v1 in self.rdsregion:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RDSRegion'] = []
        if self.rdsregion is not None:
            for k1 in self.rdsregion:
                result['RDSRegion'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rdsregion = []
        if m.get('RDSRegion') is not None:
            for k1 in m.get('RDSRegion'):
                temp_model = main_models.DescribeRegionInfosResponseBodyRegionsRDSRegion()
                self.rdsregion.append(temp_model.from_map(k1))

        return self

class DescribeRegionInfosResponseBodyRegionsRDSRegion(DaraModel):
    def __init__(
        self,
        region_id: str = None,
    ):
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

