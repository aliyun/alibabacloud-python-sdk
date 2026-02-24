# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetConfigRuleResponseBody(DaraModel):
    def __init__(
        self,
        config_rule: main_models.GetConfigRuleResponseBodyConfigRule = None,
        request_id: str = None,
    ):
        # The details of the rule.
        self.config_rule = config_rule
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.config_rule:
            self.config_rule.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule is not None:
            result['ConfigRule'] = self.config_rule.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRule') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRule()
            self.config_rule = temp_model.from_map(m.get('ConfigRule'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetConfigRuleResponseBodyConfigRule(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        compliance: main_models.GetConfigRuleResponseBodyConfigRuleCompliance = None,
        config_rule_arn: str = None,
        config_rule_evaluation_status: main_models.GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus = None,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_state: str = None,
        config_rule_trigger_types: str = None,
        create_by: main_models.GetConfigRuleResponseBodyConfigRuleCreateBy = None,
        create_timestamp: int = None,
        description: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.GetConfigRuleResponseBodyConfigRuleExcludeTagsScope] = None,
        extend_content: str = None,
        input_parameters: Dict[str, Any] = None,
        managed_rule: main_models.GetConfigRuleResponseBodyConfigRuleManagedRule = None,
        maximum_execution_frequency: str = None,
        modified_timestamp: int = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        resource_name_scope: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
        scope: main_models.GetConfigRuleResponseBodyConfigRuleScope = None,
        source: main_models.GetConfigRuleResponseBodyConfigRuleSource = None,
        tag_key_logic_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags: List[main_models.GetConfigRuleResponseBodyConfigRuleTags] = None,
        tags_scope: List[main_models.GetConfigRuleResponseBodyConfigRuleTagsScope] = None,
    ):
        # The ID of the Alibaba Cloud account to which the rule belongs.
        self.account_id = account_id
        # The compliance statistics of the rule.
        self.compliance = compliance
        # The Alibaba Cloud Resource Name (ARN) of the rule.
        self.config_rule_arn = config_rule_arn
        # The execution status of the rule.
        self.config_rule_evaluation_status = config_rule_evaluation_status
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The rule name.
        self.config_rule_name = config_rule_name
        # The status of the rule. Valid values:
        # 
        # - ACTIVE: The rule is enabled.
        # 
        # - DELETING: The rule is being deleted.
        # 
        # - EVALUATING: The rule is being used to evaluate resource configurations.
        # 
        # - INACTIVE: The rule is disabled.
        self.config_rule_state = config_rule_state
        # The trigger type of the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # 
        # - ScheduledNotification: The rule is triggered periodically.
        self.config_rule_trigger_types = config_rule_trigger_types
        # The information about the creator of the rule.
        self.create_by = create_by
        # The timestamp when the rule was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The description of the rule.
        self.description = description
        # The IDs of the regions where the rule does not apply. The rule does not evaluate resources in these regions. Separate multiple region IDs with a comma (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of the resource groups where the rule does not apply. The rule does not evaluate resources in these resource groups. Separate multiple resource group IDs with a comma (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of the resources that are not evaluated by the rule. Separate multiple resource IDs with a comma (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The tags of the resources that are not evaluated by the rule.
        self.exclude_tags_scope = exclude_tags_scope
        # The extended content. This parameter is used only to specify the trigger time for a rule that is triggered on a 24-hour cycle.
        self.extend_content = extend_content
        # The input parameters of the rule.
        self.input_parameters = input_parameters
        # The details of the managed rule.
        self.managed_rule = managed_rule
        # The execution frequency of the rule. Valid values:
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
        # > This parameter is returned only when the rule is triggered periodically.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The timestamp when the rule was last updated. Unit: milliseconds.
        self.modified_timestamp = modified_timestamp
        # The IDs of the regions where the rule applies. The rule evaluates only resources in these regions.
        self.region_ids_scope = region_ids_scope
        # The IDs of the resource groups where the rule applies. The rule evaluates only resources in these resource groups.
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of the resources that are evaluated by the rule. Separate multiple resource IDs with a comma (,).
        self.resource_ids_scope = resource_ids_scope
        # The rule evaluates only resources that have the specified names.
        self.resource_name_scope = resource_name_scope
        # The types of the resources that are evaluated by the rule.
        self.resource_types_scope = resource_types_scope
        # The risk level of the rule. Valid values:
        # 
        # - 1: high
        # 
        # - 2: medium
        # 
        # - 3: low
        self.risk_level = risk_level
        # The effective scope of the rule.
        self.scope = scope
        # The source of the rule.
        self.source = source
        # This parameter is not returned for rules that are created using the `TagsScope` parameter.
        # 
        # This parameter is returned for rules that are created using the deprecated TagKeyScope parameter. We do not recommend that you use the `TagKeyScope` parameter. For example, if `TagKeyScope` is set to `ECS,OSS` and this parameter is set to `AND`, the rule applies only to resources that have both the `ECS` and `OSS` tags.
        # 
        # Valid values:
        # 
        # - AND
        # 
        # - OR
        self.tag_key_logic_scope = tag_key_logic_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources with the specified tag.
        # 
        # > The `TagKeyScope` and `TagValueScope` parameters are returned at the same time.
        self.tag_key_scope = tag_key_scope
        # This parameter is deprecated. Use the `TagsScope` parameter instead.
        # 
        # The rule applies only to resources with the specified tag.
        # 
        # > The `TagKeyScope` and `TagValueScope` parameters are returned at the same time.
        self.tag_value_scope = tag_value_scope
        # The tags of the resource.
        self.tags = tags
        # The tag-based scope.
        self.tags_scope = tags_scope

    def validate(self):
        if self.compliance:
            self.compliance.validate()
        if self.config_rule_evaluation_status:
            self.config_rule_evaluation_status.validate()
        if self.create_by:
            self.create_by.validate()
        if self.exclude_tags_scope:
            for v1 in self.exclude_tags_scope:
                 if v1:
                    v1.validate()
        if self.managed_rule:
            self.managed_rule.validate()
        if self.scope:
            self.scope.validate()
        if self.source:
            self.source.validate()
        if self.tags:
            for v1 in self.tags:
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
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.compliance is not None:
            result['Compliance'] = self.compliance.to_map()

        if self.config_rule_arn is not None:
            result['ConfigRuleArn'] = self.config_rule_arn

        if self.config_rule_evaluation_status is not None:
            result['ConfigRuleEvaluationStatus'] = self.config_rule_evaluation_status.to_map()

        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        if self.config_rule_state is not None:
            result['ConfigRuleState'] = self.config_rule_state

        if self.config_rule_trigger_types is not None:
            result['ConfigRuleTriggerTypes'] = self.config_rule_trigger_types

        if self.create_by is not None:
            result['CreateBy'] = self.create_by.to_map()

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

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

        if self.input_parameters is not None:
            result['InputParameters'] = self.input_parameters

        if self.managed_rule is not None:
            result['ManagedRule'] = self.managed_rule.to_map()

        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency

        if self.modified_timestamp is not None:
            result['ModifiedTimestamp'] = self.modified_timestamp

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

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        if self.source is not None:
            result['Source'] = self.source.to_map()

        if self.tag_key_logic_scope is not None:
            result['TagKeyLogicScope'] = self.tag_key_logic_scope

        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope

        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['TagsScope'] = []
        if self.tags_scope is not None:
            for k1 in self.tags_scope:
                result['TagsScope'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('Compliance') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleCompliance()
            self.compliance = temp_model.from_map(m.get('Compliance'))

        if m.get('ConfigRuleArn') is not None:
            self.config_rule_arn = m.get('ConfigRuleArn')

        if m.get('ConfigRuleEvaluationStatus') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus()
            self.config_rule_evaluation_status = temp_model.from_map(m.get('ConfigRuleEvaluationStatus'))

        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        if m.get('ConfigRuleState') is not None:
            self.config_rule_state = m.get('ConfigRuleState')

        if m.get('ConfigRuleTriggerTypes') is not None:
            self.config_rule_trigger_types = m.get('ConfigRuleTriggerTypes')

        if m.get('CreateBy') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleCreateBy()
            self.create_by = temp_model.from_map(m.get('CreateBy'))

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

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
                temp_model = main_models.GetConfigRuleResponseBodyConfigRuleExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('ExtendContent') is not None:
            self.extend_content = m.get('ExtendContent')

        if m.get('InputParameters') is not None:
            self.input_parameters = m.get('InputParameters')

        if m.get('ManagedRule') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleManagedRule()
            self.managed_rule = temp_model.from_map(m.get('ManagedRule'))

        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')

        if m.get('ModifiedTimestamp') is not None:
            self.modified_timestamp = m.get('ModifiedTimestamp')

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

        if m.get('Scope') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('Source') is not None:
            temp_model = main_models.GetConfigRuleResponseBodyConfigRuleSource()
            self.source = temp_model.from_map(m.get('Source'))

        if m.get('TagKeyLogicScope') is not None:
            self.tag_key_logic_scope = m.get('TagKeyLogicScope')

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetConfigRuleResponseBodyConfigRuleTags()
                self.tags.append(temp_model.from_map(k1))

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.GetConfigRuleResponseBodyConfigRuleTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class GetConfigRuleResponseBodyConfigRuleTagsScope(DaraModel):
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

class GetConfigRuleResponseBodyConfigRuleTags(DaraModel):
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

class GetConfigRuleResponseBodyConfigRuleSource(DaraModel):
    def __init__(
        self,
        identifier: str = None,
        owner: str = None,
        source_details: List[main_models.GetConfigRuleResponseBodyConfigRuleSourceSourceDetails] = None,
    ):
        # The identifier of the rule.
        # 
        # - If the rule is a managed rule, the value of this parameter is the identifier of the managed rule.
        # 
        # - If the rule is a custom rule, the value of this parameter is the ARN of the function.
        self.identifier = identifier
        # The owner of the rule. Valid values:
        # 
        # - CUSTOM_FC: a custom rule.
        # 
        # - ALIYUN: a managed rule.
        self.owner = owner
        # The source details.
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for v1 in self.source_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.owner is not None:
            result['Owner'] = self.owner

        result['SourceDetails'] = []
        if self.source_details is not None:
            for k1 in self.source_details:
                result['SourceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k1 in m.get('SourceDetails'):
                temp_model = main_models.GetConfigRuleResponseBodyConfigRuleSourceSourceDetails()
                self.source_details.append(temp_model.from_map(k1))

        return self

class GetConfigRuleResponseBodyConfigRuleSourceSourceDetails(DaraModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        # The event source.
        # 
        # > Only Cloud Config events are supported. The value is aliyun.config.
        self.event_source = event_source
        # The execution frequency of the rule. Valid values:
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
        # > This parameter is returned only when the rule is triggered periodically.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The trigger type of the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # 
        # - ScheduledNotification: The rule is triggered periodically.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        return self

class GetConfigRuleResponseBodyConfigRuleScope(DaraModel):
    def __init__(
        self,
        compliance_resource_types: List[str] = None,
    ):
        # The list of resource types that are evaluated by the rule. You can also view this information in the ResourceTypesScope field.
        self.compliance_resource_types = compliance_resource_types

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_resource_types is not None:
            result['ComplianceResourceTypes'] = self.compliance_resource_types

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceResourceTypes') is not None:
            self.compliance_resource_types = m.get('ComplianceResourceTypes')

        return self

class GetConfigRuleResponseBodyConfigRuleManagedRule(DaraModel):
    def __init__(
        self,
        compulsory_input_parameter_details: Dict[str, Any] = None,
        description: str = None,
        identifier: str = None,
        labels: List[str] = None,
        managed_rule_name: str = None,
        optional_input_parameter_details: Dict[str, Any] = None,
        source_details: List[main_models.GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails] = None,
    ):
        # The details of the required input parameters of the managed rule.
        self.compulsory_input_parameter_details = compulsory_input_parameter_details
        # The description of the managed rule.
        self.description = description
        # The identifier of the managed rule.
        self.identifier = identifier
        # The list of rule labels.
        self.labels = labels
        # The name of the managed rule.
        self.managed_rule_name = managed_rule_name
        # The details of the optional input parameters of the managed rule.
        self.optional_input_parameter_details = optional_input_parameter_details
        # The source details of the managed rule.
        self.source_details = source_details

    def validate(self):
        if self.source_details:
            for v1 in self.source_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compulsory_input_parameter_details is not None:
            result['CompulsoryInputParameterDetails'] = self.compulsory_input_parameter_details

        if self.description is not None:
            result['Description'] = self.description

        if self.identifier is not None:
            result['Identifier'] = self.identifier

        if self.labels is not None:
            result['Labels'] = self.labels

        if self.managed_rule_name is not None:
            result['ManagedRuleName'] = self.managed_rule_name

        if self.optional_input_parameter_details is not None:
            result['OptionalInputParameterDetails'] = self.optional_input_parameter_details

        result['SourceDetails'] = []
        if self.source_details is not None:
            for k1 in self.source_details:
                result['SourceDetails'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompulsoryInputParameterDetails') is not None:
            self.compulsory_input_parameter_details = m.get('CompulsoryInputParameterDetails')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Identifier') is not None:
            self.identifier = m.get('Identifier')

        if m.get('Labels') is not None:
            self.labels = m.get('Labels')

        if m.get('ManagedRuleName') is not None:
            self.managed_rule_name = m.get('ManagedRuleName')

        if m.get('OptionalInputParameterDetails') is not None:
            self.optional_input_parameter_details = m.get('OptionalInputParameterDetails')

        self.source_details = []
        if m.get('SourceDetails') is not None:
            for k1 in m.get('SourceDetails'):
                temp_model = main_models.GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails()
                self.source_details.append(temp_model.from_map(k1))

        return self

class GetConfigRuleResponseBodyConfigRuleManagedRuleSourceDetails(DaraModel):
    def __init__(
        self,
        event_source: str = None,
        maximum_execution_frequency: str = None,
        message_type: str = None,
    ):
        # The event source.
        # 
        # > Only Cloud Config events are supported. The value is aliyun.config.
        self.event_source = event_source
        # The execution frequency of the rule. Valid values:
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
        # > This parameter is returned only when the rule is triggered periodically.
        self.maximum_execution_frequency = maximum_execution_frequency
        # The trigger type of the rule. Valid values:
        # 
        # - ConfigurationItemChangeNotification: The rule is triggered by configuration changes.
        # 
        # - ScheduledNotification: The rule is triggered periodically.
        self.message_type = message_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_source is not None:
            result['EventSource'] = self.event_source

        if self.maximum_execution_frequency is not None:
            result['MaximumExecutionFrequency'] = self.maximum_execution_frequency

        if self.message_type is not None:
            result['MessageType'] = self.message_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventSource') is not None:
            self.event_source = m.get('EventSource')

        if m.get('MaximumExecutionFrequency') is not None:
            self.maximum_execution_frequency = m.get('MaximumExecutionFrequency')

        if m.get('MessageType') is not None:
            self.message_type = m.get('MessageType')

        return self

class GetConfigRuleResponseBodyConfigRuleExcludeTagsScope(DaraModel):
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

class GetConfigRuleResponseBodyConfigRuleCreateBy(DaraModel):
    def __init__(
        self,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        creator_id: str = None,
        creator_name: str = None,
    ):
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        self.compliance_pack_name = compliance_pack_name
        # The ID of the Alibaba Cloud account that was used to create the rule.
        self.creator_id = creator_id
        # The name of the creator.
        self.creator_name = creator_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        return self

class GetConfigRuleResponseBodyConfigRuleConfigRuleEvaluationStatus(DaraModel):
    def __init__(
        self,
        first_activated_timestamp: int = None,
        first_evaluation_started: bool = None,
        last_error_code: str = None,
        last_error_message: str = None,
        last_failed_evaluation_timestamp: int = None,
        last_failed_invocation_timestamp: int = None,
        last_successful_evaluation_timestamp: int = None,
        last_successful_invocation_timestamp: int = None,
    ):
        # The timestamp when the rule was first activated. Unit: milliseconds.
        self.first_activated_timestamp = first_activated_timestamp
        # Indicates whether the rule has been evaluated. Valid values:
        # 
        # - true: The rule has been evaluated.
        # 
        # - false: The rule has not been evaluated.
        self.first_evaluation_started = first_evaluation_started
        # The error code returned for the last failed execution of the rule.
        self.last_error_code = last_error_code
        # The error message returned for the last failed execution of the rule.
        self.last_error_message = last_error_message
        # The timestamp when the last failed evaluation of the rule ended. Unit: milliseconds.
        self.last_failed_evaluation_timestamp = last_failed_evaluation_timestamp
        # The timestamp when the last failed invocation of the rule started. Unit: milliseconds.
        self.last_failed_invocation_timestamp = last_failed_invocation_timestamp
        # The timestamp when the last successful evaluation of the rule ended. Unit: milliseconds.
        self.last_successful_evaluation_timestamp = last_successful_evaluation_timestamp
        # The timestamp when the last successful invocation of the rule started. Unit: milliseconds.
        self.last_successful_invocation_timestamp = last_successful_invocation_timestamp

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_activated_timestamp is not None:
            result['FirstActivatedTimestamp'] = self.first_activated_timestamp

        if self.first_evaluation_started is not None:
            result['FirstEvaluationStarted'] = self.first_evaluation_started

        if self.last_error_code is not None:
            result['LastErrorCode'] = self.last_error_code

        if self.last_error_message is not None:
            result['LastErrorMessage'] = self.last_error_message

        if self.last_failed_evaluation_timestamp is not None:
            result['LastFailedEvaluationTimestamp'] = self.last_failed_evaluation_timestamp

        if self.last_failed_invocation_timestamp is not None:
            result['LastFailedInvocationTimestamp'] = self.last_failed_invocation_timestamp

        if self.last_successful_evaluation_timestamp is not None:
            result['LastSuccessfulEvaluationTimestamp'] = self.last_successful_evaluation_timestamp

        if self.last_successful_invocation_timestamp is not None:
            result['LastSuccessfulInvocationTimestamp'] = self.last_successful_invocation_timestamp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstActivatedTimestamp') is not None:
            self.first_activated_timestamp = m.get('FirstActivatedTimestamp')

        if m.get('FirstEvaluationStarted') is not None:
            self.first_evaluation_started = m.get('FirstEvaluationStarted')

        if m.get('LastErrorCode') is not None:
            self.last_error_code = m.get('LastErrorCode')

        if m.get('LastErrorMessage') is not None:
            self.last_error_message = m.get('LastErrorMessage')

        if m.get('LastFailedEvaluationTimestamp') is not None:
            self.last_failed_evaluation_timestamp = m.get('LastFailedEvaluationTimestamp')

        if m.get('LastFailedInvocationTimestamp') is not None:
            self.last_failed_invocation_timestamp = m.get('LastFailedInvocationTimestamp')

        if m.get('LastSuccessfulEvaluationTimestamp') is not None:
            self.last_successful_evaluation_timestamp = m.get('LastSuccessfulEvaluationTimestamp')

        if m.get('LastSuccessfulInvocationTimestamp') is not None:
            self.last_successful_invocation_timestamp = m.get('LastSuccessfulInvocationTimestamp')

        return self

class GetConfigRuleResponseBodyConfigRuleCompliance(DaraModel):
    def __init__(
        self,
        compliance_type: str = None,
        count: int = None,
    ):
        # The compliance evaluation result. Valid values:
        # 
        # - COMPLIANT: The resource is compliant.
        # 
        # - NON_COMPLIANT: The resource is non-compliant.
        # 
        # - NOT_APPLICABLE: The rule does not apply to the resource.
        # 
        # - INSUFFICIENT_DATA: No data is available.
        self.compliance_type = compliance_type
        # The number of resources that are evaluated based on the compliance result.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_type is not None:
            result['ComplianceType'] = self.compliance_type

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComplianceType') is not None:
            self.compliance_type = m.get('ComplianceType')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

