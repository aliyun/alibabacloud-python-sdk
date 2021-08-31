# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        build_task_id: str = None,
    ):
        self.instance_id = instance_id
        self.build_task_id = build_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        return self


class CancelArtifactBuildTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelArtifactBuildTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelArtifactBuildTaskResponseBody = None,
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
            temp_model = CancelArtifactBuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        build_record_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.build_record_id = build_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        return self


class CancelRepoBuildRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelRepoBuildRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelRepoBuildRecordResponseBody = None,
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
            temp_model = CancelRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        build_rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.build_rule_id = build_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        return self


class CreateBuildRecordByRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        build_record_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.build_record_id = build_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        return self


class CreateBuildRecordByRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateBuildRecordByRuleResponseBody = None,
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
            temp_model = CreateBuildRecordByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        return self


class CreateChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateChartNamespaceResponseBody = None,
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
            temp_model = CreateChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_type: str = None,
        summary: str = None,
    ):
        self.instance_id = instance_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_type = repo_type
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class CreateChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        repo_id: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.repo_id = repo_id
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateChartRepositoryResponseBody = None,
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
            temp_model = CreateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        endpoint_type: str = None,
        entry: str = None,
        comment: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.endpoint_type = endpoint_type
        self.entry = entry
        self.comment = comment
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class CreateInstanceEndpointAclPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceEndpointAclPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceEndpointAclPolicyResponseBody = None,
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
            temp_model = CreateInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class CreateInstanceVpcEndpointLinkedVpcResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateInstanceVpcEndpointLinkedVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateInstanceVpcEndpointLinkedVpcResponseBody = None,
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
            temp_model = CreateInstanceVpcEndpointLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        return self


class CreateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateNamespaceResponseBody = None,
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        push_type: str = None,
        push_name: str = None,
        image_tag: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.dockerfile_location = dockerfile_location
        self.dockerfile_name = dockerfile_name
        self.push_type = push_type
        self.push_name = push_name
        self.image_tag = image_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        return self


class CreateRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        build_rule_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.build_rule_id = build_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        return self


class CreateRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoBuildRuleResponseBody = None,
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
            temp_model = CreateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_type: str = None,
        summary: str = None,
        detail: str = None,
        tag_immutability: bool = None,
    ):
        self.instance_id = instance_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_type = repo_type
        self.summary = summary
        self.detail = detail
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        repo_id: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.repo_id = repo_id
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepositoryResponseBody = None,
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        code_repo_type: str = None,
        code_repo_namespace_name: str = None,
        code_repo_name: str = None,
        auto_build: bool = None,
        oversea_build: bool = None,
        disable_cache_build: bool = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.code_repo_type = code_repo_type
        self.code_repo_namespace_name = code_repo_namespace_name
        self.code_repo_name = code_repo_name
        self.auto_build = auto_build
        self.oversea_build = oversea_build
        self.disable_cache_build = disable_cache_build

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        return self


class CreateRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoSourceCodeRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoSourceCodeRepoResponseBody = None,
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
            temp_model = CreateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        target_region_id: str = None,
        target_instance_id: str = None,
        target_namespace_name: str = None,
        target_repo_name: str = None,
        tag_filter: str = None,
        sync_scope: str = None,
        sync_rule_name: str = None,
        sync_trigger: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repo_name = repo_name
        self.target_region_id = target_region_id
        self.target_instance_id = target_instance_id
        self.target_namespace_name = target_namespace_name
        self.target_repo_name = target_repo_name
        self.tag_filter = tag_filter
        self.sync_scope = sync_scope
        self.sync_rule_name = sync_rule_name
        self.sync_trigger = sync_trigger

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        return self


class CreateRepoSyncRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        sync_rule_id: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.sync_rule_id = sync_rule_id
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoSyncRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoSyncRuleResponseBody = None,
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
            temp_model = CreateRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncTaskByRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        sync_rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.sync_rule_id = sync_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        return self


class CreateRepoSyncTaskByRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        sync_task_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.sync_task_id = sync_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        return self


class CreateRepoSyncTaskByRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoSyncTaskByRuleResponseBody = None,
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
            temp_model = CreateRepoSyncTaskByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        from_tag: str = None,
        to_tag: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repo_name = repo_name
        self.from_tag = from_tag
        self.to_tag = to_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.from_tag is not None:
            result['FromTag'] = self.from_tag
        if self.to_tag is not None:
            result['ToTag'] = self.to_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('FromTag') is not None:
            self.from_tag = m.get('FromTag')
        if m.get('ToTag') is not None:
            self.to_tag = m.get('ToTag')
        return self


class CreateRepoTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoTagResponseBody = None,
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
            temp_model = CreateRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagScanTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        digest: str = None,
        scan_service: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.digest = digest
        self.scan_service = scan_service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        return self


class CreateRepoTagScanTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoTagScanTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoTagScanTaskResponseBody = None,
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
            temp_model = CreateRepoTagScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_name: str = None,
        trigger_url: str = None,
        trigger_type: str = None,
        trigger_tag: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.trigger_name = trigger_name
        self.trigger_url = trigger_url
        self.trigger_type = trigger_type
        self.trigger_tag = trigger_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        return self


class CreateRepoTriggerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        trigger_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.trigger_id = trigger_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        return self


class CreateRepoTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRepoTriggerResponseBody = None,
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
            temp_model = CreateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DeleteChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChartNamespaceResponseBody = None,
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
            temp_model = DeleteChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartReleaseRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        chart: str = None,
        release: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.chart = chart
        self.release = release
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.release is not None:
            result['Release'] = self.release
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class DeleteChartReleaseResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChartReleaseResponseBody = None,
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
            temp_model = DeleteChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class DeleteChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteChartRepositoryResponseBody = None,
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
            temp_model = DeleteChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        endpoint_type: str = None,
        entry: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.endpoint_type = endpoint_type
        self.entry = entry
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class DeleteInstanceEndpointAclPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceEndpointAclPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceEndpointAclPolicyResponseBody = None,
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
            temp_model = DeleteInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class DeleteInstanceVpcEndpointLinkedVpcResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteInstanceVpcEndpointLinkedVpcResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteInstanceVpcEndpointLinkedVpcResponseBody = None,
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
            temp_model = DeleteInstanceVpcEndpointLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class DeleteNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteNamespaceResponseBody = None,
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        build_rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.build_rule_id = build_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        return self


class DeleteRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepoBuildRuleResponseBody = None,
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
            temp_model = DeleteRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class DeleteRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepositoryResponseBody = None,
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
            temp_model = DeleteRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoSyncRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sync_rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.sync_rule_id = sync_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        return self


class DeleteRepoSyncRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoSyncRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepoSyncRuleResponseBody = None,
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
            temp_model = DeleteRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class DeleteRepoTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepoTagResponseBody = None,
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
            temp_model = DeleteRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.trigger_id = trigger_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        return self


class DeleteRepoTriggerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRepoTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRepoTriggerResponseBody = None,
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
            temp_model = DeleteRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        build_task_id: str = None,
    ):
        self.instance_id = instance_id
        self.build_task_id = build_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        return self


class GetArtifactBuildTaskResponseBodySourceArtifact(TeaModel):
    def __init__(
        self,
        repo_id: str = None,
        version: str = None,
        artifact_type: str = None,
    ):
        self.repo_id = repo_id
        self.version = version
        self.artifact_type = artifact_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        return self


class GetArtifactBuildTaskResponseBodyTargetArtifact(TeaModel):
    def __init__(
        self,
        repo_id: str = None,
        version: str = None,
        artifact_type: str = None,
    ):
        self.repo_id = repo_id
        self.version = version
        self.artifact_type = artifact_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        return self


class GetArtifactBuildTaskResponseBody(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        start_time: int = None,
        artifact_build_type: str = None,
        request_id: str = None,
        task_status: str = None,
        build_task_id: str = None,
        code: str = None,
        is_success: bool = None,
        instructions: List[str] = None,
        source_artifact: GetArtifactBuildTaskResponseBodySourceArtifact = None,
        target_artifact: GetArtifactBuildTaskResponseBodyTargetArtifact = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.artifact_build_type = artifact_build_type
        self.request_id = request_id
        self.task_status = task_status
        self.build_task_id = build_task_id
        self.code = code
        self.is_success = is_success
        self.instructions = instructions
        self.source_artifact = source_artifact
        self.target_artifact = target_artifact

    def validate(self):
        if self.source_artifact:
            self.source_artifact.validate()
        if self.target_artifact:
            self.target_artifact.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.instructions is not None:
            result['Instructions'] = self.instructions
        if self.source_artifact is not None:
            result['SourceArtifact'] = self.source_artifact.to_map()
        if self.target_artifact is not None:
            result['TargetArtifact'] = self.target_artifact.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')
        if m.get('SourceArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodySourceArtifact()
            self.source_artifact = temp_model.from_map(m['SourceArtifact'])
        if m.get('TargetArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodyTargetArtifact()
            self.target_artifact = temp_model.from_map(m['TargetArtifact'])
        return self


class GetArtifactBuildTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetArtifactBuildTaskResponseBody = None,
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
            temp_model = GetArtifactBuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetAuthorizationTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        expire_time: int = None,
        code: str = None,
        is_success: bool = None,
        temp_username: str = None,
        authorization_token: str = None,
    ):
        self.request_id = request_id
        self.expire_time = expire_time
        self.code = code
        self.is_success = is_success
        self.temp_username = temp_username
        self.authorization_token = authorization_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.temp_username is not None:
            result['TempUsername'] = self.temp_username
        if self.authorization_token is not None:
            result['AuthorizationToken'] = self.authorization_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('TempUsername') is not None:
            self.temp_username = m.get('TempUsername')
        if m.get('AuthorizationToken') is not None:
            self.authorization_token = m.get('AuthorizationToken')
        return self


class GetAuthorizationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthorizationTokenResponseBody = None,
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
            temp_model = GetAuthorizationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        default_repo_type: str = None,
        namespace_id: str = None,
        namespace_status: str = None,
        request_id: str = None,
        code: str = None,
        instance_id: str = None,
        auto_create_repo: bool = None,
        is_success: bool = None,
        namespace_name: str = None,
    ):
        self.default_repo_type = default_repo_type
        self.namespace_id = namespace_id
        self.namespace_status = namespace_status
        self.request_id = request_id
        self.code = code
        self.instance_id = instance_id
        self.auto_create_repo = auto_create_repo
        self.is_success = is_success
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetChartNamespaceResponseBody = None,
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
            temp_model = GetChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class GetChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        summary: str = None,
        create_time: int = None,
        is_success: bool = None,
        instance_id: str = None,
        repo_status: str = None,
        repo_type: str = None,
        request_id: str = None,
        repo_id: str = None,
        modified_time: int = None,
        code: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
    ):
        self.summary = summary
        self.create_time = create_time
        self.is_success = is_success
        self.instance_id = instance_id
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.request_id = request_id
        self.repo_id = repo_id
        self.modified_time = modified_time
        self.code = code
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.code is not None:
            result['Code'] = self.code
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class GetChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetChartRepositoryResponseBody = None,
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
            temp_model = GetChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        modified_time: int = None,
        request_id: str = None,
        create_time: int = None,
        instance_name: str = None,
        instance_specification: str = None,
        code: str = None,
        instance_status: str = None,
        instance_id: str = None,
        is_success: bool = None,
    ):
        self.modified_time = modified_time
        self.request_id = request_id
        self.create_time = create_time
        self.instance_name = instance_name
        self.instance_specification = instance_specification
        self.code = code
        self.instance_status = instance_status
        self.instance_id = instance_id
        self.is_success = is_success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceResponseBody = None,
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        count: int = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.count is not None:
            result['Count'] = self.count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        return self


class GetInstanceCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceCountResponseBody = None,
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
            temp_model = GetInstanceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceEndpointRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        endpoint_type: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.endpoint_type = endpoint_type
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class GetInstanceEndpointResponseBodyDomains(TeaModel):
    def __init__(
        self,
        type: str = None,
        domain: str = None,
    ):
        self.type = type
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class GetInstanceEndpointResponseBodyAclEntries(TeaModel):
    def __init__(
        self,
        comment: str = None,
        entry: str = None,
    ):
        self.comment = comment
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class GetInstanceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        request_id: str = None,
        code: str = None,
        is_success: bool = None,
        acl_enable: bool = None,
        enable: bool = None,
        domains: List[GetInstanceEndpointResponseBodyDomains] = None,
        acl_entries: List[GetInstanceEndpointResponseBodyAclEntries] = None,
    ):
        self.status = status
        self.request_id = request_id
        self.code = code
        self.is_success = is_success
        self.acl_enable = acl_enable
        self.enable = enable
        self.domains = domains
        self.acl_entries = acl_entries

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = GetInstanceEndpointResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetInstanceEndpointResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        return self


class GetInstanceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceEndpointResponseBody = None,
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
            temp_model = GetInstanceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceUsageRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetInstanceUsageResponseBody(TeaModel):
    def __init__(
        self,
        namespace_usage: str = None,
        repo_quota: str = None,
        request_id: str = None,
        chart_namespace_quota: str = None,
        repo_usage: str = None,
        namespace_quota: str = None,
        code: str = None,
        is_success: bool = None,
        chart_repo_usage: str = None,
        chart_namespace_usage: str = None,
        chart_repo_quota: str = None,
    ):
        self.namespace_usage = namespace_usage
        self.repo_quota = repo_quota
        self.request_id = request_id
        self.chart_namespace_quota = chart_namespace_quota
        self.repo_usage = repo_usage
        self.namespace_quota = namespace_quota
        self.code = code
        self.is_success = is_success
        self.chart_repo_usage = chart_repo_usage
        self.chart_namespace_usage = chart_namespace_usage
        self.chart_repo_quota = chart_repo_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_usage is not None:
            result['NamespaceUsage'] = self.namespace_usage
        if self.repo_quota is not None:
            result['RepoQuota'] = self.repo_quota
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.chart_namespace_quota is not None:
            result['ChartNamespaceQuota'] = self.chart_namespace_quota
        if self.repo_usage is not None:
            result['RepoUsage'] = self.repo_usage
        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.chart_repo_usage is not None:
            result['ChartRepoUsage'] = self.chart_repo_usage
        if self.chart_namespace_usage is not None:
            result['ChartNamespaceUsage'] = self.chart_namespace_usage
        if self.chart_repo_quota is not None:
            result['ChartRepoQuota'] = self.chart_repo_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NamespaceUsage') is not None:
            self.namespace_usage = m.get('NamespaceUsage')
        if m.get('RepoQuota') is not None:
            self.repo_quota = m.get('RepoQuota')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ChartNamespaceQuota') is not None:
            self.chart_namespace_quota = m.get('ChartNamespaceQuota')
        if m.get('RepoUsage') is not None:
            self.repo_usage = m.get('RepoUsage')
        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ChartRepoUsage') is not None:
            self.chart_repo_usage = m.get('ChartRepoUsage')
        if m.get('ChartNamespaceUsage') is not None:
            self.chart_namespace_usage = m.get('ChartNamespaceUsage')
        if m.get('ChartRepoQuota') is not None:
            self.chart_repo_quota = m.get('ChartRepoQuota')
        return self


class GetInstanceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceUsageResponseBody = None,
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
            temp_model = GetInstanceUsageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceVpcEndpointRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class GetInstanceVpcEndpointResponseBodyLinkedVpcs(TeaModel):
    def __init__(
        self,
        status: str = None,
        vpc_id: str = None,
        ip: str = None,
        default_access: bool = None,
        vswitch_id: str = None,
    ):
        self.status = status
        self.vpc_id = vpc_id
        self.ip = ip
        self.default_access = default_access
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.default_access is not None:
            result['DefaultAccess'] = self.default_access
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('DefaultAccess') is not None:
            self.default_access = m.get('DefaultAccess')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class GetInstanceVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        enable: bool = None,
        domains: List[str] = None,
        linked_vpcs: List[GetInstanceVpcEndpointResponseBodyLinkedVpcs] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.enable = enable
        self.domains = domains
        self.linked_vpcs = linked_vpcs

    def validate(self):
        if self.linked_vpcs:
            for k in self.linked_vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.domains is not None:
            result['Domains'] = self.domains
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = GetInstanceVpcEndpointResponseBodyLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        return self


class GetInstanceVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetInstanceVpcEndpointResponseBody = None,
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
            temp_model = GetInstanceVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        namespace_id: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.namespace_id = namespace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        return self


class GetNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        default_repo_type: str = None,
        namespace_id: str = None,
        namespace_status: str = None,
        request_id: str = None,
        code: str = None,
        instance_id: str = None,
        auto_create_repo: bool = None,
        is_success: bool = None,
        namespace_name: str = None,
    ):
        self.default_repo_type = default_repo_type
        self.namespace_id = namespace_id
        self.namespace_status = namespace_status
        self.request_id = request_id
        self.code = code
        self.instance_id = instance_id
        self.auto_create_repo = auto_create_repo
        self.is_success = is_success
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetNamespaceResponseBody = None,
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
            temp_model = GetNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        build_record_id: str = None,
    ):
        self.instance_id = instance_id
        self.build_record_id = build_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        return self


class GetRepoBuildRecordResponseBodyImage(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        image_tag: str = None,
        repo_name: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.image_tag = image_tag
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class GetRepoBuildRecordResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        end_time: int = None,
        start_time: int = None,
        request_id: str = None,
        code: str = None,
        is_success: bool = None,
        build_record_id: str = None,
        image: GetRepoBuildRecordResponseBodyImage = None,
    ):
        self.status = status
        self.end_time = end_time
        self.start_time = start_time
        self.request_id = request_id
        self.code = code
        self.is_success = is_success
        self.build_record_id = build_record_id
        self.image = image

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.image is not None:
            result['Image'] = self.image.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Image') is not None:
            temp_model = GetRepoBuildRecordResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        return self


class GetRepoBuildRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoBuildRecordResponseBody = None,
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
            temp_model = GetRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        build_record_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.build_record_id = build_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        return self


class GetRepoBuildRecordStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        build_status: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.build_status = build_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        return self


class GetRepoBuildRecordStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoBuildRecordStatusResponseBody = None,
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
            temp_model = GetRepoBuildRecordStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class GetRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        summary: str = None,
        create_time: int = None,
        is_success: bool = None,
        instance_id: str = None,
        repo_status: str = None,
        repo_type: str = None,
        repo_build_type: str = None,
        modified_time: int = None,
        request_id: str = None,
        repo_id: str = None,
        code: str = None,
        repo_namespace_name: str = None,
        tag_immutability: bool = None,
        repo_name: str = None,
        detail: str = None,
    ):
        self.summary = summary
        self.create_time = create_time
        self.is_success = is_success
        self.instance_id = instance_id
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.repo_build_type = repo_build_type
        self.modified_time = modified_time
        self.request_id = request_id
        self.repo_id = repo_id
        self.code = code
        self.repo_namespace_name = repo_namespace_name
        self.tag_immutability = tag_immutability
        self.repo_name = repo_name
        self.detail = detail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.code is not None:
            result['Code'] = self.code
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.detail is not None:
            result['Detail'] = self.detail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        return self


class GetRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepositoryResponseBody = None,
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
            temp_model = GetRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoSourceCodeRepoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class GetRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(
        self,
        code_repo_type: str = None,
        repo_id: str = None,
        request_id: str = None,
        code_repo_namespace_name: str = None,
        oversea_build: str = None,
        code: str = None,
        code_repo_name: str = None,
        auto_build: str = None,
        is_success: bool = None,
        disable_cache_build: str = None,
        code_repo_domain: str = None,
    ):
        self.code_repo_type = code_repo_type
        self.repo_id = repo_id
        self.request_id = request_id
        self.code_repo_namespace_name = code_repo_namespace_name
        self.oversea_build = oversea_build
        self.code = code
        self.code_repo_name = code_repo_name
        self.auto_build = auto_build
        self.is_success = is_success
        self.disable_cache_build = disable_cache_build
        self.code_repo_domain = code_repo_domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.code is not None:
            result['Code'] = self.code
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.code_repo_domain is not None:
            result['CodeRepoDomain'] = self.code_repo_domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('CodeRepoDomain') is not None:
            self.code_repo_domain = m.get('CodeRepoDomain')
        return self


class GetRepoSourceCodeRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoSourceCodeRepoResponseBody = None,
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
            temp_model = GetRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoSyncTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sync_task_id: str = None,
    ):
        self.instance_id = instance_id
        self.sync_task_id = sync_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        return self


class GetRepoSyncTaskResponseBodyImageFrom(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        instance_id: str = None,
        image_tag: str = None,
        repo_name: str = None,
        region_id: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.instance_id = instance_id
        self.image_tag = image_tag
        self.repo_name = repo_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetRepoSyncTaskResponseBodyImageTo(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        instance_id: str = None,
        image_tag: str = None,
        repo_name: str = None,
        region_id: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.instance_id = instance_id
        self.image_tag = image_tag
        self.repo_name = repo_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetRepoSyncTaskResponseBodyLayerTasks(TeaModel):
    def __init__(
        self,
        task_status: str = None,
        digest: str = None,
        synced_size: int = None,
        size: int = None,
        sync_layer_task_id: str = None,
        artifact_digest: str = None,
    ):
        self.task_status = task_status
        self.digest = digest
        self.synced_size = synced_size
        self.size = size
        self.sync_layer_task_id = sync_layer_task_id
        self.artifact_digest = artifact_digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.size is not None:
            result['Size'] = self.size
        if self.sync_layer_task_id is not None:
            result['SyncLayerTaskId'] = self.sync_layer_task_id
        if self.artifact_digest is not None:
            result['ArtifactDigest'] = self.artifact_digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SyncLayerTaskId') is not None:
            self.sync_layer_task_id = m.get('SyncLayerTaskId')
        if m.get('ArtifactDigest') is not None:
            self.artifact_digest = m.get('ArtifactDigest')
        return self


class GetRepoSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        sync_rule_id: str = None,
        progress: int = None,
        request_id: str = None,
        synced_size: int = None,
        task_status: str = None,
        sync_task_id: str = None,
        sync_batch_task_id: str = None,
        code: str = None,
        is_success: bool = None,
        task_trigger: str = None,
        image_from: GetRepoSyncTaskResponseBodyImageFrom = None,
        image_to: GetRepoSyncTaskResponseBodyImageTo = None,
        layer_tasks: List[GetRepoSyncTaskResponseBodyLayerTasks] = None,
    ):
        self.sync_rule_id = sync_rule_id
        self.progress = progress
        self.request_id = request_id
        self.synced_size = synced_size
        self.task_status = task_status
        self.sync_task_id = sync_task_id
        self.sync_batch_task_id = sync_batch_task_id
        self.code = code
        self.is_success = is_success
        self.task_trigger = task_trigger
        self.image_from = image_from
        self.image_to = image_to
        self.layer_tasks = layer_tasks

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()
        if self.layer_tasks:
            for k in self.layer_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        result['LayerTasks'] = []
        if self.layer_tasks is not None:
            for k in self.layer_tasks:
                result['LayerTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        if m.get('ImageFrom') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        self.layer_tasks = []
        if m.get('LayerTasks') is not None:
            for k in m.get('LayerTasks'):
                temp_model = GetRepoSyncTaskResponseBodyLayerTasks()
                self.layer_tasks.append(temp_model.from_map(k))
        return self


class GetRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoSyncTaskResponseBody = None,
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
            temp_model = GetRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagLayersRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        digest: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.digest = digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.digest is not None:
            result['Digest'] = self.digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        return self


class GetRepoTagLayersResponseBodyLayers(TeaModel):
    def __init__(
        self,
        blob_digest: str = None,
        layer_index: int = None,
        layer_instruction: str = None,
        layer_cmd: str = None,
        blob_size: int = None,
    ):
        self.blob_digest = blob_digest
        self.layer_index = layer_index
        self.layer_instruction = layer_instruction
        self.layer_cmd = layer_cmd
        self.blob_size = blob_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blob_digest is not None:
            result['BlobDigest'] = self.blob_digest
        if self.layer_index is not None:
            result['LayerIndex'] = self.layer_index
        if self.layer_instruction is not None:
            result['LayerInstruction'] = self.layer_instruction
        if self.layer_cmd is not None:
            result['LayerCMD'] = self.layer_cmd
        if self.blob_size is not None:
            result['BlobSize'] = self.blob_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlobDigest') is not None:
            self.blob_digest = m.get('BlobDigest')
        if m.get('LayerIndex') is not None:
            self.layer_index = m.get('LayerIndex')
        if m.get('LayerInstruction') is not None:
            self.layer_instruction = m.get('LayerInstruction')
        if m.get('LayerCMD') is not None:
            self.layer_cmd = m.get('LayerCMD')
        if m.get('BlobSize') is not None:
            self.blob_size = m.get('BlobSize')
        return self


class GetRepoTagLayersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        layers: List[GetRepoTagLayersResponseBodyLayers] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.layers = layers

    def validate(self):
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        return self


class GetRepoTagLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoTagLayersResponseBody = None,
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
            temp_model = GetRepoTagLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagManifestRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        tag: str = None,
        schema_version: int = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.tag = tag
        self.schema_version = schema_version
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class GetRepoTagManifestResponseBodyManifestFsLayers(TeaModel):
    def __init__(
        self,
        blob_sum: str = None,
    ):
        self.blob_sum = blob_sum

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blob_sum is not None:
            result['BlobSum'] = self.blob_sum
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlobSum') is not None:
            self.blob_sum = m.get('BlobSum')
        return self


class GetRepoTagManifestResponseBodyManifestHistory(TeaModel):
    def __init__(
        self,
        v_1compatibility: Dict[str, Any] = None,
    ):
        self.v_1compatibility = v_1compatibility

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.v_1compatibility is not None:
            result['V1Compatibility'] = self.v_1compatibility
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('V1Compatibility') is not None:
            self.v_1compatibility = m.get('V1Compatibility')
        return self


class GetRepoTagManifestResponseBodyManifestSignatures(TeaModel):
    def __init__(
        self,
        signature: str = None,
        header: Dict[str, Any] = None,
        protected: str = None,
    ):
        self.signature = signature
        self.header = header
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.signature is not None:
            result['Signature'] = self.signature
        if self.header is not None:
            result['Header'] = self.header
        if self.protected is not None:
            result['Protected'] = self.protected
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Protected') is not None:
            self.protected = m.get('Protected')
        return self


class GetRepoTagManifestResponseBodyManifestLayers(TeaModel):
    def __init__(
        self,
        digest: str = None,
        media_type: str = None,
        size: int = None,
    ):
        self.digest = digest
        self.media_type = media_type
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetRepoTagManifestResponseBodyManifestConfig(TeaModel):
    def __init__(
        self,
        digest: str = None,
        media_type: str = None,
        size: int = None,
    ):
        self.digest = digest
        self.media_type = media_type
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class GetRepoTagManifestResponseBodyManifest(TeaModel):
    def __init__(
        self,
        tag: str = None,
        name: str = None,
        media_type: str = None,
        schema_version: int = None,
        architecture: str = None,
        fs_layers: List[GetRepoTagManifestResponseBodyManifestFsLayers] = None,
        history: List[GetRepoTagManifestResponseBodyManifestHistory] = None,
        signatures: List[GetRepoTagManifestResponseBodyManifestSignatures] = None,
        layers: List[GetRepoTagManifestResponseBodyManifestLayers] = None,
        config: GetRepoTagManifestResponseBodyManifestConfig = None,
    ):
        self.tag = tag
        self.name = name
        self.media_type = media_type
        self.schema_version = schema_version
        self.architecture = architecture
        self.fs_layers = fs_layers
        self.history = history
        self.signatures = signatures
        self.layers = layers
        self.config = config

    def validate(self):
        if self.fs_layers:
            for k in self.fs_layers:
                if k:
                    k.validate()
        if self.history:
            for k in self.history:
                if k:
                    k.validate()
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.name is not None:
            result['Name'] = self.name
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        result['FsLayers'] = []
        if self.fs_layers is not None:
            for k in self.fs_layers:
                result['FsLayers'].append(k.to_map() if k else None)
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.config is not None:
            result['Config'] = self.config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        self.fs_layers = []
        if m.get('FsLayers') is not None:
            for k in m.get('FsLayers'):
                temp_model = GetRepoTagManifestResponseBodyManifestFsLayers()
                self.fs_layers.append(temp_model.from_map(k))
        self.history = []
        if m.get('History') is not None:
            for k in m.get('History'):
                temp_model = GetRepoTagManifestResponseBodyManifestHistory()
                self.history.append(temp_model.from_map(k))
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = GetRepoTagManifestResponseBodyManifestSignatures()
                self.signatures.append(temp_model.from_map(k))
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagManifestResponseBodyManifestLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('Config') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifestConfig()
            self.config = temp_model.from_map(m['Config'])
        return self


class GetRepoTagManifestResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        manifest: GetRepoTagManifestResponseBodyManifest = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.manifest = manifest

    def validate(self):
        if self.manifest:
            self.manifest.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.manifest is not None:
            result['Manifest'] = self.manifest.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Manifest') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifest()
            self.manifest = temp_model.from_map(m['Manifest'])
        return self


class GetRepoTagManifestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoTagManifestResponseBody = None,
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
            temp_model = GetRepoTagManifestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        scan_task_id: str = None,
        digest: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.scan_task_id = scan_task_id
        self.digest = digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.digest is not None:
            result['Digest'] = self.digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        return self


class GetRepoTagScanStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        scan_service: str = None,
    ):
        self.status = status
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.scan_service = scan_service

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        return self


class GetRepoTagScanStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoTagScanStatusResponseBody = None,
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
            temp_model = GetRepoTagScanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanSummaryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        scan_task_id: str = None,
        digest: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.scan_task_id = scan_task_id
        self.digest = digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.digest is not None:
            result['Digest'] = self.digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        return self


class GetRepoTagScanSummaryResponseBody(TeaModel):
    def __init__(
        self,
        unknown_severity: int = None,
        request_id: str = None,
        total_severity: int = None,
        code: str = None,
        medium_severity: int = None,
        is_success: bool = None,
        high_severity: int = None,
        low_severity: int = None,
    ):
        self.unknown_severity = unknown_severity
        self.request_id = request_id
        self.total_severity = total_severity
        self.code = code
        self.medium_severity = medium_severity
        self.is_success = is_success
        self.high_severity = high_severity
        self.low_severity = low_severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.unknown_severity is not None:
            result['UnknownSeverity'] = self.unknown_severity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_severity is not None:
            result['TotalSeverity'] = self.total_severity
        if self.code is not None:
            result['Code'] = self.code
        if self.medium_severity is not None:
            result['MediumSeverity'] = self.medium_severity
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.high_severity is not None:
            result['HighSeverity'] = self.high_severity
        if self.low_severity is not None:
            result['LowSeverity'] = self.low_severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UnknownSeverity') is not None:
            self.unknown_severity = m.get('UnknownSeverity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalSeverity') is not None:
            self.total_severity = m.get('TotalSeverity')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('MediumSeverity') is not None:
            self.medium_severity = m.get('MediumSeverity')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('HighSeverity') is not None:
            self.high_severity = m.get('HighSeverity')
        if m.get('LowSeverity') is not None:
            self.low_severity = m.get('LowSeverity')
        return self


class GetRepoTagScanSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRepoTagScanSummaryResponseBody = None,
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
            temp_model = GetRepoTagScanSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactBuildTaskLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        build_task_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.build_task_id = build_task_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactBuildTaskLogResponseBodyBuildTaskLogs(TeaModel):
    def __init__(
        self,
        message: str = None,
        line_number: int = None,
    ):
        self.message = message
        self.line_number = line_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.line_number is not None:
            result['LineNumber'] = self.line_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        return self


class ListArtifactBuildTaskLogResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        total_count: int = None,
        build_task_logs: List[ListArtifactBuildTaskLogResponseBodyBuildTaskLogs] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.total_count = total_count
        self.build_task_logs = build_task_logs

    def validate(self):
        if self.build_task_logs:
            for k in self.build_task_logs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['BuildTaskLogs'] = []
        if self.build_task_logs is not None:
            for k in self.build_task_logs:
                result['BuildTaskLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.build_task_logs = []
        if m.get('BuildTaskLogs') is not None:
            for k in m.get('BuildTaskLogs'):
                temp_model = ListArtifactBuildTaskLogResponseBodyBuildTaskLogs()
                self.build_task_logs.append(temp_model.from_map(k))
        return self


class ListArtifactBuildTaskLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListArtifactBuildTaskLogResponseBody = None,
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
            temp_model = ListArtifactBuildTaskLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_status: str = None,
        namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.namespace_status = namespace_status
        self.namespace_name = namespace_name
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChartNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        default_repo_type: str = None,
        namespace_status: str = None,
        namespace_id: str = None,
        auto_create_repo: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.default_repo_type = default_repo_type
        self.namespace_status = namespace_status
        self.namespace_id = namespace_id
        self.auto_create_repo = auto_create_repo
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class ListChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        namespaces: List[ListChartNamespaceResponseBodyNamespaces] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.namespaces = namespaces

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListChartNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        return self


class ListChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChartNamespaceResponseBody = None,
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
            temp_model = ListChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartReleaseRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
        chart: str = None,
    ):
        self.instance_id = instance_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.page_no = page_no
        self.page_size = page_size
        self.chart = chart

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.chart is not None:
            result['Chart'] = self.chart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        return self


class ListChartReleaseResponseBodyChartReleases(TeaModel):
    def __init__(
        self,
        status: str = None,
        modified_time: int = None,
        repo_id: str = None,
        release: str = None,
        size: str = None,
        instance_id: str = None,
        chart: str = None,
    ):
        self.status = status
        self.modified_time = modified_time
        self.repo_id = repo_id
        self.release = release
        self.size = size
        self.instance_id = instance_id
        self.chart = chart

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.release is not None:
            result['Release'] = self.release
        if self.size is not None:
            result['Size'] = self.size
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.chart is not None:
            result['Chart'] = self.chart
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        return self


class ListChartReleaseResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        chart_releases: List[ListChartReleaseResponseBodyChartReleases] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.chart_releases = chart_releases

    def validate(self):
        if self.chart_releases:
            for k in self.chart_releases:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['ChartReleases'] = []
        if self.chart_releases is not None:
            for k in self.chart_releases:
                result['ChartReleases'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.chart_releases = []
        if m.get('ChartReleases') is not None:
            for k in m.get('ChartReleases'):
                temp_model = ListChartReleaseResponseBodyChartReleases()
                self.chart_releases.append(temp_model.from_map(k))
        return self


class ListChartReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChartReleaseResponseBody = None,
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
            temp_model = ListChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_status: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.repo_status = repo_status
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChartRepositoryResponseBodyRepositories(TeaModel):
    def __init__(
        self,
        summary: str = None,
        modified_time: int = None,
        repo_id: str = None,
        create_time: int = None,
        repo_namespace_name: str = None,
        instance_id: str = None,
        repo_type: str = None,
        repo_status: str = None,
        repo_name: str = None,
    ):
        self.summary = summary
        self.modified_time = modified_time
        self.repo_id = repo_id
        self.create_time = create_time
        self.repo_namespace_name = repo_namespace_name
        self.instance_id = instance_id
        self.repo_type = repo_type
        self.repo_status = repo_status
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class ListChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        repositories: List[ListChartRepositoryResponseBodyRepositories] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.repositories = repositories

    def validate(self):
        if self.repositories:
            for k in self.repositories:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListChartRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        return self


class ListChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListChartRepositoryResponseBody = None,
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
            temp_model = ListChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_status: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(
        self,
        modified_time: str = None,
        instance_name: str = None,
        create_time: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        instance_id: str = None,
        region_id: str = None,
    ):
        self.modified_time = modified_time
        self.instance_name = instance_name
        self.create_time = create_time
        self.instance_specification = instance_specification
        self.instance_status = instance_status
        self.instance_id = instance_id
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: int = None,
        instances: List[ListInstanceResponseBodyInstances] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceResponseBody = None,
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
            temp_model = ListInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceEndpointRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class ListInstanceEndpointResponseBodyEndpointsDomains(TeaModel):
    def __init__(
        self,
        type: str = None,
        domain: str = None,
    ):
        self.type = type
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.domain is not None:
            result['Domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        return self


class ListInstanceEndpointResponseBodyEndpointsLinkedVpcs(TeaModel):
    def __init__(
        self,
        vpc_id: str = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        return self


class ListInstanceEndpointResponseBodyEndpointsAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
    ):
        self.entry = entry

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.entry is not None:
            result['Entry'] = self.entry
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        return self


class ListInstanceEndpointResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        status: str = None,
        endpoint_type: str = None,
        acl_enable: bool = None,
        enable: bool = None,
        domains: List[ListInstanceEndpointResponseBodyEndpointsDomains] = None,
        linked_vpcs: List[ListInstanceEndpointResponseBodyEndpointsLinkedVpcs] = None,
        acl_entries: List[ListInstanceEndpointResponseBodyEndpointsAclEntries] = None,
    ):
        self.status = status
        self.endpoint_type = endpoint_type
        self.acl_enable = acl_enable
        self.enable = enable
        self.domains = domains
        self.linked_vpcs = linked_vpcs
        self.acl_entries = acl_entries

    def validate(self):
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.linked_vpcs:
            for k in self.linked_vpcs:
                if k:
                    k.validate()
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        if self.enable is not None:
            result['Enable'] = self.enable
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsDomains()
                self.domains.append(temp_model.from_map(k))
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        return self


class ListInstanceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        endpoints: List[ListInstanceEndpointResponseBodyEndpoints] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.endpoints = endpoints

    def validate(self):
        if self.endpoints:
            for k in self.endpoints:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListInstanceEndpointResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        return self


class ListInstanceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceEndpointResponseBody = None,
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
            temp_model = ListInstanceEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRegionRequest(TeaModel):
    def __init__(
        self,
        lang: str = None,
    ):
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.lang is not None:
            result['Lang'] = self.lang
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        return self


class ListInstanceRegionResponseBodyRegions(TeaModel):
    def __init__(
        self,
        local_name: str = None,
        region_id: str = None,
    ):
        self.local_name = local_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListInstanceRegionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        regions: List[ListInstanceRegionResponseBodyRegions] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.regions = regions

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListInstanceRegionResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        return self


class ListInstanceRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListInstanceRegionResponseBody = None,
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
            temp_model = ListInstanceRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_status: str = None,
        namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.namespace_status = namespace_status
        self.namespace_name = namespace_name
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        default_repo_type: str = None,
        namespace_status: str = None,
        namespace_id: str = None,
        auto_create_repo: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.default_repo_type = default_repo_type
        self.namespace_status = namespace_status
        self.namespace_id = namespace_id
        self.auto_create_repo = auto_create_repo
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class ListNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        namespaces: List[ListNamespaceResponseBodyNamespaces] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.namespaces = namespaces

    def validate(self):
        if self.namespaces:
            for k in self.namespaces:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        return self


class ListNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListNamespaceResponseBody = None,
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
            temp_model = ListNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepoBuildRecordResponseBodyBuildRecordsImage(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        image_tag: str = None,
        repo_id: str = None,
        repo_name: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.image_tag = image_tag
        self.repo_id = repo_id
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class ListRepoBuildRecordResponseBodyBuildRecords(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        start_time: str = None,
        build_status: str = None,
        build_record_id: str = None,
        image: ListRepoBuildRecordResponseBodyBuildRecordsImage = None,
    ):
        self.end_time = end_time
        self.start_time = start_time
        self.build_status = build_status
        self.build_record_id = build_record_id
        self.image = image

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.image is not None:
            result['Image'] = self.image.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Image') is not None:
            temp_model = ListRepoBuildRecordResponseBodyBuildRecordsImage()
            self.image = temp_model.from_map(m['Image'])
        return self


class ListRepoBuildRecordResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        build_records: List[ListRepoBuildRecordResponseBodyBuildRecords] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.build_records = build_records

    def validate(self):
        if self.build_records:
            for k in self.build_records:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['BuildRecords'] = []
        if self.build_records is not None:
            for k in self.build_records:
                result['BuildRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.build_records = []
        if m.get('BuildRecords') is not None:
            for k in m.get('BuildRecords'):
                temp_model = ListRepoBuildRecordResponseBodyBuildRecords()
                self.build_records.append(temp_model.from_map(k))
        return self


class ListRepoBuildRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoBuildRecordResponseBody = None,
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
            temp_model = ListRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordLogRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        build_record_id: str = None,
        offset: int = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.build_record_id = build_record_id
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.offset is not None:
            result['Offset'] = self.offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        return self


class ListRepoBuildRecordLogResponseBodyBuildRecordLogs(TeaModel):
    def __init__(
        self,
        line_number: int = None,
        message: str = None,
        build_stage: str = None,
    ):
        self.line_number = line_number
        self.message = message
        self.build_stage = build_stage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.line_number is not None:
            result['LineNumber'] = self.line_number
        if self.message is not None:
            result['Message'] = self.message
        if self.build_stage is not None:
            result['BuildStage'] = self.build_stage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('BuildStage') is not None:
            self.build_stage = m.get('BuildStage')
        return self


class ListRepoBuildRecordLogResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        build_record_logs: List[ListRepoBuildRecordLogResponseBodyBuildRecordLogs] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.build_record_logs = build_record_logs

    def validate(self):
        if self.build_record_logs:
            for k in self.build_record_logs:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['BuildRecordLogs'] = []
        if self.build_record_logs is not None:
            for k in self.build_record_logs:
                result['BuildRecordLogs'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.build_record_logs = []
        if m.get('BuildRecordLogs') is not None:
            for k in m.get('BuildRecordLogs'):
                temp_model = ListRepoBuildRecordLogResponseBodyBuildRecordLogs()
                self.build_record_logs.append(temp_model.from_map(k))
        return self


class ListRepoBuildRecordLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoBuildRecordLogResponseBody = None,
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
            temp_model = ListRepoBuildRecordLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepoBuildRuleResponseBodyBuildRules(TeaModel):
    def __init__(
        self,
        dockerfile_location: str = None,
        build_rule_id: str = None,
        push_type: str = None,
        push_name: str = None,
        image_tag: str = None,
        dockerfile_name: str = None,
        platforms: List[str] = None,
        build_args: List[str] = None,
    ):
        self.dockerfile_location = dockerfile_location
        self.build_rule_id = build_rule_id
        self.push_type = push_type
        self.push_name = push_name
        self.image_tag = image_tag
        self.dockerfile_name = dockerfile_name
        self.platforms = platforms
        self.build_args = build_args

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        return self


class ListRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        build_rules: List[ListRepoBuildRuleResponseBodyBuildRules] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.build_rules = build_rules

    def validate(self):
        if self.build_rules:
            for k in self.build_rules:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['BuildRules'] = []
        if self.build_rules is not None:
            for k in self.build_rules:
                result['BuildRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.build_rules = []
        if m.get('BuildRules') is not None:
            for k in m.get('BuildRules'):
                temp_model = ListRepoBuildRuleResponseBodyBuildRules()
                self.build_rules.append(temp_model.from_map(k))
        return self


class ListRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoBuildRuleResponseBody = None,
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
            temp_model = ListRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_status: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.repo_status = repo_status
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepositoryResponseBodyRepositories(TeaModel):
    def __init__(
        self,
        summary: str = None,
        repo_build_type: str = None,
        modified_time: int = None,
        repo_id: str = None,
        create_time: int = None,
        repo_namespace_name: str = None,
        tag_immutability: bool = None,
        instance_id: str = None,
        repo_type: str = None,
        repo_status: str = None,
        repo_name: str = None,
    ):
        self.summary = summary
        self.repo_build_type = repo_build_type
        self.modified_time = modified_time
        self.repo_id = repo_id
        self.create_time = create_time
        self.repo_namespace_name = repo_namespace_name
        self.tag_immutability = tag_immutability
        self.instance_id = instance_id
        self.repo_type = repo_type
        self.repo_status = repo_status
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class ListRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        repositories: List[ListRepositoryResponseBodyRepositories] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.repositories = repositories

    def validate(self):
        if self.repositories:
            for k in self.repositories:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        return self


class ListRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepositoryResponseBody = None,
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
            temp_model = ListRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        namespace_name: str = None,
        repo_name: str = None,
        target_instance_id: str = None,
        target_region_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.namespace_name = namespace_name
        self.repo_name = repo_name
        self.target_instance_id = target_instance_id
        self.target_region_id = target_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        return self


class ListRepoSyncRuleResponseBodySyncRules(TeaModel):
    def __init__(
        self,
        sync_trigger: str = None,
        create_time: int = None,
        local_region_id: str = None,
        sync_scope: str = None,
        tag_filter: str = None,
        target_namespace_name: str = None,
        target_instance_id: str = None,
        target_repo_name: str = None,
        sync_rule_id: str = None,
        modified_time: int = None,
        sync_rule_name: str = None,
        target_region_id: str = None,
        local_instance_id: str = None,
        local_namespace_name: str = None,
        local_repo_name: str = None,
        sync_direction: str = None,
    ):
        self.sync_trigger = sync_trigger
        self.create_time = create_time
        self.local_region_id = local_region_id
        self.sync_scope = sync_scope
        self.tag_filter = tag_filter
        self.target_namespace_name = target_namespace_name
        self.target_instance_id = target_instance_id
        self.target_repo_name = target_repo_name
        self.sync_rule_id = sync_rule_id
        self.modified_time = modified_time
        self.sync_rule_name = sync_rule_name
        self.target_region_id = target_region_id
        self.local_instance_id = local_instance_id
        self.local_namespace_name = local_namespace_name
        self.local_repo_name = local_repo_name
        self.sync_direction = sync_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.local_instance_id is not None:
            result['LocalInstanceId'] = self.local_instance_id
        if self.local_namespace_name is not None:
            result['LocalNamespaceName'] = self.local_namespace_name
        if self.local_repo_name is not None:
            result['LocalRepoName'] = self.local_repo_name
        if self.sync_direction is not None:
            result['SyncDirection'] = self.sync_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('LocalInstanceId') is not None:
            self.local_instance_id = m.get('LocalInstanceId')
        if m.get('LocalNamespaceName') is not None:
            self.local_namespace_name = m.get('LocalNamespaceName')
        if m.get('LocalRepoName') is not None:
            self.local_repo_name = m.get('LocalRepoName')
        if m.get('SyncDirection') is not None:
            self.sync_direction = m.get('SyncDirection')
        return self


class ListRepoSyncRuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: int = None,
        sync_rules: List[ListRepoSyncRuleResponseBodySyncRules] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.sync_rules = sync_rules

    def validate(self):
        if self.sync_rules:
            for k in self.sync_rules:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SyncRules'] = []
        if self.sync_rules is not None:
            for k in self.sync_rules:
                result['SyncRules'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sync_rules = []
        if m.get('SyncRules') is not None:
            for k in m.get('SyncRules'):
                temp_model = ListRepoSyncRuleResponseBodySyncRules()
                self.sync_rules.append(temp_model.from_map(k))
        return self


class ListRepoSyncRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoSyncRuleResponseBody = None,
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
            temp_model = ListRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
        tag: str = None,
        page_no: int = None,
        page_size: int = None,
        sync_record_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name
        self.tag = tag
        self.page_no = page_no
        self.page_size = page_size
        self.sync_record_id = sync_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sync_record_id is not None:
            result['SyncRecordId'] = self.sync_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SyncRecordId') is not None:
            self.sync_record_id = m.get('SyncRecordId')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageFrom(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        instance_id: str = None,
        image_tag: str = None,
        repo_name: str = None,
        region_id: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.instance_id = instance_id
        self.image_tag = image_tag
        self.repo_name = repo_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageTo(TeaModel):
    def __init__(
        self,
        repo_namespace_name: str = None,
        instance_id: str = None,
        image_tag: str = None,
        repo_name: str = None,
        region_id: str = None,
    ):
        self.repo_namespace_name = repo_namespace_name
        self.instance_id = instance_id
        self.image_tag = image_tag
        self.repo_name = repo_name
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListRepoSyncTaskResponseBodySyncTasks(TeaModel):
    def __init__(
        self,
        modifed_time: int = None,
        sync_rule_id: str = None,
        sync_task_id: str = None,
        task_status: str = None,
        create_time: int = None,
        sync_batch_task_id: str = None,
        task_trigger: str = None,
        image_from: ListRepoSyncTaskResponseBodySyncTasksImageFrom = None,
        image_to: ListRepoSyncTaskResponseBodySyncTasksImageTo = None,
    ):
        self.modifed_time = modifed_time
        self.sync_rule_id = sync_rule_id
        self.sync_task_id = sync_task_id
        self.task_status = task_status
        self.create_time = create_time
        self.sync_batch_task_id = sync_batch_task_id
        self.task_trigger = task_trigger
        self.image_from = image_from
        self.image_to = image_to

    def validate(self):
        if self.image_from:
            self.image_from.validate()
        if self.image_to:
            self.image_to.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.modifed_time is not None:
            result['ModifedTime'] = self.modifed_time
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModifedTime') is not None:
            self.modifed_time = m.get('ModifedTime')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        if m.get('ImageFrom') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        return self


class ListRepoSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        sync_tasks: List[ListRepoSyncTaskResponseBodySyncTasks] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.sync_tasks = sync_tasks

    def validate(self):
        if self.sync_tasks:
            for k in self.sync_tasks:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['SyncTasks'] = []
        if self.sync_tasks is not None:
            for k in self.sync_tasks:
                result['SyncTasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.sync_tasks = []
        if m.get('SyncTasks') is not None:
            for k in m.get('SyncTasks'):
                temp_model = ListRepoSyncTaskResponseBodySyncTasks()
                self.sync_tasks.append(temp_model.from_map(k))
        return self


class ListRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoSyncTaskResponseBody = None,
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
            temp_model = ListRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.page_no = page_no
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRepoTagResponseBodyImages(TeaModel):
    def __init__(
        self,
        status: str = None,
        image_size: int = None,
        image_create: str = None,
        digest: str = None,
        image_update: str = None,
        tag: str = None,
        image_id: str = None,
    ):
        self.status = status
        self.image_size = image_size
        self.image_create = image_create
        self.digest = digest
        self.image_update = image_update
        self.tag = tag
        self.image_id = image_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_create is not None:
            result['ImageCreate'] = self.image_create
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        return self


class ListRepoTagResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: str = None,
        images: List[ListRepoTagResponseBodyImages] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.images = images

    def validate(self):
        if self.images:
            for k in self.images:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListRepoTagResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        return self


class ListRepoTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoTagResponseBody = None,
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
            temp_model = ListRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagScanResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
        scan_task_id: str = None,
        page_no: int = None,
        page_size: int = None,
        severity: str = None,
        digest: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.tag = tag
        self.scan_task_id = scan_task_id
        self.page_no = page_no
        self.page_size = page_size
        self.severity = severity
        self.digest = digest

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.digest is not None:
            result['Digest'] = self.digest
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        return self


class ListRepoTagScanResultResponseBodyVulnerabilities(TeaModel):
    def __init__(
        self,
        severity: str = None,
        added_by: str = None,
        cve_name: str = None,
        description: str = None,
        feature: str = None,
        version: str = None,
        version_format: str = None,
        cve_link: str = None,
        version_fixed: str = None,
        fix_cmd: str = None,
    ):
        self.severity = severity
        self.added_by = added_by
        self.cve_name = cve_name
        self.description = description
        self.feature = feature
        self.version = version
        self.version_format = version_format
        self.cve_link = cve_link
        self.version_fixed = version_fixed
        self.fix_cmd = fix_cmd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.added_by is not None:
            result['AddedBy'] = self.added_by
        if self.cve_name is not None:
            result['CveName'] = self.cve_name
        if self.description is not None:
            result['Description'] = self.description
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.version is not None:
            result['Version'] = self.version
        if self.version_format is not None:
            result['VersionFormat'] = self.version_format
        if self.cve_link is not None:
            result['CveLink'] = self.cve_link
        if self.version_fixed is not None:
            result['VersionFixed'] = self.version_fixed
        if self.fix_cmd is not None:
            result['FixCmd'] = self.fix_cmd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('AddedBy') is not None:
            self.added_by = m.get('AddedBy')
        if m.get('CveName') is not None:
            self.cve_name = m.get('CveName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionFormat') is not None:
            self.version_format = m.get('VersionFormat')
        if m.get('CveLink') is not None:
            self.cve_link = m.get('CveLink')
        if m.get('VersionFixed') is not None:
            self.version_fixed = m.get('VersionFixed')
        if m.get('FixCmd') is not None:
            self.fix_cmd = m.get('FixCmd')
        return self


class ListRepoTagScanResultResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        page_no: int = None,
        is_success: bool = None,
        page_size: int = None,
        total_count: int = None,
        vulnerabilities: List[ListRepoTagScanResultResponseBodyVulnerabilities] = None,
    ):
        self.request_id = request_id
        self.code = code
        self.page_no = page_no
        self.is_success = is_success
        self.page_size = page_size
        self.total_count = total_count
        self.vulnerabilities = vulnerabilities

    def validate(self):
        if self.vulnerabilities:
            for k in self.vulnerabilities:
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
            result['Code'] = self.code
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vulnerabilities'] = []
        if self.vulnerabilities is not None:
            for k in self.vulnerabilities:
                result['Vulnerabilities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.vulnerabilities = []
        if m.get('Vulnerabilities') is not None:
            for k in m.get('Vulnerabilities'):
                temp_model = ListRepoTagScanResultResponseBodyVulnerabilities()
                self.vulnerabilities.append(temp_model.from_map(k))
        return self


class ListRepoTagScanResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoTagScanResultResponseBody = None,
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
            temp_model = ListRepoTagScanResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoTriggerResponseBodyTriggers(TeaModel):
    def __init__(
        self,
        trigger_name: str = None,
        repo_event: str = None,
        trigger_id: str = None,
        trigger_url: str = None,
        trigger_type: str = None,
        trigger_tag: str = None,
    ):
        self.trigger_name = trigger_name
        self.repo_event = repo_event
        self.trigger_id = trigger_id
        self.trigger_url = trigger_url
        self.trigger_type = trigger_type
        self.trigger_tag = trigger_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.repo_event is not None:
            result['RepoEvent'] = self.repo_event
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('RepoEvent') is not None:
            self.repo_event = m.get('RepoEvent')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        return self


class ListRepoTriggerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        triggers: List[ListRepoTriggerResponseBodyTriggers] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.triggers = triggers

    def validate(self):
        if self.triggers:
            for k in self.triggers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Triggers'] = []
        if self.triggers is not None:
            for k in self.triggers:
                result['Triggers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.triggers = []
        if m.get('Triggers') is not None:
            for k in m.get('Triggers'):
                temp_model = ListRepoTriggerResponseBodyTriggers()
                self.triggers.append(temp_model.from_map(k))
        return self


class ListRepoTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoTriggerResponseBody = None,
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
            temp_model = ListRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTriggerRecordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        trigger_record_id: str = None,
    ):
        self.instance_id = instance_id
        self.trigger_record_id = trigger_record_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.trigger_record_id is not None:
            result['TriggerRecordId'] = self.trigger_record_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TriggerRecordId') is not None:
            self.trigger_record_id = m.get('TriggerRecordId')
        return self


class ListRepoTriggerRecordResponseBodyRepoTriggerRecords(TeaModel):
    def __init__(
        self,
        request_headers: str = None,
        trigger_name: str = None,
        response_headers: str = None,
        trigger_log_id: str = None,
        response_body: str = None,
        trigger_url: str = None,
        request_body: str = None,
        trigger_type: str = None,
        trigger_tag: str = None,
        status_code: str = None,
        repo_event: str = None,
        trigger_id: str = None,
        request_time: int = None,
    ):
        self.request_headers = request_headers
        self.trigger_name = trigger_name
        self.response_headers = response_headers
        self.trigger_log_id = trigger_log_id
        self.response_body = response_body
        self.trigger_url = trigger_url
        self.request_body = request_body
        self.trigger_type = trigger_type
        self.trigger_tag = trigger_tag
        self.status_code = status_code
        self.repo_event = repo_event
        self.trigger_id = trigger_id
        self.request_time = request_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_headers is not None:
            result['RequestHeaders'] = self.request_headers
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.response_headers is not None:
            result['ResponseHeaders'] = self.response_headers
        if self.trigger_log_id is not None:
            result['TriggerLogId'] = self.trigger_log_id
        if self.response_body is not None:
            result['ResponseBody'] = self.response_body
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        if self.request_body is not None:
            result['RequestBody'] = self.request_body
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.status_code is not None:
            result['StatusCode'] = self.status_code
        if self.repo_event is not None:
            result['RepoEvent'] = self.repo_event
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        if self.request_time is not None:
            result['RequestTime'] = self.request_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestHeaders') is not None:
            self.request_headers = m.get('RequestHeaders')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('ResponseHeaders') is not None:
            self.response_headers = m.get('ResponseHeaders')
        if m.get('TriggerLogId') is not None:
            self.trigger_log_id = m.get('TriggerLogId')
        if m.get('ResponseBody') is not None:
            self.response_body = m.get('ResponseBody')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        if m.get('RequestBody') is not None:
            self.request_body = m.get('RequestBody')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('StatusCode') is not None:
            self.status_code = m.get('StatusCode')
        if m.get('RepoEvent') is not None:
            self.repo_event = m.get('RepoEvent')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('RequestTime') is not None:
            self.request_time = m.get('RequestTime')
        return self


class ListRepoTriggerRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        repo_trigger_records: List[ListRepoTriggerRecordResponseBodyRepoTriggerRecords] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.repo_trigger_records = repo_trigger_records

    def validate(self):
        if self.repo_trigger_records:
            for k in self.repo_trigger_records:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['RepoTriggerRecords'] = []
        if self.repo_trigger_records is not None:
            for k in self.repo_trigger_records:
                result['RepoTriggerRecords'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.repo_trigger_records = []
        if m.get('RepoTriggerRecords') is not None:
            for k in m.get('RepoTriggerRecords'):
                temp_model = ListRepoTriggerRecordResponseBodyRepoTriggerRecords()
                self.repo_trigger_records.append(temp_model.from_map(k))
        return self


class ListRepoTriggerRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRepoTriggerRecordResponseBody = None,
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
            temp_model = ListRepoTriggerRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetLoginPasswordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
    ):
        self.instance_id = instance_id
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.password is not None:
            result['Password'] = self.password
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        return self


class ResetLoginPasswordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ResetLoginPasswordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ResetLoginPasswordResponseBody = None,
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
            temp_model = ResetLoginPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        return self


class UpdateChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateChartNamespaceResponseBody = None,
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
            temp_model = UpdateChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_type: str = None,
        summary: str = None,
        repo_namespace_name: str = None,
        repo_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_type = repo_type
        self.summary = summary
        self.repo_namespace_name = repo_namespace_name
        self.repo_name = repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        return self


class UpdateChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateChartRepositoryResponseBody = None,
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
            temp_model = UpdateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceEndpointStatusRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        endpoint_type: str = None,
        enable: bool = None,
        module_name: str = None,
    ):
        self.instance_id = instance_id
        self.endpoint_type = endpoint_type
        self.enable = enable
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        return self


class UpdateInstanceEndpointStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateInstanceEndpointStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateInstanceEndpointStatusResponseBody = None,
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
            temp_model = UpdateInstanceEndpointStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        return self


class UpdateNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateNamespaceResponseBody = None,
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
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        push_type: str = None,
        push_name: str = None,
        image_tag: str = None,
        build_rule_id: str = None,
        platforms: List[str] = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.dockerfile_location = dockerfile_location
        self.dockerfile_name = dockerfile_name
        self.push_type = push_type
        self.push_name = push_name
        self.image_tag = image_tag
        self.build_rule_id = build_rule_id
        self.platforms = platforms

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        return self


class UpdateRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        build_rule_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.build_rule_id = build_rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        return self


class UpdateRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepoBuildRuleResponseBody = None,
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
            temp_model = UpdateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        repo_type: str = None,
        summary: str = None,
        detail: str = None,
        tag_immutability: bool = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.repo_type = repo_type
        self.summary = summary
        self.detail = detail
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class UpdateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepositoryResponseBody = None,
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
            temp_model = UpdateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        code_repo_type: str = None,
        code_repo_namespace_name: str = None,
        code_repo_name: str = None,
        auto_build: str = None,
        oversea_build: str = None,
        disable_cache_build: str = None,
        code_repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.code_repo_type = code_repo_type
        self.code_repo_namespace_name = code_repo_namespace_name
        self.code_repo_name = code_repo_name
        self.auto_build = auto_build
        self.oversea_build = oversea_build
        self.disable_cache_build = disable_cache_build
        self.code_repo_id = code_repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.code_repo_id is not None:
            result['CodeRepoId'] = self.code_repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('CodeRepoId') is not None:
            self.code_repo_id = m.get('CodeRepoId')
        return self


class UpdateRepoSourceCodeRepoResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoSourceCodeRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepoSourceCodeRepoResponseBody = None,
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
            temp_model = UpdateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_name: str = None,
        trigger_url: str = None,
        trigger_type: str = None,
        trigger_tag: str = None,
        trigger_id: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.trigger_name = trigger_name
        self.trigger_url = trigger_url
        self.trigger_type = trigger_type
        self.trigger_tag = trigger_tag
        self.trigger_id = trigger_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        return self


class UpdateRepoTriggerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoTriggerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRepoTriggerResponseBody = None,
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
            temp_model = UpdateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


