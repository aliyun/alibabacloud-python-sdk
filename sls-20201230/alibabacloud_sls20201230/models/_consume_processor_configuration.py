# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConsumeProcessorConfiguration(DaraModel):
    def __init__(
        self,
        spl: str = None,
    ):
        # This parameter is required.
        self.spl = spl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spl is not None:
            result['spl'] = self.spl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('spl') is not None:
            self.spl = m.get('spl')

        return self

