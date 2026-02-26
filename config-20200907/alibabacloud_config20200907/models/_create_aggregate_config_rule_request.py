# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class CreateAggregateConfigRuleRequest(DaraModel):
    def __init__(
        self,
        account_ids_scope: str = None,
        aggregator_id: str = None,
        client_token: str = None,
        conditions: str = None,
        config_rule_name: str = None,
        config_rule_trigger_types: str = None,
        description: str = None,
        exclude_account_ids_scope: str = None,
        exclude_folder_ids_scope: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.CreateAggregateConfigRuleRequestExcludeTagsScope] = None,
        extend_content: str = None,
        folder_ids_scope: str = None,
        input_parameters: Dict[str, Any] = None,
        maximum_execution_frequency: str = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_name_scope: str = None,
        resource_types_scope: List[str] = None,
        risk_level: int = None,
        source_identifier: str = None,
        source_owner: str = None,
        tag: List[main_models.CreateAggregateConfigRuleRequestTag] = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.CreateAggregateConfigRuleRequestTagsScope] = None,
    ):
        # The rule applies only to resources of the specified member accounts. Separate multiple member account IDs with commas (,).
        # 
        # > This parameter applies only to rule templates.
        self.account_ids_scope = account_ids_scope
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [the referenced document](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # A client token that ensures the request is idempotent. Generate a unique value from your client for each request. The `ClientToken` parameter must contain only ASCII characters and be no more than 64 characters long.
        self.client_token = client_token
        # The conditions for a custom condition rule, in JSON format.
        self.conditions = conditions
        # The name of the rule.
        # 
        # This parameter is required.
        self.config_rule_name = config_rule_name
        # The trigger type for the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: The rule triggers when a resource configuration changes.
        # 
        # - ScheduledNotification: The rule triggers on a schedule.
        # 
        # This parameter is required.
        self.config_rule_trigger_types = config_rule_trigger_types
        # A description of the rule.
        self.description = description
        # The rule does not apply to resources of the specified member accounts. Resources in these accounts are not evaluated. Separate multiple member account IDs with commas (,).
        # 
        # > This parameter applies only to rule templates.
        self.exclude_account_ids_scope = exclude_account_ids_scope
        # The rule does not apply to resources of member accounts in the specified folders. Resources in these folders are not evaluated. Separate multiple folder IDs with commas (,).
        # 
        # > - This parameter applies only to global account group rules.
        # >
        # > - This parameter applies only to rule templates.
        self.exclude_folder_ids_scope = exclude_folder_ids_scope
        # The rule does not apply to resources in the specified regions. Resources in these regions are not evaluated. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The rule does not apply to resources in the specified resource groups. Resources in these groups are not evaluated. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The rule does not apply to the specified resources. These resources are not evaluated. Separate multiple resource IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The scope of tags to exclude.
        self.exclude_tags_scope = exclude_tags_scope
        # Extended content. This parameter currently supports only setting the trigger time for rules that run on a 24-hour cycle.
        self.extend_content = extend_content
        # The rule applies only to resources of member accounts in the specified folders. Separate multiple folder IDs with commas (,).
        # 
        # > - This parameter applies only to global account group rules.
        # >
        # > - This parameter applies only to rule templates.
        self.folder_ids_scope = folder_ids_scope
        # The input parameters for the rule.
        self.input_parameters = input_parameters
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
        # - TwentyFour_Hours (default): 24 hours.
        # 
        # > Set this parameter if you set `ConfigRuleTriggerTypes` to `ScheduledNotification`.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The rule applies only to resources in the specified regions. Separate multiple region IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The rule applies only to resources in the specified resource groups. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The rule applies only to the specified resources. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The rule applies only to resources with the specified names.
        self.resource_name_scope = resource_name_scope
        # The resource types to evaluate. Separate multiple types with commas (,).
        # 
        # This parameter is required.
        self.resource_types_scope = resource_types_scope
        # The risk level of the rule. Valid values:
        # 
        # - 1: high
        # 
        # - 2: medium
        # 
        # - 3: low
        # 
        # This parameter is required.
        self.risk_level = risk_level
        # The identifier of the rule.
        # 
        # - If `SourceOwner` is `ALIYUN`, enter the identifier of the rule template, such as `required-tags`.
        # 
        #   > For more information about how to query rule template identifiers, see [the referenced document](https://help.aliyun.com/document_detail/127404.html).
        # 
        # - If `SourceOwner` is `CUSTOM_CONFIGURATION`, enter `acs-config-configuration`.
        # 
        # - If `SourceOwner` is `CUSTOM_FC`, enter the Alibaba Cloud Resource Name (ARN) of the Function Compute function.
        # 
        #   The ARN format is `acs:fc:{region}:{accountId}:services/{serviceName}.LATEST/functions/{functionName}`. For example, `acs:fc:cn-hangzhou:120886317861****:services/service-test.LATEST/functions/config-test`.
        # 
        #   > For more information about how to obtain a function ARN, see [the referenced document](https://help.aliyun.com/document_detail/415752.html).
        # 
        # This parameter is required.
        self.source_identifier = source_identifier
        # The type of rule. Valid values:
        # 
        # - ALIYUN: rule template
        # 
        # - CUSTOM_FC: custom Function Compute rule
        # 
        # - CUSTOM_CONFIGURATION: custom condition rule
        # 
        # This parameter is required.
        self.source_owner = source_owner
        # The tag of the rule.
        self.tag = tag
        # The logical relationship between multiple tags in the `TagsScope` parameter. For example, if you set `TagsScope` to `"TagsScope.1.TagKey":"a","TagsScope.1.TagValue":"a","TagsScope.2.TagKey":"b","TagsScope.2.TagValue":"b"` and set this parameter to `AND`, the rule applies only to resources that have both the `a:a` and `b:b` tags. The default value is `OR`.
        # 
        # You can also use this parameter with the deprecated `TagKeyScope` parameter, but this is not recommended. For example, if you set `TagKeyScope` to `ECS,OSS` and set this parameter to `AND`, the rule applies only to resources that have both the `ECS` and `OSS` tags.
        # 
        # Valid values:
        # 
        # - AND
        # 
        # - OR
        self.tag_key_logic_scope = tag_key_logic_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources that have the specified tag keys. Separate multiple tag keys with commas (,).
        # 
        # > This parameter applies only to rule templates. Set both `TagKeyScope` and `TagValueScope` together.
        self.tag_key_scope = tag_key_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources that have the specified tag values.
        # 
        # > This parameter applies only to rule templates. Set both `TagKeyScope` and `TagValueScope` together.
        self.tag_value_scope = tag_value_scope
        # The scope of tags to include.
        self.tags_scope = tags_scope

    def validate(self):
        if self.exclude_tags_scope:
            for v1 in self.exclude_tags_scope:
                 if v1:
                    v1.validate()
        if self.tag:
            for v1 in self.tag:
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

        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters

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

        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.source_identifier is not None:
            result['SourceIdentifier'] = self.source_identifier

        if self.source_owner is not None:
            result['SourceOwner'] = self.source_owner

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.CreateAggregateConfigRuleRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')

        if m.get('FolderIdsScope') is not None:
            self.folder_ids_scope = m.get('FolderIdsScope')

        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')

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
            self.resource_types_scope = m.get('ResourceTypesScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SourceIdentifier') is not None:
            self.source_identifier = m.get('SourceIdentifier')

        if m.get('SourceOwner') is not None:
            self.source_owner = m.get('SourceOwner')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateAggregateConfigRuleRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.CreateAggregateConfigRuleRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class CreateAggregateConfigRuleRequestTagsScope(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource.
        self.tag_key = tag_key
        # The tag value of the resource.
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

class CreateAggregateConfigRuleRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # You can add up to 20 tag keys.
        self.key = key
        # The value of the tag.
        # 
        # You can add up to 20 tag values.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateAggregateConfigRuleRequestExcludeTagsScope(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key of the resource to exclude.
        self.tag_key = tag_key
        # The tag value of the resource to exclude.
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

