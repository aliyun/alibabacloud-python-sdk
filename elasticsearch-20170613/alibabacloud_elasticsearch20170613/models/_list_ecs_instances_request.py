# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEcsInstancesRequest(DaraModel):
    def __init__(
        self,
        ecs_instance_ids: str = None,
        ecs_instance_name: str = None,
        page: int = None,
        size: int = None,
        tags: str = None,
        vpc_id: str = None,
    ):
        # The list of ECS instance IDs. The value can be a JSON array that consists of up to 100 instance IDs. Separate multiple IDs with commas (,).
        self.ecs_instance_ids = ecs_instance_ids
        # The name of the ECS instance.
        self.ecs_instance_name = ecs_instance_name
        # The page number of the returned results. Maximum value: 500.
        self.page = page
        # The number of results per page. Default value: 10. Maximum value: 500.
        self.size = size
        # Instance tags of the ECS instance. The following fields must be included:
        # 
        # - tagKey: instance tag key.
        # - tagValue: instance tag value.
        self.tags = tags
        # The ID of the VPC where the ECS instance resides.
        self.vpc_id = vpc_id

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

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

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

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self

