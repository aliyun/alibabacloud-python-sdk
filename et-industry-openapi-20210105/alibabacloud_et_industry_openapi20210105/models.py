# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict


class OpenApiInvokeRequest(TeaModel):
    def __init__(
        self,
        service_id: str = None,
        type: str = None,
        node_id: str = None,
        params: str = None,
        job_id: str = None,
    ):
        # 服务Id
        self.service_id = service_id
        # 类型，EXPERIMENT-画布,NODE-节点
        self.type = type
        # 节点id
        self.node_id = node_id
        self.params = params
        # 任务id，需要全局唯一
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.service_id is not None:
            result['serviceId'] = self.service_id
        if self.type is not None:
            result['type'] = self.type
        if self.node_id is not None:
            result['nodeId'] = self.node_id
        if self.params is not None:
            result['params'] = self.params
        if self.job_id is not None:
            result['jobId'] = self.job_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('serviceId') is not None:
            self.service_id = m.get('serviceId')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('nodeId') is not None:
            self.node_id = m.get('nodeId')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        return self


class OpenApiInvokeResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        code: str = None,
        message: str = None,
        data: str = None,
        rid: str = None,
        inner_code: str = None,
    ):
        # 是否成功
        self.success = success
        # 返回码
        self.code = code
        # 消息
        self.message = message
        # 结果
        self.data = data
        self.rid = rid
        # 内部, 统一错误码
        self.inner_code = inner_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.code is not None:
            result['code'] = self.code
        if self.message is not None:
            result['message'] = self.message
        if self.data is not None:
            result['data'] = self.data
        if self.rid is not None:
            result['rid'] = self.rid
        if self.inner_code is not None:
            result['innerCode'] = self.inner_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('rid') is not None:
            self.rid = m.get('rid')
        if m.get('innerCode') is not None:
            self.inner_code = m.get('innerCode')
        return self


class OpenApiInvokeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OpenApiInvokeResponseBody = None,
    ):
        self.headers = headers
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = OpenApiInvokeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


