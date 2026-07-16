# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Histogram(DaraModel):
    def __init__(
        self,
        count: int = None,
        from_: int = None,
        progress: str = None,
        to: int = None,
    ):
        # The number of logs that are generated during the subinterval.
        self.count = count
        # The start time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.from_ = from_
        # Indicates whether the query result in the subinterval is complete. Valid values:
        # 
        # *   Complete: The query is successful, and the complete result is returned.
        # *   Incomplete: The query is successful, but the query result is incomplete. To obtain the complete result, you must repeat the request.
        self.progress = progress
        # The end time of the subinterval. The value is a UNIX timestamp representing the number of seconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['count'] = self.count

        if self.from_ is not None:
            result['from'] = self.from_

        if self.progress is not None:
            result['progress'] = self.progress

        if self.to is not None:
            result['to'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')

        if m.get('from') is not None:
            self.from_ = m.get('from')

        if m.get('progress') is not None:
            self.progress = m.get('progress')

        if m.get('to') is not None:
            self.to = m.get('to')

        return self

