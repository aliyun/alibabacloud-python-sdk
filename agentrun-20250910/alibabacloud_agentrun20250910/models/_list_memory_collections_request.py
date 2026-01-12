# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMemoryCollectionsRequest(DaraModel):
    def __init__(
        self,
        memory_collection_name: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        type: str = None,
    ):
        self.memory_collection_name = memory_collection_name
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.memory_collection_name is not None:
            result['memoryCollectionName'] = self.memory_collection_name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.status is not None:
            result['status'] = self.status

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('memoryCollectionName') is not None:
            self.memory_collection_name = m.get('memoryCollectionName')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

