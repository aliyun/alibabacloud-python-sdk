# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyAppVulScanCycleRequest(DaraModel):
    def __init__(
        self,
        cycle: str = None,
    ):
        # The scan cycle for application vulnerabilities.
        # 
        # *   1week
        # *   2weeks
        # *   3days
        self.cycle = cycle

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle is not None:
            result['Cycle'] = self.cycle

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cycle') is not None:
            self.cycle = m.get('Cycle')

        return self

