# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceResourceTablesRequest(DaraModel):
    def __init__(
        self,
        maxcompute_schema: str = None,
    ):
        self.maxcompute_schema = maxcompute_schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.maxcompute_schema is not None:
            result['MaxcomputeSchema'] = self.maxcompute_schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxcomputeSchema') is not None:
            self.maxcompute_schema = m.get('MaxcomputeSchema')

        return self

