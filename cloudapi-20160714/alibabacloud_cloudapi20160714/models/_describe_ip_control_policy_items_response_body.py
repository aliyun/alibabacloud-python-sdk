# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeIpControlPolicyItemsResponseBody(DaraModel):
    def __init__(
        self,
        ip_control_policy_items: main_models.DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about policies. The information is an array of IpControlPolicyItem data.
        self.ip_control_policy_items = ip_control_policy_items
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.ip_control_policy_items:
            self.ip_control_policy_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_control_policy_items is not None:
            result['IpControlPolicyItems'] = self.ip_control_policy_items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IpControlPolicyItems') is not None:
            temp_model = main_models.DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems()
            self.ip_control_policy_items = temp_model.from_map(m.get('IpControlPolicyItems'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItems(DaraModel):
    def __init__(
        self,
        ip_control_policy_item: List[main_models.DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem] = None,
    ):
        self.ip_control_policy_item = ip_control_policy_item

    def validate(self):
        if self.ip_control_policy_item:
            for v1 in self.ip_control_policy_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IpControlPolicyItem'] = []
        if self.ip_control_policy_item is not None:
            for k1 in self.ip_control_policy_item:
                result['IpControlPolicyItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ip_control_policy_item = []
        if m.get('IpControlPolicyItem') is not None:
            for k1 in m.get('IpControlPolicyItem'):
                temp_model = main_models.DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem()
                self.ip_control_policy_item.append(temp_model.from_map(k1))

        return self

class DescribeIpControlPolicyItemsResponseBodyIpControlPolicyItemsIpControlPolicyItem(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        cidr_ip: str = None,
        create_time: str = None,
        modified_time: str = None,
        policy_item_id: str = None,
    ):
        # The ID of the application.
        self.app_id = app_id
        # The IP addresses or CIDR blocks.
        self.cidr_ip = cidr_ip
        # The time when the policy was created. The time is displayed in UTC.
        self.create_time = create_time
        # The time when the policy was modified. The time is displayed in UTC.
        self.modified_time = modified_time
        # The ID of the policy.
        self.policy_item_id = policy_item_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.cidr_ip is not None:
            result['CidrIp'] = self.cidr_ip

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.policy_item_id is not None:
            result['PolicyItemId'] = self.policy_item_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('CidrIp') is not None:
            self.cidr_ip = m.get('CidrIp')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('PolicyItemId') is not None:
            self.policy_item_id = m.get('PolicyItemId')

        return self

