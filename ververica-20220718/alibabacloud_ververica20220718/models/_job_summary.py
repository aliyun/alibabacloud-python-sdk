# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class JobSummary(DaraModel):
    def __init__(
        self,
        cancelled: int = None,
        cancelling: int = None,
        failed: int = None,
        finished: int = None,
        running: int = None,
        starting: int = None,
    ):
        # The number of jobs that are in the cancelled state.
        self.cancelled = cancelled
        # The number of jobs that are in the cancelling state.
        self.cancelling = cancelling
        # The number of jobs that are in the failed state.
        self.failed = failed
        # The number of jobs that are in the finished state.
        self.finished = finished
        # The number of jobs that are in the running state.
        self.running = running
        # The number of jobs that are in the starting state.
        self.starting = starting

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cancelled is not None:
            result['cancelled'] = self.cancelled

        if self.cancelling is not None:
            result['cancelling'] = self.cancelling

        if self.failed is not None:
            result['failed'] = self.failed

        if self.finished is not None:
            result['finished'] = self.finished

        if self.running is not None:
            result['running'] = self.running

        if self.starting is not None:
            result['starting'] = self.starting

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cancelled') is not None:
            self.cancelled = m.get('cancelled')

        if m.get('cancelling') is not None:
            self.cancelling = m.get('cancelling')

        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('finished') is not None:
            self.finished = m.get('finished')

        if m.get('running') is not None:
            self.running = m.get('running')

        if m.get('starting') is not None:
            self.starting = m.get('starting')

        return self

