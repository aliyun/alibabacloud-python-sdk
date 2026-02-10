# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class RunCompletionRequest(DaraModel):
    def __init__(
        self,
        dialogue: main_models.RunCompletionRequestDialogue = None,
        fields: List[main_models.RunCompletionRequestFields] = None,
        model_code: str = None,
        service_inspection: main_models.RunCompletionRequestServiceInspection = None,
        stream: bool = None,
        template_ids: List[int] = None,
        response_format_type: str = None,
        variables: List[main_models.RunCompletionRequestVariables] = None,
    ):
        # This parameter is required.
        self.dialogue = dialogue
        self.fields = fields
        self.model_code = model_code
        self.service_inspection = service_inspection
        self.stream = stream
        # This parameter is required.
        self.template_ids = template_ids
        self.response_format_type = response_format_type
        self.variables = variables

    def validate(self):
        if self.dialogue:
            self.dialogue.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.variables:
            for v1 in self.variables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialogue is not None:
            result['Dialogue'] = self.dialogue.to_map()

        result['Fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['Fields'].append(k1.to_map() if k1 else None)

        if self.model_code is not None:
            result['ModelCode'] = self.model_code

        if self.service_inspection is not None:
            result['ServiceInspection'] = self.service_inspection.to_map()

        if self.stream is not None:
            result['Stream'] = self.stream

        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids

        if self.response_format_type is not None:
            result['responseFormatType'] = self.response_format_type

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dialogue') is not None:
            temp_model = main_models.RunCompletionRequestDialogue()
            self.dialogue = temp_model.from_map(m.get('Dialogue'))

        self.fields = []
        if m.get('Fields') is not None:
            for k1 in m.get('Fields'):
                temp_model = main_models.RunCompletionRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')

        if m.get('ServiceInspection') is not None:
            temp_model = main_models.RunCompletionRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m.get('ServiceInspection'))

        if m.get('Stream') is not None:
            self.stream = m.get('Stream')

        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')

        if m.get('responseFormatType') is not None:
            self.response_format_type = m.get('responseFormatType')

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.RunCompletionRequestVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class RunCompletionRequestVariables(DaraModel):
    def __init__(
        self,
        variable_code: str = None,
        variable_value: str = None,
    ):
        self.variable_code = variable_code
        self.variable_value = variable_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.variable_code is not None:
            result['variableCode'] = self.variable_code

        if self.variable_value is not None:
            result['variableValue'] = self.variable_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('variableCode') is not None:
            self.variable_code = m.get('variableCode')

        if m.get('variableValue') is not None:
            self.variable_value = m.get('variableValue')

        return self

class RunCompletionRequestServiceInspection(DaraModel):
    def __init__(
        self,
        inspection_contents: List[main_models.RunCompletionRequestServiceInspectionInspectionContents] = None,
        inspection_introduction: str = None,
        scene_introduction: str = None,
    ):
        self.inspection_contents = inspection_contents
        self.inspection_introduction = inspection_introduction
        self.scene_introduction = scene_introduction

    def validate(self):
        if self.inspection_contents:
            for v1 in self.inspection_contents:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['InspectionContents'] = []
        if self.inspection_contents is not None:
            for k1 in self.inspection_contents:
                result['InspectionContents'].append(k1.to_map() if k1 else None)

        if self.inspection_introduction is not None:
            result['InspectionIntroduction'] = self.inspection_introduction

        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('InspectionContents') is not None:
            for k1 in m.get('InspectionContents'):
                temp_model = main_models.RunCompletionRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k1))

        if m.get('InspectionIntroduction') is not None:
            self.inspection_introduction = m.get('InspectionIntroduction')

        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')

        return self

class RunCompletionRequestServiceInspectionInspectionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

class RunCompletionRequestFields(DaraModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[main_models.RunCompletionRequestFieldsEnumValues] = None,
        name: str = None,
    ):
        self.code = code
        self.desc = desc
        self.enum_values = enum_values
        # This parameter is required.
        self.name = name

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
        if self.code is not None:
            result['Code'] = self.code

        if self.desc is not None:
            result['Desc'] = self.desc

        result['EnumValues'] = []
        if self.enum_values is not None:
            for k1 in self.enum_values:
                result['EnumValues'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        self.enum_values = []
        if m.get('EnumValues') is not None:
            for k1 in m.get('EnumValues'):
                temp_model = main_models.RunCompletionRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class RunCompletionRequestFieldsEnumValues(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enum_value: str = None,
    ):
        self.desc = desc
        # This parameter is required.
        self.enum_value = enum_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desc is not None:
            result['Desc'] = self.desc

        if self.enum_value is not None:
            result['EnumValue'] = self.enum_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')

        if m.get('EnumValue') is not None:
            self.enum_value = m.get('EnumValue')

        return self

class RunCompletionRequestDialogue(DaraModel):
    def __init__(
        self,
        sentences: List[main_models.RunCompletionRequestDialogueSentences] = None,
        session_id: str = None,
    ):
        self.sentences = sentences
        self.session_id = session_id

    def validate(self):
        if self.sentences:
            for v1 in self.sentences:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Sentences'] = []
        if self.sentences is not None:
            for k1 in self.sentences:
                result['Sentences'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentences = []
        if m.get('Sentences') is not None:
            for k1 in m.get('Sentences'):
                temp_model = main_models.RunCompletionRequestDialogueSentences()
                self.sentences.append(temp_model.from_map(k1))

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        return self

class RunCompletionRequestDialogueSentences(DaraModel):
    def __init__(
        self,
        chat_id: str = None,
        role: str = None,
        text: str = None,
    ):
        self.chat_id = chat_id
        # This parameter is required.
        self.role = role
        # This parameter is required.
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_id is not None:
            result['ChatId'] = self.chat_id

        if self.role is not None:
            result['Role'] = self.role

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatId') is not None:
            self.chat_id = m.get('ChatId')

        if m.get('Role') is not None:
            self.role = m.get('Role')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

