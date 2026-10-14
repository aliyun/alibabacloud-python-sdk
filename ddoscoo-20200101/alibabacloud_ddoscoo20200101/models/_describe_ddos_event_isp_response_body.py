# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribeDDosEventIspResponseBody(DaraModel):
    def __init__(
        self,
        isps: List[main_models.DescribeDDosEventIspResponseBodyIsps] = None,
        request_id: str = None,
    ):
        # The ISP information of attack sources.
        self.isps = isps
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.isps:
            for v1 in self.isps:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Isps'] = []
        if self.isps is not None:
            for k1 in self.isps:
                result['Isps'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.isps = []
        if m.get('Isps') is not None:
            for k1 in m.get('Isps'):
                temp_model = main_models.DescribeDDosEventIspResponseBodyIsps()
                self.isps.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDDosEventIspResponseBodyIsps(DaraModel):
    def __init__(
        self,
        in_pkts: int = None,
        isp: str = None,
    ):
        # The number of request packets from the ISP.
        self.in_pkts = in_pkts
        # The code of the attack source ISP. Valid values:
        # 
        # - **100017**: China Telecom
        # - **100026**: China Unicom
        # - **100025**: China Mobile
        # - **100027**: CERNET
        # - **100020**: China Tietong
        # - **1000143**: Dr. Peng
        # - **100080**: Gehua
        # - **1000139**: China Broadcasting Network
        # - **100023**: Youxiantong
        # - **100063**: Founder Broadband
        # - **1000337**: Haokuan Network
        # - **100021**: 21Vianet
        # - **1000333**: Wasu Media
        # - **100093**: ChinaNetCenter
        # - **1000401**: Tencent
        # - **100099**: Baidu
        # - **1000323**: Alibaba Cloud
        # - **100098**: Alibaba
        self.isp = isp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_pkts is not None:
            result['InPkts'] = self.in_pkts

        if self.isp is not None:
            result['Isp'] = self.isp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InPkts') is not None:
            self.in_pkts = m.get('InPkts')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        return self

