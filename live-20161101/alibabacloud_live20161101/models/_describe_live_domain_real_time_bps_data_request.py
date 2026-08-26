# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLiveDomainRealTimeBpsDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        owner_id: int = None,
        region_id: str = None,
        start_time: str = None,
    ):
        # The streaming domain.
        # 
        # Separate multiple domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end time. It must be later than the start time. The format is *yyyy-MM-dd*T*HH:mm:ss*Z (UTC).
        # 
        # > If you do not specify this parameter, data within one hour of the start time is queried by default.
        self.end_time = end_time
        # The English name of the carrier.
        # 
        # For more information, see [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html).
        self.isp_name_en = isp_name_en
        # The English name of the region.
        # 
        # For more information, see [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html).
        self.location_name_en = location_name_en
        self.owner_id = owner_id
        # The region ID.
        self.region_id = region_id
        # The start time. The format is *yyyy-MM-dd*T*HH:mm:ss*Z (UTC).
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

