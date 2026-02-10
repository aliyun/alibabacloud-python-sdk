# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScreenScoreThreadRequest(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        source: int = None,
        start_time: int = None,
    ):
        # The end of the time range to query. This value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # Source of security score, default is Cloud Security Center if left empty. Enum values: 
        # - 0:Cloud Security Center. 
        # - 1:Yaochi Console.
        self.source = source
        # The beginning of the time range to query. This value is a UNIX timestamp. Unit: milliseconds.
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

        if self.source is not None:
            result['Source'] = self.source

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

