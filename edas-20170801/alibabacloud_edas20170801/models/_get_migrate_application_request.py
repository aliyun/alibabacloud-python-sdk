# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetMigrateApplicationRequest(DaraModel):
    def __init__(
        self,
        migration_id: str = None,
        migration_type: int = None,
        region_id: str = None,
    ):
        # The migration ID.
        self.migration_id = migration_id
        # The operation type of the migration task. Valid values: 1: import. 2: export. 3: clone. If this parameter is not specified, all types are returned.
        self.migration_type = migration_type
        # regionId
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.migration_id is not None:
            result['migrationId'] = self.migration_id

        if self.migration_type is not None:
            result['migrationType'] = self.migration_type

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('migrationId') is not None:
            self.migration_id = m.get('migrationId')

        if m.get('migrationType') is not None:
            self.migration_type = m.get('migrationType')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self

