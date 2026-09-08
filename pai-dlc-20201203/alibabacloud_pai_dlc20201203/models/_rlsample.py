# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLSample(DaraModel):
    def __init__(
        self,
        latest_detail: str = None,
        latest_stage: str = None,
        latest_status: str = None,
        latest_timestamp_ms: int = None,
        prompt_uid: str = None,
        sample_index: str = None,
        terminal_state: str = None,
        trace_count: int = None,
    ):
        # The detail of the latest event.
        self.latest_detail = latest_detail
        # The stage of the latest event.
        self.latest_stage = latest_stage
        # The latest sample_status.
        self.latest_status = latest_status
        # The millisecond timestamp of the latest event.
        self.latest_timestamp_ms = latest_timestamp_ms
        # The sample UID.
        self.prompt_uid = prompt_uid
        # The trajectory ordinal number (numeric string).
        self.sample_index = sample_index
        # The desired state. Valid values: trained (training completed) and empty string (in progress). The current frame does not perform oversampling, so discarded and cancelled do not occur.
        self.terminal_state = terminal_state
        # The number of trace rows for the trajectory, including B/C type allocations.
        self.trace_count = trace_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latest_detail is not None:
            result['LatestDetail'] = self.latest_detail

        if self.latest_stage is not None:
            result['LatestStage'] = self.latest_stage

        if self.latest_status is not None:
            result['LatestStatus'] = self.latest_status

        if self.latest_timestamp_ms is not None:
            result['LatestTimestampMs'] = self.latest_timestamp_ms

        if self.prompt_uid is not None:
            result['PromptUid'] = self.prompt_uid

        if self.sample_index is not None:
            result['SampleIndex'] = self.sample_index

        if self.terminal_state is not None:
            result['TerminalState'] = self.terminal_state

        if self.trace_count is not None:
            result['TraceCount'] = self.trace_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatestDetail') is not None:
            self.latest_detail = m.get('LatestDetail')

        if m.get('LatestStage') is not None:
            self.latest_stage = m.get('LatestStage')

        if m.get('LatestStatus') is not None:
            self.latest_status = m.get('LatestStatus')

        if m.get('LatestTimestampMs') is not None:
            self.latest_timestamp_ms = m.get('LatestTimestampMs')

        if m.get('PromptUid') is not None:
            self.prompt_uid = m.get('PromptUid')

        if m.get('SampleIndex') is not None:
            self.sample_index = m.get('SampleIndex')

        if m.get('TerminalState') is not None:
            self.terminal_state = m.get('TerminalState')

        if m.get('TraceCount') is not None:
            self.trace_count = m.get('TraceCount')

        return self

