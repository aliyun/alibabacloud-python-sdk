# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableTokenRequest(DaraModel):
    def __init__(
        self,
        is_internal: bool = None,
    ):
        self.is_internal = is_internal

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_internal is not None:
            result['isInternal'] = self.is_internal

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isInternal') is not None:
            self.is_internal = m.get('isInternal')

        return self

