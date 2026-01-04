# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ddoscoo20200101 import models as main_models
from darabonba.model import DaraModel

class DescribePortCcAttackTopIPResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        top_ip: List[main_models.DescribePortCcAttackTopIPResponseBodyTopIp] = None,
    ):
        # The request ID, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The top IP addresses from which most attacks are initiated.
        self.top_ip = top_ip

    def validate(self):
        if self.top_ip:
            for v1 in self.top_ip:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['TopIp'] = []
        if self.top_ip is not None:
            for k1 in self.top_ip:
                result['TopIp'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.top_ip = []
        if m.get('TopIp') is not None:
            for k1 in m.get('TopIp'):
                temp_model = main_models.DescribePortCcAttackTopIPResponseBodyTopIp()
                self.top_ip.append(temp_model.from_map(k1))

        return self

class DescribePortCcAttackTopIPResponseBodyTopIp(DaraModel):
    def __init__(
        self,
        area_id: str = None,
        pv: int = None,
        src_ip: str = None,
    ):
        # The code of the location from which the attack is initiated. For more information, see [Codes of administrative regions in China and codes of countries and areas](https://help.aliyun.com/document_detail/167926.html). For example, **110000** indicates Beijing, China, and **us** indicates the United States.
        self.area_id = area_id
        # The number of attacks from the IP address.
        self.pv = pv
        # The source IP address of the attack.
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

        if self.pv is not None:
            result['Pv'] = self.pv

        if self.src_ip is not None:
            result['SrcIp'] = self.src_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AreaId') is not None:
            self.area_id = m.get('AreaId')

        if m.get('Pv') is not None:
            self.pv = m.get('Pv')

        if m.get('SrcIp') is not None:
            self.src_ip = m.get('SrcIp')

        return self

