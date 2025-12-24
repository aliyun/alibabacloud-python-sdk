# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeEniMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        monitor_data: main_models.DescribeEniMonitorDataResponseBodyMonitorData = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The monitoring data of the secondary ENI.
        self.monitor_data = monitor_data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeEniMonitorDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeEniMonitorDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        eni_monitor_data: List[main_models.DescribeEniMonitorDataResponseBodyMonitorDataEniMonitorData] = None,
    ):
        self.eni_monitor_data = eni_monitor_data

    def validate(self):
        if self.eni_monitor_data:
            for v1 in self.eni_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EniMonitorData'] = []
        if self.eni_monitor_data is not None:
            for k1 in self.eni_monitor_data:
                result['EniMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eni_monitor_data = []
        if m.get('EniMonitorData') is not None:
            for k1 in m.get('EniMonitorData'):
                temp_model = main_models.DescribeEniMonitorDataResponseBodyMonitorDataEniMonitorData()
                self.eni_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeEniMonitorDataResponseBodyMonitorDataEniMonitorData(DaraModel):
    def __init__(
        self,
        drop_packet_rx: str = None,
        drop_packet_tx: str = None,
        eni_id: str = None,
        intranet_rx: str = None,
        intranet_tx: str = None,
        packet_rx: str = None,
        packet_tx: str = None,
        time_stamp: str = None,
    ):
        # The number of received packets that were dropped by the secondary ENI over the internal network.
        self.drop_packet_rx = drop_packet_rx
        # The number of sent packets that were dropped by the secondary ENI over the internal network.
        self.drop_packet_tx = drop_packet_tx
        # The ID of the secondary ENI.
        self.eni_id = eni_id
        # The average rate at which the secondary ENI received data over the internal network. Unit: Kbit/s.
        self.intranet_rx = intranet_rx
        # The average rate at which the secondary ENI sent data over the internal network. Unit: Kbit/s.
        self.intranet_tx = intranet_tx
        # The number of packets received by the secondary ENI over the internal network.
        self.packet_rx = packet_rx
        # The number of packets sent by the secondary ENI over the internal network.
        self.packet_tx = packet_tx
        # The timestamp of the monitoring data. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drop_packet_rx is not None:
            result['DropPacketRx'] = self.drop_packet_rx

        if self.drop_packet_tx is not None:
            result['DropPacketTx'] = self.drop_packet_tx

        if self.eni_id is not None:
            result['EniId'] = self.eni_id

        if self.intranet_rx is not None:
            result['IntranetRx'] = self.intranet_rx

        if self.intranet_tx is not None:
            result['IntranetTx'] = self.intranet_tx

        if self.packet_rx is not None:
            result['PacketRx'] = self.packet_rx

        if self.packet_tx is not None:
            result['PacketTx'] = self.packet_tx

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DropPacketRx') is not None:
            self.drop_packet_rx = m.get('DropPacketRx')

        if m.get('DropPacketTx') is not None:
            self.drop_packet_tx = m.get('DropPacketTx')

        if m.get('EniId') is not None:
            self.eni_id = m.get('EniId')

        if m.get('IntranetRx') is not None:
            self.intranet_rx = m.get('IntranetRx')

        if m.get('IntranetTx') is not None:
            self.intranet_tx = m.get('IntranetTx')

        if m.get('PacketRx') is not None:
            self.packet_rx = m.get('PacketRx')

        if m.get('PacketTx') is not None:
            self.packet_tx = m.get('PacketTx')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

