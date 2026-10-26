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
        # 分组归属的阿里云主账号 UID。
        self.ali_uid = ali_uid
        # 创建时间，UTC 格式 yyyy-MM-ddTHH:mm:ssZ。
        self.create_time = create_time
        # 观测分组描述（业务用途说明）。
        self.description = description
        # 实体发现规则列表，定义分组自动匹配哪些实体。
        self.discover_rules = discover_rules
        # 各分类实体数量。key=分类 domain（acs=云产品 / apm / rum，可扩展），value=该分类下属于本分组的实体数。仅 withEntityCount=true 时返回。
        self.entity_counts = entity_counts
        # 扩展信息（JSON 字符串，承载告警模板/联系人组/暂停策略等）。
        self.extra_info = extra_info
        # 当前用户是否已关注该分组（「我的关注」筛选依据）。
        self.favorited = favorited
        # 观测分组全局唯一 ID，格式 og-<16位hash>，指标/告警/控制台统一使用。
        self.group_id = group_id
        # 观测分组名称（同 workspace 下唯一）。
        self.group_name = group_name
        # 观测分组类型。
        self.group_type = group_type
        # 分组健康状态：-1 未知（占位）/ 1 健康 / 0 不健康。
        self.health = health
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

