# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        parent_id: str = None,
        type: str = None,
    ):
        # The collection description.
        self.description = description
        # The ID of the collection.
        # 
        # This parameter is required.
        self.name = name
        # The parent collection ID.
        self.parent_id = parent_id
        # The collection name.
        # 
        # *   Category
        # *   Album
        # *   AlbumCategory: Album subcategory.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

