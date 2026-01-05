# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddEntityIntoMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        meta_collection_id: str = None,
        remark: str = None,
    ):
        # The entity ID. Currently, only table entities are supported. You can call the ListTables operation to obtain the ID.
        # 
        # This parameter is required.
        self.id = id
        # The collection ID. You can refer to the return result of the ListMetaCollections operation.
        # 
        # This parameter is required.
        self.meta_collection_id = meta_collection_id
        # Remarks added when adding the entity to a collection. This parameter is currently valid only for album collections.
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.meta_collection_id is not None:
            result['MetaCollectionId'] = self.meta_collection_id

        if self.remark is not None:
            result['Remark'] = self.remark

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetaCollectionId') is not None:
            self.meta_collection_id = m.get('MetaCollectionId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        return self

