# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AICreateSessionMessageRequestContext(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        error: str = None,
        kind: str = None,
        name: str = None,
        namespace: str = None,
        uuid: str = None,
    ):
        self.cluster_id = cluster_id
        self.error = error
        self.kind = kind
        self.name = name
        self.namespace = namespace
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.error is not None:
            result['error'] = self.error
        if self.kind is not None:
            result['kind'] = self.kind
        if self.name is not None:
            result['name'] = self.name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.uuid is not None:
            result['uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('error') is not None:
            self.error = m.get('error')
        if m.get('kind') is not None:
            self.kind = m.get('kind')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('uuid') is not None:
            self.uuid = m.get('uuid')
        return self


class AICreateSessionMessageRequest(TeaModel):
    def __init__(
        self,
        context: AICreateSessionMessageRequestContext = None,
        language: str = None,
        message: str = None,
        session_id: str = None,
        type: str = None,
        employee_id: str = None,
    ):
        self.context = context
        self.language = language
        self.message = message
        self.session_id = session_id
        self.type = type
        # This parameter is required.
        self.employee_id = employee_id

    def validate(self):
        if self.context:
            self.context.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.context is not None:
            result['context'] = self.context.to_map()
        if self.language is not None:
            result['language'] = self.language
        if self.message is not None:
            result['message'] = self.message
        if self.session_id is not None:
            result['session_id'] = self.session_id
        if self.type is not None:
            result['type'] = self.type
        if self.employee_id is not None:
            result['employee_id'] = self.employee_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('context') is not None:
            temp_model = AICreateSessionMessageRequestContext()
            self.context = temp_model.from_map(m['context'])
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('employee_id') is not None:
            self.employee_id = m.get('employee_id')
        return self


class AICreateSessionMessageResponseBodyReference(TeaModel):
    def __init__(
        self,
        title: str = None,
        url: str = None,
    ):
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.title is not None:
            result['Title'] = self.title
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class AICreateSessionMessageResponseBody(TeaModel):
    def __init__(
        self,
        answer: str = None,
        code: int = None,
        data: str = None,
        msg: str = None,
        reference: List[AICreateSessionMessageResponseBodyReference] = None,
        request_id: str = None,
        session_id: str = None,
    ):
        self.answer = answer
        self.code = code
        self.data = data
        self.msg = msg
        self.reference = reference
        self.request_id = request_id
        self.session_id = session_id

    def validate(self):
        if self.reference:
            for k in self.reference:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.answer is not None:
            result['answer'] = self.answer
        if self.code is not None:
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data
        if self.msg is not None:
            result['msg'] = self.msg
        result['reference'] = []
        if self.reference is not None:
            for k in self.reference:
                result['reference'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.session_id is not None:
            result['session_id'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        self.reference = []
        if m.get('reference') is not None:
            for k in m.get('reference'):
                temp_model = AICreateSessionMessageResponseBodyReference()
                self.reference.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('session_id') is not None:
            self.session_id = m.get('session_id')
        return self


class AICreateSessionMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AICreateSessionMessageResponseBody = None,
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
            temp_model = AICreateSessionMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDiagnosisRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        cluster_id: str = None,
        diagnosis_type: str = None,
    ):
        self.body = body
        self.cluster_id = cluster_id
        self.diagnosis_type = diagnosis_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        if self.diagnosis_type is not None:
            result['diagnosisType'] = self.diagnosis_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('diagnosisType') is not None:
            self.diagnosis_type = m.get('diagnosisType')
        return self


class CreateDiagnosisResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: Any = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateDiagnosisResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDiagnosisResponseBody = None,
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
            temp_model = CreateDiagnosisResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        return self


class GetClusterResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_type: str = None,
        current_version: str = None,
        name: str = None,
        profile: str = None,
        region_id: str = None,
        security_group_id: str = None,
        spec: str = None,
        state: str = None,
        user_id: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_type = cluster_type
        self.current_version = current_version
        self.name = name
        self.profile = profile
        self.region_id = region_id
        self.security_group_id = security_group_id
        self.spec = spec
        self.state = state
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.current_version is not None:
            result['currentVersion'] = self.current_version
        if self.name is not None:
            result['name'] = self.name
        if self.profile is not None:
            result['profile'] = self.profile
        if self.region_id is not None:
            result['regionID'] = self.region_id
        if self.security_group_id is not None:
            result['securityGroupId'] = self.security_group_id
        if self.spec is not None:
            result['spec'] = self.spec
        if self.state is not None:
            result['state'] = self.state
        if self.user_id is not None:
            result['userID'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('currentVersion') is not None:
            self.current_version = m.get('currentVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('profile') is not None:
            self.profile = m.get('profile')
        if m.get('regionID') is not None:
            self.region_id = m.get('regionID')
        if m.get('securityGroupId') is not None:
            self.security_group_id = m.get('securityGroupId')
        if m.get('spec') is not None:
            self.spec = m.get('spec')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('userID') is not None:
            self.user_id = m.get('userID')
        return self


class GetClusterResponseBody(TeaModel):
    def __init__(
        self,
        data: GetClusterResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = GetClusterResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetClusterResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterResponseBody = None,
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
            temp_model = GetClusterResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetClusterWarningRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
    ):
        self.cluster_id = cluster_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterID'] = self.cluster_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterID') is not None:
            self.cluster_id = m.get('clusterID')
        return self


class GetClusterWarningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetClusterWarningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetClusterWarningResponseBody = None,
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
            temp_model = GetClusterWarningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDiagnosisResultRequest(TeaModel):
    def __init__(
        self,
        diagnosis_id: str = None,
        owner_uid: str = None,
    ):
        self.diagnosis_id = diagnosis_id
        self.owner_uid = owner_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.diagnosis_id is not None:
            result['diagnosisId'] = self.diagnosis_id
        if self.owner_uid is not None:
            result['ownerUid'] = self.owner_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('diagnosisId') is not None:
            self.diagnosis_id = m.get('diagnosisId')
        if m.get('ownerUid') is not None:
            self.owner_uid = m.get('ownerUid')
        return self


class GetDiagnosisResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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


class GetUserClusterWarningRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['userID'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('userID') is not None:
            self.user_id = m.get('userID')
        return self


class GetUserClusterWarningResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetUserClusterWarningResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserClusterWarningResponseBody = None,
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
            temp_model = GetUserClusterWarningResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWebshellTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetWebshellTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWebshellTokenResponseBody = None,
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
            temp_model = GetWebshellTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class HelloRequest(TeaModel):
    def __init__(
        self,
        user: str = None,
    ):
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user is not None:
            result['user'] = self.user
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user') is not None:
            self.user = m.get('user')
        return self


class HelloResponseBodyData(TeaModel):
    def __init__(
        self,
        date: str = None,
        name: str = None,
        success: bool = None,
    ):
        self.date = date
        self.name = name
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['date'] = self.date
        if self.name is not None:
            result['name'] = self.name
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('date') is not None:
            self.date = m.get('date')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class HelloResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: HelloResponseBodyData = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = HelloResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class HelloResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: HelloResponseBody = None,
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
            temp_model = HelloResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterDeprecatedAPIRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        page_no: int = None,
        page_size: int = None,
        target_version: str = None,
    ):
        self.cluster_id = cluster_id
        self.page_no = page_no
        self.page_size = page_size
        self.target_version = target_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.target_version is not None:
            result['target_version'] = self.target_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('target_version') is not None:
            self.target_version = m.get('target_version')
        return self


class ListClusterDeprecatedAPIResponseBodyDatasData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        content: str = None,
        count: int = None,
        current_version: str = None,
        deprecated_k8s_version: str = None,
        ds: str = None,
        label: str = None,
        last_time: str = None,
        request_uri: str = None,
        source_ips: str = None,
        target_version: str = None,
        user_agent: str = None,
    ):
        self.cluster_id = cluster_id
        self.content = content
        self.count = count
        self.current_version = current_version
        self.deprecated_k8s_version = deprecated_k8s_version
        self.ds = ds
        self.label = label
        self.last_time = last_time
        self.request_uri = request_uri
        self.source_ips = source_ips
        self.target_version = target_version
        self.user_agent = user_agent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.content is not None:
            result['content'] = self.content
        if self.count is not None:
            result['count'] = self.count
        if self.current_version is not None:
            result['current_version'] = self.current_version
        if self.deprecated_k8s_version is not None:
            result['deprecated_k8s_version'] = self.deprecated_k8s_version
        if self.ds is not None:
            result['ds'] = self.ds
        if self.label is not None:
            result['label'] = self.label
        if self.last_time is not None:
            result['last_time'] = self.last_time
        if self.request_uri is not None:
            result['request_uri'] = self.request_uri
        if self.source_ips is not None:
            result['source_ips'] = self.source_ips
        if self.target_version is not None:
            result['target_version'] = self.target_version
        if self.user_agent is not None:
            result['user_agent'] = self.user_agent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('current_version') is not None:
            self.current_version = m.get('current_version')
        if m.get('deprecated_k8s_version') is not None:
            self.deprecated_k8s_version = m.get('deprecated_k8s_version')
        if m.get('ds') is not None:
            self.ds = m.get('ds')
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('last_time') is not None:
            self.last_time = m.get('last_time')
        if m.get('request_uri') is not None:
            self.request_uri = m.get('request_uri')
        if m.get('source_ips') is not None:
            self.source_ips = m.get('source_ips')
        if m.get('target_version') is not None:
            self.target_version = m.get('target_version')
        if m.get('user_agent') is not None:
            self.user_agent = m.get('user_agent')
        return self


class ListClusterDeprecatedAPIResponseBodyDatas(TeaModel):
    def __init__(
        self,
        current: int = None,
        data: List[ListClusterDeprecatedAPIResponseBodyDatasData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.data = data
        self.page_size = page_size
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
        if self.current is not None:
            result['current'] = self.current
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListClusterDeprecatedAPIResponseBodyDatasData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListClusterDeprecatedAPIResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datas: ListClusterDeprecatedAPIResponseBodyDatas = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.datas = datas
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.datas:
            self.datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.datas is not None:
            result['datas'] = self.datas.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('datas') is not None:
            temp_model = ListClusterDeprecatedAPIResponseBodyDatas()
            self.datas = temp_model.from_map(m['datas'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListClusterDeprecatedAPIResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterDeprecatedAPIResponseBody = None,
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
            temp_model = ListClusterDeprecatedAPIResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListClusterImagesRequest(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        image_hash: str = None,
        image_name: str = None,
        page_no: int = None,
        page_size: int = None,
        uid: str = None,
    ):
        self.cluster_id = cluster_id
        self.image_hash = image_hash
        self.image_name = image_name
        self.page_no = page_no
        self.page_size = page_size
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.image_hash is not None:
            result['image_hash'] = self.image_hash
        if self.image_name is not None:
            result['image_name'] = self.image_name
        if self.page_no is not None:
            result['page_no'] = self.page_no
        if self.page_size is not None:
            result['page_size'] = self.page_size
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('image_hash') is not None:
            self.image_hash = m.get('image_hash')
        if m.get('image_name') is not None:
            self.image_name = m.get('image_name')
        if m.get('page_no') is not None:
            self.page_no = m.get('page_no')
        if m.get('page_size') is not None:
            self.page_size = m.get('page_size')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class ListClusterImagesResponseBodyDatasData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        controller_name: str = None,
        controller_type: str = None,
        created: str = None,
        image_hash: str = None,
        image_name: str = None,
        namespace: str = None,
        uid: str = None,
        updated: str = None,
    ):
        self.cluster_id = cluster_id
        self.controller_name = controller_name
        self.controller_type = controller_type
        self.created = created
        self.image_hash = image_hash
        self.image_name = image_name
        self.namespace = namespace
        self.uid = uid
        self.updated = updated

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.controller_name is not None:
            result['controller_name'] = self.controller_name
        if self.controller_type is not None:
            result['controller_type'] = self.controller_type
        if self.created is not None:
            result['created'] = self.created
        if self.image_hash is not None:
            result['image_hash'] = self.image_hash
        if self.image_name is not None:
            result['image_name'] = self.image_name
        if self.namespace is not None:
            result['namespace'] = self.namespace
        if self.uid is not None:
            result['uid'] = self.uid
        if self.updated is not None:
            result['updated'] = self.updated
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('controller_name') is not None:
            self.controller_name = m.get('controller_name')
        if m.get('controller_type') is not None:
            self.controller_type = m.get('controller_type')
        if m.get('created') is not None:
            self.created = m.get('created')
        if m.get('image_hash') is not None:
            self.image_hash = m.get('image_hash')
        if m.get('image_name') is not None:
            self.image_name = m.get('image_name')
        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        if m.get('updated') is not None:
            self.updated = m.get('updated')
        return self


class ListClusterImagesResponseBodyDatas(TeaModel):
    def __init__(
        self,
        current: int = None,
        data: List[ListClusterImagesResponseBodyDatasData] = None,
        page_size: int = None,
        total: int = None,
    ):
        self.current = current
        self.data = data
        self.page_size = page_size
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
        if self.current is not None:
            result['current'] = self.current
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListClusterImagesResponseBodyDatasData()
                self.data.append(temp_model.from_map(k))
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListClusterImagesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        datas: ListClusterImagesResponseBodyDatas = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.datas = datas
        self.msg = msg
        self.request_id = request_id

    def validate(self):
        if self.datas:
            self.datas.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.datas is not None:
            result['datas'] = self.datas.to_map()
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('datas') is not None:
            temp_model = ListClusterImagesResponseBodyDatas()
            self.datas = temp_model.from_map(m['datas'])
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListClusterImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListClusterImagesResponseBody = None,
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
            temp_model = ListClusterImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserClustersRequest(TeaModel):
    def __init__(
        self,
        current: str = None,
        page_size: str = None,
        user_id: str = None,
    ):
        self.current = current
        self.page_size = page_size
        self.user_id = user_id

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
        if self.user_id is not None:
            result['userID'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('current') is not None:
            self.current = m.get('current')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('userID') is not None:
            self.user_id = m.get('userID')
        return self


class ListUserClustersResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['msg'] = self.msg
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            self.data = m.get('data')
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListUserClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserClustersResponseBody = None,
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
            temp_model = ListUserClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryByInstanceInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: List[str] = None,
        region_id: str = None,
    ):
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class QueryByInstanceInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        instance_id: str = None,
        region_id: str = None,
        uid: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.instance_id = instance_id
        self.region_id = region_id
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.cluster_name is not None:
            result['clusterName'] = self.cluster_name
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class QueryByInstanceInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryByInstanceInfoResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['msg'] = self.msg
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
                temp_model = QueryByInstanceInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryByInstanceInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryByInstanceInfoResponseBody = None,
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
            temp_model = QueryByInstanceInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryNodeInfoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        region_id: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region_id is not None:
            result['regionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')
        return self


class QueryNodeInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        cluser_name: str = None,
        cluster_id: str = None,
        instance_id: str = None,
        region: str = None,
        uid: str = None,
    ):
        self.cluser_name = cluser_name
        self.cluster_id = cluster_id
        self.instance_id = instance_id
        self.region = region
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluser_name is not None:
            result['cluserName'] = self.cluser_name
        if self.cluster_id is not None:
            result['clusterId'] = self.cluster_id
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.region is not None:
            result['region'] = self.region
        if self.uid is not None:
            result['uid'] = self.uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cluserName') is not None:
            self.cluser_name = m.get('cluserName')
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('region') is not None:
            self.region = m.get('region')
        if m.get('uid') is not None:
            self.uid = m.get('uid')
        return self


class QueryNodeInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[QueryNodeInfoResponseBodyData] = None,
        msg: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg
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
        if self.msg is not None:
            result['msg'] = self.msg
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
                temp_model = QueryNodeInfoResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('msg') is not None:
            self.msg = m.get('msg')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class QueryNodeInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryNodeInfoResponseBody = None,
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
            temp_model = QueryNodeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


