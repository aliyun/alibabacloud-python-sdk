# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vpc20160428 import models as main_models
from darabonba.model import DaraModel

class DescribeEipGatewayInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        eip_infos: main_models.DescribeEipGatewayInfoResponseBodyEipInfos = None,
        message: str = None,
        request_id: str = None,
    ):
        # The status code of the operation.
        self.code = code
        # The detailed information about the EIP.
        self.eip_infos = eip_infos
        # The result of the operation.
        self.message = message
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.eip_infos:
            self.eip_infos.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.eip_infos is not None:
            result['EipInfos'] = self.eip_infos.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('EipInfos') is not None:
            temp_model = main_models.DescribeEipGatewayInfoResponseBodyEipInfos()
            self.eip_infos = temp_model.from_map(m.get('EipInfos'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEipGatewayInfoResponseBodyEipInfos(DaraModel):
    def __init__(
        self,
        eip_info: List[main_models.DescribeEipGatewayInfoResponseBodyEipInfosEipInfo] = None,
    ):
        self.eip_info = eip_info

    def validate(self):
        if self.eip_info:
            for v1 in self.eip_info:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipInfo'] = []
        if self.eip_info is not None:
            for k1 in self.eip_info:
                result['EipInfo'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_info = []
        if m.get('EipInfo') is not None:
            for k1 in m.get('EipInfo'):
                temp_model = main_models.DescribeEipGatewayInfoResponseBodyEipInfosEipInfo()
                self.eip_info.append(temp_model.from_map(k1))

        return self

class DescribeEipGatewayInfoResponseBodyEipInfosEipInfo(DaraModel):
    def __init__(
        self,
        ip: str = None,
        ip_gw: str = None,
        ip_mask: str = None,
    ):
        # The IP address of the EIP.
        self.ip = ip
        # The IP address of the gateway that is associated with the EIP.
        self.ip_gw = ip_gw
        # The subnet mask of the EIP.
        self.ip_mask = ip_mask

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['Ip'] = self.ip

        if self.ip_gw is not None:
            result['IpGw'] = self.ip_gw

        if self.ip_mask is not None:
            result['IpMask'] = self.ip_mask

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('IpGw') is not None:
            self.ip_gw = m.get('IpGw')

        if m.get('IpMask') is not None:
            self.ip_mask = m.get('IpMask')

        return self

