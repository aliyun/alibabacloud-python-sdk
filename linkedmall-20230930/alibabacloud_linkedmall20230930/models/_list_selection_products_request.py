# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSelectionProductsRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        purchaser_id: str = None,
    ):
        # The page number. The value must be 1 or greater.
        # 
        # This parameter is required.
        self.page_number = page_number
        # The number of entries per page. Valid values: 1 to 20.
        # 
        # This parameter is required.
        self.page_size = page_size
        # The ID of the purchaser.
        # 
        # This parameter is required.
        self.purchaser_id = purchaser_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.purchaser_id is not None:
            result['purchaserId'] = self.purchaser_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('purchaserId') is not None:
            self.purchaser_id = m.get('purchaserId')

        return self

