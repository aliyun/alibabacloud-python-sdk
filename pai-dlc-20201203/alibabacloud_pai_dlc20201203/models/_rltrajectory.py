# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLTrajectory(DaraModel):
    def __init__(
        self,
        latest_timestamp_ms: int = None,
        sample_index: str = None,
        terminal_state: str = None,
        trace_count: int = None,
    ):
        # The latest event millisecond UNIX timestamp.
        self.latest_timestamp_ms = latest_timestamp_ms
        # The trajectory ordinal number.
        self.sample_index = sample_index
        # The desired state. Valid values:
        # - trained: Training is complete.
        # - Empty string: In progress.
        # 
        # The current frame does not perform oversampling, so discarded and cancelled do not occur.
        self.terminal_state = terminal_state
        # The number of trace rows.
        self.trace_count = trace_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_timestamp_ms is not None:
            result['LatestTimestampMs'] = self.latest_timestamp_ms

        if self.sample_index is not None:
            result['SampleIndex'] = self.sample_index

        if self.terminal_state is not None:
            result['TerminalState'] = self.terminal_state

        if self.trace_count is not None:
            result['TraceCount'] = self.trace_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestTimestampMs') is not None:
            self.latest_timestamp_ms = m.get('LatestTimestampMs')

        if m.get('SampleIndex') is not None:
            self.sample_index = m.get('SampleIndex')

        if m.get('TerminalState') is not None:
            self.terminal_state = m.get('TerminalState')

        if m.get('TraceCount') is not None:
            self.trace_count = m.get('TraceCount')

        return self

