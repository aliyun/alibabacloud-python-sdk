# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEntitiesByTagsShrinkRequest(DaraModel):
    def __init__(
        self,
        entity_type: str = None,
        next_token: str = None,
        page_size: int = None,
        tags_shrink: str = None,
    ):
        # The type of the entity.
        # 
        # This parameter is required.
        self.entity_type = entity_type
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The number of entries per page. Default value: 10. Valid values: 1 to 100.
        self.page_size = page_size
        # The tags.
        # 
        # This parameter is required.
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tags_shrink is not None:
            result['Tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Tags') is not None:
            self.tags_shrink = m.get('Tags')

        return self

