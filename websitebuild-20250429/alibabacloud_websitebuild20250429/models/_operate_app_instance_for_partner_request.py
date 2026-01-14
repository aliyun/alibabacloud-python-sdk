# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OperateAppInstanceForPartnerRequest(DaraModel):
    def __init__(
        self,
        extend: str = None,
        operate_event: str = None,
    ):
        self.extend = extend
        self.operate_event = operate_event

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend is not None:
            result['Extend'] = self.extend

        if self.operate_event is not None:
            result['OperateEvent'] = self.operate_event

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')

        if m.get('OperateEvent') is not None:
            self.operate_event = m.get('OperateEvent')

        return self

