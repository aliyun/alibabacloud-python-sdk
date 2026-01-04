# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainH2FingerprintRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        limit: int = None,
        start_time: int = None,
    ):
        # The domain name of the website.
        # 
        # >  You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query the domain names of all websites that are protected by Anti-DDoS Proxy.
        self.domain = domain
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time
        # The maximum number of entries to return.
        # 
        # This parameter is required.
        self.limit = limit
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # >  This UNIX timestamp must indicate a point in time that is accurate to the minute.
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

