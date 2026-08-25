# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class ListUpstreamTaskInstancesResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # The request ID, which is used to locate logs and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        task_instances: List[main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstances] = None,
        total_count: int = None,
        upstream_task_instances: List[main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstances] = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # **[Deprecated]** The list of task instances. This field is deprecated. Use UpstreamTaskInstances instead.
        self.task_instances = task_instances
        # The total number of records.
        self.total_count = total_count
        # The list of upstream task instances.
        self.upstream_task_instances = upstream_task_instances

    def validate(self):
        if self.task_instances:
            for v1 in self.task_instances:
                 if v1:
                    v1.validate()
        if self.upstream_task_instances:
            for v1 in self.upstream_task_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['TaskInstances'] = []
        if self.task_instances is not None:
            for k1 in self.task_instances:
                result['TaskInstances'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['UpstreamTaskInstances'] = []
        if self.upstream_task_instances is not None:
            for k1 in self.upstream_task_instances:
                result['UpstreamTaskInstances'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.task_instances = []
        if m.get('TaskInstances') is not None:
            for k1 in m.get('TaskInstances'):
                temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstances()
                self.task_instances.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.upstream_task_instances = []
        if m.get('UpstreamTaskInstances') is not None:
            for k1 in m.get('UpstreamTaskInstances'):
                temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstances()
                self.upstream_task_instances.append(temp_model.from_map(k1))

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstances(DaraModel):
    def __init__(
        self,
        dependency_type: str = None,
        task_instance: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstance = None,
    ):
        # The dependency type.
        self.dependency_type = dependency_type
        # The details of the task instance.
        self.task_instance = task_instance

    def validate(self):
        if self.task_instance:
            self.task_instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dependency_type is not None:
            result['DependencyType'] = self.dependency_type

        if self.task_instance is not None:
            result['TaskInstance'] = self.task_instance.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependencyType') is not None:
            self.dependency_type = m.get('DependencyType')

        if m.get('TaskInstance') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstance()
            self.task_instance = temp_model.from_map(m.get('TaskInstance'))

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstance(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        bizdate: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceDataSource = None,
        description: str = None,
        env_type: str = None,
        finished_time: int = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        owner: str = None,
        period_number: int = None,
        priority: int = None,
        project_id: int = None,
        rerun_mode: str = None,
        run_number: int = None,
        runtime: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntime = None,
        runtime_resource: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntimeResource = None,
        started_time: int = None,
        status: str = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
        timeout: int = None,
        trigger_recurrence: str = None,
        trigger_time: int = None,
        trigger_type: str = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_instance_type: str = None,
        workflow_name: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The business date.
        self.bizdate = bizdate
        # The creation time.
        self.create_time = create_time
        # The account ID of the user who created the instance.
        self.create_user = create_user
        # The data source information associated with the instance.
        self.data_source = data_source
        # The description.
        self.description = description
        # The environment of the target data source. Valid values:
        self.env_type = env_type
        # The time when the instance finished running.
        self.finished_time = finished_time
        # The unique identifier of the task instance.
        self.id = id
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the user who last modified the instance.
        self.modify_user = modify_user
        # The account ID of the task owner.
        self.owner = owner
        # The period number. Indicates which scheduling cycle of the day the task instance belongs to.
        self.period_number = period_number
        # The task running priority. Minimum value: 1. Maximum value: 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The project ID.
        self.project_id = project_id
        # The configuration that specifies whether the task can be rerun.
        self.rerun_mode = rerun_mode
        # The current run number, starting from 1 by default.
        self.run_number = run_number
        # The instance runtime information.
        self.runtime = runtime
        # The runtime environment configuration, such as resource group information.
        self.runtime_resource = runtime_resource
        # The time when the instance started running.
        self.started_time = started_time
        # The instance running status.
        self.status = status
        # The ID of the corresponding task.
        self.task_id = task_id
        # The name of the corresponding task.
        self.task_name = task_name
        # The type of the corresponding task.
        self.task_type = task_type
        # The timeout period for task execution, in seconds.
        self.timeout = timeout
        # The run mode when the instance is triggered. This parameter takes effect when TriggerType is set to Scheduler.
        # 
        # Valid values:
        # - Pause: paused.
        # - Skip: dry run.
        # - Normal: normal run.
        self.trigger_recurrence = trigger_recurrence
        # The scheduled trigger time.
        self.trigger_time = trigger_time
        # The trigger type.
        self.trigger_type = trigger_type
        # The ID of the workflow to which the instance belongs.
        self.workflow_id = workflow_id
        # The ID of the workflow instance to which the instance belongs.
        self.workflow_instance_id = workflow_instance_id
        # The type of the workflow instance to which the instance belongs.
        self.workflow_instance_type = workflow_instance_type
        # The name of the workflow to which the instance belongs.
        self.workflow_name = workflow_name

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime:
            self.runtime.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.period_number is not None:
            result['PeriodNumber'] = self.period_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.run_number is not None:
            result['RunNumber'] = self.run_number

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_instance_type is not None:
            result['WorkflowInstanceType'] = self.workflow_instance_type

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PeriodNumber') is not None:
            self.period_number = m.get('PeriodNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RunNumber') is not None:
            self.run_number = m.get('RunNumber')

        if m.get('Runtime') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowInstanceType') is not None:
            self.workflow_instance_type = m.get('WorkflowInstanceType')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The compute unit (CU) consumption configured for the task.
        self.cu = cu
        # The image ID configured for the task.
        self.image = image
        # The identifier of the schedule resource group configured for the task.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.image is not None:
            result['Image'] = self.image

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceRuntime(DaraModel):
    def __init__(
        self,
        gateway: str = None,
        process_id: str = None,
    ):
        # The machine on which the task runs.
        self.gateway = gateway
        # The unique run ID.
        self.process_id = process_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoUpstreamTaskInstancesTaskInstanceDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The data source name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstances(DaraModel):
    def __init__(
        self,
        baseline_id: int = None,
        bizdate: int = None,
        create_time: int = None,
        create_user: str = None,
        data_source: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesDataSource = None,
        description: str = None,
        env_type: str = None,
        finished_time: int = None,
        id: int = None,
        modify_time: int = None,
        modify_user: str = None,
        owner: str = None,
        period_number: int = None,
        priority: int = None,
        project_env: str = None,
        project_id: int = None,
        rerun_mode: str = None,
        run_number: int = None,
        runtime: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntime = None,
        runtime_resource: main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntimeResource = None,
        started_time: int = None,
        status: str = None,
        step_type: str = None,
        task_id: int = None,
        task_name: str = None,
        task_type: str = None,
        timeout: int = None,
        trigger_recurrence: str = None,
        trigger_time: int = None,
        trigger_type: str = None,
        workflow_id: int = None,
        workflow_instance_id: int = None,
        workflow_instance_type: str = None,
        workflow_name: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The business date.
        self.bizdate = bizdate
        # The creation time.
        self.create_time = create_time
        # The account ID of the user who created the instance.
        self.create_user = create_user
        # The data source information associated with the instance.
        self.data_source = data_source
        # The description.
        self.description = description
        # The project environment.
        self.env_type = env_type
        # The time when the instance finished running.
        self.finished_time = finished_time
        # The unique identifier of the task instance.
        self.id = id
        # The modification time.
        self.modify_time = modify_time
        # The account ID of the user who last modified the instance.
        self.modify_user = modify_user
        # The account ID of the task owner.
        self.owner = owner
        # The period number. Indicates which scheduling cycle of the day the task instance belongs to.
        self.period_number = period_number
        # The task running priority. Minimum value: 1. Maximum value: 8. A larger value indicates a higher priority. Default value: 1.
        self.priority = priority
        # The project environment.
        self.project_env = project_env
        # The project ID.
        self.project_id = project_id
        # The rerun configuration of the node. Valid values:
        # - AllDenied: The node cannot be rerun regardless of whether it fails or succeeds.
        # - FailureAllowed: The node can be rerun only after it fails.
        # - AllAllowed: The node can be rerun regardless of whether it fails or succeeds.
        self.rerun_mode = rerun_mode
        # The current run number, starting from 1 by default.
        self.run_number = run_number
        # The instance runtime information.
        self.runtime = runtime
        # The runtime environment configuration, such as resource group information.
        self.runtime_resource = runtime_resource
        # The time when the instance started running.
        self.started_time = started_time
        # The instance running status.
        self.status = status
        # The dependency type.
        self.step_type = step_type
        # The ID of the corresponding task.
        self.task_id = task_id
        # The name of the corresponding task.
        self.task_name = task_name
        # The type of the corresponding task.
        self.task_type = task_type
        # The timeout period for task execution, in seconds.
        self.timeout = timeout
        # The run mode when the instance is triggered. This parameter takes effect when TriggerType is set to Scheduler.
        # 
        # Valid values:
        # - Pause: paused
        # - Skip: dry run
        # - Normal: normal execution
        self.trigger_recurrence = trigger_recurrence
        # The scheduled trigger time.
        self.trigger_time = trigger_time
        # The trigger type.
        self.trigger_type = trigger_type
        # The ID of the workflow to which the instance belongs.
        self.workflow_id = workflow_id
        # The ID of the workflow instance to which the instance belongs.
        self.workflow_instance_id = workflow_instance_id
        # The type of the workflow instance to which the instance belongs.
        self.workflow_instance_type = workflow_instance_type
        # The name of the workflow to which the instance belongs.
        self.workflow_name = workflow_name

    def validate(self):
        if self.data_source:
            self.data_source.validate()
        if self.runtime:
            self.runtime.validate()
        if self.runtime_resource:
            self.runtime_resource.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.bizdate is not None:
            result['Bizdate'] = self.bizdate

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_source is not None:
            result['DataSource'] = self.data_source.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.finished_time is not None:
            result['FinishedTime'] = self.finished_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.modify_user is not None:
            result['ModifyUser'] = self.modify_user

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.period_number is not None:
            result['PeriodNumber'] = self.period_number

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_env is not None:
            result['ProjectEnv'] = self.project_env

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.rerun_mode is not None:
            result['RerunMode'] = self.rerun_mode

        if self.run_number is not None:
            result['RunNumber'] = self.run_number

        if self.runtime is not None:
            result['Runtime'] = self.runtime.to_map()

        if self.runtime_resource is not None:
            result['RuntimeResource'] = self.runtime_resource.to_map()

        if self.started_time is not None:
            result['StartedTime'] = self.started_time

        if self.status is not None:
            result['Status'] = self.status

        if self.step_type is not None:
            result['StepType'] = self.step_type

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        if self.trigger_recurrence is not None:
            result['TriggerRecurrence'] = self.trigger_recurrence

        if self.trigger_time is not None:
            result['TriggerTime'] = self.trigger_time

        if self.trigger_type is not None:
            result['TriggerType'] = self.trigger_type

        if self.workflow_id is not None:
            result['WorkflowId'] = self.workflow_id

        if self.workflow_instance_id is not None:
            result['WorkflowInstanceId'] = self.workflow_instance_id

        if self.workflow_instance_type is not None:
            result['WorkflowInstanceType'] = self.workflow_instance_type

        if self.workflow_name is not None:
            result['WorkflowName'] = self.workflow_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('Bizdate') is not None:
            self.bizdate = m.get('Bizdate')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataSource') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesDataSource()
            self.data_source = temp_model.from_map(m.get('DataSource'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('FinishedTime') is not None:
            self.finished_time = m.get('FinishedTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('ModifyUser') is not None:
            self.modify_user = m.get('ModifyUser')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('PeriodNumber') is not None:
            self.period_number = m.get('PeriodNumber')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectEnv') is not None:
            self.project_env = m.get('ProjectEnv')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('RerunMode') is not None:
            self.rerun_mode = m.get('RerunMode')

        if m.get('RunNumber') is not None:
            self.run_number = m.get('RunNumber')

        if m.get('Runtime') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntime()
            self.runtime = temp_model.from_map(m.get('Runtime'))

        if m.get('RuntimeResource') is not None:
            temp_model = main_models.ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntimeResource()
            self.runtime_resource = temp_model.from_map(m.get('RuntimeResource'))

        if m.get('StartedTime') is not None:
            self.started_time = m.get('StartedTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StepType') is not None:
            self.step_type = m.get('StepType')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        if m.get('TriggerRecurrence') is not None:
            self.trigger_recurrence = m.get('TriggerRecurrence')

        if m.get('TriggerTime') is not None:
            self.trigger_time = m.get('TriggerTime')

        if m.get('TriggerType') is not None:
            self.trigger_type = m.get('TriggerType')

        if m.get('WorkflowId') is not None:
            self.workflow_id = m.get('WorkflowId')

        if m.get('WorkflowInstanceId') is not None:
            self.workflow_instance_id = m.get('WorkflowInstanceId')

        if m.get('WorkflowInstanceType') is not None:
            self.workflow_instance_type = m.get('WorkflowInstanceType')

        if m.get('WorkflowName') is not None:
            self.workflow_name = m.get('WorkflowName')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntimeResource(DaraModel):
    def __init__(
        self,
        cu: str = None,
        image: str = None,
        resource_group_id: str = None,
    ):
        # The compute unit (CU) consumption configured for the task.
        self.cu = cu
        # The image ID configured for the task.
        self.image = image
        # The identifier of the schedule resource group configured for the task.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cu is not None:
            result['Cu'] = self.cu

        if self.image is not None:
            result['Image'] = self.image

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cu') is not None:
            self.cu = m.get('Cu')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesRuntime(DaraModel):
    def __init__(
        self,
        gateway: str = None,
        process_id: str = None,
    ):
        # The machine on which the task runs.
        self.gateway = gateway
        # The unique run ID.
        self.process_id = process_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.gateway is not None:
            result['Gateway'] = self.gateway

        if self.process_id is not None:
            result['ProcessId'] = self.process_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Gateway') is not None:
            self.gateway = m.get('Gateway')

        if m.get('ProcessId') is not None:
            self.process_id = m.get('ProcessId')

        return self

class ListUpstreamTaskInstancesResponseBodyPagingInfoTaskInstancesDataSource(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The data source name.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

