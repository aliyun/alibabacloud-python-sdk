# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AnalyzeConversationRequestCategoryTags(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequestDialogueSentences(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequestDialogue(TeaModel):
    def __init__(
        self,
        sentences: List[AnalyzeConversationRequestDialogueSentences] = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.sentences = sentences
        self.session_id = session_id

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['sentences'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentences = []
        if m.get('sentences') is not None:
            for k in m.get('sentences'):
                temp_model = AnalyzeConversationRequestDialogueSentences()
                self.sentences.append(temp_model.from_map(k))
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class AnalyzeConversationRequestExamplesSentences(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequestExamples(TeaModel):
    def __init__(
        self,
        output: str = None,
        sentences: List[AnalyzeConversationRequestExamplesSentences] = None,
    ):
        # This parameter is required.
        self.output = output
        # This parameter is required.
        self.sentences = sentences

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        result['sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['sentences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        self.sentences = []
        if m.get('sentences') is not None:
            for k in m.get('sentences'):
                temp_model = AnalyzeConversationRequestExamplesSentences()
                self.sentences.append(temp_model.from_map(k))
        return self


class AnalyzeConversationRequestFieldsEnumValues(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequestFields(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[AnalyzeConversationRequestFieldsEnumValues] = None,
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
            for k in self.enum_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.desc is not None:
            result['desc'] = self.desc
        result['enumValues'] = []
        if self.enum_values is not None:
            for k in self.enum_values:
                result['enumValues'].append(k.to_map() if k else None)
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
            for k in m.get('enumValues'):
                temp_model = AnalyzeConversationRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class AnalyzeConversationRequestServiceInspectionInspectionContents(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequestServiceInspection(TeaModel):
    def __init__(
        self,
        inspection_contents: List[AnalyzeConversationRequestServiceInspectionInspectionContents] = None,
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
            for k in self.inspection_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['inspectionContents'] = []
        if self.inspection_contents is not None:
            for k in self.inspection_contents:
                result['inspectionContents'].append(k.to_map() if k else None)
        if self.inspection_introduction is not None:
            result['inspectionIntroduction'] = self.inspection_introduction
        if self.scene_introduction is not None:
            result['sceneIntroduction'] = self.scene_introduction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('inspectionContents') is not None:
            for k in m.get('inspectionContents'):
                temp_model = AnalyzeConversationRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k))
        if m.get('inspectionIntroduction') is not None:
            self.inspection_introduction = m.get('inspectionIntroduction')
        if m.get('sceneIntroduction') is not None:
            self.scene_introduction = m.get('sceneIntroduction')
        return self


class AnalyzeConversationRequestUserProfiles(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class AnalyzeConversationRequest(TeaModel):
    def __init__(
        self,
        category_tags: List[AnalyzeConversationRequestCategoryTags] = None,
        custom_prompt: str = None,
        dialogue: AnalyzeConversationRequestDialogue = None,
        examples: List[AnalyzeConversationRequestExamples] = None,
        fields: List[AnalyzeConversationRequestFields] = None,
        model_code: str = None,
        result_types: List[str] = None,
        scene_name: str = None,
        service_inspection: AnalyzeConversationRequestServiceInspection = None,
        source_caller_uid: str = None,
        stream: bool = None,
        time_constraint_list: List[str] = None,
        user_profiles: List[AnalyzeConversationRequestUserProfiles] = None,
    ):
        self.category_tags = category_tags
        self.custom_prompt = custom_prompt
        self.dialogue = dialogue
        self.examples = examples
        self.fields = fields
        self.model_code = model_code
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
            for k in self.category_tags:
                if k:
                    k.validate()
        if self.dialogue:
            self.dialogue.validate()
        if self.examples:
            for k in self.examples:
                if k:
                    k.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.user_profiles:
            for k in self.user_profiles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['categoryTags'] = []
        if self.category_tags is not None:
            for k in self.category_tags:
                result['categoryTags'].append(k.to_map() if k else None)
        if self.custom_prompt is not None:
            result['customPrompt'] = self.custom_prompt
        if self.dialogue is not None:
            result['dialogue'] = self.dialogue.to_map()
        result['examples'] = []
        if self.examples is not None:
            for k in self.examples:
                result['examples'].append(k.to_map() if k else None)
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.model_code is not None:
            result['modelCode'] = self.model_code
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
            for k in self.user_profiles:
                result['userProfiles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.category_tags = []
        if m.get('categoryTags') is not None:
            for k in m.get('categoryTags'):
                temp_model = AnalyzeConversationRequestCategoryTags()
                self.category_tags.append(temp_model.from_map(k))
        if m.get('customPrompt') is not None:
            self.custom_prompt = m.get('customPrompt')
        if m.get('dialogue') is not None:
            temp_model = AnalyzeConversationRequestDialogue()
            self.dialogue = temp_model.from_map(m['dialogue'])
        self.examples = []
        if m.get('examples') is not None:
            for k in m.get('examples'):
                temp_model = AnalyzeConversationRequestExamples()
                self.examples.append(temp_model.from_map(k))
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = AnalyzeConversationRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')
        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')
        if m.get('sceneName') is not None:
            self.scene_name = m.get('sceneName')
        if m.get('serviceInspection') is not None:
            temp_model = AnalyzeConversationRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m['serviceInspection'])
        if m.get('sourceCallerUid') is not None:
            self.source_caller_uid = m.get('sourceCallerUid')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        if m.get('timeConstraintList') is not None:
            self.time_constraint_list = m.get('timeConstraintList')
        self.user_profiles = []
        if m.get('userProfiles') is not None:
            for k in m.get('userProfiles'):
                temp_model = AnalyzeConversationRequestUserProfiles()
                self.user_profiles.append(temp_model.from_map(k))
        return self


class AnalyzeConversationResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_info: str = None,
        finish_reason: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        request_id: str = None,
        success: bool = None,
        text: str = None,
        total_tokens: str = None,
    ):
        self.error_code = error_code
        self.error_info = error_info
        self.finish_reason = finish_reason
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success
        self.text = text
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_info is not None:
            result['errorInfo'] = self.error_info
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.text is not None:
            result['text'] = self.text
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorInfo') is not None:
            self.error_info = m.get('errorInfo')
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class AnalyzeConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnalyzeConversationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AnalyzeConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AnalyzeImageRequest(TeaModel):
    def __init__(
        self,
        image_urls: List[str] = None,
        result_types: List[str] = None,
        stream: bool = None,
    ):
        self.image_urls = image_urls
        self.result_types = result_types
        # This parameter is required.
        self.stream = stream

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_urls is not None:
            result['imageUrls'] = self.image_urls
        if self.result_types is not None:
            result['resultTypes'] = self.result_types
        if self.stream is not None:
            result['stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('imageUrls') is not None:
            self.image_urls = m.get('imageUrls')
        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')
        if m.get('stream') is not None:
            self.stream = m.get('stream')
        return self


class AnalyzeImageResponseBody(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        request_id: str = None,
        success: bool = None,
        text: str = None,
        total_tokens: str = None,
    ):
        self.finish_reason = finish_reason
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success
        self.text = text
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['finishReason'] = self.finish_reason
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        if self.text is not None:
            result['text'] = self.text
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('finishReason') is not None:
            self.finish_reason = m.get('finishReason')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class AnalyzeImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnalyzeImageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AnalyzeImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequestDialogueSentences(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateTaskRequestDialogue(TeaModel):
    def __init__(
        self,
        sentences: List[CreateTaskRequestDialogueSentences] = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.sentences = sentences
        self.session_id = session_id

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['sentences'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentences = []
        if m.get('sentences') is not None:
            for k in m.get('sentences'):
                temp_model = CreateTaskRequestDialogueSentences()
                self.sentences.append(temp_model.from_map(k))
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CreateTaskRequestExamplesSentences(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateTaskRequestExamples(TeaModel):
    def __init__(
        self,
        output: str = None,
        sentences: List[CreateTaskRequestExamplesSentences] = None,
    ):
        self.output = output
        # This parameter is required.
        self.sentences = sentences

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['output'] = self.output
        result['sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['sentences'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('output') is not None:
            self.output = m.get('output')
        self.sentences = []
        if m.get('sentences') is not None:
            for k in m.get('sentences'):
                temp_model = CreateTaskRequestExamplesSentences()
                self.sentences.append(temp_model.from_map(k))
        return self


class CreateTaskRequestFieldsEnumValues(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateTaskRequestFields(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[CreateTaskRequestFieldsEnumValues] = None,
        name: str = None,
    ):
        self.code = code
        # This parameter is required.
        self.desc = desc
        # This parameter is required.
        self.enum_values = enum_values
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.enum_values:
            for k in self.enum_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.desc is not None:
            result['desc'] = self.desc
        result['enumValues'] = []
        if self.enum_values is not None:
            for k in self.enum_values:
                result['enumValues'].append(k.to_map() if k else None)
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
            for k in m.get('enumValues'):
                temp_model = CreateTaskRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateTaskRequestServiceInspectionInspectionContents(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateTaskRequestServiceInspection(TeaModel):
    def __init__(
        self,
        inspection_contents: List[CreateTaskRequestServiceInspectionInspectionContents] = None,
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
            for k in self.inspection_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['inspectionContents'] = []
        if self.inspection_contents is not None:
            for k in self.inspection_contents:
                result['inspectionContents'].append(k.to_map() if k else None)
        if self.inspection_introduction is not None:
            result['inspectionIntroduction'] = self.inspection_introduction
        if self.scene_introduction is not None:
            result['sceneIntroduction'] = self.scene_introduction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('inspectionContents') is not None:
            for k in m.get('inspectionContents'):
                temp_model = CreateTaskRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k))
        if m.get('inspectionIntroduction') is not None:
            self.inspection_introduction = m.get('inspectionIntroduction')
        if m.get('sceneIntroduction') is not None:
            self.scene_introduction = m.get('sceneIntroduction')
        return self


class CreateTaskRequestTranscription(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        dialogue: CreateTaskRequestDialogue = None,
        examples: CreateTaskRequestExamples = None,
        fields: List[CreateTaskRequestFields] = None,
        model_code: str = None,
        result_types: List[str] = None,
        service_inspection: CreateTaskRequestServiceInspection = None,
        task_type: str = None,
        template_ids: List[str] = None,
        transcription: CreateTaskRequestTranscription = None,
    ):
        self.dialogue = dialogue
        self.examples = examples
        self.fields = fields
        # This parameter is required.
        self.model_code = model_code
        self.result_types = result_types
        self.service_inspection = service_inspection
        # This parameter is required.
        self.task_type = task_type
        self.template_ids = template_ids
        self.transcription = transcription

    def validate(self):
        if self.dialogue:
            self.dialogue.validate()
        if self.examples:
            self.examples.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.service_inspection:
            self.service_inspection.validate()
        if self.transcription:
            self.transcription.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue is not None:
            result['dialogue'] = self.dialogue.to_map()
        if self.examples is not None:
            result['examples'] = self.examples.to_map()
        result['fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['fields'].append(k.to_map() if k else None)
        if self.model_code is not None:
            result['modelCode'] = self.model_code
        if self.result_types is not None:
            result['resultTypes'] = self.result_types
        if self.service_inspection is not None:
            result['serviceInspection'] = self.service_inspection.to_map()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.template_ids is not None:
            result['templateIds'] = self.template_ids
        if self.transcription is not None:
            result['transcription'] = self.transcription.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dialogue') is not None:
            temp_model = CreateTaskRequestDialogue()
            self.dialogue = temp_model.from_map(m['dialogue'])
        if m.get('examples') is not None:
            temp_model = CreateTaskRequestExamples()
            self.examples = temp_model.from_map(m['examples'])
        self.fields = []
        if m.get('fields') is not None:
            for k in m.get('fields'):
                temp_model = CreateTaskRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('modelCode') is not None:
            self.model_code = m.get('modelCode')
        if m.get('resultTypes') is not None:
            self.result_types = m.get('resultTypes')
        if m.get('serviceInspection') is not None:
            temp_model = CreateTaskRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m['serviceInspection'])
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('templateIds') is not None:
            self.template_ids = m.get('templateIds')
        if m.get('transcription') is not None:
            temp_model = CreateTaskRequestTranscription()
            self.transcription = temp_model.from_map(m['transcription'])
        return self


class CreateTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateTaskResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateTaskResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResultRequest(TeaModel):
    def __init__(
        self,
        required_field_list: List[str] = None,
        task_id: str = None,
    ):
        self.required_field_list = required_field_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_field_list is not None:
            result['requiredFieldList'] = self.required_field_list
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredFieldList') is not None:
            self.required_field_list = m.get('requiredFieldList')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResultShrinkRequest(TeaModel):
    def __init__(
        self,
        required_field_list_shrink: str = None,
        task_id: str = None,
    ):
        self.required_field_list_shrink = required_field_list_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.required_field_list_shrink is not None:
            result['requiredFieldList'] = self.required_field_list_shrink
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requiredFieldList') is not None:
            self.required_field_list_shrink = m.get('requiredFieldList')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class GetTaskResultResponseBodyDataAsrResult(TeaModel):
    def __init__(
        self,
        begin: int = None,
        emotion_value: int = None,
        end: int = None,
        role: str = None,
        speech_rate: int = None,
        words: str = None,
    ):
        self.begin = begin
        self.emotion_value = emotion_value
        self.end = end
        self.role = role
        self.speech_rate = speech_rate
        self.words = words

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.begin is not None:
            result['begin'] = self.begin
        if self.emotion_value is not None:
            result['emotionValue'] = self.emotion_value
        if self.end is not None:
            result['end'] = self.end
        if self.role is not None:
            result['role'] = self.role
        if self.speech_rate is not None:
            result['speechRate'] = self.speech_rate
        if self.words is not None:
            result['words'] = self.words
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('begin') is not None:
            self.begin = m.get('begin')
        if m.get('emotionValue') is not None:
            self.emotion_value = m.get('emotionValue')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('speechRate') is not None:
            self.speech_rate = m.get('speechRate')
        if m.get('words') is not None:
            self.words = m.get('words')
        return self


class GetTaskResultResponseBodyData(TeaModel):
    def __init__(
        self,
        asr_result: List[GetTaskResultResponseBodyDataAsrResult] = None,
        extra: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_status: str = None,
        text: str = None,
    ):
        self.asr_result = asr_result
        self.extra = extra
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_status = task_status
        self.text = text

    def validate(self):
        if self.asr_result:
            for k in self.asr_result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['asrResult'] = []
        if self.asr_result is not None:
            for k in self.asr_result:
                result['asrResult'].append(k.to_map() if k else None)
        if self.extra is not None:
            result['extra'] = self.extra
        if self.task_error_message is not None:
            result['taskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_status is not None:
            result['taskStatus'] = self.task_status
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.asr_result = []
        if m.get('asrResult') is not None:
            for k in m.get('asrResult'):
                temp_model = GetTaskResultResponseBodyDataAsrResult()
                self.asr_result.append(temp_model.from_map(k))
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('taskErrorMessage') is not None:
            self.task_error_message = m.get('taskErrorMessage')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskStatus') is not None:
            self.task_status = m.get('taskStatus')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class GetTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        data: GetTaskResultResponseBodyData = None,
        request_id: str = None,
        success: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetTaskResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCompletionRequestDialogueSentences(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RunCompletionRequestDialogue(TeaModel):
    def __init__(
        self,
        sentences: List[RunCompletionRequestDialogueSentences] = None,
        session_id: str = None,
    ):
        self.sentences = sentences
        self.session_id = session_id

    def validate(self):
        if self.sentences:
            for k in self.sentences:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Sentences'] = []
        if self.sentences is not None:
            for k in self.sentences:
                result['Sentences'].append(k.to_map() if k else None)
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.sentences = []
        if m.get('Sentences') is not None:
            for k in m.get('Sentences'):
                temp_model = RunCompletionRequestDialogueSentences()
                self.sentences.append(temp_model.from_map(k))
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class RunCompletionRequestFieldsEnumValues(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RunCompletionRequestFields(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enum_values: List[RunCompletionRequestFieldsEnumValues] = None,
        name: str = None,
    ):
        self.code = code
        self.desc = desc
        self.enum_values = enum_values
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.enum_values:
            for k in self.enum_values:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desc is not None:
            result['Desc'] = self.desc
        result['EnumValues'] = []
        if self.enum_values is not None:
            for k in self.enum_values:
                result['EnumValues'].append(k.to_map() if k else None)
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
            for k in m.get('EnumValues'):
                temp_model = RunCompletionRequestFieldsEnumValues()
                self.enum_values.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RunCompletionRequestServiceInspectionInspectionContents(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
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


class RunCompletionRequestServiceInspection(TeaModel):
    def __init__(
        self,
        inspection_contents: List[RunCompletionRequestServiceInspectionInspectionContents] = None,
        inspection_introduction: str = None,
        scene_introduction: str = None,
    ):
        self.inspection_contents = inspection_contents
        self.inspection_introduction = inspection_introduction
        self.scene_introduction = scene_introduction

    def validate(self):
        if self.inspection_contents:
            for k in self.inspection_contents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InspectionContents'] = []
        if self.inspection_contents is not None:
            for k in self.inspection_contents:
                result['InspectionContents'].append(k.to_map() if k else None)
        if self.inspection_introduction is not None:
            result['InspectionIntroduction'] = self.inspection_introduction
        if self.scene_introduction is not None:
            result['SceneIntroduction'] = self.scene_introduction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.inspection_contents = []
        if m.get('InspectionContents') is not None:
            for k in m.get('InspectionContents'):
                temp_model = RunCompletionRequestServiceInspectionInspectionContents()
                self.inspection_contents.append(temp_model.from_map(k))
        if m.get('InspectionIntroduction') is not None:
            self.inspection_introduction = m.get('InspectionIntroduction')
        if m.get('SceneIntroduction') is not None:
            self.scene_introduction = m.get('SceneIntroduction')
        return self


class RunCompletionRequest(TeaModel):
    def __init__(
        self,
        dialogue: RunCompletionRequestDialogue = None,
        fields: List[RunCompletionRequestFields] = None,
        model_code: str = None,
        service_inspection: RunCompletionRequestServiceInspection = None,
        stream: bool = None,
        template_ids: List[int] = None,
    ):
        # This parameter is required.
        self.dialogue = dialogue
        self.fields = fields
        self.model_code = model_code
        self.service_inspection = service_inspection
        self.stream = stream
        # This parameter is required.
        self.template_ids = template_ids

    def validate(self):
        if self.dialogue:
            self.dialogue.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()
        if self.service_inspection:
            self.service_inspection.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue is not None:
            result['Dialogue'] = self.dialogue.to_map()
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.model_code is not None:
            result['ModelCode'] = self.model_code
        if self.service_inspection is not None:
            result['ServiceInspection'] = self.service_inspection.to_map()
        if self.stream is not None:
            result['Stream'] = self.stream
        if self.template_ids is not None:
            result['TemplateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dialogue') is not None:
            temp_model = RunCompletionRequestDialogue()
            self.dialogue = temp_model.from_map(m['Dialogue'])
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = RunCompletionRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')
        if m.get('ServiceInspection') is not None:
            temp_model = RunCompletionRequestServiceInspection()
            self.service_inspection = temp_model.from_map(m['ServiceInspection'])
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        if m.get('TemplateIds') is not None:
            self.template_ids = m.get('TemplateIds')
        return self


class RunCompletionResponseBody(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        request_id: str = None,
        text: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        total_tokens: str = None,
    ):
        self.finish_reason = finish_reason
        self.request_id = request_id
        self.text = text
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text is not None:
            result['Text'] = self.text
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunCompletionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCompletionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunCompletionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCompletionMessageRequestMessages(TeaModel):
    def __init__(
        self,
        content: str = None,
        role: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class RunCompletionMessageRequest(TeaModel):
    def __init__(
        self,
        messages: List[RunCompletionMessageRequestMessages] = None,
        model_code: str = None,
        stream: bool = None,
    ):
        # This parameter is required.
        self.messages = messages
        self.model_code = model_code
        self.stream = stream

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        if self.model_code is not None:
            result['ModelCode'] = self.model_code
        if self.stream is not None:
            result['Stream'] = self.stream
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = RunCompletionMessageRequestMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')
        if m.get('Stream') is not None:
            self.stream = m.get('Stream')
        return self


class RunCompletionMessageResponseBody(TeaModel):
    def __init__(
        self,
        finish_reason: str = None,
        request_id: str = None,
        text: str = None,
        input_tokens: str = None,
        output_tokens: str = None,
        total_tokens: str = None,
    ):
        self.finish_reason = finish_reason
        self.request_id = request_id
        self.text = text
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.finish_reason is not None:
            result['FinishReason'] = self.finish_reason
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.text is not None:
            result['Text'] = self.text
        if self.input_tokens is not None:
            result['inputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['outputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['totalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('inputTokens') is not None:
            self.input_tokens = m.get('inputTokens')
        if m.get('outputTokens') is not None:
            self.output_tokens = m.get('outputTokens')
        if m.get('totalTokens') is not None:
            self.total_tokens = m.get('totalTokens')
        return self


class RunCompletionMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCompletionMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunCompletionMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


