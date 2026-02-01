# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotSpotUniqListRequest(DaraModel):
    def __init__(
        self,
        beg_end: int = None,
        beg_start: int = None,
        instance: str = None,
        pid: int = None,
        table: str = None,
        uniq: str = None,
    ):
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.instance = instance
        self.pid = pid
        self.table = table
        # This parameter is required.
        self.uniq = uniq

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.beg_end is not None:
            result['beg_end'] = self.beg_end

        if self.beg_start is not None:
            result['beg_start'] = self.beg_start

        if self.instance is not None:
            result['instance'] = self.instance

        if self.pid is not None:
            result['pid'] = self.pid

        if self.table is not None:
            result['table'] = self.table

        if self.uniq is not None:
            result['uniq'] = self.uniq

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')

        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('pid') is not None:
            self.pid = m.get('pid')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('uniq') is not None:
            self.uniq = m.get('uniq')

        return self

