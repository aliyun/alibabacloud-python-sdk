# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEpnBandWidthDataRequest(DaraModel):
    def __init__(
        self,
        epninstance_id: str = None,
        end_time: str = None,
        ens_region_id: str = None,
        instance_id: str = None,
        isp: str = None,
        networking_model: str = None,
        period: str = None,
        start_time: str = None,
    ):
        # The instance ID of the edge-to-edge network.
        self.epninstance_id = epninstance_id
        # The end of the time range to query.
        # 
        # - The time must be in UTC and in the ISO 8601 standard format: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # - If the seconds value is not 00, the end time is automatically set to the beginning of the next minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The ENS edge zone ID.
        self.ens_region_id = ens_region_id
        # The instance ID.
        self.instance_id = instance_id
        # The Internet service provider (ISP). Valid values:
        # - cmcc: China Mobile.
        # - telecom: China Telecom.
        # - unicom: China Unicom.
        # - multiCarrier: multi-ISP.
        self.isp = isp
        # The networking mode. Valid values:
        # - **SpeedUp**: intelligent acceleration (public network).
        # - **Connection**: internal network connectivity (internal network mode).
        # - **SpeedUpAndConnection**: intelligent acceleration and internal network connectivity (internal network mode).
        self.networking_model = networking_model
        # The precision of the monitoring data. Valid values: 300 (default), 1200, 3600, and 14400. Unit: seconds.
        # 
        # This parameter is required.
        self.period = period
        # The start of the time range to query.
        # 
        # - The time must be in UTC and in the ISO 8601 standard format: yyyy-MM-ddTHH:mm:ssZ.
        # 
        # - If the seconds value is not 00, the start time is automatically set to the beginning of the next minute.
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
        if self.epninstance_id is not None:
            result['EPNInstanceId'] = self.epninstance_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ens_region_id is not None:
            result['EnsRegionId'] = self.ens_region_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.networking_model is not None:
            result['NetworkingModel'] = self.networking_model

        if self.period is not None:
            result['Period'] = self.period

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EPNInstanceId') is not None:
            self.epninstance_id = m.get('EPNInstanceId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EnsRegionId') is not None:
            self.ens_region_id = m.get('EnsRegionId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('NetworkingModel') is not None:
            self.networking_model = m.get('NetworkingModel')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

