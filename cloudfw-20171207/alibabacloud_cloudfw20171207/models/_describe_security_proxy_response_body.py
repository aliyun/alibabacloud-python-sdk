# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeSecurityProxyResponseBody(DaraModel):
    def __init__(
        self,
        proxy_list: List[main_models.DescribeSecurityProxyResponseBodyProxyList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.proxy_list = proxy_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.proxy_list:
            for v1 in self.proxy_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProxyList'] = []
        if self.proxy_list is not None:
            for k1 in self.proxy_list:
                result['ProxyList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.proxy_list = []
        if m.get('ProxyList') is not None:
            for k1 in m.get('ProxyList'):
                temp_model = main_models.DescribeSecurityProxyResponseBodyProxyList()
                self.proxy_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeSecurityProxyResponseBodyProxyList(DaraModel):
    def __init__(
        self,
        cidr_block: str = None,
        detail: str = None,
        member_uid: str = None,
        nat_gateway_id: str = None,
        nat_gateway_name: str = None,
        proxy_id: str = None,
        proxy_name: str = None,
        region_no: str = None,
        snat_ip_list: List[str] = None,
        status: str = None,
        strict_mode: int = None,
        v_switch_id: str = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.cidr_block = cidr_block
        self.detail = detail
        self.member_uid = member_uid
        self.nat_gateway_id = nat_gateway_id
        self.nat_gateway_name = nat_gateway_name
        self.proxy_id = proxy_id
        self.proxy_name = proxy_name
        self.region_no = region_no
        self.snat_ip_list = snat_ip_list
        self.status = status
        self.strict_mode = strict_mode
        self.v_switch_id = v_switch_id
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cidr_block is not None:
            result['CidrBlock'] = self.cidr_block

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.member_uid is not None:
            result['MemberUid'] = self.member_uid

        if self.nat_gateway_id is not None:
            result['NatGatewayId'] = self.nat_gateway_id

        if self.nat_gateway_name is not None:
            result['NatGatewayName'] = self.nat_gateway_name

        if self.proxy_id is not None:
            result['ProxyId'] = self.proxy_id

        if self.proxy_name is not None:
            result['ProxyName'] = self.proxy_name

        if self.region_no is not None:
            result['RegionNo'] = self.region_no

        if self.snat_ip_list is not None:
            result['SnatIpList'] = self.snat_ip_list

        if self.status is not None:
            result['Status'] = self.status

        if self.strict_mode is not None:
            result['StrictMode'] = self.strict_mode

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CidrBlock') is not None:
            self.cidr_block = m.get('CidrBlock')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('MemberUid') is not None:
            self.member_uid = m.get('MemberUid')

        if m.get('NatGatewayId') is not None:
            self.nat_gateway_id = m.get('NatGatewayId')

        if m.get('NatGatewayName') is not None:
            self.nat_gateway_name = m.get('NatGatewayName')

        if m.get('ProxyId') is not None:
            self.proxy_id = m.get('ProxyId')

        if m.get('ProxyName') is not None:
            self.proxy_name = m.get('ProxyName')

        if m.get('RegionNo') is not None:
            self.region_no = m.get('RegionNo')

        if m.get('SnatIpList') is not None:
            self.snat_ip_list = m.get('SnatIpList')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrictMode') is not None:
            self.strict_mode = m.get('StrictMode')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

