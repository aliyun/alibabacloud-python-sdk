# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class WindowLimit(DaraModel):
    def __init__(
        self,
        duration_secs: int = None,
        limit: int = None,
    ):
        # The duration of the time window in seconds.
        # 
        # This parameter is required.
        self.duration_secs = duration_secs
        # The maximum requests allowed within the time window.
        # 
        # This parameter is required.
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration_secs is not None:
            result['durationSecs'] = self.duration_secs

        if self.limit is not None:
            result['limit'] = self.limit

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('durationSecs') is not None:
            self.duration_secs = m.get('durationSecs')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        return self

