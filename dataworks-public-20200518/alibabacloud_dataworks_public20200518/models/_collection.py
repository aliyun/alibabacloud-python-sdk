# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Collection(DaraModel):
    def __init__(
        self,
        collection_type: str = None,
        comment: str = None,
        create_time: int = None,
        level: int = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        qualified_name: str = None,
        update_time: int = None,
    ):
        # The type of the collection. Valid values:
        # 
        # *   **ALBUM**: data album
        # *   **ALBUM_CATEGORY**: category in a data album
        self.collection_type = collection_type
        # The remarks.
        self.comment = comment
        # The creation time.
        self.create_time = create_time
        # The level of the collection. This parameter takes effect only if the CollectionType parameter is set to ALBUM_CATEGORY. Maximum value: 4.
        self.level = level
        # The name of the collection.
        self.name = name
        # The ID of the Alibaba Cloud account that is used by the collection owner.
        self.owner_id = owner_id
        # The name of the collection owner.
        self.owner_name = owner_name
        # The unique identifier of the collection.
        self.qualified_name = qualified_name
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_type is not None:
            result['CollectionType'] = self.collection_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.level is not None:
            result['Level'] = self.level

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.qualified_name is not None:
            result['QualifiedName'] = self.qualified_name

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('QualifiedName') is not None:
            self.qualified_name = m.get('QualifiedName')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

