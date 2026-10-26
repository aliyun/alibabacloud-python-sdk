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
        discover_rules: List[main_models.ObserveGroupDiscoverRule] = None,
        entity_summaries: List[main_models.ObserveGroupDetailEntitySummaries] = None,
        extra_info: str = None,
        favorited: bool = None,
        group_id: str = None,
        group_name: str = None,
        group_type: str = None,
        modify_time: str = None,
        og_entity_info_enabled: bool = None,
        og_entity_info_prom_instances: List[main_models.ObserveGroupPromInstance] = None,
        origin_group_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        source_origin: str = None,
        tags: List[main_models.ObserveGroupDetailTags] = None,
        workspace_id: str = None,
    ):
        # 分组归属的阿里云主账号 UID。
        self.ali_uid = ali_uid
        # 创建时间，UTC 格式 yyyy-MM-ddTHH:mm:ssZ。
        self.create_time = create_time
        # 观测分组描述（业务用途说明）。
        self.description = description
        # 实体发现规则列表，定义分组自动匹配哪些实体。
        self.discover_rules = discover_rules
        # 分组内实体按类型的统计。
        self.entity_summaries = entity_summaries
        # 扩展信息（JSON 字符串，承载告警模板/联系人组/暂停策略等）。
        self.extra_info = extra_info
        # 当前用户是否已关注该分组。
        self.favorited = favorited
        self.group_id = group_id
        # 观测分组名称（同 workspace 下唯一）。
        self.group_name = group_name
        # 观测分组类型。
        self.group_type = group_type
        # 最后修改时间，UTC 格式 yyyy-MM-ddTHH:mm:ssZ。资源任意属性变更时自动更新。
        self.modify_time = modify_time
        # 是否开启 og_entity_info 指标输出。开启后数据面会把本分组归属写入目标 Prometheus 实例。
        self.og_entity_info_enabled = og_entity_info_enabled
        # 写入 og_entity_info 的 Prometheus 实例集合，包含系统自动识别(system)和用户自定义(custom)两类来源。
        self.og_entity_info_prom_instances = og_entity_info_prom_instances
        # 仅 synced_from_1_0 时填值，存 1.0 应用分组的 product_group.id。
        self.origin_group_id = origin_group_id
        # 分组所属地域 ID。
        self.region_id = region_id
        # 阿里云资源组 ID。
        self.resource_group_id = resource_group_id
        # 数据来源：native_2_0（2.0 原生）/ synced_from_1_0（从 1.0 应用分组同步）。
        self.source_origin = source_origin
        # 资源标签（阿里云标准标签），键值对数组。
        self.tags = tags
        # 分组归属的 workspace ID（workspace 级归属，创建后不可变）。
        self.workspace_id = workspace_id

    def validate(self):
        if self.discover_rules:
            for v1 in self.discover_rules:
                 if v1:
                    v1.validate()
        if self.entity_summaries:
            for v1 in self.entity_summaries:
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
                temp_model = main_models.ObserveGroupDetailTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class ObserveGroupDetailTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # 标签键。
        self.tag_key = tag_key
        # 标签值。
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

class ObserveGroupDetailEntitySummaries(DaraModel):
    def __init__(
        self,
        entity_category: str = None,
        entity_count: int = None,
        entity_domain: str = None,
        entity_type: str = None,
    ):
        # 实体分类。
        self.entity_category = entity_category
        # 实体数量。
        self.entity_count = entity_count
        # 实体域。
        self.entity_domain = entity_domain
        # 实体类型。
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

