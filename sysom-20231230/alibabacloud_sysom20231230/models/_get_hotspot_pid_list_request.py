# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotspotPidListRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        beg_end: int = None,
        beg_start: int = None,
        instance: str = None,
        table: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The end time.
        # 
        # This parameter is required.
        self.beg_end = beg_end
        # The start time.
        # 
        # This parameter is required.
        self.beg_start = beg_start
        # The instance ID.
        # 
        # This parameter is required.
        self.instance = instance
        # The name of the table to query.
        # 
        # This parameter is required.
        self.table = table
        self.x_sysom_invoke_source = x_sysom_invoke_source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_debug_id is not None:
            result['X-Debug-Id'] = self.x_debug_id

        if self.beg_end is not None:
            result['beg_end'] = self.beg_end

        if self.beg_start is not None:
            result['beg_start'] = self.beg_start

        if self.instance is not None:
            result['instance'] = self.instance

        if self.table is not None:
            result['table'] = self.table

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')

        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')

        if m.get('instance') is not None:
            self.instance = m.get('instance')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

