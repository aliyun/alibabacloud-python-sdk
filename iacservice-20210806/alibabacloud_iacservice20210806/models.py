# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class JobStatusDetailValue(TeaModel):
    def __init__(
        self,
        comment: str = None,
        job_result: str = None,
        time_stamps: str = None,
    ):
        self.comment = comment
        self.job_result = job_result
        self.time_stamps = time_stamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        return self


class JobsStatusDetailValue(TeaModel):
    def __init__(
        self,
        job_result: str = None,
        comment: str = None,
        time_stamps: str = None,
    ):
        self.job_result = job_result
        self.comment = comment
        self.time_stamps = time_stamps

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_result is not None:
            result['jobResult'] = self.job_result
        if self.comment is not None:
            result['comment'] = self.comment
        if self.time_stamps is not None:
            result['timeStamps'] = self.time_stamps
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobResult') is not None:
            self.job_result = m.get('jobResult')
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('timeStamps') is not None:
            self.time_stamps = m.get('timeStamps')
        return self


class AddSharedAccountsRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        self.account_ids = account_ids
        self.resource_id = resource_id
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class AddSharedAccountsResponseBody(TeaModel):
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


class AddSharedAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSharedAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AddSharedAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        project_id: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        self.project_id = project_id
        # This parameter is required.
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class AssociateGroupResponseBody(TeaModel):
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


class AssociateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AssociateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class CancelResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CancelResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CancelResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequestNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class CreateGroupRequestTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        client_token: str = None,
        description: str = None,
        forced_setting: bool = None,
        name: str = None,
        notify_config: List[CreateGroupRequestNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        terraform_provider_version: str = None,
        trigger_config: List[CreateGroupRequestTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.forced_setting = forced_setting
        # This parameter is required.
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        # This parameter is required.
        self.project_id = project_id
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = CreateGroupRequestNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = CreateGroupRequestTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        request_id: str = None,
    ):
        self.group_id = group_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateJobRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        sub_command: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.description = description
        self.sub_command = sub_command
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class CreateJobResponseBody(TeaModel):
    def __init__(
        self,
        job_id: str = None,
        request_id: str = None,
    ):
        self.job_id = job_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateModuleRequestTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class CreateModuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_info: CreateModuleRequestGroupInfo = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        tags: List[CreateModuleRequestTags] = None,
        version_strategy: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.tags = tags
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = CreateModuleRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateModuleRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class CreateModuleResponseBody(TeaModel):
    def __init__(
        self,
        module_id: str = None,
        request_id: str = None,
    ):
        self.module_id = module_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateModuleVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        module_version: str = None,
        request_id: str = None,
    ):
        self.module_version = module_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        project_id: str = None,
        request_id: str = None,
    ):
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRegistryModuleRequest(TeaModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        type: str = None,
    ):
        self.acl = acl
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        # This parameter is required.
        self.module_name = module_name
        # This parameter is required.
        self.namespace_name = namespace_name
        self.provider = provider
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class CreateRegistryModuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        source: str = None,
    ):
        self.request_id = request_id
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.source is not None:
            result['source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('source') is not None:
            self.source = m.get('source')
        return self


class CreateRegistryModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRegistryModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRegistryModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRegistryNamespaceRequest(TeaModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
        maintainer: str = None,
        namespace_name: str = None,
    ):
        self.acl = acl
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.maintainer = maintainer
        # This parameter is required.
        self.namespace_name = namespace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.maintainer is not None:
            result['maintainer'] = self.maintainer
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('maintainer') is not None:
            self.maintainer = m.get('maintainer')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        return self


class CreateRegistryNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        namespace_name: str = None,
        request_id: str = None,
    ):
        self.namespace_name = namespace_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateRegistryNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRegistryNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateRegistryNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceExportTaskRequestExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class CreateResourceExportTaskRequestIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class CreateResourceExportTaskRequestVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class CreateResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        export_to_module: CreateResourceExportTaskRequestExportToModule = None,
        include_rules: List[CreateResourceExportTaskRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[CreateResourceExportTaskRequestVariables] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.export_to_module = export_to_module
        self.include_rules = include_rules
        # This parameter is required.
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exportToModule') is not None:
            temp_model = CreateResourceExportTaskRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = CreateResourceExportTaskRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = CreateResourceExportTaskRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class CreateResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class CreateResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTaskRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class CreateTaskRequestTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class CreateTaskRequestTaskBackend(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        object_path: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.object_path = object_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.object_path is not None:
            result['objectPath'] = self.object_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('objectPath') is not None:
            self.object_path = m.get('objectPath')
        return self


class CreateTaskRequest(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        client_token: str = None,
        description: str = None,
        group_info: CreateTaskRequestGroupInfo = None,
        init_module_state: bool = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        tags: List[CreateTaskRequestTags] = None,
        task_backend: CreateTaskRequestTaskBackend = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        # This parameter is required.
        self.module_id = module_id
        # This parameter is required.
        self.module_version = module_version
        # This parameter is required.
        self.name = name
        self.protection_strategy = protection_strategy
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.tags = tags
        self.task_backend = task_backend
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_backend:
            self.task_backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_backend is not None:
            result['taskBackend'] = self.task_backend.to_map()
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = CreateTaskRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = CreateTaskRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskBackend') is not None:
            temp_model = CreateTaskRequestTaskBackend()
            self.task_backend = temp_model.from_map(m['taskBackend'])
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class CreateTaskResponseBody(TeaModel):
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
            result['requestId'] = self.request_id
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class CreateTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupResponseBody(TeaModel):
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


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteModuleResponseBody(TeaModel):
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


class DeleteModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectResponseBody(TeaModel):
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


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistryModuleResponseBody(TeaModel):
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


class DeleteRegistryModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRegistryModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRegistryModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistryModuleVersionResponseBody(TeaModel):
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


class DeleteRegistryModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRegistryModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRegistryModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRegistryNamespaceResponseBody(TeaModel):
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


class DeleteRegistryNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteRegistryNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteRegistryNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceExportTaskResponseBody(TeaModel):
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


class DeleteResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteTaskResponseBody(TeaModel):
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


class DeleteTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DissociateGroupRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        resource_ids: List[str] = None,
        resource_type: str = None,
    ):
        self.client_token = client_token
        # This parameter is required.
        self.resource_ids = resource_ids
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.resource_ids is not None:
            result['resourceIds'] = self.resource_ids
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('resourceIds') is not None:
            self.resource_ids = m.get('resourceIds')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class DissociateGroupResponseBody(TeaModel):
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


class DissociateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DissociateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DissociateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteRegistryModuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        parameters: Dict[str, Any] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.parameters is not None:
            result['parameters'] = self.parameters
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        return self


class ExecuteRegistryModuleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteRegistryModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteRegistryModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteRegistryModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        return self


class ExecuteResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ExecuteResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTerraformApplyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        state_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.code = code
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code is not None:
            result['code'] = self.code
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformApplyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformApplyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTerraformApplyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteTerraformApplyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTerraformDestroyRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        state_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformDestroyResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformDestroyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTerraformDestroyResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteTerraformDestroyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteTerraformPlanRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        state_id: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.code = code
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code is not None:
            result['code'] = self.code
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformPlanResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        state_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.state_id = state_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.state_id is not None:
            result['stateId'] = self.state_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('stateId') is not None:
            self.state_id = m.get('stateId')
        return self


class ExecuteTerraformPlanResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteTerraformPlanResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ExecuteTerraformPlanResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetExecuteStateResponseBody(TeaModel):
    def __init__(
        self,
        error_message: str = None,
        log_file: Dict[str, Any] = None,
        request_id: str = None,
        state: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.log_file = log_file
        # Id of the request
        self.request_id = request_id
        self.state = state
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_message is not None:
            result['errorMessage'] = self.error_message
        if self.log_file is not None:
            result['logFile'] = self.log_file
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.state is not None:
            result['state'] = self.state
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorMessage') is not None:
            self.error_message = m.get('errorMessage')
        if m.get('logFile') is not None:
            self.log_file = m.get('logFile')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetExecuteStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetExecuteStateResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetExecuteStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupResponseBodyGroupNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class GetGroupResponseBodyGroupTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class GetGroupResponseBodyGroup(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        create_time: str = None,
        description: str = None,
        forced_setting: bool = None,
        group_id: str = None,
        name: str = None,
        notify_config: List[GetGroupResponseBodyGroupNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        project_id: str = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        task_cnt: int = None,
        terraform_provider_version: str = None,
        trigger_config: List[GetGroupResponseBodyGroupTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        self.create_time = create_time
        self.description = description
        self.forced_setting = forced_setting
        self.group_id = group_id
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        self.project_id = project_id
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.task_cnt = task_cnt
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = GetGroupResponseBodyGroupNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = GetGroupResponseBodyGroupTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class GetGroupResponseBody(TeaModel):
    def __init__(
        self,
        group: GetGroupResponseBodyGroup = None,
        request_id: str = None,
    ):
        self.group = group
        self.request_id = request_id

    def validate(self):
        if self.group:
            self.group.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group is not None:
            result['group'] = self.group.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            temp_model = GetGroupResponseBodyGroup()
            self.group = temp_model.from_map(m['group'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        task_type: str = None,
    ):
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class GetJobResponseBodyJobAssertCheckDetail(TeaModel):
    def __init__(
        self,
        comparison: str = None,
        expected_value: str = None,
        is_pass: bool = None,
        type: str = None,
    ):
        self.comparison = comparison
        self.expected_value = expected_value
        self.is_pass = is_pass
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comparison is not None:
            result['comparison'] = self.comparison
        if self.expected_value is not None:
            result['expectedValue'] = self.expected_value
        if self.is_pass is not None:
            result['isPass'] = self.is_pass
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comparison') is not None:
            self.comparison = m.get('comparison')
        if m.get('expectedValue') is not None:
            self.expected_value = m.get('expectedValue')
        if m.get('isPass') is not None:
            self.is_pass = m.get('isPass')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetJobResponseBodyJobConfig(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        is_destroy: bool = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        self.auto_apply = auto_apply
        self.is_destroy = is_destroy
        self.module_version = module_version
        self.resources_changed = resources_changed
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        return self


class GetJobResponseBodyJob(TeaModel):
    def __init__(
        self,
        assert_check_detail: List[GetJobResponseBodyJobAssertCheckDetail] = None,
        config: GetJobResponseBodyJobConfig = None,
        create_time: str = None,
        description: str = None,
        download_url: Dict[str, Any] = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        log_file: Dict[str, Any] = None,
        output: str = None,
        output_json_plan: Any = None,
        parameters: Dict[str, str] = None,
        status: str = None,
        status_detail: Dict[str, JobStatusDetailValue] = None,
        task_id: str = None,
        task_type: str = None,
        terraform_provider_version: str = None,
    ):
        self.assert_check_detail = assert_check_detail
        self.config = config
        self.create_time = create_time
        self.description = description
        self.download_url = download_url
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.log_file = log_file
        self.output = output
        self.output_json_plan = output_json_plan
        self.parameters = parameters
        self.status = status
        self.status_detail = status_detail
        self.task_id = task_id
        self.task_type = task_type
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.assert_check_detail:
            for k in self.assert_check_detail:
                if k:
                    k.validate()
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['assertCheckDetail'] = []
        if self.assert_check_detail is not None:
            for k in self.assert_check_detail:
                result['assertCheckDetail'].append(k.to_map() if k else None)
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.download_url is not None:
            result['downloadUrl'] = self.download_url
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.log_file is not None:
            result['logFile'] = self.log_file
        if self.output is not None:
            result['output'] = self.output
        if self.output_json_plan is not None:
            result['outputJsonPlan'] = self.output_json_plan
        if self.parameters is not None:
            result['parameters'] = self.parameters
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assert_check_detail = []
        if m.get('assertCheckDetail') is not None:
            for k in m.get('assertCheckDetail'):
                temp_model = GetJobResponseBodyJobAssertCheckDetail()
                self.assert_check_detail.append(temp_model.from_map(k))
        if m.get('config') is not None:
            temp_model = GetJobResponseBodyJobConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('downloadUrl') is not None:
            self.download_url = m.get('downloadUrl')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('logFile') is not None:
            self.log_file = m.get('logFile')
        if m.get('output') is not None:
            self.output = m.get('output')
        if m.get('outputJsonPlan') is not None:
            self.output_json_plan = m.get('outputJsonPlan')
        if m.get('parameters') is not None:
            self.parameters = m.get('parameters')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        job: GetJobResponseBodyJob = None,
        request_id: str = None,
    ):
        self.job = job
        self.request_id = request_id

    def validate(self):
        if self.job:
            self.job.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.job is not None:
            result['job'] = self.job.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('job') is not None:
            temp_model = GetJobResponseBodyJob()
            self.job = temp_model.from_map(m['job'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleResponseBodyModuleGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class GetModuleResponseBodyModuleTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class GetModuleResponseBodyModule(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_info: GetModuleResponseBodyModuleGroupInfo = None,
        latest_version: str = None,
        module_id: str = None,
        name: str = None,
        output_path: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        status: str = None,
        tags: List[GetModuleResponseBodyModuleTags] = None,
        version_strategy: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_info = group_info
        self.latest_version = latest_version
        self.module_id = module_id
        self.name = name
        self.output_path = output_path
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.status = status
        self.tags = tags
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
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
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.output_path is not None:
            result['outputPath'] = self.output_path
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = GetModuleResponseBodyModuleGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('outputPath') is not None:
            self.output_path = m.get('outputPath')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetModuleResponseBodyModuleTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleResponseBody(TeaModel):
    def __init__(
        self,
        module: GetModuleResponseBodyModule = None,
        request_id: str = None,
    ):
        self.module = module
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.module:
            self.module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module is not None:
            result['module'] = self.module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('module') is not None:
            temp_model = GetModuleResponseBodyModule()
            self.module = temp_model.from_map(m['module'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetModuleVersionResponseBodyVersion(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
        terraform_context: Dict[str, Any] = None,
        version_strategy: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.source = source
        self.source_path = source_path
        self.state_path = state_path
        self.terraform_context = terraform_context
        self.version_strategy = version_strategy

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class GetModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: GetModuleVersionResponseBodyVersion = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        if self.version:
            self.version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.version is not None:
            result['version'] = self.version.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('version') is not None:
            temp_model = GetModuleVersionResponseBodyVersion()
            self.version = temp_model.from_map(m['version'])
        return self


class GetModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetProjectResponseBodyProject(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.task_cnt = task_cnt

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class GetProjectResponseBody(TeaModel):
    def __init__(
        self,
        project: GetProjectResponseBodyProject = None,
        request_id: str = None,
    ):
        self.project = project
        self.request_id = request_id

    def validate(self):
        if self.project:
            self.project.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project is not None:
            result['project'] = self.project.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('project') is not None:
            temp_model = GetProjectResponseBodyProject()
            self.project = temp_model.from_map(m['project'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegistryModuleResponseBodyRegistryModule(TeaModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        downloads: int = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        shared_accounts: List[int] = None,
        source: str = None,
        source_url: str = None,
        type: str = None,
        version: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.downloads = downloads
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.shared_accounts = shared_accounts
        self.source = source
        self.source_url = source_url
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.downloads is not None:
            result['downloads'] = self.downloads
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts
        if self.source is not None:
            result['source'] = self.source
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetRegistryModuleResponseBody(TeaModel):
    def __init__(
        self,
        registry_module: GetRegistryModuleResponseBodyRegistryModule = None,
        request_id: str = None,
    ):
        self.registry_module = registry_module
        self.request_id = request_id

    def validate(self):
        if self.registry_module:
            self.registry_module.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.registry_module is not None:
            result['registryModule'] = self.registry_module.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('registryModule') is not None:
            temp_model = GetRegistryModuleResponseBodyRegistryModule()
            self.registry_module = temp_model.from_map(m['registryModule'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRegistryModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegistryModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegistryModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegistryModuleVersionResponseBodyModuleVersion(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        detail_url: str = None,
        downloads: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        source: str = None,
        source_url: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.detail_url = detail_url
        self.downloads = downloads
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.source = source
        self.source_url = source_url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.detail_url is not None:
            result['detailUrl'] = self.detail_url
        if self.downloads is not None:
            result['downloads'] = self.downloads
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.source is not None:
            result['source'] = self.source
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('detailUrl') is not None:
            self.detail_url = m.get('detailUrl')
        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetRegistryModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        module_version: GetRegistryModuleVersionResponseBodyModuleVersion = None,
        request_id: str = None,
    ):
        self.module_version = module_version
        self.request_id = request_id

    def validate(self):
        if self.module_version:
            self.module_version.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleVersion') is not None:
            temp_model = GetRegistryModuleVersionResponseBodyModuleVersion()
            self.module_version = temp_model.from_map(m['moduleVersion'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRegistryModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegistryModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegistryModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRegistryNamespaceResponseBodyNamespace(TeaModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        maintainer: str = None,
        modules: int = None,
        namespace_name: str = None,
        shared_accounts: List[int] = None,
        type: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.maintainer = maintainer
        self.modules = modules
        self.namespace_name = namespace_name
        self.shared_accounts = shared_accounts
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.maintainer is not None:
            result['maintainer'] = self.maintainer
        if self.modules is not None:
            result['modules'] = self.modules
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('maintainer') is not None:
            self.maintainer = m.get('maintainer')
        if m.get('modules') is not None:
            self.modules = m.get('modules')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetRegistryNamespaceResponseBody(TeaModel):
    def __init__(
        self,
        namespace: GetRegistryNamespaceResponseBodyNamespace = None,
        request_id: str = None,
    ):
        self.namespace = namespace
        self.request_id = request_id

    def validate(self):
        if self.namespace:
            self.namespace.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace is not None:
            result['namespace'] = self.namespace.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespace') is not None:
            temp_model = GetRegistryNamespaceResponseBodyNamespace()
            self.namespace = temp_model.from_map(m['namespace'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class GetRegistryNamespaceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRegistryNamespaceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetRegistryNamespaceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceExportTaskRequest(TeaModel):
    def __init__(
        self,
        export_version: str = None,
    ):
        self.export_version = export_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        return self


class GetResourceExportTaskResponseBodyTaskExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class GetResourceExportTaskResponseBodyTaskIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class GetResourceExportTaskResponseBodyTaskModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class GetResourceExportTaskResponseBodyTaskVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class GetResourceExportTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_task_id: str = None,
        export_to_module: GetResourceExportTaskResponseBodyTaskExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        include_rules: List[GetResourceExportTaskResponseBodyTaskIncludeRules] = None,
        modules: List[GetResourceExportTaskResponseBodyTaskModules] = None,
        name: str = None,
        ram_role: str = None,
        status: str = None,
        task_output_path: str = None,
        terraform_context: Dict[str, Any] = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[GetResourceExportTaskResponseBodyTaskVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.failed_reason = failed_reason
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.ram_role = ram_role
        self.status = status
        self.task_output_path = task_output_path
        self.terraform_context = terraform_context
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.status is not None:
            result['status'] = self.status
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_context is not None:
            result['terraformContext'] = self.terraform_context
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = GetResourceExportTaskResponseBodyTaskExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = GetResourceExportTaskResponseBodyTaskIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = GetResourceExportTaskResponseBodyTaskModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformContext') is not None:
            self.terraform_context = m.get('terraformContext')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = GetResourceExportTaskResponseBodyTaskVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class GetResourceExportTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetResourceExportTaskResponseBodyTask = None,
    ):
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetResourceExportTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetResourceExportTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceExportTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceExportTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetResourceTypeRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        filter_read_only: bool = None,
        terraform_provider_version: str = None,
    ):
        self.accept_language = accept_language
        self.filter_read_only = filter_read_only
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.filter_read_only is not None:
            result['filterReadOnly'] = self.filter_read_only
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('filterReadOnly') is not None:
            self.filter_read_only = m.get('filterReadOnly')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class GetResourceTypeResponseBodyResourceTypeOperations(TeaModel):
    def __init__(
        self,
        api_name: str = None,
        api_version: str = None,
        operation_type: str = None,
        service_code: str = None,
    ):
        self.api_name = api_name
        self.api_version = api_version
        self.operation_type = operation_type
        # serviceCode
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_name is not None:
            result['apiName'] = self.api_name
        if self.api_version is not None:
            result['apiVersion'] = self.api_version
        if self.operation_type is not None:
            result['operationType'] = self.operation_type
        if self.service_code is not None:
            result['serviceCode'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('apiName') is not None:
            self.api_name = m.get('apiName')
        if m.get('apiVersion') is not None:
            self.api_version = m.get('apiVersion')
        if m.get('operationType') is not None:
            self.operation_type = m.get('operationType')
        if m.get('serviceCode') is not None:
            self.service_code = m.get('serviceCode')
        return self


class GetResourceTypeResponseBodyResourceType(TeaModel):
    def __init__(
        self,
        description: str = None,
        operations: List[GetResourceTypeResponseBodyResourceTypeOperations] = None,
        product: str = None,
        product_name: str = None,
        product_name_en: str = None,
        properties: Dict[str, Any] = None,
        resource_detail_page_url: str = None,
        resource_list_page_url: str = None,
        status: str = None,
        status_start_version: str = None,
        subcategory: str = None,
        support_exported: bool = None,
        terraform_provider_version: str = None,
        terraform_resource_type: str = None,
        title: str = None,
    ):
        self.description = description
        self.operations = operations
        self.product = product
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.properties = properties
        self.resource_detail_page_url = resource_detail_page_url
        self.resource_list_page_url = resource_list_page_url
        self.status = status
        self.status_start_version = status_start_version
        self.subcategory = subcategory
        self.support_exported = support_exported
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_type = terraform_resource_type
        self.title = title

    def validate(self):
        if self.operations:
            for k in self.operations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        result['operations'] = []
        if self.operations is not None:
            for k in self.operations:
                result['operations'].append(k.to_map() if k else None)
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_name_en is not None:
            result['productNameEn'] = self.product_name_en
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_detail_page_url is not None:
            result['resourceDetailPageUrl'] = self.resource_detail_page_url
        if self.resource_list_page_url is not None:
            result['resourceListPageUrl'] = self.resource_list_page_url
        if self.status is not None:
            result['status'] = self.status
        if self.status_start_version is not None:
            result['statusStartVersion'] = self.status_start_version
        if self.subcategory is not None:
            result['subcategory'] = self.subcategory
        if self.support_exported is not None:
            result['supportExported'] = self.support_exported
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        self.operations = []
        if m.get('operations') is not None:
            for k in m.get('operations'):
                temp_model = GetResourceTypeResponseBodyResourceTypeOperations()
                self.operations.append(temp_model.from_map(k))
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productNameEn') is not None:
            self.product_name_en = m.get('productNameEn')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceDetailPageUrl') is not None:
            self.resource_detail_page_url = m.get('resourceDetailPageUrl')
        if m.get('resourceListPageUrl') is not None:
            self.resource_list_page_url = m.get('resourceListPageUrl')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStartVersion') is not None:
            self.status_start_version = m.get('statusStartVersion')
        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')
        if m.get('supportExported') is not None:
            self.support_exported = m.get('supportExported')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class GetResourceTypeResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        resource_type: GetResourceTypeResponseBodyResourceType = None,
    ):
        self.request_id = request_id
        self.resource_type = resource_type

    def validate(self):
        if self.resource_type:
            self.resource_type.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceType') is not None:
            temp_model = GetResourceTypeResponseBodyResourceType()
            self.resource_type = temp_model.from_map(m['resourceType'])
        return self


class GetResourceTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetResourceTypeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetResourceTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResponseBodyTaskGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class GetTaskResponseBodyTaskTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class GetTaskResponseBodyTaskTaskBackend(TeaModel):
    def __init__(
        self,
        bucket_endpoint: str = None,
        bucket_name: str = None,
        object_path: str = None,
    ):
        self.bucket_endpoint = bucket_endpoint
        self.bucket_name = bucket_name
        self.object_path = object_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_endpoint is not None:
            result['bucketEndpoint'] = self.bucket_endpoint
        if self.bucket_name is not None:
            result['bucketName'] = self.bucket_name
        if self.object_path is not None:
            result['objectPath'] = self.object_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucketEndpoint') is not None:
            self.bucket_endpoint = m.get('bucketEndpoint')
        if m.get('bucketName') is not None:
            self.bucket_name = m.get('bucketName')
        if m.get('objectPath') is not None:
            self.object_path = m.get('objectPath')
        return self


class GetTaskResponseBodyTask(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        description: str = None,
        group_info: GetTaskResponseBodyTaskGroupInfo = None,
        init_module_state: bool = None,
        latest_module_version: str = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        status: str = None,
        tags: List[GetTaskResponseBodyTaskTags] = None,
        task_backend: GetTaskResponseBodyTaskTaskBackend = None,
        task_id: str = None,
        task_output_path: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.current_job_status = current_job_status
        self.deletion_protection = deletion_protection
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        self.latest_module_version = latest_module_version
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.protection_strategy = protection_strategy
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.status = status
        self.tags = tags
        self.task_backend = task_backend
        self.task_id = task_id
        self.task_output_path = task_output_path
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()
        if self.task_backend:
            self.task_backend.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.latest_module_version is not None:
            result['latestModuleVersion'] = self.latest_module_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_backend is not None:
            result['taskBackend'] = self.task_backend.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.task_output_path is not None:
            result['taskOutputPath'] = self.task_output_path
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = GetTaskResponseBodyTaskGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('latestModuleVersion') is not None:
            self.latest_module_version = m.get('latestModuleVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = GetTaskResponseBodyTaskTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskBackend') is not None:
            temp_model = GetTaskResponseBodyTaskTaskBackend()
            self.task_backend = temp_model.from_map(m['taskBackend'])
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('taskOutputPath') is not None:
            self.task_output_path = m.get('taskOutputPath')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class GetTaskResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task: GetTaskResponseBodyTask = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.task = task

    def validate(self):
        if self.task:
            self.task.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.task is not None:
            result['task'] = self.task.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('task') is not None:
            temp_model = GetTaskResponseBodyTask()
            self.task = temp_model.from_map(m['task'])
        return self


class GetTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExplorerRegistryModuleExamplesRequest(TeaModel):
    def __init__(
        self,
        example_name: str = None,
        keyword: str = None,
        max_results: int = None,
        module_name: str = None,
        module_version: str = None,
        namespace_name: str = None,
        next_token: str = None,
    ):
        self.example_name = example_name
        self.keyword = keyword
        self.max_results = max_results
        self.module_name = module_name
        self.module_version = module_version
        self.namespace_name = namespace_name
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.example_name is not None:
            result['exampleName'] = self.example_name
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exampleName') is not None:
            self.example_name = m.get('exampleName')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples(TeaModel):
    def __init__(
        self,
        example_name: str = None,
        example_path: str = None,
        example_schema: Dict[str, Any] = None,
        module_name: str = None,
        module_version: str = None,
        namespace_name: str = None,
        status: str = None,
    ):
        self.example_name = example_name
        self.example_path = example_path
        self.example_schema = example_schema
        self.module_name = module_name
        self.module_version = module_version
        self.namespace_name = namespace_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.example_name is not None:
            result['exampleName'] = self.example_name
        if self.example_path is not None:
            result['examplePath'] = self.example_path
        if self.example_schema is not None:
            result['exampleSchema'] = self.example_schema
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exampleName') is not None:
            self.example_name = m.get('exampleName')
        if m.get('examplePath') is not None:
            self.example_path = m.get('examplePath')
        if m.get('exampleSchema') is not None:
            self.example_schema = m.get('exampleSchema')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListExplorerRegistryModuleExamplesResponseBody(TeaModel):
    def __init__(
        self,
        explorer_registry_module_examples: List[ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_module_examples = explorer_registry_module_examples
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_module_examples:
            for k in self.explorer_registry_module_examples:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['explorerRegistryModuleExamples'] = []
        if self.explorer_registry_module_examples is not None:
            for k in self.explorer_registry_module_examples:
                result['explorerRegistryModuleExamples'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.explorer_registry_module_examples = []
        if m.get('explorerRegistryModuleExamples') is not None:
            for k in m.get('explorerRegistryModuleExamples'):
                temp_model = ListExplorerRegistryModuleExamplesResponseBodyExplorerRegistryModuleExamples()
                self.explorer_registry_module_examples.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListExplorerRegistryModuleExamplesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExplorerRegistryModuleExamplesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExplorerRegistryModuleExamplesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExplorerRegistryModuleVersionsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        module_name: str = None,
        module_version: str = None,
        namespace_name: str = None,
        next_token: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.module_name = module_name
        self.module_version = module_version
        self.namespace_name = namespace_name
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions(TeaModel):
    def __init__(
        self,
        module_detail: Dict[str, Any] = None,
        module_file: Dict[str, Any] = None,
        module_name: str = None,
        namespace_name: str = None,
        properties: Dict[str, Any] = None,
        source: str = None,
        version: str = None,
    ):
        self.module_detail = module_detail
        self.module_file = module_file
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.properties = properties
        self.source = source
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.module_detail is not None:
            result['moduleDetail'] = self.module_detail
        if self.module_file is not None:
            result['moduleFile'] = self.module_file
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.properties is not None:
            result['properties'] = self.properties
        if self.source is not None:
            result['source'] = self.source
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('moduleDetail') is not None:
            self.module_detail = m.get('moduleDetail')
        if m.get('moduleFile') is not None:
            self.module_file = m.get('moduleFile')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListExplorerRegistryModuleVersionsResponseBody(TeaModel):
    def __init__(
        self,
        explorer_registry_module_versions: List[ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_module_versions = explorer_registry_module_versions
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_module_versions:
            for k in self.explorer_registry_module_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['explorerRegistryModuleVersions'] = []
        if self.explorer_registry_module_versions is not None:
            for k in self.explorer_registry_module_versions:
                result['explorerRegistryModuleVersions'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.explorer_registry_module_versions = []
        if m.get('explorerRegistryModuleVersions') is not None:
            for k in m.get('explorerRegistryModuleVersions'):
                temp_model = ListExplorerRegistryModuleVersionsResponseBodyExplorerRegistryModuleVersions()
                self.explorer_registry_module_versions.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListExplorerRegistryModuleVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExplorerRegistryModuleVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExplorerRegistryModuleVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListExplorerRegistryModulesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        module_name: str = None,
        next_token: str = None,
        sort: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.module_name = module_name
        self.next_token = next_token
        self.sort = sort

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.sort is not None:
            result['sort'] = self.sort
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        return self


class ListExplorerRegistryModulesResponseBodyExplorerRegistryModules(TeaModel):
    def __init__(
        self,
        description: str = None,
        downloads: int = None,
        latest_version: str = None,
        module_name: str = None,
        namespace_name: str = None,
        source: str = None,
        status: str = None,
    ):
        self.description = description
        self.downloads = downloads
        self.latest_version = latest_version
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.source = source
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.downloads is not None:
            result['downloads'] = self.downloads
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListExplorerRegistryModulesResponseBody(TeaModel):
    def __init__(
        self,
        explorer_registry_modules: List[ListExplorerRegistryModulesResponseBodyExplorerRegistryModules] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.explorer_registry_modules = explorer_registry_modules
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.explorer_registry_modules:
            for k in self.explorer_registry_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['explorerRegistryModules'] = []
        if self.explorer_registry_modules is not None:
            for k in self.explorer_registry_modules:
                result['explorerRegistryModules'].append(k.to_map() if k else None)
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.explorer_registry_modules = []
        if m.get('explorerRegistryModules') is not None:
            for k in m.get('explorerRegistryModules'):
                temp_model = ListExplorerRegistryModulesResponseBodyExplorerRegistryModules()
                self.explorer_registry_modules.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListExplorerRegistryModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListExplorerRegistryModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListExplorerRegistryModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequestTag(TeaModel):
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


class ListGroupRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: str = None,
        tag: List[ListGroupRequestTag] = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListGroupRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        project_id: str = None,
        tag_shrink: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListGroupResponseBodyGroupsTags(TeaModel):
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


class ListGroupResponseBodyGroups(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        group_id: str = None,
        is_default: bool = None,
        module_cnt: int = None,
        name: str = None,
        project_id: str = None,
        scene_testing_task_cnt: int = None,
        tags: List[ListGroupResponseBodyGroupsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.group_id = group_id
        self.is_default = is_default
        self.module_cnt = module_cnt
        self.name = name
        self.project_id = project_id
        self.scene_testing_task_cnt = scene_testing_task_cnt
        self.tags = tags
        self.task_cnt = task_cnt

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
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.is_default is not None:
            result['isDefault'] = self.is_default
        if self.module_cnt is not None:
            result['moduleCnt'] = self.module_cnt
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.scene_testing_task_cnt is not None:
            result['sceneTestingTaskCnt'] = self.scene_testing_task_cnt
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('isDefault') is not None:
            self.is_default = m.get('isDefault')
        if m.get('moduleCnt') is not None:
            self.module_cnt = m.get('moduleCnt')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('sceneTestingTaskCnt') is not None:
            self.scene_testing_task_cnt = m.get('sceneTestingTaskCnt')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListGroupResponseBodyGroupsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListGroupResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        groups: List[ListGroupResponseBodyGroups] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
    ):
        self.count = count
        self.groups = groups
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = ListGroupResponseBodyGroups()
                self.groups.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListJobsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
        task_type: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.status = status
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class ListJobsResponseBodyJobsConfig(TeaModel):
    def __init__(
        self,
        is_destroy: bool = None,
        module_description: str = None,
        module_version: str = None,
        resources_changed: str = None,
        sub_command: str = None,
    ):
        self.is_destroy = is_destroy
        self.module_description = module_description
        self.module_version = module_version
        self.resources_changed = resources_changed
        self.sub_command = sub_command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_destroy is not None:
            result['isDestroy'] = self.is_destroy
        if self.module_description is not None:
            result['moduleDescription'] = self.module_description
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.resources_changed is not None:
            result['resourcesChanged'] = self.resources_changed
        if self.sub_command is not None:
            result['subCommand'] = self.sub_command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isDestroy') is not None:
            self.is_destroy = m.get('isDestroy')
        if m.get('moduleDescription') is not None:
            self.module_description = m.get('moduleDescription')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('resourcesChanged') is not None:
            self.resources_changed = m.get('resourcesChanged')
        if m.get('subCommand') is not None:
            self.sub_command = m.get('subCommand')
        return self


class ListJobsResponseBodyJobs(TeaModel):
    def __init__(
        self,
        config: ListJobsResponseBodyJobsConfig = None,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        execute_type: str = None,
        is_pass_assert_check: bool = None,
        job_id: str = None,
        status: str = None,
        status_detail: Dict[str, JobsStatusDetailValue] = None,
        task_id: str = None,
        terraform_provider_version: str = None,
    ):
        self.config = config
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.execute_type = execute_type
        self.is_pass_assert_check = is_pass_assert_check
        self.job_id = job_id
        self.status = status
        self.status_detail = status_detail
        self.task_id = task_id
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        if self.config:
            self.config.validate()
        if self.status_detail:
            for v in self.status_detail.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['config'] = self.config.to_map()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.execute_type is not None:
            result['executeType'] = self.execute_type
        if self.is_pass_assert_check is not None:
            result['isPassAssertCheck'] = self.is_pass_assert_check
        if self.job_id is not None:
            result['jobId'] = self.job_id
        if self.status is not None:
            result['status'] = self.status
        result['statusDetail'] = {}
        if self.status_detail is not None:
            for k, v in self.status_detail.items():
                result['statusDetail'][k] = v.to_map()
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            temp_model = ListJobsResponseBodyJobsConfig()
            self.config = temp_model.from_map(m['config'])
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('executeType') is not None:
            self.execute_type = m.get('executeType')
        if m.get('isPassAssertCheck') is not None:
            self.is_pass_assert_check = m.get('isPassAssertCheck')
        if m.get('jobId') is not None:
            self.job_id = m.get('jobId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.status_detail = {}
        if m.get('statusDetail') is not None:
            for k, v in m.get('statusDetail').items():
                temp_model = JobsStatusDetailValue()
                self.status_detail[k] = temp_model.from_map(v)
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class ListJobsResponseBody(TeaModel):
    def __init__(
        self,
        jobs: List[ListJobsResponseBodyJobs] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.jobs = jobs
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

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
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.jobs = []
        if m.get('jobs') is not None:
            for k in m.get('jobs'):
                temp_model = ListJobsResponseBodyJobs()
                self.jobs.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListJobsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListJobsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListJobsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModuleVersionRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListModuleVersionResponseBodyVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        module_id: str = None,
        module_version: str = None,
        name: str = None,
        source_path: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.module_id = module_id
        self.module_version = module_version
        self.name = name
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        return self


class ListModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[ListModuleVersionResponseBodyVersions] = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count
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
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListModuleVersionResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListModulesRequestTag(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListModulesRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag: List[ListModulesRequestTag] = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_name = module_name
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListModulesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListModulesShrinkRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_name: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        tag_shrink: str = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_name = module_name
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListModulesResponseBodyModulesGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListModulesResponseBodyModulesTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
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
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListModulesResponseBodyModules(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        deletion_protection: bool = None,
        description: str = None,
        group_info: ListModulesResponseBodyModulesGroupInfo = None,
        latest_version: str = None,
        module_id: str = None,
        name: str = None,
        source: str = None,
        status: str = None,
        tags: List[ListModulesResponseBodyModulesTags] = None,
    ):
        self.create_time = create_time
        self.deletion_protection = deletion_protection
        self.description = description
        self.group_info = group_info
        self.latest_version = latest_version
        self.module_id = module_id
        self.name = name
        self.source = source
        self.status = status
        self.tags = tags

    def validate(self):
        if self.group_info:
            self.group_info.validate()
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
            result['createTime'] = self.create_time
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.latest_version is not None:
            result['latestVersion'] = self.latest_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.name is not None:
            result['name'] = self.name
        if self.source is not None:
            result['source'] = self.source
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = ListModulesResponseBodyModulesGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('latestVersion') is not None:
            self.latest_version = m.get('latestVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListModulesResponseBodyModulesTags()
                self.tags.append(temp_model.from_map(k))
        return self


class ListModulesResponseBody(TeaModel):
    def __init__(
        self,
        modules: List[ListModulesResponseBodyModules] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.modules = modules
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListModulesResponseBodyModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProductsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        sort: str = None,
        status: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.sort = sort
        self.status = status
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.sort is not None:
            result['sort'] = self.sort
        if self.status is not None:
            result['status'] = self.status
        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class ListProductsResponseBodyProducts(TeaModel):
    def __init__(
        self,
        first_category_name: str = None,
        first_category_name_en: str = None,
        product: str = None,
        product_name: str = None,
        product_name_en: str = None,
        second_category_name: str = None,
        second_category_name_en: str = None,
        status: str = None,
        subcategory: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
    ):
        self.first_category_name = first_category_name
        self.first_category_name_en = first_category_name_en
        self.product = product
        self.product_name = product_name
        self.product_name_en = product_name_en
        self.second_category_name = second_category_name
        self.second_category_name_en = second_category_name_en
        self.status = status
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.first_category_name is not None:
            result['firstCategoryName'] = self.first_category_name
        if self.first_category_name_en is not None:
            result['firstCategoryNameEn'] = self.first_category_name_en
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.product_name_en is not None:
            result['productNameEn'] = self.product_name_en
        if self.second_category_name is not None:
            result['secondCategoryName'] = self.second_category_name
        if self.second_category_name_en is not None:
            result['secondCategoryNameEn'] = self.second_category_name_en
        if self.status is not None:
            result['status'] = self.status
        if self.subcategory is not None:
            result['subcategory'] = self.subcategory
        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('firstCategoryName') is not None:
            self.first_category_name = m.get('firstCategoryName')
        if m.get('firstCategoryNameEn') is not None:
            self.first_category_name_en = m.get('firstCategoryNameEn')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('productNameEn') is not None:
            self.product_name_en = m.get('productNameEn')
        if m.get('secondCategoryName') is not None:
            self.second_category_name = m.get('secondCategoryName')
        if m.get('secondCategoryNameEn') is not None:
            self.second_category_name_en = m.get('secondCategoryNameEn')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')
        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        return self


class ListProductsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        products: List[ListProductsResponseBodyProducts] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.products = products
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.products:
            for k in self.products:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['products'] = []
        if self.products is not None:
            for k in self.products:
                result['products'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.products = []
        if m.get('products') is not None:
            for k in m.get('products'):
                temp_model = ListProductsResponseBodyProducts()
                self.products.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListProductsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProductsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProductsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequestTag(TeaModel):
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


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        tag: List[ListProjectRequestTag] = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
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
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListProjectRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListProjectShrinkRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: str = None,
        page_size: str = None,
        tag_shrink: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        return self


class ListProjectResponseBodyProjectsTags(TeaModel):
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


class ListProjectResponseBodyProjects(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        project_id: str = None,
        tags: List[ListProjectResponseBodyProjectsTags] = None,
        task_cnt: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.project_id = project_id
        self.tags = tags
        self.task_cnt = task_cnt

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
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_cnt is not None:
            result['taskCnt'] = self.task_cnt
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListProjectResponseBodyProjectsTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskCnt') is not None:
            self.task_cnt = m.get('taskCnt')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        page_number: int = None,
        page_size: int = None,
        projects: List[ListProjectResponseBodyProjects] = None,
        request_id: str = None,
    ):
        self.count = count
        self.page_number = page_number
        self.page_size = page_size
        self.projects = projects
        self.request_id = request_id

    def validate(self):
        if self.projects:
            for k in self.projects:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        result['projects'] = []
        if self.projects is not None:
            for k in self.projects:
                result['projects'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        self.projects = []
        if m.get('projects') is not None:
            for k in m.get('projects'):
                temp_model = ListProjectResponseBodyProjects()
                self.projects.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistryModuleVersionsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        module_name: str = None,
        namespace_name: str = None,
        next_token: str = None,
    ):
        self.max_results = max_results
        # This parameter is required.
        self.module_name = module_name
        # This parameter is required.
        self.namespace_name = namespace_name
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        return self


class ListRegistryModuleVersionsResponseBodyModuleVersions(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        source: str = None,
        source_url: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.source = source
        self.source_url = source_url
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.source is not None:
            result['source'] = self.source
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListRegistryModuleVersionsResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        module_versions: List[ListRegistryModuleVersionsResponseBodyModuleVersions] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.module_versions = module_versions
        self.next_token = next_token
        self.request_id = request_id

    def validate(self):
        if self.module_versions:
            for k in self.module_versions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['moduleVersions'] = []
        if self.module_versions is not None:
            for k in self.module_versions:
                result['moduleVersions'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.module_versions = []
        if m.get('moduleVersions') is not None:
            for k in m.get('moduleVersions'):
                temp_model = ListRegistryModuleVersionsResponseBodyModuleVersions()
                self.module_versions.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRegistryModuleVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegistryModuleVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegistryModuleVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistryModulesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        namespace_name: str = None,
        next_token: str = None,
        type: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.namespace_name = namespace_name
        self.next_token = next_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRegistryModulesResponseBodyRegistryModules(TeaModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        downloads: int = None,
        module_name: str = None,
        namespace_name: str = None,
        provider: str = None,
        shared_accounts: List[int] = None,
        source: str = None,
        source_url: str = None,
        type: str = None,
        version: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.downloads = downloads
        self.module_name = module_name
        self.namespace_name = namespace_name
        self.provider = provider
        self.shared_accounts = shared_accounts
        self.source = source
        self.source_url = source_url
        self.type = type
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.downloads is not None:
            result['downloads'] = self.downloads
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.provider is not None:
            result['provider'] = self.provider
        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts
        if self.source is not None:
            result['source'] = self.source
        if self.source_url is not None:
            result['sourceUrl'] = self.source_url
        if self.type is not None:
            result['type'] = self.type
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('downloads') is not None:
            self.downloads = m.get('downloads')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourceUrl') is not None:
            self.source_url = m.get('sourceUrl')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListRegistryModulesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        next_token: str = None,
        registry_modules: List[ListRegistryModulesResponseBodyRegistryModules] = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.next_token = next_token
        self.registry_modules = registry_modules
        self.request_id = request_id

    def validate(self):
        if self.registry_modules:
            for k in self.registry_modules:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        result['registryModules'] = []
        if self.registry_modules is not None:
            for k in self.registry_modules:
                result['registryModules'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        self.registry_modules = []
        if m.get('registryModules') is not None:
            for k in m.get('registryModules'):
                temp_model = ListRegistryModulesResponseBodyRegistryModules()
                self.registry_modules.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRegistryModulesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegistryModulesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegistryModulesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRegistryNamespacesRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        type: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRegistryNamespacesResponseBodyNamespaces(TeaModel):
    def __init__(
        self,
        acl: str = None,
        create_time: str = None,
        description: str = None,
        maintainer: str = None,
        modules: int = None,
        namespace_name: str = None,
        shared_accounts: List[int] = None,
        type: str = None,
    ):
        self.acl = acl
        self.create_time = create_time
        self.description = description
        self.maintainer = maintainer
        self.modules = modules
        self.namespace_name = namespace_name
        self.shared_accounts = shared_accounts
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.maintainer is not None:
            result['maintainer'] = self.maintainer
        if self.modules is not None:
            result['modules'] = self.modules
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.shared_accounts is not None:
            result['sharedAccounts'] = self.shared_accounts
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('maintainer') is not None:
            self.maintainer = m.get('maintainer')
        if m.get('modules') is not None:
            self.modules = m.get('modules')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('sharedAccounts') is not None:
            self.shared_accounts = m.get('sharedAccounts')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListRegistryNamespacesResponseBody(TeaModel):
    def __init__(
        self,
        count: int = None,
        max_results: int = None,
        namespaces: List[ListRegistryNamespacesResponseBodyNamespaces] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        self.count = count
        self.max_results = max_results
        self.namespaces = namespaces
        self.next_token = next_token
        self.request_id = request_id

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
        if self.count is not None:
            result['count'] = self.count
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        result['namespaces'] = []
        if self.namespaces is not None:
            for k in self.namespaces:
                result['namespaces'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        self.namespaces = []
        if m.get('namespaces') is not None:
            for k in m.get('namespaces'):
                temp_model = ListRegistryNamespacesResponseBodyNamespaces()
                self.namespaces.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListRegistryNamespacesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRegistryNamespacesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListRegistryNamespacesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTaskVersionsRequest(TeaModel):
    def __init__(
        self,
        export_version: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        status: str = None,
    ):
        self.export_version = export_version
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasksVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTaskVersionsResponseBodyExportTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_task_id: str = None,
        export_to_module: ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        failed_reason: str = None,
        include_rules: List[ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules] = None,
        modules: List[ListResourceExportTaskVersionsResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[ListResourceExportTaskVersionsResponseBodyExportTasksVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.failed_reason = failed_reason
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.status = status
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.failed_reason is not None:
            result['failedReason'] = self.failed_reason
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('failedReason') is not None:
            self.failed_reason = m.get('failedReason')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTaskVersionsResponseBody(TeaModel):
    def __init__(
        self,
        export_tasks: List[ListResourceExportTaskVersionsResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.export_tasks = export_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTaskVersionsResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTaskVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceExportTaskVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTaskVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceExportTasksRequest(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.export_task_id = export_task_id
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListResourceExportTasksResponseBodyExportTasksExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class ListResourceExportTasksResponseBodyExportTasksIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class ListResourceExportTasksResponseBodyExportTasksModules(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        version: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListResourceExportTasksResponseBodyExportTasksVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class ListResourceExportTasksResponseBodyExportTasks(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        elapsed_time: int = None,
        export_status: str = None,
        export_task_id: str = None,
        export_to_module: ListResourceExportTasksResponseBodyExportTasksExportToModule = None,
        export_version: str = None,
        include_rules: List[ListResourceExportTasksResponseBodyExportTasksIncludeRules] = None,
        modules: List[ListResourceExportTasksResponseBodyExportTasksModules] = None,
        name: str = None,
        status: str = None,
        variables: List[ListResourceExportTasksResponseBodyExportTasksVariables] = None,
    ):
        self.create_time = create_time
        self.description = description
        self.elapsed_time = elapsed_time
        self.export_status = export_status
        self.export_task_id = export_task_id
        self.export_to_module = export_to_module
        self.export_version = export_version
        self.include_rules = include_rules
        self.modules = modules
        self.name = name
        self.status = status
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.modules:
            for k in self.modules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.elapsed_time is not None:
            result['elapsedTime'] = self.elapsed_time
        if self.export_status is not None:
            result['exportStatus'] = self.export_status
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        result['modules'] = []
        if self.modules is not None:
            for k in self.modules:
                result['modules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('elapsedTime') is not None:
            self.elapsed_time = m.get('elapsedTime')
        if m.get('exportStatus') is not None:
            self.export_status = m.get('exportStatus')
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportToModule') is not None:
            temp_model = ListResourceExportTasksResponseBodyExportTasksExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        self.modules = []
        if m.get('modules') is not None:
            for k in m.get('modules'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksModules()
                self.modules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = ListResourceExportTasksResponseBodyExportTasksVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class ListResourceExportTasksResponseBody(TeaModel):
    def __init__(
        self,
        export_tasks: List[ListResourceExportTasksResponseBodyExportTasks] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.export_tasks = export_tasks
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.export_tasks:
            for k in self.export_tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['exportTasks'] = []
        if self.export_tasks is not None:
            for k in self.export_tasks:
                result['exportTasks'].append(k.to_map() if k else None)
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.export_tasks = []
        if m.get('exportTasks') is not None:
            for k in m.get('exportTasks'):
                temp_model = ListResourceExportTasksResponseBodyExportTasks()
                self.export_tasks.append(temp_model.from_map(k))
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceExportTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceExportTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceExportTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceTypesRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product: str = None,
        sort: str = None,
        status: str = None,
        subcategory: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
        terraform_resource_types: List[str] = None,
    ):
        self.accept_language = accept_language
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.product = product
        self.sort = sort
        self.status = status
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_types = terraform_resource_types

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.product is not None:
            result['product'] = self.product
        if self.sort is not None:
            result['sort'] = self.sort
        if self.status is not None:
            result['status'] = self.status
        if self.subcategory is not None:
            result['subcategory'] = self.subcategory
        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_resource_types is not None:
            result['terraformResourceTypes'] = self.terraform_resource_types
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')
        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformResourceTypes') is not None:
            self.terraform_resource_types = m.get('terraformResourceTypes')
        return self


class ListResourceTypesShrinkRequest(TeaModel):
    def __init__(
        self,
        accept_language: str = None,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        product: str = None,
        sort: str = None,
        status: str = None,
        subcategory: str = None,
        support_terraformer: bool = None,
        terraform_provider_version: str = None,
        terraform_resource_types_shrink: str = None,
    ):
        self.accept_language = accept_language
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.product = product
        self.sort = sort
        self.status = status
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_types_shrink = terraform_resource_types_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['acceptLanguage'] = self.accept_language
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.product is not None:
            result['product'] = self.product
        if self.sort is not None:
            result['sort'] = self.sort
        if self.status is not None:
            result['status'] = self.status
        if self.subcategory is not None:
            result['subcategory'] = self.subcategory
        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_resource_types_shrink is not None:
            result['terraformResourceTypes'] = self.terraform_resource_types_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acceptLanguage') is not None:
            self.accept_language = m.get('acceptLanguage')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')
        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformResourceTypes') is not None:
            self.terraform_resource_types_shrink = m.get('terraformResourceTypes')
        return self


class ListResourceTypesResponseBodyResourceTypes(TeaModel):
    def __init__(
        self,
        description: str = None,
        product: str = None,
        product_name: str = None,
        resource_detail_page_url: str = None,
        resource_list_page_url: str = None,
        status: str = None,
        status_start_version: str = None,
        subcategory: str = None,
        support_terraformer: str = None,
        terraform_provider_version: str = None,
        terraform_resource_type: str = None,
        title: str = None,
    ):
        self.description = description
        self.product = product
        self.product_name = product_name
        self.resource_detail_page_url = resource_detail_page_url
        self.resource_list_page_url = resource_list_page_url
        self.status = status
        self.status_start_version = status_start_version
        self.subcategory = subcategory
        self.support_terraformer = support_terraformer
        self.terraform_provider_version = terraform_provider_version
        self.terraform_resource_type = terraform_resource_type
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.product is not None:
            result['product'] = self.product
        if self.product_name is not None:
            result['productName'] = self.product_name
        if self.resource_detail_page_url is not None:
            result['resourceDetailPageUrl'] = self.resource_detail_page_url
        if self.resource_list_page_url is not None:
            result['resourceListPageUrl'] = self.resource_list_page_url
        if self.status is not None:
            result['status'] = self.status
        if self.status_start_version is not None:
            result['statusStartVersion'] = self.status_start_version
        if self.subcategory is not None:
            result['subcategory'] = self.subcategory
        if self.support_terraformer is not None:
            result['supportTerraformer'] = self.support_terraformer
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_resource_type is not None:
            result['terraformResourceType'] = self.terraform_resource_type
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('product') is not None:
            self.product = m.get('product')
        if m.get('productName') is not None:
            self.product_name = m.get('productName')
        if m.get('resourceDetailPageUrl') is not None:
            self.resource_detail_page_url = m.get('resourceDetailPageUrl')
        if m.get('resourceListPageUrl') is not None:
            self.resource_list_page_url = m.get('resourceListPageUrl')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('statusStartVersion') is not None:
            self.status_start_version = m.get('statusStartVersion')
        if m.get('subcategory') is not None:
            self.subcategory = m.get('subcategory')
        if m.get('supportTerraformer') is not None:
            self.support_terraformer = m.get('supportTerraformer')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformResourceType') is not None:
            self.terraform_resource_type = m.get('terraformResourceType')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class ListResourceTypesResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        resource_types: List[ListResourceTypesResponseBodyResourceTypes] = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.resource_types = resource_types
        self.total_count = total_count

    def validate(self):
        if self.resource_types:
            for k in self.resource_types:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['resourceTypes'] = []
        if self.resource_types is not None:
            for k in self.resource_types:
                result['resourceTypes'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.resource_types = []
        if m.get('resourceTypes') is not None:
            for k in m.get('resourceTypes'):
                temp_model = ListResourceTypesResponseBodyResourceTypes()
                self.resource_types.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceTypesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceTypesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceTypesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequestTag(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        tag: List[ListTasksRequestTag] = None,
        task_id: str = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.tag = tag
        self.task_id = task_id

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
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        result['tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['tag'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tag = []
        if m.get('tag') is not None:
            for k in m.get('tag'):
                temp_model = ListTasksRequestTag()
                self.tag.append(temp_model.from_map(k))
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksShrinkRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        keyword: str = None,
        module_id: str = None,
        page_number: int = None,
        page_size: int = None,
        project_id: str = None,
        status: str = None,
        tag_shrink: str = None,
        task_id: str = None,
    ):
        self.group_id = group_id
        self.keyword = keyword
        self.module_id = module_id
        self.page_number = page_number
        self.page_size = page_size
        self.project_id = project_id
        self.status = status
        self.tag_shrink = tag_shrink
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.status is not None:
            result['status'] = self.status
        if self.tag_shrink is not None:
            result['tag'] = self.tag_shrink
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('tag') is not None:
            self.tag_shrink = m.get('tag')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBodyTasksGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        group_name: str = None,
        project_id: str = None,
        project_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name
        self.project_id = project_id
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.project_name is not None:
            result['projectName'] = self.project_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')
        return self


class ListTasksResponseBodyTasksTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        tag_key: str = None,
        tag_value: str = None,
        value: str = None,
    ):
        self.key = key
        self.tag_key = tag_key
        self.tag_value = tag_value
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
        if self.tag_key is not None:
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class ListTasksResponseBodyTasks(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        create_time: str = None,
        current_job_id: str = None,
        current_job_status: str = None,
        deletion_protection: bool = None,
        group_info: ListTasksResponseBodyTasksGroupInfo = None,
        latest_module_version: str = None,
        module_id: str = None,
        module_name: str = None,
        module_version: str = None,
        name: str = None,
        status: str = None,
        tags: List[ListTasksResponseBodyTasksTags] = None,
        task_id: str = None,
    ):
        self.auto_apply = auto_apply
        self.create_time = create_time
        self.current_job_id = current_job_id
        self.current_job_status = current_job_status
        self.deletion_protection = deletion_protection
        self.group_info = group_info
        self.latest_module_version = latest_module_version
        self.module_id = module_id
        self.module_name = module_name
        self.module_version = module_version
        self.name = name
        self.status = status
        self.tags = tags
        self.task_id = task_id

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.current_job_id is not None:
            result['currentJobId'] = self.current_job_id
        if self.current_job_status is not None:
            result['currentJobStatus'] = self.current_job_status
        if self.deletion_protection is not None:
            result['deletionProtection'] = self.deletion_protection
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.latest_module_version is not None:
            result['latestModuleVersion'] = self.latest_module_version
        if self.module_id is not None:
            result['moduleId'] = self.module_id
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.task_id is not None:
            result['taskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('currentJobId') is not None:
            self.current_job_id = m.get('currentJobId')
        if m.get('currentJobStatus') is not None:
            self.current_job_status = m.get('currentJobStatus')
        if m.get('deletionProtection') is not None:
            self.deletion_protection = m.get('deletionProtection')
        if m.get('groupInfo') is not None:
            temp_model = ListTasksResponseBodyTasksGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('latestModuleVersion') is not None:
            self.latest_module_version = m.get('latestModuleVersion')
        if m.get('moduleId') is not None:
            self.module_id = m.get('moduleId')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ListTasksResponseBodyTasksTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        tasks: List[ListTasksResponseBodyTasks] = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.tasks = tasks
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
        if self.page_number is not None:
            result['pageNumber'] = self.page_number
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('pageNumber') is not None:
            self.page_number = m.get('pageNumber')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = ListTasksResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTerraformProviderVersionsRequest(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        max_results: int = None,
        next_token: str = None,
        usage: str = None,
    ):
        self.keyword = keyword
        self.max_results = max_results
        self.next_token = next_token
        self.usage = usage

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['keyword'] = self.keyword
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.usage is not None:
            result['usage'] = self.usage
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keyword') is not None:
            self.keyword = m.get('keyword')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('usage') is not None:
            self.usage = m.get('usage')
        return self


class ListTerraformProviderVersionsResponseBodyVersions(TeaModel):
    def __init__(
        self,
        published_time: str = None,
        status: str = None,
        version: str = None,
    ):
        self.published_time = published_time
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.published_time is not None:
            result['publishedTime'] = self.published_time
        if self.status is not None:
            result['status'] = self.status
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class ListTerraformProviderVersionsResponseBody(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[ListTerraformProviderVersionsResponseBodyVersions] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
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
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        result['versions'] = []
        if self.versions is not None:
            for k in self.versions:
                result['versions'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        self.versions = []
        if m.get('versions') is not None:
            for k in m.get('versions'):
                temp_model = ListTerraformProviderVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k))
        return self


class ListTerraformProviderVersionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTerraformProviderVersionsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTerraformProviderVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateJobRequest(TeaModel):
    def __init__(
        self,
        comment: str = None,
        task_type: str = None,
    ):
        # This parameter is required.
        self.comment = comment
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['comment'] = self.comment
        if self.task_type is not None:
            result['taskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        return self


class OperateJobResponseBody(TeaModel):
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


class OperateJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateJobResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishRegistryModuleVersionRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        module_name: str = None,
        namespace_name: str = None,
        version: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        # This parameter is required.
        self.module_name = module_name
        # This parameter is required.
        self.namespace_name = namespace_name
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.module_name is not None:
            result['moduleName'] = self.module_name
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('moduleName') is not None:
            self.module_name = m.get('moduleName')
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PublishRegistryModuleVersionResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        version: str = None,
    ):
        self.request_id = request_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class PublishRegistryModuleVersionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PublishRegistryModuleVersionResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = PublishRegistryModuleVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSharedAccountsRequest(TeaModel):
    def __init__(
        self,
        account_ids: List[int] = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.account_ids = account_ids
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids is not None:
            result['accountIds'] = self.account_ids
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids = m.get('accountIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class RemoveSharedAccountsShrinkRequest(TeaModel):
    def __init__(
        self,
        account_ids_shrink: str = None,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # This parameter is required.
        self.account_ids_shrink = account_ids_shrink
        # This parameter is required.
        self.resource_id = resource_id
        # This parameter is required.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account_ids_shrink is not None:
            result['accountIds'] = self.account_ids_shrink
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountIds') is not None:
            self.account_ids_shrink = m.get('accountIds')
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class RemoveSharedAccountsResponseBody(TeaModel):
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


class RemoveSharedAccountsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSharedAccountsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RemoveSharedAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateExplorerModuleAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        self.client_token = client_token
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateExplorerModuleAttributeResponseBody(TeaModel):
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


class UpdateExplorerModuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateExplorerModuleAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateExplorerModuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequestNotifyConfig(TeaModel):
    def __init__(
        self,
        notify_path: str = None,
        notify_type: str = None,
    ):
        self.notify_path = notify_path
        self.notify_type = notify_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.notify_path is not None:
            result['notifyPath'] = self.notify_path
        if self.notify_type is not None:
            result['notifyType'] = self.notify_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('notifyPath') is not None:
            self.notify_path = m.get('notifyPath')
        if m.get('notifyType') is not None:
            self.notify_type = m.get('notifyType')
        return self


class UpdateGroupRequestTriggerConfig(TeaModel):
    def __init__(
        self,
        trigger_strategy: str = None,
        trigger_value: str = None,
    ):
        self.trigger_strategy = trigger_strategy
        self.trigger_value = trigger_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        if self.trigger_value is not None:
            result['triggerValue'] = self.trigger_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        if m.get('triggerValue') is not None:
            self.trigger_value = m.get('triggerValue')
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        auto_destroy: bool = None,
        auto_trigger: bool = None,
        client_token: str = None,
        description: str = None,
        forced_setting: bool = None,
        name: str = None,
        notify_config: List[UpdateGroupRequestNotifyConfig] = None,
        notify_operation_types: List[str] = None,
        ram_role: str = None,
        report_export_field: List[str] = None,
        report_export_path: str = None,
        terraform_provider_version: str = None,
        trigger_config: List[UpdateGroupRequestTriggerConfig] = None,
        trigger_resource_type: List[str] = None,
    ):
        self.auto_destroy = auto_destroy
        self.auto_trigger = auto_trigger
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.forced_setting = forced_setting
        self.name = name
        self.notify_config = notify_config
        self.notify_operation_types = notify_operation_types
        self.ram_role = ram_role
        self.report_export_field = report_export_field
        self.report_export_path = report_export_path
        self.terraform_provider_version = terraform_provider_version
        self.trigger_config = trigger_config
        self.trigger_resource_type = trigger_resource_type

    def validate(self):
        if self.notify_config:
            for k in self.notify_config:
                if k:
                    k.validate()
        if self.trigger_config:
            for k in self.trigger_config:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.auto_trigger is not None:
            result['autoTrigger'] = self.auto_trigger
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.forced_setting is not None:
            result['forcedSetting'] = self.forced_setting
        if self.name is not None:
            result['name'] = self.name
        result['notifyConfig'] = []
        if self.notify_config is not None:
            for k in self.notify_config:
                result['notifyConfig'].append(k.to_map() if k else None)
        if self.notify_operation_types is not None:
            result['notifyOperationTypes'] = self.notify_operation_types
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.report_export_field is not None:
            result['reportExportField'] = self.report_export_field
        if self.report_export_path is not None:
            result['reportExportPath'] = self.report_export_path
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        result['triggerConfig'] = []
        if self.trigger_config is not None:
            for k in self.trigger_config:
                result['triggerConfig'].append(k.to_map() if k else None)
        if self.trigger_resource_type is not None:
            result['triggerResourceType'] = self.trigger_resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('autoTrigger') is not None:
            self.auto_trigger = m.get('autoTrigger')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('forcedSetting') is not None:
            self.forced_setting = m.get('forcedSetting')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.notify_config = []
        if m.get('notifyConfig') is not None:
            for k in m.get('notifyConfig'):
                temp_model = UpdateGroupRequestNotifyConfig()
                self.notify_config.append(temp_model.from_map(k))
        if m.get('notifyOperationTypes') is not None:
            self.notify_operation_types = m.get('notifyOperationTypes')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('reportExportField') is not None:
            self.report_export_field = m.get('reportExportField')
        if m.get('reportExportPath') is not None:
            self.report_export_path = m.get('reportExportPath')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        self.trigger_config = []
        if m.get('triggerConfig') is not None:
            for k in m.get('triggerConfig'):
                temp_model = UpdateGroupRequestTriggerConfig()
                self.trigger_config.append(temp_model.from_map(k))
        if m.get('triggerResourceType') is not None:
            self.trigger_resource_type = m.get('triggerResourceType')
        return self


class UpdateGroupResponseBody(TeaModel):
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


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateModuleAttributeRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class UpdateModuleAttributeRequestTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class UpdateModuleAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        group_info: UpdateModuleAttributeRequestGroupInfo = None,
        name: str = None,
        source_path: str = None,
        state_path: str = None,
        tags: List[UpdateModuleAttributeRequestTags] = None,
        version_strategy: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        self.name = name
        self.source_path = source_path
        self.state_path = state_path
        self.tags = tags
        self.version_strategy = version_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.name is not None:
            result['name'] = self.name
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.version_strategy is not None:
            result['versionStrategy'] = self.version_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = UpdateModuleAttributeRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = UpdateModuleAttributeRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('versionStrategy') is not None:
            self.version_strategy = m.get('versionStrategy')
        return self


class UpdateModuleAttributeResponseBody(TeaModel):
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


class UpdateModuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateModuleAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateModuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class UpdateProjectResponseBody(TeaModel):
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


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegistryModuleAttributeRequest(TeaModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.acl = acl
        # This parameter is required.
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateRegistryModuleAttributeResponseBody(TeaModel):
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


class UpdateRegistryModuleAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRegistryModuleAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRegistryModuleAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRegistryNamespaceAttributeRequest(TeaModel):
    def __init__(
        self,
        acl: str = None,
        client_token: str = None,
        description: str = None,
    ):
        self.acl = acl
        # This parameter is required.
        self.client_token = client_token
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acl is not None:
            result['acl'] = self.acl
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acl') is not None:
            self.acl = m.get('acl')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        return self


class UpdateRegistryNamespaceAttributeResponseBody(TeaModel):
    def __init__(
        self,
        namespace_name: str = None,
        request_id: str = None,
    ):
        self.namespace_name = namespace_name
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.namespace_name is not None:
            result['namespaceName'] = self.namespace_name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('namespaceName') is not None:
            self.namespace_name = m.get('namespaceName')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateRegistryNamespaceAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateRegistryNamespaceAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateRegistryNamespaceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceExportTaskAttributeRequestExportToModule(TeaModel):
    def __init__(
        self,
        source: str = None,
        source_path: str = None,
        state_path: str = None,
    ):
        self.source = source
        self.source_path = source_path
        self.state_path = state_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        if self.state_path is not None:
            result['statePath'] = self.state_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        if m.get('statePath') is not None:
            self.state_path = m.get('statePath')
        return self


class UpdateResourceExportTaskAttributeRequestIncludeRules(TeaModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        self.key = key
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.values is not None:
            result['values'] = self.values
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('values') is not None:
            self.values = m.get('values')
        return self


class UpdateResourceExportTaskAttributeRequestVariables(TeaModel):
    def __init__(
        self,
        properties: List[str] = None,
        resource_type: str = None,
    ):
        self.properties = properties
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.properties is not None:
            result['properties'] = self.properties
        if self.resource_type is not None:
            result['resourceType'] = self.resource_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')
        return self


class UpdateResourceExportTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        description: str = None,
        export_to_module: UpdateResourceExportTaskAttributeRequestExportToModule = None,
        include_rules: List[UpdateResourceExportTaskAttributeRequestIncludeRules] = None,
        name: str = None,
        ram_role: str = None,
        terraform_provider_version: str = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
        variables: List[UpdateResourceExportTaskAttributeRequestVariables] = None,
    ):
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.export_to_module = export_to_module
        self.include_rules = include_rules
        self.name = name
        self.ram_role = ram_role
        self.terraform_provider_version = terraform_provider_version
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy
        self.variables = variables

    def validate(self):
        if self.export_to_module:
            self.export_to_module.validate()
        if self.include_rules:
            for k in self.include_rules:
                if k:
                    k.validate()
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.export_to_module is not None:
            result['exportToModule'] = self.export_to_module.to_map()
        result['includeRules'] = []
        if self.include_rules is not None:
            for k in self.include_rules:
                result['includeRules'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.terraform_provider_version is not None:
            result['terraformProviderVersion'] = self.terraform_provider_version
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('exportToModule') is not None:
            temp_model = UpdateResourceExportTaskAttributeRequestExportToModule()
            self.export_to_module = temp_model.from_map(m['exportToModule'])
        self.include_rules = []
        if m.get('includeRules') is not None:
            for k in m.get('includeRules'):
                temp_model = UpdateResourceExportTaskAttributeRequestIncludeRules()
                self.include_rules.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('terraformProviderVersion') is not None:
            self.terraform_provider_version = m.get('terraformProviderVersion')
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = UpdateResourceExportTaskAttributeRequestVariables()
                self.variables.append(temp_model.from_map(k))
        return self


class UpdateResourceExportTaskAttributeResponseBody(TeaModel):
    def __init__(
        self,
        export_task_id: str = None,
        export_version: str = None,
        request_id: str = None,
    ):
        self.export_task_id = export_task_id
        self.export_version = export_version
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.export_task_id is not None:
            result['exportTaskId'] = self.export_task_id
        if self.export_version is not None:
            result['exportVersion'] = self.export_version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exportTaskId') is not None:
            self.export_task_id = m.get('exportTaskId')
        if m.get('exportVersion') is not None:
            self.export_version = m.get('exportVersion')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class UpdateResourceExportTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateResourceExportTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceExportTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTaskAttributeRequestGroupInfo(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        project_id: str = None,
    ):
        self.group_id = group_id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['groupId'] = self.group_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class UpdateTaskAttributeRequestTags(TeaModel):
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
            result['tagKey'] = self.tag_key
        if self.tag_value is not None:
            result['tagValue'] = self.tag_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('tagKey') is not None:
            self.tag_key = m.get('tagKey')
        if m.get('tagValue') is not None:
            self.tag_value = m.get('tagValue')
        return self


class UpdateTaskAttributeRequest(TeaModel):
    def __init__(
        self,
        auto_apply: bool = None,
        auto_destroy: bool = None,
        client_token: str = None,
        description: str = None,
        group_info: UpdateTaskAttributeRequestGroupInfo = None,
        init_module_state: bool = None,
        module_version: str = None,
        name: str = None,
        protection_strategy: List[str] = None,
        ram_role: str = None,
        skip_property_validation: bool = None,
        tags: List[UpdateTaskAttributeRequestTags] = None,
        terraform_version: str = None,
        trigger_strategy: str = None,
    ):
        self.auto_apply = auto_apply
        self.auto_destroy = auto_destroy
        # This parameter is required.
        self.client_token = client_token
        self.description = description
        self.group_info = group_info
        self.init_module_state = init_module_state
        self.module_version = module_version
        self.name = name
        self.protection_strategy = protection_strategy
        self.ram_role = ram_role
        self.skip_property_validation = skip_property_validation
        self.tags = tags
        self.terraform_version = terraform_version
        self.trigger_strategy = trigger_strategy

    def validate(self):
        if self.group_info:
            self.group_info.validate()
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_apply is not None:
            result['autoApply'] = self.auto_apply
        if self.auto_destroy is not None:
            result['autoDestroy'] = self.auto_destroy
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.description is not None:
            result['description'] = self.description
        if self.group_info is not None:
            result['groupInfo'] = self.group_info.to_map()
        if self.init_module_state is not None:
            result['initModuleState'] = self.init_module_state
        if self.module_version is not None:
            result['moduleVersion'] = self.module_version
        if self.name is not None:
            result['name'] = self.name
        if self.protection_strategy is not None:
            result['protectionStrategy'] = self.protection_strategy
        if self.ram_role is not None:
            result['ramRole'] = self.ram_role
        if self.skip_property_validation is not None:
            result['skipPropertyValidation'] = self.skip_property_validation
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        if self.terraform_version is not None:
            result['terraformVersion'] = self.terraform_version
        if self.trigger_strategy is not None:
            result['triggerStrategy'] = self.trigger_strategy
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('autoApply') is not None:
            self.auto_apply = m.get('autoApply')
        if m.get('autoDestroy') is not None:
            self.auto_destroy = m.get('autoDestroy')
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupInfo') is not None:
            temp_model = UpdateTaskAttributeRequestGroupInfo()
            self.group_info = temp_model.from_map(m['groupInfo'])
        if m.get('initModuleState') is not None:
            self.init_module_state = m.get('initModuleState')
        if m.get('moduleVersion') is not None:
            self.module_version = m.get('moduleVersion')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('protectionStrategy') is not None:
            self.protection_strategy = m.get('protectionStrategy')
        if m.get('ramRole') is not None:
            self.ram_role = m.get('ramRole')
        if m.get('skipPropertyValidation') is not None:
            self.skip_property_validation = m.get('skipPropertyValidation')
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = UpdateTaskAttributeRequestTags()
                self.tags.append(temp_model.from_map(k))
        if m.get('terraformVersion') is not None:
            self.terraform_version = m.get('terraformVersion')
        if m.get('triggerStrategy') is not None:
            self.trigger_strategy = m.get('triggerStrategy')
        return self


class UpdateTaskAttributeResponseBody(TeaModel):
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


class UpdateTaskAttributeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTaskAttributeResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateTaskAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ValidateModuleRequest(TeaModel):
    def __init__(
        self,
        client_token: str = None,
        code: str = None,
        code_map: Dict[str, Any] = None,
        source: str = None,
        source_path: str = None,
    ):
        self.client_token = client_token
        self.code = code
        self.code_map = code_map
        self.source = source
        self.source_path = source_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_token is not None:
            result['clientToken'] = self.client_token
        if self.code is not None:
            result['code'] = self.code
        if self.code_map is not None:
            result['codeMap'] = self.code_map
        if self.source is not None:
            result['source'] = self.source
        if self.source_path is not None:
            result['sourcePath'] = self.source_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clientToken') is not None:
            self.client_token = m.get('clientToken')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('codeMap') is not None:
            self.code_map = m.get('codeMap')
        if m.get('source') is not None:
            self.source = m.get('source')
        if m.get('sourcePath') is not None:
            self.source_path = m.get('sourcePath')
        return self


class ValidateModuleResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        module_validation_id: str = None,
        request_id: str = None,
        status: str = None,
    ):
        self.message = message
        self.module_validation_id = module_validation_id
        self.request_id = request_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['message'] = self.message
        if self.module_validation_id is not None:
            result['moduleValidationId'] = self.module_validation_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('moduleValidationId') is not None:
            self.module_validation_id = m.get('moduleValidationId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ValidateModuleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ValidateModuleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ValidateModuleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


