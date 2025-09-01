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


class CheckInstanceSupportRequest(TeaModel):
    def __init__(
        self,
        instances: List[str] = None,
        region: str = None,
    ):
        self.instances = instances
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instances is not None:
            result['instances'] = self.instances
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instances') is not None:
            self.instances = m.get('instances')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class CheckInstanceSupportResponseBodyData(TeaModel):
    def __init__(
        self,
        instance: str = None,
        reason: str = None,
        support: bool = None,
    ):
        self.instance = instance
        self.reason = reason
        self.support = support

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance is not None:
            result['instance'] = self.instance
        if self.reason is not None:
            result['reason'] = self.reason
        if self.support is not None:
            result['support'] = self.support
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('reason') is not None:
            self.reason = m.get('reason')
        if m.get('support') is not None:
            self.support = m.get('support')
        return self


class CheckInstanceSupportResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[CheckInstanceSupportResponseBodyData] = None,
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = CheckInstanceSupportResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CheckInstanceSupportResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckInstanceSupportResponseBody = None,
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
            temp_model = CheckInstanceSupportResponseBody()
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


class GenerateCopilotStreamResponseRequest(TeaModel):
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


class GenerateCopilotStreamResponseResponseBody(TeaModel):
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


class GenerateCopilotStreamResponseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GenerateCopilotStreamResponseResponseBody = None,
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
            temp_model = GenerateCopilotStreamResponseResponseBody()
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
        level: str = None,
        namespace: str = None,
        pod: str = None,
        show_pod: int = None,
        start: float = None,
    ):
        self.cluster = cluster
        self.end = end
        self.instance = instance
        self.level = level
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
        if self.level is not None:
            result['level'] = self.level
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
        if m.get('level') is not None:
            self.level = m.get('level')
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
        event_list: List[str] = None,
        type: str = None,
        value: int = None,
    ):
        self.event_list = event_list
        self.type = type
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_list is not None:
            result['eventList'] = self.event_list
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('eventList') is not None:
            self.event_list = m.get('eventList')
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


class GetCopilotHistoryRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
    ):
        # This parameter is required.
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        return self


class GetCopilotHistoryResponseBodyData(TeaModel):
    def __init__(
        self,
        content: str = None,
        time: str = None,
        user: str = None,
    ):
        self.content = content
        self.time = time
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.time is not None:
            result['time'] = self.time
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class GetCopilotHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[GetCopilotHistoryResponseBodyData] = None,
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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = GetCopilotHistoryResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetCopilotHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCopilotHistoryResponseBody = None,
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
            temp_model = GetCopilotHistoryResponseBody()
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


class GetHotSpotUniqListRequest(TeaModel):
    def __init__(
        self,
        beg_end: int = None,
        beg_start: int = None,
        instance: str = None,
        pid: int = None,
        table: str = None,
        uniq: str = None,
    ):
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.instance = instance
        self.pid = pid
        self.table = table
        # This parameter is required.
        self.uniq = uniq

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
        if self.pid is not None:
            result['pid'] = self.pid
        if self.table is not None:
            result['table'] = self.table
        if self.uniq is not None:
            result['uniq'] = self.uniq
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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
        if m.get('uniq') is not None:
            self.uniq = m.get('uniq')
        return self


class GetHotSpotUniqListResponseBodyData(TeaModel):
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


class GetHotSpotUniqListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotSpotUniqListResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
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
            temp_model = GetHotSpotUniqListResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetHotSpotUniqListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotSpotUniqListResponseBody = None,
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
            temp_model = GetHotSpotUniqListResponseBody()
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


class GetHotspotCompareRequest(TeaModel):
    def __init__(
        self,
        beg_1end: int = None,
        beg_1start: int = None,
        beg_2end: int = None,
        beg_2start: int = None,
        hot_type: str = None,
        instance_1: str = None,
        instance_2: str = None,
        pid_1: int = None,
        pid_2: int = None,
        table: str = None,
    ):
        # This parameter is required.
        self.beg_1end = beg_1end
        # This parameter is required.
        self.beg_1start = beg_1start
        # This parameter is required.
        self.beg_2end = beg_2end
        # This parameter is required.
        self.beg_2start = beg_2start
        self.hot_type = hot_type
        # This parameter is required.
        self.instance_1 = instance_1
        # This parameter is required.
        self.instance_2 = instance_2
        self.pid_1 = pid_1
        self.pid_2 = pid_2
        # This parameter is required.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.beg_1end is not None:
            result['beg1_end'] = self.beg_1end
        if self.beg_1start is not None:
            result['beg1_start'] = self.beg_1start
        if self.beg_2end is not None:
            result['beg2_end'] = self.beg_2end
        if self.beg_2start is not None:
            result['beg2_start'] = self.beg_2start
        if self.hot_type is not None:
            result['hot_type'] = self.hot_type
        if self.instance_1 is not None:
            result['instance1'] = self.instance_1
        if self.instance_2 is not None:
            result['instance2'] = self.instance_2
        if self.pid_1 is not None:
            result['pid1'] = self.pid_1
        if self.pid_2 is not None:
            result['pid2'] = self.pid_2
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beg1_end') is not None:
            self.beg_1end = m.get('beg1_end')
        if m.get('beg1_start') is not None:
            self.beg_1start = m.get('beg1_start')
        if m.get('beg2_end') is not None:
            self.beg_2end = m.get('beg2_end')
        if m.get('beg2_start') is not None:
            self.beg_2start = m.get('beg2_start')
        if m.get('hot_type') is not None:
            self.hot_type = m.get('hot_type')
        if m.get('instance1') is not None:
            self.instance_1 = m.get('instance1')
        if m.get('instance2') is not None:
            self.instance_2 = m.get('instance2')
        if m.get('pid1') is not None:
            self.pid_1 = m.get('pid1')
        if m.get('pid2') is not None:
            self.pid_2 = m.get('pid2')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetHotspotCompareResponseBodyDataFlame(TeaModel):
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


class GetHotspotCompareResponseBodyDataSeriesInstance1(TeaModel):
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


class GetHotspotCompareResponseBodyDataSeriesInstance2(TeaModel):
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


class GetHotspotCompareResponseBodyData(TeaModel):
    def __init__(
        self,
        flame: GetHotspotCompareResponseBodyDataFlame = None,
        series_instance_1: GetHotspotCompareResponseBodyDataSeriesInstance1 = None,
        series_instance_2: GetHotspotCompareResponseBodyDataSeriesInstance2 = None,
    ):
        self.flame = flame
        self.series_instance_1 = series_instance_1
        self.series_instance_2 = series_instance_2

    def validate(self):
        if self.flame:
            self.flame.validate()
        if self.series_instance_1:
            self.series_instance_1.validate()
        if self.series_instance_2:
            self.series_instance_2.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flame is not None:
            result['flame'] = self.flame.to_map()
        if self.series_instance_1 is not None:
            result['series_instance1'] = self.series_instance_1.to_map()
        if self.series_instance_2 is not None:
            result['series_instance2'] = self.series_instance_2.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flame') is not None:
            temp_model = GetHotspotCompareResponseBodyDataFlame()
            self.flame = temp_model.from_map(m['flame'])
        if m.get('series_instance1') is not None:
            temp_model = GetHotspotCompareResponseBodyDataSeriesInstance1()
            self.series_instance_1 = temp_model.from_map(m['series_instance1'])
        if m.get('series_instance2') is not None:
            temp_model = GetHotspotCompareResponseBodyDataSeriesInstance2()
            self.series_instance_2 = temp_model.from_map(m['series_instance2'])
        return self


class GetHotspotCompareResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotspotCompareResponseBodyData = None,
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
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetHotspotCompareResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetHotspotCompareResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotspotCompareResponseBody = None,
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
            temp_model = GetHotspotCompareResponseBody()
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


class GetHotspotTrackingRequest(TeaModel):
    def __init__(
        self,
        beg_end: int = None,
        beg_start: int = None,
        hot_type: str = None,
        instance: str = None,
        pid: int = None,
        table: str = None,
    ):
        # This parameter is required.
        self.beg_end = beg_end
        # This parameter is required.
        self.beg_start = beg_start
        # This parameter is required.
        self.hot_type = hot_type
        # This parameter is required.
        self.instance = instance
        self.pid = pid
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
        if self.hot_type is not None:
            result['hot_type'] = self.hot_type
        if self.instance is not None:
            result['instance'] = self.instance
        if self.pid is not None:
            result['pid'] = self.pid
        if self.table is not None:
            result['table'] = self.table
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('beg_end') is not None:
            self.beg_end = m.get('beg_end')
        if m.get('beg_start') is not None:
            self.beg_start = m.get('beg_start')
        if m.get('hot_type') is not None:
            self.hot_type = m.get('hot_type')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('table') is not None:
            self.table = m.get('table')
        return self


class GetHotspotTrackingResponseBodyDataFlame(TeaModel):
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


class GetHotspotTrackingResponseBodyDataSeries(TeaModel):
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


class GetHotspotTrackingResponseBodyData(TeaModel):
    def __init__(
        self,
        flame: GetHotspotTrackingResponseBodyDataFlame = None,
        series: GetHotspotTrackingResponseBodyDataSeries = None,
    ):
        self.flame = flame
        self.series = series

    def validate(self):
        if self.flame:
            self.flame.validate()
        if self.series:
            self.series.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.flame is not None:
            result['flame'] = self.flame.to_map()
        if self.series is not None:
            result['series'] = self.series.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('flame') is not None:
            temp_model = GetHotspotTrackingResponseBodyDataFlame()
            self.flame = temp_model.from_map(m['flame'])
        if m.get('series') is not None:
            temp_model = GetHotspotTrackingResponseBodyDataSeries()
            self.series = temp_model.from_map(m['series'])
        return self


class GetHotspotTrackingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetHotspotTrackingResponseBodyData = None,
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
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetHotspotTrackingResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetHotspotTrackingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetHotspotTrackingResponseBody = None,
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
            temp_model = GetHotspotTrackingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstantScoreRequest(TeaModel):
    def __init__(
        self,
        cluster: str = None,
        instance: str = None,
    ):
        self.cluster = cluster
        self.instance = instance

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster') is not None:
            self.cluster = m.get('cluster')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        return self


class GetInstantScoreResponseBodyData(TeaModel):
    def __init__(
        self,
        error: float = None,
        latency: float = None,
        load: float = None,
        saturation: float = None,
        total: float = None,
    ):
        self.error = error
        self.latency = latency
        self.load = load
        self.saturation = saturation
        self.total = total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error is not None:
            result['error'] = self.error
        if self.latency is not None:
            result['latency'] = self.latency
        if self.load is not None:
            result['load'] = self.load
        if self.saturation is not None:
            result['saturation'] = self.saturation
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('latency') is not None:
            self.latency = m.get('latency')
        if m.get('load') is not None:
            self.load = m.get('load')
        if m.get('saturation') is not None:
            self.saturation = m.get('saturation')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class GetInstantScoreResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetInstantScoreResponseBodyData = None,
        message: str = None,
        request_id: str = None,
    ):
        # 集群ID
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
            temp_model = GetInstantScoreResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetInstantScoreResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstantScoreResponseBody = None,
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
            temp_model = GetInstantScoreResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetListRecordRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        region: str = None,
    ):
        self.current = current
        self.page_size = page_size
        self.region = region

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
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
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
        time: int = None,
        type: str = None,
        value: int = None,
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


class GetServiceFuncStatusRequestParams(TeaModel):
    def __init__(
        self,
        function_name: str = None,
        instance: str = None,
        uid: str = None,
    ):
        # This parameter is required.
        self.function_name = function_name
        self.instance = instance
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.function_name is not None:
            result['function_name'] = self.function_name
        if self.instance is not None:
            result['instance'] = self.instance
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('function_name') is not None:
            self.function_name = m.get('function_name')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class GetServiceFuncStatusRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        params: GetServiceFuncStatusRequestParams = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.service_name is not None:
            result['service_name'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('params') is not None:
            temp_model = GetServiceFuncStatusRequestParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        return self


class GetServiceFuncStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        params_shrink: str = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params_shrink = params_shrink
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
        if self.params_shrink is not None:
            result['params'] = self.params_shrink
        if self.service_name is not None:
            result['service_name'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('params') is not None:
            self.params_shrink = m.get('params')
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        return self


class GetServiceFuncStatusResponseBodyDataArgs(TeaModel):
    def __init__(
        self,
        add_cmd: str = None,
        cpu: str = None,
        java_store_path: str = None,
        locks: str = None,
        loop: int = None,
        mem: str = None,
        system_profiling: str = None,
    ):
        self.add_cmd = add_cmd
        self.cpu = cpu
        self.java_store_path = java_store_path
        self.locks = locks
        self.loop = loop
        self.mem = mem
        self.system_profiling = system_profiling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_cmd is not None:
            result['add_cmd'] = self.add_cmd
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.java_store_path is not None:
            result['java_store_path'] = self.java_store_path
        if self.locks is not None:
            result['locks'] = self.locks
        if self.loop is not None:
            result['loop'] = self.loop
        if self.mem is not None:
            result['mem'] = self.mem
        if self.system_profiling is not None:
            result['system_profiling'] = self.system_profiling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_cmd') is not None:
            self.add_cmd = m.get('add_cmd')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('java_store_path') is not None:
            self.java_store_path = m.get('java_store_path')
        if m.get('locks') is not None:
            self.locks = m.get('locks')
        if m.get('loop') is not None:
            self.loop = m.get('loop')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('system_profiling') is not None:
            self.system_profiling = m.get('system_profiling')
        return self


class GetServiceFuncStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        args: GetServiceFuncStatusResponseBodyDataArgs = None,
    ):
        self.args = args

    def validate(self):
        if self.args:
            self.args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            temp_model = GetServiceFuncStatusResponseBodyDataArgs()
            self.args = temp_model.from_map(m['args'])
        return self


class GetServiceFuncStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetServiceFuncStatusResponseBodyData = None,
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
            temp_model = GetServiceFuncStatusResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetServiceFuncStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetServiceFuncStatusResponseBody = None,
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
            temp_model = GetServiceFuncStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitialSysomRequest(TeaModel):
    def __init__(
        self,
        check_only: bool = None,
        source: str = None,
    ):
        self.check_only = check_only
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_only is not None:
            result['check_only'] = self.check_only
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_only') is not None:
            self.check_only = m.get('check_only')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class InitialSysomResponseBodyData(TeaModel):
    def __init__(
        self,
        role_exist: bool = None,
    ):
        self.role_exist = role_exist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.role_exist is not None:
            result['role_exist'] = self.role_exist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('role_exist') is not None:
            self.role_exist = m.get('role_exist')
        return self


class InitialSysomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: InitialSysomResponseBodyData = None,
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
            temp_model = InitialSysomResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class InitialSysomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitialSysomResponseBody = None,
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
            temp_model = InitialSysomResponseBody()
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


class InstallAgentForClusterRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        cluster_id: str = None,
        config_id: str = None,
        grayscale_config: str = None,
    ):
        self.agent_id = agent_id
        self.agent_version = agent_version
        self.cluster_id = cluster_id
        self.config_id = config_id
        self.grayscale_config = grayscale_config

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.config_id is not None:
            result['config_id'] = self.config_id
        if self.grayscale_config is not None:
            result['grayscale_config'] = self.grayscale_config
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('config_id') is not None:
            self.config_id = m.get('config_id')
        if m.get('grayscale_config') is not None:
            self.grayscale_config = m.get('grayscale_config')
        return self


class InstallAgentForClusterResponseBodyData(TeaModel):
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


class InstallAgentForClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: InstallAgentForClusterResponseBodyData = None,
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
            temp_model = InstallAgentForClusterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class InstallAgentForClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InstallAgentForClusterResponseBody = None,
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
            temp_model = InstallAgentForClusterResponseBody()
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
        event: str = None,
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
        self.event = event
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
        if self.event is not None:
            result['event'] = self.event
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
        if m.get('event') is not None:
            self.event = m.get('event')
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


class ListAbnormalyEventsResponseBodyDataOptsResult(TeaModel):
    def __init__(
        self,
        status: str = None,
        url: str = None,
    ):
        self.status = status
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class ListAbnormalyEventsResponseBodyDataOpts(TeaModel):
    def __init__(
        self,
        label: str = None,
        result: ListAbnormalyEventsResponseBodyDataOptsResult = None,
        type: str = None,
    ):
        self.label = label
        self.result = result
        self.type = type

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.result is not None:
            result['result'] = self.result.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('result') is not None:
            temp_model = ListAbnormalyEventsResponseBodyDataOptsResult()
            self.result = temp_model.from_map(m['result'])
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListAbnormalyEventsResponseBodyData(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        diag_status: int = None,
        end_at: int = None,
        instance: str = None,
        item: str = None,
        level: str = None,
        namespace: str = None,
        opts: List[ListAbnormalyEventsResponseBodyDataOpts] = None,
        pod: str = None,
        region_id: str = None,
        type: str = None,
        uuid: str = None,
    ):
        self.created_at = created_at
        self.description = description
        self.diag_status = diag_status
        self.end_at = end_at
        self.instance = instance
        self.item = item
        self.level = level
        self.namespace = namespace
        self.opts = opts
        self.pod = pod
        self.region_id = region_id
        self.type = type
        self.uuid = uuid

    def validate(self):
        if self.opts:
            for k in self.opts:
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
        if self.diag_status is not None:
            result['diag_status'] = self.diag_status
        if self.end_at is not None:
            result['end_at'] = self.end_at
        if self.instance is not None:
            result['instance'] = self.instance
        if self.item is not None:
            result['item'] = self.item
        if self.level is not None:
            result['level'] = self.level
        if self.namespace is not None:
            result['namespace'] = self.namespace
        result['opts'] = []
        if self.opts is not None:
            for k in self.opts:
                result['opts'].append(k.to_map() if k else None)
        if self.pod is not None:
            result['pod'] = self.pod
        if self.region_id is not None:
            result['region_id'] = self.region_id
        if self.type is not None:
            result['type'] = self.type
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('diag_status') is not None:
            self.diag_status = m.get('diag_status')
        if m.get('end_at') is not None:
            self.end_at = m.get('end_at')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('item') is not None:
            self.item = m.get('item')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        self.opts = []
        if m.get('opts') is not None:
            for k in m.get('opts'):
                temp_model = ListAbnormalyEventsResponseBodyDataOpts()
                self.opts.append(temp_model.from_map(k))
        if m.get('pod') is not None:
            self.pod = m.get('pod')
        if m.get('region_id') is not None:
            self.region_id = m.get('region_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class ListAbnormalyEventsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListAbnormalyEventsResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
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
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAbnormalyEventsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
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
        region: str = None,
        status: str = None,
    ):
        self.current = current
        self.instance_id = instance_id
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.region = region
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
        if self.region is not None:
            result['region'] = self.region
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
        if m.get('region') is not None:
            self.region = m.get('region')
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


class ListClusterAgentInstallRecordsRequest(TeaModel):
    def __init__(
        self,
        agent_config_id: str = None,
        cluster_id: str = None,
        current: int = None,
        page_size: int = None,
        plugin_id: str = None,
        plugin_version: str = None,
    ):
        self.agent_config_id = agent_config_id
        self.cluster_id = cluster_id
        self.current = current
        self.page_size = page_size
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_config_id is not None:
            result['agent_config_id'] = self.agent_config_id
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.current is not None:
            result['current'] = self.current
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_config_id') is not None:
            self.agent_config_id = m.get('agent_config_id')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')
        return self


class ListClusterAgentInstallRecordsResponseBodyData(TeaModel):
    def __init__(
        self,
        agent_config_id: str = None,
        agent_config_name: str = None,
        cluster_id: str = None,
        created_at: str = None,
        grayscale_config: str = None,
        plugin_id: str = None,
        plugin_version: str = None,
        updated_at: str = None,
    ):
        self.agent_config_id = agent_config_id
        self.agent_config_name = agent_config_name
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.grayscale_config = grayscale_config
        self.plugin_id = plugin_id
        self.plugin_version = plugin_version
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_config_id is not None:
            result['agent_config_id'] = self.agent_config_id
        if self.agent_config_name is not None:
            result['agent_config_name'] = self.agent_config_name
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.grayscale_config is not None:
            result['grayscale_config'] = self.grayscale_config
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.plugin_version is not None:
            result['plugin_version'] = self.plugin_version
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_config_id') is not None:
            self.agent_config_id = m.get('agent_config_id')
        if m.get('agent_config_name') is not None:
            self.agent_config_name = m.get('agent_config_name')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('grayscale_config') is not None:
            self.grayscale_config = m.get('grayscale_config')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('plugin_version') is not None:
            self.plugin_version = m.get('plugin_version')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ListClusterAgentInstallRecordsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListClusterAgentInstallRecordsResponseBodyData] = None,
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
                temp_model = ListClusterAgentInstallRecordsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListClusterAgentInstallRecordsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterAgentInstallRecordsResponseBody = None,
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
            temp_model = ListClusterAgentInstallRecordsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClustersRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_status: str = None,
        cluster_type: str = None,
        current: int = None,
        id: str = None,
        name: str = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_status = cluster_status
        self.cluster_type = cluster_type
        self.current = current
        self.id = id
        self.name = name
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_status is not None:
            result['cluster_status'] = self.cluster_status
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.current is not None:
            result['current'] = self.current
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_status') is not None:
            self.cluster_status = m.get('cluster_status')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListClustersResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_status: str = None,
        cluster_type: str = None,
        created_at: str = None,
        id: str = None,
        name: str = None,
        region: str = None,
        updated_at: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_status = cluster_status
        self.cluster_type = cluster_type
        self.created_at = created_at
        self.id = id
        self.name = name
        self.region = region
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.cluster_status is not None:
            result['cluster_status'] = self.cluster_status
        if self.cluster_type is not None:
            result['cluster_type'] = self.cluster_type
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.id is not None:
            result['id'] = self.id
        if self.name is not None:
            result['name'] = self.name
        if self.region is not None:
            result['region'] = self.region
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('cluster_status') is not None:
            self.cluster_status = m.get('cluster_status')
        if m.get('cluster_type') is not None:
            self.cluster_type = m.get('cluster_type')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ListClustersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListClustersResponseBodyData] = None,
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
                temp_model = ListClustersResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClustersResponseBody = None,
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
            temp_model = ListClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDiagnosisRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        page_size: int = None,
        params: str = None,
        service_name: str = None,
        status: str = None,
    ):
        self.current = current
        self.page_size = page_size
        self.params = params
        self.service_name = service_name
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
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.params is not None:
            result['params'] = self.params
        if self.service_name is not None:
            result['service_name'] = self.service_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('params') is not None:
            self.params = m.get('params')
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListDiagnosisResponseBodyData(TeaModel):
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


class ListDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListDiagnosisResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        # This parameter is required.
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
                temp_model = ListDiagnosisResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDiagnosisResponseBody = None,
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
            temp_model = ListDiagnosisResponseBody()
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
        data: List[ListInstanceHealthResponseBodyData] = None,
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
                temp_model = ListInstanceHealthResponseBodyData()
                self.data.append(temp_model.from_map(k))
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


class ListInstanceStatusRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        instance: str = None,
        page_size: int = None,
        region: str = None,
        status: str = None,
    ):
        self.current = current
        self.instance = instance
        self.page_size = page_size
        self.region = region
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
        if self.instance is not None:
            result['instance'] = self.instance
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstanceStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        instance: str = None,
        region: str = None,
        status: str = None,
    ):
        self.instance = instance
        self.region = region
        self.status = status

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
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstanceStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListInstanceStatusResponseBodyData] = None,
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
                temp_model = ListInstanceStatusResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListInstanceStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceStatusResponseBody = None,
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
            temp_model = ListInstanceStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        current: int = None,
        instance: str = None,
        page_size: int = None,
        region: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.current = current
        self.instance = instance
        self.page_size = page_size
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.current is not None:
            result['current'] = self.current
        if self.instance is not None:
            result['instance'] = self.instance
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance: str = None,
        kernel_version: str = None,
        meta: Any = None,
        os_arch: str = None,
        os_health_score: str = None,
        os_name: str = None,
        os_name_id: str = None,
        os_version: str = None,
        os_version_id: str = None,
        region: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance = instance
        self.kernel_version = kernel_version
        self.meta = meta
        self.os_arch = os_arch
        self.os_health_score = os_health_score
        self.os_name = os_name
        self.os_name_id = os_name_id
        self.os_version = os_version
        self.os_version_id = os_version_id
        self.region = region
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.instance is not None:
            result['instance'] = self.instance
        if self.kernel_version is not None:
            result['kernel_version'] = self.kernel_version
        if self.meta is not None:
            result['meta'] = self.meta
        if self.os_arch is not None:
            result['os_arch'] = self.os_arch
        if self.os_health_score is not None:
            result['os_health_score'] = self.os_health_score
        if self.os_name is not None:
            result['os_name'] = self.os_name
        if self.os_name_id is not None:
            result['os_name_id'] = self.os_name_id
        if self.os_version is not None:
            result['os_version'] = self.os_version
        if self.os_version_id is not None:
            result['os_version_id'] = self.os_version_id
        if self.region is not None:
            result['region'] = self.region
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('kernel_version') is not None:
            self.kernel_version = m.get('kernel_version')
        if m.get('meta') is not None:
            self.meta = m.get('meta')
        if m.get('os_arch') is not None:
            self.os_arch = m.get('os_arch')
        if m.get('os_health_score') is not None:
            self.os_health_score = m.get('os_health_score')
        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')
        if m.get('os_name_id') is not None:
            self.os_name_id = m.get('os_name_id')
        if m.get('os_version') is not None:
            self.os_version = m.get('os_version')
        if m.get('os_version_id') is not None:
            self.os_version_id = m.get('os_version_id')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListInstancesResponseBodyData] = None,
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
                temp_model = ListInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesResponseBody = None,
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
            temp_model = ListInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesEcsInfoListRequest(TeaModel):
    def __init__(
        self,
        info_type: str = None,
        instance_id: str = None,
        managed_type: str = None,
        plugin_id: str = None,
        region: str = None,
    ):
        # This parameter is required.
        self.info_type = info_type
        self.instance_id = instance_id
        self.managed_type = managed_type
        self.plugin_id = plugin_id
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.info_type is not None:
            result['info_type'] = self.info_type
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.managed_type is not None:
            result['managed_type'] = self.managed_type
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('info_type') is not None:
            self.info_type = m.get('info_type')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('managed_type') is not None:
            self.managed_type = m.get('managed_type')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class ListInstancesEcsInfoListResponseBodyData(TeaModel):
    def __init__(
        self,
        ip: str = None,
        tag_key: str = None,
        tag_value: str = None,
        type: str = None,
    ):
        self.ip = ip
        self.tag_key = tag_key
        self.tag_value = tag_value
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip is not None:
            result['ip'] = self.ip
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip') is not None:
            self.ip = m.get('ip')
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')
        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListInstancesEcsInfoListResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListInstancesEcsInfoListResponseBodyData] = None,
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
                temp_model = ListInstancesEcsInfoListResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListInstancesEcsInfoListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesEcsInfoListResponseBody = None,
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
            temp_model = ListInstancesEcsInfoListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstancesWithEcsInfoRequestInstanceTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListInstancesWithEcsInfoRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        health_status: str = None,
        instance_id: str = None,
        instance_id_name: str = None,
        instance_name: str = None,
        instance_tag: ListInstancesWithEcsInfoRequestInstanceTag = None,
        is_managed: int = None,
        os_name: str = None,
        page_size: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_group_id_name: str = None,
        resource_group_name: str = None,
    ):
        self.current = current
        self.health_status = health_status
        self.instance_id = instance_id
        self.instance_id_name = instance_id_name
        self.instance_name = instance_name
        self.instance_tag = instance_tag
        self.is_managed = is_managed
        self.os_name = os_name
        self.page_size = page_size
        self.private_ip = private_ip
        self.public_ip = public_ip
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_group_id_name = resource_group_id_name
        self.resource_group_name = resource_group_name

    def validate(self):
        if self.instance_tag:
            self.instance_tag.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.health_status is not None:
            result['health_status'] = self.health_status
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_id_name is not None:
            result['instance_id_name'] = self.instance_id_name
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.instance_tag is not None:
            result['instance_tag'] = self.instance_tag.to_map()
        if self.is_managed is not None:
            result['is_managed'] = self.is_managed
        if self.os_name is not None:
            result['os_name'] = self.os_name
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.private_ip is not None:
            result['private_ip'] = self.private_ip
        if self.public_ip is not None:
            result['public_ip'] = self.public_ip
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.resource_group_id_name is not None:
            result['resource_group_id_name'] = self.resource_group_id_name
        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('health_status') is not None:
            self.health_status = m.get('health_status')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_id_name') is not None:
            self.instance_id_name = m.get('instance_id_name')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('instance_tag') is not None:
            temp_model = ListInstancesWithEcsInfoRequestInstanceTag()
            self.instance_tag = temp_model.from_map(m['instance_tag'])
        if m.get('is_managed') is not None:
            self.is_managed = m.get('is_managed')
        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')
        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('resource_group_id_name') is not None:
            self.resource_group_id_name = m.get('resource_group_id_name')
        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')
        return self


class ListInstancesWithEcsInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        health_status: str = None,
        instance_id: str = None,
        instance_id_name: str = None,
        instance_name: str = None,
        instance_tag_shrink: str = None,
        is_managed: int = None,
        os_name: str = None,
        page_size: int = None,
        private_ip: str = None,
        public_ip: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_group_id_name: str = None,
        resource_group_name: str = None,
    ):
        self.current = current
        self.health_status = health_status
        self.instance_id = instance_id
        self.instance_id_name = instance_id_name
        self.instance_name = instance_name
        self.instance_tag_shrink = instance_tag_shrink
        self.is_managed = is_managed
        self.os_name = os_name
        self.page_size = page_size
        self.private_ip = private_ip
        self.public_ip = public_ip
        # This parameter is required.
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_group_id_name = resource_group_id_name
        self.resource_group_name = resource_group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.health_status is not None:
            result['health_status'] = self.health_status
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_id_name is not None:
            result['instance_id_name'] = self.instance_id_name
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        if self.instance_tag_shrink is not None:
            result['instance_tag'] = self.instance_tag_shrink
        if self.is_managed is not None:
            result['is_managed'] = self.is_managed
        if self.os_name is not None:
            result['os_name'] = self.os_name
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.private_ip is not None:
            result['private_ip'] = self.private_ip
        if self.public_ip is not None:
            result['public_ip'] = self.public_ip
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.resource_group_id_name is not None:
            result['resource_group_id_name'] = self.resource_group_id_name
        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('health_status') is not None:
            self.health_status = m.get('health_status')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_id_name') is not None:
            self.instance_id_name = m.get('instance_id_name')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        if m.get('instance_tag') is not None:
            self.instance_tag_shrink = m.get('instance_tag')
        if m.get('is_managed') is not None:
            self.is_managed = m.get('is_managed')
        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')
        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('resource_group_id_name') is not None:
            self.resource_group_id_name = m.get('resource_group_id_name')
        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')
        return self


class ListInstancesWithEcsInfoResponseBodyDataInstanceTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')
        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')
        return self


class ListInstancesWithEcsInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_tag: List[ListInstancesWithEcsInfoResponseBodyDataInstanceTag] = None,
        kernel_version: str = None,
        os_arch: str = None,
        os_health_score: str = None,
        os_name: str = None,
        private_ip: str = None,
        public_ip: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        status: str = None,
    ):
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_tag = instance_tag
        self.kernel_version = kernel_version
        self.os_arch = os_arch
        self.os_health_score = os_health_score
        self.os_name = os_name
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.status = status

    def validate(self):
        if self.instance_tag:
            for k in self.instance_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        result['instance_tag'] = []
        if self.instance_tag is not None:
            for k in self.instance_tag:
                result['instance_tag'].append(k.to_map() if k else None)
        if self.kernel_version is not None:
            result['kernel_version'] = self.kernel_version
        if self.os_arch is not None:
            result['os_arch'] = self.os_arch
        if self.os_health_score is not None:
            result['os_health_score'] = self.os_health_score
        if self.os_name is not None:
            result['os_name'] = self.os_name
        if self.private_ip is not None:
            result['private_ip'] = self.private_ip
        if self.public_ip is not None:
            result['public_ip'] = self.public_ip
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        self.instance_tag = []
        if m.get('instance_tag') is not None:
            for k in m.get('instance_tag'):
                temp_model = ListInstancesWithEcsInfoResponseBodyDataInstanceTag()
                self.instance_tag.append(temp_model.from_map(k))
        if m.get('kernel_version') is not None:
            self.kernel_version = m.get('kernel_version')
        if m.get('os_arch') is not None:
            self.os_arch = m.get('os_arch')
        if m.get('os_health_score') is not None:
            self.os_health_score = m.get('os_health_score')
        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')
        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')
        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListInstancesWithEcsInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListInstancesWithEcsInfoResponseBodyData] = None,
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
                temp_model = ListInstancesWithEcsInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListInstancesWithEcsInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstancesWithEcsInfoResponseBody = None,
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
            temp_model = ListInstancesWithEcsInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPluginsInstancesRequest(TeaModel):
    def __init__(
        self,
        current: int = None,
        instance_id_name: str = None,
        instance_tag: str = None,
        operation_type: str = None,
        page_size: int = None,
        plugin_id: str = None,
        region: str = None,
    ):
        self.current = current
        self.instance_id_name = instance_id_name
        self.instance_tag = instance_tag
        # This parameter is required.
        self.operation_type = operation_type
        self.page_size = page_size
        # This parameter is required.
        self.plugin_id = plugin_id
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['current'] = self.current
        if self.instance_id_name is not None:
            result['instance_id_name'] = self.instance_id_name
        if self.instance_tag is not None:
            result['instance_tag'] = self.instance_tag
        if self.operation_type is not None:
            result['operation_type'] = self.operation_type
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.plugin_id is not None:
            result['plugin_id'] = self.plugin_id
        if self.region is not None:
            result['region'] = self.region
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('instance_id_name') is not None:
            self.instance_id_name = m.get('instance_id_name')
        if m.get('instance_tag') is not None:
            self.instance_tag = m.get('instance_tag')
        if m.get('operation_type') is not None:
            self.operation_type = m.get('operation_type')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('plugin_id') is not None:
            self.plugin_id = m.get('plugin_id')
        if m.get('region') is not None:
            self.region = m.get('region')
        return self


class ListPluginsInstancesResponseBodyDataInstanceTag(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['tag_key'] = self.tag_key
        if self.tag_value is not None:
            result['tag_value'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tag_key') is not None:
            self.tag_key = m.get('tag_key')
        if m.get('tag_value') is not None:
            self.tag_value = m.get('tag_value')
        return self


class ListPluginsInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        instance_name: str = None,
        instance_tag: List[ListPluginsInstancesResponseBodyDataInstanceTag] = None,
        os_name: str = None,
        private_ip: str = None,
        public_ip: str = None,
        region: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
    ):
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_tag = instance_tag
        self.os_name = os_name
        self.private_ip = private_ip
        self.public_ip = public_ip
        self.region = region
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name

    def validate(self):
        if self.instance_tag:
            for k in self.instance_tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.instance_name is not None:
            result['instance_name'] = self.instance_name
        result['instance_tag'] = []
        if self.instance_tag is not None:
            for k in self.instance_tag:
                result['instance_tag'].append(k.to_map() if k else None)
        if self.os_name is not None:
            result['os_name'] = self.os_name
        if self.private_ip is not None:
            result['private_ip'] = self.private_ip
        if self.public_ip is not None:
            result['public_ip'] = self.public_ip
        if self.region is not None:
            result['region'] = self.region
        if self.resource_group_id is not None:
            result['resource_group_id'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resource_group_name'] = self.resource_group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('instance_name') is not None:
            self.instance_name = m.get('instance_name')
        self.instance_tag = []
        if m.get('instance_tag') is not None:
            for k in m.get('instance_tag'):
                temp_model = ListPluginsInstancesResponseBodyDataInstanceTag()
                self.instance_tag.append(temp_model.from_map(k))
        if m.get('os_name') is not None:
            self.os_name = m.get('os_name')
        if m.get('private_ip') is not None:
            self.private_ip = m.get('private_ip')
        if m.get('public_ip') is not None:
            self.public_ip = m.get('public_ip')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('resource_group_id') is not None:
            self.resource_group_id = m.get('resource_group_id')
        if m.get('resource_group_name') is not None:
            self.resource_group_name = m.get('resource_group_name')
        return self


class ListPluginsInstancesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListPluginsInstancesResponseBodyData] = None,
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
                temp_model = ListPluginsInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListPluginsInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPluginsInstancesResponseBody = None,
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
            temp_model = ListPluginsInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPodsOfInstanceRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        current: int = None,
        instance: str = None,
        page_size: int = None,
    ):
        self.cluster_id = cluster_id
        self.current = current
        self.instance = instance
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.current is not None:
            result['current'] = self.current
        if self.instance is not None:
            result['instance'] = self.instance
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPodsOfInstanceResponseBodyData(TeaModel):
    def __init__(
        self,
        namespace: str = None,
        pod: str = None,
    ):
        self.namespace = namespace
        self.pod = pod

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.pod is not None:
            result['pod'] = self.pod
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('pod') is not None:
            self.pod = m.get('pod')
        return self


class ListPodsOfInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[ListPodsOfInstanceResponseBodyData] = None,
        message: str = None,
        total: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.data = data
        # This parameter is required.
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
                temp_model = ListPodsOfInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListPodsOfInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPodsOfInstanceResponseBody = None,
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
            temp_model = ListPodsOfInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegionsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: List[str] = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.data = data
        self.message = message

    def validate(self):
        pass

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
            result['data'] = self.data
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
            self.data = m.get('data')
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class ListRegionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegionsResponseBody = None,
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
            temp_model = ListRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartAIAnalysisRequest(TeaModel):
    def __init__(
        self,
        analysis_tool: str = None,
        analysis_params: List[str] = None,
        channel: str = None,
        comms: str = None,
        created_by: str = None,
        instance: str = None,
        instance_type: str = None,
        iteration_func: str = None,
        iteration_mod: str = None,
        iteration_range: List[int] = None,
        pids: str = None,
        region: str = None,
        timeout: int = None,
        uid: str = None,
    ):
        self.analysis_tool = analysis_tool
        self.analysis_params = analysis_params
        self.channel = channel
        self.comms = comms
        self.created_by = created_by
        self.instance = instance
        self.instance_type = instance_type
        self.iteration_func = iteration_func
        self.iteration_mod = iteration_mod
        self.iteration_range = iteration_range
        self.pids = pids
        self.region = region
        self.timeout = timeout
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_tool is not None:
            result['analysisTool'] = self.analysis_tool
        if self.analysis_params is not None:
            result['analysis_params'] = self.analysis_params
        if self.channel is not None:
            result['channel'] = self.channel
        if self.comms is not None:
            result['comms'] = self.comms
        if self.created_by is not None:
            result['created_by'] = self.created_by
        if self.instance is not None:
            result['instance'] = self.instance
        if self.instance_type is not None:
            result['instance_type'] = self.instance_type
        if self.iteration_func is not None:
            result['iteration_func'] = self.iteration_func
        if self.iteration_mod is not None:
            result['iteration_mod'] = self.iteration_mod
        if self.iteration_range is not None:
            result['iteration_range'] = self.iteration_range
        if self.pids is not None:
            result['pids'] = self.pids
        if self.region is not None:
            result['region'] = self.region
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisTool') is not None:
            self.analysis_tool = m.get('analysisTool')
        if m.get('analysis_params') is not None:
            self.analysis_params = m.get('analysis_params')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('comms') is not None:
            self.comms = m.get('comms')
        if m.get('created_by') is not None:
            self.created_by = m.get('created_by')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('instance_type') is not None:
            self.instance_type = m.get('instance_type')
        if m.get('iteration_func') is not None:
            self.iteration_func = m.get('iteration_func')
        if m.get('iteration_mod') is not None:
            self.iteration_mod = m.get('iteration_mod')
        if m.get('iteration_range') is not None:
            self.iteration_range = m.get('iteration_range')
        if m.get('pids') is not None:
            self.pids = m.get('pids')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
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


class StartAIDiffAnalysisRequestTask1(TeaModel):
    def __init__(
        self,
        analysis_id: str = None,
        pids: List[str] = None,
        step_end: float = None,
        step_start: float = None,
    ):
        self.analysis_id = analysis_id
        self.pids = pids
        self.step_end = step_end
        self.step_start = step_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.pids is not None:
            result['pids'] = self.pids
        if self.step_end is not None:
            result['step_end'] = self.step_end
        if self.step_start is not None:
            result['step_start'] = self.step_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('pids') is not None:
            self.pids = m.get('pids')
        if m.get('step_end') is not None:
            self.step_end = m.get('step_end')
        if m.get('step_start') is not None:
            self.step_start = m.get('step_start')
        return self


class StartAIDiffAnalysisRequestTask2(TeaModel):
    def __init__(
        self,
        analysis_id: str = None,
        pids: List[str] = None,
        step_end: float = None,
        step_start: float = None,
    ):
        # This parameter is required.
        self.analysis_id = analysis_id
        # This parameter is required.
        self.pids = pids
        # This parameter is required.
        self.step_end = step_end
        # This parameter is required.
        self.step_start = step_start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.analysis_id is not None:
            result['analysisId'] = self.analysis_id
        if self.pids is not None:
            result['pids'] = self.pids
        if self.step_end is not None:
            result['step_end'] = self.step_end
        if self.step_start is not None:
            result['step_start'] = self.step_start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysisId') is not None:
            self.analysis_id = m.get('analysisId')
        if m.get('pids') is not None:
            self.pids = m.get('pids')
        if m.get('step_end') is not None:
            self.step_end = m.get('step_end')
        if m.get('step_start') is not None:
            self.step_start = m.get('step_start')
        return self


class StartAIDiffAnalysisRequest(TeaModel):
    def __init__(
        self,
        task_1: StartAIDiffAnalysisRequestTask1 = None,
        task_2: StartAIDiffAnalysisRequestTask2 = None,
    ):
        # This parameter is required.
        self.task_1 = task_1
        # This parameter is required.
        self.task_2 = task_2

    def validate(self):
        if self.task_1:
            self.task_1.validate()
        if self.task_2:
            self.task_2.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_1 is not None:
            result['task1'] = self.task_1.to_map()
        if self.task_2 is not None:
            result['task2'] = self.task_2.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task1') is not None:
            temp_model = StartAIDiffAnalysisRequestTask1()
            self.task_1 = temp_model.from_map(m['task1'])
        if m.get('task2') is not None:
            temp_model = StartAIDiffAnalysisRequestTask2()
            self.task_2 = temp_model.from_map(m['task2'])
        return self


class StartAIDiffAnalysisResponseBody(TeaModel):
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


class StartAIDiffAnalysisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: StartAIDiffAnalysisResponseBody = None,
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
            temp_model = StartAIDiffAnalysisResponseBody()
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


class UninstallAgentForClusterRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        cluster_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_version = agent_version
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        return self


class UninstallAgentForClusterResponseBodyData(TeaModel):
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


class UninstallAgentForClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: UninstallAgentForClusterResponseBodyData = None,
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
            temp_model = UninstallAgentForClusterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UninstallAgentForClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UninstallAgentForClusterResponseBody = None,
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
            temp_model = UninstallAgentForClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventsAttentionRequest(TeaModel):
    def __init__(
        self,
        mode: int = None,
        range: str = None,
        uuid: str = None,
    ):
        self.mode = mode
        self.range = range
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        if self.range is not None:
            result['range'] = self.range
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        if m.get('range') is not None:
            self.range = m.get('range')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class UpdateEventsAttentionResponseBodyData(TeaModel):
    def __init__(
        self,
        mode: int = None,
    ):
        self.mode = mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['mode'] = self.mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('mode') is not None:
            self.mode = m.get('mode')
        return self


class UpdateEventsAttentionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: UpdateEventsAttentionResponseBodyData = None,
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
            temp_model = UpdateEventsAttentionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpdateEventsAttentionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventsAttentionResponseBody = None,
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
            temp_model = UpdateEventsAttentionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFuncSwitchRecordRequestParamsArgs(TeaModel):
    def __init__(
        self,
        add_cmd: str = None,
        cpu: str = None,
        duration: int = None,
        java_store_path: str = None,
        locks: str = None,
        loop: int = None,
        mem: str = None,
        pid: int = None,
        system_profiling: str = None,
    ):
        self.add_cmd = add_cmd
        self.cpu = cpu
        self.duration = duration
        self.java_store_path = java_store_path
        self.locks = locks
        self.loop = loop
        self.mem = mem
        self.pid = pid
        self.system_profiling = system_profiling

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_cmd is not None:
            result['add_cmd'] = self.add_cmd
        if self.cpu is not None:
            result['cpu'] = self.cpu
        if self.duration is not None:
            result['duration'] = self.duration
        if self.java_store_path is not None:
            result['java_store_path'] = self.java_store_path
        if self.locks is not None:
            result['locks'] = self.locks
        if self.loop is not None:
            result['loop'] = self.loop
        if self.mem is not None:
            result['mem'] = self.mem
        if self.pid is not None:
            result['pid'] = self.pid
        if self.system_profiling is not None:
            result['system_profiling'] = self.system_profiling
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('add_cmd') is not None:
            self.add_cmd = m.get('add_cmd')
        if m.get('cpu') is not None:
            self.cpu = m.get('cpu')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('java_store_path') is not None:
            self.java_store_path = m.get('java_store_path')
        if m.get('locks') is not None:
            self.locks = m.get('locks')
        if m.get('loop') is not None:
            self.loop = m.get('loop')
        if m.get('mem') is not None:
            self.mem = m.get('mem')
        if m.get('pid') is not None:
            self.pid = m.get('pid')
        if m.get('system_profiling') is not None:
            self.system_profiling = m.get('system_profiling')
        return self


class UpdateFuncSwitchRecordRequestParams(TeaModel):
    def __init__(
        self,
        args: UpdateFuncSwitchRecordRequestParamsArgs = None,
        function_name: str = None,
        instance: str = None,
        op: str = None,
        region: str = None,
        uid: str = None,
    ):
        self.args = args
        # This parameter is required.
        self.function_name = function_name
        self.instance = instance
        self.op = op
        self.region = region
        self.uid = uid

    def validate(self):
        if self.args:
            self.args.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.args is not None:
            result['args'] = self.args.to_map()
        if self.function_name is not None:
            result['function_name'] = self.function_name
        if self.instance is not None:
            result['instance'] = self.instance
        if self.op is not None:
            result['op'] = self.op
        if self.region is not None:
            result['region'] = self.region
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('args') is not None:
            temp_model = UpdateFuncSwitchRecordRequestParamsArgs()
            self.args = temp_model.from_map(m['args'])
        if m.get('function_name') is not None:
            self.function_name = m.get('function_name')
        if m.get('instance') is not None:
            self.instance = m.get('instance')
        if m.get('op') is not None:
            self.op = m.get('op')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class UpdateFuncSwitchRecordRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        params: UpdateFuncSwitchRecordRequestParams = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params = params
        # This parameter is required.
        self.service_name = service_name

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['channel'] = self.channel
        if self.params is not None:
            result['params'] = self.params.to_map()
        if self.service_name is not None:
            result['service_name'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('params') is not None:
            temp_model = UpdateFuncSwitchRecordRequestParams()
            self.params = temp_model.from_map(m['params'])
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        return self


class UpdateFuncSwitchRecordShrinkRequest(TeaModel):
    def __init__(
        self,
        channel: str = None,
        params_shrink: str = None,
        service_name: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        # This parameter is required.
        self.params_shrink = params_shrink
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
        if self.params_shrink is not None:
            result['params'] = self.params_shrink
        if self.service_name is not None:
            result['service_name'] = self.service_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('params') is not None:
            self.params_shrink = m.get('params')
        if m.get('service_name') is not None:
            self.service_name = m.get('service_name')
        return self


class UpdateFuncSwitchRecordResponseBodyData(TeaModel):
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


class UpdateFuncSwitchRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: UpdateFuncSwitchRecordResponseBodyData = None,
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
            temp_model = UpdateFuncSwitchRecordResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateFuncSwitchRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFuncSwitchRecordResponseBody = None,
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
            temp_model = UpdateFuncSwitchRecordResponseBody()
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


class UpgradeAgentForClusterRequest(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        agent_version: str = None,
        cluster_id: str = None,
    ):
        self.agent_id = agent_id
        self.agent_version = agent_version
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agent_id'] = self.agent_id
        if self.agent_version is not None:
            result['agent_version'] = self.agent_version
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agent_id') is not None:
            self.agent_id = m.get('agent_id')
        if m.get('agent_version') is not None:
            self.agent_version = m.get('agent_version')
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        return self


class UpgradeAgentForClusterResponseBodyData(TeaModel):
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


class UpgradeAgentForClusterResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        data: UpgradeAgentForClusterResponseBodyData = None,
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
            temp_model = UpgradeAgentForClusterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('message') is not None:
            self.message = m.get('message')
        return self


class UpgradeAgentForClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpgradeAgentForClusterResponseBody = None,
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
            temp_model = UpgradeAgentForClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


