# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class GetOssUsageDataResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        usage_list: List[main_models.GetOssUsageDataResponseBodyUsageList] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The array of usage data.
        self.usage_list = usage_list

    def validate(self):
        if self.usage_list:
            for v1 in self.usage_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['UsageList'] = []
        if self.usage_list is not None:
            for k1 in self.usage_list:
                result['UsageList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.usage_list = []
        if m.get('UsageList') is not None:
            for k1 in m.get('UsageList'):
                temp_model = main_models.GetOssUsageDataResponseBodyUsageList()
                self.usage_list.append(temp_model.from_map(k1))

        return self

class GetOssUsageDataResponseBodyUsageList(DaraModel):
    def __init__(
        self,
        lan_rx_bw: int = None,
        lan_tx_bw: int = None,
        point: int = None,
        point_ts: str = None,
        storage_usage_byte: int = None,
        wan_rx_bw: int = None,
        wan_tx_bw: int = None,
    ):
        # The inbound bandwidth over the internal network. Unit: bit/s.
        self.lan_rx_bw = lan_rx_bw
        # The outbound bandwidth over the internal network. Unit: bit/s.
        self.lan_tx_bw = lan_tx_bw
        # The number of time points within a day.
        self.point = point
        # The point in time, in UTC. Format: 2010-01-21T09:50:23Z.
        self.point_ts = point_ts
        # The storage usage. Unit: bytes.
        self.storage_usage_byte = storage_usage_byte
        # The outbound bandwidth over the Internet. Unit: bit/s.
        self.wan_rx_bw = wan_rx_bw
        # The outbound bandwidth over the Internet. Unit: bit/s.
        self.wan_tx_bw = wan_tx_bw

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lan_rx_bw is not None:
            result['LanRxBw'] = self.lan_rx_bw

        if self.lan_tx_bw is not None:
            result['LanTxBw'] = self.lan_tx_bw

        if self.point is not None:
            result['Point'] = self.point

        if self.point_ts is not None:
            result['PointTs'] = self.point_ts

        if self.storage_usage_byte is not None:
            result['StorageUsageByte'] = self.storage_usage_byte

        if self.wan_rx_bw is not None:
            result['WanRxBw'] = self.wan_rx_bw

        if self.wan_tx_bw is not None:
            result['WanTxBw'] = self.wan_tx_bw

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LanRxBw') is not None:
            self.lan_rx_bw = m.get('LanRxBw')

        if m.get('LanTxBw') is not None:
            self.lan_tx_bw = m.get('LanTxBw')

        if m.get('Point') is not None:
            self.point = m.get('Point')

        if m.get('PointTs') is not None:
            self.point_ts = m.get('PointTs')

        if m.get('StorageUsageByte') is not None:
            self.storage_usage_byte = m.get('StorageUsageByte')

        if m.get('WanRxBw') is not None:
            self.wan_rx_bw = m.get('WanRxBw')

        if m.get('WanTxBw') is not None:
            self.wan_tx_bw = m.get('WanTxBw')

        return self

