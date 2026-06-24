# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class MigrateToOtherZoneRequest(DaraModel):
    def __init__(
        self,
        body: str = None,
        dry_run: bool = None,
    ):
        self.body = body
        # Specifies whether to perform a dry run to check whether zone node migration is feasible. Valid values:
        # - true: performs only a validation check without executing the migration task.
        # - false: executes the migration task after the validation check succeeds.
        # 
        # This parameter is required.
        self.dry_run = dry_run

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.body is not None:
            result['body'] = self.body

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        return self

