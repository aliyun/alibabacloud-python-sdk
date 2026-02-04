# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class SetDefaultNormalizationRuleVersionResponseBody(DaraModel):
    def __init__(
        self,
        normalization_rule_version: main_models.SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion = None,
        request_id: str = None,
    ):
        self.normalization_rule_version = normalization_rule_version
        self.request_id = request_id

    def validate(self):
        if self.normalization_rule_version:
            self.normalization_rule_version.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRuleVersion') is not None:
            temp_model = main_models.SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion()
            self.normalization_rule_version = temp_model.from_map(m.get('NormalizationRuleVersion'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SetDefaultNormalizationRuleVersionResponseBodyNormalizationRuleVersion(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_name: str = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: int = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_rule_description is not None:
            result['NormalizationRuleDescription'] = self.normalization_rule_description

        if self.normalization_rule_expression is not None:
            result['NormalizationRuleExpression'] = self.normalization_rule_expression

        if self.normalization_rule_format is not None:
            result['NormalizationRuleFormat'] = self.normalization_rule_format

        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name

        if self.normalization_rule_status is not None:
            result['NormalizationRuleStatus'] = self.normalization_rule_status

        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type

        if self.normalization_rule_version is not None:
            result['NormalizationRuleVersion'] = self.normalization_rule_version

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationRuleDescription') is not None:
            self.normalization_rule_description = m.get('NormalizationRuleDescription')

        if m.get('NormalizationRuleExpression') is not None:
            self.normalization_rule_expression = m.get('NormalizationRuleExpression')

        if m.get('NormalizationRuleFormat') is not None:
            self.normalization_rule_format = m.get('NormalizationRuleFormat')

        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')

        if m.get('NormalizationRuleStatus') is not None:
            self.normalization_rule_status = m.get('NormalizationRuleStatus')

        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')

        if m.get('NormalizationRuleVersion') is not None:
            self.normalization_rule_version = m.get('NormalizationRuleVersion')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

