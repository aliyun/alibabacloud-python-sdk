# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeUserBandWidthDataResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        monitor_data: main_models.DescribeUserBandWidthDataResponseBodyMonitorData = None,
        request_id: str = None,
    ):
        # The returned service code. 0 indicates that the request was successful.
        self.code = code
        # The monitoring data.
        self.monitor_data = monitor_data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.monitor_data:
            self.monitor_data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.monitor_data is not None:
            result['MonitorData'] = self.monitor_data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('MonitorData') is not None:
            temp_model = main_models.DescribeUserBandWidthDataResponseBodyMonitorData()
            self.monitor_data = temp_model.from_map(m.get('MonitorData'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserBandWidthDataResponseBodyMonitorData(DaraModel):
    def __init__(
        self,
        band_width_monitor_data: List[main_models.DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData] = None,
        max_down_band_width: str = None,
        max_up_band_width: str = None,
    ):
        # The bandwidth data.
        self.band_width_monitor_data = band_width_monitor_data
        # The maximum outbound bandwidth within the queried time range. Unit: bit/s.
        self.max_down_band_width = max_down_band_width
        # The maximum inbound bandwidth within the queried time range. Unit: bit/s.
        self.max_up_band_width = max_up_band_width

    def validate(self):
        if self.band_width_monitor_data:
            for v1 in self.band_width_monitor_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BandWidthMonitorData'] = []
        if self.band_width_monitor_data is not None:
            for k1 in self.band_width_monitor_data:
                result['BandWidthMonitorData'].append(k1.to_map() if k1 else None)

        if self.max_down_band_width is not None:
            result['MaxDownBandWidth'] = self.max_down_band_width

        if self.max_up_band_width is not None:
            result['MaxUpBandWidth'] = self.max_up_band_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.band_width_monitor_data = []
        if m.get('BandWidthMonitorData') is not None:
            for k1 in m.get('BandWidthMonitorData'):
                temp_model = main_models.DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData()
                self.band_width_monitor_data.append(temp_model.from_map(k1))

        if m.get('MaxDownBandWidth') is not None:
            self.max_down_band_width = m.get('MaxDownBandWidth')

        if m.get('MaxUpBandWidth') is not None:
            self.max_up_band_width = m.get('MaxUpBandWidth')

        return self

class DescribeUserBandWidthDataResponseBodyMonitorDataBandWidthMonitorData(DaraModel):
    def __init__(
        self,
        down_band_width: int = None,
        internet_rx: int = None,
        internet_tx: int = None,
        time_stamp: str = None,
        up_band_width: int = None,
    ):
        # The outbound bandwidth. Unit: bit/s.
        self.down_band_width = down_band_width
        # The Internet traffic to the instance. Unit: bytes.
        self.internet_rx = internet_rx
        # The Internet traffic from the instance. Unit: bytes.
        self.internet_tx = internet_tx
        # The timestamp when the monitoring data was queried. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time is displayed in UTC.
        self.time_stamp = time_stamp
        # The inbound bandwidth. Unit: bit/s.
        self.up_band_width = up_band_width

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.down_band_width is not None:
            result['DownBandWidth'] = self.down_band_width

        if self.internet_rx is not None:
            result['InternetRX'] = self.internet_rx

        if self.internet_tx is not None:
            result['InternetTX'] = self.internet_tx

        if self.time_stamp is not None:
            result['TimeStamp'] = self.time_stamp

        if self.up_band_width is not None:
            result['UpBandWidth'] = self.up_band_width

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DownBandWidth') is not None:
            self.down_band_width = m.get('DownBandWidth')

        if m.get('InternetRX') is not None:
            self.internet_rx = m.get('InternetRX')

        if m.get('InternetTX') is not None:
            self.internet_tx = m.get('InternetTX')

        if m.get('TimeStamp') is not None:
            self.time_stamp = m.get('TimeStamp')

        if m.get('UpBandWidth') is not None:
            self.up_band_width = m.get('UpBandWidth')

        return self

