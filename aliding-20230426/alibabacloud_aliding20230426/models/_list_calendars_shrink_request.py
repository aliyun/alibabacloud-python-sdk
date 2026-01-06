# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCalendarsShrinkRequest(DaraModel):
    def __init__(
        self,
        request_shrink: str = None,
    ):
        self.request_shrink = request_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')

        return self

