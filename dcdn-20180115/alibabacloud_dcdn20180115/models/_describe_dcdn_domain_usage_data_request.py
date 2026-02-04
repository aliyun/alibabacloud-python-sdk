# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnDomainUsageDataRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        data_protocol: str = None,
        domain_name: str = None,
        end_time: str = None,
        field: str = None,
        interval: str = None,
        start_time: str = None,
        type: str = None,
    ):
        # The billable region. Valid values:
        # 
        # *   **CN**: Chinese mainland
        # *   **OverSeas**: outside the Chinese mainland
        # *   **AP1**: Asia Pacific 1
        # *   **AP2**: Asia Pacific 2
        # *   **AP3**: Asia Pacific 3
        # *   **NA**: North America
        # *   **SA**: South America
        # *   **EU**: Europe
        # *   **MEAA**: Middle East and Africa
        # *   **all**: all the preceding billable regions
        # 
        # Default value: **CN**
        self.area = area
        # The protocol of the data to query. Valid values:
        # 
        # *   **quic**: Quick UDP Internet Connections (QUIC)
        # *   **https**: HTTPS
        # *   **http**: HTTP
        # *   **all**: all the preceding protocols
        # 
        # Default value: **all**
        self.data_protocol = data_protocol
        # The accelerated domain name. You can specify up to 100 domain names in each request. Separate multiple domain names with commas (,).
        # 
        # >  If you do not specify this parameter, the usage data of all accelerated domain names that belong to your Alibaba Cloud account is returned.
        self.domain_name = domain_name
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The end time must be later than the start time. The maximum time range that can be queried is 31 days.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of data that you want to query. Valid values:
        # 
        # *   **bps**: bandwidth
        # *   **traf**: traffic
        # *   **acc**: requests
        # 
        # >  **acc** does not support the **Area** parameter.
        # 
        # This parameter is required.
        self.field = field
        # The time interval between the data entries to return. Unit: seconds.
        # 
        # The time interval varies with the maximum time range per query. Valid values: 300 (5 minutes), 3600 (1 hour), and 86400 (1 day). For more information, see **Usage notes**.
        self.interval = interval
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The time must be in UTC.
        # 
        # >  The minimum time granularity at which the data is queried is 5 minutes.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The type of the requests. Valid values:
        # 
        # *   **static**: static requests
        # *   **dynamic**: dynamic requests
        # *   **all**: all requests
        # 
        # Default value: **all**
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

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

