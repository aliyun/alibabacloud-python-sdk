# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListResourcesForTagOptionRequest(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        resource_type: str = None,
        tag_option_id: str = None,
    ):
        # The number of the page to return.
        # 
        # Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries to return on each page.
        # 
        # Valid values: 1 to 100 Minimum value: 1. Default value: 10.
        self.page_size = page_size
        # The type of resource that is associated with the tag option. Valid values:
        # 
        # *   product: product
        # *   Portfolio: product portfolio
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The ID of the tag option.
        # 
        # This parameter is required.
        self.tag_option_id = tag_option_id

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

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_option_id is not None:
            result['TagOptionId'] = self.tag_option_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagOptionId') is not None:
            self.tag_option_id = m.get('TagOptionId')

        return self

