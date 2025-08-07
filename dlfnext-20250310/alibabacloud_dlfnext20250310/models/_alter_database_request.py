# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations
from darabonba.model import DaraModel 
from typing import List, Dict


class AlterDatabaseRequest(DaraModel):
    def __init__(
        self,
        removals: List[str] = None,
        updates: Dict[str, str] = None,
    ):
        self.removals = removals
        self.updates = updates

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.removals is not None:
            result['removals'] = self.removals

        if self.updates is not None:
            result['updates'] = self.updates

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('removals') is not None:
            self.removals = m.get('removals')

        if m.get('updates') is not None:
            self.updates = m.get('updates')

        return self

