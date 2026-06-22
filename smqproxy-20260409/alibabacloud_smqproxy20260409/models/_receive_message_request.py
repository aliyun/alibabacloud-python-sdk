# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReceiveMessageRequest(DaraModel):
    def __init__(
        self,
        waitseconds: int = None,
    ):
        self.waitseconds = waitseconds

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.waitseconds is not None:
            result['waitseconds'] = self.waitseconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('waitseconds') is not None:
            self.waitseconds = m.get('waitseconds')

        return self

