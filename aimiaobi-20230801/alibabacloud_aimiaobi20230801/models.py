# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CancelAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CancelAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelAsyncTaskResponseBody = None,
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
            temp_model = CancelAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ClearIntervenesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ClearIntervenesResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_id_list: List[str] = None,
        task_id: str = None,
    ):
        self.fail_id_list = fail_id_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ClearIntervenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ClearIntervenesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ClearIntervenesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ClearIntervenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClearIntervenesResponseBody = None,
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
            temp_model = ClearIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGeneratedContentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        keywords: List[str] = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.keywords = keywords
        self.prompt = prompt
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.title = title
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CreateGeneratedContentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        keywords_shrink: str = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        uuid: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.keywords_shrink = keywords_shrink
        self.prompt = prompt
        # This parameter is required.
        self.task_id = task_id
        # This parameter is required.
        self.title = title
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CreateGeneratedContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateGeneratedContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGeneratedContentResponseBody = None,
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
            temp_model = CreateGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTokenRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class CreateTokenResponseBodyData(TeaModel):
    def __init__(
        self,
        expired_time: int = None,
        token: str = None,
    ):
        self.expired_time = expired_time
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time is not None:
            result['ExpiredTime'] = self.expired_time
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTime') is not None:
            self.expired_time = m.get('ExpiredTime')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class CreateTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTokenResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = CreateTokenResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTokenResponseBody = None,
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
            temp_model = CreateTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomTextRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteCustomTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomTextResponseBody = None,
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
            temp_model = DeleteCustomTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomTopicByTopicRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class DeleteCustomTopicByTopicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomTopicByTopicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomTopicByTopicResponseBody = None,
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
            temp_model = DeleteCustomTopicByTopicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteCustomTopicViewPointByIdRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.custom_view_point_id = custom_view_point_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        return self


class DeleteCustomTopicViewPointByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteCustomTopicViewPointByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteCustomTopicViewPointByIdResponseBody = None,
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
            temp_model = DeleteCustomTopicViewPointByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGeneratedContentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteGeneratedContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteGeneratedContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGeneratedContentResponseBody = None,
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
            temp_model = DeleteGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInterveneRuleRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteInterveneRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_id_list: List[str] = None,
        task_id: str = None,
    ):
        self.fail_id_list = fail_id_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class DeleteInterveneRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: DeleteInterveneRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = DeleteInterveneRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteInterveneRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteInterveneRuleResponseBody = None,
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
            temp_model = DeleteInterveneRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteMaterialByIdRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DeleteMaterialByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteMaterialByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteMaterialByIdResponseBody = None,
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
            temp_model = DeleteMaterialByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DocumentExtractionRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        urls: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.urls = urls

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.urls is not None:
            result['Urls'] = self.urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Urls') is not None:
            self.urls = m.get('Urls')
        return self


class DocumentExtractionShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        urls_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.urls_shrink = urls_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.urls_shrink is not None:
            result['Urls'] = self.urls_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Urls') is not None:
            self.urls_shrink = m.get('Urls')
        return self


class DocumentExtractionResponseBodyData(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DocumentExtractionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[DocumentExtractionResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = DocumentExtractionResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DocumentExtractionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DocumentExtractionResponseBody = None,
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
            temp_model = DocumentExtractionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportGeneratedContentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ExportGeneratedContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportGeneratedContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportGeneratedContentResponseBody = None,
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
            temp_model = ExportGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportHotTopicPlanningProposalsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_ids: List[str] = None,
        export_type: str = None,
        titles: List[str] = None,
        topic: str = None,
        topic_source: str = None,
        view_point_type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.custom_view_point_ids = custom_view_point_ids
        self.export_type = export_type
        self.titles = titles
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source
        self.view_point_type = view_point_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.custom_view_point_ids is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.titles is not None:
            result['Titles'] = self.titles
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.view_point_type is not None:
            result['ViewPointType'] = self.view_point_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids = m.get('CustomViewPointIds')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('ViewPointType') is not None:
            self.view_point_type = m.get('ViewPointType')
        return self


class ExportHotTopicPlanningProposalsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_ids_shrink: str = None,
        export_type: str = None,
        titles_shrink: str = None,
        topic: str = None,
        topic_source: str = None,
        view_point_type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.custom_view_point_ids_shrink = custom_view_point_ids_shrink
        self.export_type = export_type
        self.titles_shrink = titles_shrink
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source
        self.view_point_type = view_point_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.custom_view_point_ids_shrink is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids_shrink
        if self.export_type is not None:
            result['ExportType'] = self.export_type
        if self.titles_shrink is not None:
            result['Titles'] = self.titles_shrink
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.view_point_type is not None:
            result['ViewPointType'] = self.view_point_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids_shrink = m.get('CustomViewPointIds')
        if m.get('ExportType') is not None:
            self.export_type = m.get('ExportType')
        if m.get('Titles') is not None:
            self.titles_shrink = m.get('Titles')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('ViewPointType') is not None:
            self.view_point_type = m.get('ViewPointType')
        return self


class ExportHotTopicPlanningProposalsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportHotTopicPlanningProposalsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportHotTopicPlanningProposalsResponseBody = None,
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
            temp_model = ExportHotTopicPlanningProposalsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExportIntervenesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ExportIntervenesResponseBodyData(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ExportIntervenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ExportIntervenesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ExportIntervenesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ExportIntervenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExportIntervenesResponseBody = None,
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
            temp_model = ExportIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FeedbackDialogueRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        customer_response: str = None,
        good_text: str = None,
        modified_response: str = None,
        rating: str = None,
        rating_tags: List[str] = None,
        session_id: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.customer_response = customer_response
        self.good_text = good_text
        self.modified_response = modified_response
        self.rating = rating
        self.rating_tags = rating_tags
        # This parameter is required.
        self.session_id = session_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.customer_response is not None:
            result['CustomerResponse'] = self.customer_response
        if self.good_text is not None:
            result['GoodText'] = self.good_text
        if self.modified_response is not None:
            result['ModifiedResponse'] = self.modified_response
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.rating_tags is not None:
            result['RatingTags'] = self.rating_tags
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomerResponse') is not None:
            self.customer_response = m.get('CustomerResponse')
        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')
        if m.get('ModifiedResponse') is not None:
            self.modified_response = m.get('ModifiedResponse')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('RatingTags') is not None:
            self.rating_tags = m.get('RatingTags')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FeedbackDialogueShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        customer_response: str = None,
        good_text: str = None,
        modified_response: str = None,
        rating: str = None,
        rating_tags_shrink: str = None,
        session_id: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.customer_response = customer_response
        self.good_text = good_text
        self.modified_response = modified_response
        self.rating = rating
        self.rating_tags_shrink = rating_tags_shrink
        # This parameter is required.
        self.session_id = session_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.customer_response is not None:
            result['CustomerResponse'] = self.customer_response
        if self.good_text is not None:
            result['GoodText'] = self.good_text
        if self.modified_response is not None:
            result['ModifiedResponse'] = self.modified_response
        if self.rating is not None:
            result['Rating'] = self.rating
        if self.rating_tags_shrink is not None:
            result['RatingTags'] = self.rating_tags_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomerResponse') is not None:
            self.customer_response = m.get('CustomerResponse')
        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')
        if m.get('ModifiedResponse') is not None:
            self.modified_response = m.get('ModifiedResponse')
        if m.get('Rating') is not None:
            self.rating = m.get('Rating')
        if m.get('RatingTags') is not None:
            self.rating_tags_shrink = m.get('RatingTags')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class FeedbackDialogueResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FeedbackDialogueResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FeedbackDialogueResponseBody = None,
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
            temp_model = FeedbackDialogueResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FetchImageTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        task_id_list: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.task_id_list = task_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.task_id_list is not None:
            result['TaskIdList'] = self.task_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('TaskIdList') is not None:
            self.task_id_list = m.get('TaskIdList')
        return self


class FetchImageTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        task_id_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.task_id_list_shrink = task_id_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.task_id_list_shrink is not None:
            result['TaskIdList'] = self.task_id_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('TaskIdList') is not None:
            self.task_id_list_shrink = m.get('TaskIdList')
        return self


class FetchImageTaskResponseBodyDataTaskInfoListImageList(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        url: str = None,
    ):
        self.code = code
        self.message = message
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class FetchImageTaskResponseBodyDataTaskInfoList(TeaModel):
    def __init__(
        self,
        id: int = None,
        image_list: List[FetchImageTaskResponseBodyDataTaskInfoListImageList] = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.id = id
        self.image_list = image_list
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        if self.image_list:
            for k in self.image_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        result['ImageList'] = []
        if self.image_list is not None:
            for k in self.image_list:
                result['ImageList'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.image_list = []
        if m.get('ImageList') is not None:
            for k in m.get('ImageList'):
                temp_model = FetchImageTaskResponseBodyDataTaskInfoListImageList()
                self.image_list.append(temp_model.from_map(k))
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class FetchImageTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_info_list: List[FetchImageTaskResponseBodyDataTaskInfoList] = None,
    ):
        self.task_info_list = task_info_list

    def validate(self):
        if self.task_info_list:
            for k in self.task_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskInfoList'] = []
        if self.task_info_list is not None:
            for k in self.task_info_list:
                result['TaskInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_info_list = []
        if m.get('TaskInfoList') is not None:
            for k in m.get('TaskInfoList'):
                temp_model = FetchImageTaskResponseBodyDataTaskInfoList()
                self.task_info_list.append(temp_model.from_map(k))
        return self


class FetchImageTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: FetchImageTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = FetchImageTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FetchImageTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FetchImageTaskResponseBody = None,
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
            temp_model = FetchImageTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateFileUrlByKeyRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        file_key: str = None,
        file_name: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.file_key = file_key
        self.file_name = file_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        return self


class GenerateFileUrlByKeyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateFileUrlByKeyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateFileUrlByKeyResponseBody = None,
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
            temp_model = GenerateFileUrlByKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateImageTaskRequestParagraphList(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.id = id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GenerateImageTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        paragraph_list: List[GenerateImageTaskRequestParagraphList] = None,
        size: str = None,
        style: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.paragraph_list = paragraph_list
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.style = style

    def validate(self):
        if self.paragraph_list:
            for k in self.paragraph_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        result['ParagraphList'] = []
        if self.paragraph_list is not None:
            for k in self.paragraph_list:
                result['ParagraphList'].append(k.to_map() if k else None)
        if self.size is not None:
            result['Size'] = self.size
        if self.style is not None:
            result['Style'] = self.style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        self.paragraph_list = []
        if m.get('ParagraphList') is not None:
            for k in m.get('ParagraphList'):
                temp_model = GenerateImageTaskRequestParagraphList()
                self.paragraph_list.append(temp_model.from_map(k))
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        return self


class GenerateImageTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        article_task_id: str = None,
        paragraph_list_shrink: str = None,
        size: str = None,
        style: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.article_task_id = article_task_id
        # This parameter is required.
        self.paragraph_list_shrink = paragraph_list_shrink
        # This parameter is required.
        self.size = size
        # This parameter is required.
        self.style = style

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.article_task_id is not None:
            result['ArticleTaskId'] = self.article_task_id
        if self.paragraph_list_shrink is not None:
            result['ParagraphList'] = self.paragraph_list_shrink
        if self.size is not None:
            result['Size'] = self.size
        if self.style is not None:
            result['Style'] = self.style
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ArticleTaskId') is not None:
            self.article_task_id = m.get('ArticleTaskId')
        if m.get('ParagraphList') is not None:
            self.paragraph_list_shrink = m.get('ParagraphList')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        return self


class GenerateImageTaskResponseBodyDataTaskList(TeaModel):
    def __init__(
        self,
        content: str = None,
        id: int = None,
        task_id: str = None,
        task_status: str = None,
    ):
        self.content = content
        self.id = id
        self.task_id = task_id
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GenerateImageTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_list: List[GenerateImageTaskResponseBodyDataTaskList] = None,
    ):
        self.task_list = task_list

    def validate(self):
        if self.task_list:
            for k in self.task_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TaskList'] = []
        if self.task_list is not None:
            for k in self.task_list:
                result['TaskList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.task_list = []
        if m.get('TaskList') is not None:
            for k in m.get('TaskList'):
                temp_model = GenerateImageTaskResponseBodyDataTaskList()
                self.task_list.append(temp_model.from_map(k))
        return self


class GenerateImageTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateImageTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GenerateImageTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateImageTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateImageTaskResponseBody = None,
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
            temp_model = GenerateImageTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateUploadConfigRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        file_name: str = None,
        parent_dir: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.file_name = file_name
        # This parameter is required.
        self.parent_dir = parent_dir

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.parent_dir is not None:
            result['ParentDir'] = self.parent_dir
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('ParentDir') is not None:
            self.parent_dir = m.get('ParentDir')
        return self


class GenerateUploadConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        file_key: str = None,
        form_datas: Dict[str, Any] = None,
        post_url: str = None,
    ):
        self.file_key = file_key
        self.form_datas = form_datas
        self.post_url = post_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.form_datas is not None:
            result['FormDatas'] = self.form_datas
        if self.post_url is not None:
            result['PostUrl'] = self.post_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FormDatas') is not None:
            self.form_datas = m.get('FormDatas')
        if m.get('PostUrl') is not None:
            self.post_url = m.get('PostUrl')
        return self


class GenerateUploadConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GenerateUploadConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GenerateUploadConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateUploadConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateUploadConfigResponseBody = None,
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
            temp_model = GenerateUploadConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateViewPointRequestReferenceData(TeaModel):
    def __init__(
        self,
        mini_doc: List[str] = None,
    ):
        self.mini_doc = mini_doc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')
        return self


class GenerateViewPointRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        reference_data: GenerateViewPointRequestReferenceData = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reference_data = reference_data

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReferenceData') is not None:
            temp_model = GenerateViewPointRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        return self


class GenerateViewPointShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        reference_data_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reference_data_shrink = reference_data_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        return self


class GenerateViewPointResponseBodyData(TeaModel):
    def __init__(
        self,
        point: str = None,
    ):
        self.point = point

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.point is not None:
            result['Point'] = self.point
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Point') is not None:
            self.point = m.get('Point')
        return self


class GenerateViewPointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GenerateViewPointResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = GenerateViewPointResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GenerateViewPointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateViewPointResponseBody = None,
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
            temp_model = GenerateViewPointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomTextRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetCustomTextResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.title = title
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class GetCustomTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCustomTextResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetCustomTextResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomTextResponseBody = None,
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
            temp_model = GetCustomTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudes(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        ratio: str = None,
        view_points: List[GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResult(TeaModel):
    def __init__(
        self,
        attitudes: List[GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudes] = None,
        topic: str = None,
    ):
        self.attitudes = attitudes
        self.topic = topic

    def validate(self):
        if self.attitudes:
            for k in self.attitudes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k in self.attitudes:
                result['Attitudes'].append(k.to_map() if k else None)
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k in m.get('Attitudes'):
                temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k))
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        custom_view_points_result: GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResult = None,
        error_message: str = None,
        status: str = None,
    ):
        self.custom_view_points_result = custom_view_points_result
        self.error_message = error_message
        self.status = status

    def validate(self):
        if self.custom_view_points_result:
            self.custom_view_points_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_view_points_result is not None:
            result['CustomViewPointsResult'] = self.custom_view_points_result.to_map()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomViewPointsResult') is not None:
            temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyDataCustomViewPointsResult()
            self.custom_view_points_result = temp_model.from_map(m['CustomViewPointsResult'])
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCustomTopicSelectionPerspectiveAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBody = None,
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
            temp_model = GetCustomTopicSelectionPerspectiveAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDataSourceOrderConfigRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        product_code: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.product_code = product_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        return self


class GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        number: int = None,
        type: str = None,
    ):
        self.code = code
        self.name = name
        self.number = number
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetDataSourceOrderConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        user_config_data_source_list: List[GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList] = None,
    ):
        self.user_config_data_source_list = user_config_data_source_list

    def validate(self):
        if self.user_config_data_source_list:
            for k in self.user_config_data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k in m.get('UserConfigDataSourceList'):
                temp_model = GetDataSourceOrderConfigResponseBodyDataUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k))
        return self


class GetDataSourceOrderConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDataSourceOrderConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetDataSourceOrderConfigResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDataSourceOrderConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDataSourceOrderConfigResponseBody = None,
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
            temp_model = GetDataSourceOrderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDocClusterTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetDocClusterTaskResponseBodyDataTopics(TeaModel):
    def __init__(
        self,
        doc_ids: List[str] = None,
        summary: str = None,
        title: str = None,
    ):
        self.doc_ids = doc_ids
        self.summary = summary
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.doc_ids is not None:
            result['DocIds'] = self.doc_ids
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocIds') is not None:
            self.doc_ids = m.get('DocIds')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetDocClusterTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        status: str = None,
        topics: List[GetDocClusterTaskResponseBodyDataTopics] = None,
    ):
        self.error_message = error_message
        self.status = status
        self.topics = topics

    def validate(self):
        if self.topics:
            for k in self.topics:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.status is not None:
            result['Status'] = self.status
        result['Topics'] = []
        if self.topics is not None:
            for k in self.topics:
                result['Topics'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.topics = []
        if m.get('Topics') is not None:
            for k in m.get('Topics'):
                temp_model = GetDocClusterTaskResponseBodyDataTopics()
                self.topics.append(temp_model.from_map(k))
        return self


class GetDocClusterTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDocClusterTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetDocClusterTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetDocClusterTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDocClusterTaskResponseBody = None,
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
            temp_model = GetDocClusterTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGeneratedContentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetGeneratedContentResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        create_time: str = None,
        create_user: str = None,
        device_id: str = None,
        id: int = None,
        keyword_list: List[str] = None,
        keywords: str = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        uuid: str = None,
    ):
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.create_time = create_time
        self.create_user = create_user
        self.device_id = device_id
        self.id = id
        self.keyword_list = keyword_list
        self.keywords = keywords
        self.prompt = prompt
        self.task_id = task_id
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword_list is not None:
            result['KeywordList'] = self.keyword_list
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeywordList') is not None:
            self.keyword_list = m.get('KeywordList')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class GetGeneratedContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetGeneratedContentResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetGeneratedContentResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetGeneratedContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGeneratedContentResponseBody = None,
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
            temp_model = GetGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneGlobalReplyRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetInterveneGlobalReplyResponseBodyDataReplyMessagList(TeaModel):
    def __init__(
        self,
        message: str = None,
        reply_type: str = None,
    ):
        self.message = message
        self.reply_type = reply_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')
        return self


class GetInterveneGlobalReplyResponseBodyData(TeaModel):
    def __init__(
        self,
        reply_messag_list: List[GetInterveneGlobalReplyResponseBodyDataReplyMessagList] = None,
    ):
        self.reply_messag_list = reply_messag_list

    def validate(self):
        if self.reply_messag_list:
            for k in self.reply_messag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k in self.reply_messag_list:
                result['ReplyMessagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k in m.get('ReplyMessagList'):
                temp_model = GetInterveneGlobalReplyResponseBodyDataReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k))
        return self


class GetInterveneGlobalReplyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInterveneGlobalReplyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetInterveneGlobalReplyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInterveneGlobalReplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInterveneGlobalReplyResponseBody = None,
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
            temp_model = GetInterveneGlobalReplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneImportTaskInfoRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetInterveneImportTaskInfoResponseBodyDataStatus(TeaModel):
    def __init__(
        self,
        msg: str = None,
        percentage: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.msg = msg
        self.percentage = percentage
        self.status = status
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class GetInterveneImportTaskInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        status: GetInterveneImportTaskInfoResponseBodyDataStatus = None,
    ):
        self.status = status

    def validate(self):
        if self.status:
            self.status.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            temp_model = GetInterveneImportTaskInfoResponseBodyDataStatus()
            self.status = temp_model.from_map(m['Status'])
        return self


class GetInterveneImportTaskInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInterveneImportTaskInfoResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetInterveneImportTaskInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInterveneImportTaskInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInterveneImportTaskInfoResponseBody = None,
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
            temp_model = GetInterveneImportTaskInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneRuleDetailRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig(TeaModel):
    def __init__(
        self,
        answer_type: int = None,
        message: str = None,
        namespace: str = None,
    ):
        self.answer_type = answer_type
        self.message = message
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig(TeaModel):
    def __init__(
        self,
        effect_type: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.effect_type = effect_type
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail(TeaModel):
    def __init__(
        self,
        answer_config: List[GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig] = None,
        effect_config: GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig = None,
        intervene_type: int = None,
        namespace_list: List[str] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.answer_config = answer_config
        self.effect_config = effect_config
        self.intervene_type = intervene_type
        self.namespace_list = namespace_list
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()
        if self.effect_config:
            self.effect_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.effect_config is not None:
            result['EffectConfig'] = self.effect_config.to_map()
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('EffectConfig') is not None:
            temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetailEffectConfig()
            self.effect_config = temp_model.from_map(m['EffectConfig'])
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class GetInterveneRuleDetailResponseBodyData(TeaModel):
    def __init__(
        self,
        intervene_rule_detail: GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail = None,
    ):
        self.intervene_rule_detail = intervene_rule_detail

    def validate(self):
        if self.intervene_rule_detail:
            self.intervene_rule_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.intervene_rule_detail is not None:
            result['InterveneRuleDetail'] = self.intervene_rule_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InterveneRuleDetail') is not None:
            temp_model = GetInterveneRuleDetailResponseBodyDataInterveneRuleDetail()
            self.intervene_rule_detail = temp_model.from_map(m['InterveneRuleDetail'])
        return self


class GetInterveneRuleDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInterveneRuleDetailResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetInterveneRuleDetailResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInterveneRuleDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInterveneRuleDetailResponseBody = None,
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
            temp_model = GetInterveneRuleDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInterveneTemplateFileUrlRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetInterveneTemplateFileUrlResponseBodyData(TeaModel):
    def __init__(
        self,
        file_url: str = None,
    ):
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class GetInterveneTemplateFileUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInterveneTemplateFileUrlResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetInterveneTemplateFileUrlResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetInterveneTemplateFileUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInterveneTemplateFileUrlResponseBody = None,
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
            temp_model = GetInterveneTemplateFileUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMaterialByIdRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetMaterialByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        author: str = None,
        create_time: str = None,
        create_user: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        public_url: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        thumbnail_in_base_64: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        url: str = None,
    ):
        self.author = author
        self.create_time = create_time
        self.create_user = create_user
        self.doc_keywords = doc_keywords
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        self.id = id
        self.pub_time = pub_time
        self.public_url = public_url
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.thumbnail_in_base_64 = thumbnail_in_base_64
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.thumbnail_in_base_64 is not None:
            result['ThumbnailInBase64'] = self.thumbnail_in_base_64
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('ThumbnailInBase64') is not None:
            self.thumbnail_in_base_64 = m.get('ThumbnailInBase64')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMaterialByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetMaterialByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetMaterialByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetMaterialByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMaterialByIdResponseBody = None,
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
            temp_model = GetMaterialByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPropertiesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class GetPropertiesResponseBodyDataConsoleConfig(TeaModel):
    def __init__(
        self,
        tip_content: str = None,
        title: str = None,
    ):
        self.tip_content = tip_content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tip_content is not None:
            result['TipContent'] = self.tip_content
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TipContent') is not None:
            self.tip_content = m.get('TipContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles(TeaModel):
    def __init__(
        self,
        select: bool = None,
        stared: bool = None,
        title: str = None,
        url: str = None,
    ):
        self.select = select
        self.stared = stared
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.select is not None:
            result['Select'] = self.select
        if self.stared is not None:
            result['Stared'] = self.stared
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Select') is not None:
            self.select = m.get('Select')
        if m.get('Stared') is not None:
            self.stared = m.get('Stared')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples(TeaModel):
    def __init__(
        self,
        articles: List[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles] = None,
        prompt: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.prompt = prompt
        self.text = text

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamplesArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources(TeaModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
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
        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetPropertiesResponseBodyDataIntelligentSearchConfig(TeaModel):
    def __init__(
        self,
        product_description: str = None,
        search_samples: List[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples] = None,
        search_sources: List[GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources] = None,
    ):
        self.product_description = product_description
        self.search_samples = search_samples
        self.search_sources = search_sources

    def validate(self):
        if self.search_samples:
            for k in self.search_samples:
                if k:
                    k.validate()
        if self.search_sources:
            for k in self.search_sources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.product_description is not None:
            result['ProductDescription'] = self.product_description
        result['SearchSamples'] = []
        if self.search_samples is not None:
            for k in self.search_samples:
                result['SearchSamples'].append(k.to_map() if k else None)
        result['SearchSources'] = []
        if self.search_sources is not None:
            for k in self.search_sources:
                result['SearchSources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProductDescription') is not None:
            self.product_description = m.get('ProductDescription')
        self.search_samples = []
        if m.get('SearchSamples') is not None:
            for k in m.get('SearchSamples'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSamples()
                self.search_samples.append(temp_model.from_map(k))
        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k in m.get('SearchSources'):
                temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfigSearchSources()
                self.search_sources.append(temp_model.from_map(k))
        return self


class GetPropertiesResponseBodyDataSearchSources(TeaModel):
    def __init__(
        self,
        label: str = None,
        value: str = None,
    ):
        self.label = label
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['Label'] = self.label
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Label') is not None:
            self.label = m.get('Label')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyDataUserInfo(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        tenant_id: str = None,
        user_id: str = None,
        username: str = None,
    ):
        self.agent_id = agent_id
        self.tenant_id = tenant_id
        self.user_id = user_id
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetPropertiesResponseBodyDataWanxiangImageSizeConfig(TeaModel):
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
            result['Name'] = self.name
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyDataWanxiangImageStyleConfig(TeaModel):
    def __init__(
        self,
        name: str = None,
        pic: str = None,
        value: str = None,
    ):
        self.name = name
        self.pic = pic
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetPropertiesResponseBodyData(TeaModel):
    def __init__(
        self,
        chat_config: Dict[str, Any] = None,
        console_config: GetPropertiesResponseBodyDataConsoleConfig = None,
        general_config_map: Dict[str, Any] = None,
        intelligent_search_config: GetPropertiesResponseBodyDataIntelligentSearchConfig = None,
        search_sources: List[GetPropertiesResponseBodyDataSearchSources] = None,
        slr_authorized: bool = None,
        user_info: GetPropertiesResponseBodyDataUserInfo = None,
        wanxiang_image_size_config: List[GetPropertiesResponseBodyDataWanxiangImageSizeConfig] = None,
        wanxiang_image_style_config: List[GetPropertiesResponseBodyDataWanxiangImageStyleConfig] = None,
    ):
        self.chat_config = chat_config
        self.console_config = console_config
        self.general_config_map = general_config_map
        self.intelligent_search_config = intelligent_search_config
        self.search_sources = search_sources
        self.slr_authorized = slr_authorized
        self.user_info = user_info
        self.wanxiang_image_size_config = wanxiang_image_size_config
        self.wanxiang_image_style_config = wanxiang_image_style_config

    def validate(self):
        if self.console_config:
            self.console_config.validate()
        if self.intelligent_search_config:
            self.intelligent_search_config.validate()
        if self.search_sources:
            for k in self.search_sources:
                if k:
                    k.validate()
        if self.user_info:
            self.user_info.validate()
        if self.wanxiang_image_size_config:
            for k in self.wanxiang_image_size_config:
                if k:
                    k.validate()
        if self.wanxiang_image_style_config:
            for k in self.wanxiang_image_style_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config
        if self.console_config is not None:
            result['ConsoleConfig'] = self.console_config.to_map()
        if self.general_config_map is not None:
            result['GeneralConfigMap'] = self.general_config_map
        if self.intelligent_search_config is not None:
            result['IntelligentSearchConfig'] = self.intelligent_search_config.to_map()
        result['SearchSources'] = []
        if self.search_sources is not None:
            for k in self.search_sources:
                result['SearchSources'].append(k.to_map() if k else None)
        if self.slr_authorized is not None:
            result['SlrAuthorized'] = self.slr_authorized
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        result['WanxiangImageSizeConfig'] = []
        if self.wanxiang_image_size_config is not None:
            for k in self.wanxiang_image_size_config:
                result['WanxiangImageSizeConfig'].append(k.to_map() if k else None)
        result['WanxiangImageStyleConfig'] = []
        if self.wanxiang_image_style_config is not None:
            for k in self.wanxiang_image_style_config:
                result['WanxiangImageStyleConfig'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            self.chat_config = m.get('ChatConfig')
        if m.get('ConsoleConfig') is not None:
            temp_model = GetPropertiesResponseBodyDataConsoleConfig()
            self.console_config = temp_model.from_map(m['ConsoleConfig'])
        if m.get('GeneralConfigMap') is not None:
            self.general_config_map = m.get('GeneralConfigMap')
        if m.get('IntelligentSearchConfig') is not None:
            temp_model = GetPropertiesResponseBodyDataIntelligentSearchConfig()
            self.intelligent_search_config = temp_model.from_map(m['IntelligentSearchConfig'])
        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k in m.get('SearchSources'):
                temp_model = GetPropertiesResponseBodyDataSearchSources()
                self.search_sources.append(temp_model.from_map(k))
        if m.get('SlrAuthorized') is not None:
            self.slr_authorized = m.get('SlrAuthorized')
        if m.get('UserInfo') is not None:
            temp_model = GetPropertiesResponseBodyDataUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        self.wanxiang_image_size_config = []
        if m.get('WanxiangImageSizeConfig') is not None:
            for k in m.get('WanxiangImageSizeConfig'):
                temp_model = GetPropertiesResponseBodyDataWanxiangImageSizeConfig()
                self.wanxiang_image_size_config.append(temp_model.from_map(k))
        self.wanxiang_image_style_config = []
        if m.get('WanxiangImageStyleConfig') is not None:
            for k in m.get('WanxiangImageStyleConfig'):
                temp_model = GetPropertiesResponseBodyDataWanxiangImageStyleConfig()
                self.wanxiang_image_style_config.append(temp_model.from_map(k))
        return self


class GetPropertiesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetPropertiesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetPropertiesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPropertiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetPropertiesResponseBody = None,
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
            temp_model = GetPropertiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicByIdRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class GetTopicByIdResponseBodyDataStructureSummaryDocList(TeaModel):
    def __init__(
        self,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTopicByIdResponseBodyDataStructureSummary(TeaModel):
    def __init__(
        self,
        doc_list: List[GetTopicByIdResponseBodyDataStructureSummaryDocList] = None,
        summary: str = None,
        title: str = None,
    ):
        self.doc_list = doc_list
        self.summary = summary
        self.title = title

    def validate(self):
        if self.doc_list:
            for k in self.doc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocList'] = []
        if self.doc_list is not None:
            for k in self.doc_list:
                result['DocList'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_list = []
        if m.get('DocList') is not None:
            for k in m.get('DocList'):
                temp_model = GetTopicByIdResponseBodyDataStructureSummaryDocList()
                self.doc_list.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTopicByIdResponseBodyData(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        create_user: str = None,
        hot_value: int = None,
        id: str = None,
        status: str = None,
        structure_summary: List[GetTopicByIdResponseBodyDataStructureSummary] = None,
        summary: str = None,
        task_error_message: str = None,
        task_status: int = None,
        topic: str = None,
        topic_source: str = None,
        version: str = None,
    ):
        self.async_task_id = async_task_id
        self.create_user = create_user
        self.hot_value = hot_value
        self.id = id
        self.status = status
        self.structure_summary = structure_summary
        self.summary = summary
        self.task_error_message = task_error_message
        self.task_status = task_status
        self.topic = topic
        self.topic_source = topic_source
        self.version = version

    def validate(self):
        if self.structure_summary:
            for k in self.structure_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.hot_value is not None:
            result['HotValue'] = self.hot_value
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        result['StructureSummary'] = []
        if self.structure_summary is not None:
            for k in self.structure_summary:
                result['StructureSummary'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('HotValue') is not None:
            self.hot_value = m.get('HotValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.structure_summary = []
        if m.get('StructureSummary') is not None:
            for k in m.get('StructureSummary'):
                temp_model = GetTopicByIdResponseBodyDataStructureSummary()
                self.structure_summary.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetTopicByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTopicByIdResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetTopicByIdResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTopicByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicByIdResponseBody = None,
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
            temp_model = GetTopicByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTopicSelectionPerspectiveAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        ratio: str = None,
        view_points: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult(TeaModel):
    def __init__(
        self,
        attitudes: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for k in self.attitudes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k in self.attitudes:
                result['Attitudes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k in m.get('Attitudes'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews(TeaModel):
    def __init__(
        self,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        source: str = None,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
        topic: str = None,
        url: str = None,
    ):
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.source = source
        self.summary = summary
        self.tags = tags
        self.title = title
        self.topic = topic
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        news: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews] = None,
        ratio: str = None,
        view_points: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.news = news
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.news:
            for k in self.news:
                if k:
                    k.validate()
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        result['News'] = []
        if self.news is not None:
            for k in self.news:
                result['News'].append(k.to_map() if k else None)
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        self.news = []
        if m.get('News') is not None:
            for k in m.get('News'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesNews()
                self.news.append(temp_model.from_map(k))
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult(TeaModel):
    def __init__(
        self,
        attitudes: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for k in self.attitudes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k in self.attitudes:
                result['Attitudes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k in m.get('Attitudes'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        pub_time: str = None,
        ratio: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
        view_points: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.pub_time = pub_time
        self.ratio = ratio
        self.source = source
        self.title = title
        self.url = url
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult(TeaModel):
    def __init__(
        self,
        attitudes: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for k in self.attitudes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k in self.attitudes:
                result['Attitudes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k in m.get('Attitudes'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList(TeaModel):
    def __init__(
        self,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries(TeaModel):
    def __init__(
        self,
        doc_list: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList] = None,
        summary: str = None,
        title: str = None,
    ):
        self.doc_list = doc_list
        self.summary = summary
        self.title = title

    def validate(self):
        if self.doc_list:
            for k in self.doc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocList'] = []
        if self.doc_list is not None:
            for k in self.doc_list:
                result['DocList'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_list = []
        if m.get('DocList') is not None:
            for k in m.get('DocList'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummariesDocList()
                self.doc_list.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult(TeaModel):
    def __init__(
        self,
        summaries: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries] = None,
    ):
        self.summaries = summaries

    def validate(self):
        if self.summaries:
            for k in self.summaries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Summaries'] = []
        if self.summaries is not None:
            for k in self.summaries:
                result['Summaries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.summaries = []
        if m.get('Summaries') is not None:
            for k in m.get('Summaries'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResultSummaries()
                self.summaries.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments(TeaModel):
    def __init__(
        self,
        source: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
        username: str = None,
    ):
        self.source = source
        self.text = text
        self.title = title
        self.url = url
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        comments: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments] = None,
        ratio: str = None,
        view_points: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.comments = comments
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.comments:
            for k in self.comments:
                if k:
                    k.validate()
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        result['Comments'] = []
        if self.comments is not None:
            for k in self.comments:
                result['Comments'].append(k.to_map() if k else None)
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        self.comments = []
        if m.get('Comments') is not None:
            for k in m.get('Comments'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesComments()
                self.comments.append(temp_model.from_map(k))
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudesViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult(TeaModel):
    def __init__(
        self,
        attitudes: List[GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes] = None,
    ):
        self.attitudes = attitudes

    def validate(self):
        if self.attitudes:
            for k in self.attitudes:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Attitudes'] = []
        if self.attitudes is not None:
            for k in self.attitudes:
                result['Attitudes'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attitudes = []
        if m.get('Attitudes') is not None:
            for k in m.get('Attitudes'):
                temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResultAttitudes()
                self.attitudes.append(temp_model.from_map(k))
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        fresh_view_points_result: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult = None,
        hot_view_points_result: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult = None,
        status: str = None,
        timed_view_points_result: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult = None,
        topic: str = None,
        topic_summary_result: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult = None,
        web_review_points_result: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult = None,
    ):
        self.error_message = error_message
        self.fresh_view_points_result = fresh_view_points_result
        self.hot_view_points_result = hot_view_points_result
        self.status = status
        self.timed_view_points_result = timed_view_points_result
        self.topic = topic
        self.topic_summary_result = topic_summary_result
        self.web_review_points_result = web_review_points_result

    def validate(self):
        if self.fresh_view_points_result:
            self.fresh_view_points_result.validate()
        if self.hot_view_points_result:
            self.hot_view_points_result.validate()
        if self.timed_view_points_result:
            self.timed_view_points_result.validate()
        if self.topic_summary_result:
            self.topic_summary_result.validate()
        if self.web_review_points_result:
            self.web_review_points_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.fresh_view_points_result is not None:
            result['FreshViewPointsResult'] = self.fresh_view_points_result.to_map()
        if self.hot_view_points_result is not None:
            result['HotViewPointsResult'] = self.hot_view_points_result.to_map()
        if self.status is not None:
            result['Status'] = self.status
        if self.timed_view_points_result is not None:
            result['TimedViewPointsResult'] = self.timed_view_points_result.to_map()
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_summary_result is not None:
            result['TopicSummaryResult'] = self.topic_summary_result.to_map()
        if self.web_review_points_result is not None:
            result['WebReviewPointsResult'] = self.web_review_points_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('FreshViewPointsResult') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataFreshViewPointsResult()
            self.fresh_view_points_result = temp_model.from_map(m['FreshViewPointsResult'])
        if m.get('HotViewPointsResult') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataHotViewPointsResult()
            self.hot_view_points_result = temp_model.from_map(m['HotViewPointsResult'])
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TimedViewPointsResult') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTimedViewPointsResult()
            self.timed_view_points_result = temp_model.from_map(m['TimedViewPointsResult'])
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSummaryResult') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataTopicSummaryResult()
            self.topic_summary_result = temp_model.from_map(m['TopicSummaryResult'])
        if m.get('WebReviewPointsResult') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyDataWebReviewPointsResult()
            self.web_review_points_result = temp_model.from_map(m['WebReviewPointsResult'])
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetTopicSelectionPerspectiveAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTopicSelectionPerspectiveAnalysisTaskResponseBody = None,
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
            temp_model = GetTopicSelectionPerspectiveAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportInterveneFileRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        doc_name: str = None,
        file_key: str = None,
        file_url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.doc_name = doc_name
        self.file_key = file_key
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportInterveneFileResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_id_list: List[str] = None,
        task_id: str = None,
    ):
        self.fail_id_list = fail_id_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportInterveneFileResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ImportInterveneFileResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ImportInterveneFileResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportInterveneFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportInterveneFileResponseBody = None,
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
            temp_model = ImportInterveneFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportInterveneFileAsyncRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        doc_name: str = None,
        file_key: str = None,
        file_url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.doc_name = doc_name
        self.file_key = file_key
        self.file_url = file_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.doc_name is not None:
            result['DocName'] = self.doc_name
        if self.file_key is not None:
            result['FileKey'] = self.file_key
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('DocName') is not None:
            self.doc_name = m.get('DocName')
        if m.get('FileKey') is not None:
            self.file_key = m.get('FileKey')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        return self


class ImportInterveneFileAsyncResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_id_list: List[str] = None,
        task_id: str = None,
    ):
        self.fail_id_list = fail_id_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ImportInterveneFileAsyncResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ImportInterveneFileAsyncResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ImportInterveneFileAsyncResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ImportInterveneFileAsyncResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportInterveneFileAsyncResponseBody = None,
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
            temp_model = ImportInterveneFileAsyncResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInterveneGlobalReplyRequestReplyMessagList(TeaModel):
    def __init__(
        self,
        message: str = None,
        reply_type: str = None,
    ):
        self.message = message
        self.reply_type = reply_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.reply_type is not None:
            result['ReplyType'] = self.reply_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('ReplyType') is not None:
            self.reply_type = m.get('ReplyType')
        return self


class InsertInterveneGlobalReplyRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        reply_messag_list: List[InsertInterveneGlobalReplyRequestReplyMessagList] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reply_messag_list = reply_messag_list

    def validate(self):
        if self.reply_messag_list:
            for k in self.reply_messag_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['ReplyMessagList'] = []
        if self.reply_messag_list is not None:
            for k in self.reply_messag_list:
                result['ReplyMessagList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.reply_messag_list = []
        if m.get('ReplyMessagList') is not None:
            for k in m.get('ReplyMessagList'):
                temp_model = InsertInterveneGlobalReplyRequestReplyMessagList()
                self.reply_messag_list.append(temp_model.from_map(k))
        return self


class InsertInterveneGlobalReplyShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        reply_messag_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.reply_messag_list_shrink = reply_messag_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.reply_messag_list_shrink is not None:
            result['ReplyMessagList'] = self.reply_messag_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ReplyMessagList') is not None:
            self.reply_messag_list_shrink = m.get('ReplyMessagList')
        return self


class InsertInterveneGlobalReplyResponseBodyData(TeaModel):
    def __init__(
        self,
        fail_id_list: List[str] = None,
        task_id: str = None,
    ):
        self.fail_id_list = fail_id_list
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fail_id_list is not None:
            result['FailIdList'] = self.fail_id_list
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailIdList') is not None:
            self.fail_id_list = m.get('FailIdList')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class InsertInterveneGlobalReplyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: InsertInterveneGlobalReplyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = InsertInterveneGlobalReplyResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertInterveneGlobalReplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertInterveneGlobalReplyResponseBody = None,
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
            temp_model = InsertInterveneGlobalReplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig(TeaModel):
    def __init__(
        self,
        answer_type: int = None,
        message: str = None,
        namespace: str = None,
    ):
        self.answer_type = answer_type
        self.message = message
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class InsertInterveneRuleRequestInterveneRuleConfigEffectConfig(TeaModel):
    def __init__(
        self,
        effect_type: int = None,
        end_time: str = None,
        start_time: str = None,
    ):
        self.effect_type = effect_type
        self.end_time = end_time
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_type is not None:
            result['EffectType'] = self.effect_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectType') is not None:
            self.effect_type = m.get('EffectType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList(TeaModel):
    def __init__(
        self,
        id: str = None,
        operation_type: int = None,
        query: str = None,
    ):
        # id
        self.id = id
        self.operation_type = operation_type
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.operation_type is not None:
            result['OperationType'] = self.operation_type
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class InsertInterveneRuleRequestInterveneRuleConfig(TeaModel):
    def __init__(
        self,
        answer_config: List[InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig] = None,
        effect_config: InsertInterveneRuleRequestInterveneRuleConfigEffectConfig = None,
        intervene_config_list: List[InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList] = None,
        intervene_type: int = None,
        namespace_list: List[str] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.answer_config = answer_config
        self.effect_config = effect_config
        self.intervene_config_list = intervene_config_list
        self.intervene_type = intervene_type
        self.namespace_list = namespace_list
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()
        if self.effect_config:
            self.effect_config.validate()
        if self.intervene_config_list:
            for k in self.intervene_config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.effect_config is not None:
            result['EffectConfig'] = self.effect_config.to_map()
        result['InterveneConfigList'] = []
        if self.intervene_config_list is not None:
            for k in self.intervene_config_list:
                result['InterveneConfigList'].append(k.to_map() if k else None)
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = InsertInterveneRuleRequestInterveneRuleConfigAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('EffectConfig') is not None:
            temp_model = InsertInterveneRuleRequestInterveneRuleConfigEffectConfig()
            self.effect_config = temp_model.from_map(m['EffectConfig'])
        self.intervene_config_list = []
        if m.get('InterveneConfigList') is not None:
            for k in m.get('InterveneConfigList'):
                temp_model = InsertInterveneRuleRequestInterveneRuleConfigInterveneConfigList()
                self.intervene_config_list.append(temp_model.from_map(k))
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class InsertInterveneRuleRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_rule_config: InsertInterveneRuleRequestInterveneRuleConfig = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_rule_config = intervene_rule_config

    def validate(self):
        if self.intervene_rule_config:
            self.intervene_rule_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_rule_config is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneRuleConfig') is not None:
            temp_model = InsertInterveneRuleRequestInterveneRuleConfig()
            self.intervene_rule_config = temp_model.from_map(m['InterveneRuleConfig'])
        return self


class InsertInterveneRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_rule_config_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_rule_config_shrink = intervene_rule_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_rule_config_shrink is not None:
            result['InterveneRuleConfig'] = self.intervene_rule_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneRuleConfig') is not None:
            self.intervene_rule_config_shrink = m.get('InterveneRuleConfig')
        return self


class InsertInterveneRuleResponseBodyData(TeaModel):
    def __init__(
        self,
        rule_id: int = None,
    ):
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class InsertInterveneRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: InsertInterveneRuleResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = InsertInterveneRuleResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class InsertInterveneRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InsertInterveneRuleResponseBody = None,
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
            temp_model = InsertInterveneRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAsyncTasksRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        size: int = None,
        task_code: str = None,
        task_name: str = None,
        task_status: int = None,
        task_status_list: List[int] = None,
        task_type: str = None,
        task_type_list: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.current = current
        self.size = size
        self.task_code = task_code
        self.task_name = task_name
        self.task_status = task_status
        self.task_status_list = task_status_list
        self.task_type = task_type
        self.task_type_list = task_type_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_list is not None:
            result['TaskStatusList'] = self.task_status_list
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_list is not None:
            result['TaskTypeList'] = self.task_type_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusList') is not None:
            self.task_status_list = m.get('TaskStatusList')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeList') is not None:
            self.task_type_list = m.get('TaskTypeList')
        return self


class ListAsyncTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        size: int = None,
        task_code: str = None,
        task_name: str = None,
        task_status: int = None,
        task_status_list_shrink: str = None,
        task_type: str = None,
        task_type_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.current = current
        self.size = size
        self.task_code = task_code
        self.task_name = task_name
        self.task_status = task_status
        self.task_status_list_shrink = task_status_list_shrink
        self.task_type = task_type
        self.task_type_list_shrink = task_type_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.size is not None:
            result['Size'] = self.size
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_status_list_shrink is not None:
            result['TaskStatusList'] = self.task_status_list_shrink
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_type_list_shrink is not None:
            result['TaskTypeList'] = self.task_type_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskStatusList') is not None:
            self.task_status_list_shrink = m.get('TaskStatusList')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskTypeList') is not None:
            self.task_type_list_shrink = m.get('TaskTypeList')
        return self


class ListAsyncTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        task_code: str = None,
        task_definition: str = None,
        task_end_time: str = None,
        task_error_message: str = None,
        task_execute_time: str = None,
        task_id: str = None,
        task_inner_error_message: str = None,
        task_intermediate_result: str = None,
        task_name: str = None,
        task_param: str = None,
        task_progress_message: str = None,
        task_result: str = None,
        task_retry_count: str = None,
        task_start_time: str = None,
        task_status: int = None,
        task_type: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.task_code = task_code
        self.task_definition = task_definition
        self.task_end_time = task_end_time
        self.task_error_message = task_error_message
        self.task_execute_time = task_execute_time
        self.task_id = task_id
        self.task_inner_error_message = task_inner_error_message
        self.task_intermediate_result = task_intermediate_result
        self.task_name = task_name
        self.task_param = task_param
        self.task_progress_message = task_progress_message
        self.task_result = task_result
        self.task_retry_count = task_retry_count
        self.task_start_time = task_start_time
        self.task_status = task_status
        self.task_type = task_type
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_definition is not None:
            result['TaskDefinition'] = self.task_definition
        if self.task_end_time is not None:
            result['TaskEndTime'] = self.task_end_time
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_inner_error_message is not None:
            result['TaskInnerErrorMessage'] = self.task_inner_error_message
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_progress_message is not None:
            result['TaskProgressMessage'] = self.task_progress_message
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_retry_count is not None:
            result['TaskRetryCount'] = self.task_retry_count
        if self.task_start_time is not None:
            result['TaskStartTime'] = self.task_start_time
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskDefinition') is not None:
            self.task_definition = m.get('TaskDefinition')
        if m.get('TaskEndTime') is not None:
            self.task_end_time = m.get('TaskEndTime')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInnerErrorMessage') is not None:
            self.task_inner_error_message = m.get('TaskInnerErrorMessage')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskProgressMessage') is not None:
            self.task_progress_message = m.get('TaskProgressMessage')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskRetryCount') is not None:
            self.task_retry_count = m.get('TaskRetryCount')
        if m.get('TaskStartTime') is not None:
            self.task_start_time = m.get('TaskStartTime')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class ListAsyncTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListAsyncTasksResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListAsyncTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListAsyncTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAsyncTasksResponseBody = None,
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
            temp_model = ListAsyncTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBuildConfigsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        region_id: str = None,
        type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.region_id = region_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListBuildConfigsResponseBodyDataKeywords(TeaModel):
    def __init__(
        self,
        description: str = None,
        key: str = None,
    ):
        self.description = description
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class ListBuildConfigsResponseBodyData(TeaModel):
    def __init__(
        self,
        build_in: bool = None,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        keywords: List[ListBuildConfigsResponseBodyDataKeywords] = None,
        tag: str = None,
        tag_description: str = None,
        type: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.build_in = build_in
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.keywords = keywords
        self.tag = tag
        self.tag_description = tag_description
        self.type = type
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        if self.keywords:
            for k in self.keywords:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_in is not None:
            result['BuildIn'] = self.build_in
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        result['Keywords'] = []
        if self.keywords is not None:
            for k in self.keywords:
                result['Keywords'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.tag_description is not None:
            result['TagDescription'] = self.tag_description
        if self.type is not None:
            result['Type'] = self.type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildIn') is not None:
            self.build_in = m.get('BuildIn')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        self.keywords = []
        if m.get('Keywords') is not None:
            for k in m.get('Keywords'):
                temp_model = ListBuildConfigsResponseBodyDataKeywords()
                self.keywords.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TagDescription') is not None:
            self.tag_description = m.get('TagDescription')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class ListBuildConfigsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListBuildConfigsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListBuildConfigsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListBuildConfigsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBuildConfigsResponseBody = None,
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
            temp_model = ListBuildConfigsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomTextRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        return self


class ListCustomTextResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        create_time: str = None,
        create_user: str = None,
        id: int = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.content = content
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.title = title
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class ListCustomTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListCustomTextResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListCustomTextResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCustomTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomTextResponseBody = None,
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
            temp_model = ListCustomTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCustomViewPointsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        attitude: str = None,
        attitudes: List[str] = None,
        custom_view_point_id: str = None,
        custom_view_point_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.attitude = attitude
        self.attitudes = attitudes
        self.custom_view_point_id = custom_view_point_id
        self.custom_view_point_ids = custom_view_point_ids
        self.max_results = max_results
        self.next_token = next_token
        self.topic = topic
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitudes is not None:
            result['Attitudes'] = self.attitudes
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        if self.custom_view_point_ids is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('Attitudes') is not None:
            self.attitudes = m.get('Attitudes')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids = m.get('CustomViewPointIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ListCustomViewPointsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        attitude: str = None,
        attitudes_shrink: str = None,
        custom_view_point_id: str = None,
        custom_view_point_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.attitude = attitude
        self.attitudes_shrink = attitudes_shrink
        self.custom_view_point_id = custom_view_point_id
        self.custom_view_point_ids_shrink = custom_view_point_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.topic = topic
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitudes_shrink is not None:
            result['Attitudes'] = self.attitudes_shrink
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        if self.custom_view_point_ids_shrink is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('Attitudes') is not None:
            self.attitudes_shrink = m.get('Attitudes')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids_shrink = m.get('CustomViewPointIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ListCustomViewPointsResponseBodyDataViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListCustomViewPointsResponseBodyDataViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[ListCustomViewPointsResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListCustomViewPointsResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListCustomViewPointsResponseBodyData(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        attitude: str = None,
        create_time: str = None,
        create_user: str = None,
        id: str = None,
        status: str = None,
        task_error_message: str = None,
        task_status: int = None,
        view_points: List[ListCustomViewPointsResponseBodyDataViewPoints] = None,
    ):
        self.async_task_id = async_task_id
        self.attitude = attitude
        self.create_time = create_time
        self.create_user = create_user
        self.id = id
        self.status = status
        self.task_error_message = task_error_message
        self.task_status = task_status
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = ListCustomViewPointsResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class ListCustomViewPointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListCustomViewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListCustomViewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListCustomViewPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCustomViewPointsResponseBody = None,
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
            temp_model = ListCustomViewPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDialoguesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        dialogue_type: int = None,
        end_time: str = None,
        size: int = None,
        start_time: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.current = current
        self.dialogue_type = dialogue_type
        self.end_time = end_time
        self.size = size
        self.start_time = start_time
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class ListDialoguesResponseBodyData(TeaModel):
    def __init__(
        self,
        bot: str = None,
        create_time: str = None,
        create_user: str = None,
        dialogue_type: int = None,
        task_id: str = None,
        user: str = None,
    ):
        self.bot = bot
        self.create_time = create_time
        self.create_user = create_user
        self.dialogue_type = dialogue_type
        self.task_id = task_id
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot is not None:
            result['Bot'] = self.bot
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user is not None:
            result['User'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bot') is not None:
            self.bot = m.get('Bot')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('User') is not None:
            self.user = m.get('User')
        return self


class ListDialoguesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListDialoguesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListDialoguesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListDialoguesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDialoguesResponseBody = None,
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
            temp_model = ListDialoguesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFreshViewPointsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_source: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        return self


class ListFreshViewPointsResponseBodyDataOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListFreshViewPointsResponseBodyData(TeaModel):
    def __init__(
        self,
        outlines: List[ListFreshViewPointsResponseBodyDataOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListFreshViewPointsResponseBodyDataOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListFreshViewPointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListFreshViewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListFreshViewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListFreshViewPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFreshViewPointsResponseBody = None,
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
            temp_model = ListFreshViewPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGeneratedContentsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content_domain: str = None,
        current: int = None,
        end_time: str = None,
        query: str = None,
        size: int = None,
        start_time: str = None,
        task_id: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content_domain = content_domain
        self.current = current
        self.end_time = end_time
        self.query = query
        self.size = size
        self.start_time = start_time
        self.task_id = task_id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.current is not None:
            result['Current'] = self.current
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.query is not None:
            result['Query'] = self.query
        if self.size is not None:
            result['Size'] = self.size
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListGeneratedContentsResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        content_domain: str = None,
        content_text: str = None,
        create_time: str = None,
        create_user: str = None,
        device_id: str = None,
        id: int = None,
        keyword_list: List[str] = None,
        keywords: str = None,
        prompt: str = None,
        task_id: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        uuid: str = None,
    ):
        self.content = content
        self.content_domain = content_domain
        self.content_text = content_text
        self.create_time = create_time
        self.create_user = create_user
        self.device_id = device_id
        self.id = id
        self.keyword_list = keyword_list
        self.keywords = keywords
        self.prompt = prompt
        self.task_id = task_id
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.content_domain is not None:
            result['ContentDomain'] = self.content_domain
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.keyword_list is not None:
            result['KeywordList'] = self.keyword_list
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentDomain') is not None:
            self.content_domain = m.get('ContentDomain')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('KeywordList') is not None:
            self.keyword_list = m.get('KeywordList')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ListGeneratedContentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListGeneratedContentsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListGeneratedContentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListGeneratedContentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGeneratedContentsResponseBody = None,
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
            temp_model = ListGeneratedContentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotNewsWithTypeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        news_type: str = None,
        news_types: List[str] = None,
        size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.current = current
        self.news_type = news_type
        self.news_types = news_types
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_types is not None:
            result['NewsTypes'] = self.news_types
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypes') is not None:
            self.news_types = m.get('NewsTypes')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListHotNewsWithTypeShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        current: int = None,
        news_type: str = None,
        news_types_shrink: str = None,
        size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.current = current
        self.news_type = news_type
        self.news_types_shrink = news_types_shrink
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.current is not None:
            result['Current'] = self.current
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_types_shrink is not None:
            result['NewsTypes'] = self.news_types_shrink
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypes') is not None:
            self.news_types_shrink = m.get('NewsTypes')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListHotNewsWithTypeResponseBodyDataNews(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        update_time: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.update_time = update_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.search_source is not None:
            result['SearchSource'] = self.search_source
        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')
        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotNewsWithTypeResponseBodyData(TeaModel):
    def __init__(
        self,
        news: List[ListHotNewsWithTypeResponseBodyDataNews] = None,
        news_type: str = None,
        news_type_name: str = None,
        total_pages: int = None,
    ):
        self.news = news
        self.news_type = news_type
        self.news_type_name = news_type_name
        self.total_pages = total_pages

    def validate(self):
        if self.news:
            for k in self.news:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['News'] = []
        if self.news is not None:
            for k in self.news:
                result['News'].append(k.to_map() if k else None)
        if self.news_type is not None:
            result['NewsType'] = self.news_type
        if self.news_type_name is not None:
            result['NewsTypeName'] = self.news_type_name
        if self.total_pages is not None:
            result['TotalPages'] = self.total_pages
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.news = []
        if m.get('News') is not None:
            for k in m.get('News'):
                temp_model = ListHotNewsWithTypeResponseBodyDataNews()
                self.news.append(temp_model.from_map(k))
        if m.get('NewsType') is not None:
            self.news_type = m.get('NewsType')
        if m.get('NewsTypeName') is not None:
            self.news_type_name = m.get('NewsTypeName')
        if m.get('TotalPages') is not None:
            self.total_pages = m.get('TotalPages')
        return self


class ListHotNewsWithTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHotNewsWithTypeResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListHotNewsWithTypeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListHotNewsWithTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotNewsWithTypeResponseBody = None,
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
            temp_model = ListHotNewsWithTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotSourcesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListHotSourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        show: bool = None,
        sort: int = None,
        source: str = None,
    ):
        self.description = description
        self.show = show
        self.sort = sort
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.show is not None:
            result['Show'] = self.show
        if self.sort is not None:
            result['Sort'] = self.sort
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Show') is not None:
            self.show = m.get('Show')
        if m.get('Sort') is not None:
            self.sort = m.get('Sort')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class ListHotSourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHotSourcesResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotSourcesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHotSourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotSourcesResponseBody = None,
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
            temp_model = ListHotSourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotTopicsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic_ids: List[str] = None,
        topic_query: str = None,
        topic_source: str = None,
        topic_version: str = None,
        topics: List[str] = None,
        with_news: bool = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        self.topic_ids = topic_ids
        self.topic_query = topic_query
        self.topic_source = topic_source
        self.topic_version = topic_version
        self.topics = topics
        self.with_news = with_news

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic_ids is not None:
            result['TopicIds'] = self.topic_ids
        if self.topic_query is not None:
            result['TopicQuery'] = self.topic_query
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version
        if self.topics is not None:
            result['Topics'] = self.topics
        if self.with_news is not None:
            result['WithNews'] = self.with_news
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TopicIds') is not None:
            self.topic_ids = m.get('TopicIds')
        if m.get('TopicQuery') is not None:
            self.topic_query = m.get('TopicQuery')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')
        if m.get('Topics') is not None:
            self.topics = m.get('Topics')
        if m.get('WithNews') is not None:
            self.with_news = m.get('WithNews')
        return self


class ListHotTopicsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic_ids_shrink: str = None,
        topic_query: str = None,
        topic_source: str = None,
        topic_version: str = None,
        topics_shrink: str = None,
        with_news: bool = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        self.topic_ids_shrink = topic_ids_shrink
        self.topic_query = topic_query
        self.topic_source = topic_source
        self.topic_version = topic_version
        self.topics_shrink = topics_shrink
        self.with_news = with_news

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic_ids_shrink is not None:
            result['TopicIds'] = self.topic_ids_shrink
        if self.topic_query is not None:
            result['TopicQuery'] = self.topic_query
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version
        if self.topics_shrink is not None:
            result['Topics'] = self.topics_shrink
        if self.with_news is not None:
            result['WithNews'] = self.with_news
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('TopicIds') is not None:
            self.topic_ids_shrink = m.get('TopicIds')
        if m.get('TopicQuery') is not None:
            self.topic_query = m.get('TopicQuery')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')
        if m.get('Topics') is not None:
            self.topics_shrink = m.get('Topics')
        if m.get('WithNews') is not None:
            self.with_news = m.get('WithNews')
        return self


class ListHotTopicsResponseBodyDataStructureSummaryDocList(TeaModel):
    def __init__(
        self,
        source: str = None,
        title: str = None,
        url: str = None,
    ):
        self.source = source
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotTopicsResponseBodyDataStructureSummary(TeaModel):
    def __init__(
        self,
        doc_list: List[ListHotTopicsResponseBodyDataStructureSummaryDocList] = None,
        summary: str = None,
        title: str = None,
    ):
        self.doc_list = doc_list
        self.summary = summary
        self.title = title

    def validate(self):
        if self.doc_list:
            for k in self.doc_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DocList'] = []
        if self.doc_list is not None:
            for k in self.doc_list:
                result['DocList'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.doc_list = []
        if m.get('DocList') is not None:
            for k in m.get('DocList'):
                temp_model = ListHotTopicsResponseBodyDataStructureSummaryDocList()
                self.doc_list.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListHotTopicsResponseBodyData(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        create_user: str = None,
        hot_value: int = None,
        id: str = None,
        status: str = None,
        structure_summary: List[ListHotTopicsResponseBodyDataStructureSummary] = None,
        summary: str = None,
        task_error_message: str = None,
        task_status: int = None,
        topic: str = None,
        topic_source: str = None,
        version: str = None,
    ):
        self.async_task_id = async_task_id
        self.create_user = create_user
        self.hot_value = hot_value
        self.id = id
        self.status = status
        self.structure_summary = structure_summary
        self.summary = summary
        self.task_error_message = task_error_message
        self.task_status = task_status
        self.topic = topic
        self.topic_source = topic_source
        self.version = version

    def validate(self):
        if self.structure_summary:
            for k in self.structure_summary:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.hot_value is not None:
            result['HotValue'] = self.hot_value
        if self.id is not None:
            result['Id'] = self.id
        if self.status is not None:
            result['Status'] = self.status
        result['StructureSummary'] = []
        if self.structure_summary is not None:
            for k in self.structure_summary:
                result['StructureSummary'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('HotValue') is not None:
            self.hot_value = m.get('HotValue')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        self.structure_summary = []
        if m.get('StructureSummary') is not None:
            for k in m.get('StructureSummary'):
                temp_model = ListHotTopicsResponseBodyDataStructureSummary()
                self.structure_summary.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListHotTopicsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHotTopicsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotTopicsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHotTopicsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotTopicsResponseBody = None,
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
            temp_model = ListHotTopicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHotViewPointsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_source: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        return self


class ListHotViewPointsResponseBodyDataNews(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tags: List[str] = None,
        title: str = None,
        topic: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tags = tags
        self.title = title
        self.topic = topic
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tags is not None:
            result['Tags'] = self.tags
        if self.title is not None:
            result['Title'] = self.title
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tags') is not None:
            self.tags = m.get('Tags')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListHotViewPointsResponseBodyDataViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListHotViewPointsResponseBodyDataViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[ListHotViewPointsResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListHotViewPointsResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListHotViewPointsResponseBodyData(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        news: List[ListHotViewPointsResponseBodyDataNews] = None,
        ratio: str = None,
        view_points: List[ListHotViewPointsResponseBodyDataViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.news = news
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.news:
            for k in self.news:
                if k:
                    k.validate()
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        result['News'] = []
        if self.news is not None:
            for k in self.news:
                result['News'].append(k.to_map() if k else None)
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        self.news = []
        if m.get('News') is not None:
            for k in m.get('News'):
                temp_model = ListHotViewPointsResponseBodyDataNews()
                self.news.append(temp_model.from_map(k))
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = ListHotViewPointsResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class ListHotViewPointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListHotViewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListHotViewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHotViewPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListHotViewPointsResponseBody = None,
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
            temp_model = ListHotViewPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneCntRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneCntResponseBodyData(TeaModel):
    def __init__(
        self,
        cnt_list: List[Any] = None,
        page_cnt: int = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.cnt_list = cnt_list
        self.page_cnt = page_cnt
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cnt_list is not None:
            result['CntList'] = self.cnt_list
        if self.page_cnt is not None:
            result['PageCnt'] = self.page_cnt
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CntList') is not None:
            self.cnt_list = m.get('CntList')
        if m.get('PageCnt') is not None:
            self.page_cnt = m.get('PageCnt')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneCntResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInterveneCntResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListInterveneCntResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInterveneCntResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterveneCntResponseBody = None,
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
            temp_model = ListInterveneCntResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneImportTasksRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneImportTasksResponseBodyDataStatusList(TeaModel):
    def __init__(
        self,
        msg: str = None,
        percentage: int = None,
        status: int = None,
        task_id: str = None,
        task_name: str = None,
    ):
        self.msg = msg
        self.percentage = percentage
        self.status = status
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg is not None:
            result['Msg'] = self.msg
        if self.percentage is not None:
            result['Percentage'] = self.percentage
        if self.status is not None:
            result['Status'] = self.status
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        if m.get('Percentage') is not None:
            self.percentage = m.get('Percentage')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class ListInterveneImportTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        page_index: int = None,
        page_size: int = None,
        status_list: List[ListInterveneImportTasksResponseBodyDataStatusList] = None,
        total_size: int = None,
    ):
        self.page_index = page_index
        self.page_size = page_size
        self.status_list = status_list
        self.total_size = total_size

    def validate(self):
        if self.status_list:
            for k in self.status_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['StatusList'] = []
        if self.status_list is not None:
            for k in self.status_list:
                result['StatusList'].append(k.to_map() if k else None)
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.status_list = []
        if m.get('StatusList') is not None:
            for k in m.get('StatusList'):
                temp_model = ListInterveneImportTasksResponseBodyDataStatusList()
                self.status_list.append(temp_model.from_map(k))
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListInterveneImportTasksResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInterveneImportTasksResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListInterveneImportTasksResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInterveneImportTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterveneImportTasksResponseBody = None,
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
            temp_model = ListInterveneImportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInterveneRulesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig(TeaModel):
    def __init__(
        self,
        answer_type: int = None,
        message: str = None,
        namespace: str = None,
    ):
        self.answer_type = answer_type
        self.message = message
        self.namespace = namespace

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer_type is not None:
            result['AnswerType'] = self.answer_type
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnswerType') is not None:
            self.answer_type = m.get('AnswerType')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        return self


class ListInterveneRulesResponseBodyDataInterveneRuleList(TeaModel):
    def __init__(
        self,
        answer_config: List[ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig] = None,
        create_time: str = None,
        effect_time: str = None,
        intervene_type: int = None,
        namespace_list: List[str] = None,
        rule_id: int = None,
        rule_name: str = None,
    ):
        self.answer_config = answer_config
        self.create_time = create_time
        self.effect_time = effect_time
        self.intervene_type = intervene_type
        self.namespace_list = namespace_list
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        if self.answer_config:
            for k in self.answer_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AnswerConfig'] = []
        if self.answer_config is not None:
            for k in self.answer_config:
                result['AnswerConfig'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.effect_time is not None:
            result['EffectTime'] = self.effect_time
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.namespace_list is not None:
            result['NamespaceList'] = self.namespace_list
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.answer_config = []
        if m.get('AnswerConfig') is not None:
            for k in m.get('AnswerConfig'):
                temp_model = ListInterveneRulesResponseBodyDataInterveneRuleListAnswerConfig()
                self.answer_config.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EffectTime') is not None:
            self.effect_time = m.get('EffectTime')
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('NamespaceList') is not None:
            self.namespace_list = m.get('NamespaceList')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListInterveneRulesResponseBodyData(TeaModel):
    def __init__(
        self,
        count: int = None,
        intervene_rule_list: List[ListInterveneRulesResponseBodyDataInterveneRuleList] = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.count = count
        self.intervene_rule_list = intervene_rule_list
        self.page_index = page_index
        self.page_size = page_size

    def validate(self):
        if self.intervene_rule_list:
            for k in self.intervene_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        result['InterveneRuleList'] = []
        if self.intervene_rule_list is not None:
            for k in self.intervene_rule_list:
                result['InterveneRuleList'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        self.intervene_rule_list = []
        if m.get('InterveneRuleList') is not None:
            for k in m.get('InterveneRuleList'):
                temp_model = ListInterveneRulesResponseBodyDataInterveneRuleList()
                self.intervene_rule_list.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInterveneRulesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInterveneRulesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListInterveneRulesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListInterveneRulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInterveneRulesResponseBody = None,
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
            temp_model = ListInterveneRulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIntervenesRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        intervene_type: int = None,
        page_index: int = None,
        page_size: int = None,
        query: str = None,
        rule_id: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.intervene_type = intervene_type
        self.page_index = page_index
        self.page_size = page_size
        self.query = query
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.intervene_type is not None:
            result['InterveneType'] = self.intervene_type
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('InterveneType') is not None:
            self.intervene_type = m.get('InterveneType')
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListIntervenesResponseBodyDataInterveneList(TeaModel):
    def __init__(
        self,
        id: str = None,
        query: str = None,
    ):
        # id
        self.id = id
        self.query = query

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.query is not None:
            result['Query'] = self.query
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        return self


class ListIntervenesResponseBodyData(TeaModel):
    def __init__(
        self,
        intervene_list: List[ListIntervenesResponseBodyDataInterveneList] = None,
        page_index: int = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.intervene_list = intervene_list
        self.page_index = page_index
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.intervene_list:
            for k in self.intervene_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['InterveneList'] = []
        if self.intervene_list is not None:
            for k in self.intervene_list:
                result['InterveneList'].append(k.to_map() if k else None)
        if self.page_index is not None:
            result['PageIndex'] = self.page_index
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.intervene_list = []
        if m.get('InterveneList') is not None:
            for k in m.get('InterveneList'):
                temp_model = ListIntervenesResponseBodyDataInterveneList()
                self.intervene_list.append(temp_model.from_map(k))
        if m.get('PageIndex') is not None:
            self.page_index = m.get('PageIndex')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListIntervenesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListIntervenesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = ListIntervenesResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListIntervenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIntervenesResponseBody = None,
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
            temp_model = ListIntervenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMaterialDocumentsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        doc_type: str = None,
        doc_type_list: List[str] = None,
        generate_public_url: bool = None,
        id: int = None,
        keywords: List[str] = None,
        query: str = None,
        share_attr: int = None,
        size: int = None,
        title: str = None,
        update_time_end: str = None,
        update_time_start: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content = content
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.current = current
        self.doc_type = doc_type
        self.doc_type_list = doc_type_list
        self.generate_public_url = generate_public_url
        self.id = id
        self.keywords = keywords
        self.query = query
        self.share_attr = share_attr
        self.size = size
        self.title = title
        self.update_time_end = update_time_end
        self.update_time_start = update_time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_type_list is not None:
            result['DocTypeList'] = self.doc_type_list
        if self.generate_public_url is not None:
            result['GeneratePublicUrl'] = self.generate_public_url
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.query is not None:
            result['Query'] = self.query
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.size is not None:
            result['Size'] = self.size
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_end is not None:
            result['UpdateTimeEnd'] = self.update_time_end
        if self.update_time_start is not None:
            result['UpdateTimeStart'] = self.update_time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocTypeList') is not None:
            self.doc_type_list = m.get('DocTypeList')
        if m.get('GeneratePublicUrl') is not None:
            self.generate_public_url = m.get('GeneratePublicUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeEnd') is not None:
            self.update_time_end = m.get('UpdateTimeEnd')
        if m.get('UpdateTimeStart') is not None:
            self.update_time_start = m.get('UpdateTimeStart')
        return self


class ListMaterialDocumentsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        create_time_end: str = None,
        create_time_start: str = None,
        current: int = None,
        doc_type: str = None,
        doc_type_list_shrink: str = None,
        generate_public_url: bool = None,
        id: int = None,
        keywords_shrink: str = None,
        query: str = None,
        share_attr: int = None,
        size: int = None,
        title: str = None,
        update_time_end: str = None,
        update_time_start: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content = content
        self.create_time_end = create_time_end
        self.create_time_start = create_time_start
        self.current = current
        self.doc_type = doc_type
        self.doc_type_list_shrink = doc_type_list_shrink
        self.generate_public_url = generate_public_url
        self.id = id
        self.keywords_shrink = keywords_shrink
        self.query = query
        self.share_attr = share_attr
        self.size = size
        self.title = title
        self.update_time_end = update_time_end
        self.update_time_start = update_time_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time_end is not None:
            result['CreateTimeEnd'] = self.create_time_end
        if self.create_time_start is not None:
            result['CreateTimeStart'] = self.create_time_start
        if self.current is not None:
            result['Current'] = self.current
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.doc_type_list_shrink is not None:
            result['DocTypeList'] = self.doc_type_list_shrink
        if self.generate_public_url is not None:
            result['GeneratePublicUrl'] = self.generate_public_url
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.query is not None:
            result['Query'] = self.query
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.size is not None:
            result['Size'] = self.size
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time_end is not None:
            result['UpdateTimeEnd'] = self.update_time_end
        if self.update_time_start is not None:
            result['UpdateTimeStart'] = self.update_time_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTimeEnd') is not None:
            self.create_time_end = m.get('CreateTimeEnd')
        if m.get('CreateTimeStart') is not None:
            self.create_time_start = m.get('CreateTimeStart')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('DocTypeList') is not None:
            self.doc_type_list_shrink = m.get('DocTypeList')
        if m.get('GeneratePublicUrl') is not None:
            self.generate_public_url = m.get('GeneratePublicUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTimeEnd') is not None:
            self.update_time_end = m.get('UpdateTimeEnd')
        if m.get('UpdateTimeStart') is not None:
            self.update_time_start = m.get('UpdateTimeStart')
        return self


class ListMaterialDocumentsResponseBodyData(TeaModel):
    def __init__(
        self,
        author: str = None,
        create_time: str = None,
        create_user: str = None,
        create_user_name: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        public_url: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        thumbnail_in_base_64: str = None,
        title: str = None,
        update_time: str = None,
        update_user: str = None,
        update_user_name: str = None,
        url: str = None,
    ):
        self.author = author
        self.create_time = create_time
        self.create_user = create_user
        self.create_user_name = create_user_name
        self.doc_keywords = doc_keywords
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        self.id = id
        self.pub_time = pub_time
        self.public_url = public_url
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.thumbnail_in_base_64 = thumbnail_in_base_64
        self.title = title
        self.update_time = update_time
        self.update_user = update_user
        self.update_user_name = update_user_name
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.public_url is not None:
            result['PublicUrl'] = self.public_url
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.thumbnail_in_base_64 is not None:
            result['ThumbnailInBase64'] = self.thumbnail_in_base_64
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        if self.update_user_name is not None:
            result['UpdateUserName'] = self.update_user_name
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('PublicUrl') is not None:
            self.public_url = m.get('PublicUrl')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('ThumbnailInBase64') is not None:
            self.thumbnail_in_base_64 = m.get('ThumbnailInBase64')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        if m.get('UpdateUserName') is not None:
            self.update_user_name = m.get('UpdateUserName')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListMaterialDocumentsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[ListMaterialDocumentsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListMaterialDocumentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class ListMaterialDocumentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMaterialDocumentsResponseBody = None,
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
            temp_model = ListMaterialDocumentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPlanningProposalRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_id: str = None,
        custom_view_point_ids: List[str] = None,
        max_results: int = None,
        next_token: str = None,
        titles: List[str] = None,
        topic: str = None,
        topic_source: str = None,
        topic_version: str = None,
        view_point_type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.custom_view_point_id = custom_view_point_id
        self.custom_view_point_ids = custom_view_point_ids
        self.max_results = max_results
        self.next_token = next_token
        self.titles = titles
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source
        self.topic_version = topic_version
        # This parameter is required.
        self.view_point_type = view_point_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        if self.custom_view_point_ids is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.titles is not None:
            result['Titles'] = self.titles
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version
        if self.view_point_type is not None:
            result['ViewPointType'] = self.view_point_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids = m.get('CustomViewPointIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Titles') is not None:
            self.titles = m.get('Titles')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')
        if m.get('ViewPointType') is not None:
            self.view_point_type = m.get('ViewPointType')
        return self


class ListPlanningProposalShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        custom_view_point_id: str = None,
        custom_view_point_ids_shrink: str = None,
        max_results: int = None,
        next_token: str = None,
        titles_shrink: str = None,
        topic: str = None,
        topic_source: str = None,
        topic_version: str = None,
        view_point_type: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.custom_view_point_id = custom_view_point_id
        self.custom_view_point_ids_shrink = custom_view_point_ids_shrink
        self.max_results = max_results
        self.next_token = next_token
        self.titles_shrink = titles_shrink
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source
        self.topic_version = topic_version
        # This parameter is required.
        self.view_point_type = view_point_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        if self.custom_view_point_ids_shrink is not None:
            result['CustomViewPointIds'] = self.custom_view_point_ids_shrink
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.titles_shrink is not None:
            result['Titles'] = self.titles_shrink
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version
        if self.view_point_type is not None:
            result['ViewPointType'] = self.view_point_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        if m.get('CustomViewPointIds') is not None:
            self.custom_view_point_ids_shrink = m.get('CustomViewPointIds')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Titles') is not None:
            self.titles_shrink = m.get('Titles')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')
        if m.get('ViewPointType') is not None:
            self.view_point_type = m.get('ViewPointType')
        return self


class ListPlanningProposalResponseBodyDataOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListPlanningProposalResponseBodyData(TeaModel):
    def __init__(
        self,
        outlines: List[ListPlanningProposalResponseBodyDataOutlines] = None,
        summary: str = None,
        title: str = None,
    ):
        self.outlines = outlines
        self.summary = summary
        self.title = title

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListPlanningProposalResponseBodyDataOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListPlanningProposalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPlanningProposalResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListPlanningProposalResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListPlanningProposalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPlanningProposalResponseBody = None,
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
            temp_model = ListPlanningProposalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTimedViewAttitudeRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_source: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        return self


class ListTimedViewAttitudeResponseBodyDataViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListTimedViewAttitudeResponseBodyDataViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[ListTimedViewAttitudeResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListTimedViewAttitudeResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListTimedViewAttitudeResponseBodyData(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        pub_time: str = None,
        ratio: str = None,
        source: str = None,
        title: str = None,
        url: str = None,
        view_points: List[ListTimedViewAttitudeResponseBodyDataViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.pub_time = pub_time
        self.ratio = ratio
        self.source = source
        self.title = title
        self.url = url
        self.view_points = view_points

    def validate(self):
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = ListTimedViewAttitudeResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class ListTimedViewAttitudeResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTimedViewAttitudeResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListTimedViewAttitudeResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTimedViewAttitudeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTimedViewAttitudeResponseBody = None,
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
            temp_model = ListTimedViewAttitudeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicRecommendEventListRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTopicRecommendEventListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTopicRecommendEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicRecommendEventListResponseBody = None,
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
            temp_model = ListTopicRecommendEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTopicViewPointRecommendEventListRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        id: str = None,
        max_results: int = None,
        next_token: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.id = id
        self.max_results = max_results
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.id is not None:
            result['Id'] = self.id
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        return self


class ListTopicViewPointRecommendEventListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[str] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTopicViewPointRecommendEventListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTopicViewPointRecommendEventListResponseBody = None,
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
            temp_model = ListTopicViewPointRecommendEventListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListVersionsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        return self


class ListVersionsResponseBodyData(TeaModel):
    def __init__(
        self,
        concurrent_count: int = None,
        end_time: str = None,
        instance_count: int = None,
        instance_id: str = None,
        order_id: int = None,
        product_type: str = None,
        quota: int = None,
        start_time: str = None,
        use_quota: int = None,
        version_detail: str = None,
        version_name: str = None,
        version_status: int = None,
    ):
        self.concurrent_count = concurrent_count
        self.end_time = end_time
        self.instance_count = instance_count
        self.instance_id = instance_id
        self.order_id = order_id
        self.product_type = product_type
        self.quota = quota
        self.start_time = start_time
        self.use_quota = use_quota
        self.version_detail = version_detail
        self.version_name = version_name
        self.version_status = version_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.concurrent_count is not None:
            result['ConcurrentCount'] = self.concurrent_count
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_count is not None:
            result['InstanceCount'] = self.instance_count
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.product_type is not None:
            result['ProductType'] = self.product_type
        if self.quota is not None:
            result['Quota'] = self.quota
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.use_quota is not None:
            result['UseQuota'] = self.use_quota
        if self.version_detail is not None:
            result['VersionDetail'] = self.version_detail
        if self.version_name is not None:
            result['VersionName'] = self.version_name
        if self.version_status is not None:
            result['VersionStatus'] = self.version_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConcurrentCount') is not None:
            self.concurrent_count = m.get('ConcurrentCount')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceCount') is not None:
            self.instance_count = m.get('InstanceCount')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')
        if m.get('Quota') is not None:
            self.quota = m.get('Quota')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('UseQuota') is not None:
            self.use_quota = m.get('UseQuota')
        if m.get('VersionDetail') is not None:
            self.version_detail = m.get('VersionDetail')
        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')
        if m.get('VersionStatus') is not None:
            self.version_status = m.get('VersionStatus')
        return self


class ListVersionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListVersionsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
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
            for k in m.get('Data'):
                temp_model = ListVersionsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListVersionsResponseBody = None,
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
            temp_model = ListVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWebReviewPointsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        max_results: int = None,
        next_token: str = None,
        topic: str = None,
        topic_source: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.topic = topic
        # This parameter is required.
        self.topic_source = topic_source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        return self


class ListWebReviewPointsResponseBodyDataComments(TeaModel):
    def __init__(
        self,
        source: str = None,
        text: str = None,
        title: str = None,
        url: str = None,
        username: str = None,
    ):
        self.source = source
        self.text = text
        self.title = title
        self.url = url
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['Source'] = self.source
        if self.text is not None:
            result['Text'] = self.text
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class ListWebReviewPointsResponseBodyDataViewPointsOutlines(TeaModel):
    def __init__(
        self,
        outline: str = None,
        summary: str = None,
    ):
        self.outline = outline
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.outline is not None:
            result['Outline'] = self.outline
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListWebReviewPointsResponseBodyDataViewPoints(TeaModel):
    def __init__(
        self,
        outlines: List[ListWebReviewPointsResponseBodyDataViewPointsOutlines] = None,
        point: str = None,
        summary: str = None,
    ):
        self.outlines = outlines
        self.point = point
        self.summary = summary

    def validate(self):
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.point is not None:
            result['Point'] = self.point
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = ListWebReviewPointsResponseBodyDataViewPointsOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Point') is not None:
            self.point = m.get('Point')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListWebReviewPointsResponseBodyData(TeaModel):
    def __init__(
        self,
        attitude: str = None,
        attitude_type: str = None,
        comments: List[ListWebReviewPointsResponseBodyDataComments] = None,
        ratio: str = None,
        view_points: List[ListWebReviewPointsResponseBodyDataViewPoints] = None,
    ):
        self.attitude = attitude
        self.attitude_type = attitude_type
        self.comments = comments
        self.ratio = ratio
        self.view_points = view_points

    def validate(self):
        if self.comments:
            for k in self.comments:
                if k:
                    k.validate()
        if self.view_points:
            for k in self.view_points:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.attitude_type is not None:
            result['AttitudeType'] = self.attitude_type
        result['Comments'] = []
        if self.comments is not None:
            for k in self.comments:
                result['Comments'].append(k.to_map() if k else None)
        if self.ratio is not None:
            result['Ratio'] = self.ratio
        result['ViewPoints'] = []
        if self.view_points is not None:
            for k in self.view_points:
                result['ViewPoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('AttitudeType') is not None:
            self.attitude_type = m.get('AttitudeType')
        self.comments = []
        if m.get('Comments') is not None:
            for k in m.get('Comments'):
                temp_model = ListWebReviewPointsResponseBodyDataComments()
                self.comments.append(temp_model.from_map(k))
        if m.get('Ratio') is not None:
            self.ratio = m.get('Ratio')
        self.view_points = []
        if m.get('ViewPoints') is not None:
            for k in m.get('ViewPoints'):
                temp_model = ListWebReviewPointsResponseBodyDataViewPoints()
                self.view_points.append(temp_model.from_map(k))
        return self


class ListWebReviewPointsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListWebReviewPointsResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.message is not None:
            result['Message'] = self.message
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListWebReviewPointsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListWebReviewPointsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWebReviewPointsResponseBody = None,
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
            temp_model = ListWebReviewPointsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_id: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class QueryAsyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        create_user: str = None,
        task_code: str = None,
        task_error_message: str = None,
        task_id: str = None,
        task_intermediate_result: str = None,
        task_name: str = None,
        task_param: str = None,
        task_progress_message: str = None,
        task_result: str = None,
        task_retry_count: str = None,
        task_status: int = None,
        update_time: str = None,
        update_user: str = None,
    ):
        self.create_time = create_time
        self.create_user = create_user
        self.task_code = task_code
        self.task_error_message = task_error_message
        self.task_id = task_id
        self.task_intermediate_result = task_intermediate_result
        self.task_name = task_name
        self.task_param = task_param
        self.task_progress_message = task_progress_message
        self.task_result = task_result
        self.task_retry_count = task_retry_count
        self.task_status = task_status
        self.update_time = update_time
        self.update_user = update_user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.create_user is not None:
            result['CreateUser'] = self.create_user
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_error_message is not None:
            result['TaskErrorMessage'] = self.task_error_message
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        if self.task_progress_message is not None:
            result['TaskProgressMessage'] = self.task_progress_message
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_retry_count is not None:
            result['TaskRetryCount'] = self.task_retry_count
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.update_user is not None:
            result['UpdateUser'] = self.update_user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskErrorMessage') is not None:
            self.task_error_message = m.get('TaskErrorMessage')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        if m.get('TaskProgressMessage') is not None:
            self.task_progress_message = m.get('TaskProgressMessage')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskRetryCount') is not None:
            self.task_retry_count = m.get('TaskRetryCount')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')
        return self


class QueryAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: QueryAsyncTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = QueryAsyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryAsyncTaskResponseBody = None,
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
            temp_model = QueryAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunAbbreviationContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunAbbreviationContentResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunAbbreviationContentResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunAbbreviationContentResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunAbbreviationContentResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunAbbreviationContentResponseBodyPayloadOutput = None,
        usage: RunAbbreviationContentResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunAbbreviationContentResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunAbbreviationContentResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunAbbreviationContentResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunAbbreviationContentResponseBodyHeader = None,
        payload: RunAbbreviationContentResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Header') is not None:
            temp_model = RunAbbreviationContentResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunAbbreviationContentResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunAbbreviationContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunAbbreviationContentResponseBody = None,
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
            temp_model = RunAbbreviationContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunContinueContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunContinueContentResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunContinueContentResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunContinueContentResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunContinueContentResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunContinueContentResponseBodyPayloadOutput = None,
        usage: RunContinueContentResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunContinueContentResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunContinueContentResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunContinueContentResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunContinueContentResponseBodyHeader = None,
        payload: RunContinueContentResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Header') is not None:
            temp_model = RunContinueContentResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunContinueContentResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunContinueContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunContinueContentResponseBody = None,
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
            temp_model = RunContinueContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCustomHotTopicAnalysisRequest(TeaModel):
    def __init__(
        self,
        ask_user: str = None,
        force_analysis_exists_topic: bool = None,
        prompt: str = None,
        session_id: str = None,
        task_id: str = None,
        user_back: str = None,
        workspace_id: str = None,
    ):
        self.ask_user = ask_user
        self.force_analysis_exists_topic = force_analysis_exists_topic
        # This parameter is required.
        self.prompt = prompt
        self.session_id = session_id
        self.task_id = task_id
        self.user_back = user_back
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user
        if self.force_analysis_exists_topic is not None:
            result['ForceAnalysisExistsTopic'] = self.force_analysis_exists_topic
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.user_back is not None:
            result['UserBack'] = self.user_back
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')
        if m.get('ForceAnalysisExistsTopic') is not None:
            self.force_analysis_exists_topic = m.get('ForceAnalysisExistsTopic')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('UserBack') is not None:
            self.user_back = m.get('UserBack')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunCustomHotTopicAnalysisResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunCustomHotTopicAnalysisResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        articles: List[RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles] = None,
        ask_user: List[str] = None,
        async_task_id: str = None,
        attitude: str = None,
        search_query: str = None,
        text: str = None,
        topic_id: str = None,
    ):
        self.articles = articles
        self.ask_user = ask_user
        self.async_task_id = async_task_id
        self.attitude = attitude
        self.search_query = search_query
        self.text = text
        self.topic_id = topic_id

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.search_query is not None:
            result['SearchQuery'] = self.search_query
        if self.text is not None:
            result['Text'] = self.text
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunCustomHotTopicAnalysisResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class RunCustomHotTopicAnalysisResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunCustomHotTopicAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunCustomHotTopicAnalysisResponseBodyPayloadOutput = None,
        usage: RunCustomHotTopicAnalysisResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunCustomHotTopicAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunCustomHotTopicAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunCustomHotTopicAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        header: RunCustomHotTopicAnalysisResponseBodyHeader = None,
        payload: RunCustomHotTopicAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunCustomHotTopicAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunCustomHotTopicAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCustomHotTopicAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCustomHotTopicAnalysisResponseBody = None,
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
            temp_model = RunCustomHotTopicAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunCustomHotTopicViewPointAnalysisRequest(TeaModel):
    def __init__(
        self,
        ask_user: str = None,
        prompt: str = None,
        search_query: str = None,
        skip_ask_user: bool = None,
        topic: str = None,
        topic_id: str = None,
        topic_source: str = None,
        topic_version: str = None,
        user_back: str = None,
        workspace_id: str = None,
    ):
        self.ask_user = ask_user
        # This parameter is required.
        self.prompt = prompt
        self.search_query = search_query
        self.skip_ask_user = skip_ask_user
        self.topic = topic
        self.topic_id = topic_id
        self.topic_source = topic_source
        self.topic_version = topic_version
        self.user_back = user_back
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.search_query is not None:
            result['SearchQuery'] = self.search_query
        if self.skip_ask_user is not None:
            result['SkipAskUser'] = self.skip_ask_user
        if self.topic is not None:
            result['Topic'] = self.topic
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        if self.topic_source is not None:
            result['TopicSource'] = self.topic_source
        if self.topic_version is not None:
            result['TopicVersion'] = self.topic_version
        if self.user_back is not None:
            result['UserBack'] = self.user_back
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')
        if m.get('SkipAskUser') is not None:
            self.skip_ask_user = m.get('SkipAskUser')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        if m.get('TopicSource') is not None:
            self.topic_source = m.get('TopicSource')
        if m.get('TopicVersion') is not None:
            self.topic_version = m.get('TopicVersion')
        if m.get('UserBack') is not None:
            self.user_back = m.get('UserBack')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunCustomHotTopicViewPointAnalysisResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunCustomHotTopicViewPointAnalysisResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        ask_user: List[str] = None,
        async_task_id: str = None,
        attitude: str = None,
        custom_view_point_id: str = None,
        text: str = None,
        topic_id: str = None,
    ):
        self.ask_user = ask_user
        self.async_task_id = async_task_id
        self.attitude = attitude
        self.custom_view_point_id = custom_view_point_id
        self.text = text
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user
        if self.async_task_id is not None:
            result['AsyncTaskId'] = self.async_task_id
        if self.attitude is not None:
            result['Attitude'] = self.attitude
        if self.custom_view_point_id is not None:
            result['CustomViewPointId'] = self.custom_view_point_id
        if self.text is not None:
            result['Text'] = self.text
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')
        if m.get('AsyncTaskId') is not None:
            self.async_task_id = m.get('AsyncTaskId')
        if m.get('Attitude') is not None:
            self.attitude = m.get('Attitude')
        if m.get('CustomViewPointId') is not None:
            self.custom_view_point_id = m.get('CustomViewPointId')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class RunCustomHotTopicViewPointAnalysisResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunCustomHotTopicViewPointAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunCustomHotTopicViewPointAnalysisResponseBodyPayloadOutput = None,
        usage: RunCustomHotTopicViewPointAnalysisResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunCustomHotTopicViewPointAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunCustomHotTopicViewPointAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunCustomHotTopicViewPointAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        header: RunCustomHotTopicViewPointAnalysisResponseBodyHeader = None,
        payload: RunCustomHotTopicViewPointAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunCustomHotTopicViewPointAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunCustomHotTopicViewPointAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunCustomHotTopicViewPointAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunCustomHotTopicViewPointAnalysisResponseBody = None,
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
            temp_model = RunCustomHotTopicViewPointAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunExpandContentRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunExpandContentResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunExpandContentResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunExpandContentResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunExpandContentResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunExpandContentResponseBodyPayloadOutput = None,
        usage: RunExpandContentResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunExpandContentResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunExpandContentResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunExpandContentResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunExpandContentResponseBodyHeader = None,
        payload: RunExpandContentResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Header') is not None:
            temp_model = RunExpandContentResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunExpandContentResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunExpandContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunExpandContentResponseBody = None,
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
            temp_model = RunExpandContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunKeywordsExtractionGenerationRequestReferenceData(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
    ):
        # This parameter is required.
        self.contents = contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RunKeywordsExtractionGenerationRequest(TeaModel):
    def __init__(
        self,
        reference_data: RunKeywordsExtractionGenerationRequestReferenceData = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.reference_data = reference_data
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceData') is not None:
            temp_model = RunKeywordsExtractionGenerationRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunKeywordsExtractionGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        reference_data_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunKeywordsExtractionGenerationResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunKeywordsExtractionGenerationResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunKeywordsExtractionGenerationResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunKeywordsExtractionGenerationResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunKeywordsExtractionGenerationResponseBodyPayloadOutput = None,
        usage: RunKeywordsExtractionGenerationResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunKeywordsExtractionGenerationResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunKeywordsExtractionGenerationResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunKeywordsExtractionGenerationResponseBody(TeaModel):
    def __init__(
        self,
        header: RunKeywordsExtractionGenerationResponseBodyHeader = None,
        payload: RunKeywordsExtractionGenerationResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunKeywordsExtractionGenerationResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunKeywordsExtractionGenerationResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunKeywordsExtractionGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunKeywordsExtractionGenerationResponseBody = None,
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
            temp_model = RunKeywordsExtractionGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunStepByStepWritingRequestReferenceDataArticles(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        media_url: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.media_url = media_url
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunStepByStepWritingRequestReferenceDataOutlinesArticles(TeaModel):
    def __init__(
        self,
        content: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.title = title
        self.url = url

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
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunStepByStepWritingRequestReferenceDataOutlines(TeaModel):
    def __init__(
        self,
        articles: List[RunStepByStepWritingRequestReferenceDataOutlinesArticles] = None,
        outline: str = None,
    ):
        self.articles = articles
        self.outline = outline

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.outline is not None:
            result['Outline'] = self.outline
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunStepByStepWritingRequestReferenceDataOutlinesArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('Outline') is not None:
            self.outline = m.get('Outline')
        return self


class RunStepByStepWritingRequestReferenceData(TeaModel):
    def __init__(
        self,
        articles: List[RunStepByStepWritingRequestReferenceDataArticles] = None,
        mini_doc: List[str] = None,
        outlines: List[RunStepByStepWritingRequestReferenceDataOutlines] = None,
        summarization: List[str] = None,
    ):
        self.articles = articles
        self.mini_doc = mini_doc
        self.outlines = outlines
        self.summarization = summarization

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()
        if self.outlines:
            for k in self.outlines:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc
        result['Outlines'] = []
        if self.outlines is not None:
            for k in self.outlines:
                result['Outlines'].append(k.to_map() if k else None)
        if self.summarization is not None:
            result['Summarization'] = self.summarization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunStepByStepWritingRequestReferenceDataArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')
        self.outlines = []
        if m.get('Outlines') is not None:
            for k in m.get('Outlines'):
                temp_model = RunStepByStepWritingRequestReferenceDataOutlines()
                self.outlines.append(temp_model.from_map(k))
        if m.get('Summarization') is not None:
            self.summarization = m.get('Summarization')
        return self


class RunStepByStepWritingRequestWritingConfigPromptTag(TeaModel):
    def __init__(
        self,
        necessary_tips: str = None,
        position: str = None,
        reverse_words: str = None,
        theme: str = None,
    ):
        self.necessary_tips = necessary_tips
        self.position = position
        self.reverse_words = reverse_words
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.necessary_tips is not None:
            result['NecessaryTips'] = self.necessary_tips
        if self.position is not None:
            result['Position'] = self.position
        if self.reverse_words is not None:
            result['ReverseWords'] = self.reverse_words
        if self.theme is not None:
            result['Theme'] = self.theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NecessaryTips') is not None:
            self.necessary_tips = m.get('NecessaryTips')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('ReverseWords') is not None:
            self.reverse_words = m.get('ReverseWords')
        if m.get('Theme') is not None:
            self.theme = m.get('Theme')
        return self


class RunStepByStepWritingRequestWritingConfigTags(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        tag: str = None,
    ):
        self.keyword = keyword
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class RunStepByStepWritingRequestWritingConfig(TeaModel):
    def __init__(
        self,
        domain: str = None,
        keywords: List[str] = None,
        prompt_tag: RunStepByStepWritingRequestWritingConfigPromptTag = None,
        scene: str = None,
        step: str = None,
        tags: List[RunStepByStepWritingRequestWritingConfigTags] = None,
        use_search: bool = None,
    ):
        self.domain = domain
        self.keywords = keywords
        self.prompt_tag = prompt_tag
        self.scene = scene
        self.step = step
        self.tags = tags
        self.use_search = use_search

    def validate(self):
        if self.prompt_tag:
            self.prompt_tag.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt_tag is not None:
            result['PromptTag'] = self.prompt_tag.to_map()
        if self.scene is not None:
            result['Scene'] = self.scene
        if self.step is not None:
            result['Step'] = self.step
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.use_search is not None:
            result['UseSearch'] = self.use_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('PromptTag') is not None:
            temp_model = RunStepByStepWritingRequestWritingConfigPromptTag()
            self.prompt_tag = temp_model.from_map(m['PromptTag'])
        if m.get('Scene') is not None:
            self.scene = m.get('Scene')
        if m.get('Step') is not None:
            self.step = m.get('Step')
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RunStepByStepWritingRequestWritingConfigTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')
        return self


class RunStepByStepWritingRequest(TeaModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data: RunStepByStepWritingRequestReferenceData = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config: RunStepByStepWritingRequestWritingConfig = None,
    ):
        self.origin_session_id = origin_session_id
        # This parameter is required.
        self.prompt = prompt
        self.reference_data = reference_data
        self.session_id = session_id
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_config = writing_config

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()
        if self.writing_config:
            self.writing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.writing_config is not None:
            result['WritingConfig'] = self.writing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            temp_model = RunStepByStepWritingRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WritingConfig') is not None:
            temp_model = RunStepByStepWritingRequestWritingConfig()
            self.writing_config = temp_model.from_map(m['WritingConfig'])
        return self


class RunStepByStepWritingShrinkRequest(TeaModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data_shrink: str = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config_shrink: str = None,
    ):
        self.origin_session_id = origin_session_id
        # This parameter is required.
        self.prompt = prompt
        self.reference_data_shrink = reference_data_shrink
        self.session_id = session_id
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_config_shrink = writing_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.writing_config_shrink is not None:
            result['WritingConfig'] = self.writing_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WritingConfig') is not None:
            self.writing_config_shrink = m.get('WritingConfig')
        return self


class RunStepByStepWritingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunStepByStepWritingResponseBodyPayloadOutputArticles(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        media_url: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.media_url = media_url
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.media_url is not None:
            result['MediaUrl'] = self.media_url
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('MediaUrl') is not None:
            self.media_url = m.get('MediaUrl')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunStepByStepWritingResponseBodyPayloadOutputExtraOutput(TeaModel):
    def __init__(
        self,
        summarization: List[str] = None,
    ):
        self.summarization = summarization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summarization is not None:
            result['summarization'] = self.summarization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('summarization') is not None:
            self.summarization = m.get('summarization')
        return self


class RunStepByStepWritingResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        articles: List[RunStepByStepWritingResponseBodyPayloadOutputArticles] = None,
        extra_output: RunStepByStepWritingResponseBodyPayloadOutputExtraOutput = None,
        mini_doc: List[str] = None,
        search_query: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.extra_output = extra_output
        self.mini_doc = mini_doc
        self.search_query = search_query
        self.text = text

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()
        if self.extra_output:
            self.extra_output.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.extra_output is not None:
            result['ExtraOutput'] = self.extra_output.to_map()
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc
        if self.search_query is not None:
            result['SearchQuery'] = self.search_query
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunStepByStepWritingResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('ExtraOutput') is not None:
            temp_model = RunStepByStepWritingResponseBodyPayloadOutputExtraOutput()
            self.extra_output = temp_model.from_map(m['ExtraOutput'])
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')
        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunStepByStepWritingResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunStepByStepWritingResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunStepByStepWritingResponseBodyPayloadOutput = None,
        usage: RunStepByStepWritingResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunStepByStepWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunStepByStepWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunStepByStepWritingResponseBody(TeaModel):
    def __init__(
        self,
        header: RunStepByStepWritingResponseBodyHeader = None,
        payload: RunStepByStepWritingResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunStepByStepWritingResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunStepByStepWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunStepByStepWritingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunStepByStepWritingResponseBody = None,
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
            temp_model = RunStepByStepWritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunStyleFeatureAnalysisRequest(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
        material_ids: List[int] = None,
        workspace_id: str = None,
    ):
        self.contents = contents
        self.material_ids = material_ids
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        if self.material_ids is not None:
            result['MaterialIds'] = self.material_ids
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        if m.get('MaterialIds') is not None:
            self.material_ids = m.get('MaterialIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunStyleFeatureAnalysisShrinkRequest(TeaModel):
    def __init__(
        self,
        contents_shrink: str = None,
        material_ids_shrink: str = None,
        workspace_id: str = None,
    ):
        self.contents_shrink = contents_shrink
        self.material_ids_shrink = material_ids_shrink
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents_shrink is not None:
            result['Contents'] = self.contents_shrink
        if self.material_ids_shrink is not None:
            result['MaterialIds'] = self.material_ids_shrink
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents_shrink = m.get('Contents')
        if m.get('MaterialIds') is not None:
            self.material_ids_shrink = m.get('MaterialIds')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunStyleFeatureAnalysisResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunStyleFeatureAnalysisResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunStyleFeatureAnalysisResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunStyleFeatureAnalysisResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunStyleFeatureAnalysisResponseBodyPayloadOutput = None,
        usage: RunStyleFeatureAnalysisResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunStyleFeatureAnalysisResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunStyleFeatureAnalysisResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunStyleFeatureAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunStyleFeatureAnalysisResponseBodyHeader = None,
        payload: RunStyleFeatureAnalysisResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Header') is not None:
            temp_model = RunStyleFeatureAnalysisResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunStyleFeatureAnalysisResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunStyleFeatureAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunStyleFeatureAnalysisResponseBody = None,
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
            temp_model = RunStyleFeatureAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunSummaryGenerateRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        prompt: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.prompt = prompt
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunSummaryGenerateResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.event_info is not None:
            result['EventInfo'] = self.event_info
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunSummaryGenerateResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunSummaryGenerateResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunSummaryGenerateResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunSummaryGenerateResponseBodyPayloadOutput = None,
        usage: RunSummaryGenerateResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunSummaryGenerateResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunSummaryGenerateResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunSummaryGenerateResponseBody(TeaModel):
    def __init__(
        self,
        end: bool = None,
        header: RunSummaryGenerateResponseBodyHeader = None,
        payload: RunSummaryGenerateResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.end = end
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['End'] = self.end
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')
        if m.get('Header') is not None:
            temp_model = RunSummaryGenerateResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunSummaryGenerateResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunSummaryGenerateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunSummaryGenerateResponseBody = None,
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
            temp_model = RunSummaryGenerateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunTextPolishingRequest(TeaModel):
    def __init__(
        self,
        content: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.content = content
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunTextPolishingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunTextPolishingResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunTextPolishingResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunTextPolishingResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunTextPolishingResponseBodyPayloadOutput = None,
        usage: RunTextPolishingResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunTextPolishingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunTextPolishingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunTextPolishingResponseBody(TeaModel):
    def __init__(
        self,
        header: RunTextPolishingResponseBodyHeader = None,
        payload: RunTextPolishingResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunTextPolishingResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunTextPolishingResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunTextPolishingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunTextPolishingResponseBody = None,
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
            temp_model = RunTextPolishingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunTitleGenerationRequestReferenceData(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
    ):
        # This parameter is required.
        self.contents = contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RunTitleGenerationRequest(TeaModel):
    def __init__(
        self,
        reference_data: RunTitleGenerationRequestReferenceData = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.reference_data = reference_data
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceData') is not None:
            temp_model = RunTitleGenerationRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunTitleGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        reference_data_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunTitleGenerationResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.session_id = session_id
        self.status_code = status_code
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunTitleGenerationResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunTitleGenerationResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunTitleGenerationResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunTitleGenerationResponseBodyPayloadOutput = None,
        usage: RunTitleGenerationResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunTitleGenerationResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunTitleGenerationResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunTitleGenerationResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        header: RunTitleGenerationResponseBodyHeader = None,
        http_status_code: str = None,
        message: str = None,
        payload: RunTitleGenerationResponseBodyPayload = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.header = header
        self.http_status_code = http_status_code
        self.message = message
        self.payload = payload
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Header') is not None:
            temp_model = RunTitleGenerationResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Payload') is not None:
            temp_model = RunTitleGenerationResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RunTitleGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunTitleGenerationResponseBody = None,
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
            temp_model = RunTitleGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunTranslateGenerationRequestReferenceData(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
    ):
        # This parameter is required.
        self.contents = contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RunTranslateGenerationRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data: RunTranslateGenerationRequestReferenceData = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.reference_data = reference_data
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            temp_model = RunTranslateGenerationRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunTranslateGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunTranslateGenerationResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunTranslateGenerationResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunTranslateGenerationResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunTranslateGenerationResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunTranslateGenerationResponseBodyPayloadOutput = None,
        usage: RunTranslateGenerationResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunTranslateGenerationResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunTranslateGenerationResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunTranslateGenerationResponseBody(TeaModel):
    def __init__(
        self,
        header: RunTranslateGenerationResponseBodyHeader = None,
        payload: RunTranslateGenerationResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunTranslateGenerationResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunTranslateGenerationResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunTranslateGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunTranslateGenerationResponseBody = None,
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
            temp_model = RunTranslateGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunWriteToneGenerationRequestReferenceData(TeaModel):
    def __init__(
        self,
        contents: List[str] = None,
    ):
        # This parameter is required.
        self.contents = contents

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.contents is not None:
            result['Contents'] = self.contents
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Contents') is not None:
            self.contents = m.get('Contents')
        return self


class RunWriteToneGenerationRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data: RunWriteToneGenerationRequestReferenceData = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.reference_data = reference_data
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            temp_model = RunWriteToneGenerationRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunWriteToneGenerationShrinkRequest(TeaModel):
    def __init__(
        self,
        prompt: str = None,
        reference_data_shrink: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.prompt = prompt
        # This parameter is required.
        self.reference_data_shrink = reference_data_shrink
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        return self


class RunWriteToneGenerationResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunWriteToneGenerationResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        text: str = None,
    ):
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunWriteToneGenerationResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
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
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunWriteToneGenerationResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunWriteToneGenerationResponseBodyPayloadOutput = None,
        usage: RunWriteToneGenerationResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunWriteToneGenerationResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunWriteToneGenerationResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunWriteToneGenerationResponseBody(TeaModel):
    def __init__(
        self,
        header: RunWriteToneGenerationResponseBodyHeader = None,
        payload: RunWriteToneGenerationResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunWriteToneGenerationResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunWriteToneGenerationResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunWriteToneGenerationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunWriteToneGenerationResponseBody = None,
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
            temp_model = RunWriteToneGenerationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunWritingRequestReferenceDataArticles(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunWritingRequestReferenceData(TeaModel):
    def __init__(
        self,
        articles: List[RunWritingRequestReferenceDataArticles] = None,
    ):
        self.articles = articles

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunWritingRequestReferenceDataArticles()
                self.articles.append(temp_model.from_map(k))
        return self


class RunWritingRequestWritingConfigPromptTag(TeaModel):
    def __init__(
        self,
        necessary_tips: str = None,
        position: str = None,
        reverse_words: str = None,
        theme: str = None,
    ):
        self.necessary_tips = necessary_tips
        self.position = position
        self.reverse_words = reverse_words
        self.theme = theme

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.necessary_tips is not None:
            result['NecessaryTips'] = self.necessary_tips
        if self.position is not None:
            result['Position'] = self.position
        if self.reverse_words is not None:
            result['ReverseWords'] = self.reverse_words
        if self.theme is not None:
            result['Theme'] = self.theme
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NecessaryTips') is not None:
            self.necessary_tips = m.get('NecessaryTips')
        if m.get('Position') is not None:
            self.position = m.get('Position')
        if m.get('ReverseWords') is not None:
            self.reverse_words = m.get('ReverseWords')
        if m.get('Theme') is not None:
            self.theme = m.get('Theme')
        return self


class RunWritingRequestWritingConfigTags(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        tag: str = None,
    ):
        self.keyword = keyword
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class RunWritingRequestWritingConfig(TeaModel):
    def __init__(
        self,
        domain: str = None,
        prompt_tag: RunWritingRequestWritingConfigPromptTag = None,
        tags: List[RunWritingRequestWritingConfigTags] = None,
        use_search: bool = None,
    ):
        self.domain = domain
        self.prompt_tag = prompt_tag
        self.tags = tags
        self.use_search = use_search

    def validate(self):
        if self.prompt_tag:
            self.prompt_tag.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.prompt_tag is not None:
            result['PromptTag'] = self.prompt_tag.to_map()
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        if self.use_search is not None:
            result['UseSearch'] = self.use_search
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PromptTag') is not None:
            temp_model = RunWritingRequestWritingConfigPromptTag()
            self.prompt_tag = temp_model.from_map(m['PromptTag'])
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = RunWritingRequestWritingConfigTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('UseSearch') is not None:
            self.use_search = m.get('UseSearch')
        return self


class RunWritingRequest(TeaModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data: RunWritingRequestReferenceData = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config: RunWritingRequestWritingConfig = None,
    ):
        self.origin_session_id = origin_session_id
        # This parameter is required.
        self.prompt = prompt
        self.reference_data = reference_data
        self.session_id = session_id
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_config = writing_config

    def validate(self):
        if self.reference_data:
            self.reference_data.validate()
        if self.writing_config:
            self.writing_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data is not None:
            result['ReferenceData'] = self.reference_data.to_map()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.writing_config is not None:
            result['WritingConfig'] = self.writing_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            temp_model = RunWritingRequestReferenceData()
            self.reference_data = temp_model.from_map(m['ReferenceData'])
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WritingConfig') is not None:
            temp_model = RunWritingRequestWritingConfig()
            self.writing_config = temp_model.from_map(m['WritingConfig'])
        return self


class RunWritingShrinkRequest(TeaModel):
    def __init__(
        self,
        origin_session_id: str = None,
        prompt: str = None,
        reference_data_shrink: str = None,
        session_id: str = None,
        task_id: str = None,
        workspace_id: str = None,
        writing_config_shrink: str = None,
    ):
        self.origin_session_id = origin_session_id
        # This parameter is required.
        self.prompt = prompt
        self.reference_data_shrink = reference_data_shrink
        self.session_id = session_id
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id
        self.writing_config_shrink = writing_config_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.reference_data_shrink is not None:
            result['ReferenceData'] = self.reference_data_shrink
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id
        if self.writing_config_shrink is not None:
            result['WritingConfig'] = self.writing_config_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('ReferenceData') is not None:
            self.reference_data_shrink = m.get('ReferenceData')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')
        if m.get('WritingConfig') is not None:
            self.writing_config_shrink = m.get('WritingConfig')
        return self


class RunWritingResponseBodyHeader(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        origin_session_id: str = None,
        session_id: str = None,
        status_code: int = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.origin_session_id = origin_session_id
        self.session_id = session_id
        self.status_code = status_code
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.event is not None:
            result['Event'] = self.event
        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('Event') is not None:
            self.event = m.get('Event')
        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class RunWritingResponseBodyPayloadOutputArticles(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RunWritingResponseBodyPayloadOutput(TeaModel):
    def __init__(
        self,
        articles: List[RunWritingResponseBodyPayloadOutputArticles] = None,
        mini_doc: List[str] = None,
        search_query: str = None,
        text: str = None,
    ):
        self.articles = articles
        self.mini_doc = mini_doc
        self.search_query = search_query
        self.text = text

    def validate(self):
        if self.articles:
            for k in self.articles:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Articles'] = []
        if self.articles is not None:
            for k in self.articles:
                result['Articles'].append(k.to_map() if k else None)
        if self.mini_doc is not None:
            result['MiniDoc'] = self.mini_doc
        if self.search_query is not None:
            result['SearchQuery'] = self.search_query
        if self.text is not None:
            result['Text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.articles = []
        if m.get('Articles') is not None:
            for k in m.get('Articles'):
                temp_model = RunWritingResponseBodyPayloadOutputArticles()
                self.articles.append(temp_model.from_map(k))
        if m.get('MiniDoc') is not None:
            self.mini_doc = m.get('MiniDoc')
        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')
        if m.get('Text') is not None:
            self.text = m.get('Text')
        return self


class RunWritingResponseBodyPayloadUsage(TeaModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        token_map: Dict[str, int] = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.token_map = token_map
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens
        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens
        if self.token_map is not None:
            result['TokenMap'] = self.token_map
        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')
        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')
        if m.get('TokenMap') is not None:
            self.token_map = m.get('TokenMap')
        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')
        return self


class RunWritingResponseBodyPayload(TeaModel):
    def __init__(
        self,
        output: RunWritingResponseBodyPayloadOutput = None,
        usage: RunWritingResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.output is not None:
            result['Output'] = self.output.to_map()
        if self.usage is not None:
            result['Usage'] = self.usage.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = RunWritingResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m['Output'])
        if m.get('Usage') is not None:
            temp_model = RunWritingResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m['Usage'])
        return self


class RunWritingResponseBody(TeaModel):
    def __init__(
        self,
        header: RunWritingResponseBodyHeader = None,
        payload: RunWritingResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = RunWritingResponseBodyHeader()
            self.header = temp_model.from_map(m['Header'])
        if m.get('Payload') is not None:
            temp_model = RunWritingResponseBodyPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RunWritingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunWritingResponseBody = None,
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
            temp_model = RunWritingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveCustomTextRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
        content: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code
        self.content = content
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.content is not None:
            result['Content'] = self.content
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SaveCustomTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveCustomTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveCustomTextResponseBody = None,
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
            temp_model = SaveCustomTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveDataSourceOrderConfigRequestUserConfigDataSourceList(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
        number: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.code = code
        self.name = name
        # This parameter is required.
        self.number = number
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        if self.number is not None:
            result['Number'] = self.number
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Number') is not None:
            self.number = m.get('Number')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class SaveDataSourceOrderConfigRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        product_code: str = None,
        user_config_data_source_list: List[SaveDataSourceOrderConfigRequestUserConfigDataSourceList] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.user_config_data_source_list = user_config_data_source_list

    def validate(self):
        if self.user_config_data_source_list:
            for k in self.user_config_data_source_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        result['UserConfigDataSourceList'] = []
        if self.user_config_data_source_list is not None:
            for k in self.user_config_data_source_list:
                result['UserConfigDataSourceList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        self.user_config_data_source_list = []
        if m.get('UserConfigDataSourceList') is not None:
            for k in m.get('UserConfigDataSourceList'):
                temp_model = SaveDataSourceOrderConfigRequestUserConfigDataSourceList()
                self.user_config_data_source_list.append(temp_model.from_map(k))
        return self


class SaveDataSourceOrderConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        product_code: str = None,
        user_config_data_source_list_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.product_code = product_code
        # This parameter is required.
        self.user_config_data_source_list_shrink = user_config_data_source_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.product_code is not None:
            result['ProductCode'] = self.product_code
        if self.user_config_data_source_list_shrink is not None:
            result['UserConfigDataSourceList'] = self.user_config_data_source_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')
        if m.get('UserConfigDataSourceList') is not None:
            self.user_config_data_source_list_shrink = m.get('UserConfigDataSourceList')
        return self


class SaveDataSourceOrderConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveDataSourceOrderConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveDataSourceOrderConfigResponseBody = None,
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
            temp_model = SaveDataSourceOrderConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveMaterialDocumentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        author: str = None,
        both_save_private_and_share: bool = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        pub_time: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.author = author
        self.both_save_private_and_share = both_save_private_and_share
        self.doc_keywords = doc_keywords
        # This parameter is required.
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        self.pub_time = pub_time
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.both_save_private_and_share is not None:
            result['BothSavePrivateAndShare'] = self.both_save_private_and_share
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('BothSavePrivateAndShare') is not None:
            self.both_save_private_and_share = m.get('BothSavePrivateAndShare')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SaveMaterialDocumentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        author: str = None,
        both_save_private_and_share: bool = None,
        doc_keywords_shrink: str = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        pub_time: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.author = author
        self.both_save_private_and_share = both_save_private_and_share
        self.doc_keywords_shrink = doc_keywords_shrink
        # This parameter is required.
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        self.pub_time = pub_time
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.both_save_private_and_share is not None:
            result['BothSavePrivateAndShare'] = self.both_save_private_and_share
        if self.doc_keywords_shrink is not None:
            result['DocKeywords'] = self.doc_keywords_shrink
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('BothSavePrivateAndShare') is not None:
            self.both_save_private_and_share = m.get('BothSavePrivateAndShare')
        if m.get('DocKeywords') is not None:
            self.doc_keywords_shrink = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SaveMaterialDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveMaterialDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SaveMaterialDocumentResponseBody = None,
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
            temp_model = SaveMaterialDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchNewsRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        filter_not_null: bool = None,
        include_content: bool = None,
        page: int = None,
        page_size: int = None,
        query: str = None,
        search_sources: List[str] = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.filter_not_null = filter_not_null
        self.include_content = include_content
        self.page = page
        self.page_size = page_size
        self.query = query
        self.search_sources = search_sources

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.filter_not_null is not None:
            result['FilterNotNull'] = self.filter_not_null
        if self.include_content is not None:
            result['IncludeContent'] = self.include_content
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.search_sources is not None:
            result['SearchSources'] = self.search_sources
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FilterNotNull') is not None:
            self.filter_not_null = m.get('FilterNotNull')
        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchSources') is not None:
            self.search_sources = m.get('SearchSources')
        return self


class SearchNewsShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        filter_not_null: bool = None,
        include_content: bool = None,
        page: int = None,
        page_size: int = None,
        query: str = None,
        search_sources_shrink: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.filter_not_null = filter_not_null
        self.include_content = include_content
        self.page = page
        self.page_size = page_size
        self.query = query
        self.search_sources_shrink = search_sources_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.filter_not_null is not None:
            result['FilterNotNull'] = self.filter_not_null
        if self.include_content is not None:
            result['IncludeContent'] = self.include_content
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.search_sources_shrink is not None:
            result['SearchSources'] = self.search_sources_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('FilterNotNull') is not None:
            self.filter_not_null = m.get('FilterNotNull')
        if m.get('IncludeContent') is not None:
            self.include_content = m.get('IncludeContent')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('SearchSources') is not None:
            self.search_sources_shrink = m.get('SearchSources')
        return self


class SearchNewsResponseBodyData(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        doc_uuid: str = None,
        image_urls: List[str] = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        source: str = None,
        summary: str = None,
        tag: str = None,
        title: str = None,
        update_time: str = None,
        url: str = None,
    ):
        self.author = author
        self.content = content
        self.doc_uuid = doc_uuid
        self.image_urls = image_urls
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.source = source
        self.summary = summary
        self.tag = tag
        self.title = title
        self.update_time = update_time
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.search_source is not None:
            result['SearchSource'] = self.search_source
        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.title is not None:
            result['Title'] = self.title
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')
        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SearchNewsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        current: int = None,
        data: List[SearchNewsResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
    ):
        self.code = code
        self.current = current
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total

    def validate(self):
        if self.data:
            for k in self.data:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.current is not None:
            result['Current'] = self.current
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.size is not None:
            result['Size'] = self.size
        if self.success is not None:
            result['Success'] = self.success
        if self.total is not None:
            result['Total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Current') is not None:
            self.current = m.get('Current')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = SearchNewsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Total') is not None:
            self.total = m.get('Total')
        return self


class SearchNewsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchNewsResponseBody = None,
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
            temp_model = SearchNewsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        task_code: str = None,
        task_execute_time: str = None,
        task_name: str = None,
        task_param: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.task_code = task_code
        self.task_execute_time = task_execute_time
        self.task_name = task_name
        self.task_param = task_param

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.task_code is not None:
            result['TaskCode'] = self.task_code
        if self.task_execute_time is not None:
            result['TaskExecuteTime'] = self.task_execute_time
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_param is not None:
            result['TaskParam'] = self.task_param
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('TaskCode') is not None:
            self.task_code = m.get('TaskCode')
        if m.get('TaskExecuteTime') is not None:
            self.task_execute_time = m.get('TaskExecuteTime')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')
        return self


class SubmitAsyncTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_intermediate_result: Any = None,
        task_name: str = None,
    ):
        self.task_id = task_id
        self.task_intermediate_result = task_intermediate_result
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_intermediate_result is not None:
            result['TaskIntermediateResult'] = self.task_intermediate_result
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskIntermediateResult') is not None:
            self.task_intermediate_result = m.get('TaskIntermediateResult')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class SubmitAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitAsyncTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SubmitAsyncTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitAsyncTaskResponseBody = None,
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
            temp_model = SubmitAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequestDocuments(TeaModel):
    def __init__(
        self,
        author: str = None,
        content: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        # This parameter is required.
        self.content = content
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        if self.content is not None:
            result['Content'] = self.content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents: List[SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequestDocuments] = None,
        prompt: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents = documents
        # This parameter is required.
        self.prompt = prompt
        self.topic = topic

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = SubmitCustomTopicSelectionPerspectiveAnalysisTaskRequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        prompt: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents_shrink = documents_shrink
        # This parameter is required.
        self.prompt = prompt
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData(TeaModel):
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
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBody = None,
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
            temp_model = SubmitCustomTopicSelectionPerspectiveAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitDocClusterTaskRequestDocuments(TeaModel):
    def __init__(
        self,
        content: str = None,
        doc_id: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.content = content
        self.doc_id = doc_id
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SubmitDocClusterTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents: List[SubmitDocClusterTaskRequestDocuments] = None,
        summary_length: int = None,
        title_length: int = None,
        topic_count: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.documents = documents
        self.summary_length = summary_length
        self.title_length = title_length
        self.topic_count = topic_count

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.summary_length is not None:
            result['SummaryLength'] = self.summary_length
        if self.title_length is not None:
            result['TitleLength'] = self.title_length
        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = SubmitDocClusterTaskRequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('SummaryLength') is not None:
            self.summary_length = m.get('SummaryLength')
        if m.get('TitleLength') is not None:
            self.title_length = m.get('TitleLength')
        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')
        return self


class SubmitDocClusterTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        summary_length: int = None,
        title_length: int = None,
        topic_count: int = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        # This parameter is required.
        self.documents_shrink = documents_shrink
        self.summary_length = summary_length
        self.title_length = title_length
        self.topic_count = topic_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.summary_length is not None:
            result['SummaryLength'] = self.summary_length
        if self.title_length is not None:
            result['TitleLength'] = self.title_length
        if self.topic_count is not None:
            result['TopicCount'] = self.topic_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('SummaryLength') is not None:
            self.summary_length = m.get('SummaryLength')
        if m.get('TitleLength') is not None:
            self.title_length = m.get('TitleLength')
        if m.get('TopicCount') is not None:
            self.topic_count = m.get('TopicCount')
        return self


class SubmitDocClusterTaskResponseBodyData(TeaModel):
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
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class SubmitDocClusterTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitDocClusterTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SubmitDocClusterTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitDocClusterTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitDocClusterTaskResponseBody = None,
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
            temp_model = SubmitDocClusterTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments(TeaModel):
    def __init__(
        self,
        text: str = None,
        username: str = None,
    ):
        self.text = text
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.text is not None:
            result['Text'] = self.text
        if self.username is not None:
            result['Username'] = self.username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Text') is not None:
            self.text = m.get('Text')
        if m.get('Username') is not None:
            self.username = m.get('Username')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments(TeaModel):
    def __init__(
        self,
        author: str = None,
        comments: List[SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments] = None,
        content: str = None,
        pub_time: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.author = author
        self.comments = comments
        # This parameter is required.
        self.content = content
        self.pub_time = pub_time
        self.source = source
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        if self.comments:
            for k in self.comments:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author is not None:
            result['Author'] = self.author
        result['Comments'] = []
        if self.comments is not None:
            for k in self.comments:
                result['Comments'].append(k.to_map() if k else None)
        if self.content is not None:
            result['Content'] = self.content
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.source is not None:
            result['Source'] = self.source
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Author') is not None:
            self.author = m.get('Author')
        self.comments = []
        if m.get('Comments') is not None:
            for k in m.get('Comments'):
                temp_model = SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocumentsComments()
                self.comments.append(temp_model.from_map(k))
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents: List[SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments] = None,
        perspective_types: List[str] = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents = documents
        self.perspective_types = perspective_types
        self.topic = topic

    def validate(self):
        if self.documents:
            for k in self.documents:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        result['Documents'] = []
        if self.documents is not None:
            for k in self.documents:
                result['Documents'].append(k.to_map() if k else None)
        if self.perspective_types is not None:
            result['PerspectiveTypes'] = self.perspective_types
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        self.documents = []
        if m.get('Documents') is not None:
            for k in m.get('Documents'):
                temp_model = SubmitTopicSelectionPerspectiveAnalysisTaskRequestDocuments()
                self.documents.append(temp_model.from_map(k))
        if m.get('PerspectiveTypes') is not None:
            self.perspective_types = m.get('PerspectiveTypes')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        documents_shrink: str = None,
        perspective_types_shrink: str = None,
        topic: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.documents_shrink = documents_shrink
        self.perspective_types_shrink = perspective_types_shrink
        self.topic = topic

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.documents_shrink is not None:
            result['Documents'] = self.documents_shrink
        if self.perspective_types_shrink is not None:
            result['PerspectiveTypes'] = self.perspective_types_shrink
        if self.topic is not None:
            result['Topic'] = self.topic
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Documents') is not None:
            self.documents_shrink = m.get('Documents')
        if m.get('PerspectiveTypes') is not None:
            self.perspective_types_shrink = m.get('PerspectiveTypes')
        if m.get('Topic') is not None:
            self.topic = m.get('Topic')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        task_id: str = None,
        task_name: str = None,
    ):
        self.task_id = task_id
        self.task_name = task_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: SubmitTopicSelectionPerspectiveAnalysisTaskResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
        if self.code is not None:
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data.to_map()
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
        if m.get('Data') is not None:
            temp_model = SubmitTopicSelectionPerspectiveAnalysisTaskResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SubmitTopicSelectionPerspectiveAnalysisTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SubmitTopicSelectionPerspectiveAnalysisTaskResponseBody = None,
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
            temp_model = SubmitTopicSelectionPerspectiveAnalysisTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCustomTextRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        commodity_code: str = None,
        content: str = None,
        id: int = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.commodity_code = commodity_code
        self.content = content
        # This parameter is required.
        self.id = id
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code
        if self.content is not None:
            result['Content'] = self.content
        if self.id is not None:
            result['Id'] = self.id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateCustomTextResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCustomTextResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCustomTextResponseBody = None,
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
            temp_model = UpdateCustomTextResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGeneratedContentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_text: str = None,
        id: int = None,
        keywords: List[str] = None,
        prompt: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content = content
        self.content_text = content_text
        # This parameter is required.
        self.id = id
        self.keywords = keywords
        self.prompt = prompt
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords is not None:
            result['Keywords'] = self.keywords
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGeneratedContentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        content: str = None,
        content_text: str = None,
        id: int = None,
        keywords_shrink: str = None,
        prompt: str = None,
        title: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.content = content
        self.content_text = content_text
        # This parameter is required.
        self.id = id
        self.keywords_shrink = keywords_shrink
        self.prompt = prompt
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.content is not None:
            result['Content'] = self.content
        if self.content_text is not None:
            result['ContentText'] = self.content_text
        if self.id is not None:
            result['Id'] = self.id
        if self.keywords_shrink is not None:
            result['Keywords'] = self.keywords_shrink
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentText') is not None:
            self.content_text = m.get('ContentText')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Keywords') is not None:
            self.keywords_shrink = m.get('Keywords')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGeneratedContentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: bool = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateGeneratedContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGeneratedContentResponseBody = None,
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
            temp_model = UpdateGeneratedContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMaterialDocumentRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        author: str = None,
        doc_keywords: List[str] = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        region_id: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.author = author
        self.doc_keywords = doc_keywords
        # This parameter is required.
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        # This parameter is required.
        self.id = id
        self.pub_time = pub_time
        self.region_id = region_id
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.doc_keywords is not None:
            result['DocKeywords'] = self.doc_keywords
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('DocKeywords') is not None:
            self.doc_keywords = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateMaterialDocumentShrinkRequest(TeaModel):
    def __init__(
        self,
        agent_key: str = None,
        author: str = None,
        doc_keywords_shrink: str = None,
        doc_type: str = None,
        external_url: str = None,
        html_content: str = None,
        id: int = None,
        pub_time: str = None,
        region_id: str = None,
        share_attr: int = None,
        src_from: str = None,
        summary: str = None,
        text_content: str = None,
        title: str = None,
        url: str = None,
    ):
        # This parameter is required.
        self.agent_key = agent_key
        self.author = author
        self.doc_keywords_shrink = doc_keywords_shrink
        # This parameter is required.
        self.doc_type = doc_type
        self.external_url = external_url
        self.html_content = html_content
        # This parameter is required.
        self.id = id
        self.pub_time = pub_time
        self.region_id = region_id
        self.share_attr = share_attr
        self.src_from = src_from
        self.summary = summary
        self.text_content = text_content
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_key is not None:
            result['AgentKey'] = self.agent_key
        if self.author is not None:
            result['Author'] = self.author
        if self.doc_keywords_shrink is not None:
            result['DocKeywords'] = self.doc_keywords_shrink
        if self.doc_type is not None:
            result['DocType'] = self.doc_type
        if self.external_url is not None:
            result['ExternalUrl'] = self.external_url
        if self.html_content is not None:
            result['HtmlContent'] = self.html_content
        if self.id is not None:
            result['Id'] = self.id
        if self.pub_time is not None:
            result['PubTime'] = self.pub_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.share_attr is not None:
            result['ShareAttr'] = self.share_attr
        if self.src_from is not None:
            result['SrcFrom'] = self.src_from
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.text_content is not None:
            result['TextContent'] = self.text_content
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentKey') is not None:
            self.agent_key = m.get('AgentKey')
        if m.get('Author') is not None:
            self.author = m.get('Author')
        if m.get('DocKeywords') is not None:
            self.doc_keywords_shrink = m.get('DocKeywords')
        if m.get('DocType') is not None:
            self.doc_type = m.get('DocType')
        if m.get('ExternalUrl') is not None:
            self.external_url = m.get('ExternalUrl')
        if m.get('HtmlContent') is not None:
            self.html_content = m.get('HtmlContent')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ShareAttr') is not None:
            self.share_attr = m.get('ShareAttr')
        if m.get('SrcFrom') is not None:
            self.src_from = m.get('SrcFrom')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TextContent') is not None:
            self.text_content = m.get('TextContent')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class UpdateMaterialDocumentResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: int = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['Code'] = self.code
        if self.data is not None:
            result['Data'] = self.data
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
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMaterialDocumentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMaterialDocumentResponseBody = None,
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
            temp_model = UpdateMaterialDocumentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


