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


class GetAIQueryResultRequest(TeaModel):
    def __init__(
        self,
        analysis_id: str = None,
    ):
        self.analysis_id = analysis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        return self


class GetAIQueryResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
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
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetAIQueryResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAIQueryResultResponseBody = None,
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
            temp_model = GetAIQueryResultResponseBody()
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
        show_pod: int = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.end = end
        # This parameter is required.
        self.instance = instance
        self.namespace = namespace
        self.pod = pod
        self.show_pod = show_pod
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
        if self.show_pod is not None:
            result['showPod'] = self.show_pod
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
        if m.get('showPod') is not None:
            self.show_pod = m.get('showPod')
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


class GetAgentRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
    ):
        self.agent_id = agent_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        return self


class GetAgentResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        install_script: str = None,
        uninstall_script: str = None,
        updated_at: str = None,
        upgrade_script: str = None,
        version: str = None,
    ):
        self.created_at = created_at
        self.install_script = install_script
        self.uninstall_script = uninstall_script
        self.updated_at = updated_at
        self.upgrade_script = upgrade_script
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.install_script is not None:
            result['install_script'] = self.install_script
        if self.uninstall_script is not None:
            result['uninstall_script'] = self.uninstall_script
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upgrade_script is not None:
            result['upgrade_script'] = self.upgrade_script
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('install_script') is not None:
            self.install_script = m.get('install_script')
        if m.get('uninstall_script') is not None:
            self.uninstall_script = m.get('uninstall_script')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upgrade_script') is not None:
            self.upgrade_script = m.get('upgrade_script')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetAgentResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        support_arch: str = None,
        type: str = None,
        updated_at: str = None,
        versions: List[GetAgentResponseBodyDataVersions] = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.support_arch = support_arch
        self.type = type
        self.updated_at = updated_at
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.support_arch is not None:
            result['support_arch'] = self.support_arch
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('support_arch') is not None:
            self.support_arch = m.get('support_arch')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = GetAgentResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class GetAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: GetAgentResponseBodyData = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentResponseBody = None,
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
            temp_model = GetAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAgentTaskRequest(TeaModel):
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


class GetAgentTaskResponseBodyDataJobs(TeaModel):
    def __init__(
        self,
        error: str = None,
        instance: str = None,
        params: Any = None,
        region: str = None,
        result: str = None,
        status: str = None,
    ):
        self.error = error
        self.instance = instance
        self.params = params
        self.region = region
        self.result = result
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['error'] = self.error
        if self.instance is not None:
            result['instance'] = self.instance
        if self.params is not None:
            result['params'] = self.params
        if self.region is not None:
            result['region'] = self.region
        if self.result is not None:
            result['result'] = self.result
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetAgentTaskResponseBodyData(TeaModel):
    def __init__(
        self,
        jobs: List[GetAgentTaskResponseBodyDataJobs] = None,
        task_id: str = None,
    ):
        self.jobs = jobs
        self.task_id = task_id

    def validate(self):
        if self.jobs:
            for k in self.jobs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['jobs'] = []
        if self.jobs is not None:
            for k in self.jobs:
                result['jobs'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = GetAgentTaskResponseBodyDataJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetAgentTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: GetAgentTaskResponseBodyData = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetAgentTaskResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class GetAgentTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAgentTaskResponseBody = None,
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
            temp_model = GetAgentTaskResponseBody()
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


class GetHostCountRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        end: float = None,
        instance: str = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.end = end
        self.instance = instance
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


class GetHostCountResponseBodyData(TeaModel):
    def __init__(
        self,
        time: int = None,
        value: int = None,
    ):
        self.time = time
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetHostCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetHostCountResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetHostCountResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetHostCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHostCountResponseBody = None,
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
            temp_model = GetHostCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotAnalysisRequest(TeaModel):
    def __init__(
        self,
        app_type: str = None,
        beg_end: int = None,
        beg_start: int = None,
        instance: str = None,
        pid: int = None,
        table: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.instance = instance
        self.pid = pid
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_type is not None:
            result['appType'] = self.app_type
        if self.beg_end is not None:
            result['beg_end'] = self.beg_end
        if self.beg_start is not None:
            result['beg_start'] = self.beg_start
        if self.instance is not None:
            result['instance'] = self.instance
        if self.pid is not None:
            result['pid'] = self.pid
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appType') is not None:
            self.app_type = m.get('appType')
        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')
        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetHotspotAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetHotspotAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotspotAnalysisResponseBody = None,
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
            temp_model = GetHotspotAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotInstanceListRequest(TeaModel):
    def __init__(
        self,
        beg_end: int = None,
        beg_start: int = None,
        table: str = None,
    ):
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beg_end is not None:
            result['beg_end'] = self.beg_end
        if self.beg_start is not None:
            result['beg_start'] = self.beg_start
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')
        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetHotspotInstanceListResponseBodyData(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[str] = None,
    ):
        self.columns = columns
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetHotspotInstanceListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotspotInstanceListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetHotspotInstanceListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHotspotInstanceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotspotInstanceListResponseBody = None,
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
            temp_model = GetHotspotInstanceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotPidListRequest(TeaModel):
    def __init__(
        self,
        beg_end: int = None,
        beg_start: int = None,
        instance: str = None,
        table: str = None,
    ):
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.instance = instance
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beg_end is not None:
            result['beg_end'] = self.beg_end
        if self.beg_start is not None:
            result['beg_start'] = self.beg_start
        if self.instance is not None:
            result['instance'] = self.instance
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')
        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetHotspotPidListResponseBodyData(TeaModel):
    def __init__(
        self,
        columns: List[str] = None,
        values: List[List[str]] = None,
    ):
        self.columns = columns
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.columns is not None:
            result['columns'] = self.columns
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('columns') is not None:
            self.columns = m.get('columns')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetHotspotPidListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotspotPidListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetHotspotPidListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHotspotPidListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotspotPidListResponseBody = None,
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
            temp_model = GetHotspotPidListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListRecordRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
    ):
        self.current = current
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class GetListRecordResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis_id: str = None,
        analysis_time: str = None,
        arguments: str = None,
        failed_log: str = None,
        status: str = None,
    ):
        self.analysis_id = analysis_id
        self.analysis_time = analysis_time
        self.arguments = arguments
        self.failed_log = failed_log
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.analysis_time is not None:
            result['analysisTime'] = self.analysis_time
        if self.arguments is not None:
            result['arguments'] = self.arguments
        if self.failed_log is not None:
            result['failedLog'] = self.failed_log
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('analysisTime') is not None:
            self.analysis_time = m.get('analysisTime')
        if m.get('arguments') is not None:
            self.arguments = m.get('arguments')
        if m.get('failedLog') is not None:
            self.failed_log = m.get('failedLog')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetListRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetListRecordResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetListRecordResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetListRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetListRecordResponseBody = None,
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
            temp_model = GetListRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProblemPercentageRequest(TeaModel):
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


class GetProblemPercentageResponseBodyData(TeaModel):
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


class GetProblemPercentageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetProblemPercentageResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetProblemPercentageResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetProblemPercentageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProblemPercentageResponseBody = None,
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
            temp_model = GetProblemPercentageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRangeScoreRequest(TeaModel):
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


class GetRangeScoreResponseBodyData(TeaModel):
    def __init__(
        self,
        time: float = None,
        type: str = None,
        value: float = None,
    ):
        self.time = time
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.time is not None:
            result['time'] = self.time
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class GetRangeScoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetRangeScoreResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        total: float = None,
    ):
        # 代表资源一级ID的资源属性字段
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetRangeScoreResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetRangeScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRangeScoreResponseBody = None,
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
            temp_model = GetRangeScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourcesRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        instance: str = None,
        type: str = None,
    ):
        self.cluster = cluster
        self.instance = instance
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster is not None:
            result['cluster'] = self.cluster
        if self.instance is not None:
            result['instance'] = self.instance
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetResourcesResponseBodyData(TeaModel):
    def __init__(
        self,
        total: float = None,
        unit: str = None,
        usage: float = None,
    ):
        self.total = total
        self.unit = unit
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total is not None:
            result['total'] = self.total
        if self.unit is not None:
            result['unit'] = self.unit
        if self.usage is not None:
            result['usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        return self


class GetResourcesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetResourcesResponseBodyData = None,
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
            temp_model = GetResourcesResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        return self


class GetResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourcesResponseBody = None,
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
            temp_model = GetResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InstallAgentRequestInstances(TeaModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance = instance
        # This parameter is required.
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


class InstallAgentRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        install_type: str = None,
        instances: List[InstallAgentRequestInstances] = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.agent_version = agent_version
        # This parameter is required.
        self.install_type = install_type
        # This parameter is required.
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
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        if self.install_type is not None:
            result['install_type'] = self.install_type
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        if m.get('install_type') is not None:
            self.install_type = m.get('install_type')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = InstallAgentRequestInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class InstallAgentResponseBodyData(TeaModel):
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


class InstallAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: InstallAgentResponseBodyData = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = InstallAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class InstallAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallAgentResponseBody = None,
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
            temp_model = InstallAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvokeAnomalyDiagnosisRequest(TeaModel):
    def __init__(
        self,
        uuid: str = None,
    ):
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class InvokeAnomalyDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
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
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class InvokeAnomalyDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvokeAnomalyDiagnosisResponseBody = None,
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
            temp_model = InvokeAnomalyDiagnosisResponseBody()
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


class ListAbnormalyEventsRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        current: int = None,
        end: float = None,
        instance: str = None,
        level: str = None,
        namespace: str = None,
        page_size: int = None,
        pod: str = None,
        show_pod: int = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.current = current
        self.end = end
        self.instance = instance
        self.level = level
        self.namespace = namespace
        self.page_size = page_size
        self.pod = pod
        self.show_pod = show_pod
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
        if self.current is not None:
            result['current'] = self.current
        if self.end is not None:
            result['end'] = self.end
        if self.instance is not None:
            result['instance'] = self.instance
        if self.level is not None:
            result['level'] = self.level
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.pod is not None:
            result['pod'] = self.pod
        if self.show_pod is not None:
            result['showPod'] = self.show_pod
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('pod') is not None:
            self.pod = m.get('pod')
        if m.get('showPod') is not None:
            self.show_pod = m.get('showPod')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListAbnormalyEventsResponseBodyDataOpts(TeaModel):
    def __init__(
        self,
        label: str = None,
        params: str = None,
        type: str = None,
    ):
        self.label = label
        self.params = params
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.params is not None:
            result['params'] = self.params
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAbnormalyEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: float = None,
        description: str = None,
        id: str = None,
        instance: str = None,
        item: str = None,
        opts: ListAbnormalyEventsResponseBodyDataOpts = None,
        region_id: str = None,
        type: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.instance = instance
        self.item = item
        self.opts = opts
        self.region_id = region_id
        self.type = type

    def validate(self):
        if self.opts:
            self.opts.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.instance is not None:
            result['instance'] = self.instance
        if self.item is not None:
            result['item'] = self.item
        if self.opts is not None:
            result['opts'] = self.opts.to_map()
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('item') is not None:
            self.item = m.get('item')
        if m.get('opts') is not None:
            temp_model = ListAbnormalyEventsResponseBodyDataOpts()
            self.opts = temp_model.from_map(m['opts'])
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAbnormalyEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAbnormalyEventsResponseBodyData] = None,
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
                temp_model = ListAbnormalyEventsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListAbnormalyEventsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAbnormalyEventsResponseBody = None,
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
            temp_model = ListAbnormalyEventsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentInstallRecordsRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        instance_id: str = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_version: str = None,
        status: str = None,
    ):
        self.current = current
        self.instance_id = instance_id
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListAgentInstallRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        instance_id: str = None,
        plugin_id: str = None,
        plugin_version: str = None,
        status: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.instance_id = instance_id
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ListAgentInstallRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListAgentInstallRecordsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAgentInstallRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentInstallRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentInstallRecordsResponseBody = None,
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
            temp_model = ListAgentInstallRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAgentsRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        name: str = None,
        page_size: int = None,
        type: str = None,
    ):
        self.current = current
        self.name = name
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.name is not None:
            result['name'] = self.name
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAgentsResponseBodyDataVersions(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        install_script: str = None,
        uninstall_script: str = None,
        updated_at: str = None,
        upgrade_script: str = None,
        version: str = None,
    ):
        self.created_at = created_at
        self.install_script = install_script
        self.uninstall_script = uninstall_script
        self.updated_at = updated_at
        self.upgrade_script = upgrade_script
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.install_script is not None:
            result['install_script'] = self.install_script
        if self.uninstall_script is not None:
            result['uninstall_script'] = self.uninstall_script
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upgrade_script is not None:
            result['upgrade_script'] = self.upgrade_script
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('install_script') is not None:
            self.install_script = m.get('install_script')
        if m.get('uninstall_script') is not None:
            self.uninstall_script = m.get('uninstall_script')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upgrade_script') is not None:
            self.upgrade_script = m.get('upgrade_script')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListAgentsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        id: str = None,
        name: str = None,
        support_arch: str = None,
        type: str = None,
        updated_at: str = None,
        versions: List[ListAgentsResponseBodyDataVersions] = None,
    ):
        self.created_at = created_at
        self.description = description
        self.id = id
        self.name = name
        self.support_arch = support_arch
        self.type = type
        self.updated_at = updated_at
        self.versions = versions

    def validate(self):
        if self.versions:
            for k in self.versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.support_arch is not None:
            result['support_arch'] = self.support_arch
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('support_arch') is not None:
            self.support_arch = m.get('support_arch')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListAgentsResponseBodyDataVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListAgentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListAgentsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.message is not None:
            result['message'] = self.message
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAgentsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListAgentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAgentsResponseBody = None,
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
            temp_model = ListAgentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceHealthRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        current: int = None,
        end: float = None,
        instance: str = None,
        page_size: int = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.current = current
        # This parameter is required.
        self.end = end
        self.instance = instance
        self.page_size = page_size
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
        if self.current is not None:
            result['current'] = self.current
        if self.end is not None:
            result['end'] = self.end
        if self.instance is not None:
            result['instance'] = self.instance
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class ListInstanceHealthResponseBodyData(TeaModel):
    def __init__(
        self,
        images: List[str] = None,
        instance: str = None,
        namespace: str = None,
        pod: str = None,
        region_id: str = None,
        score: float = None,
        status: str = None,
    ):
        self.images = images
        self.instance = instance
        self.namespace = namespace
        self.pod = pod
        self.region_id = region_id
        self.score = score
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.images is not None:
            result['images'] = self.images
        if self.instance is not None:
            result['instance'] = self.instance
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.pod is not None:
            result['pod'] = self.pod
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.score is not None:
            result['score'] = self.score
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('images') is not None:
            self.images = m.get('images')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('pod') is not None:
            self.pod = m.get('pod')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('score') is not None:
            self.score = m.get('score')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstanceHealthResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListInstanceHealthResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        total: int = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.total = total

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
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListInstanceHealthResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListInstanceHealthResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceHealthResponseBody = None,
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
            temp_model = ListInstanceHealthResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAIAnalysisRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        comms: str = None,
        instance: str = None,
        pids: str = None,
        region: str = None,
        timeout: int = None,
    ):
        self.channel = channel
        self.comms = comms
        self.instance = instance
        self.pids = pids
        self.region = region
        self.timeout = timeout

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.comms is not None:
            result['comms'] = self.comms
        if self.instance is not None:
            result['instance'] = self.instance
        if self.pids is not None:
            result['pids'] = self.pids
        if self.region is not None:
            result['region'] = self.region
        if self.timeout is not None:
            result['timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('comms') is not None:
            self.comms = m.get('comms')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pids') is not None:
            self.pids = m.get('pids')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        return self


class StartAIAnalysisResponseBodyData(TeaModel):
    def __init__(
        self,
        analysis_id: str = None,
    ):
        self.analysis_id = analysis_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysis_id'] = self.analysis_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysis_id') is not None:
            self.analysis_id = m.get('analysis_id')
        return self


class StartAIAnalysisResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: StartAIAnalysisResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = StartAIAnalysisResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class StartAIAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAIAnalysisResponseBody = None,
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
            temp_model = StartAIAnalysisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UninstallAgentRequestInstances(TeaModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance = instance
        # This parameter is required.
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


class UninstallAgentRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        instances: List[UninstallAgentRequestInstances] = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.agent_version = agent_version
        # This parameter is required.
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
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = UninstallAgentRequestInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class UninstallAgentResponseBodyData(TeaModel):
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


class UninstallAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: UninstallAgentResponseBodyData = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UninstallAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UninstallAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallAgentResponseBody = None,
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
            temp_model = UninstallAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeAgentRequestInstances(TeaModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.instance = instance
        # This parameter is required.
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


class UpgradeAgentRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        instances: List[UpgradeAgentRequestInstances] = None,
    ):
        # This parameter is required.
        self.agent_id = agent_id
        # This parameter is required.
        self.agent_version = agent_version
        # This parameter is required.
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
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        result['instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        self.instances = []
        if m.get('instances') is not None:
            for k in m.get('instances'):
                temp_model = UpgradeAgentRequestInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class UpgradeAgentResponseBodyData(TeaModel):
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


class UpgradeAgentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: UpgradeAgentResponseBodyData = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.message is not None:
            result['message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = UpgradeAgentResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpgradeAgentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeAgentResponseBody = None,
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
            temp_model = UpgradeAgentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


