# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDosEventSrcIpResponseBody(DaraModel):
    def __init__(
        self,
        ips: List[main_models.DescribeDDosEventSrcIpResponseBodyIps] = None,
        request_id: str = None,
    ):
        # An array that consists of information about the source IP address of the volumetric attack.
        self.ips = ips
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.ips:
            for v1 in self.ips:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Ips'] = []
        if self.ips is not None:
            for k1 in self.ips:
                result['Ips'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ips = []
        if m.get('Ips') is not None:
            for k1 in m.get('Ips'):
                temp_model = main_models.DescribeDDosEventSrcIpResponseBodyIps()
                self.ips.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDDosEventSrcIpResponseBodyIps(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        isp: str = None,
        src_ip: str = None,
    ):
        # The code or ID of the source region. For more information, see [Codes of administrative regions in China and codes of countries and areas](https://help.aliyun.com/document_detail/167926.html). For example, **110000** indicates Beijing, China, and **us** indicates the United States.
        self.area_id = area_id
        # The Internet service provider (ISP) for the volumetric attack. Valid values:
        # 
        # *   **100017**: China Telecom
        # *   **100026**: China Unicom
        # *   **100025**: China Mobile
        # *   **100027**: China Education and Research Network
        # *   **100020**: China Mobile Tietong
        # *   **1000143**: Dr.Peng Telecom & Media Group
        # *   **100080**: Beijing Gehua CATV Network
        # *   **1000139**: National Radio and Television Administration
        # *   **100023**: Oriental Cable Network
        # *   **100063**: Founder Broadband
        # *   **1000337**: China Internet Exchange
        # *   **100021**: 21Vianet Group
        # *   **1000333**: Wasu Media Holding
        # *   **100093**: Wangsu Science & Technology
        # *   **1000401**: Tencent
        # *   **100099**: Baidu
        # *   **1000323**: Alibaba Cloud
        # *   **100098**: Alibaba
        self.isp = isp
        # The source IP address of the volumetric attack.
        self.src_ip = src_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

