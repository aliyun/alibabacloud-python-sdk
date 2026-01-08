# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallDomainRelationListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVpcFirewallDomainRelationListResponseBodyDataList] = None,
        dst_vpc_list: List[main_models.DescribeVpcFirewallDomainRelationListResponseBodyDstVpcList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_list = data_list
        self.dst_vpc_list = dst_vpc_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.data_list:
            for v1 in self.data_list:
                 if v1:
                    v1.validate()
        if self.dst_vpc_list:
            for v1 in self.dst_vpc_list:
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

        result['DstVpcList'] = []
        if self.dst_vpc_list is not None:
            for k1 in self.dst_vpc_list:
                result['DstVpcList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVpcFirewallDomainRelationListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        self.dst_vpc_list = []
        if m.get('DstVpcList') is not None:
            for k1 in m.get('DstVpcList'):
                temp_model = main_models.DescribeVpcFirewallDomainRelationListResponseBodyDstVpcList()
                self.dst_vpc_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallDomainRelationListResponseBodyDstVpcList(DaraModel):
    def __init__(
        self,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

class DescribeVpcFirewallDomainRelationListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        business: str = None,
        domain: str = None,
        dst_ip: str = None,
        dst_region_id: str = None,
        dst_vpc_id: str = None,
        dst_vpc_name: str = None,
        first_time: int = None,
        group_name: str = None,
        ips_hit_cnt: int = None,
        last_time: int = None,
        request_bytes: int = None,
        response_bytes: int = None,
        session_count: int = None,
        src_ip: str = None,
        src_region_id: str = None,
        src_vpc_id: str = None,
        src_vpc_name: str = None,
        total_bytes: int = None,
    ):
        self.business = business
        self.domain = domain
        self.dst_ip = dst_ip
        self.dst_region_id = dst_region_id
        self.dst_vpc_id = dst_vpc_id
        self.dst_vpc_name = dst_vpc_name
        self.first_time = first_time
        self.group_name = group_name
        self.ips_hit_cnt = ips_hit_cnt
        self.last_time = last_time
        self.request_bytes = request_bytes
        self.response_bytes = response_bytes
        self.session_count = session_count
        self.src_ip = src_ip
        self.src_region_id = src_region_id
        self.src_vpc_id = src_vpc_id
        self.src_vpc_name = src_vpc_name
        self.total_bytes = total_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business is not None:
            result['Business'] = self.business

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_region_id is not None:
            result['DstRegionId'] = self.dst_region_id

        if self.dst_vpc_id is not None:
            result['DstVpcId'] = self.dst_vpc_id

        if self.dst_vpc_name is not None:
            result['DstVpcName'] = self.dst_vpc_name

        if self.first_time is not None:
            result['FirstTime'] = self.first_time

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.ips_hit_cnt is not None:
            result['IpsHitCnt'] = self.ips_hit_cnt

        if self.last_time is not None:
            result['LastTime'] = self.last_time

        if self.request_bytes is not None:
            result['RequestBytes'] = self.request_bytes

        if self.response_bytes is not None:
            result['ResponseBytes'] = self.response_bytes

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.src_ip is not None:
            result['SrcIP'] = self.src_ip

        if self.src_region_id is not None:
            result['SrcRegionId'] = self.src_region_id

        if self.src_vpc_id is not None:
            result['SrcVpcId'] = self.src_vpc_id

        if self.src_vpc_name is not None:
            result['SrcVpcName'] = self.src_vpc_name

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstRegionId') is not None:
            self.dst_region_id = m.get('DstRegionId')

        if m.get('DstVpcId') is not None:
            self.dst_vpc_id = m.get('DstVpcId')

        if m.get('DstVpcName') is not None:
            self.dst_vpc_name = m.get('DstVpcName')

        if m.get('FirstTime') is not None:
            self.first_time = m.get('FirstTime')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('IpsHitCnt') is not None:
            self.ips_hit_cnt = m.get('IpsHitCnt')

        if m.get('LastTime') is not None:
            self.last_time = m.get('LastTime')

        if m.get('RequestBytes') is not None:
            self.request_bytes = m.get('RequestBytes')

        if m.get('ResponseBytes') is not None:
            self.response_bytes = m.get('ResponseBytes')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SrcIP') is not None:
            self.src_ip = m.get('SrcIP')

        if m.get('SrcRegionId') is not None:
            self.src_region_id = m.get('SrcRegionId')

        if m.get('SrcVpcId') is not None:
            self.src_vpc_id = m.get('SrcVpcId')

        if m.get('SrcVpcName') is not None:
            self.src_vpc_name = m.get('SrcVpcName')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

