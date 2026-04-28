# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeltaGetLastCursorRequest(DaraModel):
    def __init__(
        self,
        drive_id: str = None,
        sync_root_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the root file of the synced folder.
        self.sync_root_id = sync_root_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')

        return self

