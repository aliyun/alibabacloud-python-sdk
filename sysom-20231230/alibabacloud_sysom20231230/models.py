# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Any, Dict


class AuthDiagnosisRequestInstances(TeaModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        self.instance = instance
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['instance'] = self.instance
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class AuthDiagnosisRequest(TeaModel):
    def __init__(
        self,
        auto_create_role: bool = None,
        auto_install_agent: bool = None,
        instances: List[AuthDiagnosisRequestInstances] = None,
    ):
        self.auto_create_role = auto_create_role
        self.auto_install_agent = auto_install_agent
        self.instances = instances

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_role is not None:
            result['autoCreateRole'] = self.auto_create_role
        if self.auto_install_agent is not None:
            result['autoInstallAgent'] = self.auto_install_agent
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoCreateRole') is not None:
            self.auto_create_role = m.get('autoCreateRole')
        if m.get('autoInstallAgent') is not None:
            self.auto_install_agent = m.get('autoInstallAgent')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = AuthDiagnosisRequestInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class AuthDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

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
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class AuthDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthDiagnosisResponseBody = None,
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
            temp_model = AuthDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GenerateCopilotResponseRequest(TeaModel):
    def __init__(
        self,
        llm_param_string: str = None,
    ):
        self.llm_param_string = llm_param_string

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.llm_param_string is not None:
            result['llmParamString'] = self.llm_param_string
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('llmParamString') is not None:
            self.llm_param_string = m.get('llmParamString')
        return self


class GenerateCopilotResponseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        massage: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.massage = massage
        # Id of the request
        self.request_id = request_id

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
        if self.massage is not None:
            result['massage'] = self.massage
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('massage') is not None:
            self.massage = m.get('massage')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GenerateCopilotResponseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCopilotResponseResponseBody = None,
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
            temp_model = GenerateCopilotResponseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAbnormalEventsCountRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        end: float = None,
        instance: str = None,
        namespace: str = None,
        pod: str = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.end = end
        # This parameter is required.
        self.instance = instance
        self.namespace = namespace
        self.pod = pod
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.end is not None:
            result['end'] = self.end
        if self.instance is not None:
            result['instance'] = self.instance
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.pod is not None:
            result['pod'] = self.pod
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('pod') is not None:
            self.pod = m.get('pod')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class GetAbnormalEventsCountResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetAbnormalEventsCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetAbnormalEventsCountResponseBodyData] = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message

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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetAbnormalEventsCountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAbnormalEventsCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAbnormalEventsCountResponseBody = None,
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
            temp_model = GetAbnormalEventsCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisResultRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetDiagnosisResultResponseBodyData(TeaModel):
    def __init__(
        self,
        code: int = None,
        command: Any = None,
        created_at: str = None,
        err_msg: str = None,
        params: Any = None,
        result: Any = None,
        service_name: str = None,
        status: str = None,
        task_id: str = None,
        updated_at: str = None,
        url: str = None,
    ):
        self.code = code
        self.command = command
        self.created_at = created_at
        self.err_msg = err_msg
        self.params = params
        self.result = result
        self.service_name = service_name
        self.status = status
        self.task_id = task_id
        self.updated_at = updated_at
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.command is not None:
            result['command'] = self.command
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.err_msg is not None:
            result['err_msg'] = self.err_msg
        if self.params is not None:
            result['params'] = self.params
        if self.result is not None:
            result['result'] = self.result
        if self.service_name is not None:
            result['service_name'] = self.service_name
        if self.status is not None:
            result['status'] = self.status
        if self.task_id is not None:
            result['task_id'] = self.task_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('command') is not None:
            self.command = m.get('command')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('err_msg') is not None:
            self.err_msg = m.get('err_msg')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDiagnosisResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetDiagnosisResultResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetDiagnosisResultResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class GetDiagnosisResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDiagnosisResultResponseBody = None,
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
            temp_model = GetDiagnosisResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHealthPercentageRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        end: float = None,
        instance: str = None,
        start: float = None,
    ):
        self.cluster = cluster
        # This parameter is required.
        self.end = end
        self.instance = instance
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.end is not None:
            result['end'] = self.end
        if self.instance is not None:
            result['instance'] = self.instance
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class GetHealthPercentageResponseBodyData(TeaModel):
    def __init__(
        self,
        type: str = None,
        value: int = None,
    ):
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetHealthPercentageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetHealthPercentageResponseBodyData] = None,
        message: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message

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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetHealthPercentageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetHealthPercentageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHealthPercentageResponseBody = None,
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
            temp_model = GetHealthPercentageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeDiagnosisRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        params: str = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.params is not None:
            result['params'] = self.params
        if self.service_name is not None:
            result['service_name'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        return self


class InvokeDiagnosisResponseBodyData(TeaModel):
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
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class InvokeDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: InvokeDiagnosisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = InvokeDiagnosisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class InvokeDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokeDiagnosisResponseBody = None,
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
            temp_model = InvokeDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


