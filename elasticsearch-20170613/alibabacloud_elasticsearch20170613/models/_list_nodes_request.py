# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNodesRequest(DaraModel):
    def __init__(
        self,
        ecs_instance_ids: str = None,
        ecs_instance_name: str = None,
        page: int = None,
        size: int = None,
        tags: str = None,
    ):
        # The IDs of the ECS instances.
        self.ecs_instance_ids = ecs_instance_ids
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The number of the page to return.
        self.page = page
        # The number of entries to return on each page.
        self.size = size
        # The tags of the ECS instance. You must configure tagKey and tagValue.
        self.tags = tags

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ecs_instance_ids is not None:
            result['ecsInstanceIds'] = self.ecs_instance_ids

        if self.ecs_instance_name is not None:
            result['ecsInstanceName'] = self.ecs_instance_name

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        if self.tags is not None:
            result['tags'] = self.tags

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ecsInstanceIds') is not None:
            self.ecs_instance_ids = m.get('ecsInstanceIds')

        if m.get('ecsInstanceName') is not None:
            self.ecs_instance_name = m.get('ecsInstanceName')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        return self

