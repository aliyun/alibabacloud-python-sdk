# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RemoveEntityFromMetaCollectionRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        meta_collection_id: str = None,
    ):
        # The entity ID. Currently, entities can only be tables. You can call the ListTables operation to query the ID.
        self.id = id
        # The collection ID. You can call the ListMetaCollections operation to query the ID.
        self.meta_collection_id = meta_collection_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MetaCollectionId') is not None:
            self.meta_collection_id = m.get('MetaCollectionId')

        return self

