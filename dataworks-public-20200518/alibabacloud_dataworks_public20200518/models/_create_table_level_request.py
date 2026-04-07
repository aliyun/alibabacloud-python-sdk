# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateTableLevelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        level_type: int = None,
        name: str = None,
        project_id: int = None,
    ):
        # The description of the table level.
        self.description = description
        # The type of the table level. Valid values: 1 and 2. The value 1 indicates the logical level. The value 2 indicates the physical level.
        # 
        # This parameter is required.
        self.level_type = level_type
        # The name of the table level.
        # 
        # This parameter is required.
        self.name = name
        # The DataWorks workspace ID.
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.name is not None:
            result['Name'] = self.name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

