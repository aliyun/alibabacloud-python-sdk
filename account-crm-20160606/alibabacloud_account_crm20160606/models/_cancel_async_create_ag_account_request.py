# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CancelAsyncCreateAgAccountRequest(DaraModel):
    def __init__(
        self,
        mpk: str = None,
        trace_no: str = None,
    ):
        # This parameter is required.
        self.mpk = mpk
        # This parameter is required.
        self.trace_no = trace_no

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mpk is not None:
            result['Mpk'] = self.mpk

        if self.trace_no is not None:
            result['TraceNo'] = self.trace_no

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mpk') is not None:
            self.mpk = m.get('Mpk')

        if m.get('TraceNo') is not None:
            self.trace_no = m.get('TraceNo')

        return self

