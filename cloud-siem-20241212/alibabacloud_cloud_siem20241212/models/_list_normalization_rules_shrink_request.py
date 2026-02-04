# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListNormalizationRulesShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        max_results: int = None,
        next_token: str = None,
        normalization_category_id: str = None,
        normalization_rule_ids_shrink: str = None,
        normalization_rule_name: str = None,
        normalization_rule_type: str = None,
        normalization_schema_id: str = None,
        order_field: str = None,
        order_type: str = None,
        page_number: int = None,
        page_size: int = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        vendor_id: str = None,
    ):
        self.lang = lang
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_category_id = normalization_category_id
        self.normalization_rule_ids_shrink = normalization_rule_ids_shrink
        self.normalization_rule_name = normalization_rule_name
        self.normalization_rule_type = normalization_rule_type
        self.normalization_schema_id = normalization_schema_id
        self.order_field = order_field
        self.order_type = order_type
        self.page_number = page_number
        self.page_size = page_size
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
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_rule_ids_shrink is not None:
            result['NormalizationRuleIds'] = self.normalization_rule_ids_shrink

        if self.normalization_rule_name is not None:
            result['NormalizationRuleName'] = self.normalization_rule_name

        if self.normalization_rule_type is not None:
            result['NormalizationRuleType'] = self.normalization_rule_type

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.order_field is not None:
            result['OrderField'] = self.order_field

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

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
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationRuleIds') is not None:
            self.normalization_rule_ids_shrink = m.get('NormalizationRuleIds')

        if m.get('NormalizationRuleName') is not None:
            self.normalization_rule_name = m.get('NormalizationRuleName')

        if m.get('NormalizationRuleType') is not None:
            self.normalization_rule_type = m.get('NormalizationRuleType')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('OrderField') is not None:
            self.order_field = m.get('OrderField')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

