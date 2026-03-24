# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainTopClientIpVisitRequest(DaraModel):
    def __init__(
        self,
        domain_name: str = None,
        end_time: str = None,
        limit: str = None,
        location_name_en: str = None,
        sort_by: str = None,
        start_time: str = None,
    ):
        # The accelerated domain name. Separate multiple accelerated domain names with commas (,).
        # 
        # By default, this operation queries client IP addresses for all accelerated domain names.
        self.domain_name = domain_name
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # The end time must be later than the start time.
        self.end_time = end_time
        # The maximum number of entries to return. Maximum value: 100.
        # 
        # Default value: 20. The default value specifies that the top 20 IP addresses are returned.
        self.limit = limit
        # The name of the region. Separate multiple region names with commas (,).
        # 
        # You can call the [DescribeCdnRegionAndIsp](https://help.aliyun.com/document_detail/91077.html) operation to query regions.
        self.location_name_en = location_name_en
        # The criterion by which you want to sort client IP addresses. Valid values:
        # 
        # *   **traf**: by network traffic. This is the default value.
        # *   **acc**: by the number of requests.
        self.sort_by = sort_by
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
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

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.location_name_en is not None:
            result['LocationNameEn'] = self.location_name_en

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('LocationNameEn') is not None:
            self.location_name_en = m.get('LocationNameEn')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

