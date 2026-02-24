# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class IndexJsonKey(DaraModel):
    def __init__(
        self,
        chn: str = None,
        type: str = None,
    ):
        self.chn = chn
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chn is not None:
            result['chn'] = self.chn

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chn') is not None:
            self.chn = m.get('chn')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

