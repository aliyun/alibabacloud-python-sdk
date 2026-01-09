# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListStoreViewsRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        offset: int = None,
        size: int = None,
        store_type: str = None,
    ):
        # The dataset name that is used for fuzzy match.
        self.name = name
        # The offset of the datasets to return. Default value: 0.
        self.offset = offset
        # The number of datasets to return. Default value: 100.
        self.size = size
        # The type of the datasets to return. By default, datasets are not filtered by type.
        # 
        # Valid values:
        # 
        # *   metricstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   logstore
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.store_type = store_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        if self.store_type is not None:
            result['storeType'] = self.store_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        return self

