# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDeltaRequest(DaraModel):
    def __init__(
        self,
        cursor: str = None,
        drive_id: str = None,
        limit: int = None,
        sync_root_id: str = None,
    ):
        # The cursor of the incremental information.
        self.cursor = cursor
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The maximum number of results to return. Valid values: 0 to 100. Default value: 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The ID of the root file of the synced folder.
        self.sync_root_id = sync_root_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cursor is not None:
            result['cursor'] = self.cursor

        if self.drive_id is not None:
            result['drive_id'] = self.drive_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')

        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')

        return self

