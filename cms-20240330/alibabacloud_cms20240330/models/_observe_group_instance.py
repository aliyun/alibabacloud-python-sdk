# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class ObserveGroupInstance(DaraModel):
    def __init__(
        self,
        category: str = None,
        dimension: Dict[str, str] = None,
        entity_domain: str = None,
        entity_type: str = None,
        group_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: Dict[str, str] = None,
        user_id: str = None,
    ):
        # 实体分类（由 entityType 适配）。
        self.category = category
        # 监控维度键值对。
        self.dimension = dimension
        # 实体域（如 acs）。
        self.entity_domain = entity_domain
        # 实体类型（如 acs.ecs.instance）。
        self.entity_type = entity_type
        # 所属观测分组 ID。
        self.group_id = group_id
        # 实例 ID。
        self.instance_id = instance_id
        # 实例名称。
        self.instance_name = instance_name
        # 实例所属地域 ID。
        self.region_id = region_id
        # 实例所属资源组 ID。
        self.resource_group_id = resource_group_id
        # 实例标签键值对。
        self.tags = tags
        # 实例归属的用户 UID。
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['category'] = self.category

        if self.dimension is not None:
            result['dimension'] = self.dimension

        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.instance_name is not None:
            result['instanceName'] = self.instance_name

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.tags is not None:
            result['tags'] = self.tags

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')

        if m.get('dimension') is not None:
            self.dimension = m.get('dimension')

        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('instanceName') is not None:
            self.instance_name = m.get('instanceName')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

