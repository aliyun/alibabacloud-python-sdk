# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAsrConfigRequest(DaraModel):
    def __init__(
        self,
        config_level: int = None,
        entry_id: str = None,
    ):
        # The configuration level. Valid values: `0` (system), `1` (tenant), and `2` (instance).
        self.config_level = config_level
        # The ID of the entry at the level specified by `ConfigLevel`.
        self.entry_id = entry_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_level is not None:
            result['ConfigLevel'] = self.config_level

        if self.entry_id is not None:
            result['EntryId'] = self.entry_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigLevel') is not None:
            self.config_level = m.get('ConfigLevel')

        if m.get('EntryId') is not None:
            self.entry_id = m.get('EntryId')

        return self

