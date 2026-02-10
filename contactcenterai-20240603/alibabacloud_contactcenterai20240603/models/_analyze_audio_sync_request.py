# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_contactcenterai20240603 import models as main_models
from darabonba.model import DaraModel

class AnalyzeAudioSyncRequest(DaraModel):
    def __init__(
        self,
        category_tags: List[main_models.AnalyzeAudioSyncRequestCategoryTags] = None,
        custom_prompt: str = None,
        fields: List[main_models.AnalyzeAudioSyncRequestFields] = None,
        model_code: str = None,
        response_format_type: str = None,
        result_types: List[str] = None,
        service_inspection: main_models.AnalyzeAudioSyncRequestServiceInspection = None,
        stream: bool = None,
        template_ids: List[str] = None,
        transcription: main_models.AnalyzeAudioSyncRequestTranscription = None,
        variables: List[main_models.AnalyzeAudioSyncRequestVariables] = None,
    ):
        self.category_tags = category_tags
        self.custom_prompt = custom_prompt
        self.fields = fields
        self.model_code = model_code
        self.response_format_type = response_format_type
        self.result_types = result_types
        self.service_inspection = service_inspection
        # This parameter is required.
        self.stream = stream
        self.template_ids = template_ids
        self.transcription = transcription
        self.variables = variables

    def validate(self):
        if self.category_tags:
            for v1 in self.category_tags:
                 if v1:
                    v1.validate()
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.transcription:
            self.transcription.validate()
        if self.variables:
            for v1 in self.variables:
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

        if self.service_inspection is not None:
            result['serviceInspection'] = self.service_inspection.to_map()

        if self.stream is not None:
            result['stream'] = self.stream

        if self.template_ids is not None:
            result['templateIds'] = self.template_ids

        if self.transcription is not None:
            result['transcription'] = self.transcription.to_map()

        result['variables'] = []
        if self.variables is not None:
            for k1 in self.variables:
                result['variables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_tags = []
        if m.get('categoryTags') is not None:
            for k1 in m.get('categoryTags'):
                temp_model = main_models.AnalyzeAudioSyncRequestCategoryTags()
                self.category_tags.append(temp_model.from_map(k1))

        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.AnalyzeAudioSyncRequestFields()
                self.fields.append(temp_model.from_map(k1))

        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')

        if m.get('responseFormatType') is not None:
            self.response_format_type = m.get('responseFormatType')

        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')

        if m.get('serviceInspection') is not None:
            temp_model = main_models.AnalyzeAudioSyncRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m.get('serviceInspection'))

        if m.get('stream') is not None:
            self.stream = m.get('stream')

        if m.get('templateIds') is not None:
            self.template_ids = m.get('templateIds')

        if m.get('transcription') is not None:
            temp_model = main_models.AnalyzeAudioSyncRequestTranscription()
            self.transcription = temp_model.from_map(m.get('transcription'))

        self.variables = []
        if m.get('variables') is not None:
            for k1 in m.get('variables'):
                temp_model = main_models.AnalyzeAudioSyncRequestVariables()
                self.variables.append(temp_model.from_map(k1))

        return self

class AnalyzeAudioSyncRequestVariables(DaraModel):
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

class AnalyzeAudioSyncRequestTranscription(DaraModel):
    def __init__(
        self,
        asr_model_code: str = None,
        auto_split: int = None,
        client_channel: int = None,
        file_name: str = None,
        level: str = None,
        service_channel: int = None,
        service_channel_keywords: List[str] = None,
        vocabulary_id: str = None,
        voice_file_url: str = None,
    ):
        self.asr_model_code = asr_model_code
        self.auto_split = auto_split
        self.client_channel = client_channel
        # This parameter is required.
        self.file_name = file_name
        self.level = level
        self.service_channel = service_channel
        self.service_channel_keywords = service_channel_keywords
        self.vocabulary_id = vocabulary_id
        # This parameter is required.
        self.voice_file_url = voice_file_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_model_code is not None:
            result['asrModelCode'] = self.asr_model_code

        if self.auto_split is not None:
            result['autoSplit'] = self.auto_split

        if self.client_channel is not None:
            result['clientChannel'] = self.client_channel

        if self.file_name is not None:
            result['fileName'] = self.file_name

        if self.level is not None:
            result['level'] = self.level

        if self.service_channel is not None:
            result['serviceChannel'] = self.service_channel

        if self.service_channel_keywords is not None:
            result['serviceChannelKeywords'] = self.service_channel_keywords

        if self.vocabulary_id is not None:
            result['vocabularyId'] = self.vocabulary_id

        if self.voice_file_url is not None:
            result['voiceFileUrl'] = self.voice_file_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('asrModelCode') is not None:
            self.asr_model_code = m.get('asrModelCode')

        if m.get('autoSplit') is not None:
            self.auto_split = m.get('autoSplit')

        if m.get('clientChannel') is not None:
            self.client_channel = m.get('clientChannel')

        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')

        if m.get('level') is not None:
            self.level = m.get('level')

        if m.get('serviceChannel') is not None:
            self.service_channel = m.get('serviceChannel')

        if m.get('serviceChannelKeywords') is not None:
            self.service_channel_keywords = m.get('serviceChannelKeywords')

        if m.get('vocabularyId') is not None:
            self.vocabulary_id = m.get('vocabularyId')

        if m.get('voiceFileUrl') is not None:
            self.voice_file_url = m.get('voiceFileUrl')

        return self

class AnalyzeAudioSyncRequestServiceInspection(DaraModel):
    def __init__(
        self,
        inspection_contents: List[main_models.AnalyzeAudioSyncRequestServiceInspectionInspectionContents] = None,
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
                temp_model = main_models.AnalyzeAudioSyncRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k1))

        if m.get('inspectionIntroduction') is not None:
            self.inspection_introduction = m.get('inspectionIntroduction')

        if m.get('sceneIntroduction') is not None:
            self.scene_introduction = m.get('sceneIntroduction')

        return self

class AnalyzeAudioSyncRequestServiceInspectionInspectionContents(DaraModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
    ):
        self.content = content
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

class AnalyzeAudioSyncRequestFields(DaraModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[main_models.AnalyzeAudioSyncRequestFieldsEnumValues] = None,
        name: str = None,
    ):
        self.code = code
        self.desc = desc
        self.enum_values = enum_values
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
                temp_model = main_models.AnalyzeAudioSyncRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k1))

        if m.get('name') is not None:
            self.name = m.get('name')

        return self

class AnalyzeAudioSyncRequestFieldsEnumValues(DaraModel):
    def __init__(
        self,
        desc: str = None,
        enum_value: str = None,
    ):
        self.desc = desc
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



class AnalyzeAudioSyncRequestCategoryTags(DaraModel):
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

