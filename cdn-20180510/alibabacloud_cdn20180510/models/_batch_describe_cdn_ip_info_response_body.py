# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cdn20180510 import models as main_models
from darabonba.model import DaraModel

class BatchDescribeCdnIpInfoResponseBody(DaraModel):
    def __init__(
        self,
        ip_info_list: List[main_models.BatchDescribeCdnIpInfoResponseBodyIpInfoList] = None,
        request_id: str = None,
    ):
        # The results about IP addresses returned.
        self.ip_info_list = ip_info_list
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ip_info_list:
            for v1 in self.ip_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpInfoList'] = []
        if self.ip_info_list is not None:
            for k1 in self.ip_info_list:
                result['IpInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_info_list = []
        if m.get('IpInfoList') is not None:
            for k1 in m.get('IpInfoList'):
                temp_model = main_models.BatchDescribeCdnIpInfoResponseBodyIpInfoList()
                self.ip_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class BatchDescribeCdnIpInfoResponseBodyIpInfoList(DaraModel):
    def __init__(
        self,
        cdn_ip: str = None,
        city: str = None,
        country: str = None,
        ip_address: str = None,
        isp_name: str = None,
        province: str = None,
    ):
        # Indicates whether the IP address belongs to an Alibaba Cloud CDN point of presence (POP).
        # 
        # *   **true**
        # *   **false**
        self.cdn_ip = cdn_ip
        # The city to which the IP address belongs.
        self.city = city
        # The country to which the IP address belongs.
        self.country = country
        # The IP address.
        self.ip_address = ip_address
        # The ISP to which the IP address belongs.
        self.isp_name = isp_name
        # The province to which the IP address belongs.
        self.province = province

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cdn_ip is not None:
            result['CdnIp'] = self.cdn_ip

        if self.city is not None:
            result['City'] = self.city

        if self.country is not None:
            result['Country'] = self.country

        if self.ip_address is not None:
            result['IpAddress'] = self.ip_address

        if self.isp_name is not None:
            result['IspName'] = self.isp_name

        if self.province is not None:
            result['Province'] = self.province

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CdnIp') is not None:
            self.cdn_ip = m.get('CdnIp')

        if m.get('City') is not None:
            self.city = m.get('City')

        if m.get('Country') is not None:
            self.country = m.get('Country')

        if m.get('IpAddress') is not None:
            self.ip_address = m.get('IpAddress')

        if m.get('IspName') is not None:
            self.isp_name = m.get('IspName')

        if m.get('Province') is not None:
            self.province = m.get('Province')

        return self

