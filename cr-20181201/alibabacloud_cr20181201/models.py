# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class ArtifactLifecyclePolicyCondition(TeaModel):
    def __init__(
        self,
        last_pull_older_than_days: int = None,
        last_push_older_than_days: int = None,
        latest_tag_count: int = None,
    ):
        self.last_pull_older_than_days = last_pull_older_than_days
        self.last_push_older_than_days = last_push_older_than_days
        self.latest_tag_count = latest_tag_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_pull_older_than_days is not None:
            result['LastPullOlderThanDays'] = self.last_pull_older_than_days
        if self.last_push_older_than_days is not None:
            result['LastPushOlderThanDays'] = self.last_push_older_than_days
        if self.latest_tag_count is not None:
            result['LatestTagCount'] = self.latest_tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPullOlderThanDays') is not None:
            self.last_pull_older_than_days = m.get('LastPullOlderThanDays')
        if m.get('LastPushOlderThanDays') is not None:
            self.last_push_older_than_days = m.get('LastPushOlderThanDays')
        if m.get('LatestTagCount') is not None:
            self.latest_tag_count = m.get('LatestTagCount')
        return self


class ArtifactLifecyclePolicyFilter(TeaModel):
    def __init__(
        self,
        tag_wildcard: str = None,
    ):
        self.tag_wildcard = tag_wildcard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_wildcard is not None:
            result['TagWildcard'] = self.tag_wildcard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagWildcard') is not None:
            self.tag_wildcard = m.get('TagWildcard')
        return self


class ArtifactLifecyclePolicy(TeaModel):
    def __init__(
        self,
        condition: ArtifactLifecyclePolicyCondition = None,
        filter: ArtifactLifecyclePolicyFilter = None,
        type: str = None,
    ):
        self.condition = condition
        self.filter = filter
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = ArtifactLifecyclePolicyCondition()
            self.condition = temp_model.from_map(m['Condition'])
        if m.get('Filter') is not None:
            temp_model = ArtifactLifecyclePolicyFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RepoConfigurationArtifactBuildRuleParameters(TeaModel):
    def __init__(
        self,
        image_index_only: bool = None,
    ):
        # This parameter is required.
        self.image_index_only = image_index_only

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_index_only is not None:
            result['ImageIndexOnly'] = self.image_index_only
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIndexOnly') is not None:
            self.image_index_only = m.get('ImageIndexOnly')
        return self


class RepoConfiguration(TeaModel):
    def __init__(
        self,
        artifact_build_rule_parameters: RepoConfigurationArtifactBuildRuleParameters = None,
        repo_type: str = None,
        tag_immutability: bool = None,
    ):
        self.artifact_build_rule_parameters = artifact_build_rule_parameters
        # This parameter is required.
        self.repo_type = repo_type
        # This parameter is required.
        self.tag_immutability = tag_immutability

    def validate(self):
        if self.artifact_build_rule_parameters:
            self.artifact_build_rule_parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_build_rule_parameters is not None:
            result['ArtifactBuildRuleParameters'] = self.artifact_build_rule_parameters.to_map()
        if self.repo_type is not None:
            result['RepoType'] = self.repo_type
        if self.tag_immutability is not None:
            result['TagImmutability'] = self.tag_immutability
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactBuildRuleParameters') is not None:
            temp_model = RepoConfigurationArtifactBuildRuleParameters()
            self.artifact_build_rule_parameters = temp_model.from_map(m['ArtifactBuildRuleParameters'])
        if m.get('RepoType') is not None:
            self.repo_type = m.get('RepoType')
        if m.get('TagImmutability') is not None:
            self.tag_immutability = m.get('TagImmutability')
        return self


class CancelArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the artifact building task.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id
        # The ID of the instance.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class CancelRepoSyncTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        sync_task_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the replication task.
        # 
        # This parameter is required.
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


class CancelRepoSyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The response code.
        self.code = code
        # Indicates whether the CancelRepoSyncTask request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The request ID.
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


class CancelRepoSyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelRepoSyncTaskResponseBody = None,
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
            temp_model = CancelRepoSyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(
        self,
        resource_group_id: str = None,
        resource_id: str = None,
        resource_region_id: str = None,
    ):
        # The ID of the resource group to which you want to move the resource.
        # 
        # This parameter is required.
        self.resource_group_id = resource_group_id
        # The ID of the resource.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The ID of the region.
        # 
        # This parameter is required.
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
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class CreateArtifactBuildRuleRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        instance_id: str = None,
        parameters: Dict[str, Any] = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The type of the artifact.
        # 
        # *   `ACCELERATED_IMAGE`: accelerated images.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Additional parameters.
        self.parameters = parameters
        # The ID of the effective range of the rule.
        # 
        # *   Set the value to the ID of the image repository.
        # 
        # This parameter is required.
        self.scope_id = scope_id
        # The effective range of the rule. Valid values:
        # 
        # *   `REPOSITORY`
        # 
        # This parameter is required.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters is not None:
            result['Parameters'] = self.parameters
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class CreateArtifactBuildRuleShrinkRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        instance_id: str = None,
        parameters_shrink: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        # The type of the artifact.
        # 
        # *   `ACCELERATED_IMAGE`: accelerated images.
        # 
        # This parameter is required.
        self.artifact_type = artifact_type
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Additional parameters.
        self.parameters_shrink = parameters_shrink
        # The ID of the effective range of the rule.
        # 
        # *   Set the value to the ID of the image repository.
        # 
        # This parameter is required.
        self.scope_id = scope_id
        # The effective range of the rule. Valid values:
        # 
        # *   `REPOSITORY`
        # 
        # This parameter is required.
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.parameters_shrink is not None:
            result['Parameters'] = self.parameters_shrink
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Parameters') is not None:
            self.parameters_shrink = m.get('Parameters')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class CreateArtifactBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The ID of the accelerated image building rule.
        self.build_rule_id = build_rule_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID.
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


class CreateArtifactBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArtifactBuildRuleResponseBody = None,
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
            temp_model = CreateArtifactBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactLifecycleRuleRequest(TeaModel):
    def __init__(
        self,
        auto: bool = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Specify whether to automatically execute the lifecycle management rule.
        self.auto = auto
        # Specify whether to enable lifecycle management for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The name of the image repository.
        self.repo_name = repo_name
        # The number of images that you want to retain.
        self.retention_tag_count = retention_tag_count
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope.
        self.scope = scope
        # The regular expression that is used to indicate which image tags are retained.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class CreateArtifactLifecycleRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        rule_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The rule ID.
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
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateArtifactLifecycleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArtifactLifecycleRuleResponseBody = None,
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
            temp_model = CreateArtifactLifecycleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactSubscriptionRuleRequest(TeaModel):
    def __init__(
        self,
        accelerate: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
        override: bool = None,
        platform: List[str] = None,
        repo_name: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_regexp: str = None,
    ):
        # Indicates whether an acceleration link is enabled for image subscription. The subscription acceleration feature is in public preview. The feature is optimized based on scheduling policies and network links to accelerate image subscription.
        self.accelerate = accelerate
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the Container Registry namespace.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # Indicates whether the original image is overwritten.
        self.override = override
        # The operating system and architecture. If the source repository contains a multi-arch image, only the specified operating system and architecture are subscribed to the destination repository of the Enterprise Edition instance. Subscribe to the destination repository of an Enterprise Edition instance
        # 
        # This parameter is required.
        self.platform = platform
        # The name of the Container Registry repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The source namespace.
        self.source_namespace_name = source_namespace_name
        # The source of the artifact.
        # 
        # Valid values:
        # 
        # *   DOCKER_HUB: Docker Hub
        # *   GCR: GCR
        # *   QUAY: Quay.io
        # 
        # This parameter is required.
        self.source_provider = source_provider
        # The source repository.
        # 
        # This parameter is required.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        # 
        # This parameter is required.
        self.tag_count = tag_count
        # The image tag in the subscription source repository. Regular expressions are supported.
        # 
        # This parameter is required.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate is not None:
            result['Accelerate'] = self.accelerate
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.override is not None:
            result['Override'] = self.override
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class CreateArtifactSubscriptionRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        rule_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicate whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The ID of the artifact subscription rule.
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
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        return self


class CreateArtifactSubscriptionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArtifactSubscriptionRuleResponseBody = None,
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
            temp_model = CreateArtifactSubscriptionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateArtifactSubscriptionTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The rule ID.
        # 
        # This parameter is required.
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


class CreateArtifactSubscriptionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
        task_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The task ID.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class CreateArtifactSubscriptionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateArtifactSubscriptionTaskResponseBody = None,
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
            temp_model = CreateArtifactSubscriptionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRecordRequest(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
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


class CreateBuildRecordByRecordResponseBody(TeaModel):
    def __init__(
        self,
        build_record_id: str = None,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The HTTP status code. The status code 200 indicates that the request is successful.\\
        # Other status codes indicate that the request failed.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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


class CreateBuildRecordByRecordResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBuildRecordByRecordResponseBody = None,
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
            temp_model = CreateBuildRecordByRecordResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBuildRecordByRuleRequest(TeaModel):
    def __init__(
        self,
        build_rule_id: str = None,
        instance_id: str = None,
        repo_id: str = None,
    ):
        # The ID of the image building rule.
        # 
        # This parameter is required.
        self.build_rule_id = build_rule_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The configuration of the delivery chain in the JSON format.
        self.chain_config = chain_config
        # The description of the delivery chain.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the delivery chain.
        # 
        # This parameter is required.
        self.name = name
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name
        # Repositories in which the delivery chain does not take effect.
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
        # The ID of the delivery chain.
        self.chain_id = chain_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to automatically create repositories in the namespace. Valid values:
        # 
        # \\-`  true `: automatically creates repositories in the namespace.
        # 
        # \\-`  false `: does not automatically create repositories in the namespace.
        self.auto_create_repo = auto_create_repo
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
        self.repo_namespace_name = repo_namespace_name
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        # 
        # You can specify the RepoType or Summary parameter. The RepoType parameter is optional.
        self.repo_type = repo_type
        # The summary of the repository.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the repository.
        self.repo_id = repo_id
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description.
        self.comment = comment
        # The type of the endpoint. Set the value to Internet.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The CIDR block that is accessible.
        # 
        # This parameter is required.
        self.entry = entry
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to automatically create Alibaba Cloud DNS PrivateZone records. Valid values:
        # 
        # >  If you enable automatic creation of PrivateZone records, a PrivateZone record is automatically created when you associate a VPC with the instance.
        # 
        # *   `true`
        # *   `false`
        self.enable_create_dnsrecord_in_pvzt = enable_create_dnsrecord_in_pvzt
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: image repositories.
        # *   `Chart`: Helm charts.
        self.module_name = module_name
        # The VPC ID.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the vSwitch that is associated with the specified VPC.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        default_repo_configuration: RepoConfiguration = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        # Specifies whether to automatically create an image repository in the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration = default_repo_configuration
        # The default type of the repositories that are automatically created in the namespace. Valid values:
        # 
        # *   `PUBLIC`: public repositories
        # *   `PRIVATE`: private repositories.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace. The name must be 2 to 120 characters in length, and can contain lowercase letters, digits, and the following delimiters: underscores (_), hyphens (-), and periods (.). The name cannot start or end with a delimiter.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        if self.default_repo_configuration:
            self.default_repo_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_configuration is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration.to_map()
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
        if m.get('DefaultRepoConfiguration') is not None:
            temp_model = RepoConfiguration()
            self.default_repo_configuration = temp_model.from_map(m['DefaultRepoConfiguration'])
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class CreateNamespaceShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_configuration_shrink: str = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        # Specifies whether to automatically create an image repository in the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration_shrink = default_repo_configuration_shrink
        # The default type of the repositories that are automatically created in the namespace. Valid values:
        # 
        # *   `PUBLIC`: public repositories
        # *   `PRIVATE`: private repositories.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace. The name must be 2 to 120 characters in length, and can contain lowercase letters, digits, and the following delimiters: underscores (_), hyphens (-), and periods (.). The name cannot start or end with a delimiter.
        # 
        # This parameter is required.
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
        if self.default_repo_configuration_shrink is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration_shrink
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
        if m.get('DefaultRepoConfiguration') is not None:
            self.default_repo_configuration_shrink = m.get('DefaultRepoConfiguration')
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Building arguments.
        self.build_args = build_args
        # The path of the Dockerfile.
        self.dockerfile_location = dockerfile_location
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name
        # The tag of the image.
        # 
        # This parameter is required.
        self.image_tag = image_tag
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Architecture for image building. Valid values:
        # 
        # *   `linux/amd64`
        # *   `linux/arm64`
        # *   `linux/386`
        # *   `linux/arm/v7`
        # *   `inux/arm/v6`
        # 
        # Default value: `linux/amd64`
        self.platforms = platforms
        # The name of the push that triggers the building rule.
        # 
        # This parameter is required.
        self.push_name = push_name
        # The type of the push that triggers the building rule. Valid values:
        # 
        # *   `GIT_TAG`: tag push
        # *   `GIT_BRANCH`: branch push
        # 
        # This parameter is required.
        self.push_type = push_type
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The ID of the building rule.
        self.build_rule_id = build_rule_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to trigger image building when source code is committed. Valid values:
        # 
        # *   `true`: triggers image building when source code is committed.
        # *   `false`: does not trigger image building when source code is committed.
        self.auto_build = auto_build
        # The name of the source code repository.
        # 
        # This parameter is required.
        self.code_repo_name = code_repo_name
        # The namespace to which the source code repository belongs.
        # 
        # This parameter is required.
        self.code_repo_namespace_name = code_repo_namespace_name
        # The type of the source code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        # 
        # This parameter is required.
        self.code_repo_type = code_repo_type
        # Specifies whether to disable building caches. Valid values:
        # 
        # *   `true`: disables building caches.
        # *   `false`: enables building caches.
        self.disable_cache_build = disable_cache_build
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable Build With Servers Deployed Outside Chinese Mainland. Valid values:
        # 
        # *   `true`: enables Build With Servers Deployed Outside Chinese Mainland.
        # *   `false`: does not enable Build With Servers Deployed Outside Chinese Mainland.
        self.oversea_build = oversea_build
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        repo_name_filter: str = None,
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
        # The source instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace name of the source instance.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # The name of the image repository in the source instance.
        self.repo_name = repo_name
        # The regular expression that is used to filter repositories.
        # 
        # >  This parameter is valid only when SyncScope is set to `NAMESPACE`.
        self.repo_name_filter = repo_name_filter
        # The name of the image synchronization rule.
        # 
        # This parameter is required.
        self.sync_rule_name = sync_rule_name
        # The synchronization scope. Valid values:
        # 
        # *   `REPO`: synchronizes the image tags in an image repository that meet the synchronization rule.
        # *   `NAMESPACE`: synchronizes the image tags in a namespace that meet the synchronization rule.
        # 
        # This parameter is required.
        self.sync_scope = sync_scope
        # The mode of triggering the synchronization rule. Valid values:
        # 
        # *   `INITIATIVE`: manually triggers the synchronization rule.
        # *   `PASSIVE`: automatically triggers the synchronization rule.
        self.sync_trigger = sync_trigger
        # The regular expression that is used to filter image tags.
        # 
        # This parameter is required.
        self.tag_filter = tag_filter
        # The destination instance ID.
        # 
        # This parameter is required.
        self.target_instance_id = target_instance_id
        # The namespace name of the destination instance.
        # 
        # This parameter is required.
        self.target_namespace_name = target_namespace_name
        # The region ID of the destination instance.
        # 
        # This parameter is required.
        self.target_region_id = target_region_id
        # The name of the image repository in the destination instance.
        self.target_repo_name = target_repo_name
        # The user ID (UID) of the account to which the destination instance belongs.
        # 
        # >  If you synchronize images across accounts, you must use the UID.
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
        if self.repo_name_filter is not None:
            result['RepoNameFilter'] = self.repo_name_filter
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
        if m.get('RepoNameFilter') is not None:
            self.repo_name_filter = m.get('RepoNameFilter')
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
        # The HTTP status code.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The ID of the synchronization rule.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # This parameter is required.
        self.instance_id = instance_id
        self.override = override
        # This parameter is required.
        self.repo_id = repo_id
        # This parameter is required.
        self.tag = tag
        # This parameter is required.
        self.target_instance_id = target_instance_id
        # This parameter is required.
        self.target_namespace = target_namespace
        # This parameter is required.
        self.target_region_id = target_region_id
        # This parameter is required.
        self.target_repo_name = target_repo_name
        # This parameter is required.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The ID of the synchronization rule.
        # 
        # This parameter is required.
        self.sync_rule_id = sync_rule_id
        # The version of the image to be synchronized.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The ID of the synchronization task.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The source image tag.
        # 
        # This parameter is required.
        self.from_tag = from_tag
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name
        # The name of the image repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The image tag that you want to create.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        scan_type: str = None,
        tag: str = None,
    ):
        # The digest of the image.
        self.digest = digest
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The type of the scanning engine.
        # 
        # *   `SAS_SCAN_SERVICE`: Security Center scan engine (paid service)
        # *   `ACR_SCAN_SERVICE`: Container Registry scan engine
        self.scan_service = scan_service
        self.scan_type = scan_type
        # The image version.
        # 
        # This parameter is required.
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
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
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
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
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
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The name of the trigger.
        # 
        # This parameter is required.
        self.trigger_name = trigger_name
        # The image tag based on which the trigger is set.
        # 
        # > 
        # 
        # *   If `TriggerType` is set to `ALL`, `TriggerTag` can be set to a string or an array, for example, `*`.
        # 
        # *   If `TriggerType` is set to `TAG_LIST`, `TriggerTag` must be set to an array, for example, `[1]`.
        # *   If `TriggerType` is set to `TAG_REG_EXP`, `TriggerTag` must be set to a string, for example, `*`.
        self.trigger_tag = trigger_tag
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LIST`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        # 
        # This parameter is required.
        self.trigger_type = trigger_type
        # The URL of the trigger.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The ID of the trigger.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The description of the repository.
        self.detail = detail
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the image repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace to which the image repository belongs.
        # 
        # This parameter is required.
        self.repo_namespace_name = repo_namespace_name
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: The repository is a public repository.
        # *   `PRIVATE`: The repository is a private repository.
        # 
        # This parameter is required.
        self.repo_type = repo_type
        # The summary about the repository.
        # 
        # This parameter is required.
        self.summary = summary
        # Specifies whether to enable the feature of image tag immutability. Valid values:
        # 
        # *   `true`: enables the feature of image tag immutability.
        # *   `false`: disables the feature of image tag immutability.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class DeleteArtifactLifecycleRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The rule ID.
        # 
        # This parameter is required.
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


class DeleteArtifactLifecycleRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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


class DeleteArtifactLifecycleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteArtifactLifecycleRuleResponseBody = None,
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
            temp_model = DeleteArtifactLifecycleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteArtifactSubscriptionRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The rule ID.
        # 
        # This parameter is required.
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


class DeleteArtifactSubscriptionRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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


class DeleteArtifactSubscriptionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteArtifactSubscriptionRuleResponseBody = None,
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
            temp_model = DeleteArtifactSubscriptionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteChainRequest(TeaModel):
    def __init__(
        self,
        chain_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the delivery pipeline.
        # 
        # This parameter is required.
        self.chain_id = chain_id
        # The ID of the instance.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the chart namespace that you want to delete.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The name of the chart.
        # 
        # This parameter is required.
        self.chart = chart
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The version of the chart that you want to delete.
        # 
        # This parameter is required.
        self.release = release
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the event notification rule.
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
        # The return value.
        self.code = code
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The type of the endpoint. Set the value to Internet.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The CIDR block.
        # 
        # This parameter is required.
        self.entry = entry
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
        self.module_name = module_name
        # The ID of the VPC.
        # 
        # This parameter is required.
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the image building rule.
        # 
        # This parameter is required.
        self.build_rule_id = build_rule_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the synchronization rule.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The tag of the image.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The ID of the trigger.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
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
        # Return values
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetArtifactBuildRuleRequest(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        build_rule_id: str = None,
        instance_id: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        self.artifact_type = artifact_type
        self.build_rule_id = build_rule_id
        # This parameter is required.
        self.instance_id = instance_id
        self.scope_id = scope_id
        self.scope_type = scope_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetArtifactBuildRuleResponseBodyParameters(TeaModel):
    def __init__(
        self,
        image_index_only: bool = None,
        priority_file: str = None,
    ):
        self.image_index_only = image_index_only
        self.priority_file = priority_file

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_index_only is not None:
            result['ImageIndexOnly'] = self.image_index_only
        if self.priority_file is not None:
            result['PriorityFile'] = self.priority_file
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageIndexOnly') is not None:
            self.image_index_only = m.get('ImageIndexOnly')
        if m.get('PriorityFile') is not None:
            self.priority_file = m.get('PriorityFile')
        return self


class GetArtifactBuildRuleResponseBody(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        build_rule_id: str = None,
        code: str = None,
        is_success: bool = None,
        parameters: GetArtifactBuildRuleResponseBodyParameters = None,
        request_id: str = None,
        scope_id: str = None,
        scope_type: str = None,
    ):
        self.artifact_type = artifact_type
        self.build_rule_id = build_rule_id
        self.code = code
        self.is_success = is_success
        self.parameters = parameters
        self.request_id = request_id
        self.scope_id = scope_id
        self.scope_type = scope_type

    def validate(self):
        if self.parameters:
            self.parameters.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.build_rule_id is not None:
            result['BuildRuleId'] = self.build_rule_id
        if self.code is not None:
            result['Code'] = self.code
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.parameters is not None:
            result['Parameters'] = self.parameters.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope_id is not None:
            result['ScopeId'] = self.scope_id
        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('BuildRuleId') is not None:
            self.build_rule_id = m.get('BuildRuleId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Parameters') is not None:
            temp_model = GetArtifactBuildRuleResponseBodyParameters()
            self.parameters = temp_model.from_map(m['Parameters'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ScopeId') is not None:
            self.scope_id = m.get('ScopeId')
        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')
        return self


class GetArtifactBuildRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactBuildRuleResponseBody = None,
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
            temp_model = GetArtifactBuildRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactBuildTaskRequest(TeaModel):
    def __init__(
        self,
        build_task_id: str = None,
        instance_id: str = None,
    ):
        # The ID of the artifact building task.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id
        # The ID of the instance.
        # 
        # This parameter is required.
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
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type
        # The ID of the repository to which the source artifact belongs. The repository can only be an image repository.
        self.repo_id = repo_id
        # The version of the artifact. The artifact can only be an image.
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
        # The type of the artifact that is built in the task. The value can only be IMAGE.
        self.artifact_type = artifact_type
        # The ID of the repository to which the artifact that is built in the task belongs. The repository can only be an image repository. The value is the same as the ID of the repository to which the source artifact belongs.
        self.repo_id = repo_id
        # The version of the artifact that is built in the task. The artifact can only be an image.
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
        # The type of the artifact building task. Valid values:
        # 
        # *   `IMAGE_TO_ACCELERATED_IMAGE`: builds accelerated images for Container Service for Kubernetes (ACK) clusters.
        # *   `IMAGE_TO_ECI_ACCELERATED_IMAGE`: builds accelerated images for elastic container instances.
        self.artifact_build_type = artifact_build_type
        # The ID of the artifact building task.
        self.build_task_id = build_task_id
        # The return value.
        self.code = code
        # The time when the artifact building task ends.
        self.end_time = end_time
        self.instructions = instructions
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The information about the source artifact.
        self.source_artifact = source_artifact
        # The time when the artifact building task starts.
        self.start_time = start_time
        # The artifact that is built in the task.
        self.target_artifact = target_artifact
        # The status of the artifact that is built in the task. Valid values:
        # 
        # *   `PENDING`: The artifact is being scheduled.
        # *   `BUILDING`: The artifact is being built.
        # *   `SUCCESS`: The artifact is built.
        # *   `FAILED`: The artifact fails to be built.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetArtifactLifecycleRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The rule ID.
        # 
        # This parameter is required.
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


class GetArtifactLifecycleRuleResponseBodyPoliciesCondition(TeaModel):
    def __init__(
        self,
        last_pull_older_than_days: int = None,
        last_push_older_than_days: int = None,
        latest_tag_count: int = None,
    ):
        self.last_pull_older_than_days = last_pull_older_than_days
        self.last_push_older_than_days = last_push_older_than_days
        self.latest_tag_count = latest_tag_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_pull_older_than_days is not None:
            result['LastPullOlderThanDays'] = self.last_pull_older_than_days
        if self.last_push_older_than_days is not None:
            result['LastPushOlderThanDays'] = self.last_push_older_than_days
        if self.latest_tag_count is not None:
            result['LatestTagCount'] = self.latest_tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPullOlderThanDays') is not None:
            self.last_pull_older_than_days = m.get('LastPullOlderThanDays')
        if m.get('LastPushOlderThanDays') is not None:
            self.last_push_older_than_days = m.get('LastPushOlderThanDays')
        if m.get('LatestTagCount') is not None:
            self.latest_tag_count = m.get('LatestTagCount')
        return self


class GetArtifactLifecycleRuleResponseBodyPoliciesFilter(TeaModel):
    def __init__(
        self,
        tag_wildcard: str = None,
    ):
        self.tag_wildcard = tag_wildcard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_wildcard is not None:
            result['TagWildcard'] = self.tag_wildcard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagWildcard') is not None:
            self.tag_wildcard = m.get('TagWildcard')
        return self


class GetArtifactLifecycleRuleResponseBodyPolicies(TeaModel):
    def __init__(
        self,
        condition: GetArtifactLifecycleRuleResponseBodyPoliciesCondition = None,
        filter: GetArtifactLifecycleRuleResponseBodyPoliciesFilter = None,
        type: str = None,
    ):
        self.condition = condition
        self.filter = filter
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = GetArtifactLifecycleRuleResponseBodyPoliciesCondition()
            self.condition = temp_model.from_map(m['Condition'])
        if m.get('Filter') is not None:
            temp_model = GetArtifactLifecycleRuleResponseBodyPoliciesFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetArtifactLifecycleRuleResponseBody(TeaModel):
    def __init__(
        self,
        auto: bool = None,
        code: str = None,
        create_time: int = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        namespace_name: str = None,
        next_time: int = None,
        policies: List[GetArtifactLifecycleRuleResponseBodyPolicies] = None,
        repo_name: str = None,
        request_id: str = None,
        retention_tag_count: int = None,
        rule_id: str = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Indicates whether the lifecycle management rule is automatically executed.
        self.auto = auto
        # The return value.
        self.code = code
        # The time when the lifecycle management rule was created.
        self.create_time = create_time
        # Indicates whether lifecycle management is enabled for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the lifecycle management rule was last modified.
        self.modified_time = modified_time
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The time when the lifecycle management rule is next executed.
        self.next_time = next_time
        self.policies = policies
        # The name of the image repository.
        self.repo_name = repo_name
        # The request ID.
        self.request_id = request_id
        # The number of retained images.
        self.retention_tag_count = retention_tag_count
        # The rule ID.
        self.rule_id = rule_id
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope of artifacts.
        self.scope = scope
        # The regular expression that indicates which image tags are retained.
        self.tag_regexp = tag_regexp

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.code is not None:
            result['Code'] = self.code
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.next_time is not None:
            result['NextTime'] = self.next_time
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NextTime') is not None:
            self.next_time = m.get('NextTime')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = GetArtifactLifecycleRuleResponseBodyPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class GetArtifactLifecycleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactLifecycleRuleResponseBody = None,
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
            temp_model = GetArtifactLifecycleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactSubscriptionRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        rule_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The rule ID.
        # 
        # This parameter is required.
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


class GetArtifactSubscriptionRuleResponseBody(TeaModel):
    def __init__(
        self,
        accelerate: bool = None,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        modified_time: int = None,
        namespace_name: str = None,
        override: bool = None,
        platform: List[str] = None,
        repo_name: str = None,
        request_id: str = None,
        rule_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_regexp: str = None,
    ):
        # Indicates whether an acceleration link is enabled for image subscription. The subscription acceleration feature is in public preview. The feature is optimized based on scheduling policies and network links to accelerate image subscription.
        self.accelerate = accelerate
        # The return value.
        self.code = code
        # The time when the subscription rule was created.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the subscription rule was modified.
        self.modified_time = modified_time
        # The name of the Container Registry namespace.
        self.namespace_name = namespace_name
        # Indicates whether the original image is overwritten.
        self.override = override
        # The operating system and architecture. If the source repository contains multi-arch images, only the images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise Edition instance.
        self.platform = platform
        # The name of the Container Registry repository.
        self.repo_name = repo_name
        # The request ID.
        self.request_id = request_id
        # The rule ID.
        self.rule_id = rule_id
        # The name of the source namespace.
        self.source_namespace_name = source_namespace_name
        # The source of the artifact.
        # 
        # Valid values:
        # 
        # *   DOCKER_HUB: Docker Hub
        # *   GCR: GCR
        # *   QUAY: Quay.io
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        self.tag_count = tag_count
        # The image tag in the subscription source repository. Regular expressions are supported.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate is not None:
            result['Accelerate'] = self.accelerate
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
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.override is not None:
            result['Override'] = self.override
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')
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
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class GetArtifactSubscriptionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactSubscriptionRuleResponseBody = None,
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
            temp_model = GetArtifactSubscriptionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactSubscriptionTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        task_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetArtifactSubscriptionTaskResponseBody(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        code: str = None,
        end_time: int = None,
        instance_id: str = None,
        is_success: bool = None,
        message: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        request_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        source_repo_type: str = None,
        start_time: int = None,
        tag_subscription_count: int = None,
        tag_total_count: int = None,
        task_id: str = None,
        task_result: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The artifact type.
        self.artifact_type = artifact_type
        # The return value.
        self.code = code
        # The end time of the artifact subscription task.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The return message.
        self.message = message
        # The name of the Container Registry namespace.
        self.namespace_name = namespace_name
        # The name of the Container Registry repository.
        self.repo_name = repo_name
        # The request ID.
        self.request_id = request_id
        # The name of the source namespace.
        self.source_namespace_name = source_namespace_name
        # The artifact source.
        self.source_provider = source_provider
        # The name of the source repository.
        self.source_repo_name = source_repo_name
        # The type of the source repository.
        self.source_repo_type = source_repo_type
        # The start time of the artifact subscription task.
        self.start_time = start_time
        # The total subscribed tags.
        self.tag_subscription_count = tag_subscription_count
        # The total number of tags.
        self.tag_total_count = tag_total_count
        # The task ID.
        self.task_id = task_id
        # The task results.
        self.task_result = task_result
        # The status of the task.
        self.task_status = task_status
        # The type of the task. Valid values:
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.code is not None:
            result['Code'] = self.code
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_success is not None:
            result['IsSuccess'] = self.is_success
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.source_repo_type is not None:
            result['SourceRepoType'] = self.source_repo_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_subscription_count is not None:
            result['TagSubscriptionCount'] = self.tag_subscription_count
        if self.tag_total_count is not None:
            result['TagTotalCount'] = self.tag_total_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSuccess') is not None:
            self.is_success = m.get('IsSuccess')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('SourceRepoType') is not None:
            self.source_repo_type = m.get('SourceRepoType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagSubscriptionCount') is not None:
            self.tag_subscription_count = m.get('TagSubscriptionCount')
        if m.get('TagTotalCount') is not None:
            self.tag_total_count = m.get('TagTotalCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class GetArtifactSubscriptionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactSubscriptionTaskResponseBody = None,
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
            temp_model = GetArtifactSubscriptionTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetArtifactSubscriptionTaskResultRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
        task_id: str = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The task ID.
        # 
        # This parameter is required.
        self.task_id = task_id

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
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetArtifactSubscriptionTaskResultResponseBodyTaskResults(TeaModel):
    def __init__(
        self,
        end_time: int = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        result: str = None,
        start_time: int = None,
        status: str = None,
        tag: str = None,
        task_id: str = None,
    ):
        # The end time of the subscription task.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The name of the repository.
        self.repo_name = repo_name
        # The result of the task.
        self.result = result
        # The start time of the subscription task.
        self.start_time = start_time
        # The status of the task.
        self.status = status
        # The image tag.
        self.tag = tag
        # The task ID.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.result is not None:
            result['Result'] = self.result
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.tag is not None:
            result['Tag'] = self.tag
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetArtifactSubscriptionTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        task_results: List[GetArtifactSubscriptionTaskResultResponseBodyTaskResults] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The result of the artifact subscription task.
        self.task_results = task_results
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.task_results:
            for k in self.task_results:
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
        result['TaskResults'] = []
        if self.task_results is not None:
            for k in self.task_results:
                result['TaskResults'].append(k.to_map() if k else None)
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
        self.task_results = []
        if m.get('TaskResults') is not None:
            for k in m.get('TaskResults'):
                temp_model = GetArtifactSubscriptionTaskResultResponseBodyTaskResults()
                self.task_results.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class GetArtifactSubscriptionTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetArtifactSubscriptionTaskResultResponseBody = None,
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
            temp_model = GetArtifactSubscriptionTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthorizationTokenRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # The ID of the request.
        # 
        # This parameter is required.
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
        # The temporary password returned after you call this API operation is a Security Token Service (STS) token whose validity period is 1 hour. Take note of the following items when you log on to Container Registry instances by using an STS token:
        # 
        # *   If the STS token belongs to an Alibaba Cloud account, you can use the STS token to log on to all Container Registry instances that belong to the Alibaba Cloud account.
        # *   If the STS token belongs to a Resource Access Management (RAM) user, you can use the STS token to log on to all Container Registry instances that belong to the RAM user.
        # *   You can use an STS token to access only Container Registry instances to which the STS token is scoped.
        self.authorization_token = authorization_token
        # Indicates whether the API call is successful.
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.code = code
        # The return value.
        self.expire_time = expire_time
        # The username that is used to log on to the Container Registry instance.
        self.is_success = is_success
        # The timestamp when the temporary password expires. Unit: milliseconds.
        self.request_id = request_id
        # The password that is used to log on to the Container Registry instance.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # This parameter is required.
        self.chain_id = chain_id
        # This parameter is required.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # Indicates whether a repository was automatically created in the namespace. Valid values:
        # 
        # *   `true`: A repository was automatically created in the namespace.
        # *   `false`: No repository was automatically created in the namespace.
        self.auto_create_repo = auto_create_repo
        # The return value.
        self.code = code
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # The time when the chart repository was created.
        self.create_time = create_time
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the chart repository was last modified.
        self.modified_time = modified_time
        # The ID of the chart repository.
        self.repo_id = repo_id
        # The name of the chart repository.
        self.repo_name = repo_name
        # The name of the namespace to which the chart repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the chart repository. Valid values:
        # 
        # *   `NORMAL`: The repository is normal.
        # *   `DELETING`: The repository is being deleted.
        self.repo_status = repo_status
        # The type of the chart repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.repo_type = repo_type
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The summary about the chart repository.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
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


class GetInstanceResponseBodyTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class GetInstanceResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        create_time: int = None,
        instance_id: str = None,
        instance_issue: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        is_success: bool = None,
        modified_time: int = None,
        request_id: str = None,
        resource_group_id: str = None,
        tags: List[GetInstanceResponseBodyTags] = None,
    ):
        self.code = code
        # The time when the instance was created.
        self.create_time = create_time
        # The ID of the Container Registry instance.
        self.instance_id = instance_id
        # The issue occurs on the instance.
        self.instance_issue = instance_issue
        # The name of the instance.
        self.instance_name = instance_name
        # The edition of the instance. Valid values: Enterprise_Basic: Basic Edition instances Enterprise_Standard: Standard Edition instances Enterprise_Advanced: Advanced Edition instances
        self.instance_specification = instance_specification
        # The status of the instance. Valid values:
        # 
        # *   `PENDING`: The instance is being initialized.
        # *   `INIT_ERROR`: The instance failed to be initialized.
        # *   `STARTING`: The instance is being started.
        # *   `RUNNING`: The instance is running.
        # *   `STOPPING`: The instance is being stopped.
        # *   `STOPPED`: The instance is stopped.
        # *   `DELETING`: The instance is being deleted.
        # *   `DELETED`: The instance is deleted.
        self.instance_status = instance_status
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The time when the instance was last modified.
        self.modified_time = modified_time
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the instance.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

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
        if self.instance_issue is not None:
            result['InstanceIssue'] = self.instance_issue
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIssue') is not None:
            self.instance_issue = m.get('InstanceIssue')
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = GetInstanceResponseBodyTags()
                self.tags.append(temp_model.from_map(k))
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Return value
        self.code = code
        # Number of instances
        self.count = count
        # Indicates whether the API call was successful. Values:
        # - `true`: The API call was successful. 
        # - `false`: The API call failed.
        self.is_success = is_success
        # Request ID
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The type of the endpoint. Set the value to Internet.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
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
        # Remarks for public IP address whitelists.
        self.comment = comment
        # The public IP address whitelist.
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
        # The domain name that is used to access the Container Registry Enterprise Edition instance.
        self.domain = domain
        # The type of the domain name. Valid values:
        # 
        # *   `SYSTEM`: a system domain name.
        # *   `USER`: a user domain name.
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
        # Indicates whether the access control list (ACL) feature is enabled.
        self.acl_enable = acl_enable
        # The ACLs.
        self.acl_entries = acl_entries
        # The return value.
        self.code = code
        # Domain names.
        self.domains = domains
        # Indicates whether the ACL feature is enabled.
        self.enable = enable
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The status of the instance.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
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
        vpc_quota: str = None,
        vpc_usage: str = None,
    ):
        # The quota of chart namespaces.
        self.chart_namespace_quota = chart_namespace_quota
        # The number of chart namespaces that are created in the instance.
        self.chart_namespace_usage = chart_namespace_usage
        # The quota of chart repositories for the instance.
        self.chart_repo_quota = chart_repo_quota
        # The number of chart repositories that are created.
        self.chart_repo_usage = chart_repo_usage
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The quota of image namespaces for the instance.
        self.namespace_quota = namespace_quota
        # The number of image namespaces that are created in the instance.
        self.namespace_usage = namespace_usage
        # The quota of image repositories for the instance.
        self.repo_quota = repo_quota
        # The number of image repositories that are created in the instance.
        self.repo_usage = repo_usage
        # The ID of the request.
        self.request_id = request_id
        # VPC quota
        self.vpc_quota = vpc_quota
        # Number of bound VPCs
        self.vpc_usage = vpc_usage

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
        if self.vpc_quota is not None:
            result['VpcQuota'] = self.vpc_quota
        if self.vpc_usage is not None:
            result['VpcUsage'] = self.vpc_usage
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
        if m.get('VpcQuota') is not None:
            self.vpc_quota = m.get('VpcQuota')
        if m.get('VpcUsage') is not None:
            self.vpc_usage = m.get('VpcUsage')
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
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
        # Indicates whether the VPC is the default VPC over which the Container Registry instance is accessed.
        self.default_access = default_access
        # IP address.
        self.ip = ip
        # The status of the VPC. Valid values:
        # 
        # *   `CREATING`
        # *   `RUNNING`
        self.status = status
        # VPC ID
        self.vpc_id = vpc_id
        # The ID of the vSwitch.
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
        module_name: str = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Domain names.
        self.domains = domains
        # Indicates whether the VPC endpoint is enabled. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.enable = enable
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The VPCs that are added to the access control list.
        self.linked_vpcs = linked_vpcs
        # The name of the modules that can be accessed. Valid values:
        # 
        # *   `Registry`: image repositories.
        # *   `Chart`: Helm charts.
        self.module_name = module_name
        # The ID of the request.
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
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
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
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
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
        default_repo_configuration: RepoConfiguration = None,
        default_repo_type: str = None,
        instance_id: str = None,
        is_success: bool = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        request_id: str = None,
        resource_group_id: str = None,
    ):
        # Indicates whether a repository is automatically created when an image is pushed to the namespace.
        self.auto_create_repo = auto_create_repo
        # The return value.
        self.code = code
        self.default_repo_configuration = default_repo_configuration
        # The default type of repositories in the namespace. Valid values:
        # 
        # *   PUBLIC: public repositories.
        # *   PRIVATE: private repositories.
        self.default_repo_type = default_repo_type
        # The ID of the Container Registry instance.
        self.instance_id = instance_id
        # Indicates whether the request was successful.
        self.is_success = is_success
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The status of the namespace.
        # 
        # *   NORMAL
        # *   DELETING
        self.namespace_status = namespace_status
        # The request ID.
        self.request_id = request_id
        # The ID of the resource group to which the namespace belongs.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.default_repo_configuration:
            self.default_repo_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.code is not None:
            result['Code'] = self.code
        if self.default_repo_configuration is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration.to_map()
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
        if m.get('DefaultRepoConfiguration') is not None:
            temp_model = RepoConfiguration()
            self.default_repo_configuration = temp_model.from_map(m['DefaultRepoConfiguration'])
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The ID of the instance.
        # 
        # This parameter is required.
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
        # The tag of the image.
        self.image_tag = image_tag
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace to which the image repository belongs.
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
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The return value.
        self.code = code
        # The time when the image building was completed.
        self.end_time = end_time
        # The information about the image.
        self.image = image
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The time when the image building started.
        self.start_time = start_time
        # The status of the instance.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The status of the image building.
        self.build_status = build_status
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the repository.
        # 
        # This parameter is required.
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
        # Indicates whether image building is automatically triggered when source code is committed. Valid values:
        # 
        # *   `true`: Image building is automatically triggered when source code is committed.
        # *   `false`: Image building is not triggered when source code is committed.
        self.auto_build = auto_build
        # The response code.
        self.code = code
        # The address of the source code repository.
        self.code_repo_domain = code_repo_domain
        # The name of the source code repository.
        self.code_repo_name = code_repo_name
        # The namespace to which the source code repository belongs.
        self.code_repo_namespace_name = code_repo_namespace_name
        # The type of the code hosting platform. Valid values: `GITHUB`, `GITLAB`, `GITEE`, `CODE`, and `CODEUP`.
        self.code_repo_type = code_repo_type
        # Indicates whether build cache is disabled. Valid values:
        # 
        # *   `true`: Build cache is disabled.
        # *   `false`: Build cache is enabled.
        self.disable_cache_build = disable_cache_build
        # Indicates whether the API call is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # Indicates whether image building is accelerated for servers outside the Chinese mainland. Valid values:
        # 
        # *   `true`: Image building is accelerated for servers outside the Chinese mainland.
        # *   `false`: Image building is not accelerated for servers outside the Chinese mainland.
        self.oversea_build = oversea_build
        # The ID of the repository.
        self.repo_id = repo_id
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the synchronization task.
        # 
        # This parameter is required.
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
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace.
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
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the instance.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace.
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
        # The digest of the artifact.
        self.artifact_digest = artifact_digest
        # The digest of the image layer.
        self.digest = digest
        # The size of synchronized image layers.
        self.size = size
        # The ID of the synchronization task for the image layer.
        self.sync_layer_task_id = sync_layer_task_id
        # The size of the image layer that is synchronized.
        self.synced_size = synced_size
        # The status of the synchronization task. Valid values:
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
        task_issue: str = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the synchronization task is performed across Alibaba Cloud accounts.
        self.cross_user = cross_user
        # The source address of the image.
        self.image_from = image_from
        # The destination address of the image.
        self.image_to = image_to
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The synchronization tasks for the image layer.
        self.layer_tasks = layer_tasks
        # The synchronization progress. Valid values:
        # 
        # *   `0`: The synchronization starts or failed.
        # *   `1`: The synchronization is successful.
        self.progress = progress
        # The ID of the request.
        self.request_id = request_id
        # The ID of the synchronization task in which multiple images are synchronized at a time.
        self.sync_batch_task_id = sync_batch_task_id
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id
        # Indicates whether transfer acceleration is enabled in the synchronization process.
        self.sync_trans_accelerate = sync_trans_accelerate
        # The size of the image layer that is synchronized. Unit: bytes.
        self.synced_size = synced_size
        # The error message that is returned if the synchronization task fails.
        # 
        # >  The system uses this parameter to return an error message if the synchronization task fails.
        # 
        # Valid values:
        # 
        # *   OSS_POLICY_UNAUTHORIZED: Container Registry is not granted permissions to use Object Storage Service (OSS).
        # *   TAG_CONFLICT: The destination repository contains an image that has the same tag as the source image, and image tag immutability is enabled for the destination repository.
        # *   UNSUPPORTED_FORMAT: The manifest and config formats of the image to be synchronized are not supported.
        # *   INTERNAL_ERROR: The synchronization task failed due to internal issues on the server.
        # *   NETWORK_ERROR: The synchronization task failed due to unstable network connection.
        # *   DATA_LENGTH_EXCEEDED: The manifest or config of the image is oversized.
        self.task_issue = task_issue
        # The status of the task. Valid values:
        self.task_status = task_status
        # The policy that is used to trigger the synchronization task.
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
        if self.task_issue is not None:
            result['TaskIssue'] = self.task_issue
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
        if m.get('TaskIssue') is not None:
            self.task_issue = m.get('TaskIssue')
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The return value of status code.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The operation that you want to perform. Set the value to **GetRepoTag**.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The number of milliseconds that have elapsed since the image was created.
        # 
        # This parameter is required.
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
        # The ID of the image.
        self.code = code
        # The size of the image. Unit: Bytes.
        self.digest = digest
        # crr-tquyps22md8p****\
        self.image_create = image_create
        self.image_id = image_id
        # The number of milliseconds that have elapsed since the image was last updated.
        self.image_size = image_size
        # The ID of the request.
        self.image_update = image_update
        # The status of the image. Valid values:
        # 
        # *   `NORMAL`: The image is normal.
        # *   `DELETING`: The image is being deleted.
        self.is_success = is_success
        # 1.0
        self.request_id = request_id
        # The ID of the instance.
        self.status = status
        # The version of the repository.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class GetRepoTagScanStatusRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        repo_id: str = None,
        scan_task_id: str = None,
        scan_type: str = None,
        tag: str = None,
    ):
        # The image digest.
        self.digest = digest
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        self.scan_type = scan_type
        # The image tag.
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
        if self.scan_type is not None:
            result['ScanType'] = self.scan_type
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
        if m.get('ScanType') is not None:
            self.scan_type = m.get('ScanType')
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
        # The HTTP status code.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The type of the scanning engine.
        # 
        # *   `ACR_SCAN_SERVICE`: Trivy scan engine provided by Container Registry
        # *   `SAS_SCAN_SERVICE`: Security Center scan engine
        self.scan_service = scan_service
        # The scanning status of the image tag. Valid values:
        # 
        # *   `SCANNING`: The image tag is being scanned.
        # *   `COMPLETE`: The scanning of the image tag is complete.
        # *   `FAILED`: The image tag failed to be scanned.
        # *   `RETRYING`: The system is retrying to scan the image tag.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The number of unknown-severity vulnerabilities.
        self.digest = digest
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the image tag.
        self.repo_id = repo_id
        # The digest of the image.
        self.scan_task_id = scan_task_id
        # The ID of the security scan task.
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
        # The number of medium-severity vulnerabilities.
        self.code = code
        # The number of low-severity vulnerabilities.
        self.high_severity = high_severity
        # The number of high-severity vulnerabilities.
        self.is_success = is_success
        self.low_severity = low_severity
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.medium_severity = medium_severity
        # The total number of vulnerabilities detected on images.
        self.request_id = request_id
        # The return value.
        self.total_severity = total_severity
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
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
        # The return value.
        self.code = code
        # The time when the repository was created.
        self.create_time = create_time
        # The details of the repository.
        self.detail = detail
        # The ID of the instance.
        self.instance_id = instance_id
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The time when the repository was last modified.
        self.modified_time = modified_time
        # Indicates how the repository was created. Valid values:
        # 
        # *   `MANUAL`: The repository was manually created.
        # *   `AUTO`: The repository was automatically created.
        self.repo_build_type = repo_build_type
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace.
        self.repo_namespace_name = repo_namespace_name
        # The status of the repository.
        self.repo_status = repo_status
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: public repository.
        # *   `PRIVATE`: private repository.
        self.repo_type = repo_type
        # The ID of the request.
        self.request_id = request_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The summary of the repository.
        self.summary = summary
        # Indicates whether the feature of image tag immutability is enabled. Valid values:
        # 
        # *   `true`: The feature of image tag immutability is enabled.
        # *   `false`: The feature of image tag immutability is disabled.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the artifact build task.
        # 
        # This parameter is required.
        self.build_task_id = build_task_id
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        # 
        # This parameter is required.
        self.page = page
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        # 
        # This parameter is required.
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
        # The row number of the log entry.
        self.line_number = line_number
        # The log data.
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
        # The log entries of the artifact build task.
        self.build_task_logs = build_task_logs
        # The response code.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The request ID.
        self.request_id = request_id
        # The total number of log entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class ListArtifactLifecycleRuleRequest(TeaModel):
    def __init__(
        self,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # Specifies whether to enable lifecycle management for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The ID of the Container Registry Enterprise Edition instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition(TeaModel):
    def __init__(
        self,
        last_pull_older_than_days: int = None,
        last_push_older_than_days: int = None,
        latest_tag_count: int = None,
    ):
        self.last_pull_older_than_days = last_pull_older_than_days
        self.last_push_older_than_days = last_push_older_than_days
        self.latest_tag_count = latest_tag_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.last_pull_older_than_days is not None:
            result['LastPullOlderThanDays'] = self.last_pull_older_than_days
        if self.last_push_older_than_days is not None:
            result['LastPushOlderThanDays'] = self.last_push_older_than_days
        if self.latest_tag_count is not None:
            result['LatestTagCount'] = self.latest_tag_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPullOlderThanDays') is not None:
            self.last_pull_older_than_days = m.get('LastPullOlderThanDays')
        if m.get('LastPushOlderThanDays') is not None:
            self.last_push_older_than_days = m.get('LastPushOlderThanDays')
        if m.get('LatestTagCount') is not None:
            self.latest_tag_count = m.get('LatestTagCount')
        return self


class ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter(TeaModel):
    def __init__(
        self,
        tag_wildcard: str = None,
    ):
        self.tag_wildcard = tag_wildcard

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_wildcard is not None:
            result['TagWildcard'] = self.tag_wildcard
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagWildcard') is not None:
            self.tag_wildcard = m.get('TagWildcard')
        return self


class ListArtifactLifecycleRuleResponseBodyRulesPolicies(TeaModel):
    def __init__(
        self,
        condition: ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition = None,
        filter: ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter = None,
        type: str = None,
    ):
        self.condition = condition
        self.filter = filter
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()
        if self.filter is not None:
            result['Filter'] = self.filter.to_map()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = ListArtifactLifecycleRuleResponseBodyRulesPoliciesCondition()
            self.condition = temp_model.from_map(m['Condition'])
        if m.get('Filter') is not None:
            temp_model = ListArtifactLifecycleRuleResponseBodyRulesPoliciesFilter()
            self.filter = temp_model.from_map(m['Filter'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListArtifactLifecycleRuleResponseBodyRules(TeaModel):
    def __init__(
        self,
        auto: bool = None,
        create_time: int = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        modified_time: int = None,
        namespace_name: str = None,
        next_time: int = None,
        policies: List[ListArtifactLifecycleRuleResponseBodyRulesPolicies] = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        rule_id: str = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Indicates whether the lifecycle management rule is automatically executed.
        self.auto = auto
        # The time when the lifecycle management rule was created.
        self.create_time = create_time
        # Indicates whether lifecycle management is enabled for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        self.instance_id = instance_id
        # The time when the lifecycle management rule was last modified.
        self.modified_time = modified_time
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The time when the lifecycle management rule is next executed.
        self.next_time = next_time
        self.policies = policies
        # The name of the image repository.
        self.repo_name = repo_name
        # The number of retained images.
        self.retention_tag_count = retention_tag_count
        # The rule ID.
        self.rule_id = rule_id
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope of artifacts.
        self.scope = scope
        # The regular expression that indicates which image tags are retained.
        self.tag_regexp = tag_regexp

    def validate(self):
        if self.policies:
            for k in self.policies:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.next_time is not None:
            result['NextTime'] = self.next_time
        result['Policies'] = []
        if self.policies is not None:
            for k in self.policies:
                result['Policies'].append(k.to_map() if k else None)
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('NextTime') is not None:
            self.next_time = m.get('NextTime')
        self.policies = []
        if m.get('Policies') is not None:
            for k in m.get('Policies'):
                temp_model = ListArtifactLifecycleRuleResponseBodyRulesPolicies()
                self.policies.append(temp_model.from_map(k))
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class ListArtifactLifecycleRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[ListArtifactLifecycleRuleResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # _
        self.rules = rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
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
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
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
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListArtifactLifecycleRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactLifecycleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactLifecycleRuleResponseBody = None,
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
            temp_model = ListArtifactLifecycleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactSubscriptionRuleRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactSubscriptionRuleResponseBodyRules(TeaModel):
    def __init__(
        self,
        accelerate: bool = None,
        create_time: int = None,
        instance_id: str = None,
        modified_time: int = None,
        namespace_name: str = None,
        override: bool = None,
        platform: List[str] = None,
        repo_name: str = None,
        rule_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_regexp: str = None,
    ):
        # Indicates whether an acceleration link is enabled for image subscription. The subscription acceleration feature is in public preview. The feature is optimized based on scheduling policies and network links to accelerate image subscription.
        self.accelerate = accelerate
        # The time when the subscription rule was created.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The time when the subscription rule was modified.
        self.modified_time = modified_time
        # The name of the source namespace.
        self.namespace_name = namespace_name
        # Indicates whether the original image is overwritten.
        self.override = override
        # The operating system and architecture. If the source repository contains a multi-arch image, only the images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise Edition instance.
        self.platform = platform
        # The name of the source repository.
        self.repo_name = repo_name
        # The rule ID.
        self.rule_id = rule_id
        # The source namespace.
        self.source_namespace_name = source_namespace_name
        # The source of the artifact.
        # 
        # Valid values:
        # 
        # *   DOCKER_HUB: Docker Hub
        # *   GCR: GCR
        # *   QUAY: Quay.io
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        self.tag_count = tag_count
        # The image tag in the subscription source repository. Regular expressions are supported.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate is not None:
            result['Accelerate'] = self.accelerate
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.override is not None:
            result['Override'] = self.override
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class ListArtifactSubscriptionRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        rules: List[ListArtifactSubscriptionRuleResponseBodyRules] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`
        # *   `false`
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried artifact subscription rules.
        self.rules = rules
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.rules:
            for k in self.rules:
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
        result['Rules'] = []
        if self.rules is not None:
            for k in self.rules:
                result['Rules'].append(k.to_map() if k else None)
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
        self.rules = []
        if m.get('Rules') is not None:
            for k in m.get('Rules'):
                temp_model = ListArtifactSubscriptionRuleResponseBodyRules()
                self.rules.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactSubscriptionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactSubscriptionRuleResponseBody = None,
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
            temp_model = ListArtifactSubscriptionRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListArtifactSubscriptionTaskRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
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
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListArtifactSubscriptionTaskResponseBodyTasks(TeaModel):
    def __init__(
        self,
        artifact_type: str = None,
        end_time: str = None,
        instance_id: str = None,
        message: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        source_repo_type: str = None,
        start_time: str = None,
        tag_subscription_count: int = None,
        tag_total_count: int = None,
        task_id: str = None,
        task_result: str = None,
        task_status: str = None,
        task_type: str = None,
    ):
        # The type of the artifact.
        self.artifact_type = artifact_type
        # The end time of the artifact subscription task.
        self.end_time = end_time
        # The instance ID.
        self.instance_id = instance_id
        # The returned message.
        self.message = message
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the source namespace.
        self.source_namespace_name = source_namespace_name
        # The artifact source.
        self.source_provider = source_provider
        # The name of the source repository.
        self.source_repo_name = source_repo_name
        # The type of the source artifact.
        self.source_repo_type = source_repo_type
        # The start time of the artifact subscription task.
        self.start_time = start_time
        # The total number of subscribed tags.
        self.tag_subscription_count = tag_subscription_count
        # The total number of tags.
        self.tag_total_count = tag_total_count
        # The task ID.
        self.task_id = task_id
        # The task result.
        self.task_result = task_result
        # The status of the task.
        self.task_status = task_status
        # The type of the task.
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.artifact_type is not None:
            result['ArtifactType'] = self.artifact_type
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.source_repo_type is not None:
            result['SourceRepoType'] = self.source_repo_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.tag_subscription_count is not None:
            result['TagSubscriptionCount'] = self.tag_subscription_count
        if self.tag_total_count is not None:
            result['TagTotalCount'] = self.tag_total_count
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_result is not None:
            result['TaskResult'] = self.task_result
        if self.task_status is not None:
            result['TaskStatus'] = self.task_status
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArtifactType') is not None:
            self.artifact_type = m.get('ArtifactType')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('SourceRepoType') is not None:
            self.source_repo_type = m.get('SourceRepoType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('TagSubscriptionCount') is not None:
            self.tag_subscription_count = m.get('TagSubscriptionCount')
        if m.get('TagTotalCount') is not None:
            self.tag_total_count = m.get('TagTotalCount')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskResult') is not None:
            self.task_result = m.get('TaskResult')
        if m.get('TaskStatus') is not None:
            self.task_status = m.get('TaskStatus')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListArtifactSubscriptionTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListArtifactSubscriptionTaskResponseBodyTasks] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried artifact subscription tasks.
        self.tasks = tasks
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.tasks:
            for k in self.tasks:
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
        result['Tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['Tasks'].append(k.to_map() if k else None)
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
        self.tasks = []
        if m.get('Tasks') is not None:
            for k in m.get('Tasks'):
                temp_model = ListArtifactSubscriptionTaskResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListArtifactSubscriptionTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListArtifactSubscriptionTaskResponseBody = None,
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
            temp_model = ListArtifactSubscriptionTaskResponseBody()
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The name of the namespace.
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
        # The ID of the delivery chain.
        self.chain_id = chain_id
        # The time when the delivery chain was created.
        self.create_time = create_time
        # The description of the delivery chain.
        self.description = description
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the delivery chain was last modified.
        self.modified_time = modified_time
        # The name of the delivery chain.
        self.name = name
        # Repositories to which the delivery chain does not apply.
        self.scope_exclude = scope_exclude
        # The ID of the delivery chain scope.
        self.scope_id = scope_id
        # The type of the delivery chain scope.
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
        # The list of delivery chains.
        self.chains = chains
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of delivery chains.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The operation that you want to perform. Set this parameter to **ListChainInstance**.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The time when the delivery chain started.
        self.page_no = page_no
        # The name of the image repository.
        self.page_size = page_size
        # The time when the delivery chain is completed.
        self.repo_name = repo_name
        # The name of the delivery chain.
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
        # The name of the namespace.
        self.chain_id = chain_id
        # The number of entries returned on each page.
        self.chain_name = chain_name
        # The ID of the request.
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
        # The name of the namespace.
        self.chain = chain
        # 1
        self.chain_instance_id = chain_instance_id
        # The ID of the Container Registry instance.
        self.end_time = end_time
        # The ID of the delivery chain.
        self.repo_name = repo_name
        # The execution result of the delivery chain. Valid values:
        # 
        # *   `SUCCESS`
        # *   `FAILED`
        # *   `CANCELED`
        # *   `DENIED`
        self.repo_namespace_name = repo_namespace_name
        # The list of the execution records of delivery chains.
        self.result = result
        # test-repo
        self.start_time = start_time
        # The status of the delivery chain. Valid values:
        # 
        # *   `RUNNING`
        # *   `COMPLETE`
        # *   `CANCELING`
        # *   `CANCELED`
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
        # The number of entries to return on each page.
        self.chain_instances = chain_instances
        # The version of the delivery chain.
        self.code = code
        # The page number of the page to return.
        self.instance_id = instance_id
        # The execution record of the delivery chain.
        self.is_success = is_success
        # 30
        self.page_no = page_no
        # Indicates whether the operation is successful.
        self.page_size = page_size
        # The ID of the Container Registry instance.
        self.request_id = request_id
        # The name of the repository.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
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
        # Indicates whether a repository was automatically created when a chart is pushed to the namespace.
        self.auto_create_repo = auto_create_repo
        # The default repository type. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The ID of the namespace.
        self.namespace_id = namespace_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The ID of the resource group to which the instance belongs.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The namespaces.
        self.namespaces = namespaces
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The chart whose versions you want to query.
        self.chart = chart
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace.
        # 
        # This parameter is required.
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
        # The name of the chart version.
        self.chart = chart
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the chart was last modified.
        self.modified_time = modified_time
        # The version number of the chart.
        self.release = release
        # The ID of the chart repository.
        self.repo_id = repo_id
        # The size of the chart of the version. Unit: bytes.
        self.size = size
        # The status of the chart.
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
        # The list of chart versions.
        self.chart_releases = chart_releases
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the chart repositories that you want to query. Valid values:
        # 
        # *   `ALL`: query repositories of all status.
        # *   `NORMAL`: query normal repositories.
        # *   `DELETING`: query repositories that are being deleted.
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
        # The time when the repository was created.
        self.create_time = create_time
        # The ID of the instance.
        self.instance_id = instance_id
        # The time when the repository was last modified.
        self.modified_time = modified_time
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the repository. Valid values:
        # 
        # *   `NORMAL`: The repository is normal.
        # *   `DELETING`: The repository is being deleted.
        self.repo_status = repo_status
        # The type of the repository. Valid values:
        # 
        # *   `PRIVATE`: a private repository
        # *   `PUBLIC`: a public repository
        self.repo_type = repo_type
        # The ID of the resource group to which the repository belongs.
        self.resource_group_id = resource_group_id
        # The summary about the repository.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The queried repositories.
        self.repositories = repositories
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        repo_name: str = None,
        repo_namespace_name: str = None,
        rule_id: str = None,
    ):
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The ID of the event notification rule.
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
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.repo_namespace_name is not None:
            result['RepoNamespaceName'] = self.repo_namespace_name
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
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RepoNamespaceName') is not None:
            self.repo_namespace_name = m.get('RepoNamespaceName')
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
        # The time when the event was created.
        self.create_time = create_time
        # The event notification channel.
        self.event_channel = event_channel
        # The ID of the event notification.
        self.event_notify_id = event_notify_id
        # The notification method. Valid values:
        # 
        # *   `http`: The notification is sent over HTTP.
        # *   `https`: The notification is sent over HTTPS.
        # *   `dingding`: The notification is sent by using DingTalk.
        self.event_notify_method = event_notify_method
        # The type of the event.
        self.event_type = event_type
        # The ID of the instance.
        self.instance_id = instance_id
        # The namespace.
        self.namespace = namespace
        # The ID of the event record.
        self.record_id = record_id
        # The name of the image repository.
        self.repo_name = repo_name
        # The ID of the event notification rule.
        self.rule_id = rule_id
        # The name of the event notification rule.
        self.rule_name = rule_name
        # The tags.
        self.tag = tag
        # The time when the event was last updated.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The list of historical events.
        self.records = records
        # The ID of the request.
        self.request_id = request_id
        # The total entries of historical events.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
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
        # The ID of the event notification rule.
        self.rule_id = rule_id
        # The name of the event notification rule.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The list of names of event notification rules.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The instance name.
        self.instance_name = instance_name
        # The status of the instance. Valid values:
        # 
        # *   `PENDING`: The instance is being initialized.
        # *   `INIT_ERROR`: The initialization of the instance fails.
        # *   `STARTING`: The instance is being started.
        # *   `RUNNING`: The instance is running.
        # *   `STOPPING`: The instance is being stopped.
        # *   `STOPPED`: The instance is stopped.
        # *   `DELETING`: The instance is being deleted.
        # *   `DELETED`: The instance is deleted.
        self.instance_status = instance_status
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the resource group to which the instance belongs.
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


class ListInstanceResponseBodyInstancesTags(TeaModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListInstanceResponseBodyInstances(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        instance_id: str = None,
        instance_issue: str = None,
        instance_name: str = None,
        instance_specification: str = None,
        instance_status: str = None,
        modified_time: str = None,
        region_id: str = None,
        resource_group_id: str = None,
        tags: List[ListInstanceResponseBodyInstancesTags] = None,
    ):
        # The time when the instance was created.
        self.create_time = create_time
        # The instance ID.
        self.instance_id = instance_id
        # The issue occurs on the instance.
        self.instance_issue = instance_issue
        # The name of the instance.
        self.instance_name = instance_name
        # The edition of the Container Registry Enterprise Edition instance.
        self.instance_specification = instance_specification
        # The status of the instance.
        self.instance_status = instance_status
        # The time when the instance was last modified.
        self.modified_time = modified_time
        # The region ID of the instance.
        self.region_id = region_id
        # The ID of the resource group to which the instance belongs.
        self.resource_group_id = resource_group_id
        # The tags of the instance.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_issue is not None:
            result['InstanceIssue'] = self.instance_issue
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
        result['Tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['Tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceIssue') is not None:
            self.instance_issue = m.get('InstanceIssue')
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
        self.tags = []
        if m.get('Tags') is not None:
            for k in m.get('Tags'):
                temp_model = ListInstanceResponseBodyInstancesTags()
                self.tags.append(temp_model.from_map(k))
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
        # The return value.
        self.code = code
        # The queried instances.
        self.instances = instances
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page. Default value: 30.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        summary: bool = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: image repositories.
        # *   `Chart`: Helm charts.
        self.module_name = module_name
        # Specify whether to return endpoints in simple mode. If yes, no access control information about the endpoint is returned.
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
        if self.module_name is not None:
            result['ModuleName'] = self.module_name
        if self.summary is not None:
            result['Summary'] = self.summary
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ModuleName') is not None:
            self.module_name = m.get('ModuleName')
        if m.get('Summary') is not None:
            self.summary = m.get('Summary')
        return self


class ListInstanceEndpointResponseBodyEndpointsAclEntries(TeaModel):
    def __init__(
        self,
        entry: str = None,
    ):
        # The information about the ACL.
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
        # The domain name of the Container Registry instance.
        self.domain = domain
        # The type of the domain name. Valid values:
        # 
        # *   SYSTEM: system domain name.
        # *   USER: user domain name.
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
        # VPC ID
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
        # Indicates whether the endpoint is added to an access control list (ACL).
        self.acl_enable = acl_enable
        # The ACLs that are configured for the instance.
        self.acl_entries = acl_entries
        # The list of domain names of the Container Registry instance.
        self.domains = domains
        # Indicates whether the endpoint is added to an ACL.
        self.enable = enable
        # The type of the endpoint.
        self.endpoint_type = endpoint_type
        # The VPCs associated with the instance.
        self.linked_vpcs = linked_vpcs
        # The status of the endpoint.
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
        # The return value.
        self.code = code
        # The endpoints of the instance.
        self.endpoints = endpoints
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The language used for response parameters. Set this parameter to `zh-CN`.
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
        # The name of the region.
        self.local_name = local_name
        # The ID of the region.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The list of regions.
        self.regions = regions
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespace name.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`
        # *   `DELETING`
        self.namespace_status = namespace_status
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
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
        default_repo_configuration: RepoConfiguration = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_id: str = None,
        namespace_name: str = None,
        namespace_status: str = None,
        resource_group_id: str = None,
    ):
        # Indicates whether the automatically creating repositories feature is enabled for the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration = default_repo_configuration
        # The default type of repositories in the namespace. Valid values:
        # 
        # *   `PUBLIC`: public repositories.
        # *   `PRIVATE`: private repositories.
        self.default_repo_type = default_repo_type
        # The instance ID.
        self.instance_id = instance_id
        # The namespace ID.
        self.namespace_id = namespace_id
        # The namespace name.
        self.namespace_name = namespace_name
        # The status of the namespace. Valid values:
        # 
        # *   `NORMAL`: The namespace is normal.
        # *   `DELETING`: The namespace is being deleted.
        self.namespace_status = namespace_status
        # The resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        if self.default_repo_configuration:
            self.default_repo_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_configuration is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration.to_map()
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
        if m.get('DefaultRepoConfiguration') is not None:
            temp_model = RepoConfiguration()
            self.default_repo_configuration = temp_model.from_map(m['DefaultRepoConfiguration'])
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
        # The HTTP status code.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The queried namespaces.
        self.namespaces = namespaces
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of the queried namespaces.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the repository.
        # 
        # This parameter is required.
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
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
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
        # The ID of the image building record.
        self.build_record_id = build_record_id
        # The status of the image building.
        self.build_status = build_status
        # The time when the image building ended.
        self.end_time = end_time
        # The information about the image.
        self.image = image
        # The time when the image building started.
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
        # The list of image building records.
        self.build_records = build_records
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the image building record.
        # 
        # This parameter is required.
        self.build_record_id = build_record_id
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The offset of log lines.
        self.offset = offset
        # The ID of the image repository.
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
        # The stage of the building that is recorded in the log entry.
        self.build_stage = build_stage
        # The line number of the log entry.
        self.line_number = line_number
        # The content of the log.
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
        # The log content of the image building record.
        self.build_record_logs = build_record_logs
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The ID of the image building rule.
        self.build_rule_id = build_rule_id
        # The directory of the Dockerfile.
        self.dockerfile_location = dockerfile_location
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name
        # The tag of the image.
        self.image_tag = image_tag
        self.platforms = platforms
        # The name of the push that triggers the building rule.
        self.push_name = push_name
        # The type of the push that triggers the image building rule. Valid values:
        # 
        # *   GIT_BRANCH: branch push
        # *   GIT_TAG: tag push
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
        # The list of image building rules.
        self.build_rules = build_rules
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The name of the image repository.
        self.repo_name = repo_name
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id
        # The region ID of the destination instance.
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
        repo_name_filter: str = None,
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
        # The time when the synchronization rule was created.
        self.create_time = create_time
        # Indicates whether the synchronization is performed across Alibaba Cloud accounts. Valid values:
        # 
        # *   `true`: Images are synchronized across Alibaba Cloud accounts.
        # *   `false`: Images are synchronized within the same Alibaba Cloud account.
        # 
        # Default value: `false`.
        self.cross_user = cross_user
        # The ID of the source instance.
        self.local_instance_id = local_instance_id
        # The name of the namespace in the source instance.
        self.local_namespace_name = local_namespace_name
        # The region ID of the source instance.
        self.local_region_id = local_region_id
        # The name of the repository in the source instance.
        self.local_repo_name = local_repo_name
        # The time when the synchronization rule was last modified.
        self.modified_time = modified_time
        # The regular expression that is used to filter repositories.
        # 
        # >  This parameter is valid only when SyncScope is set to `NAMESPACE`.
        self.repo_name_filter = repo_name_filter
        # The synchronization direction. Valid values:
        # 
        # *   `FROM`: Images are synchronized from the source instance to the destination instance.
        # *   `TO`: Images are synchronized from the destination instance to the source instance.
        self.sync_direction = sync_direction
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id
        # The name of the synchronization rule.
        self.sync_rule_name = sync_rule_name
        # The synchronization scope. Valid values:
        # 
        # *   `NAMESPACE`: synchronizes the image tags in a namespace that meet the synchronization rule.
        # *   `REPO`: synchronizes the image tags in an image repository that meet the synchronization rule.
        self.sync_scope = sync_scope
        # The policy that is applied to trigger the synchronization rule. Valid values:
        # 
        # *   `INITIATIVE`: The synchronization rule is positively triggered.
        # *   `PASSIVE`: The synchronization rule is passively triggered.
        self.sync_trigger = sync_trigger
        # The regular expression that is used to filter image tags.
        self.tag_filter = tag_filter
        # The ID of the destination instance.
        self.target_instance_id = target_instance_id
        # The name of the namespace in the destination instance.
        self.target_namespace_name = target_namespace_name
        # The region ID of the destination instance.
        self.target_region_id = target_region_id
        # The name of the repository in the destination instance.
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
        if self.repo_name_filter is not None:
            result['RepoNameFilter'] = self.repo_name_filter
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
        if m.get('RepoNameFilter') is not None:
            self.repo_name_filter = m.get('RepoNameFilter')
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried synchronization rules.
        self.sync_rules = sync_rules
        # The total number of entries returned.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The repository name.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The ID of the synchronization task record, which is the same as SyncBatchTaskId in the response.
        # 
        # >  If an image meets multiple synchronization rules and multiple synchronization tasks are generated for the image, these synchronization tasks use the same SyncBatchTaskId.
        self.sync_record_id = sync_record_id
        # The image tag.
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
        # The image tag.
        self.image_tag = image_tag
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The repository name.
        self.repo_name = repo_name
        # The namespace to which the repository belongs.
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
        # The image tag.
        self.image_tag = image_tag
        # The instance ID.
        self.instance_id = instance_id
        # The region ID.
        self.region_id = region_id
        # The repository name.
        self.repo_name = repo_name
        # The namespace to which the repository belongs.
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
        task_issue: str = None,
        task_status: str = None,
        task_trigger: str = None,
    ):
        # The time when the synchronization task was created.
        self.create_time = create_time
        # Indicates whether the synchronization task is performed across Alibaba Cloud accounts. Valid values:
        # 
        # *   `true`: The image synchronization task is performed across accounts.
        # *   `false`: The image synchronization task is performed within the same account.
        # 
        # Default value: `false`.
        self.cross_user = cross_user
        # Indicates whether a custom synchronization link is used.
        self.custom_link = custom_link
        # The information about the source image.
        self.image_from = image_from
        # The information about the destination image.
        self.image_to = image_to
        # The time when the synchronization task was last modified.
        self.modifed_time = modifed_time
        # The ID of the image synchronization batch tasks, which is the same as the value of SyncRecordId in the request.
        # 
        # >  If an image meets multiple synchronization rules and multiple synchronization tasks are generated for the image, these synchronization tasks use the same SyncBatchTaskId.
        self.sync_batch_task_id = sync_batch_task_id
        # The ID of the synchronization rule.
        self.sync_rule_id = sync_rule_id
        # The ID of the synchronization task.
        self.sync_task_id = sync_task_id
        # Indicates whether the synchronization transfer acceleration feature is enabled for the synchronization task.
        self.sync_trans_accelerate = sync_trans_accelerate
        # The error message that is returned if the synchronization task fails.
        # 
        # >  The system uses this parameter to return an error message if the synchronization task fails.
        # 
        # Valid value:
        # 
        # *   OSS_POLICY_UNAUTHORIZED: Container Registry is not granted permissions to access Object Storage Service (OSS).
        # *   TAG_CONFLICT: The destination repository contains an image that has the same tag as the source image, and image tag immutability is enabled for the destination repository.
        # *   UNSUPPORTED_FORMAT: The manifest or config format of the image to be synchronized is not supported.
        # *   INTERNAL_ERROR: The synchronization task failed due to internal issues on the server.
        # *   NETWORK_ERROR: The synchronization task failed due to unstable network connection.
        # *   DATA_LENGTH_EXCEEDED: The manifest or config of the image is oversized.
        self.task_issue = task_issue
        # The status of the synchronization task.
        self.task_status = task_status
        # The policy that is configured to trigger the synchronization task. Valid values:
        # 
        # *   `PASSIVE`: automatically triggers the synchronization task.
        # *   `INITIATIVE`: manually triggers the synchronization task.
        # 
        # Default value: `PASSIVE`.
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
        if self.task_issue is not None:
            result['TaskIssue'] = self.task_issue
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
        if m.get('TaskIssue') is not None:
            self.task_issue = m.get('TaskIssue')
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
        # The HTTP status code.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried synchronization tasks.
        self.sync_tasks = sync_tasks
        # The total number of the queried synchronization tasks.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The ID of the repository.
        # 
        # This parameter is required.
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
        # The digest of the image.
        self.digest = digest
        # The time when the image was created.
        self.image_create = image_create
        # The ID of the image.
        self.image_id = image_id
        # The size of the image.
        self.image_size = image_size
        # The time when the image was last updated.
        self.image_update = image_update
        # The status of the image.
        self.status = status
        # The tag of the image.
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
        # The return value.
        self.code = code
        # The images.
        self.images = images
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of returned entries.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The digest of the image.
        self.digest = digest
        # The parameter whose value that you want to query. Fox example, if the value is `FixCmd`, only the `FixCmd` parameter is returned.
        self.filter_value = filter_value
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The number of the page to return.
        self.page_no = page_no
        # The number of entries to return on each page.
        self.page_size = page_size
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the security scan task.
        self.scan_task_id = scan_task_id
        # The type of the vulnerability. Valid values:
        # 
        # *   `cve`: image system vulnerability
        # *   `sca`: image application vulnerability
        self.scan_type = scan_type
        # The severity of the vulnerability. Valid values:
        # 
        # *   `High`
        # *   `Medium`
        # *   `Low`
        # *   `Unknown`
        self.severity = severity
        # The name of the image tag.
        self.tag = tag
        # The keyword for fuzzy search used in scanning. The value can be a CVE name.
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
        # The ID of the image layer where the vulnerability was detected.
        self.added_by = added_by
        # The name of the vulnerability.
        self.alias_name = alias_name
        # The URL of the vulnerability.
        self.cve_link = cve_link
        # The directory of the vulnerability.
        self.cve_location = cve_location
        # The name of the vulnerability.
        self.cve_name = cve_name
        # The description of the vulnerability.
        self.description = description
        # The cause of the vulnerability.
        self.feature = feature
        # The command used to fix the vulnerability.
        self.fix_cmd = fix_cmd
        # The type of the vulnerability. Valid values:
        # 
        # *   `cve`: image system vulnerability
        # *   `sca`: image application vulnerability
        self.scan_type = scan_type
        # The severity of the vulnerability.
        self.severity = severity
        # The version of the vulnerability.
        self.version = version
        # The version where the vulnerability was fixed.
        self.version_fixed = version_fixed
        # The format of the vulnerability.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request failed.
        self.is_success = is_success
        # The number of the returned page.
        self.page_no = page_no
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of vulnerabilities detected on images.
        self.total_count = total_count
        # The details about the detected vulnerabilities.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the repository.
        # 
        # This parameter is required.
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
        # The type of the event that activates the trigger. Valid values:
        # 
        # *   `BUILD_SUCCESS`: The trigger is activated when an image building task is successful.
        # *   `BUILD_Fail`: The trigger is activated when an image building task fails.
        self.repo_event = repo_event
        # The ID of the trigger.
        self.trigger_id = trigger_id
        # The name of the trigger.
        self.trigger_name = trigger_name
        # The image tag based on which the trigger is set.
        self.trigger_tag = trigger_tag
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LISTTAG`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type
        # The URL of the trigger.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
        self.request_id = request_id
        # The triggers of the repository.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the Container Registry instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value larger than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
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
        # The time when the repository was created.
        self.create_time = create_time
        # The ID of the Container Registry instance to which the repository belongs.
        self.instance_id = instance_id
        # The time when the repository was last modified.
        self.modified_time = modified_time
        # The type of the repository building. Valid values:
        # 
        # *   `AUTO`: The repository is automatically built.
        # *   `MANUAL`: The repository is manually built.
        self.repo_build_type = repo_build_type
        # The ID of the repository.
        self.repo_id = repo_id
        # The name of the repository.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        self.repo_namespace_name = repo_namespace_name
        # The status of the repository.
        self.repo_status = repo_status
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`
        # *   `PRIVATE`
        self.repo_type = repo_type
        # The ID of the resource group to which the repository belongs.
        self.resource_group_id = resource_group_id
        # The summary of the repository.
        self.summary = summary
        # Indicates whether the feature of image tag immutability is enabled for the repository.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The information about the repositories.
        self.repositories = repositories
        # The request ID.
        self.request_id = request_id
        # The total number of the queried image repositories.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class ListScanBaselineByTaskRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        level: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
        scan_task_id: str = None,
        tag: str = None,
    ):
        # The digest value of the image.
        self.digest = digest
        # The ID of the Container Registry instance.
        self.instance_id = instance_id
        # The level of the baseline risk.
        self.level = level
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The ID of the image repository.
        self.repo_id = repo_id
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The image version.
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
        if self.level is not None:
            result['Level'] = self.level
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListScanBaselineByTaskResponseBodyScanBaselines(TeaModel):
    def __init__(
        self,
        baseline_class_alias: str = None,
        baseline_detail_advice: str = None,
        baseline_detail_description: str = None,
        baseline_detail_prompt: str = None,
        baseline_item_count: int = None,
        baseline_name_alias: str = None,
        baseline_name_key: str = None,
        baseline_name_level: str = None,
        create_time: int = None,
        first_scan_time: int = None,
        high_risk_item_count: int = None,
        low_risk_item_count: int = None,
        middle_risk_item_count: int = None,
        scan_task_id: str = None,
        update_time: int = None,
    ):
        # The category to which the baseline risk belongs.
        self.baseline_class_alias = baseline_class_alias
        # Suggestions about how to fix the baseline risk.
        self.baseline_detail_advice = baseline_detail_advice
        # The description of the baseline risk.
        self.baseline_detail_description = baseline_detail_description
        # The path and content of the baseline risk.
        self.baseline_detail_prompt = baseline_detail_prompt
        # The number of baseline risks.
        self.baseline_item_count = baseline_item_count
        # The name of the baseline risk.
        self.baseline_name_alias = baseline_name_alias
        # The key of the baseline name.
        self.baseline_name_key = baseline_name_key
        # The severity of the baseline risk.
        self.baseline_name_level = baseline_name_level
        # The creation time.
        self.create_time = create_time
        # The time of the first scan.
        self.first_scan_time = first_scan_time
        # High risk quantity.
        self.high_risk_item_count = high_risk_item_count
        # Low risk quantity.
        self.low_risk_item_count = low_risk_item_count
        # Medium risk quantity.
        self.middle_risk_item_count = middle_risk_item_count
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The update time.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.baseline_class_alias is not None:
            result['BaselineClassAlias'] = self.baseline_class_alias
        if self.baseline_detail_advice is not None:
            result['BaselineDetailAdvice'] = self.baseline_detail_advice
        if self.baseline_detail_description is not None:
            result['BaselineDetailDescription'] = self.baseline_detail_description
        if self.baseline_detail_prompt is not None:
            result['BaselineDetailPrompt'] = self.baseline_detail_prompt
        if self.baseline_item_count is not None:
            result['BaselineItemCount'] = self.baseline_item_count
        if self.baseline_name_alias is not None:
            result['BaselineNameAlias'] = self.baseline_name_alias
        if self.baseline_name_key is not None:
            result['BaselineNameKey'] = self.baseline_name_key
        if self.baseline_name_level is not None:
            result['BaselineNameLevel'] = self.baseline_name_level
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time
        if self.high_risk_item_count is not None:
            result['HighRiskItemCount'] = self.high_risk_item_count
        if self.low_risk_item_count is not None:
            result['LowRiskItemCount'] = self.low_risk_item_count
        if self.middle_risk_item_count is not None:
            result['MiddleRiskItemCount'] = self.middle_risk_item_count
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineClassAlias') is not None:
            self.baseline_class_alias = m.get('BaselineClassAlias')
        if m.get('BaselineDetailAdvice') is not None:
            self.baseline_detail_advice = m.get('BaselineDetailAdvice')
        if m.get('BaselineDetailDescription') is not None:
            self.baseline_detail_description = m.get('BaselineDetailDescription')
        if m.get('BaselineDetailPrompt') is not None:
            self.baseline_detail_prompt = m.get('BaselineDetailPrompt')
        if m.get('BaselineItemCount') is not None:
            self.baseline_item_count = m.get('BaselineItemCount')
        if m.get('BaselineNameAlias') is not None:
            self.baseline_name_alias = m.get('BaselineNameAlias')
        if m.get('BaselineNameKey') is not None:
            self.baseline_name_key = m.get('BaselineNameKey')
        if m.get('BaselineNameLevel') is not None:
            self.baseline_name_level = m.get('BaselineNameLevel')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')
        if m.get('HighRiskItemCount') is not None:
            self.high_risk_item_count = m.get('HighRiskItemCount')
        if m.get('LowRiskItemCount') is not None:
            self.low_risk_item_count = m.get('LowRiskItemCount')
        if m.get('MiddleRiskItemCount') is not None:
            self.middle_risk_item_count = m.get('MiddleRiskItemCount')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListScanBaselineByTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        scan_baselines: List[ListScanBaselineByTaskResponseBodyScanBaselines] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request was successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The page number.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The scanned baseline risks.
        self.scan_baselines = scan_baselines
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scan_baselines:
            for k in self.scan_baselines:
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
        result['ScanBaselines'] = []
        if self.scan_baselines is not None:
            for k in self.scan_baselines:
                result['ScanBaselines'].append(k.to_map() if k else None)
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
        self.scan_baselines = []
        if m.get('ScanBaselines') is not None:
            for k in m.get('ScanBaselines'):
                temp_model = ListScanBaselineByTaskResponseBodyScanBaselines()
                self.scan_baselines.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScanBaselineByTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScanBaselineByTaskResponseBody = None,
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
            temp_model = ListScanBaselineByTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScanMaliciousFileByTaskRequest(TeaModel):
    def __init__(
        self,
        digest: str = None,
        instance_id: str = None,
        level: str = None,
        page_no: int = None,
        page_size: int = None,
        repo_id: str = None,
        scan_task_id: str = None,
        tag: str = None,
    ):
        # The image digest.
        self.digest = digest
        # The instance ID.
        self.instance_id = instance_id
        # The severity of the malicious file.
        self.level = level
        # The page number.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 100. If you specify a value greater than 100 for this parameter, the system reports a parameter error or uses 100 as the maximum value.
        self.page_size = page_size
        # The image repository ID.
        self.repo_id = repo_id
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The image tag.
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
        if self.level is not None:
            result['Level'] = self.level
        if self.page_no is not None:
            result['PageNo'] = self.page_no
        if self.page_size is not None:
            result['PageSize'] = self.page_size
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
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RepoId') is not None:
            self.repo_id = m.get('RepoId')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('Tag') is not None:
            self.tag = m.get('Tag')
        return self


class ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        file_path: str = None,
        first_scan_time: int = None,
        level: str = None,
        malicious_md_5: str = None,
        malicious_name: str = None,
        scan_task_id: str = None,
        update_time: int = None,
    ):
        # The time when the image was created.
        self.create_time = create_time
        # The path of the file.
        self.file_path = file_path
        # The time when the image was first scanned.
        self.first_scan_time = first_scan_time
        # The severity of the malicious file.
        self.level = level
        # The MD5 hash value of the malicious file.
        self.malicious_md_5 = malicious_md_5
        # The type of the malicious file.
        self.malicious_name = malicious_name
        # The ID of the image scan task.
        self.scan_task_id = scan_task_id
        # The time when the image was updated.
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
        if self.file_path is not None:
            result['FilePath'] = self.file_path
        if self.first_scan_time is not None:
            result['FirstScanTime'] = self.first_scan_time
        if self.level is not None:
            result['Level'] = self.level
        if self.malicious_md_5 is not None:
            result['MaliciousMd5'] = self.malicious_md_5
        if self.malicious_name is not None:
            result['MaliciousName'] = self.malicious_name
        if self.scan_task_id is not None:
            result['ScanTaskId'] = self.scan_task_id
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('FilePath') is not None:
            self.file_path = m.get('FilePath')
        if m.get('FirstScanTime') is not None:
            self.first_scan_time = m.get('FirstScanTime')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('MaliciousMd5') is not None:
            self.malicious_md_5 = m.get('MaliciousMd5')
        if m.get('MaliciousName') is not None:
            self.malicious_name = m.get('MaliciousName')
        if m.get('ScanTaskId') is not None:
            self.scan_task_id = m.get('ScanTaskId')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListScanMaliciousFileByTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        is_success: bool = None,
        page_no: int = None,
        page_size: int = None,
        request_id: str = None,
        scan_malicious_files: List[ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles] = None,
        total_count: int = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The page number. Default value: 1.
        self.page_no = page_no
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The queried malicious files.
        self.scan_malicious_files = scan_malicious_files
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.scan_malicious_files:
            for k in self.scan_malicious_files:
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
        result['ScanMaliciousFiles'] = []
        if self.scan_malicious_files is not None:
            for k in self.scan_malicious_files:
                result['ScanMaliciousFiles'].append(k.to_map() if k else None)
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
        self.scan_malicious_files = []
        if m.get('ScanMaliciousFiles') is not None:
            for k in m.get('ScanMaliciousFiles'):
                temp_model = ListScanMaliciousFileByTaskResponseBodyScanMaliciousFiles()
                self.scan_malicious_files.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListScanMaliciousFileByTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListScanMaliciousFileByTaskResponseBody = None,
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
            temp_model = ListScanMaliciousFileByTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with acs: or aliyun, and cannot contain http:// or https://.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # It can be up to 128 characters in length. It cannot start with acs: or aliyun and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[ListTagResourcesRequestTag] = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request or if no next query exists. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # The ID of the region in which the resources are deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify a maximum of 20 resource IDs.
        self.resource_id = resource_id
        # The type of the resources. Instance resources are supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag list.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResourcesTagResource(TeaModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The resource ID.
        self.resource_id = resource_id
        # The resource type.
        self.resource_type = resource_type
        # The tag key.
        self.tag_key = tag_key
        # The tag value.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(
        self,
        tag_resource: List[ListTagResourcesResponseBodyTagResourcesTagResource] = None,
    ):
        self.tag_resource = tag_resource

    def validate(self):
        if self.tag_resource:
            for k in self.tag_resource:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['TagResource'] = []
        if self.tag_resource is not None:
            for k in self.tag_resource:
                result['TagResource'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tag_resource = []
        if m.get('TagResource') is not None:
            for k in m.get('TagResource'):
                temp_model = ListTagResourcesResponseBodyTagResourcesTagResource()
                self.tag_resource.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        next_token: str = None,
        request_id: str = None,
        tag_resources: ListTagResourcesResponseBodyTagResources = None,
    ):
        # A pagination token. It can be used in the next request to retrieve a new page of results. If NextToken is empty, no next page exists.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The tags that are added to the resource.
        self.tag_resources = tag_resources

    def validate(self):
        if self.tag_resources:
            self.tag_resources.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.tag_resources is not None:
            result['TagResources'] = self.tag_resources.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TagResources') is not None:
            temp_model = ListTagResourcesResponseBodyTagResources()
            self.tag_resources = temp_model.from_map(m['TagResources'])
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagResourcesResponseBody = None,
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetLoginPasswordRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        password: str = None,
    ):
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The new password that you specify to log on to the instance. The password must be 8 to 32 bits in length, and must contain at least two of the following character types: letters, special characters, and digits.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


class TagResourcesRequestTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the resource. You can specify up to 20 tag keys. The tag key cannot be an empty string.
        # 
        # A tag key can be up to 128 characters in length. It cannot start with acs: or aliyun, and cannot contain http:// or https://.
        self.key = key
        # The tag value of the resource. You can specify up to 20 tag values. The tag value can be an empty string.
        # 
        # A tag value can be up to 128 characters in length. It cannot start with acs: or aliyun, and cannot contain http:// or https://.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag: List[TagResourcesRequestTag] = None,
    ):
        # The region ID of the resources.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify a maximum of 20 resource IDs.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the resource. Instance resources are supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag list.
        # 
        # This parameter is required.
        self.tag = tag

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class TagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TagResourcesResponseBody = None,
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to remove all tags from the resource. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        # 
        # >If you specify both this parameter and the TagKey parameter, this parameter does not take effect.
        self.all = all
        # The ID of the region in which the resources are deployed.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can specify a maximum of 20 resource IDs.
        self.resource_id = resource_id
        # The type of the resources. Instance resources are supported.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The key of tag N added to the resource. Valid values of N: 1 to 20.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # The request ID.
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


class UntagResourcesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UntagResourcesResponseBody = None,
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateArtifactLifecycleRuleRequest(TeaModel):
    def __init__(
        self,
        auto: bool = None,
        enable_delete_tag: bool = None,
        instance_id: str = None,
        namespace_name: str = None,
        repo_name: str = None,
        retention_tag_count: int = None,
        rule_id: str = None,
        schedule_time: str = None,
        scope: str = None,
        tag_regexp: str = None,
    ):
        # Specifies whether to automatically execute the lifecycle management rule.
        self.auto = auto
        # Specifies whether to enable lifecycle management for the artifact.
        self.enable_delete_tag = enable_delete_tag
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        self.namespace_name = namespace_name
        # The name of the image repository.
        self.repo_name = repo_name
        # The number of images that you want to retain.
        self.retention_tag_count = retention_tag_count
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The execution cycle of the lifecycle management rule.
        self.schedule_time = schedule_time
        # The deletion scope of artifacts.
        self.scope = scope
        # The regular expression that indicates which image tags you want to retain.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto is not None:
            result['Auto'] = self.auto
        if self.enable_delete_tag is not None:
            result['EnableDeleteTag'] = self.enable_delete_tag
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.retention_tag_count is not None:
            result['RetentionTagCount'] = self.retention_tag_count
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.schedule_time is not None:
            result['ScheduleTime'] = self.schedule_time
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Auto') is not None:
            self.auto = m.get('Auto')
        if m.get('EnableDeleteTag') is not None:
            self.enable_delete_tag = m.get('EnableDeleteTag')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RetentionTagCount') is not None:
            self.retention_tag_count = m.get('RetentionTagCount')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('ScheduleTime') is not None:
            self.schedule_time = m.get('ScheduleTime')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class UpdateArtifactLifecycleRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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


class UpdateArtifactLifecycleRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateArtifactLifecycleRuleResponseBody = None,
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
            temp_model = UpdateArtifactLifecycleRuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateArtifactSubscriptionRuleRequest(TeaModel):
    def __init__(
        self,
        accelerate: str = None,
        instance_id: str = None,
        namespace_name: str = None,
        override: str = None,
        platform: List[str] = None,
        repo_name: str = None,
        rule_id: str = None,
        source_namespace_name: str = None,
        source_provider: str = None,
        source_repo_name: str = None,
        tag_count: int = None,
        tag_regexp: str = None,
    ):
        # Specifies whether to enable an acceleration link for image subscription. The subscription acceleration feature is in public preview. The feature is optimized based on scheduling policies and network links to accelerate image subscription.
        self.accelerate = accelerate
        # The instance ID.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the Container Registry namespace.
        self.namespace_name = namespace_name
        # Specifies whether to overwrite the original image.
        self.override = override
        # The operating system and architecture. If the source repository contains multi-arch images, only the images with the specified operating system and architecture are subscribed to the destination repository of the Enterprise Edition instance.
        self.platform = platform
        # The name of the Container Registry repository.
        self.repo_name = repo_name
        # The rule ID.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the source namespace.
        self.source_namespace_name = source_namespace_name
        # The source of the artifacts.
        # 
        # Valid values:
        # 
        # *   DOCKER_HUB: Docker Hub
        # *   GCR: GCR
        # *   QUAY: Quay.io
        self.source_provider = source_provider
        # The source repository.
        self.source_repo_name = source_repo_name
        # The number of subscribed images.
        self.tag_count = tag_count
        # The image tags in the subscription source repository. Regular expressions are supported.
        self.tag_regexp = tag_regexp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accelerate is not None:
            result['Accelerate'] = self.accelerate
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.namespace_name is not None:
            result['NamespaceName'] = self.namespace_name
        if self.override is not None:
            result['Override'] = self.override
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.repo_name is not None:
            result['RepoName'] = self.repo_name
        if self.rule_id is not None:
            result['RuleId'] = self.rule_id
        if self.source_namespace_name is not None:
            result['SourceNamespaceName'] = self.source_namespace_name
        if self.source_provider is not None:
            result['SourceProvider'] = self.source_provider
        if self.source_repo_name is not None:
            result['SourceRepoName'] = self.source_repo_name
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_regexp is not None:
            result['TagRegexp'] = self.tag_regexp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accelerate') is not None:
            self.accelerate = m.get('Accelerate')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        if m.get('Override') is not None:
            self.override = m.get('Override')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('RepoName') is not None:
            self.repo_name = m.get('RepoName')
        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')
        if m.get('SourceNamespaceName') is not None:
            self.source_namespace_name = m.get('SourceNamespaceName')
        if m.get('SourceProvider') is not None:
            self.source_provider = m.get('SourceProvider')
        if m.get('SourceRepoName') is not None:
            self.source_repo_name = m.get('SourceRepoName')
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagRegexp') is not None:
            self.tag_regexp = m.get('TagRegexp')
        return self


class UpdateArtifactSubscriptionRuleResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        is_success: bool = None,
        request_id: str = None,
    ):
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The request ID.
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


class UpdateArtifactSubscriptionRuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateArtifactSubscriptionRuleResponseBody = None,
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
            temp_model = UpdateArtifactSubscriptionRuleResponseBody()
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
        # The configuration of the delivery chain in the JSON format.
        # 
        # This parameter is required.
        self.chain_config = chain_config
        # The ID of the delivery chain.
        # 
        # This parameter is required.
        self.chain_id = chain_id
        # The description of the delivery chain.
        self.description = description
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the delivery chain.
        # 
        # This parameter is required.
        self.name = name
        # Repositories in which the delivery chain does not take effect.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to automatically create repositories in the namespace. Valid values:
        # 
        # *   `true`: automatically creates repositories in the namespace.
        # *   `false`: does not automatically create repositories in the namespace.
        self.auto_create_repo = auto_create_repo
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository
        # *   `PRIVATE`: a private repository
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the API request is successful. Valid values:
        # 
        # *   `true`: successful
        # *   `false`: failed
        self.is_success = is_success
        # The request ID.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the repository.
        # 
        # This parameter is required.
        self.repo_name = repo_name
        # The name of the namespace to which the repository belongs.
        # 
        # This parameter is required.
        self.repo_namespace_name = repo_namespace_name
        # The type of the repository. Valid values:
        # 
        # *   `PUBLIC`: a public repository.
        # *   `PRIVATE`: a private repository.
        self.repo_type = repo_type
        # The summary of the repository.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The event notification channel.
        self.event_channel = event_channel
        # The event configuration.
        self.event_config = event_config
        # The event scope. Valid values:
        # 
        # *   `INSTANCE`
        # *   `NAMESPACE`
        # *   `REPO`
        # 
        # Default value: `INSTANCE`
        self.event_scope = event_scope
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespaces to which the event notification rule applies.
        self.namespaces = namespaces
        # The names of the repositories to which the event notification rule applies.
        self.repo_names = repo_names
        # The regular expression for image tags.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The ID of the event notification rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the event notification rule.
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
        # The event notification channel.
        self.event_channel = event_channel
        # The event configuration.
        self.event_config = event_config
        # The event scope. Valid values:
        # 
        # *   `INSTANCE`
        # *   `NAMESPACE`
        # *   `REPO`
        # 
        # Default value: `INSTANCE`
        self.event_scope = event_scope
        # The type of the event. Valid values:
        # 
        # *   `cr:Artifact:DeliveryChainCompleted`: The delivery chain is processed.
        # *   `cr:Artifact:SynchronizationCompleted`: The image is replicated.
        # *   `cr:Artifact:BuildCompleted`: The image is built.
        # *   `cr:Artifact:ScanCompleted`: The image is scanned.
        # *   `cr:Artifact:SigningCompleted`: The image is signed.
        self.event_type = event_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The namespaces to which the event notification rule applies.
        self.namespaces_shrink = namespaces_shrink
        # The names of the repositories to which the event notification rule applies.
        self.repo_names_shrink = repo_names_shrink
        # The regular expression for image tags.
        self.repo_tag_filter_pattern = repo_tag_filter_pattern
        # The ID of the event notification rule.
        # 
        # This parameter is required.
        self.rule_id = rule_id
        # The name of the event notification rule.
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
        # The status code.
        self.code = code
        # The ID of the request.
        self.request_id = request_id
        # The ID of the event notification rule.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to enable the instance endpoint. Valid values:
        # 
        # *   `true`: enables the instance endpoint.
        # *   `false`: disables the instance endpoint
        # 
        # This parameter is required.
        self.enable = enable
        # The type of the endpoint. Set the value to Internet.
        # 
        # This parameter is required.
        self.endpoint_type = endpoint_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the module that you want to access. Valid values:
        # 
        # *   `Registry`: the image repository.
        # *   `Chart`: a Helm chart.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        default_repo_configuration: RepoConfiguration = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        # Specifies whether to automatically create a repository when an image is pushed to the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration = default_repo_configuration
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: The repository is a public repository.
        # *   `PRIVATE`: The repository is a private repository.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        if self.default_repo_configuration:
            self.default_repo_configuration.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_create_repo is not None:
            result['AutoCreateRepo'] = self.auto_create_repo
        if self.default_repo_configuration is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration.to_map()
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
        if m.get('DefaultRepoConfiguration') is not None:
            temp_model = RepoConfiguration()
            self.default_repo_configuration = temp_model.from_map(m['DefaultRepoConfiguration'])
        if m.get('DefaultRepoType') is not None:
            self.default_repo_type = m.get('DefaultRepoType')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NamespaceName') is not None:
            self.namespace_name = m.get('NamespaceName')
        return self


class UpdateNamespaceShrinkRequest(TeaModel):
    def __init__(
        self,
        auto_create_repo: bool = None,
        default_repo_configuration_shrink: str = None,
        default_repo_type: str = None,
        instance_id: str = None,
        namespace_name: str = None,
    ):
        # Specifies whether to automatically create a repository when an image is pushed to the namespace.
        self.auto_create_repo = auto_create_repo
        self.default_repo_configuration_shrink = default_repo_configuration_shrink
        # The default type of the repository. Valid values:
        # 
        # *   `PUBLIC`: The repository is a public repository.
        # *   `PRIVATE`: The repository is a private repository.
        self.default_repo_type = default_repo_type
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The name of the namespace.
        # 
        # This parameter is required.
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
        if self.default_repo_configuration_shrink is not None:
            result['DefaultRepoConfiguration'] = self.default_repo_configuration_shrink
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
        if m.get('DefaultRepoConfiguration') is not None:
            self.default_repo_configuration_shrink = m.get('DefaultRepoConfiguration')
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Building arguments.
        self.build_args = build_args
        # The ID of the building rule.
        # 
        # This parameter is required.
        self.build_rule_id = build_rule_id
        # The path of the Dockerfile.
        self.dockerfile_location = dockerfile_location
        # The name of the Dockerfile.
        self.dockerfile_name = dockerfile_name
        # The tag of the image.
        self.image_tag = image_tag
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Architecture for image building. Valid values:
        # 
        # *   `linux/amd64`
        # *   `linux/arm64`
        # *   `linux/386`
        # *   `linux/arm/v7`
        # *   `linux/arm/v6`
        # 
        # Default value: `linux/amd64`
        self.platforms = platforms
        # The name of the push that triggers the building rule.
        self.push_name = push_name
        # The type of the push that triggers the building rule. Valid values:
        # 
        # *   `GIT_TAG`: tag push
        # *   `GIT_BRANCH`: branch push
        self.push_type = push_type
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The ID of the building rule.
        self.build_rule_id = build_rule_id
        # The return value.
        self.code = code
        # Indicates whether the request is successful. Valid values:
        # 
        # *   `true`: The request is successful.
        # *   `false`: The request fails.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # Specifies whether to enable automatic image building when code is committed. Valid values:
        # 
        # *   `true`: enables automatic image building when code is committed.
        # *   `false`: disables automatic image building when code is committed.
        self.auto_build = auto_build
        # The ID of the source code repository.
        self.code_repo_id = code_repo_id
        # The name of the source code repository.
        # 
        # This parameter is required.
        self.code_repo_name = code_repo_name
        # The namespace to which the source code repository belongs.
        # 
        # This parameter is required.
        self.code_repo_namespace_name = code_repo_namespace_name
        # The type of the source code hosting platform. Valid values: GITHUB, GITLAB, GITEE, CODE, and CODEUP.
        # 
        # This parameter is required.
        self.code_repo_type = code_repo_type
        # Specifies whether to disable building caches. Valid values:
        # 
        # *   `true`: disables building caches.
        # *   `false`: enables building caches.
        self.disable_cache_build = disable_cache_build
        # The ID of the Container Registry Enterprise Edition instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # Specifies whether to enable Build With Servers Deployed Outside Chinese Mainland. Valid values:
        # 
        # *   `true`: enables Build With Servers Deployed Outside Chinese Mainland.
        # *   `false`: disables Build With Servers Deployed Outside Chinese Mainland.
        self.oversea_build = oversea_build
        # The ID of the image repository.
        # 
        # This parameter is required.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # The ID of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The ID of the image repository.
        # 
        # This parameter is required.
        self.repo_id = repo_id
        # The ID of the trigger.
        # 
        # This parameter is required.
        self.trigger_id = trigger_id
        # The name of the trigger.
        # 
        # You can specify the TriggerName or TriggerUrl parameter. The TriggerName parameter is optional.
        self.trigger_name = trigger_name
        # The image tag based on which the trigger is set.
        self.trigger_tag = trigger_tag
        # The type of the trigger. Valid values:
        # 
        # *   `ALL`: a trigger that supports both tags and regular expressions.
        # *   `TAG_LISTTAG`: a tag-based trigger.
        # *   `TAG_REG_EXP`: a regular expression-based trigger.
        self.trigger_type = trigger_type
        # The URL of the trigger.
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
        # The return value.
        self.code = code
        # Indicates whether the request is successful.
        self.is_success = is_success
        # The ID of the request.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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
        # This parameter is required.
        self.instance_id = instance_id
        self.repo_id = repo_id
        self.repo_name = repo_name
        self.repo_namespace_name = repo_namespace_name
        # This parameter is required.
        self.repo_type = repo_type
        # This parameter is required.
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
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
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


