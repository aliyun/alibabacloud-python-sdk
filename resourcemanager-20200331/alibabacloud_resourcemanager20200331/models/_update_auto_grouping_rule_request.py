# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_resourcemanager20200331 import models as main_models
from darabonba.model import DaraModel

class UpdateAutoGroupingRuleRequest(DaraModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_resource_types_scope: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_types_scope: str = None,
        rule_contents: List[main_models.UpdateAutoGroupingRuleRequestRuleContents] = None,
        rule_desc: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        # The IDs of regions to be excluded. Separate multiple IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of resource groups to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of resources to be excluded. Separate multiple IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The resource types to be excluded. Separate multiple resource types with commas (,).
        self.exclude_resource_types_scope = exclude_resource_types_scope
        # The IDs of regions. Separate multiple IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of resource groups. Separate multiple IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of resources. Separate multiple IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The resource types. Separate multiple resource types with commas (,).
        self.resource_types_scope = resource_types_scope
        # The content records of the rule.
        # 
        # This parameter is required.
        self.rule_contents = rule_contents
        # The description of the rule.
        self.rule_desc = rule_desc
        # The ID of the rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name

    def validate(self):
        if self.rule_contents:
            for v1 in self.rule_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope

        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope

        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope

        if self.exclude_resource_types_scope is not None:
            result['ExcludeResourceTypesScope'] = self.exclude_resource_types_scope

        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope

        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope

        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope

        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope

        result['RuleContents'] = []
        if self.rule_contents is not None:
            for k1 in self.rule_contents:
                result['RuleContents'].append(k1.to_map() if k1 else None)

        if self.rule_desc is not None:
            result['RuleDesc'] = self.rule_desc

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')

        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')

        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')

        if m.get('ExcludeResourceTypesScope') is not None:
            self.exclude_resource_types_scope = m.get('ExcludeResourceTypesScope')

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')

        self.rule_contents = []
        if m.get('RuleContents') is not None:
            for k1 in m.get('RuleContents'):
                temp_model = main_models.UpdateAutoGroupingRuleRequestRuleContents()
                self.rule_contents.append(temp_model.from_map(k1))

        if m.get('RuleDesc') is not None:
            self.rule_desc = m.get('RuleDesc')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class UpdateAutoGroupingRuleRequestRuleContents(DaraModel):
    def __init__(
        self,
        auto_grouping_scope_condition: str = None,
        rule_content_id: str = None,
        target_resource_group_condition: str = None,
    ):
        # The condition for the range of resources that are automatically transferred.
        self.auto_grouping_scope_condition = auto_grouping_scope_condition
        # The ID of the content record.
        self.rule_content_id = rule_content_id
        # The condition for the destination resource group.
        # 
        # This parameter is required.
        self.target_resource_group_condition = target_resource_group_condition

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_grouping_scope_condition is not None:
            result['AutoGroupingScopeCondition'] = self.auto_grouping_scope_condition

        if self.rule_content_id is not None:
            result['RuleContentId'] = self.rule_content_id

        if self.target_resource_group_condition is not None:
            result['TargetResourceGroupCondition'] = self.target_resource_group_condition

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoGroupingScopeCondition') is not None:
            self.auto_grouping_scope_condition = m.get('AutoGroupingScopeCondition')

        if m.get('RuleContentId') is not None:
            self.rule_content_id = m.get('RuleContentId')

        if m.get('TargetResourceGroupCondition') is not None:
            self.target_resource_group_condition = m.get('TargetResourceGroupCondition')

        return self

