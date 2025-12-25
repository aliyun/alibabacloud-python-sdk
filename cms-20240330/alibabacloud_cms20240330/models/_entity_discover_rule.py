# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class EntityDiscoverRule(DaraModel):
    def __init__(
        self,
        annotations: List[main_models.EntityDiscoverRuleAnnotations] = None,
        entity_types: List[str] = None,
        field_rules: List[main_models.EntityDiscoverRuleFieldRules] = None,
        instance_ids: List[str] = None,
        ip_match_rule: List[main_models.EntityDiscoverRuleIpMatchRule] = None,
        labels: List[main_models.EntityDiscoverRuleLabels] = None,
        region_ids: List[str] = None,
        resource_group_id: str = None,
        tags: List[main_models.EntityDiscoverRuleTags] = None,
    ):
        self.annotations = annotations
        self.entity_types = entity_types
        self.field_rules = field_rules
        self.instance_ids = instance_ids
        self.ip_match_rule = ip_match_rule
        self.labels = labels
        self.region_ids = region_ids
        self.resource_group_id = resource_group_id
        self.tags = tags

    def validate(self):
        if self.annotations:
            for v1 in self.annotations:
                 if v1:
                    v1.validate()
        if self.field_rules:
            for v1 in self.field_rules:
                 if v1:
                    v1.validate()
        if self.ip_match_rule:
            for v1 in self.ip_match_rule:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
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
        result['annotations'] = []
        if self.annotations is not None:
            for k1 in self.annotations:
                result['annotations'].append(k1.to_map() if k1 else None)

        if self.entity_types is not None:
            result['entityTypes'] = self.entity_types

        result['fieldRules'] = []
        if self.field_rules is not None:
            for k1 in self.field_rules:
                result['fieldRules'].append(k1.to_map() if k1 else None)

        if self.instance_ids is not None:
            result['instanceIds'] = self.instance_ids

        result['ipMatchRule'] = []
        if self.ip_match_rule is not None:
            for k1 in self.ip_match_rule:
                result['ipMatchRule'].append(k1.to_map() if k1 else None)

        result['labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['labels'].append(k1.to_map() if k1 else None)

        if self.region_ids is not None:
            result['regionIds'] = self.region_ids

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.annotations = []
        if m.get('annotations') is not None:
            for k1 in m.get('annotations'):
                temp_model = main_models.EntityDiscoverRuleAnnotations()
                self.annotations.append(temp_model.from_map(k1))

        if m.get('entityTypes') is not None:
            self.entity_types = m.get('entityTypes')

        self.field_rules = []
        if m.get('fieldRules') is not None:
            for k1 in m.get('fieldRules'):
                temp_model = main_models.EntityDiscoverRuleFieldRules()
                self.field_rules.append(temp_model.from_map(k1))

        if m.get('instanceIds') is not None:
            self.instance_ids = m.get('instanceIds')

        self.ip_match_rule = []
        if m.get('ipMatchRule') is not None:
            for k1 in m.get('ipMatchRule'):
                temp_model = main_models.EntityDiscoverRuleIpMatchRule()
                self.ip_match_rule.append(temp_model.from_map(k1))

        self.labels = []
        if m.get('labels') is not None:
            for k1 in m.get('labels'):
                temp_model = main_models.EntityDiscoverRuleLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('regionIds') is not None:
            self.region_ids = m.get('regionIds')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.EntityDiscoverRuleTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class EntityDiscoverRuleTags(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
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

class EntityDiscoverRuleLabels(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
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

class EntityDiscoverRuleIpMatchRule(DaraModel):
    def __init__(
        self,
        ip_cidr: str = None,
        ip_field_key: str = None,
    ):
        self.ip_cidr = ip_cidr
        self.ip_field_key = ip_field_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_cidr is not None:
            result['ipCIDR'] = self.ip_cidr

        if self.ip_field_key is not None:
            result['ipFieldKey'] = self.ip_field_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipCIDR') is not None:
            self.ip_cidr = m.get('ipCIDR')

        if m.get('ipFieldKey') is not None:
            self.ip_field_key = m.get('ipFieldKey')

        return self

class EntityDiscoverRuleFieldRules(DaraModel):
    def __init__(
        self,
        field_key: str = None,
        field_values: List[str] = None,
        op: str = None,
    ):
        self.field_key = field_key
        self.field_values = field_values
        self.op = op

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.field_key is not None:
            result['fieldKey'] = self.field_key

        if self.field_values is not None:
            result['fieldValues'] = self.field_values

        if self.op is not None:
            result['op'] = self.op

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fieldKey') is not None:
            self.field_key = m.get('fieldKey')

        if m.get('fieldValues') is not None:
            self.field_values = m.get('fieldValues')

        if m.get('op') is not None:
            self.op = m.get('op')

        return self

class EntityDiscoverRuleAnnotations(DaraModel):
    def __init__(
        self,
        op: str = None,
        tag_key: str = None,
        tag_values: List[str] = None,
    ):
        self.op = op
        self.tag_key = tag_key
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

