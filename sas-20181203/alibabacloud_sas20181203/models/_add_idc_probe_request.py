# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddIdcProbeRequest(DaraModel):
    def __init__(
        self,
        idc_name: str = None,
        idc_region: str = None,
        interval_period: int = None,
        ip_segments: str = None,
        linux_port: str = None,
        period_unit: str = None,
        uuids: str = None,
        win_port: str = None,
    ):
        # The name of the data center.
        # 
        # This parameter is required.
        self.idc_name = idc_name
        # The region ID.
        # 
        # This parameter is required.
        self.idc_region = idc_region
        # The scan interval.
        # 
        # This parameter is required.
        self.interval_period = interval_period
        # The settings of the CIDR block.
        # 
        # This parameter is required.
        self.ip_segments = ip_segments
        # The Linux port.
        # 
        # This parameter is required.
        self.linux_port = linux_port
        # The unit of the scan interval. Valid values:
        # 
        # *   **day**
        # *   **hour**
        # 
        # This parameter is required.
        self.period_unit = period_unit
        # The UUID of the server. Separate multiple UUIDs with commas (,).
        # 
        # >  You can call the [DescribeCloudCenterInstances](~~DescribeCloudCenterInstances~~) operation to query the UUID.
        # 
        # This parameter is required.
        self.uuids = uuids
        # The Windows port.
        # 
        # This parameter is required.
        self.win_port = win_port

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.idc_name is not None:
            result['IdcName'] = self.idc_name

        if self.idc_region is not None:
            result['IdcRegion'] = self.idc_region

        if self.interval_period is not None:
            result['IntervalPeriod'] = self.interval_period

        if self.ip_segments is not None:
            result['IpSegments'] = self.ip_segments

        if self.linux_port is not None:
            result['LinuxPort'] = self.linux_port

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.uuids is not None:
            result['Uuids'] = self.uuids

        if self.win_port is not None:
            result['WinPort'] = self.win_port

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IdcName') is not None:
            self.idc_name = m.get('IdcName')

        if m.get('IdcRegion') is not None:
            self.idc_region = m.get('IdcRegion')

        if m.get('IntervalPeriod') is not None:
            self.interval_period = m.get('IntervalPeriod')

        if m.get('IpSegments') is not None:
            self.ip_segments = m.get('IpSegments')

        if m.get('LinuxPort') is not None:
            self.linux_port = m.get('LinuxPort')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('Uuids') is not None:
            self.uuids = m.get('Uuids')

        if m.get('WinPort') is not None:
            self.win_port = m.get('WinPort')

        return self

