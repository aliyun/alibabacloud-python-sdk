# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class AnalyzeConversationRequest(DaraModel):
    def __init__(
        self,
        category_tags: List[main_models.AnalyzeConversationRequestCategoryTags] = None,
        custom_prompt: str = None,
        dialogue: main_models.AnalyzeConversationRequestDialogue = None,
        examples: List[main_models.AnalyzeConversationRequestExamples] = None,
        fields: List[main_models.AnalyzeConversationRequestFields] = None,
        model_code: str = None,
        response_format_type: str = None,
        result_types: List[str] = None,
        scene_name: str = None,
        service_inspection: main_models.AnalyzeConversationRequestServiceInspection = None,
        source_caller_uid: str = None,
        stream: bool = None,
        time_constraint_list: List[str] = None,
        user_profiles: List[main_models.AnalyzeConversationRequestUserProfiles] = None,
    ):
        self.category_tags = category_tags
        self.custom_prompt = custom_prompt
        self.dialogue = dialogue
        self.examples = examples
        self.fields = fields
        self.model_code = model_code
        self.response_format_type = response_format_type
        # This parameter is required.
        self.result_types = result_types
        self.scene_name = scene_name
        self.service_inspection = service_inspection
        self.source_caller_uid = source_caller_uid
        # This parameter is required.
        self.stream = stream
        self.time_constraint_list = time_constraint_list
        self.user_profiles = user_profiles

    def validate(self):
        if self.category_tags:
            for v1 in self.category_tags:
                 if v1:
                    v1.validate()
        if self.dialogue:
            self.dialogue.validate()
        if self.examples:
            for v1 in self.examples:
                 if v1:
                    v1.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.user_profiles:
            for v1 in self.user_profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['categoryTags'] = []
        if self.category_tags is not None:
            for k1 in self.category_tags:
                result['categoryTags'].append(k1.to_map() if k1 else None)

        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt

        if self.dialogue is not None:
            result['dialogue'] = self.dialogue.to_map()

        result['examples'] = []
        if self.examples is not None:
            for k1 in self.examples:
                result['examples'].append(k1.to_map() if k1 else None)

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.model_code is not None:
            result['modelCode'] = self.model_code

        if self.response_format_type is not None:
            result['responseFormatType'] = self.response_format_type

        if self.result_types is not None:
            result['resultTypes'] = self.result_types

        if self.scene_name is not None:
            result['sceneName'] = self.scene_name

        if self.service_inspection is not None:
            result['serviceInspection'] = self.service_inspection.to_map()

        if self.source_caller_uid is not None:
            result['sourceCallerUid'] = self.source_caller_uid

        if self.stream is not None:
            result['stream'] = self.stream

        if self.time_constraint_list is not None:
            result['timeConstraintList'] = self.time_constraint_list

        result['userProfiles'] = []
        if self.user_profiles is not None:
            for k1 in self.user_profiles:
                result['userProfiles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_tags = []
        if m.get('categoryTags') is not None:
            for k1 in m.get('categoryTags'):
                temp_model = main_models.AnalyzeConversationRequestCategoryTags()
                self.category_tags.append(temp_model.from_map(k1))

        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        if m.get('dialogue') is not None:
            temp_model = main_models.AnalyzeConversationRequestDialogue()
            self.dialogue = temp_model.from_map(m.get('dialogue'))

        self.examples = []
        if m.get('examples') is not None:
            for k1 in m.get('examples'):
                temp_model = main_models.AnalyzeConversationRequestExamples()
                self.examples.append(temp_model.from_map(k1))

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.AnalyzeConversationRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('responseFormatType') is not None:
            self.response_format_type = m.get('responseFormatType')

        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')

        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')

        if m.get('serviceInspection') is not None:
            temp_model = main_models.AnalyzeConversationRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m.get('serviceInspection'))

        if m.get('sourceCallerUid') is not None:
            self.source_caller_uid = m.get('sourceCallerUid')

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('timeConstraintList') is not None:
            self.time_constraint_list = m.get('timeConstraintList')

        self.user_profiles = []
        if m.get('userProfiles') is not None:
            for k1 in m.get('userProfiles'):
                temp_model = main_models.AnalyzeConversationRequestUserProfiles()
                self.user_profiles.append(temp_model.from_map(k1))

        return self

class AnalyzeConversationRequestUserProfiles(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class AnalyzeConversationRequestServiceInspection(DaraModel):
    def __init__(
        self,
        inspection_contents: List[main_models.AnalyzeConversationRequestServiceInspectionInspectionContents] = None,
        inspection_introduction: str = None,
        scene_introduction: str = None,
    ):
        # This parameter is required.
        self.inspection_contents = inspection_contents
        # This parameter is required.
        self.inspection_introduction = inspection_introduction
        # This parameter is required.
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
        result['inspectionContents'] = []
        if self.inspection_contents is not None:
            for k1 in self.inspection_contents:
                result['inspectionContents'].append(k1.to_map() if k1 else None)

        if self.inspection_introduction is not None:
            result['inspectionIntroduction'] = self.inspection_introduction

        if self.scene_introduction is not None:
            result['sceneIntroduction'] = self.scene_introduction

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('inspectionContents') is not None:
            for k1 in m.get('inspectionContents'):
                temp_model = main_models.AnalyzeConversationRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k1))

        if m.get('inspectionIntroduction') is not None:
            self.inspection_introduction = m.get('inspectionIntroduction')

        if m.get('sceneIntroduction') is not None:
            self.scene_introduction = m.get('sceneIntroduction')

        return self

class AnalyzeConversationRequestServiceInspectionInspectionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        # This parameter is required.
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
            result['content'] = self.content

        if self.title is not None:
            result['title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')

        if m.get('title') is not None:
            self.title = m.get('title')

        return self

class AnalyzeConversationRequestFields(DaraModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[main_models.AnalyzeConversationRequestFieldsEnumValues] = None,
        name: str = None,
    ):
        self.code = code
        # This parameter is required.
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
            result['code'] = self.code

        if self.desc is not None:
            result['desc'] = self.desc

        result['enumValues'] = []
        if self.enum_values is not None:
            for k1 in self.enum_values:
                result['enumValues'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('desc') is not None:
            self.desc = m.get('desc')

        self.enum_values = []
        if m.get('enumValues') is not None:
            for k1 in m.get('enumValues'):
                temp_model = main_models.AnalyzeConversationRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class AnalyzeConversationRequestFieldsEnumValues(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enum_value: str = None,
    ):
        # This parameter is required.
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
            result['desc'] = self.desc

        if self.enum_value is not None:
            result['enumValue'] = self.enum_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('desc') is not None:
            self.desc = m.get('desc')

        if m.get('enumValue') is not None:
            self.enum_value = m.get('enumValue')

        return self

class AnalyzeConversationRequestExamples(DaraModel):
    def __init__(
        self,
        output: str = None,
        sentences: List[main_models.AnalyzeConversationRequestExamplesSentences] = None,
    ):
        # This parameter is required.
        self.output = output
        # This parameter is required.
        self.sentences = sentences

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
        if self.output is not None:
            result['output'] = self.output

        result['sentences'] = []
        if self.sentences is not None:
            for k1 in self.sentences:
                result['sentences'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')

        self.sentences = []
        if m.get('sentences') is not None:
            for k1 in m.get('sentences'):
                temp_model = main_models.AnalyzeConversationRequestExamplesSentences()
                self.sentences.append(temp_model.from_map(k1))

        return self

class AnalyzeConversationRequestExamplesSentences(DaraModel):
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
            result['chatId'] = self.chat_id

        if self.role is not None:
            result['role'] = self.role

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chatId') is not None:
            self.chat_id = m.get('chatId')

        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class AnalyzeConversationRequestDialogue(DaraModel):
    def __init__(
        self,
        sentences: List[main_models.AnalyzeConversationRequestDialogueSentences] = None,
        session_id: str = None,
    ):
        # This parameter is required.
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
        result['sentences'] = []
        if self.sentences is not None:
            for k1 in self.sentences:
                result['sentences'].append(k1.to_map() if k1 else None)

        if self.session_id is not None:
            result['sessionId'] = self.session_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentences = []
        if m.get('sentences') is not None:
            for k1 in m.get('sentences'):
                temp_model = main_models.AnalyzeConversationRequestDialogueSentences()
                self.sentences.append(temp_model.from_map(k1))

        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        return self

class AnalyzeConversationRequestDialogueSentences(DaraModel):
    def __init__(
        self,
        role: str = None,
        text: str = None,
    ):
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
        if self.role is not None:
            result['role'] = self.role

        if self.text is not None:
            result['text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role') is not None:
            self.role = m.get('role')

        if m.get('text') is not None:
            self.text = m.get('text')

        return self

class AnalyzeConversationRequestCategoryTags(DaraModel):
    def __init__(
        self,
        tag_desc: str = None,
        tag_name: str = None,
    ):
        self.tag_desc = tag_desc
        self.tag_name = tag_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_desc is not None:
            result['tagDesc'] = self.tag_desc

        if self.tag_name is not None:
            result['tagName'] = self.tag_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagDesc') is not None:
            self.tag_desc = m.get('tagDesc')

        if m.get('tagName') is not None:
            self.tag_name = m.get('tagName')

        return self

