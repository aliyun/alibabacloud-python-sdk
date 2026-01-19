# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class CreateAggregateConfigRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        account_ids_scope: str = None,
        aggregator_id: str = None,
        client_token: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.CreateAggregateConfigRuleShrinkRequestExcludeTagsScope] = None,
        extend_content: str = None,
        folder_ids_scope: str = None,
        input_parameters_shrink: str = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_name_scope: str = None,
        resource_types_scope_shrink: str = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag_shrink: str = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.CreateAggregateConfigRuleShrinkRequestTagsScope] = None,
    ):
        # The IDs of the member accounts to which the rule applies, which means that the resources within the member accounts are evaluated based on the rule. Separate multiple member account IDs with commas (,).
        self.account_ids_scope = account_ids_scope
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of the account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The client token that is used to ensure the idempotence of the request. You can use the client to generate the token, but you must make sure that the token is unique among different requests. The `token` can contain only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The rule name.
        # 
        # This parameter is required.
        self.config_rule_name = config_rule_name
        # The trigger type of the rule. Valid values:
        # 
        # *   ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # *   ScheduledNotification: The rule is periodically triggered.
        # 
        # This parameter is required.
        self.config_rule_trigger_types = config_rule_trigger_types
        # The description of the rule.
        self.description = description
        # The ID of the member account to which the rule does not apply, which means that the resources within the member account are not evaluated based on the rule. Separate multiple member account IDs with commas (,).
        # 
        # > This parameter applies only to a managed rule.
        self.exclude_account_ids_scope = exclude_account_ids_scope
        # The ID of the resource directory to which the rule does not apply, which means that the resources within member accounts in the resource directory are not evaluated based on the rule. Separate multiple resource directory IDs with commas (,).
        # 
        # > 
        # 
        # *   This parameter applies only to a rule of a global account group.
        # 
        # *   This parameter applies only to a managed rule.
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        # The IDs of the regions to which the rule not applies. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # ExcludeResourceGroupIdsScope. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The ID of the resource to be excluded from the compliance evaluations performed by the rule. Separate multiple resource IDs with commas (,).
        # 
        # > This parameter applies only to a managed rule.
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The scope of the tag that is excluded.
        self.exclude_tags_scope = exclude_tags_scope
        # The extended content, which is temporarily only used to configure the trigger time with a 24-hour cycle trigger.
        self.extend_content = extend_content
        # The ID of the resource directory to which the rule applies, which means that the resources within member accounts in the resource directory are evaluated based on the rule.
        # 
        # > 
        # 
        # *   This parameter applies only to a rule of a global account group.
        # 
        # *   This parameter applies only to a managed rule.
        self.folder_ids_scope = folder_ids_scope
        # The input parameter of the rule.
        self.input_parameters_shrink = input_parameters_shrink
        # The interval at which the rule is triggered. Valid values:
        # 
        # *   One_Hour
        # *   Three_Hours
        # *   Six_Hours
        # *   Twelve_Hours
        # *   TwentyFour_Hours (default)
        # 
        # >  This parameter is required if the `ConfigRuleTriggerTypes` parameter is set to `ScheduledNotification`.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The ID of the region to which the rule applies. Separate multiple region IDs with commas (,).
        # 
        # > This parameter applies only to a managed rule.
        self.region_ids_scope = region_ids_scope
        # The ID of the resource group to which the rule applies. Separate multiple resource group IDs with commas (,).
        # 
        # > This parameter applies only to a managed rule.
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of the resources included from the compliance evaluations performed by the rule. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The names of the resource to which the rule applies.
        self.resource_name_scope = resource_name_scope
        # The type of the resource evaluated by the rule. Separate multiple resource types with commas (,).
        # 
        # This parameter is required.
        self.resource_types_scope_shrink = resource_types_scope_shrink
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        # 
        # This parameter is required.
        self.risk_level = risk_level
        # The identifier of the rule.
        # 
        # *   If you set the SourceOwner parameter to ALIYUN, set this parameter to the name of the managed rule.
        # *   If you set the SourceOwner parameter to CUSTOM_FC, set this parameter to the Alibaba Cloud Resource Name (ARN) of the relevant function in Function Compute.
        # 
        # For more information about how to query the name of a managed rule, see [Managed rules](https://help.aliyun.com/document_detail/127404.html).
        # 
        # This parameter is required.
        self.source_identifier = source_identifier
        # The type of the rule. Valid values:
        # 
        # *   ALIYUN: a managed rule.
        # *   CUSTOM_FC: a custom rule.
        # 
        # This parameter is required.
        self.source_owner = source_owner
        # The tags.
        self.tag_shrink = tag_shrink
        # The logical relationship when parameter `TagsScope` takes multiple values, for example: When the parameter `TagsScope` is `"TagsScope.1.TagKey":"a", "TagsScope.1.TagValue":"a", "TagsScope.2.TagKey":"b", "TagsScope.2.TagValue":"b"`, if this parameter is set to` AND`, it means that the rule only applies to resources bound with both tags `a:a` and `b:b`. If not specified, the default logic is `OR`.
        # 
        # It can also be used for the deprecated field `TagKeyScope` (not recommended), for example: When the parameter `TagKeyScope` has a value of `ECS`,`OSS`, if this parameter is set to `AND`, it means that the rule only applies to resources bound with both labels `ECS` and `OSS`.
        # 
        # Values:
        # 
        #  - AND: And.
        # 
        #  - OR: Or.
        self.tag_key_logic_scope = tag_key_logic_scope
        # This parameter is deprecated. We recommend that you use the `TagsScope` parameter.
        # 
        # The tag key used to filter resources. The rule applies only to the resources with the specified tag key. Separate multiple parameter values with commas (,).
        # 
        # >  This parameter applies only to a managed rule. You must configure the `TagKeyScope` and `TagValueScope` parameters at the same time.
        self.tag_key_scope = tag_key_scope
        # This parameter is deprecated. We recommend that you use the `TagsScope` parameter.
        # 
        # The tag value used to filter resources. The rule applies only to the resources that use the specified tag value.
        # 
        # >  This parameter applies only to a managed rule. You must configure the `TagKeyScope` and `TagValueScope` parameters at the same time.
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

        if self.extend_content is not None:
            result['ExtendContent'] = self.extend_content

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

        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier

        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner

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
                temp_model = main_models.CreateAggregateConfigRuleShrinkRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')

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

        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')

        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')

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
                temp_model = main_models.CreateAggregateConfigRuleShrinkRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class CreateAggregateConfigRuleShrinkRequestTagsScope(DaraModel):
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

class CreateAggregateConfigRuleShrinkRequestExcludeTagsScope(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource that you want to exclude.
        self.tag_key = tag_key
        # The tag value of the resource that you want to exclude.
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

