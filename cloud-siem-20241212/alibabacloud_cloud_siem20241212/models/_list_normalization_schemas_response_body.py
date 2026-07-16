# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class ListNormalizationSchemasResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        normalization_schemas: List[main_models.ListNormalizationSchemasResponseBodyNormalizationSchemas] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The maximum number of entries to return in this request.
        self.max_results = max_results
        # The pagination token for the next query. Leave this parameter empty for the first query or if no more results exist. If more results exist, set this parameter to the NextToken value returned by the previous API call.
        self.next_token = next_token
        # The list of normalization schemas.
        self.normalization_schemas = normalization_schemas
        # The request ID.
        self.request_id = request_id
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.normalization_schemas:
            for v1 in self.normalization_schemas:
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

        result['NormalizationSchemas'] = []
        if self.normalization_schemas is not None:
            for k1 in self.normalization_schemas:
                result['NormalizationSchemas'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.normalization_schemas = []
        if m.get('NormalizationSchemas') is not None:
            for k1 in m.get('NormalizationSchemas'):
                temp_model = main_models.ListNormalizationSchemasResponseBodyNormalizationSchemas()
                self.normalization_schemas.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListNormalizationSchemasResponseBodyNormalizationSchemas(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_field_source: str = None,
        normalization_schema_description: str = None,
        normalization_schema_from: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_target_log_store: str = None,
        normalization_schema_type: str = None,
        normalization_security_domain_id: str = None,
        product_id: str = None,
        recommend_entities: List[str] = None,
        target_log_store: str = None,
        target_store_view: str = None,
        update_time: int = None,
        vendor_id: str = None,
    ):
        # The creation time.
        self.create_time = create_time
        # The ID of the normalization rule category.
        self.normalization_category_id = normalization_category_id
        # The field source. Valid values:
        # normalized: normalized field.
        # native: native field.
        self.normalization_field_source = normalization_field_source
        # The description of the normalization schema.
        self.normalization_schema_description = normalization_schema_description
        # The source of the normalization schema. Valid values: preset (predefined) and custom (user-defined).
        self.normalization_schema_from = normalization_schema_from
        # The ID of the normalization schema.
        self.normalization_schema_id = normalization_schema_id
        # The name of the normalization schema.
        self.normalization_schema_name = normalization_schema_name
        # The LogStore to which the normalization output is written.
        self.normalization_schema_target_log_store = normalization_schema_target_log_store
        # The normalization schema type.
        self.normalization_schema_type = normalization_schema_type
        # The security domain ID.
        self.normalization_security_domain_id = normalization_security_domain_id
        # The product ID.
        self.product_id = product_id
        self.recommend_entities = recommend_entities
        # The Simple Log Service LogStore.
        self.target_log_store = target_log_store
        # The Simple Log Service StoreView.
        self.target_store_view = target_store_view
        # The update time.
        self.update_time = update_time
        # The vendor ID.
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

        if self.normalization_field_source is not None:
            result['NormalizationFieldSource'] = self.normalization_field_source

        if self.normalization_schema_description is not None:
            result['NormalizationSchemaDescription'] = self.normalization_schema_description

        if self.normalization_schema_from is not None:
            result['NormalizationSchemaFrom'] = self.normalization_schema_from

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.normalization_schema_name is not None:
            result['NormalizationSchemaName'] = self.normalization_schema_name

        if self.normalization_schema_target_log_store is not None:
            result['NormalizationSchemaTargetLogStore'] = self.normalization_schema_target_log_store

        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type

        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.recommend_entities is not None:
            result['RecommendEntities'] = self.recommend_entities

        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store

        if self.target_store_view is not None:
            result['TargetStoreView'] = self.target_store_view

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

        if m.get('NormalizationFieldSource') is not None:
            self.normalization_field_source = m.get('NormalizationFieldSource')

        if m.get('NormalizationSchemaDescription') is not None:
            self.normalization_schema_description = m.get('NormalizationSchemaDescription')

        if m.get('NormalizationSchemaFrom') is not None:
            self.normalization_schema_from = m.get('NormalizationSchemaFrom')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')

        if m.get('NormalizationSchemaTargetLogStore') is not None:
            self.normalization_schema_target_log_store = m.get('NormalizationSchemaTargetLogStore')

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RecommendEntities') is not None:
            self.recommend_entities = m.get('RecommendEntities')

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('TargetStoreView') is not None:
            self.target_store_view = m.get('TargetStoreView')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

