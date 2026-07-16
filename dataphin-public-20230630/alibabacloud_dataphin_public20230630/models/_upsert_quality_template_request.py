# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpsertQualityTemplateRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        upsert_command: main_models.UpsertQualityTemplateRequestUpsertCommand = None,
    ):
        # Tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # Upsert command.
        # 
        # This parameter is required.
        self.upsert_command = upsert_command

    def validate(self):
        if self.upsert_command:
            self.upsert_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.upsert_command is not None:
            result['UpsertCommand'] = self.upsert_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('UpsertCommand') is not None:
            temp_model = main_models.UpsertQualityTemplateRequestUpsertCommand()
            self.upsert_command = temp_model.from_map(m.get('UpsertCommand'))

        return self

class UpsertQualityTemplateRequestUpsertCommand(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        description: str = None,
        form_property_list: List[main_models.UpsertQualityTemplateRequestUpsertCommandFormPropertyList] = None,
        id: int = None,
        name: str = None,
        owner: str = None,
        support_data_source_type_list: List[str] = None,
        type: str = None,
    ):
        # Template category. Valid values: CONSISTENT: consistency. EFFECTIVE: validity. TIMELINESE: timeliness. ACCURATE: accuracy. UNIQUENESS: uniqueness. COMPLETENESS: completeness. STABILITY: stability. CUSTOM: custom.
        # 
        # This parameter is required.
        self.catalog = catalog
        # Template description.
        self.description = description
        # Rule configuration key-value pairs.
        self.form_property_list = form_property_list
        # Template ID. If specified, it indicates an update operation. If not specified, it indicates a creation operation.
        self.id = id
        # Template name.
        # 
        # This parameter is required.
        self.name = name
        # Template owner ID.
        # 
        # This parameter is required.
        self.owner = owner
        # Supported data source types, such as MySQL, Oracle, Microsoft SQL Server, MaxCompute, and Hive.
        self.support_data_source_type_list = support_data_source_type_list
        # Template type. Valid values: FIELD_NULL_VALUE_VALIDATE: field null value validation. FIELD_EMPTY_STRING_VALIDATE: field empty string validation. FIELD_UNIQUE_VALIDATE: field uniqueness validation. FIELD_GROUP_COUNT_VALIDATE: field unique value count validation. FIELD_DUPLICATE_VALUE_COUNT_VALIDATE: field duplicate value count validation. FUNCTION_TIME_COMPARE: time function comparison. SINGLE_TABLE_TIME_COMPARE: single-table time field comparison. DOUBLE_TABLE_TIME_COMPARE: cross-table time field comparison. FIELD_FORMAT_VALIDATE: field format validation. FIELD_LENGTH_VALIDATE: field length validation. FIELD_VALUE_RANGE_VALIDATE: field value range validation. CODE_TABLE_COMPARE: code table reference comparison. STANDARD_CODE_TABLE_COMPARE: data standard code table reference comparison. SINGLE_TABLE_FIELD_VALUE_COMPARE: single-table field value consistency comparison. SINGLE_TABLE_FIELD_STATISTICAL_COMPARE: single-table field statistical value consistency comparison. SINGLE_TABLE_FIELD_EXP_COMPARE: single-table field business logic consistency comparison. DOUBLE_TABLE_FIELD_VALUE_COMPARE: cross-table field value consistency comparison. DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: cross-table field statistical value consistency comparison. CROSS_DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: cross-source cross-table field statistical value consistency comparison. DOUBLE_TABLE_FIELD_EXP_COMPARE: cross-table field business logic consistency comparison. TABLE_STABILITY_VALIDATE: table stability validation. TABLE_FLUCTUATION_VALIDATE: table fluctuation validation. FIELD_STABILITY_VALIDATE: field stability validation. FIELD_FLUCTUATION_VALIDATE: field fluctuation validation. CUSTOM_STATISTICAL_VALIDATE: custom statistical metric validation. CUSTOM_DATA_DETAILS_VALIDATE: custom data details validation. DATASOURCE_AVAILABLE_CHECK: data source connectivity check. TABLE_SCHEMA_CHECK: table schema change detection. REAL_TIME_OFFLINE_COMPARE: real-time and offline comparison. REAL_TIME_STATISTICAL_VALIDATE: real-time statistical value monitoring. REAL_TIME_MULTI_CHAIN_COMPARE: real-time multi-chain comparison.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        if self.form_property_list:
            for v1 in self.form_property_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.catalog is not None:
            result['Catalog'] = self.catalog

        if self.description is not None:
            result['Description'] = self.description

        result['FormPropertyList'] = []
        if self.form_property_list is not None:
            for k1 in self.form_property_list:
                result['FormPropertyList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.support_data_source_type_list is not None:
            result['SupportDataSourceTypeList'] = self.support_data_source_type_list

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.form_property_list = []
        if m.get('FormPropertyList') is not None:
            for k1 in m.get('FormPropertyList'):
                temp_model = main_models.UpsertQualityTemplateRequestUpsertCommandFormPropertyList()
                self.form_property_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('SupportDataSourceTypeList') is not None:
            self.support_data_source_type_list = m.get('SupportDataSourceTypeList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class UpsertQualityTemplateRequestUpsertCommandFormPropertyList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        name: str = None,
        value: str = None,
    ):
        # Component type.
        self.component_type = component_type
        # Property name.
        self.name = name
        # Property value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_type is not None:
            result['ComponentType'] = self.component_type

        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

