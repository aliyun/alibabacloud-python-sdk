# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeVodDomainRealTimeDetailDataRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        isp_name_en: str = None,
        location_name_en: str = None,
        merge: str = None,
        merge_loc_isp: str = None,
        owner_id: int = None,
        start_time: str = None,
    ):
        # The accelerated domain name. You can specify a maximum of 20 accelerated domain names in each call. Separate domain names with commas (,).
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2019-11-30T05:40:00Z.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of data that you want to query. You can specify multiple data types and separate them with commas (,). Valid values:
        # 
        # qps: the number of queries per second bps: bandwidth data http_code: HTTP status codes
        # 
        # This parameter is required.
        self.field = field
        # The name of the Internet service provider (ISP).
        self.isp_name_en = isp_name_en
        # The name of the region. If you do not specify a region, data in all regions is queried.
        self.location_name_en = location_name_en
        # Specifies whether to return a summary value. Valid values:
        # 
        # true false (default)
        self.merge = merge
        # Specifies whether to return a summary value. Valid values:
        # 
        # *   **true**: groups the results by domain name and merges the results by region and ISP.
        # *   **false**: groups the results by domain name.
        # 
        # Default value: **false**.
        self.merge_loc_isp = merge_loc_isp
        self.owner_id = owner_id
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC. Example: 2019-11-30T05:33:00Z.
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

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

