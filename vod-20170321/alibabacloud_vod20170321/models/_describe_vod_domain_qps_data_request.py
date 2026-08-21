# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodDomainQpsDataRequest(DaraModel):
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
        # The accelerated domain names. Separate multiple domain names with commas (,). You can specify up to 500 domain names in a single request.
        # 
        # By default, all accelerated domain names are queried.
        self.domain_name = domain_name
        # The end time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
        self.end_time = end_time
        # The time granularity of the queried data. Unit: seconds. Valid values: **300**, **3600**, and **86400**.
        self.interval = interval
        # The name of the Internet service provider (ISP). Default value: all ISPs.
        self.isp_name_en = isp_name_en
        # The name of the region. If you do not specify this parameter, all regions are queried.
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        # The start time. Specify the time in the <i>yyyy-MM-dd</i>T<i>HH:mm:ss</i>Z format (UTC).
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

