# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGdnInstanceRequest(DaraModel):
    def __init__(
        self,
        dbinstance_name: str = None,
        description: str = None,
        gdn_mode: str = None,
        region_id: str = None,
        rpl_conflict_strategy: str = None,
        rpl_dml_strategy: str = None,
        rpl_sync_ddl: bool = None,
    ):
        # This parameter is required.
        self.dbinstance_name = dbinstance_name
        self.description = description
        self.gdn_mode = gdn_mode
        # This parameter is required.
        self.region_id = region_id
        self.rpl_conflict_strategy = rpl_conflict_strategy
        self.rpl_dml_strategy = rpl_dml_strategy
        self.rpl_sync_ddl = rpl_sync_ddl

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbinstance_name is not None:
            result['DBInstanceName'] = self.dbinstance_name

        if self.description is not None:
            result['Description'] = self.description

        if self.gdn_mode is not None:
            result['GdnMode'] = self.gdn_mode

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.rpl_conflict_strategy is not None:
            result['RplConflictStrategy'] = self.rpl_conflict_strategy

        if self.rpl_dml_strategy is not None:
            result['RplDmlStrategy'] = self.rpl_dml_strategy

        if self.rpl_sync_ddl is not None:
            result['RplSyncDdl'] = self.rpl_sync_ddl

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBInstanceName') is not None:
            self.dbinstance_name = m.get('DBInstanceName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GdnMode') is not None:
            self.gdn_mode = m.get('GdnMode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RplConflictStrategy') is not None:
            self.rpl_conflict_strategy = m.get('RplConflictStrategy')

        if m.get('RplDmlStrategy') is not None:
            self.rpl_dml_strategy = m.get('RplDmlStrategy')

        if m.get('RplSyncDdl') is not None:
            self.rpl_sync_ddl = m.get('RplSyncDdl')

        return self

