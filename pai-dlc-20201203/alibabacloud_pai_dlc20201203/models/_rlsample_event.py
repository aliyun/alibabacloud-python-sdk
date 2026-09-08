# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLSampleEvent(DaraModel):
    def __init__(
        self,
        detail: str = None,
        from_: str = None,
        global_step: str = None,
        stage: str = None,
        timestamp_ms: int = None,
        to: str = None,
    ):
        # The details. For Megatron rows, the value is rank=..,global_step=..,ppo_epoch=..
        self.detail = detail
        # The event source component. For Megatron rows, the value is "{phase} {status}".
        self.from_ = from_
        # The training step to which the event belongs (raw string). For Megatron rows, this is empty because the step is included in Detail.
        self.global_step = global_step
        # The stage. For Megatron rows, this is normalized to TRAIN.
        self.stage = stage
        # The millisecond timestamp.
        self.timestamp_ms = timestamp_ms
        # The event target component. For Megatron rows, the value is the function name.
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.detail is not None:
            result['Detail'] = self.detail

        if self.from_ is not None:
            result['From'] = self.from_

        if self.global_step is not None:
            result['GlobalStep'] = self.global_step

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.timestamp_ms is not None:
            result['TimestampMs'] = self.timestamp_ms

        if self.to is not None:
            result['To'] = self.to

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('GlobalStep') is not None:
            self.global_step = m.get('GlobalStep')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('TimestampMs') is not None:
            self.timestamp_ms = m.get('TimestampMs')

        if m.get('To') is not None:
            self.to = m.get('To')

        return self

