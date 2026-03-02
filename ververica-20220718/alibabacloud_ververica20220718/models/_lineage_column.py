# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LineageColumn(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        column_native_type: str = None,
        column_type: str = None,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        id: str = None,
        modified_at: int = None,
        modifier: str = None,
        nullable: bool = None,
    ):
        # The name of the column.
        self.column_name = column_name
        # The original type of the column.
        self.column_native_type = column_native_type
        # The column type.
        self.column_type = column_type
        # The creation time.
        self.created_at = created_at
        # The user that creates the column.
        self.creator = creator
        # The description.
        self.description = description
        # The field ID.
        self.id = id
        # The modification time.
        self.modified_at = modified_at
        # The ID of the account that is used to modify the column.
        self.modifier = modifier
        # Indicates whether the value is nullable.
        self.nullable = nullable

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['columnName'] = self.column_name

        if self.column_native_type is not None:
            result['columnNativeType'] = self.column_native_type

        if self.column_type is not None:
            result['columnType'] = self.column_type

        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.description is not None:
            result['description'] = self.description

        if self.id is not None:
            result['id'] = self.id

        if self.modified_at is not None:
            result['modifiedAt'] = self.modified_at

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.nullable is not None:
            result['nullable'] = self.nullable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columnName') is not None:
            self.column_name = m.get('columnName')

        if m.get('columnNativeType') is not None:
            self.column_native_type = m.get('columnNativeType')

        if m.get('columnType') is not None:
            self.column_type = m.get('columnType')

        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('modifiedAt') is not None:
            self.modified_at = m.get('modifiedAt')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('nullable') is not None:
            self.nullable = m.get('nullable')

        return self

