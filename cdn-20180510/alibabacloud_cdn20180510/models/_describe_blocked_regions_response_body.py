# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class DescribeBlockedRegionsResponseBody(DaraModel):
    def __init__(
        self,
        info_list: main_models.DescribeBlockedRegionsResponseBodyInfoList = None,
        request_id: str = None,
    ):
        self.info_list = info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.info_list:
            self.info_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info_list is not None:
            result['InfoList'] = self.info_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InfoList') is not None:
            temp_model = main_models.DescribeBlockedRegionsResponseBodyInfoList()
            self.info_list = temp_model.from_map(m.get('InfoList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeBlockedRegionsResponseBodyInfoList(DaraModel):
    def __init__(
        self,
        info_item: List[main_models.DescribeBlockedRegionsResponseBodyInfoListInfoItem] = None,
    ):
        self.info_item = info_item

    def validate(self):
        if self.info_item:
            for v1 in self.info_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InfoItem'] = []
        if self.info_item is not None:
            for k1 in self.info_item:
                result['InfoItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.info_item = []
        if m.get('InfoItem') is not None:
            for k1 in m.get('InfoItem'):
                temp_model = main_models.DescribeBlockedRegionsResponseBodyInfoListInfoItem()
                self.info_item.append(temp_model.from_map(k1))

        return self

class DescribeBlockedRegionsResponseBodyInfoListInfoItem(DaraModel):
    def __init__(
        self,
        continent: str = None,
        countries_and_regions: str = None,
        countries_and_regions_name: str = None,
    ):
        self.continent = continent
        self.countries_and_regions = countries_and_regions
        self.countries_and_regions_name = countries_and_regions_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.continent is not None:
            result['Continent'] = self.continent

        if self.countries_and_regions is not None:
            result['CountriesAndRegions'] = self.countries_and_regions

        if self.countries_and_regions_name is not None:
            result['CountriesAndRegionsName'] = self.countries_and_regions_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')

        if m.get('CountriesAndRegions') is not None:
            self.countries_and_regions = m.get('CountriesAndRegions')

        if m.get('CountriesAndRegionsName') is not None:
            self.countries_and_regions_name = m.get('CountriesAndRegionsName')

        return self

