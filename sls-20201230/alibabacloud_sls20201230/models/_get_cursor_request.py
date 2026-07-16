# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetCursorRequest(DaraModel):
    def __init__(
        self,
        from_: str = None,
    ):
        # A point in time. This can be a UNIX timestamp or the string `begin` or `end`.
        # 
        # This parameter is required.
        self.from_ = from_

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['from'] = self.from_

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')

        return self

