# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDDosAllEventListRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        event_type: str = None,
        ip: str = None,
        page_number: int = None,
        page_size: int = None,
        start_time: int = None,
    ):
        # The end of the time range to query. DDoS attack events that occurred before **EndTime** are queried. Specify a UNIX timestamp. Unit: seconds.
        # > EndTime can specify only events within the last three months.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The type of DDoS attack event to query. Valid values:
        # 
        # - **web-cc**: web resource exhaustion attack.
        # - **cc**: connection flood attack.
        # - **defense**: volumetric attack (scrubbing event).
        # - **blackhole**: volumetric attack (blackhole filtering event).
        # 
        # You can specify multiple types. Separate them with commas (,).
        # 
        # If you do not set this parameter, attack events of all types are queried.
        self.event_type = event_type
        # The IP address of the Anti-DDoS Pro or Anti-DDoS Premium instance to query.
        self.ip = ip
        # The page number to return in a paging query.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of attack events to return on each page in a paging query.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The beginning of the time range to query. DDoS attack events that occurred after **StartTime** are queried. Specify a UNIX timestamp. Unit: seconds.
        # > StartTime can specify only events within the last three months.
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
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.event_type is not None:
            result['EventType'] = self.event_type

        if self.ip is not None:
            result['Ip'] = self.ip

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')

        if m.get('Ip') is not None:
            self.ip = m.get('Ip')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

