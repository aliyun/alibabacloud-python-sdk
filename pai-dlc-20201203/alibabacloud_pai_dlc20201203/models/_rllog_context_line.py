# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLLogContextLine(DaraModel):
    def __init__(
        self,
        message: str = None,
        timestamp_ms: int = None,
    ):
        # The log text (<= 2000 characters, with ANSI escape codes stripped).
        self.message = message
        # The millisecond timestamp of the log line.
        self.timestamp_ms = timestamp_ms

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.timestamp_ms is not None:
            result['TimestampMs'] = self.timestamp_ms

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('TimestampMs') is not None:
            self.timestamp_ms = m.get('TimestampMs')

        return self

