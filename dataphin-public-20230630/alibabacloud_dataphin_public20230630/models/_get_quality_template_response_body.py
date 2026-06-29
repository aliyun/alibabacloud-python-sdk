# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetQualityTemplateResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        quality_template_info: main_models.GetQualityTemplateResponseBodyQualityTemplateInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # The details of the template object.
        self.quality_template_info = quality_template_info
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.quality_template_info:
            self.quality_template_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.quality_template_info is not None:
            result['QualityTemplateInfo'] = self.quality_template_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('QualityTemplateInfo') is not None:
            temp_model = main_models.GetQualityTemplateResponseBodyQualityTemplateInfo()
            self.quality_template_info = temp_model.from_map(m.get('QualityTemplateInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetQualityTemplateResponseBodyQualityTemplateInfo(DaraModel):
    def __init__(
        self,
        catalog: str = None,
        catalog_name: str = None,
        create_time: str = None,
        creator: str = None,
        creator_name: str = None,
        description: str = None,
        form_property_list: List[main_models.GetQualityTemplateResponseBodyQualityTemplateInfoFormPropertyList] = None,
        id: int = None,
        is_system_template: bool = None,
        modifier: str = None,
        modifier_name: str = None,
        modify_time: str = None,
        name: str = None,
        owner: str = None,
        owner_name: str = None,
        support_all_data_source_type: bool = None,
        support_data_source_type_list: List[str] = None,
        type: str = None,
        type_name: str = None,
    ):
        # The template category. Valid values:
        # - CONSISTENT: consistency.
        # - EFFECTIVE: validity.
        # - TIMELINESE: timeliness.
        # - ACCURATE: accuracy.
        # - UNIQUENESS: uniqueness.
        # - COMPLETENESS: completeness.
        # - STABILITY: stability.
        # - CUSTOM: custom.
        self.catalog = catalog
        # The display name of the template category.
        self.catalog_name = catalog_name
        # The creation time.
        self.create_time = create_time
        # The user ID of the creator.
        self.creator = creator
        # The name of the creator.
        self.creator_name = creator_name
        # The template description.
        self.description = description
        # The key-value pairs of the rule configuration.
        self.form_property_list = form_property_list
        # The template ID.
        self.id = id
        # Indicates whether the template is a system template.
        self.is_system_template = is_system_template
        # The user ID of the last modifier.
        self.modifier = modifier
        # The name of the last modifier.
        self.modifier_name = modifier_name
        # The modification time.
        self.modify_time = modify_time
        # The template name.
        self.name = name
        # The user ID of the owner.
        self.owner = owner
        # The name of the owner.
        self.owner_name = owner_name
        # Indicates whether all data source types are supported.
        self.support_all_data_source_type = support_all_data_source_type
        # The list of supported data source types, such as MySQL, Oracle, Microsoft SQL Server, MaxCompute, and Hive.
        self.support_data_source_type_list = support_data_source_type_list
        # The templatetype. Valid values:
        # - FIELD_NULL_VALUE_VALIDATE: field null value check.
        # - FIELD_EMPTY_STRING_VALIDATE: field empty character string check.
        # - FIELD_UNIQUE_VALIDATE: field uniqueness check.
        # - FIELD_GROUP_COUNT_VALIDATE: field unique value count check.
        # - FIELD_DUPLICATE_VALUE_COUNT_VALIDATE: field duplicate value count check.
        # - FUNCTION_TIME_COMPARE: time function comparison.
        # - SINGLE_TABLE_TIME_COMPARE: non-partitioned table time field comparison.
        # - DOUBLE_TABLE_TIME_COMPARE: two-table time field comparison.
        # - FIELD_FORMAT_VALIDATE: field format check.
        # - FIELD_LENGTH_VALIDATE: field length check.
        # - FIELD_VALUE_RANGE_VALIDATE: field value range check.
        # - CODE_TABLE_COMPARE: lookup table reference comparison.
        # - STANDARD_CODE_TABLE_COMPARE: data standard lookup table reference comparison.
        # - SINGLE_TABLE_FIELD_VALUE_COMPARE: non-partitioned table field value consistency comparison.
        # - SINGLE_TABLE_FIELD_STATISTICAL_COMPARE: non-partitioned table field statistical value consistency comparison.
        # - SINGLE_TABLE_FIELD_EXP_COMPARE: non-partitioned table field business logic consistency comparison.
        # - DOUBLE_TABLE_FIELD_VALUE_COMPARE: two-table field value consistency comparison.
        # - DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: two-table field statistical value consistency comparison.
        # - CROSS_DOUBLE_TABLE_FIELD_STATISTICAL_COMPARE: cross-source two-table field statistical value consistency comparison.
        # - DOUBLE_TABLE_FIELD_EXP_COMPARE: two-table field business logic consistency comparison.
        # - TABLE_STABILITY_VALIDATE: table stability check.
        # - TABLE_FLUCTUATION_VALIDATE: table fluctuation check.
        # - FIELD_STABILITY_VALIDATE: field stability check.
        # - FIELD_FLUCTUATION_VALIDATE: field fluctuation check.
        # - CUSTOM_STATISTICAL_VALIDATE: custom statistical metric check.
        # - CUSTOM_DATA_DETAILS_VALIDATE: custom data details check.
        # - DATASOURCE_AVAILABLE_CHECK: data source connectivity monitoring.
        # - TABLE_SCHEMA_CHECK: table schema change monitoring.
        # - REAL_TIME_OFFLINE_COMPARE: real-time and offline comparison.
        # - REAL_TIME_STATISTICAL_VALIDATE: real-time statistical value monitoring.
        # - REAL_TIME_MULTI_CHAIN_COMPARE: real-time multi-link comparison.
        self.type = type
        # The display name of the templatetype.
        self.type_name = type_name

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

        if self.catalog_name is not None:
            result['CatalogName'] = self.catalog_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.description is not None:
            result['Description'] = self.description

        result['FormPropertyList'] = []
        if self.form_property_list is not None:
            for k1 in self.form_property_list:
                result['FormPropertyList'].append(k1.to_map() if k1 else None)

        if self.id is not None:
            result['Id'] = self.id

        if self.is_system_template is not None:
            result['IsSystemTemplate'] = self.is_system_template

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.modifier_name is not None:
            result['ModifierName'] = self.modifier_name

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.support_all_data_source_type is not None:
            result['SupportAllDataSourceType'] = self.support_all_data_source_type

        if self.support_data_source_type_list is not None:
            result['SupportDataSourceTypeList'] = self.support_data_source_type_list

        if self.type is not None:
            result['Type'] = self.type

        if self.type_name is not None:
            result['TypeName'] = self.type_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Catalog') is not None:
            self.catalog = m.get('Catalog')

        if m.get('CatalogName') is not None:
            self.catalog_name = m.get('CatalogName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        self.form_property_list = []
        if m.get('FormPropertyList') is not None:
            for k1 in m.get('FormPropertyList'):
                temp_model = main_models.GetQualityTemplateResponseBodyQualityTemplateInfoFormPropertyList()
                self.form_property_list.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IsSystemTemplate') is not None:
            self.is_system_template = m.get('IsSystemTemplate')

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('ModifierName') is not None:
            self.modifier_name = m.get('ModifierName')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('SupportAllDataSourceType') is not None:
            self.support_all_data_source_type = m.get('SupportAllDataSourceType')

        if m.get('SupportDataSourceTypeList') is not None:
            self.support_data_source_type_list = m.get('SupportDataSourceTypeList')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('TypeName') is not None:
            self.type_name = m.get('TypeName')

        return self

class GetQualityTemplateResponseBodyQualityTemplateInfoFormPropertyList(DaraModel):
    def __init__(
        self,
        component_type: str = None,
        name: str = None,
        value: str = None,
    ):
        # The control type.
        self.component_type = component_type
        # The property name.
        self.name = name
        # The property value.
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

