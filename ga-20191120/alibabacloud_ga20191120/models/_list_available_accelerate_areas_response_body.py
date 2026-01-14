# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ga20191120 import models as main_models
from darabonba.model import DaraModel

class ListAvailableAccelerateAreasResponseBody(DaraModel):
    def __init__(
        self,
        areas: List[main_models.ListAvailableAccelerateAreasResponseBodyAreas] = None,
        request_id: str = None,
    ):
        # The information about acceleration areas.
        self.areas = areas
        # The ID of the request.
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
                temp_model = main_models.ListAvailableAccelerateAreasResponseBodyAreas()
                self.areas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAvailableAccelerateAreasResponseBodyAreas(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        local_name: str = None,
        region_list: List[main_models.ListAvailableAccelerateAreasResponseBodyAreasRegionList] = None,
    ):
        # The ID of the acceleration area.
        self.area_id = area_id
        # The acceleration area name.
        self.local_name = local_name
        # The information about acceleration regions.
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
                temp_model = main_models.ListAvailableAccelerateAreasResponseBodyAreasRegionList()
                self.region_list.append(temp_model.from_map(k1))

        return self

class ListAvailableAccelerateAreasResponseBodyAreasRegionList(DaraModel):
    def __init__(
        self,
        china_mainland: bool = None,
        isp_type_list: List[str] = None,
        local_name: str = None,
        multi_az: bool = None,
        region_id: str = None,
        support_ipv_6: bool = None,
    ):
        # Indicates whether the region is in the Chinese mainland. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.china_mainland = china_mainland
        # The line type of the elastic IP address (EIP) in the acceleration region. Valid values:
        # 
        # *   **BGP**: BGP (Multi-ISP) lines.
        # *   **BGP_PRO**: BGP (Multi-ISP) Pro lines.
        self.isp_type_list = isp_type_list
        # The acceleration region name.
        self.local_name = local_name
        # Indicates whether multiple zones are supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.multi_az = multi_az
        # The ID of the acceleration region.
        self.region_id = region_id
        # Indicates whether IPv6 is supported. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.support_ipv_6 = support_ipv_6

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.china_mainland is not None:
            result['ChinaMainland'] = self.china_mainland

        if self.isp_type_list is not None:
            result['IspTypeList'] = self.isp_type_list

        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.multi_az is not None:
            result['MultiAz'] = self.multi_az

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.support_ipv_6 is not None:
            result['SupportIpv6'] = self.support_ipv_6

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChinaMainland') is not None:
            self.china_mainland = m.get('ChinaMainland')

        if m.get('IspTypeList') is not None:
            self.isp_type_list = m.get('IspTypeList')

        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('MultiAz') is not None:
            self.multi_az = m.get('MultiAz')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SupportIpv6') is not None:
            self.support_ipv_6 = m.get('SupportIpv6')

        return self

