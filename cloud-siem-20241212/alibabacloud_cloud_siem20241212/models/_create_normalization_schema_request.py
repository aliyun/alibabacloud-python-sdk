# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloud_siem20241212 import models as main_models
from darabonba.model import DaraModel

class CreateNormalizationSchemaRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        normalization_category_id: str = None,
        normalization_field_source: str = None,
        normalization_fields: List[main_models.CreateNormalizationSchemaRequestNormalizationFields] = None,
        normalization_schema_description: str = None,
        normalization_schema_id: str = None,
        normalization_schema_name: str = None,
        normalization_schema_type: str = None,
        normalization_security_domain_id: str = None,
        product_id: str = None,
        region_id: str = None,
        role_for: int = None,
        target_log_store: str = None,
        vendor_id: str = None,
    ):
        # The language of the response message. Valid values:
        # 
        # - **zh** (default): Chinese
        # 
        # - **en**: English
        self.lang = lang
        # The ID of the normalization classification.
        self.normalization_category_id = normalization_category_id
        self.normalization_field_source = normalization_field_source
        # The normalization fields.
        self.normalization_fields = normalization_fields
        # The description of the normalization structure.
        self.normalization_schema_description = normalization_schema_description
        # The ID of the normalization structure.
        # 
        # This parameter is required.
        self.normalization_schema_id = normalization_schema_id
        # The name of the normalization structure.
        # 
        # This parameter is required.
        self.normalization_schema_name = normalization_schema_name
        # The type of the normalization structure. Valid values:
        # 
        # - log: a log
        # 
        # - entity: an entity
        # 
        # This parameter is required.
        self.normalization_schema_type = normalization_schema_type
        self.normalization_security_domain_id = normalization_security_domain_id
        self.product_id = product_id
        # The region where the Data Management center for threat analysis is located. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: for assets in the Chinese mainland and China (Hong Kong)
        # 
        # - ap-southeast-1: for assets in regions outside China
        self.region_id = region_id
        # The user ID of a member. An administrator can use this ID to switch to the member\\"s perspective.
        self.role_for = role_for
        # The Simple Log Service Logstore.
        # 
        # This parameter is required.
        self.target_log_store = target_log_store
        self.vendor_id = vendor_id

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

        if self.normalization_category_id is not None:
            result['NormalizationCategoryId'] = self.normalization_category_id

        if self.normalization_field_source is not None:
            result['NormalizationFieldSource'] = self.normalization_field_source

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

        if self.normalization_security_domain_id is not None:
            result['NormalizationSecurityDomainId'] = self.normalization_security_domain_id

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.target_log_store is not None:
            result['TargetLogStore'] = self.target_log_store

        if self.vendor_id is not None:
            result['VendorId'] = self.vendor_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NormalizationCategoryId') is not None:
            self.normalization_category_id = m.get('NormalizationCategoryId')

        if m.get('NormalizationFieldSource') is not None:
            self.normalization_field_source = m.get('NormalizationFieldSource')

        self.normalization_fields = []
        if m.get('NormalizationFields') is not None:
            for k1 in m.get('NormalizationFields'):
                temp_model = main_models.CreateNormalizationSchemaRequestNormalizationFields()
                self.normalization_fields.append(temp_model.from_map(k1))

        if m.get('NormalizationSchemaDescription') is not None:
            self.normalization_schema_description = m.get('NormalizationSchemaDescription')

        if m.get('NormalizationSchemaId') is not None:
            self.normalization_schema_id = m.get('NormalizationSchemaId')

        if m.get('NormalizationSchemaName') is not None:
            self.normalization_schema_name = m.get('NormalizationSchemaName')

        if m.get('NormalizationSchemaType') is not None:
            self.normalization_schema_type = m.get('NormalizationSchemaType')

        if m.get('NormalizationSecurityDomainId') is not None:
            self.normalization_security_domain_id = m.get('NormalizationSecurityDomainId')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('TargetLogStore') is not None:
            self.target_log_store = m.get('TargetLogStore')

        if m.get('VendorId') is not None:
            self.vendor_id = m.get('VendorId')

        return self

class CreateNormalizationSchemaRequestNormalizationFields(DaraModel):
    def __init__(
        self,
        normalization_field_description: str = None,
        normalization_field_example: str = None,
        normalization_field_from: str = None,
        normalization_field_json_index_all: bool = None,
        normalization_field_json_keys: List[main_models.CreateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys] = None,
        normalization_field_name: str = None,
        normalization_field_required: bool = None,
        normalization_field_requirement: bool = None,
        normalization_field_reserved: bool = None,
        normalization_field_tokenize: bool = None,
        normalization_field_type: str = None,
    ):
        # The description of the normalization field.
        self.normalization_field_description = normalization_field_description
        # An example of the normalization field.
        self.normalization_field_example = normalization_field_example
        # The source of the key for a normalization field of the json type.
        self.normalization_field_from = normalization_field_from
        # Indicates whether to create an index for all keys of a json type normalization field.
        self.normalization_field_json_index_all = normalization_field_json_index_all
        # The list of keys for a normalization field of the json type.
        self.normalization_field_json_keys = normalization_field_json_keys
        # The name of the normalization field.
        # 
        # This parameter is required.
        self.normalization_field_name = normalization_field_name
        # Indicates whether the normalization field is required.
        self.normalization_field_required = normalization_field_required
        # Indicates whether the normalization field is required.
        self.normalization_field_requirement = normalization_field_requirement
        # Indicates whether the normalization field is reserved.
        self.normalization_field_reserved = normalization_field_reserved
        # Indicates whether to tokenize the normalization field.
        self.normalization_field_tokenize = normalization_field_tokenize
        # The type of the normalization field. Supported types: text, long, double, and json.
        # 
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

        if self.normalization_field_requirement is not None:
            result['NormalizationFieldRequirement'] = self.normalization_field_requirement

        if self.normalization_field_reserved is not None:
            result['NormalizationFieldReserved'] = self.normalization_field_reserved

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
                temp_model = main_models.CreateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys()
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

        return self

class CreateNormalizationSchemaRequestNormalizationFieldsNormalizationFieldJsonKeys(DaraModel):
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
        # The description of the key for a normalization field of the json type.
        self.normalization_field_description = normalization_field_description
        # An example of the key for a normalization field of the json type.
        self.normalization_field_example = normalization_field_example
        # The source of the key for a normalization field of the json type.
        self.normalization_field_from = normalization_field_from
        # The name of the key for a normalization field of the json type.
        # 
        # This parameter is required.
        self.normalization_field_name = normalization_field_name
        # Indicates whether the key for a normalization field of the json type is required.
        self.normalization_field_required = normalization_field_required
        # Indicates whether to tokenize the key for a normalization field of the json type.
        self.normalization_field_tokenize = normalization_field_tokenize
        # The type of the key for a normalization field of the json type. Supported types: text, long, double, and json.
        # 
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

