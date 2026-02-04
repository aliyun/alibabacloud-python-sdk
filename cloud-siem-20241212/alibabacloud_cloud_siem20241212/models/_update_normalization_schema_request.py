# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class UpdateNormalizationSchemaRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        normalization_fields: List[main_models.UpdateNormalizationSchemaRequestNormalizationFields] = None,
        normalization_schema_description: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_type: str = None,
        region_id: str = None,
        role_for: int = None,
    ):
        self.lang = lang
        self.normalization_fields = normalization_fields
        self.normalization_schema_description = normalization_schema_description
        # This parameter is required.
        self.normalization_schema_id = normalization_schema_id
        # This parameter is required.
        self.normalization_schema_name = normalization_schema_name
        # This parameter is required.
        self.normalization_schema_type = normalization_schema_type
        self.region_id = region_id
        self.role_for = role_for

    def validate(self):
        if self.normalization_fields:
            for v1 in self.normalization_fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        result['NormalizationFields'] = []
        if self.normalization_fields is not None:
            for k1 in self.normalization_fields:
                result['NormalizationFields'].append(k1.to_map() if k1 else None)

        if self.normalization_schema_description is not None:
            result['NormalizationSchemaDescription'] = self.normalization_schema_description

        if self.normalization_schema_id is not None:
            result['NormalizationSchemaId'] = self.normalization_schema_id

        if self.normalization_schema_name is not None:
            result['NormalizationSchemaName'] = self.normalization_schema_name

        if self.normalization_schema_type is not None:
            result['NormalizationSchemaType'] = self.normalization_schema_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        self.normalization_fields = []
        if m.get('NormalizationFields') is not None:
            for k1 in m.get('NormalizationFields'):
                temp_model = main_models.UpdateNormalizationSchemaRequestNormalizationFields()
                self.normalization_fields.append(temp_model.from_map(k1))

        if m.get('NormalizationSchemaDescription') is not None:
            self.normalization_schema_description = m.get('NormalizationSchemaDescription')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        return self

class UpdateNormalizationSchemaRequestNormalizationFields(DaraModel):
    def __init__(
        self,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_from: str = None,
        normalization_field_json_index_all: bool = None,
        normalization_field_json_keys: List[main_models.UpdateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys] = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_tokenize: bool = None,
        normalization_field_type: str = None,
    ):
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_from = normalization_field_from
        self.normalization_field_json_index_all = normalization_field_json_index_all
        self.normalization_field_json_keys = normalization_field_json_keys
        # This parameter is required.
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.normalization_field_tokenize = normalization_field_tokenize
        # This parameter is required.
        self.normalization_field_type = normalization_field_type

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

        if self.normalization_field_tokenize is not None:
            result['NormalizationFieldTokenize'] = self.normalization_field_tokenize

        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
                temp_model = main_models.UpdateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys()
                self.normalization_field_json_keys.append(temp_model.from_map(k1))

        if m.get('NormalizationFieldName') is not None:
            self.normalization_field_name = m.get('NormalizationFieldName')

        if m.get('NormalizationFieldRequired') is not None:
            self.normalization_field_required = m.get('NormalizationFieldRequired')

        if m.get('NormalizationFieldTokenize') is not None:
            self.normalization_field_tokenize = m.get('NormalizationFieldTokenize')

        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')

        return self

class UpdateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys(DaraModel):
    def __init__(
        self,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_from: str = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_tokenize: bool = None,
        normalization_field_type: str = None,
    ):
        self.normalization_field_description = normalization_field_description
        self.normalization_field_example = normalization_field_example
        self.normalization_field_from = normalization_field_from
        # This parameter is required.
        self.normalization_field_name = normalization_field_name
        self.normalization_field_required = normalization_field_required
        self.normalization_field_tokenize = normalization_field_tokenize
        # This parameter is required.
        self.normalization_field_type = normalization_field_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.normalization_field_tokenize is not None:
            result['NormalizationFieldTokenize'] = self.normalization_field_tokenize

        if self.normalization_field_type is not None:
            result['NormalizationFieldType'] = self.normalization_field_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('NormalizationFieldTokenize') is not None:
            self.normalization_field_tokenize = m.get('NormalizationFieldTokenize')

        if m.get('NormalizationFieldType') is not None:
            self.normalization_field_type = m.get('NormalizationFieldType')

        return self

