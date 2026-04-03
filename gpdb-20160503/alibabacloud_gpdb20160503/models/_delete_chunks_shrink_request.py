# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteChunksShrinkRequest(DaraModel):
    def __init__(
        self,
        chunk_ids_shrink: str = None,
        collection: str = None,
        dbinstance_id: str = None,
        namespace: str = None,
        namespace_password: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.chunk_ids_shrink = chunk_ids_shrink
        # This parameter is required.
        self.collection = collection
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        self.namespace = namespace
        # This parameter is required.
        self.namespace_password = namespace_password
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_ids_shrink is not None:
            result['ChunkIds'] = self.chunk_ids_shrink

        if self.collection is not None:
            result['Collection'] = self.collection

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.namespace_password is not None:
            result['NamespacePassword'] = self.namespace_password

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkIds') is not None:
            self.chunk_ids_shrink = m.get('ChunkIds')

        if m.get('Collection') is not None:
            self.collection = m.get('Collection')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('NamespacePassword') is not None:
            self.namespace_password = m.get('NamespacePassword')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

