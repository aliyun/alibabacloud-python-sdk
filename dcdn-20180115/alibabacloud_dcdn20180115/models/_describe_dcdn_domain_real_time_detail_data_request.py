# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainRealTimeDetailDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        merge: str = None,
        merge_loc_isp: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time, and the maximum time range to query is 10 minutes.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of information that you want to query. Separate multiple types with commas (,). Valid values:
        # 
        # *   **qps**: queries per second (QPS)
        # *   **bps**: bandwidth
        # *   **http_code**: HTTP status code
        # 
        # This parameter is required.
        self.field = field
        # The name of the ISP. You can call the [DescribeDcdnRegionAndIsp](~~DescribeDcdnRegionAndIsp~~) operation to obtain the ISP name.
        # 
        # If you do not set this parameter, data of all ISPs is queried.
        self.isp_name_en = isp_name_en
        # The name of the region. You can call the [DescribeDcdnRegionAndIsp](~~DescribeDcdnRegionAndIsp~~) operation to obtain the region name.
        # 
        # If you do not set this parameter, all regions are queried.
        self.location_name_en = location_name_en
        # Specifies whether to return a summary value. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **false**.
        self.merge = merge
        # Specifies whether to return a summary value of **LocationNameEn** and **IspNameEn**. Valid values:
        # 
        # *   **true**
        # *   **false**
        # 
        # Default value: **false**.
        self.merge_loc_isp = merge_loc_isp
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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
        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.isp_name_en is not None:
            result['IspNameEn'] = self.isp_name_en

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

        if self.merge is not None:
            result['Merge'] = self.merge

        if self.merge_loc_isp is not None:
            result['MergeLocIsp'] = self.merge_loc_isp

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('IspNameEn') is not None:
            self.isp_name_en = m.get('IspNameEn')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('Merge') is not None:
            self.merge = m.get('Merge')

        if m.get('MergeLocIsp') is not None:
            self.merge_loc_isp = m.get('MergeLocIsp')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

