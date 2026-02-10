# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeScanTaskStatisticsRequest(DaraModel):
    def __init__(
        self,
        levels: str = None,
    ):
        # The severities of the alert events handled by the virus detection task. Separate multiple severities with commas (,). The severities decrease in descending order. Valid values:
        # 
        # *   **serious**
        # *   **suspicious**
        # *   **remind**
        self.levels = levels

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.levels is not None:
            result['Levels'] = self.levels

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Levels') is not None:
            self.levels = m.get('Levels')

        return self

