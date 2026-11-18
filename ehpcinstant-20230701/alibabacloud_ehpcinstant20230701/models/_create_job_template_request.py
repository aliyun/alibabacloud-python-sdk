# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class CreateJobTemplateRequest(DaraModel):
    def __init__(
        self,
        job_template_config: main_models.CreateJobTemplateRequestJobTemplateConfig = None,
        job_template_description: str = None,
        job_template_name: str = None,
    ):
        # The configuration of the template.
        self.job_template_config = job_template_config
        # The description of the template.
        self.job_template_description = job_template_description
        # The name of the template.
        # 
        # This parameter is required.
        self.job_template_name = job_template_name

    def validate(self):
        if self.job_template_config:
            self.job_template_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_template_config is not None:
            result['JobTemplateConfig'] = self.job_template_config.to_map()

        if self.job_template_description is not None:
            result['JobTemplateDescription'] = self.job_template_description

        if self.job_template_name is not None:
            result['JobTemplateName'] = self.job_template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobTemplateConfig') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfig()
            self.job_template_config = temp_model.from_map(m.get('JobTemplateConfig'))

        if m.get('JobTemplateDescription') is not None:
            self.job_template_description = m.get('JobTemplateDescription')

        if m.get('JobTemplateName') is not None:
            self.job_template_name = m.get('JobTemplateName')

        return self

class CreateJobTemplateRequestJobTemplateConfig(DaraModel):
    def __init__(
        self,
        deployment_policy: main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicy = None,
        job_description: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        security_policy: main_models.CreateJobTemplateRequestJobTemplateConfigSecurityPolicy = None,
        tasks: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasks] = None,
    ):
        # The resource deployment policy.
        self.deployment_policy = deployment_policy
        # The description of the job.
        self.job_description = job_description
        # The name of the job.
        self.job_name = job_name
        self.job_scheduler = job_scheduler
        # The security policy.
        self.security_policy = security_policy
        # The list of tasks. A maximum of 5 tasks are supported.
        self.tasks = tasks

    def validate(self):
        if self.deployment_policy:
            self.deployment_policy.validate()
        if self.security_policy:
            self.security_policy.validate()
        if self.tasks:
            for v1 in self.tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeploymentPolicy') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m.get('DeploymentPolicy'))

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        if m.get('SecurityPolicy') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigSecurityPolicy()
            self.security_policy = temp_model.from_map(m.get('SecurityPolicy'))

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class CreateJobTemplateRequestJobTemplateConfigTasks(DaraModel):
    def __init__(
        self,
        executor_policy: main_models.CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicy = None,
        task_name: str = None,
        task_spec: main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpec = None,
        task_sustainable: bool = None,
    ):
        # The task execution policy.
        self.executor_policy = executor_policy
        # The name of the task.
        self.task_name = task_name
        # The specification details of the task.
        self.task_spec = task_spec
        # Specifies whether the job is a long-running job. Valid values:
        # - true: The job is a background service job.
        # - false: The job is a batch job.
        # Default value: false.
        self.task_sustainable = task_sustainable

    def validate(self):
        if self.executor_policy:
            self.executor_policy.validate()
        if self.task_spec:
            self.task_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.executor_policy is not None:
            result['ExecutorPolicy'] = self.executor_policy.to_map()

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
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m.get('ExecutorPolicy'))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskSpec') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpec()
            self.task_spec = temp_model.from_map(m.get('TaskSpec'))

        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpec(DaraModel):
    def __init__(
        self,
        resource: main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResource = None,
        retry_policy: main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicy = None,
        task_executor: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutor] = None,
        volume_mount: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecVolumeMount] = None,
    ):
        # The resource information of the runtime environment.
        self.resource = resource
        # The retry policy of the task.
        self.retry_policy = retry_policy
        # The execution configuration of the task.
        self.task_executor = task_executor
        # The list of data volumes mounted to the task. A maximum of 10 data volumes are supported.
        self.volume_mount = volume_mount

    def validate(self):
        if self.resource:
            self.resource.validate()
        if self.retry_policy:
            self.retry_policy.validate()
        if self.task_executor:
            for v1 in self.task_executor:
                 if v1:
                    v1.validate()
        if self.volume_mount:
            for v1 in self.volume_mount:
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

        result['VolumeMount'] = []
        if self.volume_mount is not None:
            for k1 in self.volume_mount:
                result['VolumeMount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('RetryPolicy') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicy()
            self.retry_policy = temp_model.from_map(m.get('RetryPolicy'))

        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k1 in m.get('TaskExecutor'):
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k1))

        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k1 in m.get('VolumeMount'):
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecVolumeMount()
                self.volume_mount.append(temp_model.from_map(k1))

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecVolumeMount(DaraModel):
    def __init__(
        self,
        mount_options: str = None,
        mount_path: str = None,
        read_only: bool = None,
        volume_driver: str = None,
    ):
        # The list of mount parameters for the data volume. The parameters are in key-value pair format and passed in JSON.
        self.mount_options = mount_options
        # The directory where the data volume is mounted to the task.
        self.mount_path = mount_path
        # Specifies whether the data volume is read-only.
        self.read_only = read_only
        # The type of the data volume.
        self.volume_driver = volume_driver

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_options is not None:
            result['MountOptions'] = self.mount_options

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.read_only is not None:
            result['ReadOnly'] = self.read_only

        if self.volume_driver is not None:
            result['VolumeDriver'] = self.volume_driver

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountOptions') is not None:
            self.mount_options = m.get('MountOptions')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('ReadOnly') is not None:
            self.read_only = m.get('ReadOnly')

        if m.get('VolumeDriver') is not None:
            self.volume_driver = m.get('VolumeDriver')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutor(DaraModel):
    def __init__(
        self,
        container: main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainer = None,
        vm: main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorVM = None,
    ):
        # The container environment configuration.
        self.container = container
        # The virtual machine environment configuration.
        self.vm = vm

    def validate(self):
        if self.container:
            self.container.validate()
        if self.vm:
            self.vm.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.container is not None:
            result['Container'] = self.container.to_map()

        if self.vm is not None:
            result['VM'] = self.vm.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Container') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('VM') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m.get('VM'))

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorVM(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        image: str = None,
        password: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        # The ID of the virtual machine application.
        self.app_id = app_id
        # The image ID.
        self.image = image
        # The logon password for the virtual machine environment.
        self.password = password
        # The prolog script. The script must be Base64-encoded.
        self.prolog_script = prolog_script
        # The job execution script. The script must be Base64-encoded.
        self.script = script

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.image is not None:
            result['Image'] = self.image

        if self.password is not None:
            result['Password'] = self.password

        if self.prolog_script is not None:
            result['PrologScript'] = self.prolog_script

        if self.script is not None:
            result['Script'] = self.script

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainer(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        arg: List[str] = None,
        command: List[str] = None,
        environment_vars: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainerEnvironmentVars] = None,
        gpu_driver_version: str = None,
        image: str = None,
        image_registry_options: str = None,
        privileged: bool = None,
        working_dir: str = None,
    ):
        # The ID of the container application.
        self.app_id = app_id
        # The arguments for the container startup commands.
        self.arg = arg
        # The list of startup commands for the container.
        self.command = command
        # The environment variables of the container.
        self.environment_vars = environment_vars
        # The GPU driver version.
        self.gpu_driver_version = gpu_driver_version
        # The container image.
        self.image = image
        # The list of mount parameters for the custom image registry. The parameters are in key-value pair format and passed in JSON.
        self.image_registry_options = image_registry_options
        # Specifies whether the container runs in privileged mode. Default value: false.
        self.privileged = privileged
        # The working directory of the container.
        self.working_dir = working_dir

    def validate(self):
        if self.environment_vars:
            for v1 in self.environment_vars:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.arg is not None:
            result['Arg'] = self.arg

        if self.command is not None:
            result['Command'] = self.command

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

        if self.gpu_driver_version is not None:
            result['GpuDriverVersion'] = self.gpu_driver_version

        if self.image is not None:
            result['Image'] = self.image

        if self.image_registry_options is not None:
            result['ImageRegistryOptions'] = self.image_registry_options

        if self.privileged is not None:
            result['Privileged'] = self.privileged

        if self.working_dir is not None:
            result['WorkingDir'] = self.working_dir

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Arg') is not None:
            self.arg = m.get('Arg')

        if m.get('Command') is not None:
            self.command = m.get('Command')

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainerEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('GpuDriverVersion') is not None:
            self.gpu_driver_version = m.get('GpuDriverVersion')

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageRegistryOptions') is not None:
            self.image_registry_options = m.get('ImageRegistryOptions')

        if m.get('Privileged') is not None:
            self.privileged = m.get('Privileged')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecTaskExecutorContainerEnvironmentVars(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The name of the environment variable.
        self.name = name
        # The value of the environment variable.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicy(DaraModel):
    def __init__(
        self,
        exit_code_actions: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicyExitCodeActions] = None,
        retry_count: int = None,
    ):
        # The retry rules.
        self.exit_code_actions = exit_code_actions
        # The number of retries.
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
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicyExitCodeActions()
                self.exit_code_actions.append(temp_model.from_map(k1))

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecRetryPolicyExitCodeActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        exit_code: int = None,
    ):
        # The next action of the task. Valid values:
        # - Retry: Retries the task.
        # - Exit: Exits the task.
        self.action = action
        # The exit code of the task. This code is used together with the Action parameter to form the retry rules for the job. Valid values: 0 to 255.
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

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResource(DaraModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResourceDisks] = None,
        enable_ht: bool = None,
        host_name_prefix: str = None,
        instance_types: List[str] = None,
        memory: float = None,
    ):
        # The number of CPU cores in the runtime environment.
        self.cores = cores
        # The array of cloud disks.
        self.disks = disks
        # Specifies whether hyper-threading is enabled in the runtime environment.
        self.enable_ht = enable_ht
        # The hostname prefix of the runtime environment.
        self.host_name_prefix = host_name_prefix
        # The instance types of the runtime environment.
        self.instance_types = instance_types
        # The memory size of the runtime environment. Unit: GiB.
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
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResourceDisks()
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

class CreateJobTemplateRequestJobTemplateConfigTasksTaskSpecResourceDisks(DaraModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        # The size of the cloud disk. Unit: GiB.
        self.size = size
        # The type of the cloud disk.
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

class CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicy(DaraModel):
    def __init__(
        self,
        array_spec: main_models.CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicyArraySpec = None,
        max_count: int = None,
    ):
        # The details of the array job.
        self.array_spec = array_spec
        # The maximum number of nodes on which the job can run.
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
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m.get('ArraySpec'))

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        return self

class CreateJobTemplateRequestJobTemplateConfigTasksExecutorPolicyArraySpec(DaraModel):
    def __init__(
        self,
        index_end: int = None,
        index_start: int = None,
        index_step: int = None,
    ):
        # The end value of the array job index. Valid values: 0 to 4999. The value must be greater than or equal to the value of IndexStart.
        self.index_end = index_end
        # The start value of the array job index. Valid values: 0 to 4999.
        self.index_start = index_start
        # The step size of the array job index.
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

class CreateJobTemplateRequestJobTemplateConfigSecurityPolicy(DaraModel):
    def __init__(
        self,
        security_group: main_models.CreateJobTemplateRequestJobTemplateConfigSecurityPolicySecurityGroup = None,
    ):
        # The security group.
        self.security_group = security_group

    def validate(self):
        if self.security_group:
            self.security_group.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group is not None:
            result['SecurityGroup'] = self.security_group.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroup') is not None:
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigSecurityPolicySecurityGroup()
            self.security_group = temp_model.from_map(m.get('SecurityGroup'))

        return self

class CreateJobTemplateRequestJobTemplateConfigSecurityPolicySecurityGroup(DaraModel):
    def __init__(
        self,
        security_group_ids: List[str] = None,
    ):
        # The security group IDs.
        self.security_group_ids = security_group_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')

        return self

class CreateJobTemplateRequestJobTemplateConfigDeploymentPolicy(DaraModel):
    def __init__(
        self,
        allocation_spec: str = None,
        level: str = None,
        network: main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyNetwork = None,
        pool: str = None,
        priority: int = None,
        tags: List[main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyTags] = None,
    ):
        # The resource type.
        self.allocation_spec = allocation_spec
        # The computing power level. This parameter is valid only when the resource type is economy. Valid values:
        # - General: general-purpose.
        # - Performance: performance-enhanced.
        self.level = level
        # The network configuration.
        self.network = network
        # The resource pool of the job.
        self.pool = pool
        # The priority of the job. A larger value indicates a higher scheduling priority for the job.
        self.priority = priority
        # The tags of the job.
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

        if self.pool is not None:
            result['Pool'] = self.pool

        if self.priority is not None:
            result['Priority'] = self.priority

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
            temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Pool') is not None:
            self.pool = m.get('Pool')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class CreateJobTemplateRequestJobTemplateConfigDeploymentPolicyNetwork(DaraModel):
    def __init__(
        self,
        enable_external_ip_address: bool = None,
        vswitch: List[str] = None,
    ):
        # Specifies whether to assign a public IP address to the job. Default value: false.
        self.enable_external_ip_address = enable_external_ip_address
        # The vSwitches.
        self.vswitch = vswitch

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_external_ip_address is not None:
            result['EnableExternalIpAddress'] = self.enable_external_ip_address

        if self.vswitch is not None:
            result['Vswitch'] = self.vswitch

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableExternalIpAddress') is not None:
            self.enable_external_ip_address = m.get('EnableExternalIpAddress')

        if m.get('Vswitch') is not None:
            self.vswitch = m.get('Vswitch')

        return self

