# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallTrafficAssetListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVpcFirewallTrafficAssetListResponseBodyDataList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data_list = data_list
        self.request_id = request_id
        self.total_count = total_count

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

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k1 in m.get('DataList'):
                temp_model = main_models.DescribeVpcFirewallTrafficAssetListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallTrafficAssetListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        ip: str = None,
        ips_hit_cnt: int = None,
        session_count: int = None,
        total_bytes: int = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.ip = ip
        self.ips_hit_cnt = ips_hit_cnt
        self.session_count = session_count
        self.total_bytes = total_bytes
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip is not None:
            result['IP'] = self.ip

        if self.ips_hit_cnt is not None:
            result['IpsHitCnt'] = self.ips_hit_cnt

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('IpsHitCnt') is not None:
            self.ips_hit_cnt = m.get('IpsHitCnt')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

