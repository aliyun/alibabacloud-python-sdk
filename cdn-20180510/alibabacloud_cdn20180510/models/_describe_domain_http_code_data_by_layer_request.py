# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainHttpCodeDataByLayerRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. You can specify up to 500 domain names in each request. Separate multiple domain names with commas (,).
        # 
        # If you do not specify this parameter, data of all accelerated domain names under your account is queried.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity of the data entries. Unit: seconds.
        # 
        # The time granularity varies with the maximum time range per query. Valid values: 300 (5 minutes), 3600 (1 hour), and 86400 (1 day). For more information, see **Usage notes**.
        self.interval = interval
        # The name of the Internet service provider (ISP). You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query ISP names.
        # 
        # If you do not specify an ISP, data of all ISPs is queried.
        self.isp_name_en = isp_name_en
        # The protocol by which you want to query HTTP status codes. The network layer supports **IPv4** and **IPv6**. The application layer supports **http**, **https**, and **quic**. You can also set the value to **all**.
        # 
        # Default value: **all**
        self.layer = layer
        # The name of the region. You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query regions.
        # 
        # If you do not specify a region, data in all regions is queried.
        self.location_name_en = location_name_en
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.layer is not None:
            result['Layer'] = self.layer

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

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

        if m.get('Layer') is not None:
            self.layer = m.get('Layer')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

