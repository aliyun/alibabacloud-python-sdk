# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppGroupsShrinkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        name: str = None,
        page_number: int = None,
        page_size: int = None,
        resource_group_id: str = None,
        sort_by: int = None,
        tags_shrink: str = None,
        type: str = None,
    ):
        # The ID of the instance. Exact match is used.
        self.instance_id = instance_id
        # The name of the application.
        self.name = name
        # The page number. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 10.
        self.page_size = page_size
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The method based on which applications are sorted. Valid values:
        # 
        # *   0: sorts applications in descending order by creation time.
        # *   1: sorts applications in descending order by modification time.
        # 
        # Default value: 0.
        self.sort_by = sort_by
        # The tags.
        self.tags_shrink = tags_shrink
        # The type of the application. Valid values:
        # 
        # *   standard: a High-performance Search Edition application.
        # *   enhanced: an Industry Algorithm Edition application.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.name is not None:
            result['name'] = self.name

        if self.page_number is not None:
            result['pageNumber'] = self.page_number

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.sort_by is not None:
            result['sortBy'] = self.sort_by

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sortBy') is not None:
            self.sort_by = m.get('sortBy')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

