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
        self.max_results = max_results
        self.next_token = next_token
        self.normalization_schemas = normalization_schemas
        self.request_id = request_id
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
        normalization_schema_description: str = None,
        normalization_schema_from: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_target_log_store: str = None,
        target_log_store: str = None,
        target_store_view: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_schema_description = normalization_schema_description
        self.normalization_schema_from = normalization_schema_from
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_name = normalization_schema_name
        self.normalization_schema_target_log_store = normalization_schema_target_log_store
        self.target_log_store = target_log_store
        self.target_store_view = target_store_view
        self.update_time = update_time

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

        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store

        if self.target_store_view is not None:
            result['TargetStoreView'] = self.target_store_view

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

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

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('TargetStoreView') is not None:
            self.target_store_view = m.get('TargetStoreView')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

