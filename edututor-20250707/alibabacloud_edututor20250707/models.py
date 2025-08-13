# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict


class AnswerSSERequestMessages(TeaModel):
    def __init__(
        self,
        content: List[Dict[str, str]] = None,
        role: str = None,
    ):
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
            result['content'] = self.content
        if self.role is not None:
            result['role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('role') is not None:
            self.role = m.get('role')
        return self


class AnswerSSERequestParameters(TeaModel):
    def __init__(
        self,
        grade: int = None,
        stage: str = None,
        subject: str = None,
    ):
        self.grade = grade
        self.stage = stage
        self.subject = subject

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.grade is not None:
            result['grade'] = self.grade
        if self.stage is not None:
            result['stage'] = self.stage
        if self.subject is not None:
            result['subject'] = self.subject
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('grade') is not None:
            self.grade = m.get('grade')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        if m.get('subject') is not None:
            self.subject = m.get('subject')
        return self


class AnswerSSERequest(TeaModel):
    def __init__(
        self,
        messages: List[AnswerSSERequestMessages] = None,
        parameters: AnswerSSERequestParameters = None,
        workspace_id: str = None,
    ):
        self.messages = messages
        self.parameters = parameters
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['messages'].append(k.to_map() if k else None)
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('messages') is not None:
            for k in m.get('messages'):
                temp_model = AnswerSSERequestMessages()
                self.messages.append(temp_model.from_map(k))
        if m.get('parameters') is not None:
            temp_model = AnswerSSERequestParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class AnswerSSEResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        finish_reason: str = None,
        http_status_code: int = None,
        input_tokens: int = None,
        message: str = None,
        output_tokens: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.finish_reason = finish_reason
        self.http_status_code = http_status_code
        self.input_tokens = input_tokens
        self.message = message
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.finish_reason is not None:
            result['finish_reason'] = self.finish_reason
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens
        if self.message is not None:
            result['message'] = self.message
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('finish_reason') is not None:
            self.finish_reason = m.get('finish_reason')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class AnswerSSEResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AnswerSSEResponseBody = None,
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
            temp_model = AnswerSSEResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CutQuestionsRequestParameters(TeaModel):
    def __init__(
        self,
        extract_images: bool = None,
        struct: bool = None,
    ):
        # This parameter is required.
        self.extract_images = extract_images
        # This parameter is required.
        self.struct = struct

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extract_images is not None:
            result['extract_images'] = self.extract_images
        if self.struct is not None:
            result['struct'] = self.struct
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extract_images') is not None:
            self.extract_images = m.get('extract_images')
        if m.get('struct') is not None:
            self.struct = m.get('struct')
        return self


class CutQuestionsRequest(TeaModel):
    def __init__(
        self,
        image: str = None,
        parameters: CutQuestionsRequestParameters = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.image = image
        # This parameter is required.
        self.parameters = parameters
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image is not None:
            result['image'] = self.image
        if self.parameters is not None:
            result['parameters'] = self.parameters.to_map()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image') is not None:
            self.image = m.get('image')
        if m.get('parameters') is not None:
            temp_model = CutQuestionsRequestParameters()
            self.parameters = temp_model.from_map(m['parameters'])
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CutQuestionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        input_tokens: int = None,
        message: str = None,
        output_tokens: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.input_tokens = input_tokens
        self.message = message
        self.output_tokens = output_tokens
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.input_tokens is not None:
            result['input_tokens'] = self.input_tokens
        if self.message is not None:
            result['message'] = self.message
        if self.output_tokens is not None:
            result['output_tokens'] = self.output_tokens
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('input_tokens') is not None:
            self.input_tokens = m.get('input_tokens')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('output_tokens') is not None:
            self.output_tokens = m.get('output_tokens')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CutQuestionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CutQuestionsResponseBody = None,
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
            temp_model = CutQuestionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


