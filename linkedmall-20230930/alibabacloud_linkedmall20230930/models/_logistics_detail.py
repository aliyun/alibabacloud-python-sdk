# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LogisticsDetail(DaraModel):
    def __init__(
        self,
        ocurr_time_str: str = None,
        standerd_desc: str = None,
    ):
        self.ocurr_time_str = ocurr_time_str
        self.standerd_desc = standerd_desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ocurr_time_str is not None:
            result['ocurrTimeStr'] = self.ocurr_time_str

        if self.standerd_desc is not None:
            result['standerdDesc'] = self.standerd_desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ocurrTimeStr') is not None:
            self.ocurr_time_str = m.get('ocurrTimeStr')

        if m.get('standerdDesc') is not None:
            self.standerd_desc = m.get('standerdDesc')

        return self

