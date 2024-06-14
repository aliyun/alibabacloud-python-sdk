# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


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


class RunCompletionRequestDimensions(TeaModel):
    def __init__(
        self,
        desc: str = None,
        name: str = None,
    ):
        self.desc = desc
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RunCompletionRequestFields(TeaModel):
    def __init__(
        self,
        code: str = None,
        desc: str = None,
        enums: List[str] = None,
        name: str = None,
    ):
        self.code = code
        self.desc = desc
        self.enums = enums
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.desc is not None:
            result['Desc'] = self.desc
        if self.enums is not None:
            result['Enums'] = self.enums
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Desc') is not None:
            self.desc = m.get('Desc')
        if m.get('Enums') is not None:
            self.enums = m.get('Enums')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class RunCompletionRequest(TeaModel):
    def __init__(
        self,
        dialogue: RunCompletionRequestDialogue = None,
        dimensions: List[RunCompletionRequestDimensions] = None,
        fields: List[RunCompletionRequestFields] = None,
        model_code: str = None,
        stream: bool = None,
        template_ids: List[int] = None,
    ):
        # This parameter is required.
        self.dialogue = dialogue
        self.dimensions = dimensions
        self.fields = fields
        self.model_code = model_code
        self.stream = stream
        # This parameter is required.
        self.template_ids = template_ids

    def validate(self):
        if self.dialogue:
            self.dialogue.validate()
        if self.dimensions:
            for k in self.dimensions:
                if k:
                    k.validate()
        if self.fields:
            for k in self.fields:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dialogue is not None:
            result['Dialogue'] = self.dialogue.to_map()
        result['Dimensions'] = []
        if self.dimensions is not None:
            for k in self.dimensions:
                result['Dimensions'].append(k.to_map() if k else None)
        result['Fields'] = []
        if self.fields is not None:
            for k in self.fields:
                result['Fields'].append(k.to_map() if k else None)
        if self.model_code is not None:
            result['ModelCode'] = self.model_code
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
        self.dimensions = []
        if m.get('Dimensions') is not None:
            for k in m.get('Dimensions'):
                temp_model = RunCompletionRequestDimensions()
                self.dimensions.append(temp_model.from_map(k))
        self.fields = []
        if m.get('Fields') is not None:
            for k in m.get('Fields'):
                temp_model = RunCompletionRequestFields()
                self.fields.append(temp_model.from_map(k))
        if m.get('ModelCode') is not None:
            self.model_code = m.get('ModelCode')
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
    ):
        self.finish_reason = finish_reason
        self.request_id = request_id
        self.text = text

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
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
    ):
        self.finish_reason = finish_reason
        self.request_id = request_id
        self.text = text

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FinishReason') is not None:
            self.finish_reason = m.get('FinishReason')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
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


