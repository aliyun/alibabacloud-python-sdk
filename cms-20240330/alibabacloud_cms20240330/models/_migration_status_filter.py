# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrationStatusFilter(DaraModel):
    def __init__(
        self,
        is_migrated: bool = None,
    ):
        # Specifies whether to filter by migration rule. Valid values:
        # - true: Only migrated rules (migration_status is not 0 or NULL).
        # - false: Only native rules (migration_status = 0).
        self.is_migrated = is_migrated

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_migrated is not None:
            result['isMigrated'] = self.is_migrated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isMigrated') is not None:
            self.is_migrated = m.get('isMigrated')

        return self

