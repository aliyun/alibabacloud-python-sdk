# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ObserveGroupDiscoverRule(DaraModel):
    def __init__(
        self,
        enabled: bool = None,
        entity_type: str = None,
        entity_types: List[str] = None,
        gmt_create: int = None,
        instance_ids: List[str] = None,
        name_rules: main_models.ObserveGroupDiscoverRuleNameRules = None,
        region_ids: List[str] = None,
        resource_group_id: str = None,
        rule_id: str = None,
        rule_type: str = None,
        scope: str = None,
        spl: str = None,
        tag_rules: main_models.ObserveGroupDiscoverRuleTagRules = None,
        user_id: str = None,
    ):
        # 规则是否启用；false 时数据面跳过该规则（不匹配 / 不打标 / 不下发）。
        self.enabled = enabled
        # （旧）单实体类型，向后兼容，优先用 entityTypes。
        self.entity_type = entity_type
        # 实体类型列表，支持一条规则跨多类型匹配（如 acs.ecs.instance/acs.rds.instance/acs.arms.service）。
        self.entity_types = entity_types
        # 规则创建时间（Unix 毫秒时间戳），控制台展示用。
        self.gmt_create = gmt_create
        # 手动指定的实例 ID 列表（枚举型，含 1.0 手动实例同步）。
        self.instance_ids = instance_ids
        # 名称匹配规则。
        self.name_rules = name_rules
        # 按地域过滤的 region ID 列表。
        self.region_ids = region_ids
        # 按资源组过滤。
        self.resource_group_id = resource_group_id
        # 规则稳定 ID（编辑/删除/启停锚点），格式 dr-<16位hash>。
        self.rule_id = rule_id
        # 匹配方式：byTag / byResourceGroup / byInstanceName / byManual / bySpl。
        self.rule_type = rule_type
        # 适用范围：all（全部实体类型，独占）/ entity（指定实体类型）。
        self.scope = scope
        # 完整 SPL 表达式（高级配置）；非空时优先生效，覆盖其它过滤字段。
        self.spl = spl
        # 标签匹配规则。
        self.tag_rules = tag_rules
        # 规则所属用户 UID。
        self.user_id = user_id

    def validate(self):
        if self.name_rules:
            self.name_rules.validate()
        if self.tag_rules:
            self.tag_rules.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enabled is not None:
            result['enabled'] = self.enabled

        if self.entity_type is not None:
            result['entityType'] = self.entity_type

        if self.entity_types is not None:
            result['entityTypes'] = self.entity_types

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        if self.name_rules is not None:
            result['nameRules'] = self.name_rules.to_map()

        if self.region_ids is not None:
            result['regionIds'] = self.region_ids

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.rule_id is not None:
            result['ruleId'] = self.rule_id

        if self.rule_type is not None:
            result['ruleType'] = self.rule_type

        if self.scope is not None:
            result['scope'] = self.scope

        if self.spl is not None:
            result['spl'] = self.spl

        if self.tag_rules is not None:
            result['tagRules'] = self.tag_rules.to_map()

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')

        if m.get('entityType') is not None:
            self.entity_type = m.get('entityType')

        if m.get('entityTypes') is not None:
            self.entity_types = m.get('entityTypes')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        if m.get('nameRules') is not None:
            temp_model = main_models.ObserveGroupDiscoverRuleNameRules()
            self.name_rules = temp_model.from_map(m.get('nameRules'))

        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('ruleId') is not None:
            self.rule_id = m.get('ruleId')

        if m.get('ruleType') is not None:
            self.rule_type = m.get('ruleType')

        if m.get('scope') is not None:
            self.scope = m.get('scope')

        if m.get('spl') is not None:
            self.spl = m.get('spl')

        if m.get('tagRules') is not None:
            temp_model = main_models.ObserveGroupDiscoverRuleTagRules()
            self.tag_rules = temp_model.from_map(m.get('tagRules'))

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self

class ObserveGroupDiscoverRuleTagRules(DaraModel):
    def __init__(
        self,
        op: str = None,
        tags: List[main_models.ObserveGroupDiscoverRuleTagRulesTags] = None,
    ):
        # 标签匹配逻辑。
        self.op = op
        # 标签条件列表。
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ObserveGroupDiscoverRuleTagRulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ObserveGroupDiscoverRuleTagRulesTags(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        # 匹配操作。
        self.op = op
        # 标签键。
        self.tag_key = tag_key
        # 标签值列表。
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.tag_key is not None:
            result['tagKey'] = self.tag_key

        if self.tag_values is not None:
            result['tagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')

        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')

        return self

class ObserveGroupDiscoverRuleNameRules(DaraModel):
    def __init__(
        self,
        op: str = None,
        tags: List[main_models.ObserveGroupDiscoverRuleNameRulesTags] = None,
    ):
        # 名称匹配逻辑。
        self.op = op
        # 名称条件列表。
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ObserveGroupDiscoverRuleNameRulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ObserveGroupDiscoverRuleNameRulesTags(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_values: List[str] = None,
    ):
        # 匹配操作。
        self.op = op
        # 匹配值列表。
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['op'] = self.op

        if self.tag_values is not None:
            result['tagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('op') is not None:
            self.op = m.get('op')

        if m.get('tagValues') is not None:
            self.tag_values = m.get('tagValues')

        return self

