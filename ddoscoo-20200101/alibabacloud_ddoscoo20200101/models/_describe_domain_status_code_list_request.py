# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainStatusCodeListRequest(DaraModel):
    def __init__(
        self,
        domain: str = None,
        end_time: int = None,
        interval: int = None,
        query_type: str = None,
        resource_group_id: str = None,
        start_time: int = None,
    ):
        # The domain name of the website. If you do not specify this parameter, the statistics on response status codes of all domain names are queried.
        # 
        # > A forwarding rule must be configured for the domain name. You can call the [DescribeDomains](https://help.aliyun.com/document_detail/91724.html) operation to query all domain names.
        self.domain = domain
        # The end of the time range to query. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
        self.end_time = end_time
        # The interval for returning data. Unit: seconds.
        # 
        # This parameter is required.
        self.interval = interval
        # The source of the statistics. Valid values:
        # 
        # *   **gf**: Anti-DDoS Pro or Anti-DDoS Premium
        # *   **upstrem**: origin server
        # 
        # This parameter is required.
        self.query_type = query_type
        # The ID of the resource group to which the instance belongs in Resource Management. This parameter is empty by default, which indicates that the instance belongs to the default resource group.
        self.resource_group_id = resource_group_id
        # The start time of the event. The value is a UNIX timestamp. Unit: seconds.
        # 
        # > This UNIX timestamp must indicate a point in time that is accurate to the minute.
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

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.query_type is not None:
            result['QueryType'] = self.query_type

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('QueryType') is not None:
            self.query_type = m.get('QueryType')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

