# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeSDGRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        sdgids: List[str] = None,
        same_disk_id: bool = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Default value: 10.
        self.page_size = page_size
        # The IDs of SDGs that you want to query. By default, all SDGs are queried.
        self.sdgids = sdgids
        self.same_disk_id = same_disk_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.sdgids is not None:
            result['SDGIds'] = self.sdgids

        if self.same_disk_id is not None:
            result['SameDiskId'] = self.same_disk_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SDGIds') is not None:
            self.sdgids = m.get('SDGIds')

        if m.get('SameDiskId') is not None:
            self.same_disk_id = m.get('SameDiskId')

        return self

