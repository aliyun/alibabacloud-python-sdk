# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchQueryCreateAccountTraceRequest(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        trace_no_list: str = None,
    ):
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.trace_no_list = trace_no_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.trace_no_list is not None:
            result['TraceNoList'] = self.trace_no_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('TraceNoList') is not None:
            self.trace_no_list = m.get('TraceNoList')

        return self

