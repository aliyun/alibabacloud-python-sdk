# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateNormalizationRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        extend_content_packed: str = None,
        extend_field_store_mode: str = None,
        lang: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_ids_shrink: str = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        normalization_security_domain_id: str = None,
        order_field: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        # Specifies whether to pack non-standard fields into the extension field extend_content. Valid values:
        # - enabled: Enabled.
        # - disabled: Disabled.
        self.extend_content_packed = extend_content_packed
        # The storage mode for extension fields. Valid values: flat, pack, and reject.
        self.extend_field_store_mode = extend_field_store_mode
        # The language of the response. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        self.lang = lang
        # The category ID of the normalization rule.
        self.normalization_category_id = normalization_category_id
        # The description of the normalization rule.
        self.normalization_rule_description = normalization_rule_description
        # The expression of the normalization rule.
        self.normalization_rule_expression = normalization_rule_expression
        # The format of the normalization rule.
        self.normalization_rule_format = normalization_rule_format
        # The list of normalization rule IDs.
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        # The mode of the normalization rule. Valid values:
        # - both
        # - scan
        # - realtime.
        self.normalization_rule_mode = normalization_rule_mode
        # The name of the normalization rule.
        self.normalization_rule_name = normalization_rule_name
        # The type of the normalization rule. Valid values:
        # - predefined: predefined normalization rule.
        # - custom: custom normalization rule.
        self.normalization_rule_type = normalization_rule_type
        # The version of the normalization rule.
        self.normalization_rule_version = normalization_rule_version
        # The normalization schema ID.
        self.normalization_schema_id = normalization_schema_id
        self.normalization_security_domain_id = normalization_security_domain_id
        # The field used to sort the rule list. Valid values:
        # - GmtModified: sorted by modification time.
        # - Id: sorted by rule ID (default).
        self.order_field = order_field
        # The product ID.
        self.product_id = product_id
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland.
        # - ap-southeast-1: Your assets reside outside China.
        self.region_id = region_id
        # The ID of the member accounts in the resource directory.
        self.role_for = role_for
        # The vendor ID associated with the normalization rule.
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed

        if self.extend_field_store_mode is not None:
            result['ExtendFieldStoreMode'] = self.extend_field_store_mode

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description

        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression

        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format

        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink

        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode

        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name

        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type

        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')

        if m.get('ExtendFieldStoreMode') is not None:
            self.extend_field_store_mode = m.get('ExtendFieldStoreMode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')

        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')

        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')

        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')

        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')

        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')

        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')

        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

