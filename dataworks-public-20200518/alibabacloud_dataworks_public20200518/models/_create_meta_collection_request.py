# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        collection_type: str = None,
        comment: str = None,
        name: str = None,
        parent_qualified_name: str = None,
    ):
        # The type of the collection.
        # 
        # This parameter is required.
        self.collection_type = collection_type
        # The comment of the collection. The comment must be 1 to 64 characters in length.
        self.comment = comment
        # The name of the collection. The name must be 1 to 32 characters in length.
        # 
        # This parameter is required.
        self.name = name
        # The unique identifier of the parent collection.
        self.parent_qualified_name = parent_qualified_name

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

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_qualified_name is not None:
            result['ParentQualifiedName'] = self.parent_qualified_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionType') is not None:
            self.collection_type = m.get('CollectionType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentQualifiedName') is not None:
            self.parent_qualified_name = m.get('ParentQualifiedName')

        return self

