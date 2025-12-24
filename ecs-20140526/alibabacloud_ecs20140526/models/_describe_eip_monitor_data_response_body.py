# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class DescribeEipMonitorDataResponseBody(DaraModel):
    def __init__(
        self,
        eip_monitor_datas: main_models.DescribeEipMonitorDataResponseBodyEipMonitorDatas = None,
        request_id: str = None,
    ):
        self.eip_monitor_datas = eip_monitor_datas
        self.request_id = request_id

    def validate(self):
        if self.eip_monitor_datas:
            self.eip_monitor_datas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_monitor_datas is not None:
            result['EipMonitorDatas'] = self.eip_monitor_datas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipMonitorDatas') is not None:
            temp_model = main_models.DescribeEipMonitorDataResponseBodyEipMonitorDatas()
            self.eip_monitor_datas = temp_model.from_map(m.get('EipMonitorDatas'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeEipMonitorDataResponseBodyEipMonitorDatas(DaraModel):
    def __init__(
        self,
        eip_monitor_data: List[main_models.DescribeEipMonitorDataResponseBodyEipMonitorDatasEipMonitorData] = None,
    ):
        self.eip_monitor_data = eip_monitor_data

    def validate(self):
        if self.eip_monitor_data:
            for v1 in self.eip_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EipMonitorData'] = []
        if self.eip_monitor_data is not None:
            for k1 in self.eip_monitor_data:
                result['EipMonitorData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.eip_monitor_data = []
        if m.get('EipMonitorData') is not None:
            for k1 in m.get('EipMonitorData'):
                temp_model = main_models.DescribeEipMonitorDataResponseBodyEipMonitorDatasEipMonitorData()
                self.eip_monitor_data.append(temp_model.from_map(k1))

        return self

class DescribeEipMonitorDataResponseBodyEipMonitorDatasEipMonitorData(DaraModel):
    def __init__(
        self,
        eip_bandwidth: int = None,
        eip_flow: int = None,
        eip_packets: int = None,
        eip_rx: int = None,
        eip_tx: int = None,
        time_stamp: str = None,
    ):
        self.eip_bandwidth = eip_bandwidth
        self.eip_flow = eip_flow
        self.eip_packets = eip_packets
        self.eip_rx = eip_rx
        self.eip_tx = eip_tx
        self.time_stamp = time_stamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.eip_bandwidth is not None:
            result['EipBandwidth'] = self.eip_bandwidth

        if self.eip_flow is not None:
            result['EipFlow'] = self.eip_flow

        if self.eip_packets is not None:
            result['EipPackets'] = self.eip_packets

        if self.eip_rx is not None:
            result['EipRX'] = self.eip_rx

        if self.eip_tx is not None:
            result['EipTX'] = self.eip_tx

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EipBandwidth') is not None:
            self.eip_bandwidth = m.get('EipBandwidth')

        if m.get('EipFlow') is not None:
            self.eip_flow = m.get('EipFlow')

        if m.get('EipPackets') is not None:
            self.eip_packets = m.get('EipPackets')

        if m.get('EipRX') is not None:
            self.eip_rx = m.get('EipRX')

        if m.get('EipTX') is not None:
            self.eip_tx = m.get('EipTX')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        return self

