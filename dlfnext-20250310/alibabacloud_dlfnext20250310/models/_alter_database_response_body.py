# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AlterDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        missing: List[str] = None,
        removed: List[str] = None,
        updated: List[str] = None,
    ):
        self.missing = missing
        self.removed = removed
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.missing is not None:
            result['missing'] = self.missing

        if self.removed is not None:
            result['removed'] = self.removed

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('missing') is not None:
            self.missing = m.get('missing')

        if m.get('removed') is not None:
            self.removed = m.get('removed')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

