# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudfw20171207 import models as main_models
from darabonba.model import DaraModel

class DescribeOutgoingDestinationResponseBody(DaraModel):
    def __init__(
        self,
        dst_list: List[main_models.DescribeOutgoingDestinationResponseBodyDstList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.dst_list = dst_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.dst_list:
            for v1 in self.dst_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DstList'] = []
        if self.dst_list is not None:
            for k1 in self.dst_list:
                result['DstList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dst_list = []
        if m.get('DstList') is not None:
            for k1 in m.get('DstList'):
                temp_model = main_models.DescribeOutgoingDestinationResponseBodyDstList()
                self.dst_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeOutgoingDestinationResponseBodyDstList(DaraModel):
    def __init__(
        self,
        acl_recommend_detail: str = None,
        acl_status: str = None,
        business: str = None,
        category_id: str = None,
        category_name: str = None,
        dst_domain: str = None,
        dst_ip: str = None,
        dst_type: str = None,
        group_name: str = None,
        has_acl_recommend: bool = None,
        in_bytes: int = None,
        is_mark_normal: bool = None,
        out_bytes: int = None,
        session_count: int = None,
        tag_list: List[main_models.DescribeOutgoingDestinationResponseBodyDstListTagList] = None,
    ):
        self.acl_recommend_detail = acl_recommend_detail
        self.acl_status = acl_status
        self.business = business
        self.category_id = category_id
        self.category_name = category_name
        self.dst_domain = dst_domain
        self.dst_ip = dst_ip
        self.dst_type = dst_type
        self.group_name = group_name
        self.has_acl_recommend = has_acl_recommend
        self.in_bytes = in_bytes
        self.is_mark_normal = is_mark_normal
        self.out_bytes = out_bytes
        self.session_count = session_count
        self.tag_list = tag_list

    def validate(self):
        if self.tag_list:
            for v1 in self.tag_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl_recommend_detail is not None:
            result['AclRecommendDetail'] = self.acl_recommend_detail

        if self.acl_status is not None:
            result['AclStatus'] = self.acl_status

        if self.business is not None:
            result['Business'] = self.business

        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.dst_domain is not None:
            result['DstDomain'] = self.dst_domain

        if self.dst_ip is not None:
            result['DstIP'] = self.dst_ip

        if self.dst_type is not None:
            result['DstType'] = self.dst_type

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.has_acl_recommend is not None:
            result['HasAclRecommend'] = self.has_acl_recommend

        if self.in_bytes is not None:
            result['InBytes'] = self.in_bytes

        if self.is_mark_normal is not None:
            result['IsMarkNormal'] = self.is_mark_normal

        if self.out_bytes is not None:
            result['OutBytes'] = self.out_bytes

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        result['TagList'] = []
        if self.tag_list is not None:
            for k1 in self.tag_list:
                result['TagList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclRecommendDetail') is not None:
            self.acl_recommend_detail = m.get('AclRecommendDetail')

        if m.get('AclStatus') is not None:
            self.acl_status = m.get('AclStatus')

        if m.get('Business') is not None:
            self.business = m.get('Business')

        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('DstDomain') is not None:
            self.dst_domain = m.get('DstDomain')

        if m.get('DstIP') is not None:
            self.dst_ip = m.get('DstIP')

        if m.get('DstType') is not None:
            self.dst_type = m.get('DstType')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('HasAclRecommend') is not None:
            self.has_acl_recommend = m.get('HasAclRecommend')

        if m.get('InBytes') is not None:
            self.in_bytes = m.get('InBytes')

        if m.get('IsMarkNormal') is not None:
            self.is_mark_normal = m.get('IsMarkNormal')

        if m.get('OutBytes') is not None:
            self.out_bytes = m.get('OutBytes')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        self.tag_list = []
        if m.get('TagList') is not None:
            for k1 in m.get('TagList'):
                temp_model = main_models.DescribeOutgoingDestinationResponseBodyDstListTagList()
                self.tag_list.append(temp_model.from_map(k1))

        return self

class DescribeOutgoingDestinationResponseBodyDstListTagList(DaraModel):
    def __init__(
        self,
        risk_level: int = None,
        tag_describe: str = None,
        tag_id: str = None,
        tag_name: str = None,
    ):
        self.risk_level = risk_level
        self.tag_describe = tag_describe
        self.tag_id = tag_id
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.tag_describe is not None:
            result['TagDescribe'] = self.tag_describe

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('TagDescribe') is not None:
            self.tag_describe = m.get('TagDescribe')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

