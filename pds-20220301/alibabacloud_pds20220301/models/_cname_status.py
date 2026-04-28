# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CNameStatus(DaraModel):
    def __init__(
        self,
        bingding_state: str = None,
        legal_state: str = None,
        remark: str = None,
    ):
        self.bingding_state = bingding_state
        self.legal_state = legal_state
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bingding_state is not None:
            result['bingding_state'] = self.bingding_state

        if self.legal_state is not None:
            result['legal_state'] = self.legal_state

        if self.remark is not None:
            result['remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bingding_state') is not None:
            self.bingding_state = m.get('bingding_state')

        if m.get('legal_state') is not None:
            self.legal_state = m.get('legal_state')

        if m.get('remark') is not None:
            self.remark = m.get('remark')

        return self

