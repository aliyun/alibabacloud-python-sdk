# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetAssetTypeAttributeCodesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.GetAssetTypeAttributeCodesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The list of property definitions.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.GetAssetTypeAttributeCodesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetAssetTypeAttributeCodesResponseBodyData(DaraModel):
    def __init__(
        self,
        attribute_code: str = None,
        attribute_name: str = None,
        attribute_source: str = None,
        attribute_type: str = None,
        description: str = None,
        editable_in: List[str] = None,
        enum_source_type: str = None,
        enum_values: List[main_models.GetAssetTypeAttributeCodesResponseBodyDataEnumValues] = None,
        input_mode: str = None,
        link_target: str = None,
        max_length: int = None,
        required: bool = None,
        system_reference_type: str = None,
        value_type: str = None,
        visible_in: List[str] = None,
    ):
        # The property code (unique identifier).
        self.attribute_code = attribute_code
        # The property name (display name).
        self.attribute_name = attribute_name
        # The property source. Valid values:
        # - SYSTEM: system preset.
        # - CUSTOM: custom.
        self.attribute_source = attribute_source
        # The property type. Valid values:
        # - MANAGEMENT: management property.
        # - TECHNICAL: technical property.
        # - BUSINESS: business property.
        self.attribute_type = attribute_type
        # The property description.
        self.description = description
        # The location where the property can be edited. Valid values:
        # - ASSET: asset catalog.
        # - DEVELOPMENT: development.
        self.editable_in = editable_in
        # The source of dropdown options. Valid values:
        # - MANUAL: manual input.
        # - SYSTEM_REFERENCE: reference to a system property.
        self.enum_source_type = enum_source_type
        # The list of dropdown options. This parameter has a value only when EnumSourceType is set to MANUAL.
        self.enum_values = enum_values
        # The input mode. Valid values:
        # - CUSTOM_INPUT: custom input.
        # - DROPDOWN_SINGLE: single-select dropdown.
        # - DROPDOWN_MULTI: multi-select dropdown.
        # - HYPERLINK: hyperlink.
        self.input_mode = input_mode
        # The hyperlink navigation method. This parameter has a value only when InputMode is set to HYPERLINK. Valid values:
        # - CURRENT_PAGE: opens in the current page.
        # - NEW_PAGE: opens in a new page.
        self.link_target = link_target
        # The maximum length. This parameter is valid only when ValueType is set to STRING.
        self.max_length = max_length
        # Indicates whether the property is required.
        self.required = required
        # The type of the referenced system property. This parameter has a value only when EnumSourceType is set to SYSTEM_REFERENCE.
        self.system_reference_type = system_reference_type
        # The data type of the property value.
        self.value_type = value_type
        # The location where the property is visible. Valid values:
        # - ASSET: asset catalog.
        # - DEVELOPMENT: development.
        self.visible_in = visible_in

    def validate(self):
        if self.enum_values:
            for v1 in self.enum_values:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute_code is not None:
            result['AttributeCode'] = self.attribute_code

        if self.attribute_name is not None:
            result['AttributeName'] = self.attribute_name

        if self.attribute_source is not None:
            result['AttributeSource'] = self.attribute_source

        if self.attribute_type is not None:
            result['AttributeType'] = self.attribute_type

        if self.description is not None:
            result['Description'] = self.description

        if self.editable_in is not None:
            result['EditableIn'] = self.editable_in

        if self.enum_source_type is not None:
            result['EnumSourceType'] = self.enum_source_type

        result['EnumValues'] = []
        if self.enum_values is not None:
            for k1 in self.enum_values:
                result['EnumValues'].append(k1.to_map() if k1 else None)

        if self.input_mode is not None:
            result['InputMode'] = self.input_mode

        if self.link_target is not None:
            result['LinkTarget'] = self.link_target

        if self.max_length is not None:
            result['MaxLength'] = self.max_length

        if self.required is not None:
            result['Required'] = self.required

        if self.system_reference_type is not None:
            result['SystemReferenceType'] = self.system_reference_type

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        if self.visible_in is not None:
            result['VisibleIn'] = self.visible_in

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttributeCode') is not None:
            self.attribute_code = m.get('AttributeCode')

        if m.get('AttributeName') is not None:
            self.attribute_name = m.get('AttributeName')

        if m.get('AttributeSource') is not None:
            self.attribute_source = m.get('AttributeSource')

        if m.get('AttributeType') is not None:
            self.attribute_type = m.get('AttributeType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EditableIn') is not None:
            self.editable_in = m.get('EditableIn')

        if m.get('EnumSourceType') is not None:
            self.enum_source_type = m.get('EnumSourceType')

        self.enum_values = []
        if m.get('EnumValues') is not None:
            for k1 in m.get('EnumValues'):
                temp_model = main_models.GetAssetTypeAttributeCodesResponseBodyDataEnumValues()
                self.enum_values.append(temp_model.from_map(k1))

        if m.get('InputMode') is not None:
            self.input_mode = m.get('InputMode')

        if m.get('LinkTarget') is not None:
            self.link_target = m.get('LinkTarget')

        if m.get('MaxLength') is not None:
            self.max_length = m.get('MaxLength')

        if m.get('Required') is not None:
            self.required = m.get('Required')

        if m.get('SystemReferenceType') is not None:
            self.system_reference_type = m.get('SystemReferenceType')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        if m.get('VisibleIn') is not None:
            self.visible_in = m.get('VisibleIn')

        return self

class GetAssetTypeAttributeCodesResponseBodyDataEnumValues(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        value: str = None,
    ):
        # The display name of the option.
        self.display_name = display_name
        # The option value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

