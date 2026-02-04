# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ValidateNormalizationRuleRequest(DaraModel):
    def __init__(
        self,
        data: str = None,
        extend_field_store_mode: str = None,
        lang: str = None,
        log_sample: str = None,
        normalization_category_id: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_mode: str = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.data = data
        self.extend_field_store_mode = extend_field_store_mode
        self.lang = lang
        self.log_sample = log_sample
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.region_id = region_id
        self.role_for = role_for
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data

        if self.extend_field_store_mode is not None:
            result['ExtendFieldStoreMode'] = self.extend_field_store_mode

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_sample is not None:
            result['LogSample'] = self.log_sample

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression

        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

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
        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('ExtendFieldStoreMode') is not None:
            self.extend_field_store_mode = m.get('ExtendFieldStoreMode')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogSample') is not None:
            self.log_sample = m.get('LogSample')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')

        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

