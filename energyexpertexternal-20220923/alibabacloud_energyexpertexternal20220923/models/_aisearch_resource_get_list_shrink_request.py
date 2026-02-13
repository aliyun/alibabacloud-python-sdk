# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AISearchResourceGetListShrinkRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        resource_ids_shrink: str = None,
        type: str = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.resource_ids_shrink = resource_ids_shrink
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_ids_shrink is not None:
            result['resourceIds'] = self.resource_ids_shrink

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceIds') is not None:
            self.resource_ids_shrink = m.get('resourceIds')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

