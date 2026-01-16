# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDedicatedIpWarmUpDetailRequest(DaraModel):
    def __init__(
        self,
        dedicated_ip: str = None,
        end_day_mark: int = None,
        esp: str = None,
        start_day_mark: int = None,
    ):
        self.dedicated_ip = dedicated_ip
        self.end_day_mark = end_day_mark
        self.esp = esp
        self.start_day_mark = start_day_mark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dedicated_ip is not None:
            result['DedicatedIp'] = self.dedicated_ip

        if self.end_day_mark is not None:
            result['EndDayMark'] = self.end_day_mark

        if self.esp is not None:
            result['Esp'] = self.esp

        if self.start_day_mark is not None:
            result['StartDayMark'] = self.start_day_mark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DedicatedIp') is not None:
            self.dedicated_ip = m.get('DedicatedIp')

        if m.get('EndDayMark') is not None:
            self.end_day_mark = m.get('EndDayMark')

        if m.get('Esp') is not None:
            self.esp = m.get('Esp')

        if m.get('StartDayMark') is not None:
            self.start_day_mark = m.get('StartDayMark')

        return self

