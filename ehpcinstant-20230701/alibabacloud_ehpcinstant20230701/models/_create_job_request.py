# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpcinstant20230701 import models as main_models
from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        dependency_policy: main_models.CreateJobRequestDependencyPolicy = None,
        deployment_policy: main_models.CreateJobRequestDeploymentPolicy = None,
        job_description: str = None,
        job_name: str = None,
        job_scheduler: str = None,
        job_template_id: str = None,
        security_policy: main_models.CreateJobRequestSecurityPolicy = None,
        tasks: List[main_models.CreateJobRequestTasks] = None,
    ):
        # The dependency policy.
        self.dependency_policy = dependency_policy
        # The resource deployment policy.
        self.deployment_policy = deployment_policy
        # The job description.
        self.job_description = job_description
        # The job name. The name must be 2 to 64 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        # 
        # This parameter is required.
        self.job_name = job_name
        self.job_scheduler = job_scheduler
        # The job template ID.
        self.job_template_id = job_template_id
        # The security policy.
        self.security_policy = security_policy
        # The task list. Currently, only one task is supported.
        # 
        # This parameter is required.
        self.tasks = tasks

    def validate(self):
        if self.dependency_policy:
            self.dependency_policy.validate()
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
        if self.dependency_policy is not None:
            result['DependencyPolicy'] = self.dependency_policy.to_map()

        if self.deployment_policy is not None:
            result['DeploymentPolicy'] = self.deployment_policy.to_map()

        if self.job_description is not None:
            result['JobDescription'] = self.job_description

        if self.job_name is not None:
            result['JobName'] = self.job_name

        if self.job_scheduler is not None:
            result['JobScheduler'] = self.job_scheduler

        if self.job_template_id is not None:
            result['JobTemplateId'] = self.job_template_id

        if self.security_policy is not None:
            result['SecurityPolicy'] = self.security_policy.to_map()

        result['Tasks'] = []
        if self.tasks is not None:
            for k1 in self.tasks:
                result['Tasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DependencyPolicy') is not None:
            temp_model = main_models.CreateJobRequestDependencyPolicy()
            self.dependency_policy = temp_model.from_map(m.get('DependencyPolicy'))

        if m.get('DeploymentPolicy') is not None:
            temp_model = main_models.CreateJobRequestDeploymentPolicy()
            self.deployment_policy = temp_model.from_map(m.get('DeploymentPolicy'))

        if m.get('JobDescription') is not None:
            self.job_description = m.get('JobDescription')

        if m.get('JobName') is not None:
            self.job_name = m.get('JobName')

        if m.get('JobScheduler') is not None:
            self.job_scheduler = m.get('JobScheduler')

        if m.get('JobTemplateId') is not None:
            self.job_template_id = m.get('JobTemplateId')

        if m.get('SecurityPolicy') is not None:
            temp_model = main_models.CreateJobRequestSecurityPolicy()
            self.security_policy = temp_model.from_map(m.get('SecurityPolicy'))

        self.tasks = []
        if m.get('Tasks') is not None:
            for k1 in m.get('Tasks'):
                temp_model = main_models.CreateJobRequestTasks()
                self.tasks.append(temp_model.from_map(k1))

        return self

class CreateJobRequestTasks(DaraModel):
    def __init__(
        self,
        executor_policy: main_models.CreateJobRequestTasksExecutorPolicy = None,
        task_name: str = None,
        task_spec: main_models.CreateJobRequestTasksTaskSpec = None,
        task_sustainable: bool = None,
    ):
        # The task execution policy.
        self.executor_policy = executor_policy
        # The task name. The name must be 2 to 32 characters in length and can contain letters, digits, hyphens (-), and underscores (_).
        self.task_name = task_name
        # The task specification details.
        self.task_spec = task_spec
        # Specifies whether the job is a long-running job. Valid values:
        # - true: background service job.
        # - false: batch job.
        # 
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
            temp_model = main_models.CreateJobRequestTasksExecutorPolicy()
            self.executor_policy = temp_model.from_map(m.get('ExecutorPolicy'))

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskSpec') is not None:
            temp_model = main_models.CreateJobRequestTasksTaskSpec()
            self.task_spec = temp_model.from_map(m.get('TaskSpec'))

        if m.get('TaskSustainable') is not None:
            self.task_sustainable = m.get('TaskSustainable')

        return self

class CreateJobRequestTasksTaskSpec(DaraModel):
    def __init__(
        self,
        resource: main_models.CreateJobRequestTasksTaskSpecResource = None,
        retry_policy: main_models.CreateJobRequestTasksTaskSpecRetryPolicy = None,
        task_executor: List[main_models.CreateJobRequestTasksTaskSpecTaskExecutor] = None,
        volume_mount: List[main_models.CreateJobRequestTasksTaskSpecVolumeMount] = None,
    ):
        # The resource information of the runtime environment.
        self.resource = resource
        # The task retry policy.
        self.retry_policy = retry_policy
        # The task execution configuration.
        # 
        # This parameter is required.
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
            temp_model = main_models.CreateJobRequestTasksTaskSpecResource()
            self.resource = temp_model.from_map(m.get('Resource'))

        if m.get('RetryPolicy') is not None:
            temp_model = main_models.CreateJobRequestTasksTaskSpecRetryPolicy()
            self.retry_policy = temp_model.from_map(m.get('RetryPolicy'))

        self.task_executor = []
        if m.get('TaskExecutor') is not None:
            for k1 in m.get('TaskExecutor'):
                temp_model = main_models.CreateJobRequestTasksTaskSpecTaskExecutor()
                self.task_executor.append(temp_model.from_map(k1))

        self.volume_mount = []
        if m.get('VolumeMount') is not None:
            for k1 in m.get('VolumeMount'):
                temp_model = main_models.CreateJobRequestTasksTaskSpecVolumeMount()
                self.volume_mount.append(temp_model.from_map(k1))

        return self

class CreateJobRequestTasksTaskSpecVolumeMount(DaraModel):
    def __init__(
        self,
        mount_options: str = None,
        mount_path: str = None,
        read_only: bool = None,
        volume_driver: str = None,
    ):
        # The list of volume mount parameters. Passed as key-value pairs in JSON format.
        # - Reference format for mounting NAS: {"server":"xxxxx-xxxxx.cn-heyuan.nas.aliyuncs.com","vers":"3","path":"/data","options":"nolock,tcp,noresvport"}
        # > server specifies the mount target address of the NAS file system. path specifies a subdirectory under the NAS path, starting with /, and the directory must already exist. vers specifies the NFS protocol version for mounting NAS. Version 3 is recommended. options specifies custom parameters for mounting NAS, in the format "xxx,xxx,xxx".
        # 
        # - Reference format for mounting OSS: {"bucket":"xxxxx", "url":"oss-cn-heyuan-internal.aliyuncs.com","path":"/data","akId":"xxxxx","akSecret":"xxxxx"}
        # > bucket specifies the name of the OSS bucket. url specifies the endpoint of the OSS bucket. You can log on to the OSS console and obtain the endpoint on the overview page of the target bucket. path specifies the directory structure relative to the root of the bucket when mounting. The default value is /. The directory must already exist. akId specifies the AccessKey ID used for direct authorization with an AccessKey pair. akSecret specifies the AccessKey secret used for direct authorization with an AccessKey pair.
        self.mount_options = mount_options
        # The directory where the data volume is mounted to the task.
        self.mount_path = mount_path
        # Specifies whether the data volume is read-only. Default value: false.
        self.read_only = read_only
        # The supported data volume type. Valid values:
        # - alicloud/nas: mounts a NAS file system.
        # - alicloud/oss: mounts an OSS bucket.
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

class CreateJobRequestTasksTaskSpecTaskExecutor(DaraModel):
    def __init__(
        self,
        container: main_models.CreateJobRequestTasksTaskSpecTaskExecutorContainer = None,
        vm: main_models.CreateJobRequestTasksTaskSpecTaskExecutorVM = None,
    ):
        # The container environment settings.
        self.container = container
        # The virtual machine environment settings.
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
            temp_model = main_models.CreateJobRequestTasksTaskSpecTaskExecutorContainer()
            self.container = temp_model.from_map(m.get('Container'))

        if m.get('VM') is not None:
            temp_model = main_models.CreateJobRequestTasksTaskSpecTaskExecutorVM()
            self.vm = temp_model.from_map(m.get('VM'))

        return self

class CreateJobRequestTasksTaskSpecTaskExecutorVM(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        environment_vars: List[main_models.CreateJobRequestTasksTaskSpecTaskExecutorVMEnvironmentVars] = None,
        image: str = None,
        password: str = None,
        prolog_script: str = None,
        script: str = None,
    ):
        # The virtual machine application ID.
        self.app_id = app_id
        self.environment_vars = environment_vars
        # The image ID.
        # 
        # This parameter is required.
        self.image = image
        # The logon password for the virtual machine environment. The password must be 8 to 30 characters in length and must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. Supported special characters are:
        # 
        # ()`~!@#$%^&*-_+=|{}[]:;\\"<>,.?/
        # 
        # For Windows environments, the password cannot start with a forward slash (/).
        # 
        # > If you specify the Password parameter, use HTTPS to send the request to prevent password leakage.
        self.password = password
        # The pre-processing script. The script must be Base64-encoded.
        self.prolog_script = prolog_script
        # The job execution script. The script must be Base64-encoded.
        self.script = script

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

        result['EnvironmentVars'] = []
        if self.environment_vars is not None:
            for k1 in self.environment_vars:
                result['EnvironmentVars'].append(k1.to_map() if k1 else None)

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

        self.environment_vars = []
        if m.get('EnvironmentVars') is not None:
            for k1 in m.get('EnvironmentVars'):
                temp_model = main_models.CreateJobRequestTasksTaskSpecTaskExecutorVMEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('PrologScript') is not None:
            self.prolog_script = m.get('PrologScript')

        if m.get('Script') is not None:
            self.script = m.get('Script')

        return self

class CreateJobRequestTasksTaskSpecTaskExecutorVMEnvironmentVars(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        self.name = name
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

class CreateJobRequestTasksTaskSpecTaskExecutorContainer(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        arg: List[str] = None,
        command: List[str] = None,
        environment_vars: List[main_models.CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars] = None,
        image: str = None,
        image_registry_options: str = None,
        working_dir: str = None,
    ):
        # The container application ID.
        self.app_id = app_id
        # The arguments for the container startup command. A maximum of 10 arguments are supported.
        self.arg = arg
        # The list of container startup commands. A maximum of 20 commands are supported. Each command can contain up to 256 characters.
        # > 1. If a startup command contains spaces (for example, `sleep 60s`), pass the JSON parameter as `["sleep", "60s"]`.
        # > 2. If a startup command is complex, use a combination of `Command: ["/bin/bash"]` and `Arg:["-c", "<customized command>"]`, where `<customized command>` is a user-defined command that can contain spaces and other characters.
        self.command = command
        # The environment variables of the container. A maximum of 20 environment variables are supported.
        self.environment_vars = environment_vars
        # The container image.
        # 
        # This parameter is required.
        self.image = image
        # The list of mount parameters for a self-managed image registry. The parameters are in key-value format and passed as a JSON string.
        # 
        # - Reference format: {"ImageRegistryType":"https","ImageRegistryServer":"xxx","ImageRegistryUserName":"xxx","ImageRegistryPassword":"xxx"}
        self.image_registry_options = image_registry_options
        # The container working directory.
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

        if self.image is not None:
            result['Image'] = self.image

        if self.image_registry_options is not None:
            result['ImageRegistryOptions'] = self.image_registry_options

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
                temp_model = main_models.CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars()
                self.environment_vars.append(temp_model.from_map(k1))

        if m.get('Image') is not None:
            self.image = m.get('Image')

        if m.get('ImageRegistryOptions') is not None:
            self.image_registry_options = m.get('ImageRegistryOptions')

        if m.get('WorkingDir') is not None:
            self.working_dir = m.get('WorkingDir')

        return self

class CreateJobRequestTasksTaskSpecTaskExecutorContainerEnvironmentVars(DaraModel):
    def __init__(
        self,
        name: str = None,
        value: str = None,
    ):
        # The environment variable name. The name must be 1 to 128 characters in length. The format is [0-9a-zA-Z] and underscores. The name cannot start with a digit.
        self.name = name
        # The environment variable value. The value can be 0 to 256 characters in length.
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

class CreateJobRequestTasksTaskSpecRetryPolicy(DaraModel):
    def __init__(
        self,
        exit_code_actions: List[main_models.CreateJobRequestTasksTaskSpecRetryPolicyExitCodeActions] = None,
        retry_count: int = None,
    ):
        # The retry rules. A maximum of 10 rules are supported.
        self.exit_code_actions = exit_code_actions
        # The number of retries. Valid values: 1 to 10. Default value: 3.
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
                temp_model = main_models.CreateJobRequestTasksTaskSpecRetryPolicyExitCodeActions()
                self.exit_code_actions.append(temp_model.from_map(k1))

        if m.get('RetryCount') is not None:
            self.retry_count = m.get('RetryCount')

        return self

class CreateJobRequestTasksTaskSpecRetryPolicyExitCodeActions(DaraModel):
    def __init__(
        self,
        action: str = None,
        exit_code: int = None,
    ):
        # The next action for the node. Valid values:
        # 
        # - Retry: When a specific exit code is matched, the job starts a new retry.
        # 
        # - Exit: When a specific exit code is matched, the job exits.
        # 
        # This parameter is required.
        self.action = action
        # The task exit code, which is used together with Action to form a job retry rule. Valid values: 0 to 255.
        # 
        # This parameter is required.
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

class CreateJobRequestTasksTaskSpecResource(DaraModel):
    def __init__(
        self,
        cores: float = None,
        disks: List[main_models.CreateJobRequestTasksTaskSpecResourceDisks] = None,
        enable_ht: bool = None,
        host_name_prefix: str = None,
        instance_types: List[str] = None,
        memory: float = None,
    ):
        # The number of CPUs in the runtime environment.
        self.cores = cores
        # The cloud disk array.
        self.disks = disks
        # Specifies whether hyper-threading is enabled in the runtime environment. Default value: true.
        self.enable_ht = enable_ht
        # The hostname prefix of the runtime environment. The following limits apply:
        # 
        # - A period (.) and a hyphen (-) cannot be used as the first or last character, or consecutively.
        # - Windows environment: The value can be up to 10 characters in length, cannot contain periods (.), and cannot consist of digits only. Uppercase and lowercase letters, digits, and hyphens (-) are allowed.
        # - Linux environment: The value can be up to 32 characters in length and can contain multiple periods (.). The hostname is divided into segments by periods. Each segment can contain uppercase and lowercase letters, digits, and hyphens (-).
        self.host_name_prefix = host_name_prefix
        # The instance types of the runtime environment. A maximum of 5 instance types are supported.
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
                temp_model = main_models.CreateJobRequestTasksTaskSpecResourceDisks()
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

class CreateJobRequestTasksTaskSpecResourceDisks(DaraModel):
    def __init__(
        self,
        size: int = None,
        type: str = None,
    ):
        # The cloud disk size. Unit: GiB.
        self.size = size
        # The cloud disk type. Currently, only System is supported, which indicates a system cloud disk.
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

class CreateJobRequestTasksExecutorPolicy(DaraModel):
    def __init__(
        self,
        array_spec: main_models.CreateJobRequestTasksExecutorPolicyArraySpec = None,
        max_count: int = None,
    ):
        # The array job details. Sub-job index values are passed to the runtime environment through environment variables, which can be referenced by user applications. The environment variables include:
        # - EHPC_JOB_NAME: the job name, corresponding to the JobName parameter.
        # - EHPC_JOB_ID: the job ID.
        # - EHPC_TASK_NAME: the task name, corresponding to the TaskName parameter.
        # - EHPC_EXECUTOR_ID: the executor ID.
        # - EHPC_ARRAY_TASK_ID: the sub-job index value.
        # - EHPC_ARRAY_TASK_COUNT: the total number of sub-jobs.
        # - EHPC_ARRAY_TASK_MAX: the maximum sub-job index value, corresponding to the IndexStart parameter.
        # - EHPC_ARRAY_TASK_MIN: the minimum sub-job index value, corresponding to the IndexEnd parameter.
        # - EHPC_ARRAY_TASK_STEP: the sub-job index step, corresponding to the IndexStep parameter.
        self.array_spec = array_spec
        # The maximum number of nodes for the job.
        # > The value must comply with the following formula: `MaxCount = (IndexEnd - IndexStart) / IndexStep + 1`
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
            temp_model = main_models.CreateJobRequestTasksExecutorPolicyArraySpec()
            self.array_spec = temp_model.from_map(m.get('ArraySpec'))

        if m.get('MaxCount') is not None:
            self.max_count = m.get('MaxCount')

        return self

class CreateJobRequestTasksExecutorPolicyArraySpec(DaraModel):
    def __init__(
        self,
        index_end: int = None,
        index_start: int = None,
        index_step: int = None,
    ):
        # The end value of the array job index. Valid values: 0 to 4999. The value must be greater than or equal to IndexStart.
        self.index_end = index_end
        # The start value of the array job index. Valid values: 0 to 4999.
        self.index_start = index_start
        # The interval between indexes in an array job.
        # > If the array job has the properties IndexStart=1, IndexEnd=5, and IndexStep=2, the array job contains three sub-jobs with indexes 1, 3, and 5. Your application can access these indexes through environment variables.
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

class CreateJobRequestSecurityPolicy(DaraModel):
    def __init__(
        self,
        security_group: main_models.CreateJobRequestSecurityPolicySecurityGroup = None,
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
            temp_model = main_models.CreateJobRequestSecurityPolicySecurityGroup()
            self.security_group = temp_model.from_map(m.get('SecurityGroup'))

        return self

class CreateJobRequestSecurityPolicySecurityGroup(DaraModel):
    def __init__(
        self,
        security_group_ids: List[str] = None,
    ):
        # The array of security group IDs.
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

class CreateJobRequestDeploymentPolicy(DaraModel):
    def __init__(
        self,
        allocation_spec: str = None,
        level: str = None,
        network: main_models.CreateJobRequestDeploymentPolicyNetwork = None,
        pool: str = None,
        priority: int = None,
        tag: List[main_models.CreateJobRequestDeploymentPolicyTag] = None,
    ):
        # The resource type.
        self.allocation_spec = allocation_spec
        # The computing power level. This parameter is valid only when the resource type is economy. Valid values:
        # - General: general-purpose.
        # - Performance: compute-optimized.
        # 
        # Default value: General
        self.level = level
        # The network configuration.
        self.network = network
        # The job resource pool.
        self.pool = pool
        # The job priority. A larger value indicates a higher scheduling priority. Valid values: 1 to 100.
        self.priority = priority
        # The job tag information. A maximum of 20 tags are supported.
        self.tag = tag

    def validate(self):
        if self.network:
            self.network.validate()
        if self.tag:
            for v1 in self.tag:
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

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllocationSpec') is not None:
            self.allocation_spec = m.get('AllocationSpec')

        if m.get('Level') is not None:
            self.level = m.get('Level')

        if m.get('Network') is not None:
            temp_model = main_models.CreateJobRequestDeploymentPolicyNetwork()
            self.network = temp_model.from_map(m.get('Network'))

        if m.get('Pool') is not None:
            self.pool = m.get('Pool')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateJobRequestDeploymentPolicyTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateJobRequestDeploymentPolicyTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key of the job. If you specify this parameter, the value cannot be an empty string. The tag key can be up to 128 characters in length and cannot start with aliyun or acs:. It cannot contain http:// or https://.
        # 
        # This parameter is required.
        self.key = key
        # The tag value of the job. If you specify this parameter, the value can be an empty string. The tag value can be up to 128 characters in length and cannot contain http:// or https://.
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

class CreateJobRequestDeploymentPolicyNetwork(DaraModel):
    def __init__(
        self,
        enable_external_ip_address: bool = None,
        vswitch: List[str] = None,
    ):
        # Specifies whether to create a public IP address for the job.
        self.enable_external_ip_address = enable_external_ip_address
        # The vSwitch array.
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

class CreateJobRequestDependencyPolicy(DaraModel):
    def __init__(
        self,
        job_dependency: List[main_models.CreateJobRequestDependencyPolicyJobDependency] = None,
    ):
        # The job dependencies. A maximum of 10 groups are supported.
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
                temp_model = main_models.CreateJobRequestDependencyPolicyJobDependency()
                self.job_dependency.append(temp_model.from_map(k1))

        return self

class CreateJobRequestDependencyPolicyJobDependency(DaraModel):
    def __init__(
        self,
        job_id: str = None,
        type: str = None,
    ):
        # The job ID.
        # 
        # This parameter is required.
        self.job_id = job_id
        # The dependency type. Valid values:
        # 
        # - AfterSucceeded: **All tasks** in the dependent job or array job run successfully (exit code 0).
        # - AfterFailed: **Any task** in the dependent job or array job fails (exit code is not 0).
        # - AfterAny: The dependent job finishes running (succeeded or failed).
        # - AfterCorresponding: The corresponding task in the dependent array job runs successfully (exit code 0).
        # 
        # Default value: AfterSucceeded.
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

