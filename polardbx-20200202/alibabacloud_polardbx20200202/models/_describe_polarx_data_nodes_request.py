# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarxDataNodesRequest(DaraModel):
    def __init__(
        self,
        node_type: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        search_key: str = None,
    ):
        self.node_type = node_type
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.region_id = region_id
        self.search_key = search_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_type is not None:
            result['NodeType'] = self.node_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.search_key is not None:
            result['SearchKey'] = self.search_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeType') is not None:
            self.node_type = m.get('NodeType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SearchKey') is not None:
            self.search_key = m.get('SearchKey')

        return self

