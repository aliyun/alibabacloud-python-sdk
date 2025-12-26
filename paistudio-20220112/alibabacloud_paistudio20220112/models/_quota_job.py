# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QuotaJob(DaraModel):
    def __init__(
        self,
        queuing: int = None,
        running: int = None,
        total: int = None,
    ):
        self.queuing = queuing
        self.running = running
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.queuing is not None:
            result['Queuing'] = self.queuing

        if self.running is not None:
            result['Running'] = self.running

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Queuing') is not None:
            self.queuing = m.get('Queuing')

        if m.get('Running') is not None:
            self.running = m.get('Running')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

