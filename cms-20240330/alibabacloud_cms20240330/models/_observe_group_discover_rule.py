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
        # Indicates whether the rule is enabled. If set to false, the data plane skips this rule and does not perform matching, tagging, or delivery.
        self.enabled = enabled
        # The entity type (legacy). This parameter is retained for backward compatibility. Use entityTypes instead.
        self.entity_type = entity_type
        # The list of entity types. A single rule can match across multiple types, such as acs.ecs.instance, acs.rds.instance, and acs.arms.service.
        self.entity_types = entity_types
        # The time when the rule was created, in UNIX millisecond timestamp format. This value is used for display in the console.
        self.gmt_create = gmt_create
        # The list of manually specified instance IDs. This is an enumeration type and includes instances synchronized manually in version 1.0.
        self.instance_ids = instance_ids
        # The name matching rules.
        self.name_rules = name_rules
        # The list of region IDs used for region-based filtering.
        self.region_ids = region_ids
        # The resource group ID used for filtering.
        self.resource_group_id = resource_group_id
        # The stable ID of the rule, used as an anchor for editing, deleting, and enabling or disabling operations. Format: dr-<16-character hash>.
        self.rule_id = rule_id
        # The matching method. Valid values: byTag, byResourceGroup, byInstanceName, byManual, and bySpl.
        self.rule_type = rule_type
        # The applicable scope. Valid values: all (all entity types, exclusive) and entity (specified entity types).
        self.scope = scope
        # The complete SPL expression for advanced configuration. If this parameter is not empty, it takes precedence over other filter fields.
        self.spl = spl
        # The tag matching rules.
        self.tag_rules = tag_rules
        # The UID of the user to whom the rule belongs.
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
            result['Enabled'] = self.enabled

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.entity_types is not None:
            result['EntityTypes'] = self.entity_types

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.name_rules is not None:
            result['NameRules'] = self.name_rules.to_map()

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_type is not None:
            result['RuleType'] = self.rule_type

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.spl is not None:
            result['Spl'] = self.spl

        if self.tag_rules is not None:
            result['TagRules'] = self.tag_rules.to_map()

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('EntityTypes') is not None:
            self.entity_types = m.get('EntityTypes')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('NameRules') is not None:
            temp_model = main_models.ObserveGroupDiscoverRuleNameRules()
            self.name_rules = temp_model.from_map(m.get('NameRules'))

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleType') is not None:
            self.rule_type = m.get('RuleType')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('Spl') is not None:
            self.spl = m.get('Spl')

        if m.get('TagRules') is not None:
            temp_model = main_models.ObserveGroupDiscoverRuleTagRules()
            self.tag_rules = temp_model.from_map(m.get('TagRules'))

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

class ObserveGroupDiscoverRuleTagRules(DaraModel):
    def __init__(
        self,
        op: str = None,
        tags: List[main_models.ObserveGroupDiscoverRuleTagRulesTags] = None,
    ):
        # The tag matching logic.
        self.op = op
        # The list of tag conditions.
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
            result['Op'] = self.op

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Op') is not None:
            self.op = m.get('Op')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
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
        # The matching operation.
        self.op = op
        # The tag key.
        self.tag_key = tag_key
        # The list of tag values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['Op'] = self.op

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

class ObserveGroupDiscoverRuleNameRules(DaraModel):
    def __init__(
        self,
        op: str = None,
        tags: List[main_models.ObserveGroupDiscoverRuleNameRulesTags] = None,
    ):
        # The name matching logic.
        self.op = op
        # The list of name conditions.
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
            result['Op'] = self.op

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Op') is not None:
            self.op = m.get('Op')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.ObserveGroupDiscoverRuleNameRulesTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ObserveGroupDiscoverRuleNameRulesTags(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_values: List[str] = None,
    ):
        # The matching operation.
        self.op = op
        # The list of matching values.
        self.tag_values = tag_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op is not None:
            result['Op'] = self.op

        if self.tag_values is not None:
            result['TagValues'] = self.tag_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Op') is not None:
            self.op = m.get('Op')

        if m.get('TagValues') is not None:
            self.tag_values = m.get('TagValues')

        return self

