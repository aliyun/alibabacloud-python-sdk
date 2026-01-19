# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiIpControlsResponseBody(DaraModel):
    def __init__(
        self,
        api_ip_controls: main_models.DescribeApiIpControlsResponseBodyApiIpControls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The information about the ACLs. The information is an array of ApiIpControlItem data.
        self.api_ip_controls = api_ip_controls
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_ip_controls:
            self.api_ip_controls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_ip_controls is not None:
            result['ApiIpControls'] = self.api_ip_controls.to_map()

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
        if m.get('ApiIpControls') is not None:
            temp_model = main_models.DescribeApiIpControlsResponseBodyApiIpControls()
            self.api_ip_controls = temp_model.from_map(m.get('ApiIpControls'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApiIpControlsResponseBodyApiIpControls(DaraModel):
    def __init__(
        self,
        api_ip_control_item: List[main_models.DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem] = None,
    ):
        self.api_ip_control_item = api_ip_control_item

    def validate(self):
        if self.api_ip_control_item:
            for v1 in self.api_ip_control_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiIpControlItem'] = []
        if self.api_ip_control_item is not None:
            for k1 in self.api_ip_control_item:
                result['ApiIpControlItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_ip_control_item = []
        if m.get('ApiIpControlItem') is not None:
            for k1 in m.get('ApiIpControlItem'):
                temp_model = main_models.DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem()
                self.api_ip_control_item.append(temp_model.from_map(k1))

        return self

class DescribeApiIpControlsResponseBodyApiIpControlsApiIpControlItem(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        ip_control_id: str = None,
        ip_control_name: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # The name of the API.
        self.api_name = api_name
        # The time of binding.
        self.bound_time = bound_time
        # The ID of the ACL.
        self.ip_control_id = ip_control_id
        # The name of the ACL.
        self.ip_control_name = ip_control_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_id is not None:
            result['ApiId'] = self.api_id

        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time

        if self.ip_control_id is not None:
            result['IpControlId'] = self.ip_control_id

        if self.ip_control_name is not None:
            result['IpControlName'] = self.ip_control_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('IpControlId') is not None:
            self.ip_control_id = m.get('IpControlId')

        if m.get('IpControlName') is not None:
            self.ip_control_name = m.get('IpControlName')

        return self

