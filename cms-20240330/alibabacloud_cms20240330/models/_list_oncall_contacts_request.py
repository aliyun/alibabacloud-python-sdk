# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListOncallContactsRequest(DaraModel):
    def __init__(
        self,
        timestamp: str = None,
    ):
        # The timestamp of the on-call shift to query. Unit: milliseconds.
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')

        return self

