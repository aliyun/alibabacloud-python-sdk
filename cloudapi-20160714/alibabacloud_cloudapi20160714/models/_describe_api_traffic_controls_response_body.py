# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeApiTrafficControlsResponseBody(DaraModel):
    def __init__(
        self,
        api_traffic_controls: main_models.DescribeApiTrafficControlsResponseBodyApiTrafficControls = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The returned throttling policy information. It is an array consisting of ApiTrafficControlItem data.
        self.api_traffic_controls = api_traffic_controls
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
        self.total_count = total_count

    def validate(self):
        if self.api_traffic_controls:
            self.api_traffic_controls.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_traffic_controls is not None:
            result['ApiTrafficControls'] = self.api_traffic_controls.to_map()

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
        if m.get('ApiTrafficControls') is not None:
            temp_model = main_models.DescribeApiTrafficControlsResponseBodyApiTrafficControls()
            self.api_traffic_controls = temp_model.from_map(m.get('ApiTrafficControls'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApiTrafficControlsResponseBodyApiTrafficControls(DaraModel):
    def __init__(
        self,
        api_traffic_control_item: List[main_models.DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem] = None,
    ):
        self.api_traffic_control_item = api_traffic_control_item

    def validate(self):
        if self.api_traffic_control_item:
            for v1 in self.api_traffic_control_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ApiTrafficControlItem'] = []
        if self.api_traffic_control_item is not None:
            for k1 in self.api_traffic_control_item:
                result['ApiTrafficControlItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.api_traffic_control_item = []
        if m.get('ApiTrafficControlItem') is not None:
            for k1 in m.get('ApiTrafficControlItem'):
                temp_model = main_models.DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem()
                self.api_traffic_control_item.append(temp_model.from_map(k1))

        return self

class DescribeApiTrafficControlsResponseBodyApiTrafficControlsApiTrafficControlItem(DaraModel):
    def __init__(
        self,
        api_id: str = None,
        api_name: str = None,
        bound_time: str = None,
        traffic_control_id: str = None,
        traffic_control_name: str = None,
    ):
        # The ID of the API.
        self.api_id = api_id
        # API operation
        self.api_name = api_name
        # The binding time of the throttling policy.
        self.bound_time = bound_time
        # The ID of the throttling policy.
        self.traffic_control_id = traffic_control_id
        # The name of the throttling policy.
        self.traffic_control_name = traffic_control_name

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

        if self.traffic_control_id is not None:
            result['TrafficControlId'] = self.traffic_control_id

        if self.traffic_control_name is not None:
            result['TrafficControlName'] = self.traffic_control_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiId') is not None:
            self.api_id = m.get('ApiId')

        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('TrafficControlId') is not None:
            self.traffic_control_id = m.get('TrafficControlId')

        if m.get('TrafficControlName') is not None:
            self.traffic_control_name = m.get('TrafficControlName')

        return self

