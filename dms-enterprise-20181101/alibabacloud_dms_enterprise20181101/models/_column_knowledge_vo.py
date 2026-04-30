# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ColumnKnowledgeVO(DaraModel):
    def __init__(
        self,
        asset_description: str = None,
        asset_modified_gmt: str = None,
        auto_increment: bool = None,
        column_id: int = None,
        column_key_type: str = None,
        column_name: str = None,
        column_type: str = None,
        description: str = None,
        hot_level: int = None,
        level: int = None,
        level_type: str = None,
        nullable: bool = None,
        plain: bool = None,
        position: int = None,
        security_level: str = None,
        table_id: int = None,
        title: str = None,
        user_sensitivity_level: str = None,
    ):
        self.asset_description = asset_description
        self.asset_modified_gmt = asset_modified_gmt
        self.auto_increment = auto_increment
        self.column_id = column_id
        self.column_key_type = column_key_type
        self.column_name = column_name
        self.column_type = column_type
        self.description = description
        self.hot_level = hot_level
        self.level = level
        self.level_type = level_type
        self.nullable = nullable
        self.plain = plain
        self.position = position
        self.security_level = security_level
        self.table_id = table_id
        self.title = title
        self.user_sensitivity_level = user_sensitivity_level

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_description is not None:
            result['AssetDescription'] = self.asset_description

        if self.asset_modified_gmt is not None:
            result['AssetModifiedGmt'] = self.asset_modified_gmt

        if self.auto_increment is not None:
            result['AutoIncrement'] = self.auto_increment

        if self.column_id is not None:
            result['ColumnId'] = self.column_id

        if self.column_key_type is not None:
            result['ColumnKeyType'] = self.column_key_type

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        if self.description is not None:
            result['Description'] = self.description

        if self.hot_level is not None:
            result['HotLevel'] = self.hot_level

        if self.level is not None:
            result['Level'] = self.level

        if self.level_type is not None:
            result['LevelType'] = self.level_type

        if self.nullable is not None:
            result['Nullable'] = self.nullable

        if self.plain is not None:
            result['Plain'] = self.plain

        if self.position is not None:
            result['Position'] = self.position

        if self.security_level is not None:
            result['SecurityLevel'] = self.security_level

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.title is not None:
            result['Title'] = self.title

        if self.user_sensitivity_level is not None:
            result['UserSensitivityLevel'] = self.user_sensitivity_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetDescription') is not None:
            self.asset_description = m.get('AssetDescription')

        if m.get('AssetModifiedGmt') is not None:
            self.asset_modified_gmt = m.get('AssetModifiedGmt')

        if m.get('AutoIncrement') is not None:
            self.auto_increment = m.get('AutoIncrement')

        if m.get('ColumnId') is not None:
            self.column_id = m.get('ColumnId')

        if m.get('ColumnKeyType') is not None:
            self.column_key_type = m.get('ColumnKeyType')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HotLevel') is not None:
            self.hot_level = m.get('HotLevel')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('LevelType') is not None:
            self.level_type = m.get('LevelType')

        if m.get('Nullable') is not None:
            self.nullable = m.get('Nullable')

        if m.get('Plain') is not None:
            self.plain = m.get('Plain')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('SecurityLevel') is not None:
            self.security_level = m.get('SecurityLevel')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('UserSensitivityLevel') is not None:
            self.user_sensitivity_level = m.get('UserSensitivityLevel')

        return self

