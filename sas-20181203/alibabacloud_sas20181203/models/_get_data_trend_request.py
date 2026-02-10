# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDataTrendRequest(DaraModel):
    def __init__(
        self,
        biz_types: str = None,
        end_timestamp: int = None,
        interval: int = None,
        start_timestamp: int = None,
    ):
        # The type of the security data that you want to query. Valid values:
        # 
        # *   **HC_NEW**: the number of new baseline risks.
        # *   **HC_OPERATE**: the number of handled baseline risks.
        # *   **VUL_NEW**: the number of new vulnerabilities.
        # *   **VUL_OPERATE**: the number of handled vulnerabilities.
        # *   **SUSP_NEW**: the number of new alerts.
        # *   **SUSP_OPERATE**: the number of handled alerts.
        # 
        # This parameter is required.
        self.biz_types = biz_types
        # The end of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.end_timestamp = end_timestamp
        # The interval of the data that you want to query. Unit: milliseconds.
        # 
        # >  The minimum value is 1000.
        # 
        # This parameter is required.
        self.interval = interval
        # The beginning of the time range to query. The value is a UNIX timestamp. Unit: milliseconds.
        # 
        # This parameter is required.
        self.start_timestamp = start_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_types is not None:
            result['BizTypes'] = self.biz_types

        if self.end_timestamp is not None:
            result['EndTimestamp'] = self.end_timestamp

        if self.interval is not None:
            result['Interval'] = self.interval

        if self.start_timestamp is not None:
            result['StartTimestamp'] = self.start_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizTypes') is not None:
            self.biz_types = m.get('BizTypes')

        if m.get('EndTimestamp') is not None:
            self.end_timestamp = m.get('EndTimestamp')

        if m.get('Interval') is not None:
            self.interval = m.get('Interval')

        if m.get('StartTimestamp') is not None:
            self.start_timestamp = m.get('StartTimestamp')

        return self

