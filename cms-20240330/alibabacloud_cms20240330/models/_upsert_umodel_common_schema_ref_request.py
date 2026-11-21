# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpsertUmodelCommonSchemaRefRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        group: str = None,
        version: str = None,
    ):
        # Specifies whether to perform a dry run for this request. Valid values:
        # - true: Sends a check request without performing actual changes.
        # - false: Sends a normal request.
        # Default value: false.
        self.dry_run = dry_run
        # The public Umodel schema group.
        # 
        # This parameter is required.
        self.group = group
        # The version number.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

