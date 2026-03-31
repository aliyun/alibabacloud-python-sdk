# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class GetCompliancePackResponseBody(DaraModel):
    def __init__(
        self,
        compliance_pack: main_models.GetCompliancePackResponseBodyCompliancePack = None,
        request_id: str = None,
    ):
        # The details of the compliance package.
        self.compliance_pack = compliance_pack
        # The request ID.
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
            temp_model = main_models.GetCompliancePackResponseBodyCompliancePack()
            self.compliance_pack = temp_model.from_map(m.get('CompliancePack'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetCompliancePackResponseBodyCompliancePack(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules: List[main_models.GetCompliancePackResponseBodyCompliancePackConfigRules] = None,
        create_timestamp: int = None,
        description: str = None,
        risk_level: int = None,
        scope: main_models.GetCompliancePackResponseBodyCompliancePackScope = None,
        status: str = None,
        tags: List[main_models.GetCompliancePackResponseBodyCompliancePackTags] = None,
        template_content: str = None,
    ):
        # The ID of the Alibaba Cloud account to which the compliance package belongs.
        self.account_id = account_id
        # The ID of the compliance package.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        self.compliance_pack_name = compliance_pack_name
        # The ID of the compliance package template.
        self.compliance_pack_template_id = compliance_pack_template_id
        # The rules in the compliance package.
        self.config_rules = config_rules
        # The timestamp when the compliance package was created. Unit: milliseconds.
        self.create_timestamp = create_timestamp
        # The description of the compliance package.
        self.description = description
        # The risk level of the resources that are not compliant with the rules in the compliance package. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
        self.risk_level = risk_level
        # The resource group for which the compliance package took effect.
        self.scope = scope
        # The status of the compliance package. Valid values:
        # 
        # *   ACTIVE: The compliance package is normal.
        # *   CREATING: The compliance package is being created.
        self.status = status
        # The list of tags.
        self.tags = tags
        # The information about the current compliance package template. The rules in the template do not contain custom function rules. You can quickly create the same compliance package for other accounts or account groups based on the template information.
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

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k1 in m.get('ConfigRules'):
                temp_model = main_models.GetCompliancePackResponseBodyCompliancePackConfigRules()
                self.config_rules.append(temp_model.from_map(k1))

        if m.get('CreateTimestamp') is not None:
            self.create_timestamp = m.get('CreateTimestamp')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Scope') is not None:
            temp_model = main_models.GetCompliancePackResponseBodyCompliancePackScope()
            self.scope = temp_model.from_map(m.get('Scope'))

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetCompliancePackResponseBodyCompliancePackTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        return self

class GetCompliancePackResponseBodyCompliancePackTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag keys of the resource.
        self.tag_key = tag_key
        # The tag values of the resource.
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

class GetCompliancePackResponseBodyCompliancePackScope(DaraModel):
    def __init__(
        self,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.GetCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope] = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.GetCompliancePackResponseBodyCompliancePackScopeTagsScope] = None,
    ):
        # The IDs of regions that are excluded. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The IDs of the resource groups whose resources you do not want to evaluate by using the compliance package. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The ID of the resource that you do not want to evaluate by using the compliance package.
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The scope of the tag that is excluded.
        # 
        # This parameter is required.
        self.exclude_tags_scope = exclude_tags_scope
        # The ID of the region whose resources you want to evaluate by using the compliance package.
        self.region_ids_scope = region_ids_scope
        # The ID of the resource group whose resources you want to evaluate by using the compliance package.
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of the resources to which the rule applies. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The tag key of the resource that you want to evaluate by using the compliance package.
        self.tag_key_scope = tag_key_scope
        # The tag value of the resource that you want to evaluate by using the compliance package.
        self.tag_value_scope = tag_value_scope
        # The tag scope.
        # 
        # This parameter is required.
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
                temp_model = main_models.GetCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope()
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
                temp_model = main_models.GetCompliancePackResponseBodyCompliancePackScopeTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class GetCompliancePackResponseBodyCompliancePackScopeTagsScope(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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

class GetCompliancePackResponseBodyCompliancePackScopeExcludeTagsScope(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the tag.
        self.tag_key = tag_key
        # The value of the tag.
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

class GetCompliancePackResponseBodyCompliancePackConfigRules(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[main_models.GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        resource_types_scope: str = None,
        risk_level: int = None,
    ):
        # The rule ID.
        self.config_rule_id = config_rule_id
        # The rule name.
        self.config_rule_name = config_rule_name
        # The input parameters of the rule.
        self.config_rule_parameters = config_rule_parameters
        # The rule description.
        self.description = description
        # The identifier of the managed rule.
        self.managed_rule_identifier = managed_rule_identifier
        # The type of the resource evaluated based on the rule. Separate multiple resource types with commas (,).
        self.resource_types_scope = resource_types_scope
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high
        # *   2: medium
        # *   3: low
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
                temp_model = main_models.GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters()
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

class GetCompliancePackResponseBodyCompliancePackConfigRulesConfigRuleParameters(DaraModel):
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
        # Indicates whether the input parameters are required. Valid values:
        # 
        # *   true
        # *   false
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

