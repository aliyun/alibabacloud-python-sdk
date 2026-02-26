# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateAggregateConfigRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_scope: str = None,
        aggregator_id: str = None,
        client_token: str = None,
        conditions: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.UpdateAggregateConfigRuleShrinkRequestExcludeTagsScope] = None,
        folder_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_name_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        tag_shrink: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.UpdateAggregateConfigRuleShrinkRequestTagsScope] = None,
    ):
        # The rule applies only to resources of the specified member accounts. Separate multiple member account IDs with a comma (,).
        # 
        # > This parameter applies only to rule templates.
        self.account_ids_scope = account_ids_scope
        # The account group ID.
        # 
        # For more information, see [ListAggregators]().
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # A client token used to ensure the idempotence of the request. Make sure that the client token is unique for each request. The `ClientToken` can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The conditions for the custom rule, specified in JSON format.
        self.conditions = conditions
        # The rule ID.
        # 
        # For more information, see [ListAggregateConfigRules]().
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The rule name.
        # 
        # For more information, see [ListAggregateConfigRules]().
        self.config_rule_name = config_rule_name
        # The trigger mechanism of the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: Configuration changes.
        # 
        # - ScheduledNotification: Scheduled execution.
        # 
        # > You can modify this parameter only for custom rules.
        self.config_rule_trigger_types = config_rule_trigger_types
        # The description of the rule.
        self.description = description
        # The member accounts to exclude. The rule does not apply to resources of these member accounts. Separate multiple member account IDs with a comma (,).
        # 
        # > This parameter applies only to rule templates.
        self.exclude_account_ids_scope = exclude_account_ids_scope
        # The folders to exclude. The rule does not apply to resources of member accounts in these folders. Separate multiple folder IDs with a comma (,).
        # 
        # > - This parameter applies only to rules in a global account group.
        # >
        # > - This parameter applies only to rule templates.
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        # The regions to exclude. The rule does not apply to resources in these regions. Separate multiple region IDs with a comma (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The resource groups to exclude. The rule does not apply to resources in these resource groups. Separate multiple resource group IDs with a comma (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The resources to exclude. The rule does not apply to these resources. Separate multiple resource IDs with a comma (,).
        # 
        # > This parameter applies only to rule templates.
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The excluded tag scope.
        self.exclude_tags_scope = exclude_tags_scope
        # The rule applies only to resources of member accounts in the specified resource directory IDs.
        # 
        # > - This parameter applies only to rules in a global account group.
        # >
        # > - This parameter applies only to rule templates.
        self.folder_ids_scope = folder_ids_scope
        # The rule parameters.
        self.input_parameters_shrink = input_parameters_shrink
        # The frequency at which the rule runs. Valid values:
        # 
        # - One_Hour: 1 hour.
        # 
        # - Three_Hours: 3 hours.
        # 
        # - Six_Hours: 6 hours.
        # 
        # - Twelve_Hours: 12 hours.
        # 
        # - TwentyFour_Hours: 24 hours.
        # 
        # > This parameter is required if you set `ConfigRuleTriggerTypes` to `ScheduledNotification`.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The rule applies only to resources in the specified region IDs. Separate multiple region IDs with a comma (,).
        # 
        # > This parameter applies only to rule templates.
        self.region_ids_scope = region_ids_scope
        # The rule applies only to resources in the specified resource group IDs. Separate multiple resource group IDs with a comma (,).
        # 
        # > This parameter applies only to rule templates.
        self.resource_group_ids_scope = resource_group_ids_scope
        # The rule applies only to the specified resource IDs. Separate multiple resource IDs with a comma (,).
        self.resource_ids_scope = resource_ids_scope
        # The rule applies only to resources with the specified resource name.
        self.resource_name_scope = resource_name_scope
        # The resource types that the rule evaluates. Separate multiple resource types with a comma (,).
        self.resource_types_scope_shrink = resource_types_scope_shrink
        # The risk level of the rule. Valid values:
        # 
        # - 1: high risk.
        # 
        # - 2: medium risk.
        # 
        # - 3: low risk.
        self.risk_level = risk_level
        # The rule applies only to resources with the specified resource name.
        self.tag_shrink = tag_shrink
        # The logical relationship for multiple tags in the `TagsScope` parameter. For example, if you set the `TagsScope` parameter to `"TagsScope.1.TagKey":"a","TagsScope.1.TagValue":"a","TagsScope.2.TagKey":"b","TagsScope.2.TagValue":"b"` and set this parameter to `AND`, the rule applies only to resources that have both the `a:a` and `b:b` tags. If you do not set this parameter, the default value is `OR`.
        # 
        # This parameter also works with the deprecated `TagKeyScope` parameter (not recommended). For example, if you set the `TagKeyScope` parameter to `ECS,OSS` and set this parameter to `AND`, the rule applies only to resources that have both the `ECS` and `OSS` tags.
        # 
        # Valid values:
        # 
        # - AND: Logical AND.
        # 
        # - OR: Logical OR.
        self.tag_key_logic_scope = tag_key_logic_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources with the specified tag.
        # 
        # > This parameter applies only to rule templates. You must specify both `TagKeyScope` and `TagValueScope`.
        self.tag_key_scope = tag_key_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources with the specified tag.
        # 
        # > This parameter applies only to rule templates. You must specify both `TagKeyScope` and `TagValueScope`.
        self.tag_value_scope = tag_value_scope
        # The tag scope.
        self.tags_scope = tags_scope

    def validate(self):
        if self.exclude_tags_scope:
            for v1 in self.exclude_tags_scope:
                 if v1:
                    v1.validate()
        if self.tags_scope:
            for v1 in self.tags_scope:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_ids_scope is not None:
            result['AccountIdsScope'] = self.account_ids_scope

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.conditions is not None:
            result['Conditions'] = self.conditions

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types

        if self.description is not None:
            result['Description'] = self.description

        if self.exclude_account_ids_scope is not None:
            result['ExcludeAccountIdsScope'] = self.exclude_account_ids_scope

        if self.exclude_folder_ids_scope is not None:
            result['ExcludeFolderIdsScope'] = self.exclude_folder_ids_scope

        if self.exclude_region_ids_scope is not None:
            result['ExcludeRegionIdsScope'] = self.exclude_region_ids_scope

        if self.exclude_resource_group_ids_scope is not None:
            result['ExcludeResourceGroupIdsScope'] = self.exclude_resource_group_ids_scope

        if self.exclude_resource_ids_scope is not None:
            result['ExcludeResourceIdsScope'] = self.exclude_resource_ids_scope

        result['ExcludeTagsScope'] = []
        if self.exclude_tags_scope is not None:
            for k1 in self.exclude_tags_scope:
                result['ExcludeTagsScope'].append(k1.to_map() if k1 else None)

        if self.folder_ids_scope is not None:
            result['FolderIdsScope'] = self.folder_ids_scope

        if self.input_parameters_shrink is not None:
            result['InputParameters'] = self.input_parameters_shrink

        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency

        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope

        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope

        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope

        if self.resource_name_scope is not None:
            result['ResourceNameScope'] = self.resource_name_scope

        if self.resource_types_scope_shrink is not None:
            result['ResourceTypesScope'] = self.resource_types_scope_shrink

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope

        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope

        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope

        result['TagsScope'] = []
        if self.tags_scope is not None:
            for k1 in self.tags_scope:
                result['TagsScope'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountIdsScope') is not None:
            self.account_ids_scope = m.get('AccountIdsScope')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Conditions') is not None:
            self.conditions = m.get('Conditions')

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ExcludeAccountIdsScope') is not None:
            self.exclude_account_ids_scope = m.get('ExcludeAccountIdsScope')

        if m.get('ExcludeFolderIdsScope') is not None:
            self.exclude_folder_ids_scope = m.get('ExcludeFolderIdsScope')

        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')

        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')

        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')

        self.exclude_tags_scope = []
        if m.get('ExcludeTagsScope') is not None:
            for k1 in m.get('ExcludeTagsScope'):
                temp_model = main_models.UpdateAggregateConfigRuleShrinkRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')

        if m.get('InputParameters') is not None:
            self.input_parameters_shrink = m.get('InputParameters')

        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('ResourceNameScope') is not None:
            self.resource_name_scope = m.get('ResourceNameScope')

        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope_shrink = m.get('ResourceTypesScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.UpdateAggregateConfigRuleShrinkRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class UpdateAggregateConfigRuleShrinkRequestTagsScope(DaraModel):
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
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

class UpdateAggregateConfigRuleShrinkRequestExcludeTagsScope(DaraModel):
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
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self

