# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainViewTopUrlRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        inerval: int = None,
        resource_group_id: str = None,
        start_time: int = None,
        top: int = None,
    ):
        # The domain name of the website service.
        # 
        # > The domain name must have a website service forwarding rule configured. You can invoke [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) to query all domain names that are added to Anti-DDoS Pro and Anti-DDoS Premium.
        self.domain = domain
        # The end of the time range to query. Specify a UNIX timestamp. Unit: seconds.
        # > The value must be on the exact minute.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The step size for returning data, in seconds. This parameter specifies the interval at which a result is returned. The supported step size varies based on the query time range (determined by **StartTime** and **EndTime**). Recommended settings:
        # 
        # - Query time range of up to 1 hour: minimum step size of 60 seconds, maximum not exceeding the query time range.
        # - Query time range of more than 1 hour but up to 6 hours: minimum step size of 600 seconds, maximum not exceeding the query time range.
        # - Query time range of more than 6 hours but up to 24 hours: minimum step size of 1800 seconds, maximum not exceeding the query time range.
        # - Query time range of more than 24 hours but up to 7 days: minimum step size of 3600 seconds, maximum not exceeding the query time range.
        # - Query time range of more than 7 days but up to 15 days: minimum step size of 14400 seconds, maximum not exceeding the query time range.
        # - Query time range of more than 15 days: minimum step size of 43200 seconds, maximum not exceeding the query time range.
        self.inerval = inerval
        # The ID of the resource group to which the Anti-DDoS Pro or Anti-DDoS Premium instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The beginning of the time range to query. Specify a UNIX timestamp. Unit: seconds.
        # > The value must be on the exact minute.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The number of URLs to return. Valid values: **1** to **100**.
        # 
        # This parameter is required.
        self.top = top

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

        if self.inerval is not None:
            result['Inerval'] = self.inerval

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.top is not None:
            result['Top'] = self.top

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Inerval') is not None:
            self.inerval = m.get('Inerval')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Top') is not None:
            self.top = m.get('Top')

        return self

