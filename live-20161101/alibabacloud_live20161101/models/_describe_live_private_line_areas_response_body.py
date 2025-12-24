# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePrivateLineAreasResponseBody(DaraModel):
    def __init__(
        self,
        live_areas_list: main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasList = None,
        request_id: str = None,
    ):
        # Details about the regions.
        self.live_areas_list = live_areas_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_areas_list:
            self.live_areas_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_areas_list is not None:
            result['LiveAreasList'] = self.live_areas_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveAreasList') is not None:
            temp_model = main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasList()
            self.live_areas_list = temp_model.from_map(m.get('LiveAreasList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLivePrivateLineAreasResponseBodyLiveAreasList(DaraModel):
    def __init__(
        self,
        live_area: List[main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveArea] = None,
    ):
        self.live_area = live_area

    def validate(self):
        if self.live_area:
            for v1 in self.live_area:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LiveArea'] = []
        if self.live_area is not None:
            for k1 in self.live_area:
                result['LiveArea'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_area = []
        if m.get('LiveArea') is not None:
            for k1 in m.get('LiveArea'):
                temp_model = main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveArea()
                self.live_area.append(temp_model.from_map(k1))

        return self

class DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveArea(DaraModel):
    def __init__(
        self,
        region_type: str = None,
        regions: main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegions = None,
    ):
        # The region type. Valid values:
        # 
        # *   domestic: in the Chinese mainland
        # *   overseas: outside the Chinese mainland
        self.region_type = region_type
        # The regions.
        self.regions = regions

    def validate(self):
        if self.regions:
            self.regions.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_type is not None:
            result['RegionType'] = self.region_type

        if self.regions is not None:
            result['Regions'] = self.regions.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionType') is not None:
            self.region_type = m.get('RegionType')

        if m.get('Regions') is not None:
            temp_model = main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegions()
            self.regions = temp_model.from_map(m.get('Regions'))

        return self

class DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegions(DaraModel):
    def __init__(
        self,
        region: List[main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegionsRegion] = None,
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
                temp_model = main_models.DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegionsRegion()
                self.region.append(temp_model.from_map(k1))

        return self

class DescribeLivePrivateLineAreasResponseBodyLiveAreasListLiveAreaRegionsRegion(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        # The region name.
        self.local_name = local_name
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

