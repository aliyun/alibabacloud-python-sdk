# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class IncidentPlanFieldPath(DaraModel):
    def __init__(
        self,
        field_alias: str = None,
        field_path: List[str] = None,
    ):
        self.field_alias = field_alias
        self.field_path = field_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_alias is not None:
            result['fieldAlias'] = self.field_alias

        if self.field_path is not None:
            result['fieldPath'] = self.field_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldAlias') is not None:
            self.field_alias = m.get('fieldAlias')

        if m.get('fieldPath') is not None:
            self.field_path = m.get('fieldPath')

        return self

