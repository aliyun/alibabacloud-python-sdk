# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ObserveGroup(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        create_time: str = None,
        description: str = None,
        discover_rules: List[main_models.ObserveGroupDiscoverRule] = None,
        entity_counts: Dict[str, int] = None,
        extra_info: str = None,
        favorited: bool = None,
        group_id: str = None,
        group_name: str = None,
        group_type: str = None,
        health: int = None,
        modify_time: str = None,
        og_entity_info_enabled: bool = None,
        og_entity_info_prom_instances: List[main_models.ObserveGroupPromInstance] = None,
        origin_group_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_origin: str = None,
        tags: List[main_models.ObserveGroupTags] = None,
        workspace_id: str = None,
    ):
        # The UID of the Alibaba Cloud account to which the group belongs.
        self.ali_uid = ali_uid
        # The creation time in UTC format: yyyy-MM-ddTHH:mm:ssZ.
        self.create_time = create_time
        # The description of the observability group, which explains its business purpose.
        self.description = description
        # The list of entity discovery rules that define which entities the group automatically matches.
        self.discover_rules = discover_rules
        # The number of entities in each category. The key is the category domain (acs for cloud services, apm, or rum, which is extensible). The value is the number of entities in that category that belong to this group. Returned only when withEntityCount is set to true.
        self.entity_counts = entity_counts
        # The extended information as a JSON string, which carries alert templates, alert contact groups, and suspension policies.
        self.extra_info = extra_info
        # Indicates whether the current user has followed this group. This value is used as the filter criterion for the My Favorites feature.
        self.favorited = favorited
        # The globally unique ID of the observability group. Format: og-<16-character hash>. Used uniformly across metrics, alerts, and consoles.
        self.group_id = group_id
        # The name of the observability group. Must be unique within the same workspace.
        self.group_name = group_name
        # The type of the observability group.
        self.group_type = group_type
        # The health status of the group. Valid values:
        # - -1: unknown (placeholder).
        # - 1: healthy.
        # - 0: unhealthy.
        self.health = health
        # The last modification time in UTC format: yyyy-MM-ddTHH:mm:ssZ. Automatically updated when any resource attribute changes.
        self.modify_time = modify_time
        # Specifies whether og_entity_info metric output is enabled. When enabled, the data plane writes the group membership information to the target Prometheus instance.
        self.og_entity_info_enabled = og_entity_info_enabled
        # The set of Prometheus instances to which og_entity_info is written. Includes two source types: system (automatically identified by the system) and custom (user-defined).
        self.og_entity_info_prom_instances = og_entity_info_prom_instances
        # The product_group.id of the version 1.0 application group. This parameter is valid only when sourceOrigin is set to synced_from_1_0.
        self.origin_group_id = origin_group_id
        # The region ID to which the group belongs.
        self.region_id = region_id
        # The Alibaba Cloud resource group ID.
        self.resource_group_id = resource_group_id
        # The data source. Valid values:
        # - native_2_0: created natively in version 2.0.
        # - synced_from_1_0: synchronized from a version 1.0 application group.
        self.source_origin = source_origin
        # The resource tags (Alibaba Cloud standard tags) as an array of key-value pairs.
        self.tags = tags
        # The workspace ID to which the group belongs. This value is set at the workspace level and cannot be changed after creation.
        self.workspace_id = workspace_id

    def validate(self):
        if self.discover_rules:
            for v1 in self.discover_rules:
                 if v1:
                    v1.validate()
        if self.og_entity_info_prom_instances:
            for v1 in self.og_entity_info_prom_instances:
                 if v1:
                    v1.validate()
        if self.tags:
            for v1 in self.tags:
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

        result['discoverRules'] = []
        if self.discover_rules is not None:
            for k1 in self.discover_rules:
                result['discoverRules'].append(k1.to_map() if k1 else None)

        if self.entity_counts is not None:
            result['entityCounts'] = self.entity_counts

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

        if self.health is not None:
            result['health'] = self.health

        if self.modify_time is not None:
            result['modifyTime'] = self.modify_time

        if self.og_entity_info_enabled is not None:
            result['ogEntityInfoEnabled'] = self.og_entity_info_enabled

        result['ogEntityInfoPromInstances'] = []
        if self.og_entity_info_prom_instances is not None:
            for k1 in self.og_entity_info_prom_instances:
                result['ogEntityInfoPromInstances'].append(k1.to_map() if k1 else None)

        if self.origin_group_id is not None:
            result['originGroupId'] = self.origin_group_id

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.source_origin is not None:
            result['sourceOrigin'] = self.source_origin

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

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

        self.discover_rules = []
        if m.get('discoverRules') is not None:
            for k1 in m.get('discoverRules'):
                temp_model = main_models.ObserveGroupDiscoverRule()
                self.discover_rules.append(temp_model.from_map(k1))

        if m.get('entityCounts') is not None:
            self.entity_counts = m.get('entityCounts')

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

        if m.get('health') is not None:
            self.health = m.get('health')

        if m.get('modifyTime') is not None:
            self.modify_time = m.get('modifyTime')

        if m.get('ogEntityInfoEnabled') is not None:
            self.og_entity_info_enabled = m.get('ogEntityInfoEnabled')

        self.og_entity_info_prom_instances = []
        if m.get('ogEntityInfoPromInstances') is not None:
            for k1 in m.get('ogEntityInfoPromInstances'):
                temp_model = main_models.ObserveGroupPromInstance()
                self.og_entity_info_prom_instances.append(temp_model.from_map(k1))

        if m.get('originGroupId') is not None:
            self.origin_group_id = m.get('originGroupId')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('sourceOrigin') is not None:
            self.source_origin = m.get('sourceOrigin')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ObserveGroupTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ObserveGroupTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_value is not None:
            result['tagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')

        return self

