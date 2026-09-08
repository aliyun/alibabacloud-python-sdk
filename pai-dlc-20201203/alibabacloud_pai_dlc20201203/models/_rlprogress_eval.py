# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressEval(DaraModel):
    def __init__(
        self,
        done: bool = None,
        finished: int = None,
        pct: float = None,
        progress: int = None,
        ready: int = None,
        total: int = None,
    ):
        # Indicates whether Total is greater than 0 and Finished is not less than Total.
        self.done = done
        # The number of finished samples.
        self.finished = finished
        # The progress percentage, which is the ratio of Progress to Total.
        self.pct = pct
        # The progress count, which is the greater value of Ready and Finished.
        self.progress = progress
        # The number of ready samples.
        self.ready = ready
        # The target number of samples.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.done is not None:
            result['Done'] = self.done

        if self.finished is not None:
            result['Finished'] = self.finished

        if self.pct is not None:
            result['Pct'] = self.pct

        if self.progress is not None:
            result['Progress'] = self.progress

        if self.ready is not None:
            result['Ready'] = self.ready

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Done') is not None:
            self.done = m.get('Done')

        if m.get('Finished') is not None:
            self.finished = m.get('Finished')

        if m.get('Pct') is not None:
            self.pct = m.get('Pct')

        if m.get('Progress') is not None:
            self.progress = m.get('Progress')

        if m.get('Ready') is not None:
            self.ready = m.get('Ready')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

