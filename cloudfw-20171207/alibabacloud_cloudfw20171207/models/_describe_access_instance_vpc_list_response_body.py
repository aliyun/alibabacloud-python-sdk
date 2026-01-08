# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeAccessInstanceVpcListResponseBody(DaraModel):
    def __init__(
        self,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vpc_list: List[main_models.DescribeAccessInstanceVpcListResponseBodyVpcList] = None,
    ):
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.vpc_list = vpc_list

    def validate(self):
        if self.vpc_list:
            for v1 in self.vpc_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VpcList'] = []
        if self.vpc_list is not None:
            for k1 in self.vpc_list:
                result['VpcList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.vpc_list = []
        if m.get('VpcList') is not None:
            for k1 in m.get('VpcList'):
                temp_model = main_models.DescribeAccessInstanceVpcListResponseBodyVpcList()
                self.vpc_list.append(temp_model.from_map(k1))

        return self

class DescribeAccessInstanceVpcListResponseBodyVpcList(DaraModel):
    def __init__(
        self,
        firewall_vpc: bool = None,
        vpc_id: str = None,
        vpc_name: str = None,
    ):
        self.firewall_vpc = firewall_vpc
        self.vpc_id = vpc_id
        self.vpc_name = vpc_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.firewall_vpc is not None:
            result['FirewallVpc'] = self.firewall_vpc

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        if self.vpc_name is not None:
            result['VpcName'] = self.vpc_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirewallVpc') is not None:
            self.firewall_vpc = m.get('FirewallVpc')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        if m.get('VpcName') is not None:
            self.vpc_name = m.get('VpcName')

        return self

