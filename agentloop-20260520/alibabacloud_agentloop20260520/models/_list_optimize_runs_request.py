# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOptimizeRunsRequest(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        status: str = None,
        window_start_time_begin: int = None,
        window_start_time_end: int = None,
    ):
        # The maximum number of entries to return. Default value: 20. Maximum value: 100.
        self.max_results = max_results
        # The pagination token.
        self.next_token = next_token
        # The status used to filter results.
        self.status = status
        # The lower bound of the window start time in UNIX seconds.
        self.window_start_time_begin = window_start_time_begin
        # The upper bound of the window start time in UNIX seconds.
        self.window_start_time_end = window_start_time_end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.status is not None:
            result['status'] = self.status

        if self.window_start_time_begin is not None:
            result['windowStartTimeBegin'] = self.window_start_time_begin

        if self.window_start_time_end is not None:
            result['windowStartTimeEnd'] = self.window_start_time_end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('windowStartTimeBegin') is not None:
            self.window_start_time_begin = m.get('windowStartTimeBegin')

        if m.get('windowStartTimeEnd') is not None:
            self.window_start_time_end = m.get('windowStartTimeEnd')

        return self

