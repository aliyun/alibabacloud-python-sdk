# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceNewConnectionsResponseBody(DaraModel):
    def __init__(
        self,
        instance_new_connections: main_models.DescribeInstanceNewConnectionsResponseBodyInstanceNewConnections = None,
        request_id: str = None,
    ):
        # The list of new connections in the instance.
        self.instance_new_connections = instance_new_connections
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_new_connections:
            self.instance_new_connections.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_new_connections is not None:
            result['InstanceNewConnections'] = self.instance_new_connections.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceNewConnections') is not None:
            temp_model = main_models.DescribeInstanceNewConnectionsResponseBodyInstanceNewConnections()
            self.instance_new_connections = temp_model.from_map(m.get('InstanceNewConnections'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceNewConnectionsResponseBodyInstanceNewConnections(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeInstanceNewConnectionsResponseBodyInstanceNewConnectionsMonitorItem] = None,
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
                temp_model = main_models.DescribeInstanceNewConnectionsResponseBodyInstanceNewConnectionsMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeInstanceNewConnectionsResponseBodyInstanceNewConnectionsMonitorItem(DaraModel):
    def __init__(
        self,
        item_time: str = None,
        item_value: str = None,
    ):
        # The monitoring time. The time follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
        self.item_time = item_time
        # The number of new connections in the instance.
        self.item_value = item_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.item_time is not None:
            result['ItemTime'] = self.item_time

        if self.item_value is not None:
            result['ItemValue'] = self.item_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ItemTime') is not None:
            self.item_time = m.get('ItemTime')

        if m.get('ItemValue') is not None:
            self.item_value = m.get('ItemValue')

        return self

