# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListQueryProcessorsRequest(DaraModel):
    def __init__(
        self,
        is_active: int = None,
    ):
        # The scope of query analysis rules to be queried. Default value: 0. Valid values:
        # 
        # *   0: queries all query analysis rules.
        # *   1: queries the default query analysis rules.
        # *   2: queries the query analysis rules that are not the default rules.
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_active is not None:
            result['isActive'] = self.is_active

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        return self

