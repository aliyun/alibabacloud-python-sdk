# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDcdnFullDomainsBlockIPHistoryRequest(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        iplist: str = None,
        start_time: str = None,
    ):
        # The end of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. The end time must be later than the start time.
        # 
        # This parameter is required.
        self.end_time = end_time
        # The IP address or CIDR block to query.
        # 
        # This parameter is required.
        self.iplist = iplist
        # The beginning of the time range to query. Specify the time in the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format.
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

        if self.iplist is not None:
            result['IPList'] = self.iplist

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('IPList') is not None:
            self.iplist = m.get('IPList')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

