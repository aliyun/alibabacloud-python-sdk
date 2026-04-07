# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddMetaCollectionEntityRequest(DaraModel):
    def __init__(
        self,
        collection_qualified_name: str = None,
        entity_qualified_name: str = None,
        remark: str = None,
    ):
        # The unique identifier of the collection.
        # 
        # This parameter is required.
        self.collection_qualified_name = collection_qualified_name
        # The unique identifier of the entity. Example: maxcompute-table.projectA.tableA.
        # 
        # This parameter is required.
        self.entity_qualified_name = entity_qualified_name
        # The remarks of the entity. Example: latest product table.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_qualified_name is not None:
            result['CollectionQualifiedName'] = self.collection_qualified_name

        if self.entity_qualified_name is not None:
            result['EntityQualifiedName'] = self.entity_qualified_name

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionQualifiedName') is not None:
            self.collection_qualified_name = m.get('CollectionQualifiedName')

        if m.get('EntityQualifiedName') is not None:
            self.entity_qualified_name = m.get('EntityQualifiedName')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

