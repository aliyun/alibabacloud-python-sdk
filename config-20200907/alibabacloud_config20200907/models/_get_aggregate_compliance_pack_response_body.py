# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetAggregateCompliancePackResponseBody(DaraModel):
    def __init__(
        self,
        compliance_pack: main_models.GetAggregateCompliancePackResponseBodyCompliancePack = None,
        request_id: str = None,
    ):
        # The details of the compliance pack.
        self.compliance_pack = compliance_pack
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.compliance_pack:
            self.compliance_pack.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compliance_pack is not None:
            result['CompliancePack'] = self.compliance_pack.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CompliancePack') is not None:
            temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m.get('CompliancePack'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetAggregateCompliancePackResponseBodyCompliancePack(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        aggregator_id: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[main_models.GetAggregateCompliancePackResponseBodyCompliancePackConfigRules] = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        scope: main_models.GetAggregateCompliancePackResponseBodyCompliancePackScope = None,
        status: str = None,
        tags: List[main_models.GetAggregateCompliancePackResponseBodyCompliancePackTags] = None,
        template_content: str = None,
    ):
        # The ID of the management account to which the compliance pack belongs.
        self.account_id = account_id
        # The ID of the account group.
        self.aggregator_id = aggregator_id
        # The ID of the compliance pack.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance pack.
        self.compliance_pack_name = compliance_pack_name
        # The ID of the compliance pack template.
        self.compliance_pack_template_id = compliance_pack_template_id
        # The list of rules in the compliance pack.
        self.config_rules = config_rules
        # The timestamp when the compliance pack was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The description of the compliance pack.
        self.description = description
        # The risk level of the compliance pack. Valid values:
        # 
        # - 1: high
        # 
        # - 2: medium
        # 
        # - 3: low
        self.risk_level = risk_level
        # The evaluation scope of the compliance pack.
        self.scope = scope
        # The status of the compliance pack. Valid values:
        # 
        # - ACTIVE: The compliance pack is active.
        # 
        # - CREATING: The compliance pack is being created.
        self.status = status
        # The tags of the resource.
        self.tags = tags
        # The information about the compliance pack template. The list of rules in the template does not include user-defined function rules. You can use the template to quickly create the same compliance pack for other accounts or account groups.
        self.template_content = template_content

    def validate(self):
        if self.config_rules:
            for v1 in self.config_rules:
                 if v1:
                    v1.validate()
        if self.scope:
            self.scope.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id

        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k1 in self.config_rules:
                result['ConfigRules'].append(k1.to_map() if k1 else None)

        if self.create_timestamp is not None:
            result['CreateTimestamp'] = self.create_timestamp

        if self.description is not None:
            result['Description'] = self.description

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.scope is not None:
            result['Scope'] = self.scope.to_map()

        if self.status is not None:
            result['Status'] = self.status

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k1 in m.get('ConfigRules'):
                temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k1))

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Scope') is not None:
            temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        return self

class GetAggregateCompliancePackResponseBodyCompliancePackTags(DaraModel):
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

class GetAggregateCompliancePackResponseBodyCompliancePackScope(DaraModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.GetAggregateCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope] = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.GetAggregateCompliancePackResponseBodyCompliancePackScopeTagsScope] = None,
    ):
        # The IDs of the regions to exclude. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of the resource groups to exclude. The compliance pack does not apply to resources in these groups. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The IDs of the resources to exclude. The compliance pack does not apply to these resources. Separate multiple resource IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The excluded tag scope.
        self.exclude_tags_scope = exclude_tags_scope
        # The IDs of the regions where the compliance pack applies. Separate multiple region IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The IDs of the resource groups where the compliance pack applies. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of the resources to which the rule applies. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The tag key of the resources to which the compliance pack applies.
        self.tag_key_scope = tag_key_scope
        # The tag value of the resources to which the compliance pack applies.
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

        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope

        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope

        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope

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
        if m.get('ExcludeRegionIdsScope') is not None:
            self.exclude_region_ids_scope = m.get('ExcludeRegionIdsScope')

        if m.get('ExcludeResourceGroupIdsScope') is not None:
            self.exclude_resource_group_ids_scope = m.get('ExcludeResourceGroupIdsScope')

        if m.get('ExcludeResourceIdsScope') is not None:
            self.exclude_resource_ids_scope = m.get('ExcludeResourceIdsScope')

        self.exclude_tags_scope = []
        if m.get('ExcludeTagsScope') is not None:
            for k1 in m.get('ExcludeTagsScope'):
                temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackScopeTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class GetAggregateCompliancePackResponseBodyCompliancePackScopeTagsScope(DaraModel):
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

class GetAggregateCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope(DaraModel):
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

class GetAggregateCompliancePackResponseBodyCompliancePackConfigRules(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[main_models.GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
    ):
        # The ID of the rule.
        self.config_rule_id = config_rule_id
        # The name of the rule.
        self.config_rule_name = config_rule_name
        # The input parameters of the rule.
        self.config_rule_parameters = config_rule_parameters
        # The description of the rule.
        self.description = description
        # The identifier of the rule.
        self.managed_rule_identifier = managed_rule_identifier
        # The types of the resources that are evaluated by the rule. Separate multiple resource types with commas (,).
        self.resource_types_scope = resource_types_scope
        # The risk level of the rule. Valid values:
        # 
        # - 1: high
        # 
        # - 2: medium
        # 
        # - 3: low
        self.risk_level = risk_level

    def validate(self):
        if self.config_rule_parameters:
            for v1 in self.config_rule_parameters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config_rule_id is not None:
            result['ConfigRuleId'] = self.config_rule_id

        if self.config_rule_name is not None:
            result['ConfigRuleName'] = self.config_rule_name

        result['ConfigRuleParameters'] = []
        if self.config_rule_parameters is not None:
            for k1 in self.config_rule_parameters:
                result['ConfigRuleParameters'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.managed_rule_identifier is not None:
            result['ManagedRuleIdentifier'] = self.managed_rule_identifier

        if self.resource_types_scope is not None:
            result['ResourceTypesScope'] = self.resource_types_scope

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConfigRuleId') is not None:
            self.config_rule_id = m.get('ConfigRuleId')

        if m.get('ConfigRuleName') is not None:
            self.config_rule_name = m.get('ConfigRuleName')

        self.config_rule_parameters = []
        if m.get('ConfigRuleParameters') is not None:
            for k1 in m.get('ConfigRuleParameters'):
                temp_model = main_models.GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')

        if m.get('ResourceTypesScope') is not None:
            self.resource_types_scope = m.get('ResourceTypesScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class GetAggregateCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
        required: bool = None,
    ):
        # The name of the input parameter.
        self.parameter_name = parameter_name
        # The value of the input parameter.
        self.parameter_value = parameter_value
        # Indicates whether the input parameter is required. Valid values:
        # 
        # - true: The input parameter is required.
        # 
        # - false: The input parameter is not required.
        self.required = required

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameter_name is not None:
            result['ParameterName'] = self.parameter_name

        if self.parameter_value is not None:
            result['ParameterValue'] = self.parameter_value

        if self.required is not None:
            result['Required'] = self.required

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        return self

