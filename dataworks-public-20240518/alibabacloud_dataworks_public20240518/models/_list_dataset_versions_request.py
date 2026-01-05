# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDatasetVersionsRequest(DaraModel):
    def __init__(
        self,
        creator_id: str = None,
        dataset_id: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        sort_by: str = None,
    ):
        # The creator ID.
        self.creator_id = creator_id
        # The dataset ID.
        # 
        # This parameter is required.
        self.dataset_id = dataset_id
        # The sort order. Default: Desc.
        # 
        # Valid values:
        # 
        # *   Asc: Ascending.
        # *   Desc: Descending.
        self.order = order
        # The page number. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 10. Maximum: 100.
        self.page_size = page_size
        # The sort field. Default: VersionNumber.
        # 
        # Valid values:
        # 
        # *   ModifyTime: Modification time.
        # *   CreateTime: Creation time.
        # *   VersionNumber: Version number.
        self.sort_by = sort_by

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        return self

