# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeGroupTrafficResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        traffic_per_second: main_models.DescribeGroupTrafficResponseBodyTrafficPerSecond = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The traffic information per second.
        self.traffic_per_second = traffic_per_second

    def validate(self):
        if self.traffic_per_second:
            self.traffic_per_second.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.traffic_per_second is not None:
            result['TrafficPerSecond'] = self.traffic_per_second.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TrafficPerSecond') is not None:
            temp_model = main_models.DescribeGroupTrafficResponseBodyTrafficPerSecond()
            self.traffic_per_second = temp_model.from_map(m.get('TrafficPerSecond'))

        return self

class DescribeGroupTrafficResponseBodyTrafficPerSecond(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeGroupTrafficResponseBodyTrafficPerSecondMonitorItem] = None,
    ):
        self.monitor_item = monitor_item

    def validate(self):
        if self.monitor_item:
            for v1 in self.monitor_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MonitorItem'] = []
        if self.monitor_item is not None:
            for k1 in self.monitor_item:
                result['MonitorItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.monitor_item = []
        if m.get('MonitorItem') is not None:
            for k1 in m.get('MonitorItem'):
                temp_model = main_models.DescribeGroupTrafficResponseBodyTrafficPerSecondMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeGroupTrafficResponseBodyTrafficPerSecondMonitorItem(DaraModel):
    def __init__(
        self,
        item: str = None,
        item_time: str = None,
        item_value: str = None,
    ):
        # The metric. Valid values:
        # 
        # *   inbound: traffic consumed by requests
        # *   outbound: traffic consumed by responses
        self.item = item
        # The corresponding time. The time follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ.
        self.item_time = item_time
        # The traffic volume per second.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item is not None:
            result['Item'] = self.item

        if self.item_time is not None:
            result['ItemTime'] = self.item_time

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Item') is not None:
            self.item = m.get('Item')

        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self

