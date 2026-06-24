# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceIndicesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        is_managed: bool = None,
        is_openstore: bool = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # Specifies whether to retrieve all indexes. Valid values:
        # 
        # - true: Returns the index list that includes system indexes.
        # 
        # - false (default): Returns the index list that excludes system indexes.
        self.all = all
        # Specifies whether to display only managed indexes. Valid values:
        # 
        # - true: Displays only managed indexes.
        # 
        # - false (default): Displays all indexes.
        self.is_managed = is_managed
        # Specifies whether to display only OpenStore cold-phase indexes. Valid values:
        # 
        # - true: Displays only OpenStore cold-phase indexes.
        # 
        # - false (default): Displays all indexes.
        self.is_openstore = is_openstore
        # The index name. Fuzzy match is supported.
        self.name = name
        # The page number of the instance list. Minimum value: 1. Default value: 1.
        self.page = page
        # The number of entries per page for paging. Maximum value: 100. Default value: 20.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.is_managed is not None:
            result['isManaged'] = self.is_managed

        if self.is_openstore is not None:
            result['isOpenstore'] = self.is_openstore

        if self.name is not None:
            result['name'] = self.name

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')

        if m.get('isOpenstore') is not None:
            self.is_openstore = m.get('isOpenstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self

