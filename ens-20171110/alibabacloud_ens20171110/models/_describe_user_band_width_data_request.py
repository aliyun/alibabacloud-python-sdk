# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserBandWidthDataRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        isp: str = None,
        period: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query.
        # 
        # *   Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # *   If the value of the seconds place is not 00, the start time is automatically set to the next minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ID of the node. You can specify only one node ID. By default, all nodes are queried.
        self.ens_region_id = ens_region_id
        # The ID of the instance for which you want to query the data. You can specify only one instance ID. By default, all instances are queried.
        self.instance_id = instance_id
        # The Internet service provider (ISP). Valid values:
        # 
        # *   cmcc: China Mobile
        # *   telecom: China Telecom
        # *   unicom: China Unicom
        # *   multiCarrier: multi-line ISP
        self.isp = isp
        # The precision of the monitoring data that you want to obtain. Valid values: 300, 1200, 3600, and 14400. Default value: 300. Unit: seconds.
        # 
        # This parameter is required.
        self.period = period
        # The beginning of the time range to query.
        # 
        # *   Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # *   If the value of the seconds place is not 00, the start time is automatically set to the next minute.
        # 
        # This parameter is required.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

