# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ObserveGroupDetail(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        create_time: str = None,
        description: str = None,
        discover_rules: str = None,
        entity_summaries: List[main_models.ObserveGroupDetailEntitySummaries] = None,
        extra_info: str = None,
        favorited: bool = None,
        group_id: str = None,
        group_name: str = None,
        group_type: str = None,
        modify_time: str = None,
        origin_group_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_origin: str = None,
        workspace_id: str = None,
    ):
        # The UID of the Alibaba Cloud account to which the group belongs.
        self.ali_uid = ali_uid
        # The time when the group was created, in UTC format (yyyy-MM-ddTHH:mm:ssZ).
        self.create_time = create_time
        # The description of the observability group, which explains its business purpose.
        self.description = description
        # The list of entity discovery rules that define which entities the group automatically matches.
        self.discover_rules = discover_rules
        # The statistics of entities in the group, grouped by entity type.
        self.entity_summaries = entity_summaries
        # The extended information in JSON string format, which carries alert templates, alert contact groups, pause policies, and other configurations.
        self.extra_info = extra_info
        # Indicates whether the current user has favorited the group.
        self.favorited = favorited
        self.group_id = group_id
        # The name of the observability group. The name must be unique within the workspace.
        self.group_name = group_name
        # The type of the observability group.
        self.group_type = group_type
        # The time when the group was last modified, in UTC format (yyyy-MM-ddTHH:mm:ssZ). This value is automatically updated when any property of the resource changes.
        self.modify_time = modify_time
        # The ID of the version 1.0 application group (product_group.id). This parameter is valid only when sourceOrigin is set to synced_from_1_0.
        self.origin_group_id = origin_group_id
        # The region ID of the group.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_group_id = resource_group_id
        # The data source. Valid values:
        # - native_2_0: created natively in version 2.0.
        # - synced_from_1_0: synchronized from a version 1.0 application group.
        self.source_origin = source_origin
        # The workspace ID to which the group belongs. This value is set at the workspace level and cannot be changed after the group is created.
        self.workspace_id = workspace_id

    def validate(self):
        if self.entity_summaries:
            for v1 in self.entity_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['aliUid'] = self.ali_uid

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.description is not None:
            result['description'] = self.description

        if self.discover_rules is not None:
            result['discoverRules'] = self.discover_rules

        result['entitySummaries'] = []
        if self.entity_summaries is not None:
            for k1 in self.entity_summaries:
                result['entitySummaries'].append(k1.to_map() if k1 else None)

        if self.extra_info is not None:
            result['extraInfo'] = self.extra_info

        if self.favorited is not None:
            result['favorited'] = self.favorited

        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_name is not None:
            result['groupName'] = self.group_name

        if self.group_type is not None:
            result['groupType'] = self.group_type

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.origin_group_id is not None:
            result['originGroupId'] = self.origin_group_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.source_origin is not None:
            result['sourceOrigin'] = self.source_origin

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliUid') is not None:
            self.ali_uid = m.get('aliUid')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('discoverRules') is not None:
            self.discover_rules = m.get('discoverRules')

        self.entity_summaries = []
        if m.get('entitySummaries') is not None:
            for k1 in m.get('entitySummaries'):
                temp_model = main_models.ObserveGroupDetailEntitySummaries()
                self.entity_summaries.append(temp_model.from_map(k1))

        if m.get('extraInfo') is not None:
            self.extra_info = m.get('extraInfo')

        if m.get('favorited') is not None:
            self.favorited = m.get('favorited')

        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')

        if m.get('groupType') is not None:
            self.group_type = m.get('groupType')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('originGroupId') is not None:
            self.origin_group_id = m.get('originGroupId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sourceOrigin') is not None:
            self.source_origin = m.get('sourceOrigin')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ObserveGroupDetailEntitySummaries(DaraModel):
    def __init__(
        self,
        entity_category: str = None,
        entity_count: int = None,
        entity_domain: str = None,
        entity_type: str = None,
    ):
        # The entity category.
        self.entity_category = entity_category
        # The entity count.
        self.entity_count = entity_count
        # The entity domain.
        self.entity_domain = entity_domain
        # The entity type.
        self.entity_type = entity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.entity_category is not None:
            result['entityCategory'] = self.entity_category

        if self.entity_count is not None:
            result['entityCount'] = self.entity_count

        if self.entity_domain is not None:
            result['entityDomain'] = self.entity_domain

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('entityCategory') is not None:
            self.entity_category = m.get('entityCategory')

        if m.get('entityCount') is not None:
            self.entity_count = m.get('entityCount')

        if m.get('entityDomain') is not None:
            self.entity_domain = m.get('entityDomain')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        return self

