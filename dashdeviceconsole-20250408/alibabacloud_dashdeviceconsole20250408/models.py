# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, Dict


class GetPromptRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        return self


class GetPromptResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetPromptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPromptResponseBody = None,
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
            temp_model = GetPromptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushPromptRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        prompt_content: str = None,
    ):
        self.group_id = group_id
        self.prompt_content = prompt_content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.prompt_content is not None:
            result['promptContent'] = self.prompt_content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('promptContent') is not None:
            self.prompt_content = m.get('promptContent')
        return self


class PushPromptResponseBody(TeaModel):
    def __init__(
        self,
        data: Any = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        status_code: int = None,
    ):
        self.data = data
        self.error_code = error_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['data'] = self.data
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class PushPromptResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushPromptResponseBody = None,
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
            temp_model = PushPromptResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


