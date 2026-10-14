# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainTopRefererRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        limit: int = None,
        query_type: str = None,
        region: str = None,
        start_time: int = None,
    ):
        # The domain name of the website service.
        # > The domain name must have a website traffic forwarding rule configured. You can call [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names.
        self.domain = domain
        # The end time of the query. This value is a UNIX timestamp. Unit: seconds.
        # > The value must be on the hour or half hour.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The number of data entries to return.
        # 
        # This parameter is required.
        self.limit = limit
        self.query_type = query_type
        # The region of the service. Valid values:
        # - **cn**: the Chinese mainland.
        # - **cn-hongkong**: outside the Chinese mainland.
        # 
        # This parameter is required.
        self.region = region
        # The start time of the query. This value is a UNIX timestamp. Unit: seconds.
        # > The value must be on the hour or half hour.
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
        if self.domain is not None:
            result['Domain'] = self.domain

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.region is not None:
            result['Region'] = self.region

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

