# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteInstanceInspectionResponseBody(DaraModel):
    def __init__(
        self,
        ok: bool = None,
    ):
        self.ok = ok

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ok is not None:
            result['ok'] = self.ok

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ok') is not None:
            self.ok = m.get('ok')

        return self

