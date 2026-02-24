# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateConfigRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        conditions: str = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.UpdateConfigRuleShrinkRequestExcludeTagsScope] = None,
        extend_content: str = None,
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
        tags_scope: List[main_models.UpdateConfigRuleShrinkRequestTagsScope] = None,
    ):
        # A client token used to ensure the idempotence of the request. You can use a client to generate the token, but you must make sure that the token is unique for different requests. The `ClientToken` parameter can contain only ASCII characters and cannot be more than 64 characters in length.
        self.client_token = client_token
        self.conditions = conditions
        # The rule ID.
        # 
        # For more information, see [ListConfigRules](https://help.aliyun.com/document_detail/169607.html).
        # 
        # This parameter is required.
        self.config_rule_id = config_rule_id
        # The name of the rule.
        # 
        # For more information, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        self.config_rule_name = config_rule_name
        # The trigger type of the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # 
        # - ScheduledNotification: The rule is triggered on a regular basis.
        # 
        # > This parameter can be modified only for custom rules.
        self.config_rule_trigger_types = config_rule_trigger_types
        # The description of the rule. The description can be up to 500 characters in length.
        self.description = description
        # The regions where the rule is not effective. The system does not evaluate resources in these regions. To specify multiple region IDs, separate them with a comma (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The resource groups where the rule is not effective. The system does not evaluate resources in these resource groups. To specify multiple resource group IDs, separate them with a comma (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The resources that are not evaluated by the rule. The system does not evaluate these resources. To specify multiple resource IDs, separate them with a comma (,).
        # 
        # > This parameter applies only to managed rules.
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The tags that are used to exclude resources.
        self.exclude_tags_scope = exclude_tags_scope
        # The extended content. This parameter is optional. You can use this parameter with a 24-hour trigger period to set the trigger time.
        self.extend_content = extend_content
        # The input parameters of the rule.
        self.input_parameters_shrink = input_parameters_shrink
        # The frequency at which the rule is run. Valid values:
        # 
        # - One_Hour: 1 hour.
        # 
        # - Three_Hours: 3 hours.
        # 
        # - Six_Hours: 6 hours.
        # 
        # - Twelve_Hours: 12 hours.
        # 
        # - TwentyFour_Hours (default): 24 hours.
        # 
        # > This parameter is required when `ConfigRuleTriggerTypes` is set to `ScheduledNotification`.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The regions where the rule is effective. The rule evaluates only resources in these regions. To specify multiple region IDs, separate them with a comma (,).
        # 
        # > This parameter applies only to managed rules.
        self.region_ids_scope = region_ids_scope
        # The resource groups where the rule is effective. The rule evaluates only resources in these resource groups. To specify multiple resource group IDs, separate them with a comma (,).
        # 
        # > This parameter applies only to managed rules.
        self.resource_group_ids_scope = resource_group_ids_scope
        # The resources that the rule evaluates. To specify multiple resource IDs, separate them with a comma (,).
        self.resource_ids_scope = resource_ids_scope
        # The names of the resources that the rule evaluates.
        self.resource_name_scope = resource_name_scope
        # The resource types that the rule evaluates. To specify multiple resource types, separate them with a comma (,).
        self.resource_types_scope_shrink = resource_types_scope_shrink
        # The risk level of the rule. Valid values:
        # 
        # - 1: high risk.
        # 
        # - 2: medium risk.
        # 
        # - 3: low risk.
        self.risk_level = risk_level
        # The tags of the resource. This parameter is deprecated. The value that you specify for this parameter does not take effect.
        # 
        # You can add up to 20 tags.
        self.tag_shrink = tag_shrink
        # The logical relationship for the tags that you specify for the `TagsScope` parameter. For example, if you set the `TagsScope` parameter to `"TagsScope.1.TagKey":"a","TagsScope.1.TagValue":"a","TagsScope.2.TagKey":"b","TagsScope.2.TagValue":"b"` and set this parameter to `AND`, the rule applies only to resources that have both the `a:a` and `b:b` tags. If you do not specify this parameter, the `OR` logic is used by default.
        # 
        # This parameter also applies to the deprecated `TagKeyScope` parameter, but this is not recommended. For example, if you set the `TagKeyScope` parameter to `ECS,OSS` and set this parameter to `AND`, the rule applies only to resources that have both the `ECS` and `OSS` tags.
        # 
        # Valid values:
        # 
        # - AND
        # 
        # - OR
        self.tag_key_logic_scope = tag_key_logic_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule is effective only for resources that have the specified tag.
        # 
        # > This parameter applies only to managed rules. The `TagKeyScope` and `TagValueScope` parameters must be specified at the same time.
        self.tag_key_scope = tag_key_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule is effective only for resources that have the specified tag.
        # 
        # > This parameter applies only to managed rules. The `TagKeyScope` and `TagValueScope` parameters must be specified at the same time.
        self.tag_value_scope = tag_value_scope
        # The tags that are used to filter resources.
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

        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content

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

        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')

        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')

        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')

        self.exclude_tags_scope = []
        if m.get('ExcludeTagsScope') is not None:
            for k1 in m.get('ExcludeTagsScope'):
                temp_model = main_models.UpdateConfigRuleShrinkRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')

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
                temp_model = main_models.UpdateConfigRuleShrinkRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class UpdateConfigRuleShrinkRequestTagsScope(DaraModel):
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

class UpdateConfigRuleShrinkRequestExcludeTagsScope(DaraModel):
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

