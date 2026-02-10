# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetImageScanNumInPeriodRequest(DaraModel):
    def __init__(
        self,
        past_day: str = None,
    ):
        # The number of days.
        # 
        # This parameter is required.
        self.past_day = past_day

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.past_day is not None:
            result['PastDay'] = self.past_day

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PastDay') is not None:
            self.past_day = m.get('PastDay')

        return self

