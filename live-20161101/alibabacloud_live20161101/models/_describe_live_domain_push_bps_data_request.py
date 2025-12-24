# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainPushBpsDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        interval: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The ingest domain. You can specify multiple ingest domains and separate them with commas (,). If you do not specify this parameter, the merged data of all your ingest domains is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. The end time must be later than the start time.
        self.end_time = end_time
        # The time granularity of the query. Unit: seconds. Valid values:
        # 
        # *   **300**
        # *   **3600**
        # *   **86400**
        # 
        # The default value is 300. If you specify an invalid value or do not specify this parameter, the default value is used.
        self.interval = interval
        # The name of the Internet service provider (ISP). You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query a list of available ISPs. If you do not specify this parameter, the data of all ISPs is returned.
        self.isp_name_en = isp_name_en
        # The name of the region. You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query a list of available regions. If you do not specify this parameter, the data of all regions is returned.
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        self.region_id = region_id
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the *yyyy-MM-dd*T*HH:mm:ss*Z format. The time must be in UTC. If you do not specify this parameter, the data of the last 24 hours is returned.
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

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

