# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetHotspotCompareRequest(DaraModel):
    def __init__(
        self,
        x_debug_id: str = None,
        beg_1end: int = None,
        beg_1start: int = None,
        beg_2end: int = None,
        beg_2start: int = None,
        hot_type: str = None,
        instance_1: str = None,
        instance_2: str = None,
        pid_1: int = None,
        pid_2: int = None,
        table: str = None,
        x_sysom_invoke_source: str = None,
    ):
        self.x_debug_id = x_debug_id
        # The end time 1.
        # 
        # This parameter is required.
        self.beg_1end = beg_1end
        # The start time 1.
        # 
        # This parameter is required.
        self.beg_1start = beg_1start
        # The end time 2.
        # 
        # This parameter is required.
        self.beg_2end = beg_2end
        # The start time 2.
        # 
        # This parameter is required.
        self.beg_2start = beg_2start
        # The hot spot type.
        self.hot_type = hot_type
        # The instance 1.
        # 
        # This parameter is required.
        self.instance_1 = instance_1
        # The instance 2.
        # 
        # This parameter is required.
        self.instance_2 = instance_2
        # The process of instance 1.
        self.pid_1 = pid_1
        # The process of instance 2.
        self.pid_2 = pid_2
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

        if self.beg_1end is not None:
            result['beg1_end'] = self.beg_1end

        if self.beg_1start is not None:
            result['beg1_start'] = self.beg_1start

        if self.beg_2end is not None:
            result['beg2_end'] = self.beg_2end

        if self.beg_2start is not None:
            result['beg2_start'] = self.beg_2start

        if self.hot_type is not None:
            result['hot_type'] = self.hot_type

        if self.instance_1 is not None:
            result['instance1'] = self.instance_1

        if self.instance_2 is not None:
            result['instance2'] = self.instance_2

        if self.pid_1 is not None:
            result['pid1'] = self.pid_1

        if self.pid_2 is not None:
            result['pid2'] = self.pid_2

        if self.table is not None:
            result['table'] = self.table

        if self.x_sysom_invoke_source is not None:
            result['x-sysom-invoke-source'] = self.x_sysom_invoke_source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Debug-Id') is not None:
            self.x_debug_id = m.get('X-Debug-Id')

        if m.get('beg1_end') is not None:
            self.beg_1end = m.get('beg1_end')

        if m.get('beg1_start') is not None:
            self.beg_1start = m.get('beg1_start')

        if m.get('beg2_end') is not None:
            self.beg_2end = m.get('beg2_end')

        if m.get('beg2_start') is not None:
            self.beg_2start = m.get('beg2_start')

        if m.get('hot_type') is not None:
            self.hot_type = m.get('hot_type')

        if m.get('instance1') is not None:
            self.instance_1 = m.get('instance1')

        if m.get('instance2') is not None:
            self.instance_2 = m.get('instance2')

        if m.get('pid1') is not None:
            self.pid_1 = m.get('pid1')

        if m.get('pid2') is not None:
            self.pid_2 = m.get('pid2')

        if m.get('table') is not None:
            self.table = m.get('table')

        if m.get('x-sysom-invoke-source') is not None:
            self.x_sysom_invoke_source = m.get('x-sysom-invoke-source')

        return self

