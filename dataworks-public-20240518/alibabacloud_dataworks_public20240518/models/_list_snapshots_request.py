# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSnapshotsRequest(DaraModel):
    def __init__(
        self,
        namespace: str = None,
        object_id: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        # The namespace (project space projectId or personal space baseId).
        # 
        # This parameter is required.
        self.namespace = namespace
        # The unique ID of the object.
        # 
        # This parameter is required.
        self.object_id = object_id
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # The snapshot type. Multiple values are supported. Valid values: Saved, Deployed, and UnDeployed.
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
        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.object_id is not None:
            result['ObjectId'] = self.object_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('ObjectId') is not None:
            self.object_id = m.get('ObjectId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

