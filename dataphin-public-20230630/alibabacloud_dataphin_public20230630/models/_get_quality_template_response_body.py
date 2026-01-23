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
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.quality_template_info = quality_template_info
        # Id of the request
        self.request_id = request_id
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
        self.catalog = catalog
        self.catalog_name = catalog_name
        self.create_time = create_time
        self.creator = creator
        self.creator_name = creator_name
        self.description = description
        self.form_property_list = form_property_list
        self.id = id
        self.is_system_template = is_system_template
        self.modifier = modifier
        self.modifier_name = modifier_name
        self.modify_time = modify_time
        self.name = name
        self.owner = owner
        self.owner_name = owner_name
        self.support_all_data_source_type = support_all_data_source_type
        self.support_data_source_type_list = support_data_source_type_list
        self.type = type
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
        self.component_type = component_type
        self.name = name
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

