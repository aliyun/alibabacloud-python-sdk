# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20190101 import models as main_models
from darabonba.model import DaraModel

class DescribeSiteMonitorISPCityListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        isp_city_list: main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityList = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The status code.
        # 
        # > The status code 200 indicates that the request was successful.
        self.code = code
        # The queried detection points.
        self.isp_city_list = isp_city_list
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.isp_city_list:
            self.isp_city_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.isp_city_list is not None:
            result['IspCityList'] = self.isp_city_list.to_map()

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

        if m.get('IspCityList') is not None:
            temp_model = main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityList()
            self.isp_city_list = temp_model.from_map(m.get('IspCityList'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeSiteMonitorISPCityListResponseBodyIspCityList(DaraModel):
    def __init__(
        self,
        isp_city: List[main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCity] = None,
    ):
        self.isp_city = isp_city

    def validate(self):
        if self.isp_city:
            for v1 in self.isp_city:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IspCity'] = []
        if self.isp_city is not None:
            for k1 in self.isp_city:
                result['IspCity'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isp_city = []
        if m.get('IspCity') is not None:
            for k1 in m.get('IspCity'):
                temp_model = main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCity()
                self.isp_city.append(temp_model.from_map(k1))

        return self

class DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCity(DaraModel):
    def __init__(
        self,
        area_en: str = None,
        area_zh_c_n: str = None,
        city: str = None,
        city_name_en: str = None,
        city_name_zh_c_n: str = None,
        country: str = None,
        country_en: str = None,
        country_zh_c_n: str = None,
        ippool: main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCityIPPool = None,
        ipv4probe_count: str = None,
        ipv6probe_count: str = None,
        isp: str = None,
        isp_name_en: str = None,
        isp_name_zh_c_n: str = None,
        region: str = None,
        region_en: str = None,
        region_zh_c_n: str = None,
    ):
        self.area_en = area_en
        self.area_zh_c_n = area_zh_c_n
        # The city ID.
        self.city = city
        self.city_name_en = city_name_en
        self.city_name_zh_c_n = city_name_zh_c_n
        # The country name.
        # 
        # > This parameter is valid only on the China site (aliyun.com).
        self.country = country
        self.country_en = country_en
        self.country_zh_c_n = country_zh_c_n
        # The IP address pool.
        self.ippool = ippool
        # The number of IPv4 probes.
        self.ipv4probe_count = ipv4probe_count
        # The number of IPv6 probes.
        self.ipv6probe_count = ipv6probe_count
        # The carrier ID.
        self.isp = isp
        self.isp_name_en = isp_name_en
        self.isp_name_zh_c_n = isp_name_zh_c_n
        # The province name.
        self.region = region
        self.region_en = region_en
        self.region_zh_c_n = region_zh_c_n

    def validate(self):
        if self.ippool:
            self.ippool.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_en is not None:
            result['Area.en'] = self.area_en

        if self.area_zh_c_n is not None:
            result['Area.zh_CN'] = self.area_zh_c_n

        if self.city is not None:
            result['City'] = self.city

        if self.city_name_en is not None:
            result['CityName.en'] = self.city_name_en

        if self.city_name_zh_c_n is not None:
            result['CityName.zh_CN'] = self.city_name_zh_c_n

        if self.country is not None:
            result['Country'] = self.country

        if self.country_en is not None:
            result['Country.en'] = self.country_en

        if self.country_zh_c_n is not None:
            result['Country.zh_CN'] = self.country_zh_c_n

        if self.ippool is not None:
            result['IPPool'] = self.ippool.to_map()

        if self.ipv4probe_count is not None:
            result['IPV4ProbeCount'] = self.ipv4probe_count

        if self.ipv6probe_count is not None:
            result['IPV6ProbeCount'] = self.ipv6probe_count

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.isp_name_en is not None:
            result['IspName.en'] = self.isp_name_en

        if self.isp_name_zh_c_n is not None:
            result['IspName.zh_CN'] = self.isp_name_zh_c_n

        if self.region is not None:
            result['Region'] = self.region

        if self.region_en is not None:
            result['Region.en'] = self.region_en

        if self.region_zh_c_n is not None:
            result['Region.zh_CN'] = self.region_zh_c_n

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area.en') is not None:
            self.area_en = m.get('Area.en')

        if m.get('Area.zh_CN') is not None:
            self.area_zh_c_n = m.get('Area.zh_CN')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('CityName.en') is not None:
            self.city_name_en = m.get('CityName.en')

        if m.get('CityName.zh_CN') is not None:
            self.city_name_zh_c_n = m.get('CityName.zh_CN')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('Country.en') is not None:
            self.country_en = m.get('Country.en')

        if m.get('Country.zh_CN') is not None:
            self.country_zh_c_n = m.get('Country.zh_CN')

        if m.get('IPPool') is not None:
            temp_model = main_models.DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCityIPPool()
            self.ippool = temp_model.from_map(m.get('IPPool'))

        if m.get('IPV4ProbeCount') is not None:
            self.ipv4probe_count = m.get('IPV4ProbeCount')

        if m.get('IPV6ProbeCount') is not None:
            self.ipv6probe_count = m.get('IPV6ProbeCount')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('IspName.en') is not None:
            self.isp_name_en = m.get('IspName.en')

        if m.get('IspName.zh_CN') is not None:
            self.isp_name_zh_c_n = m.get('IspName.zh_CN')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('Region.en') is not None:
            self.region_en = m.get('Region.en')

        if m.get('Region.zh_CN') is not None:
            self.region_zh_c_n = m.get('Region.zh_CN')

        return self

class DescribeSiteMonitorISPCityListResponseBodyIspCityListIspCityIPPool(DaraModel):
    def __init__(
        self,
        ippool: List[str] = None,
    ):
        self.ippool = ippool

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ippool is not None:
            result['IPPool'] = self.ippool

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IPPool') is not None:
            self.ippool = m.get('IPPool')

        return self

