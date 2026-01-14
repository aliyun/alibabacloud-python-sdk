# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListCommonAreasResponseBody(DaraModel):
    def __init__(
        self,
        areas: List[main_models.ListCommonAreasResponseBodyAreas] = None,
        request_id: str = None,
    ):
        # The information about the areas.
        self.areas = areas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.areas:
            for v1 in self.areas:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Areas'] = []
        if self.areas is not None:
            for k1 in self.areas:
                result['Areas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.areas = []
        if m.get('Areas') is not None:
            for k1 in m.get('Areas'):
                temp_model = main_models.ListCommonAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCommonAreasResponseBodyAreas(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        local_name: str = None,
        region_list: List[main_models.ListCommonAreasResponseBodyAreasRegionList] = None,
    ):
        # The area ID.
        self.area_id = area_id
        # The area name.
        self.local_name = local_name
        # The information about the regions.
        self.region_list = region_list

    def validate(self):
        if self.region_list:
            for v1 in self.region_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        result['RegionList'] = []
        if self.region_list is not None:
            for k1 in self.region_list:
                result['RegionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        self.region_list = []
        if m.get('RegionList') is not None:
            for k1 in m.get('RegionList'):
                temp_model = main_models.ListCommonAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k1))

        return self

class ListCommonAreasResponseBodyAreasRegionList(DaraModel):
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

