# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainBpsDataByLayerRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        layer: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The streaming domain. You can specify multiple domain names separated by commas (,). If this parameter is left empty, the aggregated data of all domain names is returned by default.
        self.domain_name = domain_name
        # The end of the time range to query, in the format of <i>yyyy-MM-ddTHH:mm:ssZ</i> (UTC). The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity of the data to query. Unit: seconds. Valid values:
        # 
        # - **300**
        # 
        # - **3600**
        # 
        # - **86400**
        # > - Time range ≤ 3 days: Valid data timestamp granularity values are 300, 3600, and 86400.
        # > - 3 days < time range ≤ 31 days: Valid data timestamp granularity values are 3600 and 86400.
        # > - Time range > 31 days: The only valid value is 86400.
        # > - If this parameter is not specified or the specified value is not supported, the default value 300 is used.
        self.interval = interval
        # The name of the Internet service provider (ISP) in English. If this parameter is not specified, data for all ISPs is returned.
        # >You can call the [DescribeLiveRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query the English names of regions and ISPs.
        self.isp_name_en = isp_name_en
        # The query dimension. Valid values:
        # 
        # - Network layer (IPv4, IPv6)
        # 
        # - Application layer (http, https, quic)
        # 
        # - all (default)
        # 
        # Valid values: all | IPv4 | IPv6 | http | https | quic (case-sensitive).
        self.layer = layer
        # The name of the region in English. If this parameter is not specified, data for all regions is returned.
        # >You can call the [DescribeLiveRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query the English names of regions and ISPs.
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The beginning of the time range to query, in the format of <i>yyyy-MM-ddTHH:mm:ssZ</i> (UTC).
        # >If this parameter is not specified, data for the last 24 hours is returned by default. The minimum data granularity is 5 minutes.
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

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

