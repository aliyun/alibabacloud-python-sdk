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
        # The ID of the entity. Currently, only the table type is supported. You can obtain the ID from the response of the ListTables operation.
        # 
        # This parameter is required.
        self.id = id
        # The ID of the collection object. You can obtain the ID from the response of the ListMetaCollections operation.
        # 
        # This parameter is required.
        self.meta_collection_id = meta_collection_id
        # The remarks when adding the entity to the collection. Currently, this parameter takes effect only for the album type.
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

