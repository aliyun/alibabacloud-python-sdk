# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLogsResponseBody(DaraModel):
    def __init__(
        self,
        affected_rows: int = None,
    ):
        # The number of updated log rows.
        self.affected_rows = affected_rows

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_rows is not None:
            result['affectedRows'] = self.affected_rows

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedRows') is not None:
            self.affected_rows = m.get('affectedRows')

        return self

