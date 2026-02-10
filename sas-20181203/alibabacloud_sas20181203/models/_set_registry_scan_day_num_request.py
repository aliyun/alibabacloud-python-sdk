# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetRegistryScanDayNumRequest(DaraModel):
    def __init__(
        self,
        scan_day_num: int = None,
    ):
        # The cycle at which you want to scan your images. Unit: days.
        # 
        # This parameter is required.
        self.scan_day_num = scan_day_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scan_day_num is not None:
            result['ScanDayNum'] = self.scan_day_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScanDayNum') is not None:
            self.scan_day_num = m.get('ScanDayNum')

        return self

