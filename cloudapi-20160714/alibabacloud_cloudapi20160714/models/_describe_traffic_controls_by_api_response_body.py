# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeTrafficControlsByApiResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_control_items: main_models.DescribeTrafficControlsByApiResponseBodyTrafficControlItems = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned throttling policy information. It is an array consisting of TrafficControlItem data.
        self.traffic_control_items = traffic_control_items

    def validate(self):
        if self.traffic_control_items:
            self.traffic_control_items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_control_items is not None:
            result['TrafficControlItems'] = self.traffic_control_items.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficControlItems') is not None:
            temp_model = main_models.DescribeTrafficControlsByApiResponseBodyTrafficControlItems()
            self.traffic_control_items = temp_model.from_map(m.get('TrafficControlItems'))

        return self

class DescribeTrafficControlsByApiResponseBodyTrafficControlItems(DaraModel):
    def __init__(
        self,
        traffic_control_item: List[main_models.DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem] = None,
    ):
        self.traffic_control_item = traffic_control_item

    def validate(self):
        if self.traffic_control_item:
            for v1 in self.traffic_control_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['TrafficControlItem'] = []
        if self.traffic_control_item is not None:
            for k1 in self.traffic_control_item:
                result['TrafficControlItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.traffic_control_item = []
        if m.get('TrafficControlItem') is not None:
            for k1 in m.get('TrafficControlItem'):
                temp_model = main_models.DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem()
                self.traffic_control_item.append(temp_model.from_map(k1))

        return self

class DescribeTrafficControlsByApiResponseBodyTrafficControlItemsTrafficControlItem(DaraModel):
    def __init__(
        self,
        bound_time: str = None,
        traffic_control_item_id: str = None,
        traffic_control_item_name: str = None,
    ):
        # The binding time of the policy.
        self.bound_time = bound_time
        # The ID of the throttling policy.
        self.traffic_control_item_id = traffic_control_item_id
        # The name of the throttling policy.
        self.traffic_control_item_name = traffic_control_item_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bound_time is not None:
            result['BoundTime'] = self.bound_time

        if self.traffic_control_item_id is not None:
            result['TrafficControlItemId'] = self.traffic_control_item_id

        if self.traffic_control_item_name is not None:
            result['TrafficControlItemName'] = self.traffic_control_item_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BoundTime') is not None:
            self.bound_time = m.get('BoundTime')

        if m.get('TrafficControlItemId') is not None:
            self.traffic_control_item_id = m.get('TrafficControlItemId')

        if m.get('TrafficControlItemName') is not None:
            self.traffic_control_item_name = m.get('TrafficControlItemName')

        return self

