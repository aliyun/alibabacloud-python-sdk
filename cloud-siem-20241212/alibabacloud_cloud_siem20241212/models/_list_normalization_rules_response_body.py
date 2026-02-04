# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationRulesResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_rules: List[main_models.ListNormalizationRulesResponseBodyNormalizationRules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        total_page: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_rules = normalization_rules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
        self.total_page = total_page

    def validate(self):
        if self.normalization_rules:
            for v1 in self.normalization_rules:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['NormalizationRules'] = []
        if self.normalization_rules is not None:
            for k1 in self.normalization_rules:
                result['NormalizationRules'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.total_page is not None:
            result['TotalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_rules = []
        if m.get('NormalizationRules') is not None:
            for k1 in m.get('NormalizationRules'):
                temp_model = main_models.ListNormalizationRulesResponseBodyNormalizationRules()
                self.normalization_rules.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')

        return self

class ListNormalizationRulesResponseBodyNormalizationRules(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        extend_content_packed: str = None,
        extend_field_store_mode: str = None,
        normalization_category_id: str = None,
        normalization_rule_description: str = None,
        normalization_rule_expression: str = None,
        normalization_rule_format: str = None,
        normalization_rule_id: str = None,
        normalization_rule_mode: str = None,
        normalization_rule_name: str = None,
        normalization_rule_references: List[main_models.ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences] = None,
        normalization_rule_status: str = None,
        normalization_rule_type: str = None,
        normalization_rule_version: str = None,
        normalization_schema_id: str = None,
        product_id: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        self.create_time = create_time
        self.extend_content_packed = extend_content_packed
        self.extend_field_store_mode = extend_field_store_mode
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_description = normalization_rule_description
        self.normalization_rule_expression = normalization_rule_expression
        self.normalization_rule_format = normalization_rule_format
        self.normalization_rule_id = normalization_rule_id
        self.normalization_rule_mode = normalization_rule_mode
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_references = normalization_rule_references
        self.normalization_rule_status = normalization_rule_status
        self.normalization_rule_type = normalization_rule_type
        self.normalization_rule_version = normalization_rule_version
        self.normalization_schema_id = normalization_schema_id
        self.product_id = product_id
        self.update_time = update_time
        self.vendor_id = vendor_id

    def validate(self):
        if self.normalization_rule_references:
            for v1 in self.normalization_rule_references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.extend_content_packed is not None:
            result['ExtendContentPacked'] = self.extend_content_packed

        if self.extend_field_store_mode is not None:
            result['ExtendFieldStoreMode'] = self.extend_field_store_mode

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

        if self.normalization_rule_mode is not None:
            result['NormalizationRuleMode'] = self.normalization_rule_mode

        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name

        result['NormalizationRuleReferences'] = []
        if self.normalization_rule_references is not None:
            for k1 in self.normalization_rule_references:
                result['NormalizationRuleReferences'].append(k1.to_map() if k1 else None)

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

        if m.get('ExtendContentPacked') is not None:
            self.extend_content_packed = m.get('ExtendContentPacked')

        if m.get('ExtendFieldStoreMode') is not None:
            self.extend_field_store_mode = m.get('ExtendFieldStoreMode')

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

        if m.get('NormalizationRuleMode') is not None:
            self.normalization_rule_mode = m.get('NormalizationRuleMode')

        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')

        self.normalization_rule_references = []
        if m.get('NormalizationRuleReferences') is not None:
            for k1 in m.get('NormalizationRuleReferences'):
                temp_model = main_models.ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences()
                self.normalization_rule_references.append(temp_model.from_map(k1))

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

class ListNormalizationRulesResponseBodyNormalizationRulesNormalizationRuleReferences(DaraModel):
    def __init__(
        self,
        data_ingestion_id: str = None,
    ):
        self.data_ingestion_id = data_ingestion_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_ingestion_id is not None:
            result['DataIngestionId'] = self.data_ingestion_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataIngestionId') is not None:
            self.data_ingestion_id = m.get('DataIngestionId')

        return self

