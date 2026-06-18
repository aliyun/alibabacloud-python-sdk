# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteSnapshotRequest(DaraModel):
    def __init__(
        self,
        lsn: str = None,
        project_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.lsn = lsn
        # This parameter is required.
        self.project_id = project_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lsn is not None:
            result['Lsn'] = self.lsn

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lsn') is not None:
            self.lsn = m.get('Lsn')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

