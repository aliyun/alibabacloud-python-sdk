# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SubmitCheckRequest(DaraModel):
    def __init__(
        self,
        scan_range: str = None,
        task_source: str = None,
    ):
        # The check items that are scanned. Valid values:
        # 
        # *   **FULL**: All check items are scanned.
        # *   **FULL**: Only the check items that are configured are scanned.
        self.scan_range = scan_range
        # The source of task.
        self.task_source = task_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scan_range is not None:
            result['ScanRange'] = self.scan_range

        if self.task_source is not None:
            result['TaskSource'] = self.task_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScanRange') is not None:
            self.scan_range = m.get('ScanRange')

        if m.get('TaskSource') is not None:
            self.task_source = m.get('TaskSource')

        return self

