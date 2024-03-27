# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class DescribeManualTaskRequest(TeaModel):
    def __init__(
        self,
        workspace_id: str = None,
    ):
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
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 描述
        self.description = description
        # 代表资源一级ID的资源属性字段
        self.manual_task_id = manual_task_id
        # 代表资源名称的资源属性字段
        self.manual_task_name = manual_task_name
        # 目录ID
        self.parent_directory_id = parent_directory_id
        # 项目ID
        self.project_id = project_id
        # 资源id列表
        self.resource_ids = resource_ids
        # 任务参数
        self.task_params = task_params
        # 任务类型
        self.task_type = task_type
        # 更新时间
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
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id
        # 结束时间
        self.end_time = end_time
        # 外部应用ID
        self.external_app_id = external_app_id
        # 代表资源一级ID的资源属性字段
        self.manual_task_instance_id = manual_task_instance_id
        # 代表资源名称的资源属性字段
        self.manual_task_instance_name = manual_task_instance_name
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 开始时间
        self.start_time = start_time
        # 状态
        self.status = status
        # 提交时间
        self.submit_time = submit_time
        # 任务参数
        self.task_params = task_params
        # 任务类型
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
        code: int = None,
        description: str = None,
        name: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.description = description
        self.name = name
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
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('name') is not None:
            self.name = m.get('name')
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
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 延时执行时间
        self.delay_time = delay_time
        # 描述
        self.description = description
        # 失败重试间隔
        self.fail_retry_interval = fail_retry_interval
        # 失败重试次数
        self.fail_retry_times = fail_retry_times
        # 运行标志
        self.flag = flag
        # 项目ID
        self.project_id = project_id
        # 资源ID列表
        self.resource_ids = resource_ids
        # 代表资源一级ID的资源属性字段
        self.task_id = task_id
        # 代表资源名称的资源属性字段
        self.task_name = task_name
        # 任务参数
        self.task_params = task_params
        # 任务优先级
        self.task_priority = task_priority
        # 任务类型
        self.task_type = task_type
        # 超时时长
        self.timeout = timeout
        # 超时告警标志
        self.timeout_flag = timeout_flag
        # 超时告警标志
        self.timeout_notify_strategy = timeout_notify_strategy
        # 更新时间
        self.update_time = update_time
        # 版本
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
        # 空跑标识
        self.dry_run = dry_run
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id
        # 结束时间
        self.end_time = end_time
        # 外部应用ID
        self.external_app_id = external_app_id
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 重试次数
        self.retry_times = retry_times
        # 开始时间
        self.start_time = start_time
        # 状态
        self.status = status
        # 提交时间
        self.submit_time = submit_time
        # 任务ID
        self.task_id = task_id
        # 任务实例ID
        self.task_instance_id = task_instance_id
        # 任务实例名称
        self.task_instance_name = task_instance_name
        # 任务参数
        self.task_params = task_params
        # 任务类型
        self.task_type = task_type
        # 任务版本
        self.task_version = task_version
        # 工作流实例ID
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
        workspace_id: int = None,
    ):
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


class DescribeWorkflowResponseBodyTaskRelations(TeaModel):
    def __init__(
        self,
        name: str = None,
        post_task_id: int = None,
        post_task_version: int = None,
        pre_task_id: int = None,
        pre_task_version: int = None,
    ):
        self.name = name
        self.post_task_id = post_task_id
        self.post_task_version = post_task_version
        self.pre_task_id = pre_task_id
        self.pre_task_version = pre_task_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.post_task_id is not None:
            result['postTaskId'] = self.post_task_id
        if self.post_task_version is not None:
            result['postTaskVersion'] = self.post_task_version
        if self.pre_task_id is not None:
            result['preTaskId'] = self.pre_task_id
        if self.pre_task_version is not None:
            result['preTaskVersion'] = self.pre_task_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('postTaskId') is not None:
            self.post_task_id = m.get('postTaskId')
        if m.get('postTaskVersion') is not None:
            self.post_task_version = m.get('postTaskVersion')
        if m.get('preTaskId') is not None:
            self.pre_task_id = m.get('preTaskId')
        if m.get('preTaskVersion') is not None:
            self.pre_task_version = m.get('preTaskVersion')
        return self


class DescribeWorkflowResponseBodyTasks(TeaModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        task_id: int = None,
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


class DescribeWorkflowResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        task_relations: List[DescribeWorkflowResponseBodyTaskRelations] = None,
        tasks: List[DescribeWorkflowResponseBodyTasks] = None,
    ):
        self.request_id = request_id
        self.task_relations = task_relations
        self.tasks = tasks

    def validate(self):
        if self.task_relations:
            for k in self.task_relations:
                if k:
                    k.validate()
        if self.tasks:
            for k in self.tasks:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        result['taskRelations'] = []
        if self.task_relations is not None:
            for k in self.task_relations:
                result['taskRelations'].append(k.to_map() if k else None)
        result['tasks'] = []
        if self.tasks is not None:
            for k in self.tasks:
                result['tasks'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
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
        workspace_id: int = None,
    ):
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
        emr_cluster_id: str = None,
        end_date: str = None,
        is_complement_data: bool = None,
        name: str = None,
        request_id: str = None,
        resource_group_id: str = None,
        run_times: int = None,
        schedule_time: str = None,
        start_date: str = None,
        state: str = None,
        timeout: int = None,
        workflow_id: int = None,
        workflow_version: int = None,
    ):
        self.emr_cluster_id = emr_cluster_id
        self.end_date = end_date
        self.is_complement_data = is_complement_data
        self.name = name
        self.request_id = request_id
        self.resource_group_id = resource_group_id
        self.run_times = run_times
        self.schedule_time = schedule_time
        self.start_date = start_date
        self.state = state
        self.timeout = timeout
        self.workflow_id = workflow_id
        self.workflow_version = workflow_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.emr_cluster_id is not None:
            result['emrClusterId'] = self.emr_cluster_id
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.is_complement_data is not None:
            result['isComplementData'] = self.is_complement_data
        if self.name is not None:
            result['name'] = self.name
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id
        if self.run_times is not None:
            result['runTimes'] = self.run_times
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.state is not None:
            result['state'] = self.state
        if self.timeout is not None:
            result['timeout'] = self.timeout
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('emrClusterId') is not None:
            self.emr_cluster_id = m.get('emrClusterId')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('isComplementData') is not None:
            self.is_complement_data = m.get('isComplementData')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')
        if m.get('runTimes') is not None:
            self.run_times = m.get('runTimes')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('timeout') is not None:
            self.timeout = m.get('timeout')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
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


class ListManualTaskInstancesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        execution_status: str = None,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        start_time: str = None,
        workspace_id: str = None,
    ):
        self.end_time = end_time
        self.execution_status = execution_status
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.start_time = start_time
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
        if self.execution_status is not None:
            result['executionStatus'] = self.execution_status
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionStatus') is not None:
            self.execution_status = m.get('executionStatus')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
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
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id
        # 结束时间
        self.end_time = end_time
        # 外部应用ID
        self.external_app_id = external_app_id
        # 代表资源一级ID的资源属性字段
        self.manual_task_instance_id = manual_task_instance_id
        # 代表资源名称的资源属性字段
        self.manual_task_instance_name = manual_task_instance_name
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 开始时间
        self.start_time = start_time
        # 状态
        self.status = status
        # 提交时间
        self.submit_time = submit_time
        # 任务参数
        self.task_params = task_params
        # 任务类型
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
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 描述
        self.description = description
        # 代表资源一级ID的资源属性字段
        self.manual_task_id = manual_task_id
        # 代表资源名称的资源属性字段
        self.manual_task_name = manual_task_name
        # 目录ID
        self.parent_directory_id = parent_directory_id
        # 项目ID
        self.project_id = project_id
        # 资源id列表
        self.resource_ids = resource_ids
        # 任务参数
        self.task_params = task_params
        # 任务类型
        self.task_type = task_type
        # 更新时间
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
        workspace_id: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
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
        code: int = None,
        description: str = None,
        name: str = None,
        project_id: int = None,
    ):
        self.code = code
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
        if self.code is not None:
            result['code'] = self.code
        if self.description is not None:
            result['description'] = self.description
        if self.name is not None:
            result['name'] = self.name
        if self.project_id is not None:
            result['projectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
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
    ):
        self.data = data
        self.next_token = next_token
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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
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


class ListTaskInstancesRequest(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        execution_status: str = None,
        max_results: int = None,
        next_token: str = None,
        search_val: str = None,
        start_time: str = None,
        workflow_instance_id: str = None,
        workspace_id: str = None,
    ):
        self.end_time = end_time
        self.execution_status = execution_status
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
        self.start_time = start_time
        self.workflow_instance_id = workflow_instance_id
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
        if self.execution_status is not None:
            result['executionStatus'] = self.execution_status
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.search_val is not None:
            result['searchVal'] = self.search_val
        if self.start_time is not None:
            result['startTime'] = self.start_time
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')
        if m.get('executionStatus') is not None:
            self.execution_status = m.get('executionStatus')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('searchVal') is not None:
            self.search_val = m.get('searchVal')
        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')
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
        # 空跑标识
        self.dry_run = dry_run
        # EMR集群ID
        self.emr_cluster_id = emr_cluster_id
        # 结束时间
        self.end_time = end_time
        # 外部应用ID
        self.external_app_id = external_app_id
        # 资源组ID
        self.resource_group_id = resource_group_id
        # 重试次数
        self.retry_times = retry_times
        # 开始时间
        self.start_time = start_time
        # 状态
        self.status = status
        # 提交时间
        self.submit_time = submit_time
        # 任务ID
        self.task_id = task_id
        # 任务实例ID
        self.task_instance_id = task_instance_id
        # 任务实例名称
        self.task_instance_name = task_instance_name
        # 任务参数
        self.task_params = task_params
        # 任务类型
        self.task_type = task_type
        # 任务版本
        self.task_version = task_version
        # 工作流实例ID
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
        # 代表创建时间的资源属性字段
        self.create_time = create_time
        # 延时执行时间
        self.delay_time = delay_time
        # 描述
        self.description = description
        # 失败重试间隔
        self.fail_retry_interval = fail_retry_interval
        # 失败重试次数
        self.fail_retry_times = fail_retry_times
        # 运行标志
        self.flag = flag
        # 项目ID
        self.project_id = project_id
        # 资源ID列表
        self.resource_ids = resource_ids
        # 代表资源一级ID的资源属性字段
        self.task_id = task_id
        # 代表资源名称的资源属性字段
        self.task_name = task_name
        # 任务参数
        self.task_params = task_params
        # 任务优先级
        self.task_priority = task_priority
        # 任务类型
        self.task_type = task_type
        # 超时时长
        self.timeout = timeout
        # 超时告警标志
        self.timeout_flag = timeout_flag
        # 超时告警标志
        self.timeout_notify_strategy = timeout_notify_strategy
        # 更新时间
        self.update_time = update_time
        # 版本
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


class ListWorkflowInstancesRequest(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        max_results: int = None,
        next_token: str = None,
        start_date: str = None,
        workflow_id: int = None,
        workspace_id: int = None,
    ):
        self.end_date = end_date
        self.max_results = max_results
        self.next_token = next_token
        self.start_date = start_date
        self.workflow_id = workflow_id
        self.workspace_id = workspace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('workflowId') is not None:
            self.workflow_id = m.get('workflowId')
        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')
        return self


class ListWorkflowInstancesResponseBodyData(TeaModel):
    def __init__(
        self,
        end_date: str = None,
        name: str = None,
        run_times: str = None,
        schedule_time: str = None,
        start_date: str = None,
        state: str = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_version: str = None,
    ):
        self.end_date = end_date
        self.name = name
        self.run_times = run_times
        self.schedule_time = schedule_time
        self.start_date = start_date
        self.state = state
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
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.name is not None:
            result['name'] = self.name
        if self.run_times is not None:
            result['runTimes'] = self.run_times
        if self.schedule_time is not None:
            result['scheduleTime'] = self.schedule_time
        if self.start_date is not None:
            result['startDate'] = self.start_date
        if self.state is not None:
            result['state'] = self.state
        if self.workflow_id is not None:
            result['workflowId'] = self.workflow_id
        if self.workflow_instance_id is not None:
            result['workflowInstanceId'] = self.workflow_instance_id
        if self.workflow_version is not None:
            result['workflowVersion'] = self.workflow_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('runTimes') is not None:
            self.run_times = m.get('runTimes')
        if m.get('scheduleTime') is not None:
            self.schedule_time = m.get('scheduleTime')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        if m.get('state') is not None:
            self.state = m.get('state')
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
        workspace_id: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.search_val = search_val
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
        release_state: str = None,
        update_time: str = None,
        workflow_id: int = None,
    ):
        self.create_time = create_time
        self.description = description
        self.name = name
        self.release_state = release_state
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
        if self.release_state is not None:
            result['releaseState'] = self.release_state
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
        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')
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


