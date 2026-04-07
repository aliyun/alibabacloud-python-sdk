# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateTableModelInfoRequest(DaraModel):
    def __init__(
        self,
        first_level_theme_id: int = None,
        level_id: int = None,
        level_type: int = None,
        second_level_theme_id: int = None,
        table_guid: str = None,
    ):
        # The ID of the first-level table folder.
        self.first_level_theme_id = first_level_theme_id
        # The table level ID.
        self.level_id = level_id
        # The type of the table level. Valid values: 1 and 2. The value 1 indicates the logical level. The value 2 indicates the physical level.
        self.level_type = level_type
        # The ID of the second-level table folder.
        self.second_level_theme_id = second_level_theme_id
        # The GUID of the table. Specify the GUID in the odps.{projectName}.{tableName} format.
        # 
        # This parameter is required.
        self.table_guid = table_guid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_level_theme_id is not None:
            result['FirstLevelThemeId'] = self.first_level_theme_id

        if self.level_id is not None:
            result['LevelId'] = self.level_id

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.second_level_theme_id is not None:
            result['SecondLevelThemeId'] = self.second_level_theme_id

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstLevelThemeId') is not None:
            self.first_level_theme_id = m.get('FirstLevelThemeId')

        if m.get('LevelId') is not None:
            self.level_id = m.get('LevelId')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('SecondLevelThemeId') is not None:
            self.second_level_theme_id = m.get('SecondLevelThemeId')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        return self

