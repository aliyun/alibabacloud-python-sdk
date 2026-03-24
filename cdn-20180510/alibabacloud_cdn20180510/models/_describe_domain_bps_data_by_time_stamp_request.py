# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainBpsDataByTimeStampRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        isp_names: str = None,
        location_names: str = None,
        time_point: str = None,
    ):
        # The accelerated domain name. You can specify only one domain name in each request.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The names of the Internet service providers (ISPs). Separate multiple ISPs with commas (,).
        # 
        # You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query regions.
        # 
        # This parameter is required.
        self.isp_names = isp_names
        # The regions. Separate multiple regions with commas (,).
        # 
        # You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query regions.
        # 
        # This parameter is required.
        self.location_names = location_names
        # The point in time to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The data is collected every 5 minutes.
        # 
        # This parameter is required.
        self.time_point = time_point

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.isp_names is not None:
            result['IspNames'] = self.isp_names

        if self.location_names is not None:
            result['LocationNames'] = self.location_names

        if self.time_point is not None:
            result['TimePoint'] = self.time_point

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IspNames') is not None:
            self.isp_names = m.get('IspNames')

        if m.get('LocationNames') is not None:
            self.location_names = m.get('LocationNames')

        if m.get('TimePoint') is not None:
            self.time_point = m.get('TimePoint')

        return self

