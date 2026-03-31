# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeIpAbroadCountryInfosResponseBody(DaraModel):
    def __init__(
        self,
        abroad_infos: List[main_models.DescribeIpAbroadCountryInfosResponseBodyAbroadInfos] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.abroad_infos = abroad_infos
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.abroad_infos:
            for v1 in self.abroad_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AbroadInfos'] = []
        if self.abroad_infos is not None:
            for k1 in self.abroad_infos:
                result['AbroadInfos'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.abroad_infos = []
        if m.get('AbroadInfos') is not None:
            for k1 in m.get('AbroadInfos'):
                temp_model = main_models.DescribeIpAbroadCountryInfosResponseBodyAbroadInfos()
                self.abroad_infos.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpAbroadCountryInfosResponseBodyAbroadInfos(DaraModel):
    def __init__(
        self,
        continent: str = None,
        country: str = None,
        country_name: str = None,
        regions: List[main_models.DescribeIpAbroadCountryInfosResponseBodyAbroadInfosRegions] = None,
    ):
        self.continent = continent
        self.country = country
        self.country_name = country_name
        self.regions = regions

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
        if self.continent is not None:
            result['Continent'] = self.continent

        if self.country is not None:
            result['Country'] = self.country

        if self.country_name is not None:
            result['CountryName'] = self.country_name

        result['Regions'] = []
        if self.regions is not None:
            for k1 in self.regions:
                result['Regions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Continent') is not None:
            self.continent = m.get('Continent')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CountryName') is not None:
            self.country_name = m.get('CountryName')

        self.regions = []
        if m.get('Regions') is not None:
            for k1 in m.get('Regions'):
                temp_model = main_models.DescribeIpAbroadCountryInfosResponseBodyAbroadInfosRegions()
                self.regions.append(temp_model.from_map(k1))

        return self

class DescribeIpAbroadCountryInfosResponseBodyAbroadInfosRegions(DaraModel):
    def __init__(
        self,
        abroad_region_id: str = None,
        abroad_region_name: str = None,
    ):
        self.abroad_region_id = abroad_region_id
        self.abroad_region_name = abroad_region_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.abroad_region_id is not None:
            result['AbroadRegionId'] = self.abroad_region_id

        if self.abroad_region_name is not None:
            result['AbroadRegionName'] = self.abroad_region_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AbroadRegionId') is not None:
            self.abroad_region_id = m.get('AbroadRegionId')

        if m.get('AbroadRegionName') is not None:
            self.abroad_region_name = m.get('AbroadRegionName')

        return self

