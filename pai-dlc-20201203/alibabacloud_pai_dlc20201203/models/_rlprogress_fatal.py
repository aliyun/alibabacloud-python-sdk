# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressFatal(DaraModel):
    def __init__(
        self,
        collect_ns: str = None,
        message: str = None,
        raw_message: str = None,
        subsec_ns: int = None,
        time: int = None,
    ):
        # The agent_collect_time of the anchor line, represented as a nanosecond string that exceeds the JavaScript safe integer limit.
        self.collect_ns = collect_ns
        # The error message, truncated to 500 characters.
        self.message = message
        # The raw log line, truncated to 2000 characters. It is passed as AnchorMessage when calling GetRLLogContext.
        self.raw_message = raw_message
        # The nanosecond offset within the same second, used for sorting logs within the same second.
        self.subsec_ns = subsec_ns
        # The log time in UNIX seconds.
        self.time = time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collect_ns is not None:
            result['CollectNs'] = self.collect_ns

        if self.message is not None:
            result['Message'] = self.message

        if self.raw_message is not None:
            result['RawMessage'] = self.raw_message

        if self.subsec_ns is not None:
            result['SubsecNs'] = self.subsec_ns

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectNs') is not None:
            self.collect_ns = m.get('CollectNs')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RawMessage') is not None:
            self.raw_message = m.get('RawMessage')

        if m.get('SubsecNs') is not None:
            self.subsec_ns = m.get('SubsecNs')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

