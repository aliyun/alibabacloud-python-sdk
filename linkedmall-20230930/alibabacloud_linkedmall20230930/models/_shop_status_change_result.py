# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ShopStatusChangeResult(DaraModel):
    def __init__(
        self,
        operate: bool = None,
    ):
        self.operate = operate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operate is not None:
            result['operate'] = self.operate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('operate') is not None:
            self.operate = m.get('operate')

        return self

