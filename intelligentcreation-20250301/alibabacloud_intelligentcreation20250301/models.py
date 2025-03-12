# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class CreateLabelTaskRequest(TeaModel):
    def __init__(
        self,
        callback_url: str = None,
        file_url: str = None,
        idempotent_id: str = None,
        label_template_id: str = None,
    ):
        self.callback_url = callback_url
        # This parameter is required.
        self.file_url = file_url
        self.idempotent_id = idempotent_id
        # This parameter is required.
        self.label_template_id = label_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.file_url is not None:
            result['FileUrl'] = self.file_url
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.label_template_id is not None:
            result['LabelTemplateId'] = self.label_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('LabelTemplateId') is not None:
            self.label_template_id = m.get('LabelTemplateId')
        return self


class CreateLabelTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_id: str = None,
    ):
        self.request_id = request_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateLabelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateLabelTaskResponseBody = None,
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
            temp_model = CreateLabelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateOssUploadTokenRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        file_type: str = None,
    ):
        self.file_name = file_name
        self.file_type = file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.file_type is not None:
            result['FileType'] = self.file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')
        return self


class CreateOssUploadTokenResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        expire_time: str = None,
        host: str = None,
        key: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        url: str = None,
    ):
        self.access_id = access_id
        self.expire_time = expire_time
        self.host = host
        self.key = key
        self.policy = policy
        self.request_id = request_id
        self.signature = signature
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['AccessId'] = self.access_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.host is not None:
            result['Host'] = self.host
        if self.key is not None:
            result['Key'] = self.key
        if self.policy is not None:
            result['Policy'] = self.policy
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CreateOssUploadTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOssUploadTokenResponseBody = None,
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
            temp_model = CreateOssUploadTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTextLabelRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        label_template_id: str = None,
    ):
        self.data = data
        self.label_template_id = label_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.label_template_id is not None:
            result['LabelTemplateId'] = self.label_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('LabelTemplateId') is not None:
            self.label_template_id = m.get('LabelTemplateId')
        return self


class CreateTextLabelResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        request_id: str = None,
        tokens: str = None,
    ):
        self.data = data
        self.request_id = request_id
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tokens is not None:
            result['Tokens'] = self.tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')
        return self


class CreateTextLabelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTextLabelResponseBody = None,
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
            temp_model = CreateTextLabelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLabelTaskResultRequest(TeaModel):
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


class GetLabelTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result_data_url: str = None,
        status: str = None,
        tokens: str = None,
    ):
        self.request_id = request_id
        self.result_data_url = result_data_url
        self.status = status
        self.tokens = tokens

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result_data_url is not None:
            result['ResultDataUrl'] = self.result_data_url
        if self.status is not None:
            result['Status'] = self.status
        if self.tokens is not None:
            result['Tokens'] = self.tokens
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResultDataUrl') is not None:
            self.result_data_url = m.get('ResultDataUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tokens') is not None:
            self.tokens = m.get('Tokens')
        return self


class GetLabelTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLabelTaskResultResponseBody = None,
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
            temp_model = GetLabelTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


