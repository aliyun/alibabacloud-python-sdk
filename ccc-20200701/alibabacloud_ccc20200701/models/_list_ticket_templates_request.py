# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTicketTemplatesRequest(DaraModel):
    def __init__(
        self,
        category_id: str = None,
        instance_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_pattern: str = None,
        state: str = None,
    ):
        # The ID of the ticket category.
        self.category_id = category_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number. The value must be between 1 and 100.
        self.page_number = page_number
        # The number of entries per page. The value must be between 1 and 100.
        self.page_size = page_size
        # The name of the template. Fuzzy search is supported.
        self.search_pattern = search_pattern
        # The status of the template.
        # 
        # - Enabled: The template is published.
        # 
        # - Disabled: The template is unpublished.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_id is not None:
            result['CategoryId'] = self.category_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_pattern is not None:
            result['SearchPattern'] = self.search_pattern

        if self.state is not None:
            result['State'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchPattern') is not None:
            self.search_pattern = m.get('SearchPattern')

        if m.get('State') is not None:
            self.state = m.get('State')

        return self

