# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class StackInfoExtInfo(DaraModel):
    def __init__(
        self,
        info: str = None,
        type: str = None,
    ):
        self.info = info
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.info is not None:
            result['info'] = self.info

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info') is not None:
            self.info = m.get('info')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

