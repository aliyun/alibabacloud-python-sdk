# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModelProperties(DaraModel):
    def __init__(
        self,
        context_size: int = None,
    ):
        self.context_size = context_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.context_size is not None:
            result['contextSize'] = self.context_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('contextSize') is not None:
            self.context_size = m.get('contextSize')

        return self

