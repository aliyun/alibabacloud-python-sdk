# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceSlbConnectResponseBody(DaraModel):
    def __init__(
        self,
        instance_slb_connect: main_models.DescribeInstanceSlbConnectResponseBodyInstanceSlbConnect = None,
        request_id: str = None,
    ):
        # The list of concurrent connections in the instance.
        self.instance_slb_connect = instance_slb_connect
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_slb_connect:
            self.instance_slb_connect.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_slb_connect is not None:
            result['InstanceSlbConnect'] = self.instance_slb_connect.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceSlbConnect') is not None:
            temp_model = main_models.DescribeInstanceSlbConnectResponseBodyInstanceSlbConnect()
            self.instance_slb_connect = temp_model.from_map(m.get('InstanceSlbConnect'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceSlbConnectResponseBodyInstanceSlbConnect(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeInstanceSlbConnectResponseBodyInstanceSlbConnectMonitorItem] = None,
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
                temp_model = main_models.DescribeInstanceSlbConnectResponseBodyInstanceSlbConnectMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeInstanceSlbConnectResponseBodyInstanceSlbConnectMonitorItem(DaraModel):
    def __init__(
        self,
        item: str = None,
        item_time: str = None,
        item_value: str = None,
    ):
        # The metric. Valid values:
        # 
        # *   InstanceMaxConnection: the maximum number of connections
        # *   InstanceInactiveConnection: the number of inactive connections
        # *   InstanceActiveConnection: the number of active connections
        self.item = item
        # The monitoring time. The time follows the ISO 8601 standard and UTC time is used. Format: YYYY-MM-DDThh:mm:ssZ
        self.item_time = item_time
        # The number of concurrent connections in the instance.
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

