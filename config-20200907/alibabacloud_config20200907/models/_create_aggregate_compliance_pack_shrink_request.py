# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class CreateAggregateCompliancePackShrinkRequest(DaraModel):
    def __init__(
        self,
        aggregator_id: str = None,
        client_token: str = None,
        compliance_pack_name: str = None,
        compliance_pack_template_id: str = None,
        config_rules_shrink: str = None,
        default_enable: bool = None,
        description: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.CreateAggregateCompliancePackShrinkRequestExcludeTagsScope] = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        risk_level: int = None,
        tag_shrink: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.CreateAggregateCompliancePackShrinkRequestTagsScope] = None,
        template_content: str = None,
    ):
        # The ID of the account group.
        # 
        # For more information about how to obtain the ID of an account group, see [ListAggregators](https://help.aliyun.com/document_detail/255797.html).
        # 
        # This parameter is required.
        self.aggregator_id = aggregator_id
        # A client token. It is used to ensure the idempotence of the request. Generate a value from your client to make sure that the value is unique among different requests. `ClientToken` supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # The name of the compliance pack.
        # 
        # This parameter is required.
        self.compliance_pack_name = compliance_pack_name
        # The ID of the compliance pack template.
        # 
        # For more information about how to obtain the ID of a compliance pack template, see [ListCompliancePackTemplates](https://help.aliyun.com/document_detail/261176.html).
        self.compliance_pack_template_id = compliance_pack_template_id
        # The rules in the compliance pack.
        # 
        # > Specify either this parameter or `TemplateContent`.
        self.config_rules_shrink = config_rules_shrink
        # Indicates whether the rule is enabled for quick activation. Valid values:
        # 
        # - true: The rule is enabled when you quickly activate the compliance pack.
        # 
        # - false (default): The rule is not enabled.
        self.default_enable = default_enable
        # The description of the compliance pack.
        self.description = description
        # The compliance pack does not take effect for resources in the specified regions. The resources in these regions are not evaluated. Separate multiple region IDs with commas (,).
        self.exclude_region_ids_scope = exclude_region_ids_scope
        # The compliance pack does not take effect for resources in the specified resource groups. The resources in these resource groups are not evaluated. Separate multiple resource group IDs with commas (,).
        self.exclude_resource_group_ids_scope = exclude_resource_group_ids_scope
        # The compliance pack does not take effect for the specified resources. The resources are not evaluated. Separate multiple resource IDs with commas (,).
        self.exclude_resource_ids_scope = exclude_resource_ids_scope
        # The excluded tags.
        self.exclude_tags_scope = exclude_tags_scope
        # The compliance pack takes effect only for resources in the specified regions. Separate multiple region IDs with commas (,).
        self.region_ids_scope = region_ids_scope
        # The compliance pack takes effect only for resources in the specified resource groups. Separate multiple resource group IDs with commas (,).
        self.resource_group_ids_scope = resource_group_ids_scope
        # The compliance pack takes effect only for the specified resources. Separate multiple resource IDs with commas (,).
        self.resource_ids_scope = resource_ids_scope
        # The risk level of the compliance pack. Valid values:
        # 
        # - 1: High
        # 
        # - 2 (default): Medium
        # 
        # - 3: Low
        self.risk_level = risk_level
        # The tags of the resource.
        # 
        # You can add up to 20 tags.
        self.tag_shrink = tag_shrink
        # The compliance pack takes effect only for resources that have the specified tag key.
        self.tag_key_scope = tag_key_scope
        # The compliance pack takes effect only for resources that have the specified tag key-value pair.
        # 
        # > TagValueScope must be used with TagKeyScope.
        self.tag_value_scope = tag_value_scope
        # The effective tags.
        self.tags_scope = tags_scope
        # The template information that is used to generate the compliance pack. You can view the template content in the details of an existing compliance pack or create a template. For more information, see [Create a configurable compliance pack template](https://help.aliyun.com/document_detail/2659733.html).
        # 
        # > Specify either this parameter or `ConfigRules`.
        self.template_content = template_content

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
        if self.aggregator_id is not None:
            result['AggregatorId'] = self.aggregator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        if self.compliance_pack_template_id is not None:
            result['CompliancePackTemplateId'] = self.compliance_pack_template_id

        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink

        if self.default_enable is not None:
            result['DefaultEnable'] = self.default_enable

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

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        if self.tag_key_scope is not None:
            result['TagKeyScope'] = self.tag_key_scope

        if self.tag_value_scope is not None:
            result['TagValueScope'] = self.tag_value_scope

        result['TagsScope'] = []
        if self.tags_scope is not None:
            for k1 in self.tags_scope:
                result['TagsScope'].append(k1.to_map() if k1 else None)

        if self.template_content is not None:
            result['TemplateContent'] = self.template_content

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AggregatorId') is not None:
            self.aggregator_id = m.get('AggregatorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('CompliancePackTemplateId') is not None:
            self.compliance_pack_template_id = m.get('CompliancePackTemplateId')

        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')

        if m.get('DefaultEnable') is not None:
            self.default_enable = m.get('DefaultEnable')

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
                temp_model = main_models.CreateAggregateCompliancePackShrinkRequestExcludeTagsScope()
                self.exclude_tags_scope.append(temp_model.from_map(k1))

        if m.get('RegionIdsScope') is not None:
            self.region_ids_scope = m.get('RegionIdsScope')

        if m.get('ResourceGroupIdsScope') is not None:
            self.resource_group_ids_scope = m.get('ResourceGroupIdsScope')

        if m.get('ResourceIdsScope') is not None:
            self.resource_ids_scope = m.get('ResourceIdsScope')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        if m.get('TagKeyScope') is not None:
            self.tag_key_scope = m.get('TagKeyScope')

        if m.get('TagValueScope') is not None:
            self.tag_value_scope = m.get('TagValueScope')

        self.tags_scope = []
        if m.get('TagsScope') is not None:
            for k1 in m.get('TagsScope'):
                temp_model = main_models.CreateAggregateCompliancePackShrinkRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        if m.get('TemplateContent') is not None:
            self.template_content = m.get('TemplateContent')

        return self

class CreateAggregateCompliancePackShrinkRequestTagsScope(DaraModel):
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

class CreateAggregateCompliancePackShrinkRequestExcludeTagsScope(DaraModel):
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

