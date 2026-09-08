# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RLProgressStep(DaraModel):
    def __init__(
        self,
        current: int = None,
        eta_sec: int = None,
        pace_sec: float = None,
        pct: float = None,
        time: int = None,
        total: int = None,
    ):
        # The current step.
        self.current = current
        # The estimated remaining seconds, calculated as (Total - Current) × PaceSec.
        self.eta_sec = eta_sec
        # The per-step duration, calculated as the differential between contiguous step marks, in seconds.
        self.pace_sec = pace_sec
        # The progress percentage, which is the ratio of Current to Total.
        self.pct = pct
        # The latest step mark time, in UNIX seconds.
        self.time = time
        # The total number of steps, obtained from the configuration dump.
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.eta_sec is not None:
            result['EtaSec'] = self.eta_sec

        if self.pace_sec is not None:
            result['PaceSec'] = self.pace_sec

        if self.pct is not None:
            result['Pct'] = self.pct

        if self.time is not None:
            result['Time'] = self.time

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('EtaSec') is not None:
            self.eta_sec = m.get('EtaSec')

        if m.get('PaceSec') is not None:
            self.pace_sec = m.get('PaceSec')

        if m.get('Pct') is not None:
            self.pct = m.get('Pct')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

