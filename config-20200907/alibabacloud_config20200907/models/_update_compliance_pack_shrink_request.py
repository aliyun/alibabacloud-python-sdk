# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_config20200907 import models as main_models
from darabonba.model import DaraModel

class UpdateCompliancePackShrinkRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        compliance_pack_id: str = None,
        compliance_pack_name: str = None,
        config_rules_shrink: str = None,
        description: str = None,
        exclude_region_ids_scope: str = None,
        exclude_resource_group_ids_scope: str = None,
        exclude_resource_ids_scope: str = None,
        exclude_tags_scope: List[main_models.UpdateCompliancePackShrinkRequestExcludeTagsScope] = None,
        region_ids_scope: str = None,
        resource_group_ids_scope: str = None,
        resource_ids_scope: str = None,
        risk_level: int = None,
        tag_shrink: str = None,
        tag_key_scope: str = None,
        tag_value_scope: str = None,
        tags_scope: List[main_models.UpdateCompliancePackShrinkRequestTagsScope] = None,
    ):
        # The client token that you want to use to ensure the idempotency of the request. You can use the client to generate the value, but you must ensure that it is unique among different requests. The token can contain only ASCII characters and cannot exceed 64 characters in length.``
        self.client_token = client_token
        # The ID of the compliance package.
        # 
        # For more information about how to obtain the ID of a compliance package, see [ListCompliancePacks](https://help.aliyun.com/document_detail/263332.html).
        # 
        # This parameter is required.
        self.compliance_pack_id = compliance_pack_id
        # The name of the compliance package.
        # 
        # For more information about how to obtain the name of a compliance package, see [ListCompliancePacks](https://help.aliyun.com/document_detail/263332.html).
        self.compliance_pack_name = compliance_pack_name
        # The rules in the compliance package.
        # 
        # If you leave this parameter empty, the rules in the compliance package remain unchanged. If you configure this parameter, Cloud Config replaces the existing rules in the compliance package with the specified rules.
        self.config_rules_shrink = config_rules_shrink
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
        self.tag_shrink = tag_shrink
        # The tag key of the resource that you want to evaluate by using the compliance package.
        self.tag_key_scope = tag_key_scope
        # The tag value of the resource that you want to evaluate by using the compliance package.
        # 
        # >  You must configure the TagValueScope parameter together with the TagValueScope parameter.
        self.tag_value_scope = tag_value_scope
        # TagsScope
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

        if self.compliance_pack_id is not None:
            result['CompliancePackId'] = self.compliance_pack_id

        if self.compliance_pack_name is not None:
            result['CompliancePackName'] = self.compliance_pack_name

        if self.config_rules_shrink is not None:
            result['ConfigRules'] = self.config_rules_shrink

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('CompliancePackId') is not None:
            self.compliance_pack_id = m.get('CompliancePackId')

        if m.get('CompliancePackName') is not None:
            self.compliance_pack_name = m.get('CompliancePackName')

        if m.get('ConfigRules') is not None:
            self.config_rules_shrink = m.get('ConfigRules')

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
                temp_model = main_models.UpdateCompliancePackShrinkRequestExcludeTagsScope()
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
                temp_model = main_models.UpdateCompliancePackShrinkRequestTagsScope()
                self.tags_scope.append(temp_model.from_map(k1))

        return self

class UpdateCompliancePackShrinkRequestTagsScope(DaraModel):
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

class UpdateCompliancePackShrinkRequestExcludeTagsScope(DaraModel):
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

