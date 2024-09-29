# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class CreateWorkflowRequest(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_strategy: str = None,
        task_definition_json_value: str = None,
        task_relation_json_value: str = None,
        cron_expr: str = None,
        description: str = None,
        execution_type: str = None,
        failure_strategy: str = None,
        name: str = None,
        parent_directory_id: str = None,
        resource_group_id: str = None,
        schedule_end_time: str = None,
        schedule_start_time: str = None,
        schedule_state: str = None,
        task_definition_json: str = None,
        task_relation_json: str = None,
        time_zone: str = None,
        timeout: int = None,
        workflow_instance_priority: str = None,
        workflow_params: str = None,
        workspace_id: str = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_strategy = alert_strategy
        self.task_definition_json_value = task_definition_json_value
        self.task_relation_json_value = task_relation_json_value
        self.cron_expr = cron_expr
        self.description = description
        self.execution_type = execution_type
        self.failure_strategy = failure_strategy
        # This parameter is required.
        self.name = name
        self.parent_directory_id = parent_directory_id
        self.resource_group_id = resource_group_id
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.schedule_state = schedule_state
        # This parameter is required.
        self.task_definition_json = task_definition_json
        # This parameter is required.
        self.task_relation_json = task_relation_json
        self.time_zone = time_zone
        self.timeout = timeout
        self.workflow_instance_priority = workflow_instance_priority
        self.workflow_params = workflow_params
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_strategy is not None:
            result['alertStrategy'] = self.alert_strategy
        if self.task_definition_json_value is not None:
            result['taskDefinitionJsonValue'] = self.task_definition_json_value
        if self.task_relation_json_value is not None:
            result['taskRelationJsonValue'] = self.task_relation_json_value
        if self.cron_expr is not None:
            result['cronExpr'] = self.cron_expr
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.failure_strategy is not None:
            result['failureStrategy'] = self.failure_strategy
        if self.name is not None:
            result['name'] = self.name
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.schedule_end_time is not None:
            result['scheduleEndTime'] = self.schedule_end_time
        if self.schedule_start_time is not None:
            result['scheduleStartTime'] = self.schedule_start_time
        if self.schedule_state is not None:
            result['scheduleState'] = self.schedule_state
        if self.task_definition_json is not None:
            result['taskDefinitionJson'] = self.task_definition_json
        if self.task_relation_json is not None:
            result['taskRelationJson'] = self.task_relation_json
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.workflow_instance_priority is not None:
            result['workflowInstancePriority'] = self.workflow_instance_priority
        if self.workflow_params is not None:
            result['workflowParams'] = self.workflow_params
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertStrategy') is not None:
            self.alert_strategy = m.get('alertStrategy')
        if m.get('taskDefinitionJsonValue') is not None:
            self.task_definition_json_value = m.get('taskDefinitionJsonValue')
        if m.get('taskRelationJsonValue') is not None:
            self.task_relation_json_value = m.get('taskRelationJsonValue')
        if m.get('cronExpr') is not None:
            self.cron_expr = m.get('cronExpr')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('failureStrategy') is not None:
            self.failure_strategy = m.get('failureStrategy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('scheduleEndTime') is not None:
            self.schedule_end_time = m.get('scheduleEndTime')
        if m.get('scheduleStartTime') is not None:
            self.schedule_start_time = m.get('scheduleStartTime')
        if m.get('scheduleState') is not None:
            self.schedule_state = m.get('scheduleState')
        if m.get('taskDefinitionJson') is not None:
            self.task_definition_json = m.get('taskDefinitionJson')
        if m.get('taskRelationJson') is not None:
            self.task_relation_json = m.get('taskRelationJson')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workflowInstancePriority') is not None:
            self.workflow_instance_priority = m.get('workflowInstancePriority')
        if m.get('workflowParams') is not None:
            self.workflow_params = m.get('workflowParams')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class CreateWorkflowResponseBodyData(TeaModel):
    def __init__(
        self,
        workflow_id: str = None,
    ):
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        return self


class CreateWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        data: CreateWorkflowResponseBodyData = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
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
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = CreateWorkflowResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteWorkflowRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DeleteWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class DeleteWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManualTaskRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeManualTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        manual_task_id: str = None,
        manual_task_name: str = None,
        parent_directory_id: str = None,
        project_id: str = None,
        resource_ids: str = None,
        task_params: str = None,
        task_type: str = None,
        update_time: str = None,
        request_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.manual_task_id = manual_task_id
        self.manual_task_name = manual_task_name
        self.parent_directory_id = parent_directory_id
        self.project_id = project_id
        self.resource_ids = resource_ids
        self.task_params = task_params
        self.task_type = task_type
        self.update_time = update_time
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.description is not None:
            result['Description'] = self.description
        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id
        if self.manual_task_name is not None:
            result['ManualTaskName'] = self.manual_task_name
        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')
        if m.get('ManualTaskName') is not None:
            self.manual_task_name = m.get('ManualTaskName')
        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeManualTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeManualTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManualTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeManualTaskInstanceRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeManualTaskInstanceResponseBody(TeaModel):
    def __init__(
        self,
        emr_cluster_id: str = None,
        end_time: str = None,
        external_app_id: str = None,
        manual_task_instance_id: str = None,
        manual_task_instance_name: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        status: str = None,
        submit_time: str = None,
        task_params: str = None,
        task_type: str = None,
        request_id: str = None,
    ):
        self.emr_cluster_id = emr_cluster_id
        self.end_time = end_time
        self.external_app_id = external_app_id
        self.manual_task_instance_id = manual_task_instance_id
        self.manual_task_instance_name = manual_task_instance_name
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.status = status
        self.submit_time = submit_time
        self.task_params = task_params
        self.task_type = task_type
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.manual_task_instance_id is not None:
            result['ManualTaskInstanceId'] = self.manual_task_instance_id
        if self.manual_task_instance_name is not None:
            result['ManualTaskInstanceName'] = self.manual_task_instance_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ManualTaskInstanceId') is not None:
            self.manual_task_instance_id = m.get('ManualTaskInstanceId')
        if m.get('ManualTaskInstanceName') is not None:
            self.manual_task_instance_name = m.get('ManualTaskInstanceName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeManualTaskInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeManualTaskInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeManualTaskInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeProjectRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeProjectResponseBody(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        project_id: str = None,
        request_id: str = None,
    ):
        # This parameter is required.
        self.description = description
        # This parameter is required.
        self.name = name
        self.project_id = project_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeProjectResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeTaskResponseBody(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        delay_time: int = None,
        description: str = None,
        fail_retry_interval: int = None,
        fail_retry_times: int = None,
        flag: str = None,
        project_id: str = None,
        resource_ids: str = None,
        task_id: str = None,
        task_name: str = None,
        task_params: str = None,
        task_priority: str = None,
        task_type: str = None,
        timeout: int = None,
        timeout_flag: str = None,
        timeout_notify_strategy: str = None,
        update_time: str = None,
        version: str = None,
        request_id: str = None,
    ):
        self.create_time = create_time
        self.delay_time = delay_time
        self.description = description
        self.fail_retry_interval = fail_retry_interval
        self.fail_retry_times = fail_retry_times
        self.flag = flag
        self.project_id = project_id
        self.resource_ids = resource_ids
        self.task_id = task_id
        self.task_name = task_name
        self.task_params = task_params
        self.task_priority = task_priority
        self.task_type = task_type
        self.timeout = timeout
        self.timeout_flag = timeout_flag
        self.timeout_notify_strategy = timeout_notify_strategy
        self.update_time = update_time
        self.version = version
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.description is not None:
            result['Description'] = self.description
        if self.fail_retry_interval is not None:
            result['FailRetryInterval'] = self.fail_retry_interval
        if self.fail_retry_times is not None:
            result['FailRetryTimes'] = self.fail_retry_times
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_flag is not None:
            result['TimeoutFlag'] = self.timeout_flag
        if self.timeout_notify_strategy is not None:
            result['TimeoutNotifyStrategy'] = self.timeout_notify_strategy
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailRetryInterval') is not None:
            self.fail_retry_interval = m.get('FailRetryInterval')
        if m.get('FailRetryTimes') is not None:
            self.fail_retry_times = m.get('FailRetryTimes')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutFlag') is not None:
            self.timeout_flag = m.get('TimeoutFlag')
        if m.get('TimeoutNotifyStrategy') is not None:
            self.timeout_notify_strategy = m.get('TimeoutNotifyStrategy')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeTaskInstanceRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeTaskInstanceResponseBody(TeaModel):
    def __init__(
        self,
        dry_run: str = None,
        emr_cluster_id: str = None,
        end_time: str = None,
        external_app_id: str = None,
        resource_group_id: str = None,
        retry_times: int = None,
        start_time: str = None,
        status: str = None,
        submit_time: str = None,
        task_id: str = None,
        task_instance_id: str = None,
        task_instance_name: str = None,
        task_params: str = None,
        task_type: str = None,
        task_version: str = None,
        workflow_instance_id: str = None,
        request_id: str = None,
    ):
        self.dry_run = dry_run
        self.emr_cluster_id = emr_cluster_id
        self.end_time = end_time
        self.external_app_id = external_app_id
        self.resource_group_id = resource_group_id
        self.retry_times = retry_times
        self.start_time = start_time
        self.status = status
        self.submit_time = submit_time
        self.task_id = task_id
        self.task_instance_id = task_instance_id
        self.task_instance_name = task_instance_name
        self.task_params = task_params
        self.task_type = task_type
        self.task_version = task_version
        self.workflow_instance_id = workflow_instance_id
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id
        if self.task_instance_name is not None:
            result['TaskInstanceName'] = self.task_instance_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')
        if m.get('TaskInstanceName') is not None:
            self.task_instance_name = m.get('TaskInstanceName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class DescribeTaskInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeTaskInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeTaskInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeWorkflowResponseBodySchedule(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_strategy: str = None,
        cron_expr: str = None,
        emr_cluster_id: str = None,
        failure_strategy: str = None,
        resource_group_id: str = None,
        schedule_end_time: str = None,
        schedule_start_time: str = None,
        schedule_state: str = None,
        time_zone: str = None,
        workflow_instance_priority: str = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_strategy = alert_strategy
        self.cron_expr = cron_expr
        self.emr_cluster_id = emr_cluster_id
        self.failure_strategy = failure_strategy
        self.resource_group_id = resource_group_id
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.schedule_state = schedule_state
        self.time_zone = time_zone
        self.workflow_instance_priority = workflow_instance_priority

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_strategy is not None:
            result['alertStrategy'] = self.alert_strategy
        if self.cron_expr is not None:
            result['cronExpr'] = self.cron_expr
        if self.emr_cluster_id is not None:
            result['emrClusterId'] = self.emr_cluster_id
        if self.failure_strategy is not None:
            result['failureStrategy'] = self.failure_strategy
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.schedule_end_time is not None:
            result['scheduleEndTime'] = self.schedule_end_time
        if self.schedule_start_time is not None:
            result['scheduleStartTime'] = self.schedule_start_time
        if self.schedule_state is not None:
            result['scheduleState'] = self.schedule_state
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.workflow_instance_priority is not None:
            result['workflowInstancePriority'] = self.workflow_instance_priority
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertStrategy') is not None:
            self.alert_strategy = m.get('alertStrategy')
        if m.get('cronExpr') is not None:
            self.cron_expr = m.get('cronExpr')
        if m.get('emrClusterId') is not None:
            self.emr_cluster_id = m.get('emrClusterId')
        if m.get('failureStrategy') is not None:
            self.failure_strategy = m.get('failureStrategy')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('scheduleEndTime') is not None:
            self.schedule_end_time = m.get('scheduleEndTime')
        if m.get('scheduleStartTime') is not None:
            self.schedule_start_time = m.get('scheduleStartTime')
        if m.get('scheduleState') is not None:
            self.schedule_state = m.get('scheduleState')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('workflowInstancePriority') is not None:
            self.workflow_instance_priority = m.get('workflowInstancePriority')
        return self


class DescribeWorkflowResponseBodyTaskRelations(TeaModel):
    def __init__(
        self,
        post_task_id: str = None,
        pre_task_id: str = None,
    ):
        self.post_task_id = post_task_id
        self.pre_task_id = pre_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.post_task_id is not None:
            result['postTaskId'] = self.post_task_id
        if self.pre_task_id is not None:
            result['preTaskId'] = self.pre_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('postTaskId') is not None:
            self.post_task_id = m.get('postTaskId')
        if m.get('preTaskId') is not None:
            self.pre_task_id = m.get('preTaskId')
        return self


class DescribeWorkflowResponseBodyTasks(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        task_id: str = None,
        version: int = None,
    ):
        self.description = description
        self.name = name
        self.task_id = task_id
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.task_id is not None:
            result['taskId'] = self.task_id
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('taskId') is not None:
            self.task_id = m.get('taskId')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DescribeWorkflowResponseBodyWorkflow(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        execution_type: str = None,
        name: str = None,
        parent_directory_id: str = None,
        timeout: int = None,
        update_time: str = None,
        workflow_id: str = None,
        workflow_params: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.execution_type = execution_type
        self.name = name
        self.parent_directory_id = parent_directory_id
        self.timeout = timeout
        self.update_time = update_time
        self.workflow_id = workflow_id
        self.workflow_params = workflow_params

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
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.name is not None:
            result['name'] = self.name
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_params is not None:
            result['workflowParams'] = self.workflow_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowParams') is not None:
            self.workflow_params = m.get('workflowParams')
        return self


class DescribeWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        schedule: DescribeWorkflowResponseBodySchedule = None,
        task_relations: List[DescribeWorkflowResponseBodyTaskRelations] = None,
        tasks: List[DescribeWorkflowResponseBodyTasks] = None,
        workflow: DescribeWorkflowResponseBodyWorkflow = None,
    ):
        self.request_id = request_id
        self.schedule = schedule
        self.task_relations = task_relations
        self.tasks = tasks
        self.workflow = workflow

    def validate(self):
        if self.schedule:
            self.schedule.validate()
        if self.task_relations:
            for k in self.task_relations:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()
        if self.workflow:
            self.workflow.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.schedule is not None:
            result['schedule'] = self.schedule.to_map()
        result['taskRelations'] = []
        if self.task_relations is not None:
            for k in self.task_relations:
                result['taskRelations'].append(k.to_map() if k else None)
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        if self.workflow is not None:
            result['workflow'] = self.workflow.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('schedule') is not None:
            temp_model = DescribeWorkflowResponseBodySchedule()
            self.schedule = temp_model.from_map(m['schedule'])
        self.task_relations = []
        if m.get('taskRelations') is not None:
            for k in m.get('taskRelations'):
                temp_model = DescribeWorkflowResponseBodyTaskRelations()
                self.task_relations.append(temp_model.from_map(k))
        self.tasks = []
        if m.get('tasks') is not None:
            for k in m.get('tasks'):
                temp_model = DescribeWorkflowResponseBodyTasks()
                self.tasks.append(temp_model.from_map(k))
        if m.get('workflow') is not None:
            temp_model = DescribeWorkflowResponseBodyWorkflow()
            self.workflow = temp_model.from_map(m['workflow'])
        return self


class DescribeWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeWorkflowInstanceRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class DescribeWorkflowInstanceResponseBody(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_strategy: str = None,
        emr_cluster_id: str = None,
        end_time: str = None,
        failure_strategy: str = None,
        is_complement_data: bool = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        restart_time: str = None,
        run_times: int = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        timeout: int = None,
        workflow_id: str = None,
        workflow_instance_id: str = None,
        workflow_instance_priority: str = None,
        workflow_version: int = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_strategy = alert_strategy
        self.emr_cluster_id = emr_cluster_id
        self.end_time = end_time
        self.failure_strategy = failure_strategy
        self.is_complement_data = is_complement_data
        self.name = name
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.restart_time = restart_time
        self.run_times = run_times
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.status = status
        self.timeout = timeout
        self.workflow_id = workflow_id
        self.workflow_instance_id = workflow_instance_id
        self.workflow_instance_priority = workflow_instance_priority
        self.workflow_version = workflow_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_strategy is not None:
            result['alertStrategy'] = self.alert_strategy
        if self.emr_cluster_id is not None:
            result['emrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.failure_strategy is not None:
            result['failureStrategy'] = self.failure_strategy
        if self.is_complement_data is not None:
            result['isComplementData'] = self.is_complement_data
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.restart_time is not None:
            result['restartTime'] = self.restart_time
        if self.run_times is not None:
            result['runTimes'] = self.run_times
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workflow_instance_priority is not None:
            result['workflowInstancePriority'] = self.workflow_instance_priority
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertStrategy') is not None:
            self.alert_strategy = m.get('alertStrategy')
        if m.get('emrClusterId') is not None:
            self.emr_cluster_id = m.get('emrClusterId')
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('failureStrategy') is not None:
            self.failure_strategy = m.get('failureStrategy')
        if m.get('isComplementData') is not None:
            self.is_complement_data = m.get('isComplementData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('restartTime') is not None:
            self.restart_time = m.get('restartTime')
        if m.get('runTimes') is not None:
            self.run_times = m.get('runTimes')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workflowInstancePriority') is not None:
            self.workflow_instance_priority = m.get('workflowInstancePriority')
        if m.get('workflowVersion') is not None:
            self.workflow_version = m.get('workflowVersion')
        return self


class DescribeWorkflowInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DescribeWorkflowInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeWorkflowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlertGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListAlertGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_instance_ids: str = None,
        create_time: int = None,
        description: str = None,
        group_name: str = None,
        update_time: int = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_instance_ids = alert_instance_ids
        self.create_time = create_time
        self.description = description
        self.group_name = group_name
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_instance_ids is not None:
            result['alertInstanceIds'] = self.alert_instance_ids
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.group_name is not None:
            result['groupName'] = self.group_name
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertInstanceIds') is not None:
            self.alert_instance_ids = m.get('alertInstanceIds')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('groupName') is not None:
            self.group_name = m.get('groupName')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        return self


class ListAlertGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListAlertGroupsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListAlertGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListAlertGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlertGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListAlertGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManualTaskInstancesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        start_time: str = None,
        status: str = None,
        workspace_id: str = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.start_time = start_time
        self.status = status
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListManualTaskInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        emr_cluster_id: str = None,
        end_time: str = None,
        external_app_id: str = None,
        manual_task_instance_id: str = None,
        manual_task_instance_name: str = None,
        resource_group_id: str = None,
        start_time: str = None,
        status: str = None,
        submit_time: str = None,
        task_params: str = None,
        task_type: str = None,
    ):
        self.emr_cluster_id = emr_cluster_id
        self.end_time = end_time
        self.external_app_id = external_app_id
        self.manual_task_instance_id = manual_task_instance_id
        self.manual_task_instance_name = manual_task_instance_name
        self.resource_group_id = resource_group_id
        self.start_time = start_time
        self.status = status
        self.submit_time = submit_time
        self.task_params = task_params
        self.task_type = task_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.manual_task_instance_id is not None:
            result['ManualTaskInstanceId'] = self.manual_task_instance_id
        if self.manual_task_instance_name is not None:
            result['ManualTaskInstanceName'] = self.manual_task_instance_name
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ManualTaskInstanceId') is not None:
            self.manual_task_instance_id = m.get('ManualTaskInstanceId')
        if m.get('ManualTaskInstanceName') is not None:
            self.manual_task_instance_name = m.get('ManualTaskInstanceName')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        return self


class ListManualTaskInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListManualTaskInstancesResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListManualTaskInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListManualTaskInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListManualTaskInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManualTaskInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListManualTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        task_type: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.task_type = task_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListManualTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        manual_task_id: str = None,
        manual_task_name: str = None,
        parent_directory_id: str = None,
        project_id: str = None,
        resource_ids: str = None,
        task_params: str = None,
        task_type: str = None,
        update_time: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.manual_task_id = manual_task_id
        self.manual_task_name = manual_task_name
        self.parent_directory_id = parent_directory_id
        self.project_id = project_id
        self.resource_ids = resource_ids
        self.task_params = task_params
        self.task_type = task_type
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
        if self.description is not None:
            result['Description'] = self.description
        if self.manual_task_id is not None:
            result['ManualTaskId'] = self.manual_task_id
        if self.manual_task_name is not None:
            result['ManualTaskName'] = self.manual_task_name
        if self.parent_directory_id is not None:
            result['ParentDirectoryId'] = self.parent_directory_id
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ManualTaskId') is not None:
            self.manual_task_id = m.get('ManualTaskId')
        if m.get('ManualTaskName') is not None:
            self.manual_task_name = m.get('ManualTaskName')
        if m.get('ParentDirectoryId') is not None:
            self.parent_directory_id = m.get('ParentDirectoryId')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListManualTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListManualTasksResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListManualTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListManualTasksResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListManualTasksResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListManualTasksResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListProjectsResponseBodyData(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        project_id: str = None,
    ):
        self.description = description
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        return self


class ListProjectsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListProjectsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListProjectsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListProjectsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListProjectsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListProjectsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceGroupsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        resource_group_name: str = None,
        resource_group_type: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.resource_group_name = resource_group_name
        self.resource_group_type = resource_group_type
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name
        if self.resource_group_type is not None:
            result['resourceGroupType'] = self.resource_group_type
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')
        if m.get('resourceGroupType') is not None:
            self.resource_group_type = m.get('resourceGroupType')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListResourceGroupsResponseBodyDataAssociatedClusterTemplates(TeaModel):
    def __init__(
        self,
        cluster_type: str = None,
        template_id: str = None,
        template_name: str = None,
    ):
        self.cluster_type = cluster_type
        self.template_id = template_id
        self.template_name = template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        return self


class ListResourceGroupsResponseBodyDataAssociatedClusters(TeaModel):
    def __init__(
        self,
        cluster_id: str = None,
        cluster_name: str = None,
        cluster_type: str = None,
    ):
        self.cluster_id = cluster_id
        self.cluster_name = cluster_name
        self.cluster_type = cluster_type

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
        if self.cluster_type is not None:
            result['clusterType'] = self.cluster_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('clusterId') is not None:
            self.cluster_id = m.get('clusterId')
        if m.get('clusterName') is not None:
            self.cluster_name = m.get('clusterName')
        if m.get('clusterType') is not None:
            self.cluster_type = m.get('clusterType')
        return self


class ListResourceGroupsResponseBodyDataAssociatedWorkspaces(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
        workspace_name: str = None,
    ):
        self.workspace_id = workspace_id
        self.workspace_name = workspace_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        if self.workspace_name is not None:
            result['workspaceName'] = self.workspace_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        if m.get('workspaceName') is not None:
            self.workspace_name = m.get('workspaceName')
        return self


class ListResourceGroupsResponseBodyData(TeaModel):
    def __init__(
        self,
        associated_cluster_templates: List[ListResourceGroupsResponseBodyDataAssociatedClusterTemplates] = None,
        associated_clusters: List[ListResourceGroupsResponseBodyDataAssociatedClusters] = None,
        associated_workspaces: List[ListResourceGroupsResponseBodyDataAssociatedWorkspaces] = None,
        create_time: str = None,
        node_max_count: int = None,
        node_min_count: int = None,
        node_type: str = None,
        payment_type: str = None,
        resource_group_id: str = None,
        resource_group_name: str = None,
        resource_group_type: str = None,
    ):
        self.associated_cluster_templates = associated_cluster_templates
        self.associated_clusters = associated_clusters
        self.associated_workspaces = associated_workspaces
        self.create_time = create_time
        self.node_max_count = node_max_count
        self.node_min_count = node_min_count
        self.node_type = node_type
        self.payment_type = payment_type
        self.resource_group_id = resource_group_id
        self.resource_group_name = resource_group_name
        self.resource_group_type = resource_group_type

    def validate(self):
        if self.associated_cluster_templates:
            for k in self.associated_cluster_templates:
                if k:
                    k.validate()
        if self.associated_clusters:
            for k in self.associated_clusters:
                if k:
                    k.validate()
        if self.associated_workspaces:
            for k in self.associated_workspaces:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['associatedClusterTemplates'] = []
        if self.associated_cluster_templates is not None:
            for k in self.associated_cluster_templates:
                result['associatedClusterTemplates'].append(k.to_map() if k else None)
        result['associatedClusters'] = []
        if self.associated_clusters is not None:
            for k in self.associated_clusters:
                result['associatedClusters'].append(k.to_map() if k else None)
        result['associatedWorkspaces'] = []
        if self.associated_workspaces is not None:
            for k in self.associated_workspaces:
                result['associatedWorkspaces'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.node_max_count is not None:
            result['nodeMaxCount'] = self.node_max_count
        if self.node_min_count is not None:
            result['nodeMinCount'] = self.node_min_count
        if self.node_type is not None:
            result['nodeType'] = self.node_type
        if self.payment_type is not None:
            result['paymentType'] = self.payment_type
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.resource_group_name is not None:
            result['resourceGroupName'] = self.resource_group_name
        if self.resource_group_type is not None:
            result['resourceGroupType'] = self.resource_group_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.associated_cluster_templates = []
        if m.get('associatedClusterTemplates') is not None:
            for k in m.get('associatedClusterTemplates'):
                temp_model = ListResourceGroupsResponseBodyDataAssociatedClusterTemplates()
                self.associated_cluster_templates.append(temp_model.from_map(k))
        self.associated_clusters = []
        if m.get('associatedClusters') is not None:
            for k in m.get('associatedClusters'):
                temp_model = ListResourceGroupsResponseBodyDataAssociatedClusters()
                self.associated_clusters.append(temp_model.from_map(k))
        self.associated_workspaces = []
        if m.get('associatedWorkspaces') is not None:
            for k in m.get('associatedWorkspaces'):
                temp_model = ListResourceGroupsResponseBodyDataAssociatedWorkspaces()
                self.associated_workspaces.append(temp_model.from_map(k))
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('nodeMaxCount') is not None:
            self.node_max_count = m.get('nodeMaxCount')
        if m.get('nodeMinCount') is not None:
            self.node_min_count = m.get('nodeMinCount')
        if m.get('nodeType') is not None:
            self.node_type = m.get('nodeType')
        if m.get('paymentType') is not None:
            self.payment_type = m.get('paymentType')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('resourceGroupName') is not None:
            self.resource_group_name = m.get('resourceGroupName')
        if m.get('resourceGroupType') is not None:
            self.resource_group_type = m.get('resourceGroupType')
        return self


class ListResourceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListResourceGroupsResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListResourceGroupsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListResourceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListResourceGroupsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTaskInstancesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        start_time: str = None,
        status: str = None,
        workflow_instance_id: str = None,
        workspace_id: str = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.start_time = start_time
        self.status = status
        self.workflow_instance_id = workflow_instance_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListTaskInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        dry_run: str = None,
        emr_cluster_id: str = None,
        end_time: str = None,
        external_app_id: str = None,
        resource_group_id: str = None,
        retry_times: int = None,
        start_time: str = None,
        status: str = None,
        submit_time: str = None,
        task_id: str = None,
        task_instance_id: str = None,
        task_instance_name: str = None,
        task_params: str = None,
        task_type: str = None,
        task_version: str = None,
        workflow_instance_id: str = None,
    ):
        self.dry_run = dry_run
        self.emr_cluster_id = emr_cluster_id
        self.end_time = end_time
        self.external_app_id = external_app_id
        self.resource_group_id = resource_group_id
        self.retry_times = retry_times
        self.start_time = start_time
        self.status = status
        self.submit_time = submit_time
        self.task_id = task_id
        self.task_instance_id = task_instance_id
        self.task_instance_name = task_instance_name
        self.task_params = task_params
        self.task_type = task_type
        self.task_version = task_version
        self.workflow_instance_id = workflow_instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run
        if self.emr_cluster_id is not None:
            result['EmrClusterId'] = self.emr_cluster_id
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.external_app_id is not None:
            result['ExternalAppId'] = self.external_app_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.retry_times is not None:
            result['RetryTimes'] = self.retry_times
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.status is not None:
            result['Status'] = self.status
        if self.submit_time is not None:
            result['SubmitTime'] = self.submit_time
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_instance_id is not None:
            result['TaskInstanceId'] = self.task_instance_id
        if self.task_instance_name is not None:
            result['TaskInstanceName'] = self.task_instance_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.task_version is not None:
            result['TaskVersion'] = self.task_version
        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')
        if m.get('EmrClusterId') is not None:
            self.emr_cluster_id = m.get('EmrClusterId')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ExternalAppId') is not None:
            self.external_app_id = m.get('ExternalAppId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('RetryTimes') is not None:
            self.retry_times = m.get('RetryTimes')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubmitTime') is not None:
            self.submit_time = m.get('SubmitTime')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskInstanceId') is not None:
            self.task_instance_id = m.get('TaskInstanceId')
        if m.get('TaskInstanceName') is not None:
            self.task_instance_name = m.get('TaskInstanceName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('TaskVersion') is not None:
            self.task_version = m.get('TaskVersion')
        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')
        return self


class ListTaskInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTaskInstancesResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTaskInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListTaskInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTaskInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListTaskInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTasksRequest(TeaModel):
    def __init__(
        self,
        max_results: str = None,
        next_token: str = None,
        search_val: str = None,
        task_type: str = None,
        workflow_id: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.task_type = task_type
        self.workflow_id = workflow_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.task_type is not None:
            result['taskType'] = self.task_type
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('taskType') is not None:
            self.task_type = m.get('taskType')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListTasksResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        delay_time: int = None,
        description: str = None,
        fail_retry_interval: int = None,
        fail_retry_times: int = None,
        flag: str = None,
        project_id: str = None,
        resource_ids: str = None,
        task_id: str = None,
        task_name: str = None,
        task_params: str = None,
        task_priority: str = None,
        task_type: str = None,
        timeout: int = None,
        timeout_flag: str = None,
        timeout_notify_strategy: str = None,
        update_time: str = None,
        version: str = None,
    ):
        self.create_time = create_time
        self.delay_time = delay_time
        self.description = description
        self.fail_retry_interval = fail_retry_interval
        self.fail_retry_times = fail_retry_times
        self.flag = flag
        self.project_id = project_id
        self.resource_ids = resource_ids
        self.task_id = task_id
        self.task_name = task_name
        self.task_params = task_params
        self.task_priority = task_priority
        self.task_type = task_type
        self.timeout = timeout
        self.timeout_flag = timeout_flag
        self.timeout_notify_strategy = timeout_notify_strategy
        self.update_time = update_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.delay_time is not None:
            result['DelayTime'] = self.delay_time
        if self.description is not None:
            result['Description'] = self.description
        if self.fail_retry_interval is not None:
            result['FailRetryInterval'] = self.fail_retry_interval
        if self.fail_retry_times is not None:
            result['FailRetryTimes'] = self.fail_retry_times
        if self.flag is not None:
            result['Flag'] = self.flag
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.task_name is not None:
            result['TaskName'] = self.task_name
        if self.task_params is not None:
            result['TaskParams'] = self.task_params
        if self.task_priority is not None:
            result['TaskPriority'] = self.task_priority
        if self.task_type is not None:
            result['TaskType'] = self.task_type
        if self.timeout is not None:
            result['Timeout'] = self.timeout
        if self.timeout_flag is not None:
            result['TimeoutFlag'] = self.timeout_flag
        if self.timeout_notify_strategy is not None:
            result['TimeoutNotifyStrategy'] = self.timeout_notify_strategy
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DelayTime') is not None:
            self.delay_time = m.get('DelayTime')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FailRetryInterval') is not None:
            self.fail_retry_interval = m.get('FailRetryInterval')
        if m.get('FailRetryTimes') is not None:
            self.fail_retry_times = m.get('FailRetryTimes')
        if m.get('Flag') is not None:
            self.flag = m.get('Flag')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')
        if m.get('TaskParams') is not None:
            self.task_params = m.get('TaskParams')
        if m.get('TaskPriority') is not None:
            self.task_priority = m.get('TaskPriority')
        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')
        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')
        if m.get('TimeoutFlag') is not None:
            self.timeout_flag = m.get('TimeoutFlag')
        if m.get('TimeoutNotifyStrategy') is not None:
            self.timeout_notify_strategy = m.get('TimeoutNotifyStrategy')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class ListTasksResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListTasksResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTasksResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
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


class ListWorkflowDirectoriesRequest(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        max_results: int = None,
        next_token: str = None,
        parent_directory_id: str = None,
        workspace_id: str = None,
    ):
        self.directory_id = directory_id
        self.max_results = max_results
        self.next_token = next_token
        self.parent_directory_id = parent_directory_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowDirectoriesResponseBodyData(TeaModel):
    def __init__(
        self,
        directory_id: str = None,
        name: str = None,
        parent_directory_id: str = None,
        project_id: str = None,
        workflow_id: str = None,
    ):
        self.directory_id = directory_id
        self.name = name
        self.parent_directory_id = parent_directory_id
        self.project_id = project_id
        self.workflow_id = workflow_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.directory_id is not None:
            result['directoryId'] = self.directory_id
        if self.name is not None:
            result['name'] = self.name
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.project_id is not None:
            result['projectId'] = self.project_id
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('directoryId') is not None:
            self.directory_id = m.get('directoryId')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('projectId') is not None:
            self.project_id = m.get('projectId')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        return self


class ListWorkflowDirectoriesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListWorkflowDirectoriesResponseBodyData] = None,
        max_results: str = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        # Id of the request
        self.request_id = request_id
        self.total_count = total_count

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
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
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWorkflowDirectoriesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListWorkflowDirectoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowDirectoriesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowDirectoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowInstancesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        max_results: int = None,
        next_token: str = None,
        start_time: str = None,
        status: str = None,
        workflow_id: str = None,
        workspace_id: str = None,
    ):
        self.end_time = end_time
        self.max_results = max_results
        self.next_token = next_token
        self.start_time = start_time
        self.status = status
        self.workflow_id = workflow_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        name: str = None,
        schedule_time: str = None,
        start_time: str = None,
        status: str = None,
        workflow_id: str = None,
        workflow_instance_id: str = None,
        workflow_version: int = None,
    ):
        self.end_time = end_time
        self.name = name
        self.schedule_time = schedule_time
        self.start_time = start_time
        self.status = status
        self.workflow_id = workflow_id
        self.workflow_instance_id = workflow_instance_id
        self.workflow_version = workflow_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['endTime'] = self.end_time
        if self.name is not None:
            result['name'] = self.name
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.status is not None:
            result['status'] = self.status
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workflowVersion') is not None:
            self.workflow_version = m.get('workflowVersion')
        return self


class ListWorkflowInstancesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListWorkflowInstancesResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWorkflowInstancesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListWorkflowInstancesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowInstancesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListWorkflowsRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        workspace_id: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowsResponseBodyData(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        name: str = None,
        parent_directory_id: str = None,
        update_time: str = None,
        workflow_id: str = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.parent_directory_id = parent_directory_id
        self.update_time = update_time
        self.workflow_id = workflow_id

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
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.update_time is not None:
            result['updateTime'] = self.update_time
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        return self


class ListWorkflowsResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListWorkflowsResponseBodyData] = None,
        next_token: str = None,
        request_id: str = None,
        total_size: int = None,
    ):
        self.data = data
        self.next_token = next_token
        self.request_id = request_id
        self.total_size = total_size

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.total_size is not None:
            result['totalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListWorkflowsResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('totalSize') is not None:
            self.total_size = m.get('totalSize')
        return self


class ListWorkflowsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListWorkflowsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListWorkflowsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OperateWorkflowInstanceRequest(TeaModel):
    def __init__(
        self,
        exec_type: str = None,
        workflow_instance_id: str = None,
        workspace_id: str = None,
    ):
        self.exec_type = exec_type
        self.workflow_instance_id = workflow_instance_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exec_type is not None:
            result['execType'] = self.exec_type
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('execType') is not None:
            self.exec_type = m.get('execType')
        if m.get('workflowInstanceId') is not None:
            self.workflow_instance_id = m.get('workflowInstanceId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class OperateWorkflowInstanceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class OperateWorkflowInstanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OperateWorkflowInstanceResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = OperateWorkflowInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RunWorkflowRequest(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_strategy: str = None,
        complement_dependent_mode: str = None,
        dry_run: str = None,
        exec_type: str = None,
        expected_parallelism_number: str = None,
        failure_strategy: str = None,
        resource_group_id: str = None,
        run_mode: str = None,
        schedule_time: str = None,
        start_params: str = None,
        workflow_id: str = None,
        workflow_instance_priority: str = None,
        workspace_id: str = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_strategy = alert_strategy
        self.complement_dependent_mode = complement_dependent_mode
        self.dry_run = dry_run
        self.exec_type = exec_type
        self.expected_parallelism_number = expected_parallelism_number
        self.failure_strategy = failure_strategy
        # This parameter is required.
        self.resource_group_id = resource_group_id
        self.run_mode = run_mode
        self.schedule_time = schedule_time
        self.start_params = start_params
        # This parameter is required.
        self.workflow_id = workflow_id
        self.workflow_instance_priority = workflow_instance_priority
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_strategy is not None:
            result['alertStrategy'] = self.alert_strategy
        if self.complement_dependent_mode is not None:
            result['complementDependentMode'] = self.complement_dependent_mode
        if self.dry_run is not None:
            result['dryRun'] = self.dry_run
        if self.exec_type is not None:
            result['execType'] = self.exec_type
        if self.expected_parallelism_number is not None:
            result['expectedParallelismNumber'] = self.expected_parallelism_number
        if self.failure_strategy is not None:
            result['failureStrategy'] = self.failure_strategy
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.run_mode is not None:
            result['runMode'] = self.run_mode
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_params is not None:
            result['startParams'] = self.start_params
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_instance_priority is not None:
            result['workflowInstancePriority'] = self.workflow_instance_priority
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertStrategy') is not None:
            self.alert_strategy = m.get('alertStrategy')
        if m.get('complementDependentMode') is not None:
            self.complement_dependent_mode = m.get('complementDependentMode')
        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')
        if m.get('execType') is not None:
            self.exec_type = m.get('execType')
        if m.get('expectedParallelismNumber') is not None:
            self.expected_parallelism_number = m.get('expectedParallelismNumber')
        if m.get('failureStrategy') is not None:
            self.failure_strategy = m.get('failureStrategy')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('runMode') is not None:
            self.run_mode = m.get('runMode')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startParams') is not None:
            self.start_params = m.get('startParams')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workflowInstancePriority') is not None:
            self.workflow_instance_priority = m.get('workflowInstancePriority')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class RunWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class RunWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RunWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RunWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateWorkflowRequest(TeaModel):
    def __init__(
        self,
        alert_group_id: str = None,
        alert_strategy: str = None,
        task_definition_json_value: str = None,
        task_relation_json_value: str = None,
        cron_expr: str = None,
        description: str = None,
        execution_type: str = None,
        failure_strategy: str = None,
        name: str = None,
        parent_directory_id: str = None,
        resource_group_id: str = None,
        schedule_end_time: str = None,
        schedule_start_time: str = None,
        schedule_state: str = None,
        task_definition_json: str = None,
        task_relation_json: str = None,
        time_zone: str = None,
        timeout: int = None,
        workflow_instance_priority: str = None,
        workflow_params: str = None,
        workspace_id: str = None,
    ):
        self.alert_group_id = alert_group_id
        self.alert_strategy = alert_strategy
        self.task_definition_json_value = task_definition_json_value
        self.task_relation_json_value = task_relation_json_value
        self.cron_expr = cron_expr
        self.description = description
        self.execution_type = execution_type
        self.failure_strategy = failure_strategy
        self.name = name
        self.parent_directory_id = parent_directory_id
        self.resource_group_id = resource_group_id
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
        self.schedule_state = schedule_state
        self.task_definition_json = task_definition_json
        self.task_relation_json = task_relation_json
        self.time_zone = time_zone
        self.timeout = timeout
        self.workflow_instance_priority = workflow_instance_priority
        self.workflow_params = workflow_params
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alert_group_id is not None:
            result['alertGroupId'] = self.alert_group_id
        if self.alert_strategy is not None:
            result['alertStrategy'] = self.alert_strategy
        if self.task_definition_json_value is not None:
            result['taskDefinitionJsonValue'] = self.task_definition_json_value
        if self.task_relation_json_value is not None:
            result['taskRelationJsonValue'] = self.task_relation_json_value
        if self.cron_expr is not None:
            result['cronExpr'] = self.cron_expr
        if self.description is not None:
            result['description'] = self.description
        if self.execution_type is not None:
            result['executionType'] = self.execution_type
        if self.failure_strategy is not None:
            result['failureStrategy'] = self.failure_strategy
        if self.name is not None:
            result['name'] = self.name
        if self.parent_directory_id is not None:
            result['parentDirectoryId'] = self.parent_directory_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.schedule_end_time is not None:
            result['scheduleEndTime'] = self.schedule_end_time
        if self.schedule_start_time is not None:
            result['scheduleStartTime'] = self.schedule_start_time
        if self.schedule_state is not None:
            result['scheduleState'] = self.schedule_state
        if self.task_definition_json is not None:
            result['taskDefinitionJson'] = self.task_definition_json
        if self.task_relation_json is not None:
            result['taskRelationJson'] = self.task_relation_json
        if self.time_zone is not None:
            result['timeZone'] = self.time_zone
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.workflow_instance_priority is not None:
            result['workflowInstancePriority'] = self.workflow_instance_priority
        if self.workflow_params is not None:
            result['workflowParams'] = self.workflow_params
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertGroupId') is not None:
            self.alert_group_id = m.get('alertGroupId')
        if m.get('alertStrategy') is not None:
            self.alert_strategy = m.get('alertStrategy')
        if m.get('taskDefinitionJsonValue') is not None:
            self.task_definition_json_value = m.get('taskDefinitionJsonValue')
        if m.get('taskRelationJsonValue') is not None:
            self.task_relation_json_value = m.get('taskRelationJsonValue')
        if m.get('cronExpr') is not None:
            self.cron_expr = m.get('cronExpr')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')
        if m.get('failureStrategy') is not None:
            self.failure_strategy = m.get('failureStrategy')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parentDirectoryId') is not None:
            self.parent_directory_id = m.get('parentDirectoryId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('scheduleEndTime') is not None:
            self.schedule_end_time = m.get('scheduleEndTime')
        if m.get('scheduleStartTime') is not None:
            self.schedule_start_time = m.get('scheduleStartTime')
        if m.get('scheduleState') is not None:
            self.schedule_state = m.get('scheduleState')
        if m.get('taskDefinitionJson') is not None:
            self.task_definition_json = m.get('taskDefinitionJson')
        if m.get('taskRelationJson') is not None:
            self.task_relation_json = m.get('taskRelationJson')
        if m.get('timeZone') is not None:
            self.time_zone = m.get('timeZone')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workflowInstancePriority') is not None:
            self.workflow_instance_priority = m.get('workflowInstancePriority')
        if m.get('workflowParams') is not None:
            self.workflow_params = m.get('workflowParams')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class UpdateWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
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
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class UpdateWorkflowResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateWorkflowResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateWorkflowResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


