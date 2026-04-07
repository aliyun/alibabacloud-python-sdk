# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteTableLevelRequest(DaraModel):
    def __init__(
        self,
        level_id: int = None,
        project_id: int = None,
    ):
        # The ID of the table level that you want to delete. You can call the ListTableLevel operation to query the ID.
        # 
        # This parameter is required.
        self.level_id = level_id
        # The DataWorks workspace ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.level_id is not None:
            result['LevelId'] = self.level_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LevelId') is not None:
            self.level_id = m.get('LevelId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

