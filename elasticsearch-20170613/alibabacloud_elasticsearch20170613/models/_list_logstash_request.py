# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListLogstashRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        instance_id: str = None,
        page: int = None,
        resource_group_id: str = None,
        size: int = None,
        tags: str = None,
        version: str = None,
    ):
        # The instance name. Fuzzy match is supported. For example, if you search for an instance named abc, instances named abc, abcde, xyabc, and xabcy may all be returned.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The page number of the instance list. Default value: 1.
        self.page = page
        # The resource group ID.
        self.resource_group_id = resource_group_id
        # The number of entries per page for paging. Default value: 20.
        self.size = size
        # The instance tags.
        self.tags = tags
        # The instance version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.page is not None:
            result['page'] = self.page

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.size is not None:
            result['size'] = self.size

        if self.tags is not None:
            result['tags'] = self.tags

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self

