# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDomainUsageDataRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        data_protocol: str = None,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        interval: str = None,
        service_type: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The billable region. Valid values:
        # 
        # *   **CN** (default): inside the Chinese mainland
        # *   **OverSeas**: outside the Chinese mainland
        # *   **AP1**: Asia Pacific 1
        # *   **AP2**: Asia Pacific 2
        # *   **AP3**: Asia Pacific 3
        # *   **NA**: North America
        # *   **SA**: South America
        # *   **EU**: Europe
        # *   **MEAA**: Middle East and Africa
        # *   **all**: all the preceding billable regions
        self.area = area
        # The protocol of the data that you want to query. Valid values:
        # 
        # *   **http:** HTTP
        # *   **https:** HTTPS
        # *   **quic**: QUIC
        # *   **all** (default): HTTP, HTTPS, and QUIC
        self.data_protocol = data_protocol
        # The accelerated domain name. You can specify up to 100 domain names in each request. Separate multiple domain names with commas (,).
        # 
        # > If you leave this parameter empty, the usage data of all accelerated domain names in your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > The end time must be later than the start time. The maximum time range that can be specified is 31 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of the data that you want to query. Valid values:
        # 
        # *   **bps**: bandwidth
        # *   **traf**: traffic
        # *   **acc**: requests
        # 
        # > If you set this parameter to **acc**, the **Area** parameter is not supported.
        # 
        # This parameter is required.
        self.field = field
        # The time granularity of the data entries. Unit: seconds. Valid values: **300** (5 minutes), **3600** (1 hour), and **86400** (1 day).
        # 
        # *   If **Interval** is set to **300**, you can query usage data in the last 6 months. The maximum time range per query that can be specified is 3 days.
        # *   If **Interval** is set to **3600** or **86400**, you can query usage data of the previous year.
        # *   If you leave the **Interval** parameter empty, the maximum time range that you can query is 1 month. If you specify a time range of 1 to 3 days, the time interval between the entries that are returned is 1 hour. If you specify a time range of at least 4 days, the time interval between the entries that are returned is 1 day.
        self.interval = interval
        self.service_type = service_type
        # The beginning of the time range to query.
        # 
        # Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # > Data is collected every 5 minutes.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of content that you want to query. Valid values:
        # 
        # *   **static**: static content
        # *   **dynamic**: dynamic content
        # *   **all** (default): both static and dynamic content
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.data_protocol is not None:
            result['DataProtocol'] = self.data_protocol

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.field is not None:
            result['Field'] = self.field

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DataProtocol') is not None:
            self.data_protocol = m.get('DataProtocol')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Field') is not None:
            self.field = m.get('Field')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

