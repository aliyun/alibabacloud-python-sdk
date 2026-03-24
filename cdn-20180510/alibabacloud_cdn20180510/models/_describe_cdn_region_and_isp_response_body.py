# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeCdnRegionAndIspResponseBody(DaraModel):
    def __init__(
        self,
        isps: main_models.DescribeCdnRegionAndIspResponseBodyIsps = None,
        regions: main_models.DescribeCdnRegionAndIspResponseBodyRegions = None,
        request_id: str = None,
    ):
        self.isps = isps
        self.regions = regions
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.isps:
            self.isps.validate()
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.isps is not None:
            result['Isps'] = self.isps.to_map()

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Isps') is not None:
            temp_model = main_models.DescribeCdnRegionAndIspResponseBodyIsps()
            self.isps = temp_model.from_map(m.get('Isps'))

        if m.get('Regions') is not None:
            temp_model = main_models.DescribeCdnRegionAndIspResponseBodyRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCdnRegionAndIspResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region: List[main_models.DescribeCdnRegionAndIspResponseBodyRegionsRegion] = None,
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
                temp_model = main_models.DescribeCdnRegionAndIspResponseBodyRegionsRegion()
                self.region.append(temp_model.from_map(k1))

        return self

class DescribeCdnRegionAndIspResponseBodyRegionsRegion(DaraModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        self.name_en = name_en
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_en is not None:
            result['NameEn'] = self.name_en

        if self.name_zh is not None:
            result['NameZh'] = self.name_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')

        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')

        return self

class DescribeCdnRegionAndIspResponseBodyIsps(DaraModel):
    def __init__(
        self,
        isp: List[main_models.DescribeCdnRegionAndIspResponseBodyIspsIsp] = None,
    ):
        self.isp = isp

    def validate(self):
        if self.isp:
            for v1 in self.isp:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Isp'] = []
        if self.isp is not None:
            for k1 in self.isp:
                result['Isp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp = []
        if m.get('Isp') is not None:
            for k1 in m.get('Isp'):
                temp_model = main_models.DescribeCdnRegionAndIspResponseBodyIspsIsp()
                self.isp.append(temp_model.from_map(k1))

        return self

class DescribeCdnRegionAndIspResponseBodyIspsIsp(DaraModel):
    def __init__(
        self,
        name_en: str = None,
        name_zh: str = None,
    ):
        self.name_en = name_en
        self.name_zh = name_zh

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name_en is not None:
            result['NameEn'] = self.name_en

        if self.name_zh is not None:
            result['NameZh'] = self.name_zh

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NameEn') is not None:
            self.name_en = m.get('NameEn')

        if m.get('NameZh') is not None:
            self.name_zh = m.get('NameZh')

        return self

