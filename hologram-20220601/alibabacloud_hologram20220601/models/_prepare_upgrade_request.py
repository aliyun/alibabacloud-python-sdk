# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PrepareUpgradeRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        dry_run: bool = None,
        version: str = None,
    ):
        self.region_id = region_id
        self.dry_run = dry_run
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

