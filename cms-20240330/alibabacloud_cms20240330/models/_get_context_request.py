# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetContextRequest(DaraModel):
    def __init__(
        self,
        formatted: bool = None,
    ):
        self.formatted = formatted

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.formatted is not None:
            result['formatted'] = self.formatted

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('formatted') is not None:
            self.formatted = m.get('formatted')

        return self

