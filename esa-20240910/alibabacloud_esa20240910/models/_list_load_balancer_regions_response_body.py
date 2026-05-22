# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListLoadBalancerRegionsResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        regions: List[main_models.ListLoadBalancerRegionsResponseBodyRegions] = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.regions = regions
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.regions:
            for v1 in self.regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.ListLoadBalancerRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListLoadBalancerRegionsResponseBodyRegions(DaraModel):
    def __init__(
        self,
        region_cn_name: str = None,
        region_code: str = None,
        region_en_name: str = None,
        sub_regions: List[main_models.ListLoadBalancerRegionsResponseBodyRegionsSubRegions] = None,
    ):
        self.region_cn_name = region_cn_name
        self.region_code = region_code
        self.region_en_name = region_en_name
        self.sub_regions = sub_regions

    def validate(self):
        if self.sub_regions:
            for v1 in self.sub_regions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_cn_name is not None:
            result['RegionCnName'] = self.region_cn_name

        if self.region_code is not None:
            result['RegionCode'] = self.region_code

        if self.region_en_name is not None:
            result['RegionEnName'] = self.region_en_name

        result['SubRegions'] = []
        if self.sub_regions is not None:
            for k1 in self.sub_regions:
                result['SubRegions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionCnName') is not None:
            self.region_cn_name = m.get('RegionCnName')

        if m.get('RegionCode') is not None:
            self.region_code = m.get('RegionCode')

        if m.get('RegionEnName') is not None:
            self.region_en_name = m.get('RegionEnName')

        self.sub_regions = []
        if m.get('SubRegions') is not None:
            for k1 in m.get('SubRegions'):
                temp_model = main_models.ListLoadBalancerRegionsResponseBodyRegionsSubRegions()
                self.sub_regions.append(temp_model.from_map(k1))

        return self

class ListLoadBalancerRegionsResponseBodyRegionsSubRegions(DaraModel):
    def __init__(
        self,
        sub_region_cn_name: str = None,
        sub_region_code: str = None,
        sub_region_en_name: str = None,
    ):
        self.sub_region_cn_name = sub_region_cn_name
        self.sub_region_code = sub_region_code
        self.sub_region_en_name = sub_region_en_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sub_region_cn_name is not None:
            result['SubRegionCnName'] = self.sub_region_cn_name

        if self.sub_region_code is not None:
            result['SubRegionCode'] = self.sub_region_code

        if self.sub_region_en_name is not None:
            result['SubRegionEnName'] = self.sub_region_en_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubRegionCnName') is not None:
            self.sub_region_cn_name = m.get('SubRegionCnName')

        if m.get('SubRegionCode') is not None:
            self.sub_region_code = m.get('SubRegionCode')

        if m.get('SubRegionEnName') is not None:
            self.sub_region_en_name = m.get('SubRegionEnName')

        return self

