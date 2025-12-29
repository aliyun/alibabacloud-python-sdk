# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dytnsapi20200217 import models as main_models
from darabonba.model import DaraModel

class QueryTagInfoBySelectionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.QueryTagInfoBySelectionResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code. **OK** indicates that the request is successful.
        self.code = code
        # The returned data.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   true
        # *   false
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
                temp_model = main_models.QueryTagInfoBySelectionResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTagInfoBySelectionResponseBodyData(DaraModel):
    def __init__(
        self,
        auth_code_list: List[str] = None,
        complexity_type: str = None,
        demo_address: str = None,
        doc_address: str = None,
        enum_definition_address: str = None,
        flow_name: str = None,
        industry_id: int = None,
        industry_name: str = None,
        param_list: List[main_models.QueryTagInfoBySelectionResponseBodyDataParamList] = None,
        rich_text_description: str = None,
        scene_id: int = None,
        scene_name: str = None,
        tag_id: int = None,
        tag_name: str = None,
    ):
        # The list of available authorization codes.
        self.auth_code_list = auth_code_list
        self.complexity_type = complexity_type
        # The URL for the API demo.
        self.demo_address = demo_address
        # The URL for the API documentation.
        self.doc_address = doc_address
        # The URL for the definitions of the enumerated values.
        self.enum_definition_address = enum_definition_address
        # The flow name.
        self.flow_name = flow_name
        # The industry ID.
        self.industry_id = industry_id
        # The industry name.
        self.industry_name = industry_name
        # The list of tag parameters.
        self.param_list = param_list
        self.rich_text_description = rich_text_description
        # The scene ID.
        self.scene_id = scene_id
        # The scene name.
        self.scene_name = scene_name
        # The tag ID.
        self.tag_id = tag_id
        # The tag name.
        self.tag_name = tag_name

    def validate(self):
        if self.param_list:
            for v1 in self.param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_code_list is not None:
            result['AuthCodeList'] = self.auth_code_list

        if self.complexity_type is not None:
            result['ComplexityType'] = self.complexity_type

        if self.demo_address is not None:
            result['DemoAddress'] = self.demo_address

        if self.doc_address is not None:
            result['DocAddress'] = self.doc_address

        if self.enum_definition_address is not None:
            result['EnumDefinitionAddress'] = self.enum_definition_address

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.industry_id is not None:
            result['IndustryId'] = self.industry_id

        if self.industry_name is not None:
            result['IndustryName'] = self.industry_name

        result['ParamList'] = []
        if self.param_list is not None:
            for k1 in self.param_list:
                result['ParamList'].append(k1.to_map() if k1 else None)

        if self.rich_text_description is not None:
            result['RichTextDescription'] = self.rich_text_description

        if self.scene_id is not None:
            result['SceneId'] = self.scene_id

        if self.scene_name is not None:
            result['SceneName'] = self.scene_name

        if self.tag_id is not None:
            result['TagId'] = self.tag_id

        if self.tag_name is not None:
            result['TagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCodeList') is not None:
            self.auth_code_list = m.get('AuthCodeList')

        if m.get('ComplexityType') is not None:
            self.complexity_type = m.get('ComplexityType')

        if m.get('DemoAddress') is not None:
            self.demo_address = m.get('DemoAddress')

        if m.get('DocAddress') is not None:
            self.doc_address = m.get('DocAddress')

        if m.get('EnumDefinitionAddress') is not None:
            self.enum_definition_address = m.get('EnumDefinitionAddress')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('IndustryId') is not None:
            self.industry_id = m.get('IndustryId')

        if m.get('IndustryName') is not None:
            self.industry_name = m.get('IndustryName')

        self.param_list = []
        if m.get('ParamList') is not None:
            for k1 in m.get('ParamList'):
                temp_model = main_models.QueryTagInfoBySelectionResponseBodyDataParamList()
                self.param_list.append(temp_model.from_map(k1))

        if m.get('RichTextDescription') is not None:
            self.rich_text_description = m.get('RichTextDescription')

        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')

        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')

        if m.get('TagId') is not None:
            self.tag_id = m.get('TagId')

        if m.get('TagName') is not None:
            self.tag_name = m.get('TagName')

        return self

class QueryTagInfoBySelectionResponseBodyDataParamList(DaraModel):
    def __init__(
        self,
        code: str = None,
        hint: str = None,
        must: bool = None,
        name: str = None,
        type: str = None,
        value_dict: List[main_models.QueryTagInfoBySelectionResponseBodyDataParamListValueDict] = None,
    ):
        # The English name of the parameter.
        self.code = code
        # The input hint.
        self.hint = hint
        # Indicates whether the parameter is required.
        self.must = must
        # The Chinese name of the parameter.
        self.name = name
        # The type. The code that corresponds to EnumUIWidgetTypes.
        self.type = type
        # The definitions of the enumerated values such as Code or Desc.
        self.value_dict = value_dict

    def validate(self):
        if self.value_dict:
            for v1 in self.value_dict:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.hint is not None:
            result['Hint'] = self.hint

        if self.must is not None:
            result['Must'] = self.must

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        result['ValueDict'] = []
        if self.value_dict is not None:
            for k1 in self.value_dict:
                result['ValueDict'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Hint') is not None:
            self.hint = m.get('Hint')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.value_dict = []
        if m.get('ValueDict') is not None:
            for k1 in m.get('ValueDict'):
                temp_model = main_models.QueryTagInfoBySelectionResponseBodyDataParamListValueDict()
                self.value_dict.append(temp_model.from_map(k1))

        return self

class QueryTagInfoBySelectionResponseBodyDataParamListValueDict(DaraModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
    ):
        # The English name.
        self.code = code
        # The Chinese name.
        self.desc = desc

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.desc is not None:
            result['Desc'] = self.desc

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        return self

