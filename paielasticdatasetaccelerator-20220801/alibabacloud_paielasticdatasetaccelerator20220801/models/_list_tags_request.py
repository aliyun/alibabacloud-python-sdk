# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTagsRequest(DaraModel):
    def __init__(
        self,
        key: str = None,
        order: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_id: str = None,
        resource_type: str = None,
        sort_by: str = None,
        value: str = None,
    ):
        self.key = key
        self.order = order
        self.page_number = page_number
        self.page_size = page_size
        self.resource_id = resource_id
        self.resource_type = resource_type
        self.sort_by = sort_by
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.order is not None:
            result['Order'] = self.order

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.sort_by is not None:
            result['SortBy'] = self.sort_by

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Order') is not None:
            self.order = m.get('Order')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

