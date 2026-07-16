# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVsDomainReqTrafficDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        # Visual Edge Computing Service domain name.
        self.domain_name = domain_name
        # End time of the query. Must be later than the start time. Specify in ISO 8601 format using UTC time.<br>Format: YYYY-MM-DDThh:mm:ssZ<br>
        self.end_time = end_time
        # Time granularity of the query. Unit: seconds. Valid values:
        # 
        # - **300** (default).
        # 
        # - **3600**.
        # 
        # - **86400**.
        # 
        # > If you omit this parameter or specify an unsupported value, the default value **300** is used.
        self.interval = interval
        # ISP name in English. Call DescribeCdnRegionAndIsp to get valid values. If you omit this parameter, the system returns data for all ISPs.
        self.isp_name_en = isp_name_en
        # Region name in English. Call DescribeCdnRegionAndIsp to get valid values. If you omit this parameter, the system returns data for all regions.
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        # Start time of the query. Specify in ISO 8601 format using UTC time.<br>Format: YYYY-MM-DDThh:mm:ssZ<br>Minimum time granularity is 5 minutes.<br>If you omit this parameter, the system returns data for the last 24 hours.<br><br><br>
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

