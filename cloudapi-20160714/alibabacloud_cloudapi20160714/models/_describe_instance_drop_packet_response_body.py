# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceDropPacketResponseBody(DaraModel):
    def __init__(
        self,
        instance_drop_packet: main_models.DescribeInstanceDropPacketResponseBodyInstanceDropPacket = None,
        request_id: str = None,
    ):
        # The list of dropped packets in the instance.
        self.instance_drop_packet = instance_drop_packet
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.instance_drop_packet:
            self.instance_drop_packet.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_drop_packet is not None:
            result['InstanceDropPacket'] = self.instance_drop_packet.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceDropPacket') is not None:
            temp_model = main_models.DescribeInstanceDropPacketResponseBodyInstanceDropPacket()
            self.instance_drop_packet = temp_model.from_map(m.get('InstanceDropPacket'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeInstanceDropPacketResponseBodyInstanceDropPacket(DaraModel):
    def __init__(
        self,
        monitor_item: List[main_models.DescribeInstanceDropPacketResponseBodyInstanceDropPacketMonitorItem] = None,
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
                temp_model = main_models.DescribeInstanceDropPacketResponseBodyInstanceDropPacketMonitorItem()
                self.monitor_item.append(temp_model.from_map(k1))

        return self

class DescribeInstanceDropPacketResponseBodyInstanceDropPacketMonitorItem(DaraModel):
    def __init__(
        self,
        item: str = None,
        item_time: str = None,
        item_value: str = None,
    ):
        # The metric. Valid values:
        # 
        # *   InstanceDropPacketRX: the number of inbound packets dropped in the instance per second.
        # *   InstanceDropPacketTX: the number of outbound packets dropped in the instance per second.
        self.item = item
        # The monitoring time. The time follows the ISO 8601 standard. Format: YYYY-MM-DDThh:mm:ssZ
        self.item_time = item_time
        # The number of dropped packets in the instance.
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

