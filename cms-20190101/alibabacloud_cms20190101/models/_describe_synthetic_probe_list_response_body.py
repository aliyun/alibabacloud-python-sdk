# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSyntheticProbeListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        isp_city_list: List[main_models.DescribeSyntheticProbeListResponseBodyIspCityList] = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        # The queried detection points.
        self.isp_city_list = isp_city_list
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.isp_city_list:
            for v1 in self.isp_city_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['IspCityList'] = []
        if self.isp_city_list is not None:
            for k1 in self.isp_city_list:
                result['IspCityList'].append(k1.to_map() if k1 else None)

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.isp_city_list = []
        if m.get('IspCityList') is not None:
            for k1 in m.get('IspCityList'):
                temp_model = main_models.DescribeSyntheticProbeListResponseBodyIspCityList()
                self.isp_city_list.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSyntheticProbeListResponseBodyIspCityList(DaraModel):
    def __init__(
        self,
        area_cn: str = None,
        area_en: str = None,
        city: str = None,
        city_cn: str = None,
        city_en: str = None,
        country: str = None,
        country_cn: str = None,
        country_en: str = None,
        idc_v4probe_count: int = None,
        idc_v6probe_count: int = None,
        ip_pool: List[str] = None,
        isp: str = None,
        isp_cn: str = None,
        isp_en: str = None,
        lm_probe_count: int = None,
        mb_probe_count: int = None,
        region: str = None,
        region_cn: str = None,
        region_en: str = None,
    ):
        self.area_cn = area_cn
        self.area_en = area_en
        self.city = city
        self.city_cn = city_cn
        self.city_en = city_en
        self.country = country
        self.country_cn = country_cn
        self.country_en = country_en
        self.idc_v4probe_count = idc_v4probe_count
        # The number of IPv6 nodes in data centers.
        self.idc_v6probe_count = idc_v6probe_count
        # The IP addresses of the monitored nodes.
        self.ip_pool = ip_pool
        self.isp = isp
        self.isp_cn = isp_cn
        self.isp_en = isp_en
        self.lm_probe_count = lm_probe_count
        self.mb_probe_count = mb_probe_count
        self.region = region
        self.region_cn = region_cn
        self.region_en = region_en

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_cn is not None:
            result['AreaCn'] = self.area_cn

        if self.area_en is not None:
            result['AreaEn'] = self.area_en

        if self.city is not None:
            result['City'] = self.city

        if self.city_cn is not None:
            result['CityCn'] = self.city_cn

        if self.city_en is not None:
            result['CityEn'] = self.city_en

        if self.country is not None:
            result['Country'] = self.country

        if self.country_cn is not None:
            result['CountryCn'] = self.country_cn

        if self.country_en is not None:
            result['CountryEn'] = self.country_en

        if self.idc_v4probe_count is not None:
            result['IdcV4ProbeCount'] = self.idc_v4probe_count

        if self.idc_v6probe_count is not None:
            result['IdcV6ProbeCount'] = self.idc_v6probe_count

        if self.ip_pool is not None:
            result['IpPool'] = self.ip_pool

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_cn is not None:
            result['IspCn'] = self.isp_cn

        if self.isp_en is not None:
            result['IspEn'] = self.isp_en

        if self.lm_probe_count is not None:
            result['LmProbeCount'] = self.lm_probe_count

        if self.mb_probe_count is not None:
            result['MbProbeCount'] = self.mb_probe_count

        if self.region is not None:
            result['Region'] = self.region

        if self.region_cn is not None:
            result['RegionCn'] = self.region_cn

        if self.region_en is not None:
            result['RegionEn'] = self.region_en

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaCn') is not None:
            self.area_cn = m.get('AreaCn')

        if m.get('AreaEn') is not None:
            self.area_en = m.get('AreaEn')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityCn') is not None:
            self.city_cn = m.get('CityCn')

        if m.get('CityEn') is not None:
            self.city_en = m.get('CityEn')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('CountryCn') is not None:
            self.country_cn = m.get('CountryCn')

        if m.get('CountryEn') is not None:
            self.country_en = m.get('CountryEn')

        if m.get('IdcV4ProbeCount') is not None:
            self.idc_v4probe_count = m.get('IdcV4ProbeCount')

        if m.get('IdcV6ProbeCount') is not None:
            self.idc_v6probe_count = m.get('IdcV6ProbeCount')

        if m.get('IpPool') is not None:
            self.ip_pool = m.get('IpPool')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspCn') is not None:
            self.isp_cn = m.get('IspCn')

        if m.get('IspEn') is not None:
            self.isp_en = m.get('IspEn')

        if m.get('LmProbeCount') is not None:
            self.lm_probe_count = m.get('LmProbeCount')

        if m.get('MbProbeCount') is not None:
            self.mb_probe_count = m.get('MbProbeCount')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RegionCn') is not None:
            self.region_cn = m.get('RegionCn')

        if m.get('RegionEn') is not None:
            self.region_en = m.get('RegionEn')

        return self

