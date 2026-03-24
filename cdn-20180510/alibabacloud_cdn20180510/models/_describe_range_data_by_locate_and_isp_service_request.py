# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRangeDataByLocateAndIspServiceRequest(DaraModel):
    def __init__(
        self,
        domain_names: str = None,
        end_time: str = None,
        isp_names: str = None,
        location_names: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name.
        # 
        # This parameter is required.
        self.domain_names = domain_names
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is 1 hour.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The name of the ISP. You can specify only one ISP name in each call.
        # 
        # You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query ISPs.
        self.isp_names = isp_names
        # The names of the regions. Separate multiple region names with commas (,).
        # 
        # You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query the most recent region list.
        self.location_names = location_names
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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
        if self.domain_names is not None:
            result['DomainNames'] = self.domain_names

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.isp_names is not None:
            result['IspNames'] = self.isp_names

        if self.location_names is not None:
            result['LocationNames'] = self.location_names

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainNames') is not None:
            self.domain_names = m.get('DomainNames')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')

        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

