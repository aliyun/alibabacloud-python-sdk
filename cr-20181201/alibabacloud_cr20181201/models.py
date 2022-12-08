# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class CancelArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
    ):
        self.build_task_id = build_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        status_code: int = None,
        body: CancelArtifactBuildTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelArtifactBuildTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.build_record_id = build_record_id
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
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
        status_code: int = None,
        body: CancelRepoBuildRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
    ):
        self.resource_group_id = resource_group_id
        self.resource_id = resource_id
        self.resource_region_id = resource_region_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
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
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ChangeResourceGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRuleRequest(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.build_rule_id = build_rule_id
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateBuildRecordByRuleResponseBody(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.build_record_id = build_record_id
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
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateBuildRecordByRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBuildRecordByRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateBuildRecordByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChainRequest(TeaModel):
    def __init__(
        self,
        chain_config: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        scope_exclude: List[str] = None,
    ):
        self.chain_config = chain_config
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.scope_exclude = scope_exclude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            self.chain_config = m.get('ChainConfig')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        return self


class CreateChainResponseBody(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.chain_id = chain_id
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
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
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
        status_code: int = None,
        body: CreateChartNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        is_success: bool = None,
        repo_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.repo_id = repo_id
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
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChartRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        endpoint_type: str = None,
        entry: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.comment = comment
        self.endpoint_type = endpoint_type
        self.entry = entry
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        status_code: int = None,
        body: CreateInstanceEndpointAclPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        enable_create_dnsrecord_in_pvzt: bool = None,
        instance_id: str = None,
        module_name: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.enable_create_dnsrecord_in_pvzt = enable_create_dnsrecord_in_pvzt
        self.instance_id = instance_id
        self.module_name = module_name
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_create_dnsrecord_in_pvzt is not None:
            result['EnableCreateDNSRecordInPvzt'] = self.enable_create_dnsrecord_in_pvzt
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableCreateDNSRecordInPvzt') is not None:
            self.enable_create_dnsrecord_in_pvzt = m.get('EnableCreateDNSRecordInPvzt')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
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
        status_code: int = None,
        body: CreateInstanceVpcEndpointLinkedVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateInstanceVpcEndpointLinkedVpcResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNamespaceRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
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
        status_code: int = None,
        body: CreateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        build_args: List[str] = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        image_tag: str = None,
        instance_id: str = None,
        platforms: List[str] = None,
        push_name: str = None,
        push_type: str = None,
        repo_id: str = None,
    ):
        self.build_args = build_args
        self.dockerfile_location = dockerfile_location
        self.dockerfile_name = dockerfile_name
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.platforms = platforms
        self.push_name = push_name
        self.push_type = push_type
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class CreateRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.build_rule_id = build_rule_id
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
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRepoBuildRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(
        self,
        auto_build: bool = None,
        code_repo_name: str = None,
        code_repo_namespace_name: str = None,
        code_repo_type: str = None,
        disable_cache_build: bool = None,
        instance_id: str = None,
        oversea_build: bool = None,
        repo_id: str = None,
    ):
        self.auto_build = auto_build
        self.code_repo_name = code_repo_name
        self.code_repo_namespace_name = code_repo_namespace_name
        self.code_repo_type = code_repo_type
        self.disable_cache_build = disable_cache_build
        self.instance_id = instance_id
        self.oversea_build = oversea_build
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
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
        status_code: int = None,
        body: CreateRepoSourceCodeRepoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        sync_rule_name: str = None,
        sync_scope: str = None,
        sync_trigger: str = None,
        tag_filter: str = None,
        target_instance_id: str = None,
        target_namespace_name: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
        target_user_id: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repo_name = repo_name
        self.sync_rule_name = sync_rule_name
        self.sync_scope = sync_scope
        self.sync_trigger = sync_trigger
        self.tag_filter = tag_filter
        self.target_instance_id = target_instance_id
        self.target_namespace_name = target_namespace_name
        self.target_region_id = target_region_id
        self.target_repo_name = target_repo_name
        self.target_user_id = target_user_id

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
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class CreateRepoSyncRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        sync_rule_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.sync_rule_id = sync_rule_id

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
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        return self


class CreateRepoSyncRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRepoSyncRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        override: bool = None,
        repo_id: str = None,
        tag: str = None,
        target_instance_id: str = None,
        target_namespace: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
        target_tag: str = None,
        target_user_id: str = None,
    ):
        self.instance_id = instance_id
        self.override = override
        self.repo_id = repo_id
        self.tag = tag
        self.target_instance_id = target_instance_id
        self.target_namespace = target_namespace
        self.target_region_id = target_region_id
        self.target_repo_name = target_repo_name
        self.target_tag = target_tag
        self.target_user_id = target_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.override is not None:
            result['Override'] = self.override
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace is not None:
            result['TargetNamespace'] = self.target_namespace
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        if self.target_tag is not None:
            result['TargetTag'] = self.target_tag
        if self.target_user_id is not None:
            result['TargetUserId'] = self.target_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespace') is not None:
            self.target_namespace = m.get('TargetNamespace')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        if m.get('TargetTag') is not None:
            self.target_tag = m.get('TargetTag')
        if m.get('TargetUserId') is not None:
            self.target_user_id = m.get('TargetUserId')
        return self


class CreateRepoSyncTaskResponseBody(TeaModel):
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


class CreateRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRepoSyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoSyncTaskByRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        sync_rule_id: str = None,
        tag: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.sync_rule_id = sync_rule_id
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
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
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
        status_code: int = None,
        body: CreateRepoSyncTaskByRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoSyncTaskByRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagRequest(TeaModel):
    def __init__(
        self,
        from_tag: str = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        to_tag: str = None,
    ):
        self.from_tag = from_tag
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.repo_name = repo_name
        self.to_tag = to_tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_tag is not None:
            result['FromTag'] = self.from_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.to_tag is not None:
            result['ToTag'] = self.to_tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromTag') is not None:
            self.from_tag = m.get('FromTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
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
        status_code: int = None,
        body: CreateRepoTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTagScanTaskRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        scan_service: str = None,
        tag: str = None,
    ):
        self.digest = digest
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.scan_service = scan_service
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
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
        status_code: int = None,
        body: CreateRepoTagScanTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoTagScanTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_name: str = None,
        trigger_tag: str = None,
        trigger_type: str = None,
        trigger_url: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.trigger_name = trigger_name
        self.trigger_tag = trigger_tag
        self.trigger_type = trigger_type
        self.trigger_url = trigger_url

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
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
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
        status_code: int = None,
        body: CreateRepoTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRepositoryRequest(TeaModel):
    def __init__(
        self,
        detail: str = None,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_type: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        self.detail = detail
        self.instance_id = instance_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_type = repo_type
        self.summary = summary
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
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
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
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
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class CreateRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        repo_id: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.repo_id = repo_id
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
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChainRequest(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        instance_id: str = None,
    ):
        self.chain_id = chain_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class DeleteChainResponseBody(TeaModel):
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


class DeleteChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteChainResponseBody()
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
        status_code: int = None,
        body: DeleteChartNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartReleaseRequest(TeaModel):
    def __init__(
        self,
        chart: str = None,
        instance_id: str = None,
        release: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.chart = chart
        self.instance_id = instance_id
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
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.release is not None:
            result['Release'] = self.release
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        status_code: int = None,
        body: DeleteChartReleaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
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
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
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
        status_code: int = None,
        body: DeleteChartRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteEventCenterRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        self.instance_id = instance_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class DeleteEventCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        request_id: str = None,
    ):
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteEventCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteEventCenterRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteEventCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceEndpointAclPolicyRequest(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        entry: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.endpoint_type = endpoint_type
        self.entry = entry
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.entry is not None:
            result['Entry'] = self.entry
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('Entry') is not None:
            self.entry = m.get('Entry')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        status_code: int = None,
        body: DeleteInstanceEndpointAclPolicyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteInstanceEndpointAclPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteInstanceVpcEndpointLinkedVpcRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        module_name: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.instance_id = instance_id
        self.module_name = module_name
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

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
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
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
        status_code: int = None,
        body: DeleteInstanceVpcEndpointLinkedVpcResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: DeleteNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.build_rule_id = build_rule_id
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
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
        status_code: int = None,
        body: DeleteRepoBuildRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteRepoBuildRuleResponseBody()
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
        status_code: int = None,
        body: DeleteRepoSyncRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: DeleteRepoTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        status_code: int = None,
        body: DeleteRepoTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
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
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
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
        status_code: int = None,
        body: DeleteRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
    ):
        self.build_task_id = build_task_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetArtifactBuildTaskResponseBodySourceArtifact(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        repo_id: str = None,
        version: str = None,
    ):
        self.artifact_type = artifact_type
        self.repo_id = repo_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetArtifactBuildTaskResponseBodyTargetArtifact(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        repo_id: str = None,
        version: str = None,
    ):
        self.artifact_type = artifact_type
        self.repo_id = repo_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetArtifactBuildTaskResponseBody(TeaModel):
    def __init__(
        self,
        artifact_build_type: str = None,
        build_task_id: str = None,
        code: str = None,
        end_time: int = None,
        instructions: List[str] = None,
        is_success: bool = None,
        request_id: str = None,
        source_artifact: GetArtifactBuildTaskResponseBodySourceArtifact = None,
        start_time: int = None,
        target_artifact: GetArtifactBuildTaskResponseBodyTargetArtifact = None,
        task_status: str = None,
    ):
        self.artifact_build_type = artifact_build_type
        self.build_task_id = build_task_id
        self.code = code
        self.end_time = end_time
        self.instructions = instructions
        self.is_success = is_success
        self.request_id = request_id
        self.source_artifact = source_artifact
        self.start_time = start_time
        self.target_artifact = target_artifact
        self.task_status = task_status

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
        if self.artifact_build_type is not None:
            result['ArtifactBuildType'] = self.artifact_build_type
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instructions is not None:
            result['Instructions'] = self.instructions
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_artifact is not None:
            result['SourceArtifact'] = self.source_artifact.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.target_artifact is not None:
            result['TargetArtifact'] = self.target_artifact.to_map()
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildType') is not None:
            self.artifact_build_type = m.get('ArtifactBuildType')
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Instructions') is not None:
            self.instructions = m.get('Instructions')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodySourceArtifact()
            self.source_artifact = temp_model.from_map(m['SourceArtifact'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TargetArtifact') is not None:
            temp_model = GetArtifactBuildTaskResponseBodyTargetArtifact()
            self.target_artifact = temp_model.from_map(m['TargetArtifact'])
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetArtifactBuildTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactBuildTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        authorization_token: str = None,
        code: str = None,
        expire_time: int = None,
        is_success: bool = None,
        request_id: str = None,
        temp_username: str = None,
    ):
        self.authorization_token = authorization_token
        self.code = code
        self.expire_time = expire_time
        self.is_success = is_success
        self.request_id = request_id
        self.temp_username = temp_username

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorization_token is not None:
            result['AuthorizationToken'] = self.authorization_token
        if self.code is not None:
            result['Code'] = self.code
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.temp_username is not None:
            result['TempUsername'] = self.temp_username
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorizationToken') is not None:
            self.authorization_token = m.get('AuthorizationToken')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TempUsername') is not None:
            self.temp_username = m.get('TempUsername')
        return self


class GetAuthorizationTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAuthorizationTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetAuthorizationTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChainRequest(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        instance_id: str = None,
    ):
        self.chain_id = chain_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy(TeaModel):
    def __init__(
        self,
        action: str = None,
        baseline_list: str = None,
        issue_count: str = None,
        issue_level: str = None,
        issue_list: str = None,
        logic: str = None,
        malicious_list: str = None,
    ):
        self.action = action
        self.baseline_list = baseline_list
        self.issue_count = issue_count
        self.issue_level = issue_level
        self.issue_list = issue_list
        self.logic = logic
        self.malicious_list = malicious_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['Action'] = self.action
        if self.baseline_list is not None:
            result['BaselineList'] = self.baseline_list
        if self.issue_count is not None:
            result['IssueCount'] = self.issue_count
        if self.issue_level is not None:
            result['IssueLevel'] = self.issue_level
        if self.issue_list is not None:
            result['IssueList'] = self.issue_list
        if self.logic is not None:
            result['Logic'] = self.logic
        if self.malicious_list is not None:
            result['MaliciousList'] = self.malicious_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')
        if m.get('BaselineList') is not None:
            self.baseline_list = m.get('BaselineList')
        if m.get('IssueCount') is not None:
            self.issue_count = m.get('IssueCount')
        if m.get('IssueLevel') is not None:
            self.issue_level = m.get('IssueLevel')
        if m.get('IssueList') is not None:
            self.issue_list = m.get('IssueList')
        if m.get('Logic') is not None:
            self.logic = m.get('Logic')
        if m.get('MaliciousList') is not None:
            self.malicious_list = m.get('MaliciousList')
        return self


class GetChainResponseBodyChainConfigNodesNodeConfig(TeaModel):
    def __init__(
        self,
        deny_policy: GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy = None,
        retry: int = None,
        scan_engine: str = None,
        timeout: int = None,
    ):
        self.deny_policy = deny_policy
        self.retry = retry
        self.scan_engine = scan_engine
        self.timeout = timeout

    def validate(self):
        if self.deny_policy:
            self.deny_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.deny_policy is not None:
            result['DenyPolicy'] = self.deny_policy.to_map()
        if self.retry is not None:
            result['Retry'] = self.retry
        if self.scan_engine is not None:
            result['ScanEngine'] = self.scan_engine
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DenyPolicy') is not None:
            temp_model = GetChainResponseBodyChainConfigNodesNodeConfigDenyPolicy()
            self.deny_policy = temp_model.from_map(m['DenyPolicy'])
        if m.get('Retry') is not None:
            self.retry = m.get('Retry')
        if m.get('ScanEngine') is not None:
            self.scan_engine = m.get('ScanEngine')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        return self


class GetChainResponseBodyChainConfigNodes(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        node_config: GetChainResponseBodyChainConfigNodesNodeConfig = None,
        node_name: str = None,
    ):
        self.enable = enable
        self.node_config = node_config
        self.node_name = node_name

    def validate(self):
        if self.node_config:
            self.node_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.node_config is not None:
            result['NodeConfig'] = self.node_config.to_map()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('NodeConfig') is not None:
            temp_model = GetChainResponseBodyChainConfigNodesNodeConfig()
            self.node_config = temp_model.from_map(m['NodeConfig'])
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRoutersFrom(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRoutersTo(TeaModel):
    def __init__(
        self,
        node_name: str = None,
    ):
        self.node_name = node_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.node_name is not None:
            result['NodeName'] = self.node_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')
        return self


class GetChainResponseBodyChainConfigRouters(TeaModel):
    def __init__(
        self,
        from_: GetChainResponseBodyChainConfigRoutersFrom = None,
        to: GetChainResponseBodyChainConfigRoutersTo = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        if self.from_:
            self.from_.validate()
        if self.to:
            self.to.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['From'] = self.from_.to_map()
        if self.to is not None:
            result['To'] = self.to.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            temp_model = GetChainResponseBodyChainConfigRoutersFrom()
            self.from_ = temp_model.from_map(m['From'])
        if m.get('To') is not None:
            temp_model = GetChainResponseBodyChainConfigRoutersTo()
            self.to = temp_model.from_map(m['To'])
        return self


class GetChainResponseBodyChainConfig(TeaModel):
    def __init__(
        self,
        chain_config_id: str = None,
        is_active: bool = None,
        nodes: List[GetChainResponseBodyChainConfigNodes] = None,
        routers: List[GetChainResponseBodyChainConfigRouters] = None,
        version: str = None,
    ):
        self.chain_config_id = chain_config_id
        self.is_active = is_active
        self.nodes = nodes
        self.routers = routers
        self.version = version

    def validate(self):
        if self.nodes:
            for k in self.nodes:
                if k:
                    k.validate()
        if self.routers:
            for k in self.routers:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config_id is not None:
            result['ChainConfigId'] = self.chain_config_id
        if self.is_active is not None:
            result['IsActive'] = self.is_active
        result['Nodes'] = []
        if self.nodes is not None:
            for k in self.nodes:
                result['Nodes'].append(k.to_map() if k else None)
        result['Routers'] = []
        if self.routers is not None:
            for k in self.routers:
                result['Routers'].append(k.to_map() if k else None)
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfigId') is not None:
            self.chain_config_id = m.get('ChainConfigId')
        if m.get('IsActive') is not None:
            self.is_active = m.get('IsActive')
        self.nodes = []
        if m.get('Nodes') is not None:
            for k in m.get('Nodes'):
                temp_model = GetChainResponseBodyChainConfigNodes()
                self.nodes.append(temp_model.from_map(k))
        self.routers = []
        if m.get('Routers') is not None:
            for k in m.get('Routers'):
                temp_model = GetChainResponseBodyChainConfigRouters()
                self.routers.append(temp_model.from_map(k))
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetChainResponseBody(TeaModel):
    def __init__(
        self,
        chain_config: GetChainResponseBodyChainConfig = None,
        chain_id: str = None,
        code: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        name: str = None,
        request_id: str = None,
        scope_exclude: List[str] = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        self.chain_config = chain_config
        self.chain_id = chain_id
        self.code = code
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.is_success = is_success
        self.modified_time = modified_time
        self.name = name
        self.request_id = request_id
        self.scope_exclude = scope_exclude
        self.scope_id = scope_id
        self.scope_type = scope_type

    def validate(self):
        if self.chain_config:
            self.chain_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config.to_map()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            temp_model = GetChainResponseBodyChainConfig()
            self.chain_config = temp_model.from_map(m['ChainConfig'])
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetChainResponseBody()
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
        auto_create_repo: bool = None,
        code: str = None,
        default_repo_type: str = None,
        instance_id: str = None,
        is_success: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.code = code
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.is_success = is_success
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
        self.request_id = request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.code is not None:
            result['Code'] = self.code
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChartNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
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
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        summary: str = None,
    ):
        self.code = code
        self.create_time = create_time
        self.instance_id = instance_id
        self.is_success = is_success
        self.modified_time = modified_time
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class GetChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetChartRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        is_success: bool = None,
        modified_time: int = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        self.code = code
        self.create_time = create_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_specification = instance_specification
        self.instance_status = instance_status
        self.is_success = is_success
        self.modified_time = modified_time
        self.request_id = request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.count = count
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
        if self.count is not None:
            result['Count'] = self.count
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceCountResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceEndpointRequest(TeaModel):
    def __init__(
        self,
        endpoint_type: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.endpoint_type = endpoint_type
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
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


class GetInstanceEndpointResponseBodyDomains(TeaModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
    ):
        self.domain = domain
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetInstanceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        acl_enable: bool = None,
        acl_entries: List[GetInstanceEndpointResponseBodyAclEntries] = None,
        code: str = None,
        domains: List[GetInstanceEndpointResponseBodyDomains] = None,
        enable: bool = None,
        is_success: bool = None,
        request_id: str = None,
        status: str = None,
    ):
        self.acl_enable = acl_enable
        self.acl_entries = acl_entries
        self.code = code
        self.domains = domains
        self.enable = enable
        self.is_success = is_success
        self.request_id = request_id
        self.status = status

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = GetInstanceEndpointResponseBodyAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = GetInstanceEndpointResponseBodyDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetInstanceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        chart_namespace_quota: str = None,
        chart_namespace_usage: str = None,
        chart_repo_quota: str = None,
        chart_repo_usage: str = None,
        code: str = None,
        is_success: bool = None,
        namespace_quota: str = None,
        namespace_usage: str = None,
        repo_quota: str = None,
        repo_usage: str = None,
        request_id: str = None,
    ):
        self.chart_namespace_quota = chart_namespace_quota
        self.chart_namespace_usage = chart_namespace_usage
        self.chart_repo_quota = chart_repo_quota
        self.chart_repo_usage = chart_repo_usage
        self.code = code
        self.is_success = is_success
        self.namespace_quota = namespace_quota
        self.namespace_usage = namespace_usage
        self.repo_quota = repo_quota
        self.repo_usage = repo_usage
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart_namespace_quota is not None:
            result['ChartNamespaceQuota'] = self.chart_namespace_quota
        if self.chart_namespace_usage is not None:
            result['ChartNamespaceUsage'] = self.chart_namespace_usage
        if self.chart_repo_quota is not None:
            result['ChartRepoQuota'] = self.chart_repo_quota
        if self.chart_repo_usage is not None:
            result['ChartRepoUsage'] = self.chart_repo_usage
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_quota is not None:
            result['NamespaceQuota'] = self.namespace_quota
        if self.namespace_usage is not None:
            result['NamespaceUsage'] = self.namespace_usage
        if self.repo_quota is not None:
            result['RepoQuota'] = self.repo_quota
        if self.repo_usage is not None:
            result['RepoUsage'] = self.repo_usage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChartNamespaceQuota') is not None:
            self.chart_namespace_quota = m.get('ChartNamespaceQuota')
        if m.get('ChartNamespaceUsage') is not None:
            self.chart_namespace_usage = m.get('ChartNamespaceUsage')
        if m.get('ChartRepoQuota') is not None:
            self.chart_repo_quota = m.get('ChartRepoQuota')
        if m.get('ChartRepoUsage') is not None:
            self.chart_repo_usage = m.get('ChartRepoUsage')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceQuota') is not None:
            self.namespace_quota = m.get('NamespaceQuota')
        if m.get('NamespaceUsage') is not None:
            self.namespace_usage = m.get('NamespaceUsage')
        if m.get('RepoQuota') is not None:
            self.repo_quota = m.get('RepoQuota')
        if m.get('RepoUsage') is not None:
            self.repo_usage = m.get('RepoUsage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceUsageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceUsageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        default_access: bool = None,
        ip: str = None,
        status: str = None,
        vpc_id: str = None,
        vswitch_id: str = None,
    ):
        self.default_access = default_access
        self.ip = ip
        self.status = status
        self.vpc_id = vpc_id
        self.vswitch_id = vswitch_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default_access is not None:
            result['DefaultAccess'] = self.default_access
        if self.ip is not None:
            result['Ip'] = self.ip
        if self.status is not None:
            result['Status'] = self.status
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultAccess') is not None:
            self.default_access = m.get('DefaultAccess')
        if m.get('Ip') is not None:
            self.ip = m.get('Ip')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class GetInstanceVpcEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        domains: List[str] = None,
        enable: bool = None,
        is_success: bool = None,
        linked_vpcs: List[GetInstanceVpcEndpointResponseBodyLinkedVpcs] = None,
        request_id: str = None,
    ):
        self.code = code
        self.domains = domains
        self.enable = enable
        self.is_success = is_success
        self.linked_vpcs = linked_vpcs
        self.request_id = request_id

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
        if self.domains is not None:
            result['Domains'] = self.domains
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Domains') is not None:
            self.domains = m.get('Domains')
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = GetInstanceVpcEndpointResponseBodyLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceVpcEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetInstanceVpcEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetInstanceVpcEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_id = namespace_id
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
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class GetNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        code: str = None,
        default_repo_type: str = None,
        instance_id: str = None,
        is_success: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.code = code
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.is_success = is_success
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
        self.request_id = request_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.code is not None:
            result['Code'] = self.code
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class GetNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
    ):
        self.build_record_id = build_record_id
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetRepoBuildRecordResponseBodyImage(TeaModel):
    def __init__(
        self,
        image_tag: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoBuildRecordResponseBody(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        code: str = None,
        end_time: int = None,
        image: GetRepoBuildRecordResponseBodyImage = None,
        is_success: bool = None,
        request_id: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.build_record_id = build_record_id
        self.code = code
        self.end_time = end_time
        self.image = image
        self.is_success = is_success
        self.request_id = request_id
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Image') is not None:
            temp_model = GetRepoBuildRecordResponseBodyImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoBuildRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoBuildRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoBuildRecordStatusRequest(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        self.build_record_id = build_record_id
        self.instance_id = instance_id
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class GetRepoBuildRecordStatusResponseBody(TeaModel):
    def __init__(
        self,
        build_status: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.build_status = build_status
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
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoBuildRecordStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoBuildRecordStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoBuildRecordStatusResponseBody()
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
        auto_build: str = None,
        code: str = None,
        code_repo_domain: str = None,
        code_repo_name: str = None,
        code_repo_namespace_name: str = None,
        code_repo_type: str = None,
        disable_cache_build: str = None,
        is_success: bool = None,
        oversea_build: str = None,
        repo_id: str = None,
        request_id: str = None,
    ):
        self.auto_build = auto_build
        self.code = code
        self.code_repo_domain = code_repo_domain
        self.code_repo_name = code_repo_name
        self.code_repo_namespace_name = code_repo_namespace_name
        self.code_repo_type = code_repo_type
        self.disable_cache_build = disable_cache_build
        self.is_success = is_success
        self.oversea_build = oversea_build
        self.repo_id = repo_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code is not None:
            result['Code'] = self.code
        if self.code_repo_domain is not None:
            result['CodeRepoDomain'] = self.code_repo_domain
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CodeRepoDomain') is not None:
            self.code_repo_domain = m.get('CodeRepoDomain')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoSourceCodeRepoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoSourceCodeRepoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoSyncTaskResponseBodyImageTo(TeaModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepoSyncTaskResponseBodyLayerTasks(TeaModel):
    def __init__(
        self,
        artifact_digest: str = None,
        digest: str = None,
        size: int = None,
        sync_layer_task_id: str = None,
        synced_size: int = None,
        task_status: str = None,
    ):
        self.artifact_digest = artifact_digest
        self.digest = digest
        self.size = size
        self.sync_layer_task_id = sync_layer_task_id
        self.synced_size = synced_size
        self.task_status = task_status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_digest is not None:
            result['ArtifactDigest'] = self.artifact_digest
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.size is not None:
            result['Size'] = self.size
        if self.sync_layer_task_id is not None:
            result['SyncLayerTaskId'] = self.sync_layer_task_id
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactDigest') is not None:
            self.artifact_digest = m.get('ArtifactDigest')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('SyncLayerTaskId') is not None:
            self.sync_layer_task_id = m.get('SyncLayerTaskId')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        return self


class GetRepoSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        cross_user: bool = None,
        image_from: GetRepoSyncTaskResponseBodyImageFrom = None,
        image_to: GetRepoSyncTaskResponseBodyImageTo = None,
        is_success: bool = None,
        layer_tasks: List[GetRepoSyncTaskResponseBodyLayerTasks] = None,
        progress: int = None,
        request_id: str = None,
        sync_batch_task_id: str = None,
        sync_rule_id: str = None,
        sync_task_id: str = None,
        sync_trans_accelerate: bool = None,
        synced_size: int = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        self.code = code
        self.cross_user = cross_user
        self.image_from = image_from
        self.image_to = image_to
        self.is_success = is_success
        self.layer_tasks = layer_tasks
        self.progress = progress
        self.request_id = request_id
        self.sync_batch_task_id = sync_batch_task_id
        self.sync_rule_id = sync_rule_id
        self.sync_task_id = sync_task_id
        self.sync_trans_accelerate = sync_trans_accelerate
        self.synced_size = synced_size
        self.task_status = task_status
        self.task_trigger = task_trigger

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
        if self.code is not None:
            result['Code'] = self.code
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['LayerTasks'] = []
        if self.layer_tasks is not None:
            for k in self.layer_tasks:
                result['LayerTasks'].append(k.to_map() if k else None)
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate
        if self.synced_size is not None:
            result['SyncedSize'] = self.synced_size
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('ImageFrom') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = GetRepoSyncTaskResponseBodyImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.layer_tasks = []
        if m.get('LayerTasks') is not None:
            for k in m.get('LayerTasks'):
                temp_model = GetRepoSyncTaskResponseBodyLayerTasks()
                self.layer_tasks.append(temp_model.from_map(k))
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')
        if m.get('SyncedSize') is not None:
            self.synced_size = m.get('SyncedSize')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        return self


class GetRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoSyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagRequest(TeaModel):
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


class GetRepoTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        digest: str = None,
        image_create: int = None,
        image_id: str = None,
        image_size: int = None,
        image_update: int = None,
        is_success: bool = None,
        request_id: str = None,
        status: str = None,
        tag: str = None,
    ):
        self.code = code
        self.digest = digest
        self.image_create = image_create
        self.image_id = image_id
        self.image_size = image_size
        self.image_update = image_update
        self.is_success = is_success
        self.request_id = request_id
        self.status = status
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.image_create is not None:
            result['ImageCreate'] = self.image_create
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagLayersRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        tag: str = None,
    ):
        self.digest = digest
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
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagLayersResponseBodyLayers(TeaModel):
    def __init__(
        self,
        blob_digest: str = None,
        blob_size: int = None,
        layer_cmd: str = None,
        layer_index: int = None,
        layer_instruction: str = None,
    ):
        self.blob_digest = blob_digest
        self.blob_size = blob_size
        self.layer_cmd = layer_cmd
        self.layer_index = layer_index
        self.layer_instruction = layer_instruction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.blob_digest is not None:
            result['BlobDigest'] = self.blob_digest
        if self.blob_size is not None:
            result['BlobSize'] = self.blob_size
        if self.layer_cmd is not None:
            result['LayerCMD'] = self.layer_cmd
        if self.layer_index is not None:
            result['LayerIndex'] = self.layer_index
        if self.layer_instruction is not None:
            result['LayerInstruction'] = self.layer_instruction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BlobDigest') is not None:
            self.blob_digest = m.get('BlobDigest')
        if m.get('BlobSize') is not None:
            self.blob_size = m.get('BlobSize')
        if m.get('LayerCMD') is not None:
            self.layer_cmd = m.get('LayerCMD')
        if m.get('LayerIndex') is not None:
            self.layer_index = m.get('LayerIndex')
        if m.get('LayerInstruction') is not None:
            self.layer_instruction = m.get('LayerInstruction')
        return self


class GetRepoTagLayersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        layers: List[GetRepoTagLayersResponseBodyLayers] = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.layers = layers
        self.request_id = request_id

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
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagLayersResponseBodyLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoTagLayersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoTagLayersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoTagLayersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagManifestRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        schema_version: int = None,
        tag: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.schema_version = schema_version
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
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
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


class GetRepoTagManifestResponseBodyManifestSignatures(TeaModel):
    def __init__(
        self,
        header: Dict[str, Any] = None,
        protected: str = None,
        signature: str = None,
    ):
        self.header = header
        self.protected = protected
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.header is not None:
            result['Header'] = self.header
        if self.protected is not None:
            result['Protected'] = self.protected
        if self.signature is not None:
            result['Signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            self.header = m.get('Header')
        if m.get('Protected') is not None:
            self.protected = m.get('Protected')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        return self


class GetRepoTagManifestResponseBodyManifest(TeaModel):
    def __init__(
        self,
        architecture: str = None,
        config: GetRepoTagManifestResponseBodyManifestConfig = None,
        fs_layers: List[GetRepoTagManifestResponseBodyManifestFsLayers] = None,
        history: List[GetRepoTagManifestResponseBodyManifestHistory] = None,
        layers: List[GetRepoTagManifestResponseBodyManifestLayers] = None,
        media_type: str = None,
        name: str = None,
        schema_version: int = None,
        signatures: List[GetRepoTagManifestResponseBodyManifestSignatures] = None,
        tag: str = None,
    ):
        self.architecture = architecture
        self.config = config
        self.fs_layers = fs_layers
        self.history = history
        self.layers = layers
        self.media_type = media_type
        self.name = name
        self.schema_version = schema_version
        self.signatures = signatures
        self.tag = tag

    def validate(self):
        if self.config:
            self.config.validate()
        if self.fs_layers:
            for k in self.fs_layers:
                if k:
                    k.validate()
        if self.history:
            for k in self.history:
                if k:
                    k.validate()
        if self.layers:
            for k in self.layers:
                if k:
                    k.validate()
        if self.signatures:
            for k in self.signatures:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.architecture is not None:
            result['Architecture'] = self.architecture
        if self.config is not None:
            result['Config'] = self.config.to_map()
        result['FsLayers'] = []
        if self.fs_layers is not None:
            for k in self.fs_layers:
                result['FsLayers'].append(k.to_map() if k else None)
        result['History'] = []
        if self.history is not None:
            for k in self.history:
                result['History'].append(k.to_map() if k else None)
        result['Layers'] = []
        if self.layers is not None:
            for k in self.layers:
                result['Layers'].append(k.to_map() if k else None)
        if self.media_type is not None:
            result['MediaType'] = self.media_type
        if self.name is not None:
            result['Name'] = self.name
        if self.schema_version is not None:
            result['SchemaVersion'] = self.schema_version
        result['Signatures'] = []
        if self.signatures is not None:
            for k in self.signatures:
                result['Signatures'].append(k.to_map() if k else None)
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')
        if m.get('Config') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifestConfig()
            self.config = temp_model.from_map(m['Config'])
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
        self.layers = []
        if m.get('Layers') is not None:
            for k in m.get('Layers'):
                temp_model = GetRepoTagManifestResponseBodyManifestLayers()
                self.layers.append(temp_model.from_map(k))
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SchemaVersion') is not None:
            self.schema_version = m.get('SchemaVersion')
        self.signatures = []
        if m.get('Signatures') is not None:
            for k in m.get('Signatures'):
                temp_model = GetRepoTagManifestResponseBodyManifestSignatures()
                self.signatures.append(temp_model.from_map(k))
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagManifestResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        manifest: GetRepoTagManifestResponseBodyManifest = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.manifest = manifest
        self.request_id = request_id

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
        if self.manifest is not None:
            result['Manifest'] = self.manifest.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Manifest') is not None:
            temp_model = GetRepoTagManifestResponseBodyManifest()
            self.manifest = temp_model.from_map(m['Manifest'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetRepoTagManifestResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoTagManifestResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoTagManifestResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanStatusRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        scan_task_id: str = None,
        tag: str = None,
    ):
        self.digest = digest
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.scan_task_id = scan_task_id
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagScanStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        scan_service: str = None,
        status: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.scan_service = scan_service
        self.status = status

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
        if self.scan_service is not None:
            result['ScanService'] = self.scan_service
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScanService') is not None:
            self.scan_service = m.get('ScanService')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetRepoTagScanStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoTagScanStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoTagScanStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepoTagScanSummaryRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        scan_task_id: str = None,
        tag: str = None,
    ):
        self.digest = digest
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.scan_task_id = scan_task_id
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class GetRepoTagScanSummaryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        high_severity: int = None,
        is_success: bool = None,
        low_severity: int = None,
        medium_severity: int = None,
        request_id: str = None,
        total_severity: int = None,
        unknown_severity: int = None,
    ):
        self.code = code
        self.high_severity = high_severity
        self.is_success = is_success
        self.low_severity = low_severity
        self.medium_severity = medium_severity
        self.request_id = request_id
        self.total_severity = total_severity
        self.unknown_severity = unknown_severity

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.high_severity is not None:
            result['HighSeverity'] = self.high_severity
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.low_severity is not None:
            result['LowSeverity'] = self.low_severity
        if self.medium_severity is not None:
            result['MediumSeverity'] = self.medium_severity
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_severity is not None:
            result['TotalSeverity'] = self.total_severity
        if self.unknown_severity is not None:
            result['UnknownSeverity'] = self.unknown_severity
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HighSeverity') is not None:
            self.high_severity = m.get('HighSeverity')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('LowSeverity') is not None:
            self.low_severity = m.get('LowSeverity')
        if m.get('MediumSeverity') is not None:
            self.medium_severity = m.get('MediumSeverity')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalSeverity') is not None:
            self.total_severity = m.get('TotalSeverity')
        if m.get('UnknownSeverity') is not None:
            self.unknown_severity = m.get('UnknownSeverity')
        return self


class GetRepoTagScanSummaryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepoTagScanSummaryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepoTagScanSummaryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
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
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class GetRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        detail: str = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        repo_build_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        self.code = code
        self.create_time = create_time
        self.detail = detail
        self.instance_id = instance_id
        self.is_success = is_success
        self.modified_time = modified_time
        self.repo_build_type = repo_build_type
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.summary = summary
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class GetRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactBuildTaskLogRequest(TeaModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
        page: int = None,
        page_size: int = None,
    ):
        self.build_task_id = build_task_id
        self.instance_id = instance_id
        self.page = page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_task_id is not None:
            result['BuildTaskId'] = self.build_task_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page is not None:
            result['Page'] = self.page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildTaskId') is not None:
            self.build_task_id = m.get('BuildTaskId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Page') is not None:
            self.page = m.get('Page')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactBuildTaskLogResponseBodyBuildTaskLogs(TeaModel):
    def __init__(
        self,
        line_number: int = None,
        message: str = None,
    ):
        self.line_number = line_number
        self.message = message

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListArtifactBuildTaskLogResponseBody(TeaModel):
    def __init__(
        self,
        build_task_logs: List[ListArtifactBuildTaskLogResponseBodyBuildTaskLogs] = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.build_task_logs = build_task_logs
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.total_count = total_count

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
        result['BuildTaskLogs'] = []
        if self.build_task_logs is not None:
            for k in self.build_task_logs:
                result['BuildTaskLogs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_task_logs = []
        if m.get('BuildTaskLogs') is not None:
            for k in m.get('BuildTaskLogs'):
                temp_model = ListArtifactBuildTaskLogResponseBodyBuildTaskLogs()
                self.build_task_logs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactBuildTaskLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactBuildTaskLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListArtifactBuildTaskLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChainRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChainResponseBodyChains(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        modified_time: int = None,
        name: str = None,
        scope_exclude: List[str] = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        self.chain_id = chain_id
        self.create_time = create_time
        self.description = description
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.name = name
        self.scope_exclude = scope_exclude
        self.scope_id = scope_id
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class ListChainResponseBody(TeaModel):
    def __init__(
        self,
        chains: List[ListChainResponseBodyChains] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.chains = chains
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.chains:
            for k in self.chains:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Chains'] = []
        if self.chains is not None:
            for k in self.chains:
                result['Chains'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chains = []
        if m.get('Chains') is not None:
            for k in m.get('Chains'):
                temp_model = ListChainResponseBodyChains()
                self.chains.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChainInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChainInstanceResponseBodyChainInstancesChain(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        chain_name: str = None,
        version: int = None,
    ):
        self.chain_id = chain_id
        self.chain_name = chain_name
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.chain_name is not None:
            result['ChainName'] = self.chain_name
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('ChainName') is not None:
            self.chain_name = m.get('ChainName')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListChainInstanceResponseBodyChainInstances(TeaModel):
    def __init__(
        self,
        chain: ListChainInstanceResponseBodyChainInstancesChain = None,
        chain_instance_id: str = None,
        end_time: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        result: str = None,
        start_time: int = None,
        status: str = None,
    ):
        self.chain = chain
        self.chain_instance_id = chain_instance_id
        self.end_time = end_time
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.result = result
        self.start_time = start_time
        self.status = status

    def validate(self):
        if self.chain:
            self.chain.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain is not None:
            result['Chain'] = self.chain.to_map()
        if self.chain_instance_id is not None:
            result['ChainInstanceId'] = self.chain_instance_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.result is not None:
            result['Result'] = self.result
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chain') is not None:
            temp_model = ListChainInstanceResponseBodyChainInstancesChain()
            self.chain = temp_model.from_map(m['Chain'])
        if m.get('ChainInstanceId') is not None:
            self.chain_instance_id = m.get('ChainInstanceId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChainInstanceResponseBody(TeaModel):
    def __init__(
        self,
        chain_instances: List[ListChainInstanceResponseBodyChainInstances] = None,
        code: str = None,
        instance_id: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.chain_instances = chain_instances
        self.code = code
        self.instance_id = instance_id
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.chain_instances:
            for k in self.chain_instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ChainInstances'] = []
        if self.chain_instances is not None:
            for k in self.chain_instances:
                result['ChainInstances'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chain_instances = []
        if m.get('ChainInstances') is not None:
            for k in m.get('ChainInstances'):
                temp_model = ListChainInstanceResponseBodyChainInstances()
                self.chain_instances.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChainInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChainInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChainInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
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
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListChartNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        resource_group_id: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListChartNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        namespaces: List[ListChartNamespaceResponseBodyNamespaces] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.namespaces = namespaces
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListChartNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChartNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartReleaseRequest(TeaModel):
    def __init__(
        self,
        chart: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.chart = chart
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListChartReleaseResponseBodyChartReleases(TeaModel):
    def __init__(
        self,
        chart: str = None,
        instance_id: str = None,
        modified_time: int = None,
        release: str = None,
        repo_id: str = None,
        size: str = None,
        status: str = None,
    ):
        self.chart = chart
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.release = release
        self.repo_id = repo_id
        self.size = size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chart is not None:
            result['Chart'] = self.chart
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.release is not None:
            result['Release'] = self.release
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.size is not None:
            result['Size'] = self.size
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chart') is not None:
            self.chart = m.get('Chart')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Release') is not None:
            self.release = m.get('Release')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListChartReleaseResponseBody(TeaModel):
    def __init__(
        self,
        chart_releases: List[ListChartReleaseResponseBodyChartReleases] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.chart_releases = chart_releases
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['ChartReleases'] = []
        if self.chart_releases is not None:
            for k in self.chart_releases:
                result['ChartReleases'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.chart_releases = []
        if m.get('ChartReleases') is not None:
            for k in m.get('ChartReleases'):
                temp_model = ListChartReleaseResponseBodyChartReleases()
                self.chart_releases.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartReleaseResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChartReleaseResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChartReleaseResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListChartRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status

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
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        return self


class ListChartRepositoryResponseBodyRepositories(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        modified_time: int = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        resource_group_id: str = None,
        summary: str = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.resource_group_id = resource_group_id
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListChartRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        repositories: List[ListChartRepositoryResponseBodyRepositories] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.repositories = repositories
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListChartRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListChartRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListChartRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventCenterRecordRequest(TeaModel):
    def __init__(
        self,
        event_type: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        rule_id: str = None,
    ):
        self.event_type = event_type
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class ListEventCenterRecordResponseBodyRecords(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        event_channel: str = None,
        event_notify_id: str = None,
        event_notify_method: str = None,
        event_type: str = None,
        instance_id: str = None,
        namespace: str = None,
        record_id: str = None,
        repo_name: str = None,
        rule_id: str = None,
        rule_name: str = None,
        tag: str = None,
        update_time: int = None,
    ):
        self.create_time = create_time
        self.event_channel = event_channel
        self.event_notify_id = event_notify_id
        self.event_notify_method = event_notify_method
        self.event_type = event_type
        self.instance_id = instance_id
        self.namespace = namespace
        self.record_id = record_id
        self.repo_name = repo_name
        self.rule_id = rule_id
        self.rule_name = rule_name
        self.tag = tag
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_notify_id is not None:
            result['EventNotifyId'] = self.event_notify_id
        if self.event_notify_method is not None:
            result['EventNotifyMethod'] = self.event_notify_method
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace is not None:
            result['Namespace'] = self.namespace
        if self.record_id is not None:
            result['RecordId'] = self.record_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventNotifyId') is not None:
            self.event_notify_id = m.get('EventNotifyId')
        if m.get('EventNotifyMethod') is not None:
            self.event_notify_method = m.get('EventNotifyMethod')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')
        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListEventCenterRecordResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        records: List[ListEventCenterRecordResponseBodyRecords] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.records = records
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.records:
            for k in self.records:
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Records'] = []
        if self.records is not None:
            for k in self.records:
                result['Records'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.records = []
        if m.get('Records') is not None:
            for k in m.get('Records'):
                temp_model = ListEventCenterRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListEventCenterRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventCenterRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListEventCenterRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListEventCenterRuleNameRequest(TeaModel):
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


class ListEventCenterRuleNameResponseBodyRuleNames(TeaModel):
    def __init__(
        self,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class ListEventCenterRuleNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        rule_names: List[ListEventCenterRuleNameResponseBodyRuleNames] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.request_id = request_id
        self.rule_names = rule_names

    def validate(self):
        if self.rule_names:
            for k in self.rule_names:
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
        result['RuleNames'] = []
        if self.rule_names is not None:
            for k in self.rule_names:
                result['RuleNames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.rule_names = []
        if m.get('RuleNames') is not None:
            for k in m.get('RuleNames'):
                temp_model = ListEventCenterRuleNameResponseBodyRuleNames()
                self.rule_names.append(temp_model.from_map(k))
        return self


class ListEventCenterRuleNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListEventCenterRuleNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListEventCenterRuleNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListInstanceRequest(TeaModel):
    def __init__(
        self,
        instance_name: str = None,
        instance_status: str = None,
        page_no: int = None,
        page_size: int = None,
        resource_group_id: str = None,
    ):
        self.instance_name = instance_name
        self.instance_status = instance_status
        self.page_no = page_no
        self.page_size = page_size
        self.resource_group_id = resource_group_id

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
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
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
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        modified_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.instance_specification = instance_specification
        self.instance_status = instance_status
        self.modified_time = modified_time
        self.region_id = region_id
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name
        if self.instance_specification is not None:
            result['InstanceSpecification'] = self.instance_specification
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')
        if m.get('InstanceSpecification') is not None:
            self.instance_specification = m.get('InstanceSpecification')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        instances: List[ListInstanceResponseBodyInstances] = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.code = code
        self.instances = instances
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = ListInstanceResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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


class ListInstanceEndpointResponseBodyEndpointsDomains(TeaModel):
    def __init__(
        self,
        domain: str = None,
        type: str = None,
    ):
        self.domain = domain
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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


class ListInstanceEndpointResponseBodyEndpoints(TeaModel):
    def __init__(
        self,
        acl_enable: bool = None,
        acl_entries: List[ListInstanceEndpointResponseBodyEndpointsAclEntries] = None,
        domains: List[ListInstanceEndpointResponseBodyEndpointsDomains] = None,
        enable: bool = None,
        endpoint_type: str = None,
        linked_vpcs: List[ListInstanceEndpointResponseBodyEndpointsLinkedVpcs] = None,
        status: str = None,
    ):
        self.acl_enable = acl_enable
        self.acl_entries = acl_entries
        self.domains = domains
        self.enable = enable
        self.endpoint_type = endpoint_type
        self.linked_vpcs = linked_vpcs
        self.status = status

    def validate(self):
        if self.acl_entries:
            for k in self.acl_entries:
                if k:
                    k.validate()
        if self.domains:
            for k in self.domains:
                if k:
                    k.validate()
        if self.linked_vpcs:
            for k in self.linked_vpcs:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl_enable is not None:
            result['AclEnable'] = self.acl_enable
        result['AclEntries'] = []
        if self.acl_entries is not None:
            for k in self.acl_entries:
                result['AclEntries'].append(k.to_map() if k else None)
        result['Domains'] = []
        if self.domains is not None:
            for k in self.domains:
                result['Domains'].append(k.to_map() if k else None)
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        result['LinkedVpcs'] = []
        if self.linked_vpcs is not None:
            for k in self.linked_vpcs:
                result['LinkedVpcs'].append(k.to_map() if k else None)
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AclEnable') is not None:
            self.acl_enable = m.get('AclEnable')
        self.acl_entries = []
        if m.get('AclEntries') is not None:
            for k in m.get('AclEntries'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsAclEntries()
                self.acl_entries.append(temp_model.from_map(k))
        self.domains = []
        if m.get('Domains') is not None:
            for k in m.get('Domains'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsDomains()
                self.domains.append(temp_model.from_map(k))
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        self.linked_vpcs = []
        if m.get('LinkedVpcs') is not None:
            for k in m.get('LinkedVpcs'):
                temp_model = ListInstanceEndpointResponseBodyEndpointsLinkedVpcs()
                self.linked_vpcs.append(temp_model.from_map(k))
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListInstanceEndpointResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        endpoints: List[ListInstanceEndpointResponseBodyEndpoints] = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.code = code
        self.endpoints = endpoints
        self.is_success = is_success
        self.request_id = request_id

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
        result['Endpoints'] = []
        if self.endpoints is not None:
            for k in self.endpoints:
                result['Endpoints'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.endpoints = []
        if m.get('Endpoints') is not None:
            for k in m.get('Endpoints'):
                temp_model = ListInstanceEndpointResponseBodyEndpoints()
                self.endpoints.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceEndpointResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        regions: List[ListInstanceRegionResponseBodyRegions] = None,
        request_id: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.regions = regions
        self.request_id = request_id

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
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = ListInstanceRegionResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListInstanceRegionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListInstanceRegionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListInstanceRegionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListNamespaceRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
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
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListNamespaceResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        resource_group_id: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_id = namespace_id
        self.namespace_name = namespace_name
        self.namespace_status = namespace_status
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.namespace_status is not None:
            result['NamespaceStatus'] = self.namespace_status
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NamespaceStatus') is not None:
            self.namespace_status = m.get('NamespaceStatus')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        return self


class ListNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        namespaces: List[ListNamespaceResponseBodyNamespaces] = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.namespaces = namespaces
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        result['Namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['Namespaces'].append(k.to_map() if k else None)
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        self.namespaces = []
        if m.get('Namespaces') is not None:
            for k in m.get('Namespaces'):
                temp_model = ListNamespaceResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRecordResponseBodyBuildRecordsImage(TeaModel):
    def __init__(
        self,
        image_tag: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoBuildRecordResponseBodyBuildRecords(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        build_status: str = None,
        end_time: str = None,
        image: ListRepoBuildRecordResponseBodyBuildRecordsImage = None,
        start_time: str = None,
    ):
        self.build_record_id = build_record_id
        self.build_status = build_status
        self.end_time = end_time
        self.image = image
        self.start_time = start_time

    def validate(self):
        if self.image:
            self.image.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.build_status is not None:
            result['BuildStatus'] = self.build_status
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.image is not None:
            result['Image'] = self.image.to_map()
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('BuildStatus') is not None:
            self.build_status = m.get('BuildStatus')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Image') is not None:
            temp_model = ListRepoBuildRecordResponseBodyBuildRecordsImage()
            self.image = temp_model.from_map(m['Image'])
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListRepoBuildRecordResponseBody(TeaModel):
    def __init__(
        self,
        build_records: List[ListRepoBuildRecordResponseBodyBuildRecords] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.build_records = build_records
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['BuildRecords'] = []
        if self.build_records is not None:
            for k in self.build_records:
                result['BuildRecords'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_records = []
        if m.get('BuildRecords') is not None:
            for k in m.get('BuildRecords'):
                temp_model = ListRepoBuildRecordResponseBodyBuildRecords()
                self.build_records.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoBuildRecordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoBuildRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRecordLogRequest(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
        offset: int = None,
        repo_id: str = None,
    ):
        self.build_record_id = build_record_id
        self.instance_id = instance_id
        self.offset = offset
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_record_id is not None:
            result['BuildRecordId'] = self.build_record_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.offset is not None:
            result['Offset'] = self.offset
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRecordId') is not None:
            self.build_record_id = m.get('BuildRecordId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRecordLogResponseBodyBuildRecordLogs(TeaModel):
    def __init__(
        self,
        build_stage: str = None,
        line_number: int = None,
        message: str = None,
    ):
        self.build_stage = build_stage
        self.line_number = line_number
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_stage is not None:
            result['BuildStage'] = self.build_stage
        if self.line_number is not None:
            result['LineNumber'] = self.line_number
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildStage') is not None:
            self.build_stage = m.get('BuildStage')
        if m.get('LineNumber') is not None:
            self.line_number = m.get('LineNumber')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ListRepoBuildRecordLogResponseBody(TeaModel):
    def __init__(
        self,
        build_record_logs: List[ListRepoBuildRecordLogResponseBodyBuildRecordLogs] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.build_record_logs = build_record_logs
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['BuildRecordLogs'] = []
        if self.build_record_logs is not None:
            for k in self.build_record_logs:
                result['BuildRecordLogs'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_record_logs = []
        if m.get('BuildRecordLogs') is not None:
            for k in m.get('BuildRecordLogs'):
                temp_model = ListRepoBuildRecordLogResponseBodyBuildRecordLogs()
                self.build_record_logs.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRecordLogResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoBuildRecordLogResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoBuildRecordLogResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoBuildRuleResponseBodyBuildRules(TeaModel):
    def __init__(
        self,
        build_args: List[str] = None,
        build_rule_id: str = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        image_tag: str = None,
        platforms: List[str] = None,
        push_name: str = None,
        push_type: str = None,
    ):
        self.build_args = build_args
        self.build_rule_id = build_rule_id
        self.dockerfile_location = dockerfile_location
        self.dockerfile_name = dockerfile_name
        self.image_tag = image_tag
        self.platforms = platforms
        self.push_name = push_name
        self.push_type = push_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        return self


class ListRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        build_rules: List[ListRepoBuildRuleResponseBodyBuildRules] = None,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.build_rules = build_rules
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        result['BuildRules'] = []
        if self.build_rules is not None:
            for k in self.build_rules:
                result['BuildRules'].append(k.to_map() if k else None)
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.build_rules = []
        if m.get('BuildRules') is not None:
            for k in m.get('BuildRules'):
                temp_model = ListRepoBuildRuleResponseBodyBuildRules()
                self.build_rules.append(temp_model.from_map(k))
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoBuildRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        namespace_name: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        target_instance_id: str = None,
        target_region_id: str = None,
    ):
        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.page_no = page_no
        self.page_size = page_size
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
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
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
        create_time: int = None,
        cross_user: bool = None,
        local_instance_id: str = None,
        local_namespace_name: str = None,
        local_region_id: str = None,
        local_repo_name: str = None,
        modified_time: int = None,
        sync_direction: str = None,
        sync_rule_id: str = None,
        sync_rule_name: str = None,
        sync_scope: str = None,
        sync_trigger: str = None,
        tag_filter: str = None,
        target_instance_id: str = None,
        target_namespace_name: str = None,
        target_region_id: str = None,
        target_repo_name: str = None,
    ):
        self.create_time = create_time
        self.cross_user = cross_user
        self.local_instance_id = local_instance_id
        self.local_namespace_name = local_namespace_name
        self.local_region_id = local_region_id
        self.local_repo_name = local_repo_name
        self.modified_time = modified_time
        self.sync_direction = sync_direction
        self.sync_rule_id = sync_rule_id
        self.sync_rule_name = sync_rule_name
        self.sync_scope = sync_scope
        self.sync_trigger = sync_trigger
        self.tag_filter = tag_filter
        self.target_instance_id = target_instance_id
        self.target_namespace_name = target_namespace_name
        self.target_region_id = target_region_id
        self.target_repo_name = target_repo_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.local_instance_id is not None:
            result['LocalInstanceId'] = self.local_instance_id
        if self.local_namespace_name is not None:
            result['LocalNamespaceName'] = self.local_namespace_name
        if self.local_region_id is not None:
            result['LocalRegionId'] = self.local_region_id
        if self.local_repo_name is not None:
            result['LocalRepoName'] = self.local_repo_name
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.sync_direction is not None:
            result['SyncDirection'] = self.sync_direction
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_rule_name is not None:
            result['SyncRuleName'] = self.sync_rule_name
        if self.sync_scope is not None:
            result['SyncScope'] = self.sync_scope
        if self.sync_trigger is not None:
            result['SyncTrigger'] = self.sync_trigger
        if self.tag_filter is not None:
            result['TagFilter'] = self.tag_filter
        if self.target_instance_id is not None:
            result['TargetInstanceId'] = self.target_instance_id
        if self.target_namespace_name is not None:
            result['TargetNamespaceName'] = self.target_namespace_name
        if self.target_region_id is not None:
            result['TargetRegionId'] = self.target_region_id
        if self.target_repo_name is not None:
            result['TargetRepoName'] = self.target_repo_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('LocalInstanceId') is not None:
            self.local_instance_id = m.get('LocalInstanceId')
        if m.get('LocalNamespaceName') is not None:
            self.local_namespace_name = m.get('LocalNamespaceName')
        if m.get('LocalRegionId') is not None:
            self.local_region_id = m.get('LocalRegionId')
        if m.get('LocalRepoName') is not None:
            self.local_repo_name = m.get('LocalRepoName')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('SyncDirection') is not None:
            self.sync_direction = m.get('SyncDirection')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncRuleName') is not None:
            self.sync_rule_name = m.get('SyncRuleName')
        if m.get('SyncScope') is not None:
            self.sync_scope = m.get('SyncScope')
        if m.get('SyncTrigger') is not None:
            self.sync_trigger = m.get('SyncTrigger')
        if m.get('TagFilter') is not None:
            self.tag_filter = m.get('TagFilter')
        if m.get('TargetInstanceId') is not None:
            self.target_instance_id = m.get('TargetInstanceId')
        if m.get('TargetNamespaceName') is not None:
            self.target_namespace_name = m.get('TargetNamespaceName')
        if m.get('TargetRegionId') is not None:
            self.target_region_id = m.get('TargetRegionId')
        if m.get('TargetRepoName') is not None:
            self.target_repo_name = m.get('TargetRepoName')
        return self


class ListRepoSyncRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sync_rules: List[ListRepoSyncRuleResponseBodySyncRules] = None,
        total_count: int = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.sync_rules = sync_rules
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SyncRules'] = []
        if self.sync_rules is not None:
            for k in self.sync_rules:
                result['SyncRules'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sync_rules = []
        if m.get('SyncRules') is not None:
            for k in m.get('SyncRules'):
                temp_model = ListRepoSyncRuleResponseBodySyncRules()
                self.sync_rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoSyncRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoSyncRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoSyncRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoSyncTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        sync_record_id: str = None,
        tag: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.sync_record_id = sync_record_id
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.sync_record_id is not None:
            result['SyncRecordId'] = self.sync_record_id
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('SyncRecordId') is not None:
            self.sync_record_id = m.get('SyncRecordId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageFrom(TeaModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoSyncTaskResponseBodySyncTasksImageTo(TeaModel):
    def __init__(
        self,
        image_tag: str = None,
        instance_id: str = None,
        region_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
    ):
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.region_id = region_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        return self


class ListRepoSyncTaskResponseBodySyncTasks(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        cross_user: bool = None,
        custom_link: bool = None,
        image_from: ListRepoSyncTaskResponseBodySyncTasksImageFrom = None,
        image_to: ListRepoSyncTaskResponseBodySyncTasksImageTo = None,
        modifed_time: int = None,
        sync_batch_task_id: str = None,
        sync_rule_id: str = None,
        sync_task_id: str = None,
        sync_trans_accelerate: bool = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        self.create_time = create_time
        self.cross_user = cross_user
        self.custom_link = custom_link
        self.image_from = image_from
        self.image_to = image_to
        self.modifed_time = modifed_time
        self.sync_batch_task_id = sync_batch_task_id
        self.sync_rule_id = sync_rule_id
        self.sync_task_id = sync_task_id
        self.sync_trans_accelerate = sync_trans_accelerate
        self.task_status = task_status
        self.task_trigger = task_trigger

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
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.cross_user is not None:
            result['CrossUser'] = self.cross_user
        if self.custom_link is not None:
            result['CustomLink'] = self.custom_link
        if self.image_from is not None:
            result['ImageFrom'] = self.image_from.to_map()
        if self.image_to is not None:
            result['ImageTo'] = self.image_to.to_map()
        if self.modifed_time is not None:
            result['ModifedTime'] = self.modifed_time
        if self.sync_batch_task_id is not None:
            result['SyncBatchTaskId'] = self.sync_batch_task_id
        if self.sync_rule_id is not None:
            result['SyncRuleId'] = self.sync_rule_id
        if self.sync_task_id is not None:
            result['SyncTaskId'] = self.sync_task_id
        if self.sync_trans_accelerate is not None:
            result['SyncTransAccelerate'] = self.sync_trans_accelerate
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_trigger is not None:
            result['TaskTrigger'] = self.task_trigger
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('CrossUser') is not None:
            self.cross_user = m.get('CrossUser')
        if m.get('CustomLink') is not None:
            self.custom_link = m.get('CustomLink')
        if m.get('ImageFrom') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageFrom()
            self.image_from = temp_model.from_map(m['ImageFrom'])
        if m.get('ImageTo') is not None:
            temp_model = ListRepoSyncTaskResponseBodySyncTasksImageTo()
            self.image_to = temp_model.from_map(m['ImageTo'])
        if m.get('ModifedTime') is not None:
            self.modifed_time = m.get('ModifedTime')
        if m.get('SyncBatchTaskId') is not None:
            self.sync_batch_task_id = m.get('SyncBatchTaskId')
        if m.get('SyncRuleId') is not None:
            self.sync_rule_id = m.get('SyncRuleId')
        if m.get('SyncTaskId') is not None:
            self.sync_task_id = m.get('SyncTaskId')
        if m.get('SyncTransAccelerate') is not None:
            self.sync_trans_accelerate = m.get('SyncTransAccelerate')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskTrigger') is not None:
            self.task_trigger = m.get('TaskTrigger')
        return self


class ListRepoSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        sync_tasks: List[ListRepoSyncTaskResponseBodySyncTasks] = None,
        total_count: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.sync_tasks = sync_tasks
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SyncTasks'] = []
        if self.sync_tasks is not None:
            for k in self.sync_tasks:
                result['SyncTasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.sync_tasks = []
        if m.get('SyncTasks') is not None:
            for k in m.get('SyncTasks'):
                temp_model = ListRepoSyncTaskResponseBodySyncTasks()
                self.sync_tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoSyncTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class ListRepoTagResponseBodyImages(TeaModel):
    def __init__(
        self,
        digest: str = None,
        image_create: str = None,
        image_id: str = None,
        image_size: int = None,
        image_update: str = None,
        status: str = None,
        tag: str = None,
    ):
        self.digest = digest
        self.image_create = image_create
        self.image_id = image_id
        self.image_size = image_size
        self.image_update = image_update
        self.status = status
        self.tag = tag

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.image_create is not None:
            result['ImageCreate'] = self.image_create
        if self.image_id is not None:
            result['ImageId'] = self.image_id
        if self.image_size is not None:
            result['ImageSize'] = self.image_size
        if self.image_update is not None:
            result['ImageUpdate'] = self.image_update
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('ImageCreate') is not None:
            self.image_create = m.get('ImageCreate')
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')
        if m.get('ImageSize') is not None:
            self.image_size = m.get('ImageSize')
        if m.get('ImageUpdate') is not None:
            self.image_update = m.get('ImageUpdate')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListRepoTagResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        images: List[ListRepoTagResponseBodyImages] = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.images = images
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        result['Images'] = []
        if self.images is not None:
            for k in self.images:
                result['Images'].append(k.to_map() if k else None)
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.images = []
        if m.get('Images') is not None:
            for k in m.get('Images'):
                temp_model = ListRepoTagResponseBodyImages()
                self.images.append(temp_model.from_map(k))
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepoTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepoTagResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepoTagScanResultRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        filter_value: str = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
        scan_task_id: str = None,
        scan_type: str = None,
        severity: str = None,
        tag: str = None,
        vul_query_key: str = None,
    ):
        self.digest = digest
        self.filter_value = filter_value
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.repo_id = repo_id
        self.scan_task_id = scan_task_id
        self.scan_type = scan_type
        self.severity = severity
        self.tag = tag
        self.vul_query_key = vul_query_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.digest is not None:
            result['Digest'] = self.digest
        if self.filter_value is not None:
            result['FilterValue'] = self.filter_value
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.vul_query_key is not None:
            result['VulQueryKey'] = self.vul_query_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Digest') is not None:
            self.digest = m.get('Digest')
        if m.get('FilterValue') is not None:
            self.filter_value = m.get('FilterValue')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('VulQueryKey') is not None:
            self.vul_query_key = m.get('VulQueryKey')
        return self


class ListRepoTagScanResultResponseBodyVulnerabilities(TeaModel):
    def __init__(
        self,
        added_by: str = None,
        alias_name: str = None,
        cve_link: str = None,
        cve_location: str = None,
        cve_name: str = None,
        description: str = None,
        feature: str = None,
        fix_cmd: str = None,
        scan_type: str = None,
        severity: str = None,
        version: str = None,
        version_fixed: str = None,
        version_format: str = None,
    ):
        self.added_by = added_by
        self.alias_name = alias_name
        self.cve_link = cve_link
        self.cve_location = cve_location
        self.cve_name = cve_name
        self.description = description
        self.feature = feature
        self.fix_cmd = fix_cmd
        self.scan_type = scan_type
        self.severity = severity
        self.version = version
        self.version_fixed = version_fixed
        self.version_format = version_format

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.added_by is not None:
            result['AddedBy'] = self.added_by
        if self.alias_name is not None:
            result['AliasName'] = self.alias_name
        if self.cve_link is not None:
            result['CveLink'] = self.cve_link
        if self.cve_location is not None:
            result['CveLocation'] = self.cve_location
        if self.cve_name is not None:
            result['CveName'] = self.cve_name
        if self.description is not None:
            result['Description'] = self.description
        if self.feature is not None:
            result['Feature'] = self.feature
        if self.fix_cmd is not None:
            result['FixCmd'] = self.fix_cmd
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
        if self.severity is not None:
            result['Severity'] = self.severity
        if self.version is not None:
            result['Version'] = self.version
        if self.version_fixed is not None:
            result['VersionFixed'] = self.version_fixed
        if self.version_format is not None:
            result['VersionFormat'] = self.version_format
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddedBy') is not None:
            self.added_by = m.get('AddedBy')
        if m.get('AliasName') is not None:
            self.alias_name = m.get('AliasName')
        if m.get('CveLink') is not None:
            self.cve_link = m.get('CveLink')
        if m.get('CveLocation') is not None:
            self.cve_location = m.get('CveLocation')
        if m.get('CveName') is not None:
            self.cve_name = m.get('CveName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')
        if m.get('FixCmd') is not None:
            self.fix_cmd = m.get('FixCmd')
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
        if m.get('Severity') is not None:
            self.severity = m.get('Severity')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('VersionFixed') is not None:
            self.version_fixed = m.get('VersionFixed')
        if m.get('VersionFormat') is not None:
            self.version_format = m.get('VersionFormat')
        return self


class ListRepoTagScanResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        vulnerabilities: List[ListRepoTagScanResultResponseBodyVulnerabilities] = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.request_id = request_id
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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Vulnerabilities'] = []
        if self.vulnerabilities is not None:
            for k in self.vulnerabilities:
                result['Vulnerabilities'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
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
        status_code: int = None,
        body: ListRepoTagScanResultResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        repo_event: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_tag: str = None,
        trigger_type: str = None,
        trigger_url: str = None,
    ):
        self.repo_event = repo_event
        self.trigger_id = trigger_id
        self.trigger_name = trigger_name
        self.trigger_tag = trigger_tag
        self.trigger_type = trigger_type
        self.trigger_url = trigger_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.repo_event is not None:
            result['RepoEvent'] = self.repo_event
        if self.trigger_id is not None:
            result['TriggerId'] = self.trigger_id
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RepoEvent') is not None:
            self.repo_event = m.get('RepoEvent')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
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
        status_code: int = None,
        body: ListRepoTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRepositoryRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
    ):
        self.instance_id = instance_id
        self.page_no = page_no
        self.page_size = page_size
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status

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
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        return self


class ListRepositoryResponseBodyRepositories(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        instance_id: str = None,
        modified_time: int = None,
        repo_build_type: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_status: str = None,
        repo_type: str = None,
        resource_group_id: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        self.create_time = create_time
        self.instance_id = instance_id
        self.modified_time = modified_time
        self.repo_build_type = repo_build_type
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_status = repo_status
        self.repo_type = repo_type
        self.resource_group_id = resource_group_id
        self.summary = summary
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.repo_build_type is not None:
            result['RepoBuildType'] = self.repo_build_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_status is not None:
            result['RepoStatus'] = self.repo_status
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('RepoBuildType') is not None:
            self.repo_build_type = m.get('RepoBuildType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoStatus') is not None:
            self.repo_status = m.get('RepoStatus')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class ListRepositoryResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        repositories: List[ListRepositoryResponseBodyRepositories] = None,
        request_id: str = None,
        total_count: str = None,
    ):
        self.code = code
        self.is_success = is_success
        self.page_no = page_no
        self.page_size = page_size
        self.repositories = repositories
        self.request_id = request_id
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        result['Repositories'] = []
        if self.repositories is not None:
            for k in self.repositories:
                result['Repositories'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        self.repositories = []
        if m.get('Repositories') is not None:
            for k in m.get('Repositories'):
                temp_model = ListRepositoryResponseBodyRepositories()
                self.repositories.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRepositoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRepositoryResponseBody()
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
        status_code: int = None,
        body: ResetLoginPasswordResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ResetLoginPasswordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChainRequest(TeaModel):
    def __init__(
        self,
        chain_config: str = None,
        chain_id: str = None,
        description: str = None,
        instance_id: str = None,
        name: str = None,
        scope_exclude: List[str] = None,
    ):
        self.chain_config = chain_config
        self.chain_id = chain_id
        self.description = description
        self.instance_id = instance_id
        self.name = name
        self.scope_exclude = scope_exclude

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.chain_config is not None:
            result['ChainConfig'] = self.chain_config
        if self.chain_id is not None:
            result['ChainId'] = self.chain_id
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.name is not None:
            result['Name'] = self.name
        if self.scope_exclude is not None:
            result['ScopeExclude'] = self.scope_exclude
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChainConfig') is not None:
            self.chain_config = m.get('ChainConfig')
        if m.get('ChainId') is not None:
            self.chain_id = m.get('ChainId')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ScopeExclude') is not None:
            self.scope_exclude = m.get('ScopeExclude')
        return self


class UpdateChainResponseBody(TeaModel):
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


class UpdateChainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateChainResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateChainResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartNamespaceRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
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
        status_code: int = None,
        body: UpdateChartNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateChartNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateChartRepositoryRequest(TeaModel):
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
        status_code: int = None,
        body: UpdateChartRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateChartRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateEventCenterRuleRequest(TeaModel):
    def __init__(
        self,
        event_channel: str = None,
        event_config: str = None,
        event_scope: str = None,
        event_type: str = None,
        instance_id: str = None,
        namespaces: List[str] = None,
        repo_names: List[str] = None,
        repo_tag_filter_pattern: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.event_channel = event_channel
        self.event_config = event_config
        self.event_scope = event_scope
        self.event_type = event_type
        self.instance_id = instance_id
        self.namespaces = namespaces
        self.repo_names = repo_names
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_config is not None:
            result['EventConfig'] = self.event_config
        if self.event_scope is not None:
            result['EventScope'] = self.event_scope
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespaces is not None:
            result['Namespaces'] = self.namespaces
        if self.repo_names is not None:
            result['RepoNames'] = self.repo_names
        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventConfig') is not None:
            self.event_config = m.get('EventConfig')
        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespaces') is not None:
            self.namespaces = m.get('Namespaces')
        if m.get('RepoNames') is not None:
            self.repo_names = m.get('RepoNames')
        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateEventCenterRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        event_channel: str = None,
        event_config: str = None,
        event_scope: str = None,
        event_type: str = None,
        instance_id: str = None,
        namespaces_shrink: str = None,
        repo_names_shrink: str = None,
        repo_tag_filter_pattern: str = None,
        rule_id: str = None,
        rule_name: str = None,
    ):
        self.event_channel = event_channel
        self.event_config = event_config
        self.event_scope = event_scope
        self.event_type = event_type
        self.instance_id = instance_id
        self.namespaces_shrink = namespaces_shrink
        self.repo_names_shrink = repo_names_shrink
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        self.rule_id = rule_id
        self.rule_name = rule_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.event_channel is not None:
            result['EventChannel'] = self.event_channel
        if self.event_config is not None:
            result['EventConfig'] = self.event_config
        if self.event_scope is not None:
            result['EventScope'] = self.event_scope
        if self.event_type is not None:
            result['EventType'] = self.event_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespaces_shrink is not None:
            result['Namespaces'] = self.namespaces_shrink
        if self.repo_names_shrink is not None:
            result['RepoNames'] = self.repo_names_shrink
        if self.repo_tag_filter_pattern is not None:
            result['RepoTagFilterPattern'] = self.repo_tag_filter_pattern
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.rule_name is not None:
            result['RuleName'] = self.rule_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventChannel') is not None:
            self.event_channel = m.get('EventChannel')
        if m.get('EventConfig') is not None:
            self.event_config = m.get('EventConfig')
        if m.get('EventScope') is not None:
            self.event_scope = m.get('EventScope')
        if m.get('EventType') is not None:
            self.event_type = m.get('EventType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Namespaces') is not None:
            self.namespaces_shrink = m.get('Namespaces')
        if m.get('RepoNames') is not None:
            self.repo_names_shrink = m.get('RepoNames')
        if m.get('RepoTagFilterPattern') is not None:
            self.repo_tag_filter_pattern = m.get('RepoTagFilterPattern')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')
        return self


class UpdateEventCenterRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
        rule_id: str = None,
    ):
        self.code = code
        self.request_id = request_id
        self.rule_id = rule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class UpdateEventCenterRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateEventCenterRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateEventCenterRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateInstanceEndpointStatusRequest(TeaModel):
    def __init__(
        self,
        enable: bool = None,
        endpoint_type: str = None,
        instance_id: str = None,
        module_name: str = None,
    ):
        self.enable = enable
        self.endpoint_type = endpoint_type
        self.instance_id = instance_id
        self.module_name = module_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        if self.endpoint_type is not None:
            result['EndpointType'] = self.endpoint_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        if m.get('EndpointType') is not None:
            self.endpoint_type = m.get('EndpointType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
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
        status_code: int = None,
        body: UpdateInstanceEndpointStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateInstanceEndpointStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateNamespaceRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        self.auto_create_repo = auto_create_repo
        self.default_repo_type = default_repo_type
        self.instance_id = instance_id
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_type is not None:
            result['DefaultRepoType'] = self.default_repo_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoCreateRepo') is not None:
            self.auto_create_repo = m.get('AutoCreateRepo')
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
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
        status_code: int = None,
        body: UpdateNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoBuildRuleRequest(TeaModel):
    def __init__(
        self,
        build_args: List[str] = None,
        build_rule_id: str = None,
        dockerfile_location: str = None,
        dockerfile_name: str = None,
        image_tag: str = None,
        instance_id: str = None,
        platforms: List[str] = None,
        push_name: str = None,
        push_type: str = None,
        repo_id: str = None,
    ):
        self.build_args = build_args
        self.build_rule_id = build_rule_id
        self.dockerfile_location = dockerfile_location
        self.dockerfile_name = dockerfile_name
        self.image_tag = image_tag
        self.instance_id = instance_id
        self.platforms = platforms
        self.push_name = push_name
        self.push_type = push_type
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.build_args is not None:
            result['BuildArgs'] = self.build_args
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.dockerfile_location is not None:
            result['DockerfileLocation'] = self.dockerfile_location
        if self.dockerfile_name is not None:
            result['DockerfileName'] = self.dockerfile_name
        if self.image_tag is not None:
            result['ImageTag'] = self.image_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.platforms is not None:
            result['Platforms'] = self.platforms
        if self.push_name is not None:
            result['PushName'] = self.push_name
        if self.push_type is not None:
            result['PushType'] = self.push_type
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildArgs') is not None:
            self.build_args = m.get('BuildArgs')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('DockerfileLocation') is not None:
            self.dockerfile_location = m.get('DockerfileLocation')
        if m.get('DockerfileName') is not None:
            self.dockerfile_name = m.get('DockerfileName')
        if m.get('ImageTag') is not None:
            self.image_tag = m.get('ImageTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Platforms') is not None:
            self.platforms = m.get('Platforms')
        if m.get('PushName') is not None:
            self.push_name = m.get('PushName')
        if m.get('PushType') is not None:
            self.push_type = m.get('PushType')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        return self


class UpdateRepoBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        self.build_rule_id = build_rule_id
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
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRepoBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRepoBuildRuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateRepoBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoSourceCodeRepoRequest(TeaModel):
    def __init__(
        self,
        auto_build: str = None,
        code_repo_id: str = None,
        code_repo_name: str = None,
        code_repo_namespace_name: str = None,
        code_repo_type: str = None,
        disable_cache_build: str = None,
        instance_id: str = None,
        oversea_build: str = None,
        repo_id: str = None,
    ):
        self.auto_build = auto_build
        self.code_repo_id = code_repo_id
        self.code_repo_name = code_repo_name
        self.code_repo_namespace_name = code_repo_namespace_name
        self.code_repo_type = code_repo_type
        self.disable_cache_build = disable_cache_build
        self.instance_id = instance_id
        self.oversea_build = oversea_build
        self.repo_id = repo_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_build is not None:
            result['AutoBuild'] = self.auto_build
        if self.code_repo_id is not None:
            result['CodeRepoId'] = self.code_repo_id
        if self.code_repo_name is not None:
            result['CodeRepoName'] = self.code_repo_name
        if self.code_repo_namespace_name is not None:
            result['CodeRepoNamespaceName'] = self.code_repo_namespace_name
        if self.code_repo_type is not None:
            result['CodeRepoType'] = self.code_repo_type
        if self.disable_cache_build is not None:
            result['DisableCacheBuild'] = self.disable_cache_build
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.oversea_build is not None:
            result['OverseaBuild'] = self.oversea_build
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBuild') is not None:
            self.auto_build = m.get('AutoBuild')
        if m.get('CodeRepoId') is not None:
            self.code_repo_id = m.get('CodeRepoId')
        if m.get('CodeRepoName') is not None:
            self.code_repo_name = m.get('CodeRepoName')
        if m.get('CodeRepoNamespaceName') is not None:
            self.code_repo_namespace_name = m.get('CodeRepoNamespaceName')
        if m.get('CodeRepoType') is not None:
            self.code_repo_type = m.get('CodeRepoType')
        if m.get('DisableCacheBuild') is not None:
            self.disable_cache_build = m.get('DisableCacheBuild')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OverseaBuild') is not None:
            self.oversea_build = m.get('OverseaBuild')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
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
        status_code: int = None,
        body: UpdateRepoSourceCodeRepoResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateRepoSourceCodeRepoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepoTriggerRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        repo_id: str = None,
        trigger_id: str = None,
        trigger_name: str = None,
        trigger_tag: str = None,
        trigger_type: str = None,
        trigger_url: str = None,
    ):
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.trigger_id = trigger_id
        self.trigger_name = trigger_name
        self.trigger_tag = trigger_tag
        self.trigger_type = trigger_type
        self.trigger_url = trigger_url

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
        if self.trigger_name is not None:
            result['TriggerName'] = self.trigger_name
        if self.trigger_tag is not None:
            result['TriggerTag'] = self.trigger_tag
        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type
        if self.trigger_url is not None:
            result['TriggerUrl'] = self.trigger_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('TriggerId') is not None:
            self.trigger_id = m.get('TriggerId')
        if m.get('TriggerName') is not None:
            self.trigger_name = m.get('TriggerName')
        if m.get('TriggerTag') is not None:
            self.trigger_tag = m.get('TriggerTag')
        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')
        if m.get('TriggerUrl') is not None:
            self.trigger_url = m.get('TriggerUrl')
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
        status_code: int = None,
        body: UpdateRepoTriggerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateRepoTriggerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRepositoryRequest(TeaModel):
    def __init__(
        self,
        detail: str = None,
        instance_id: str = None,
        repo_id: str = None,
        repo_name: str = None,
        repo_namespace_name: str = None,
        repo_type: str = None,
        summary: str = None,
        tag_immutability: bool = None,
    ):
        self.detail = detail
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        self.repo_type = repo_type
        self.summary = summary
        self.tag_immutability = tag_immutability

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.detail is not None:
            result['Detail'] = self.detail
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.repo_id is not None:
            result['RepoId'] = self.repo_id
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.summary is not None:
            result['Summary'] = self.summary
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Detail') is not None:
            self.detail = m.get('Detail')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
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
        status_code: int = None,
        body: UpdateRepositoryResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateRepositoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


