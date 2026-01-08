# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeVpcFirewallDomainListResponseBody(DaraModel):
    def __init__(
        self,
        data_list: List[main_models.DescribeVpcFirewallDomainListResponseBodyDataList] = None,
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
                temp_model = main_models.DescribeVpcFirewallDomainListResponseBodyDataList()
                self.data_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeVpcFirewallDomainListResponseBodyDataList(DaraModel):
    def __init__(
        self,
        application_name_list: List[str] = None,
        business: str = None,
        domain: str = None,
        group_name: str = None,
        request_bytes: int = None,
        response_bytes: int = None,
        session_count: int = None,
        src_ip_count: int = None,
        src_vpc_count: int = None,
        total_bytes: int = None,
    ):
        self.application_name_list = application_name_list
        self.business = business
        self.domain = domain
        self.group_name = group_name
        self.request_bytes = request_bytes
        self.response_bytes = response_bytes
        self.session_count = session_count
        self.src_ip_count = src_ip_count
        self.src_vpc_count = src_vpc_count
        self.total_bytes = total_bytes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name_list is not None:
            result['ApplicationNameList'] = self.application_name_list

        if self.business is not None:
            result['Business'] = self.business

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.request_bytes is not None:
            result['RequestBytes'] = self.request_bytes

        if self.response_bytes is not None:
            result['ResponseBytes'] = self.response_bytes

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.src_ip_count is not None:
            result['SrcIpCount'] = self.src_ip_count

        if self.src_vpc_count is not None:
            result['SrcVpcCount'] = self.src_vpc_count

        if self.total_bytes is not None:
            result['TotalBytes'] = self.total_bytes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationNameList') is not None:
            self.application_name_list = m.get('ApplicationNameList')

        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('RequestBytes') is not None:
            self.request_bytes = m.get('RequestBytes')

        if m.get('ResponseBytes') is not None:
            self.response_bytes = m.get('ResponseBytes')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SrcIpCount') is not None:
            self.src_ip_count = m.get('SrcIpCount')

        if m.get('SrcVpcCount') is not None:
            self.src_vpc_count = m.get('SrcVpcCount')

        if m.get('TotalBytes') is not None:
            self.total_bytes = m.get('TotalBytes')

        return self

