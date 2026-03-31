# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateAggregateCompliancePackRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules: List[main_models.UpdateAggregateCompliancePackRequestConfigRules] = None,
        description: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.UpdateAggregateCompliancePackRequestExcludeTagsScope] = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        risk_level: int = None,
        tag: List[main_models.UpdateAggregateCompliancePackRequestTag] = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.UpdateAggregateCompliancePackRequestTagsScope] = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # The client token that you want to use to ensure the idempotency of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.``
        self.client_token = client_token
        # The ID of the compliance package.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListAggregateCompliancePacks](https://help.aliyun.com/document_detail/262059.html).
        # 
        # This parameter is required.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        # 
        # For more information about how to obtain the name of a compliance package, see [ListAggregateCompliancePacks](https://help.aliyun.com/document_detail/262059.html).
        self.compliance_pack_name = compliance_pack_name
        # The rules in the compliance package.
        # 
        # If you leave this parameter empty, the rules in the compliance package remain unchanged. If you set this parameter, Cloud Config replaces the existing rules in the compliance package with the specified rules.
        self.config_rules = config_rules
        # The description of the compliance package.
        self.description = description
        # The IDs of the regions to which the rule not applies. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # ExcludeResourceGroupIdsScope. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The ID of the resource that you do not want to evaluate by using the compliance package. Separate multiple resource IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # ExcludeTagsScope
        self.exclude_tags_scope = exclude_tags_scope
        # The ID of the region whose resources you want to evaluate by using the compliance package. Separate multiple region IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The ID of the resource group whose resources you want to evaluate by using the compliance package. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The IDs of the resources included from the compliance evaluations performed by the rule. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The risk level of the resources that are not compliant with the rules in the compliance package. Valid values:
        # 
        # *   1: high risk level
        # *   2: medium risk level
        # *   3: low risk level
        self.risk_level = risk_level
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag = tag
        # The tag key of the resource that you want to evaluate by using the compliance package.
        self.tag_key_scope = tag_key_scope
        # The tag value of the resource that you want to evaluate by using the compliance package.
        # 
        # >  You must configure the TagValueScope parameter together with the TagKeyScope parameter.
        self.tag_value_scope = tag_value_scope
        # TagsScope
        self.tags_scope = tags_scope

    def validate(self):
        if self.config_rules:
            for v1 in self.config_rules:
                 if v1:
                    v1.validate()
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
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        result['ConfigRules'] = []
        if self.config_rules is not None:
            for k1 in self.config_rules:
                result['ConfigRules'].append(k1.to_map() if k1 else None)

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

        if self.region_ids_scope is not None:
            result['RegionIdsScope'] = self.region_ids_scope

        if self.resource_group_ids_scope is not None:
            result['ResourceGroupIdsScope'] = self.resource_group_ids_scope

        if self.resource_ids_scope is not None:
            result['ResourceIdsScope'] = self.resource_ids_scope

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

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
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        self.config_rules = []
        if m.get('ConfigRules') is not None:
            for k1 in m.get('ConfigRules'):
                temp_model = main_models.UpdateAggregateCompliancePackRequestConfigRules()
                self.config_rules.append(temp_model.from_map(k1))

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
                temp_model = main_models.UpdateAggregateCompliancePackRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.UpdateAggregateCompliancePackRequestTag()
                self.tag.append(temp_model.from_map(k1))

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.UpdateAggregateCompliancePackRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class UpdateAggregateCompliancePackRequestTagsScope(DaraModel):
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

class UpdateAggregateCompliancePackRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys.
        # 
        # The tag key cannot be an empty string. The tag key must be 1 to 64 characters in length and cannot start with `aliyun` or `acs`:. The tag key cannot contain `http://` or `https://`.
        self.key = key
        # The tag values.
        # 
        # The tag values can be an empty string or up to 128 characters in length. The tag values cannot start with `aliyun` or `acs:` and cannot contain `http://` or `https://`.
        # 
        # Each key-value must be unique. You can specify at most 20 tag values in each call.
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

class UpdateAggregateCompliancePackRequestExcludeTagsScope(DaraModel):
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

class UpdateAggregateCompliancePackRequestConfigRules(DaraModel):
    def __init__(
        self,
        config_rule_id: str = None,
        config_rule_name: str = None,
        config_rule_parameters: List[main_models.UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters] = None,
        description: str = None,
        managed_rule_identifier: str = None,
        risk_level: int = None,
    ):
        # The rule ID. If you specify this parameter, Cloud Config adds the rule that has the specified ID to the compliance package.
        # 
        # You only need to configure the `ManagedRuleIdentifier` or `ConfigRuleId` parameter. If you configure both parameters, the value of the `ConfigRuleId` parameter takes precedence. For more information about how to obtain the ID of a rule, see [ListAggregateConfigRules](https://help.aliyun.com/document_detail/264148.html).
        self.config_rule_id = config_rule_id
        # The rule name.
        self.config_rule_name = config_rule_name
        # The details of the input parameter of the rule.
        self.config_rule_parameters = config_rule_parameters
        # The rule description.
        self.description = description
        # The identifier of the managed rule. Cloud Config automatically creates a rule based on the identifier of the managed rule and adds the rule to the current compliance package.
        # 
        # You need to only configure the `ManagedRuleIdentifier` or `ConfigRuleId` parameter. If you configure both parameters, the value of the `ConfigRuleId` parameter takes precedence. You can call the [ListCompliancePackTemplates](https://help.aliyun.com/document_detail/261176.html) operation to obtain the identifier of the managed rule.
        self.managed_rule_identifier = managed_rule_identifier
        # The risk level of the resources that do not comply with the rule. Valid values:
        # 
        # *   1: high risk level
        # *   2: medium risk level
        # *   3: low risk level
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
                temp_model = main_models.UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters()
                self.config_rule_parameters.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ManagedRuleIdentifier') is not None:
            self.managed_rule_identifier = m.get('ManagedRuleIdentifier')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        return self

class UpdateAggregateCompliancePackRequestConfigRulesConfigRuleParameters(DaraModel):
    def __init__(
        self,
        parameter_name: str = None,
        parameter_value: str = None,
    ):
        # The name of the input parameter.
        # 
        # You must specify both `ParameterName` and `ParameterValue` or neither of them. If the managed rule has an input parameter but no default value exists, you must configure this parameter. For more information about how to obtain the name of an input parameter for a managed rule, see [ListCompliancePackTemplates](https://help.aliyun.com/document_detail/261176.html).
        self.parameter_name = parameter_name
        # The value of the input parameter.
        # 
        # You must specify both `ParameterName` and `ParameterValue` or neither of them. If the managed rule has an input parameter but no default value exists, you must configure this parameter. For more information about how to obtain the value of an input parameter for a managed rule, see [ListCompliancePackTemplates](https://help.aliyun.com/document_detail/261176.html).
        self.parameter_value = parameter_value

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParameterName') is not None:
            self.parameter_name = m.get('ParameterName')

        if m.get('ParameterValue') is not None:
            self.parameter_value = m.get('ParameterValue')

        return self

