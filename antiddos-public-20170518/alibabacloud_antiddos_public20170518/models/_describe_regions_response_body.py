# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_antiddos_public20170518 import models as main_models
from darabonba.model import DaraModel

class DescribeRegionsResponseBody(DaraModel):
    def __init__(
        self,
        regions: main_models.DescribeRegionsResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.regions = regions
        # The ID of the request.
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
        region_en_name: str = None,
        region_name: str = None,
        region_no: str = None,
        region_no_alias: str = None,
    ):
        self.region_en_name = region_en_name
        self.region_name = region_name
        self.region_no = region_no
        self.region_no_alias = region_no_alias

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.region_no_alias is not None:
            result['RegionNoAlias'] = self.region_no_alias

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('RegionNoAlias') is not None:
            self.region_no_alias = m.get('RegionNoAlias')

        return self

