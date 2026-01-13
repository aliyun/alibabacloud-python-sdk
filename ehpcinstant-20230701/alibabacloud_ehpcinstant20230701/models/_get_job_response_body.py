# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class GetJobResponseBody(DaraModel):
    def __init__(
        self,
        job_info: main_models.GetJobResponseBodyJobInfo = None,
        request_id: str = None,
    ):
        # The job details.
        self.job_info = job_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.job_info:
            self.job_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_info is not None:
            result['JobInfo'] = self.job_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobInfo') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfo()
            self.job_info = temp_model.from_map(m.get('JobInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetJobResponseBodyJobInfo(DaraModel):
    def __init__(
        self,
        app_extra_info: str = None,
        create_time: str = None,
        dependency_policy: main_models.GetJobResponseBodyJobInfoDependencyPolicy = None,
        deployment_policy: main_models.GetJobResponseBodyJobInfoDeploymentPolicy = None,
        end_time: str = None,
        job_description: str = None,
        job_id: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        start_time: str = None,
        status: str = None,
        tasks: List[main_models.GetJobResponseBodyJobInfoTasks] = None,
    ):
        # The additional information about the application.
        self.app_extra_info = app_extra_info
        # The time when the job was submitted.
        self.create_time = create_time
        self.dependency_policy = dependency_policy
        # The resource deployment policy.
        self.deployment_policy = deployment_policy
        # The time when the job is complete.
        self.end_time = end_time
        # The description of the job.
        self.job_description = job_description
        # The ID of the job.
        self.job_id = job_id
        # The job name.
        self.job_name = job_name
        # The type of the job scheduler.
        self.job_scheduler = job_scheduler
        # The time when the job started.
        self.start_time = start_time
        # The job status. Valid values:
        # 
        # *   Pending: The job is being queued.
        # *   Initing: The job is being initialized.
        # *   Succeed: The job is successfully run.
        # *   Failed: The job failed to run.
        # *   Running: The job is running.
        # *   Exception: scheduling exception
        # *   Retrying: The job is being retried.
        # *   Expired: The job timed out.
        # *   Deleted: The job is deleted.
        # *   Suspended: job hibernation
        # *   Restarting: The job is being restarted.
        self.status = status
        # The list of tasks. Only one task is supported.
        self.tasks = tasks

    def validate(self):
        if self.dependency_policy:
            self.dependency_policy.validate()
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_extra_info is not None:
            result['AppExtraInfo'] = self.app_extra_info

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dependency_policy is not None:
            result['DependencyPolicy'] = self.dependency_policy.to_map()

        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppExtraInfo') is not None:
            self.app_extra_info = m.get('AppExtraInfo')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DependencyPolicy') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoDependencyPolicy()
            self.dependency_policy = temp_model.from_map(m.get('DependencyPolicy'))

        if m.get('DeploymentPolicy') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m.get('DeploymentPolicy'))

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.GetJobResponseBodyJobInfoTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class GetJobResponseBodyJobInfoTasks(DaraModel):
    def __init__(
        self,
        executor_policy: main_models.GetJobResponseBodyJobInfoTasksExecutorPolicy = None,
        executor_status: List[main_models.GetJobResponseBodyJobInfoTasksExecutorStatus] = None,
        task_name: str = None,
        task_spec: main_models.GetJobResponseBodyJobInfoTasksTaskSpec = None,
        task_sustainable: bool = None,
    ):
        # The task execution policy.
        self.executor_policy = executor_policy
        # The execution status of the task.
        self.executor_status = executor_status
        # The name of the task.
        self.task_name = task_name
        # The details of the task specification.
        self.task_spec = task_spec
        # Indicate whether the job is a long-running job.
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.executor_status:
            for v1 in self.executor_status:
                 if v1:
                    v1.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()

        result['ExecutorStatus'] = []
        if self.executor_status is not None:
            for k1 in self.executor_status:
                result['ExecutorStatus'].append(k1.to_map() if k1 else None)

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_spec is not None:
            result['TaskSpec'] = self.task_spec.to_map()

        if self.task_sustainable is not None:
            result['TaskSustainable'] = self.task_sustainable

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecutorPolicy') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m.get('ExecutorPolicy'))

        self.executor_status = []
        if m.get('ExecutorStatus') is not None:
            for k1 in m.get('ExecutorStatus'):
                temp_model = main_models.GetJobResponseBodyJobInfoTasksExecutorStatus()
                self.executor_status.append(temp_model.from_map(k1))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskSpec') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpec()
            self.task_spec = temp_model.from_map(m.get('TaskSpec'))

        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')

        return self

class GetJobResponseBodyJobInfoTasksTaskSpec(DaraModel):
    def __init__(
        self,
        resource: main_models.GetJobResponseBodyJobInfoTasksTaskSpecResource = None,
        retry_policy: main_models.GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicy = None,
        task_executor: List[main_models.GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor] = None,
    ):
        # The resource information.
        self.resource = resource
        self.retry_policy = retry_policy
        # The task execution configurations.
        self.task_executor = task_executor

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.retry_policy:
            self.retry_policy.validate()
        if self.task_executor:
            for v1 in self.task_executor:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource is not None:
            result['Resource'] = self.resource.to_map()

        if self.retry_policy is not None:
            result['RetryPolicy'] = self.retry_policy.to_map()

        result['TaskExecutor'] = []
        if self.task_executor is not None:
            for k1 in self.task_executor:
                result['TaskExecutor'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('RetryPolicy') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicy()
            self.retry_policy = temp_model.from_map(m.get('RetryPolicy'))

        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k1 in m.get('TaskExecutor'):
                temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k1))

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutor(DaraModel):
    def __init__(
        self,
        vm: main_models.GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM = None,
    ):
        # Use ECS instances.
        self.vm = vm

    def validate(self):
        if self.vm:
            self.vm.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.vm is not None:
            result['VM'] = self.vm.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VM') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m.get('VM'))

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecTaskExecutorVM(DaraModel):
    def __init__(
        self,
        image: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        # The image ID.
        self.image = image
        # The pre-processing script. Base64 encoding is required.
        self.prolog_script = prolog_script
        # The running-job script. Base64 encoding is required.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image is not None:
            result['Image'] = self.image

        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicy(DaraModel):
    def __init__(
        self,
        exit_code_actions: List[main_models.GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicyExitCodeActions] = None,
        retry_count: int = None,
    ):
        self.exit_code_actions = exit_code_actions
        self.retry_count = retry_count

    def validate(self):
        if self.exit_code_actions:
            for v1 in self.exit_code_actions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ExitCodeActions'] = []
        if self.exit_code_actions is not None:
            for k1 in self.exit_code_actions:
                result['ExitCodeActions'].append(k1.to_map() if k1 else None)

        if self.retry_count is not None:
            result['RetryCount'] = self.retry_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.exit_code_actions = []
        if m.get('ExitCodeActions') is not None:
            for k1 in m.get('ExitCodeActions'):
                temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicyExitCodeActions()
                self.exit_code_actions.append(temp_model.from_map(k1))

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecRetryPolicyExitCodeActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        exit_code: int = None,
    ):
        self.action = action
        self.exit_code = exit_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecResource(DaraModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[main_models.GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks] = None,
        enable_ht: bool = None,
        host_name_prefix: str = None,
        instance_types: List[str] = None,
        memory: int = None,
    ):
        # The number of CPUs on which the job is run.
        self.cores = cores
        # The array of the disks.
        self.disks = disks
        self.enable_ht = enable_ht
        self.host_name_prefix = host_name_prefix
        self.instance_types = instance_types
        # The memory capacity. Unit: GiB.
        self.memory = memory

    def validate(self):
        if self.disks:
            for v1 in self.disks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cores is not None:
            result['Cores'] = self.cores

        result['Disks'] = []
        if self.disks is not None:
            for k1 in self.disks:
                result['Disks'].append(k1.to_map() if k1 else None)

        if self.enable_ht is not None:
            result['EnableHT'] = self.enable_ht

        if self.host_name_prefix is not None:
            result['HostNamePrefix'] = self.host_name_prefix

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.memory is not None:
            result['Memory'] = self.memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cores') is not None:
            self.cores = m.get('Cores')

        self.disks = []
        if m.get('Disks') is not None:
            for k1 in m.get('Disks'):
                temp_model = main_models.GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks()
                self.disks.append(temp_model.from_map(k1))

        if m.get('EnableHT') is not None:
            self.enable_ht = m.get('EnableHT')

        if m.get('HostNamePrefix') is not None:
            self.host_name_prefix = m.get('HostNamePrefix')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        return self

class GetJobResponseBodyJobInfoTasksTaskSpecResourceDisks(DaraModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        # The size of the disk.
        self.size = size
        # The type of the disk. The following disk categories are supported:
        # 
        # *   System: system disk.
        # *   Data: data disk.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.size is not None:
            result['Size'] = self.size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetJobResponseBodyJobInfoTasksExecutorStatus(DaraModel):
    def __init__(
        self,
        array_id: int = None,
        create_time: str = None,
        end_time: str = None,
        start_time: str = None,
        status: str = None,
        status_reason: str = None,
    ):
        # Sub-job ID
        self.array_id = array_id
        # The time when the job was created.
        self.create_time = create_time
        # The end time of the scaling plan job.
        self.end_time = end_time
        # The start time of the scaling plan job.
        self.start_time = start_time
        # The status of the job.
        self.status = status
        # The reason why the stack instance is in the OUTDATED state.
        self.status_reason = status_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_id is not None:
            result['ArrayId'] = self.array_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.status is not None:
            result['Status'] = self.status

        if self.status_reason is not None:
            result['StatusReason'] = self.status_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArrayId') is not None:
            self.array_id = m.get('ArrayId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusReason') is not None:
            self.status_reason = m.get('StatusReason')

        return self

class GetJobResponseBodyJobInfoTasksExecutorPolicy(DaraModel):
    def __init__(
        self,
        array_spec: main_models.GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec = None,
        max_count: int = None,
    ):
        # The details of the array job.
        self.array_spec = array_spec
        # The maximum number of nodes to run the job.
        self.max_count = max_count

    def validate(self):
        if self.array_spec:
            self.array_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.array_spec is not None:
            result['ArraySpec'] = self.array_spec.to_map()

        if self.max_count is not None:
            result['MaxCount'] = self.max_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ArraySpec') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m.get('ArraySpec'))

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        return self

class GetJobResponseBodyJobInfoTasksExecutorPolicyArraySpec(DaraModel):
    def __init__(
        self,
        index_end: int = None,
        index_start: int = None,
        index_step: int = None,
    ):
        # The end value of the array job index. Valid values: 0 to 4999. The value must be greater than or equal to the value of IndexStart.
        self.index_end = index_end
        # The starting value of the array job index. Valid values: 0 to 4999.
        self.index_start = index_start
        # The interval of the array job index.
        # 
        # > If the array job property is IndexStart=1,IndexEnd=5, and IndexStep=2, the array job contains three subtasks. The values of the subtask indexes are 1,3, and 5.
        self.index_step = index_step

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.index_end is not None:
            result['IndexEnd'] = self.index_end

        if self.index_start is not None:
            result['IndexStart'] = self.index_start

        if self.index_step is not None:
            result['IndexStep'] = self.index_step

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IndexEnd') is not None:
            self.index_end = m.get('IndexEnd')

        if m.get('IndexStart') is not None:
            self.index_start = m.get('IndexStart')

        if m.get('IndexStep') is not None:
            self.index_step = m.get('IndexStep')

        return self

class GetJobResponseBodyJobInfoDeploymentPolicy(DaraModel):
    def __init__(
        self,
        allocation_spec: str = None,
        level: str = None,
        network: main_models.GetJobResponseBodyJobInfoDeploymentPolicyNetwork = None,
        tags: List[main_models.GetJobResponseBodyJobInfoDeploymentPolicyTags] = None,
    ):
        # The type of the resource. Only Dedicated is supported. You must enable a whitelist.
        self.allocation_spec = allocation_spec
        # The computing power level. The following disk categories are supported:
        # 
        # *   General
        # *   Performance
        # 
        # Default value: General
        self.level = level
        # The network configuration information.
        self.network = network
        # The list of job tags.
        self.tags = tags

    def validate(self):
        if self.network:
            self.network.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allocation_spec is not None:
            result['AllocationSpec'] = self.allocation_spec

        if self.level is not None:
            result['Level'] = self.level

        if self.network is not None:
            result['Network'] = self.network.to_map()

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Network') is not None:
            temp_model = main_models.GetJobResponseBodyJobInfoDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.GetJobResponseBodyJobInfoDeploymentPolicyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class GetJobResponseBodyJobInfoDeploymentPolicyTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        # The key of the job tag.
        self.tag_key = tag_key
        # The value of the job tag.
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class GetJobResponseBodyJobInfoDeploymentPolicyNetwork(DaraModel):
    def __init__(
        self,
        enable_enimapping: bool = None,
        enable_external_ip_address: bool = None,
        vswitch: List[str] = None,
    ):
        # Whether the resource is created in the zone corresponding to the passed-in VSwitch parameter.
        # 
        # *   true: The resource is created in the zone corresponding to the passed-in VSwitch parameter.
        # *   false: The resource is created in any zone that has resources.
        self.enable_enimapping = enable_enimapping
        # Whether to create a public IP address.
        # 
        # Valid values:
        # 
        # *   false: false.
        # *   true: true.
        self.enable_external_ip_address = enable_external_ip_address
        # The VSwitch array.
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_enimapping is not None:
            result['EnableENIMapping'] = self.enable_enimapping

        if self.enable_external_ip_address is not None:
            result['EnableExternalIpAddress'] = self.enable_external_ip_address

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableENIMapping') is not None:
            self.enable_enimapping = m.get('EnableENIMapping')

        if m.get('EnableExternalIpAddress') is not None:
            self.enable_external_ip_address = m.get('EnableExternalIpAddress')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        return self

class GetJobResponseBodyJobInfoDependencyPolicy(DaraModel):
    def __init__(
        self,
        job_dependency: List[main_models.GetJobResponseBodyJobInfoDependencyPolicyJobDependency] = None,
    ):
        self.job_dependency = job_dependency

    def validate(self):
        if self.job_dependency:
            for v1 in self.job_dependency:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['JobDependency'] = []
        if self.job_dependency is not None:
            for k1 in self.job_dependency:
                result['JobDependency'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.job_dependency = []
        if m.get('JobDependency') is not None:
            for k1 in m.get('JobDependency'):
                temp_model = main_models.GetJobResponseBodyJobInfoDependencyPolicyJobDependency()
                self.job_dependency.append(temp_model.from_map(k1))

        return self

class GetJobResponseBodyJobInfoDependencyPolicyJobDependency(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        type: str = None,
    ):
        self.job_id = job_id
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

