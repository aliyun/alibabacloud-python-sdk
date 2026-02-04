# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class GetNormalizationSchemaResponseBody(DaraModel):
    def __init__(
        self,
        normalization_schema: main_models.GetNormalizationSchemaResponseBodyNormalizationSchema = None,
        request_id: str = None,
    ):
        self.normalization_schema = normalization_schema
        self.request_id = request_id

    def validate(self):
        if self.normalization_schema:
            self.normalization_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normalization_schema is not None:
            result['NormalizationSchema'] = self.normalization_schema.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationSchema') is not None:
            temp_model = main_models.GetNormalizationSchemaResponseBodyNormalizationSchema()
            self.normalization_schema = temp_model.from_map(m.get('NormalizationSchema'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetNormalizationSchemaResponseBodyNormalizationSchema(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_category_id: str = None,
        normalization_fields: List[main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields] = None,
        normalization_schema_description: str = None,
        normalization_schema_from: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_references: List[main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationSchemaReferences] = None,
        normalization_schema_type: str = None,
        target_log_store: str = None,
        target_store_view: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_category_id = normalization_category_id
        self.normalization_fields = normalization_fields
        self.normalization_schema_description = normalization_schema_description
        self.normalization_schema_from = normalization_schema_from
        self.normalization_schema_id = normalization_schema_id
        self.normalization_schema_name = normalization_schema_name
        self.normalization_schema_references = normalization_schema_references
        self.normalization_schema_type = normalization_schema_type
        self.target_log_store = target_log_store
        self.target_store_view = target_store_view
        self.update_time = update_time

    def validate(self):
        if self.normalization_fields:
            for v1 in self.normalization_fields:
                 if v1:
                    v1.validate()
        if self.normalization_schema_references:
            for v1 in self.normalization_schema_references:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        result['NormalizationFields'] = []
        if self.normalization_fields is not None:
            for k1 in self.normalization_fields:
                result['NormalizationFields'].append(k1.to_map() if k1 else None)

        if self.normalization_schema_description is not None:
            result['NormalizationSchemaDescription'] = self.normalization_schema_description

        if self.normalization_schema_from is not None:
            result['NormalizationSchemaFrom'] = self.normalization_schema_from

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.normalization_schema_name is not None:
            result['NormalizationSchemaName'] = self.normalization_schema_name

        result['NormalizationSchemaReferences'] = []
        if self.normalization_schema_references is not None:
            for k1 in self.normalization_schema_references:
                result['NormalizationSchemaReferences'].append(k1.to_map() if k1 else None)

        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type

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

        self.normalization_fields = []
        if m.get('NormalizationFields') is not None:
            for k1 in m.get('NormalizationFields'):
                temp_model = main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields()
                self.normalization_fields.append(temp_model.from_map(k1))

        if m.get('NormalizationSchemaDescription') is not None:
            self.normalization_schema_description = m.get('NormalizationSchemaDescription')

        if m.get('NormalizationSchemaFrom') is not None:
            self.normalization_schema_from = m.get('NormalizationSchemaFrom')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')

        self.normalization_schema_references = []
        if m.get('NormalizationSchemaReferences') is not None:
            for k1 in m.get('NormalizationSchemaReferences'):
                temp_model = main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationSchemaReferences()
                self.normalization_schema_references.append(temp_model.from_map(k1))

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('TargetStoreView') is not None:
            self.target_store_view = m.get('TargetStoreView')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationSchemaReferences(DaraModel):
    def __init__(
        self,
        normalization_rule_id: str = None,
    ):
        self.normalization_rule_id = normalization_rule_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.normalization_rule_id is not None:
            result['NormalizationRuleId'] = self.normalization_rule_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NormalizationRuleId') is not None:
            self.normalization_rule_id = m.get('NormalizationRuleId')

        return self

class GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFields(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_from: str = None,
        normalization_field_json_index_all: bool = None,
        normalization_field_json_keys: List[main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFieldsNormalizationFieldJsonKeys] = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_requirement: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_tokenize: bool = None,
        normalization_field_type: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_from = normalization_field_from
        self.normalization_field_json_index_all = normalization_field_json_index_all
        self.normalization_field_json_keys = normalization_field_json_keys
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.normalization_field_requirement = normalization_field_requirement
        self.normalization_field_reserved = normalization_field_reserved
        self.normalization_field_tokenize = normalization_field_tokenize
        self.normalization_field_type = normalization_field_type
        self.update_time = update_time

    def validate(self):
        if self.normalization_field_json_keys:
            for v1 in self.normalization_field_json_keys:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.normalization_field_description is not None:
            result['NormalizationFieldDescription'] = self.normalization_field_description

        if self.normalization_field_example is not None:
            result['NormalizationFieldExample'] = self.normalization_field_example

        if self.normalization_field_from is not None:
            result['NormalizationFieldFrom'] = self.normalization_field_from

        if self.normalization_field_json_index_all is not None:
            result['NormalizationFieldJsonIndexAll'] = self.normalization_field_json_index_all

        result['NormalizationFieldJsonKeys'] = []
        if self.normalization_field_json_keys is not None:
            for k1 in self.normalization_field_json_keys:
                result['NormalizationFieldJsonKeys'].append(k1.to_map() if k1 else None)

        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name

        if self.normalization_field_required is not None:
            result['NormalizationFieldRequired'] = self.normalization_field_required

        if self.normalization_field_requirement is not None:
            result['NormalizationFieldRequirement'] = self.normalization_field_requirement

        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved

        if self.normalization_field_tokenize is not None:
            result['NormalizationFieldTokenize'] = self.normalization_field_tokenize

        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NormalizationFieldDescription') is not None:
            self.normalization_field_description = m.get('NormalizationFieldDescription')

        if m.get('NormalizationFieldExample') is not None:
            self.normalization_field_example = m.get('NormalizationFieldExample')

        if m.get('NormalizationFieldFrom') is not None:
            self.normalization_field_from = m.get('NormalizationFieldFrom')

        if m.get('NormalizationFieldJsonIndexAll') is not None:
            self.normalization_field_json_index_all = m.get('NormalizationFieldJsonIndexAll')

        self.normalization_field_json_keys = []
        if m.get('NormalizationFieldJsonKeys') is not None:
            for k1 in m.get('NormalizationFieldJsonKeys'):
                temp_model = main_models.GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFieldsNormalizationFieldJsonKeys()
                self.normalization_field_json_keys.append(temp_model.from_map(k1))

        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')

        if m.get('NormalizationFieldRequired') is not None:
            self.normalization_field_required = m.get('NormalizationFieldRequired')

        if m.get('NormalizationFieldRequirement') is not None:
            self.normalization_field_requirement = m.get('NormalizationFieldRequirement')

        if m.get('NormalizationFieldReserved') is not None:
            self.normalization_field_reserved = m.get('NormalizationFieldReserved')

        if m.get('NormalizationFieldTokenize') is not None:
            self.normalization_field_tokenize = m.get('NormalizationFieldTokenize')

        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class GetNormalizationSchemaResponseBodyNormalizationSchemaNormalizationFieldsNormalizationFieldJsonKeys(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_from: str = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_tokenize: bool = None,
        normalization_field_type: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_from = normalization_field_from
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.normalization_field_reserved = normalization_field_reserved
        self.normalization_field_tokenize = normalization_field_tokenize
        self.normalization_field_type = normalization_field_type
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

        if self.normalization_field_description is not None:
            result['NormalizationFieldDescription'] = self.normalization_field_description

        if self.normalization_field_example is not None:
            result['NormalizationFieldExample'] = self.normalization_field_example

        if self.normalization_field_from is not None:
            result['NormalizationFieldFrom'] = self.normalization_field_from

        if self.normalization_field_name is not None:
            result['NormalizationFieldName'] = self.normalization_field_name

        if self.normalization_field_required is not None:
            result['NormalizationFieldRequired'] = self.normalization_field_required

        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved

        if self.normalization_field_tokenize is not None:
            result['NormalizationFieldTokenize'] = self.normalization_field_tokenize

        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('NormalizationFieldDescription') is not None:
            self.normalization_field_description = m.get('NormalizationFieldDescription')

        if m.get('NormalizationFieldExample') is not None:
            self.normalization_field_example = m.get('NormalizationFieldExample')

        if m.get('NormalizationFieldFrom') is not None:
            self.normalization_field_from = m.get('NormalizationFieldFrom')

        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')

        if m.get('NormalizationFieldRequired') is not None:
            self.normalization_field_required = m.get('NormalizationFieldRequired')

        if m.get('NormalizationFieldReserved') is not None:
            self.normalization_field_reserved = m.get('NormalizationFieldReserved')

        if m.get('NormalizationFieldTokenize') is not None:
            self.normalization_field_tokenize = m.get('NormalizationFieldTokenize')

        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

