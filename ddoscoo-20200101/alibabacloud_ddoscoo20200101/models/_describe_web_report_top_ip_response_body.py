# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeWebReportTopIpResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeWebReportTopIpResponseBodyDataList] = None,
        request_id: str = None,
    ):
        # The information about the IP addresses.
        self.data_list = data_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DataList'] = []
        if self.data_list is not None:
            for k1 in self.data_list:
                result['DataList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeWebReportTopIpResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeWebReportTopIpResponseBodyDataList(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        count: int = None,
        isp: str = None,
        source_ip: str = None,
    ):
        # The ID of the location.
        self.area_id = area_id
        # The number of entries returned.
        self.count = count
        # The Internet service provider (ISP) for the attack. Valid values:
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
        # The source IP address.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area_id is not None:
            result['AreaId'] = self.area_id

        if self.count is not None:
            result['Count'] = self.count

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self

