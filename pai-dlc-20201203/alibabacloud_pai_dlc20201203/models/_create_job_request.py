# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pai_dlc20201203 import models as main_models
from darabonba.model import DaraModel

class CreateJobRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        code_source: main_models.CreateJobRequestCodeSource = None,
        credential_config: main_models.CredentialConfig = None,
        data_sources: List[main_models.CreateJobRequestDataSources] = None,
        debugger_config_content: str = None,
        display_name: str = None,
        elastic_spec: main_models.JobElasticSpec = None,
        envs: Dict[str, str] = None,
        job_max_running_time_minutes: int = None,
        job_specs: List[main_models.JobSpec] = None,
        job_type: str = None,
        options: str = None,
        priority: int = None,
        resource_id: str = None,
        settings: main_models.JobSettings = None,
        success_policy: str = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        user_command: str = None,
        user_vpc: main_models.CreateJobRequestUserVpc = None,
        workspace_id: str = None,
    ):
        # The job visibility. Valid values:
        # 
        # *   PUBLIC: The job is visible to all members in the workspace.
        # *   PRIVATE: The job is visible only to you and the administrator of the workspace.
        self.accessibility = accessibility
        # The code source of the job. Before the node of the job runs, DLC automatically downloads the configured code from the code source and mounts the code to the local path of the container.
        self.code_source = code_source
        # The access credential configuration.
        self.credential_config = credential_config
        # The data sources for job running.
        self.data_sources = data_sources
        # This parameter is not supported.
        self.debugger_config_content = debugger_config_content
        # The job name. The name must be in the following format:
        # 
        # *   The name must be 1 to 256 characters in length.
        # *   The name can contain digits, letters, underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.display_name = display_name
        # This parameter is not supported.
        self.elastic_spec = elastic_spec
        # The environment variables.
        self.envs = envs
        # The maximum running duration of the job. Unit: minutes.
        self.job_max_running_time_minutes = job_max_running_time_minutes
        # **JobSpecs** describes the configurations for job running, such as the image address, startup command, node resource declaration, and number of replicas.
        # 
        # A DLC job consists of different types of nodes. If nodes of the same type have exactly the same configuration, the configuration is called JobSpec. **JobSpecs** specifies the configurations of all types of nodes. The value is of the array type.
        # 
        # This parameter is required.
        self.job_specs = job_specs
        # The job type. The value is case-sensitive. The following job types are supported:
        # 
        # *   TFJob
        # *   PyTorchJob
        # *   MPIJob
        # *   XGBoostJob
        # *   OneFlowJob
        # *   ElasticBatchJob
        # *   SlurmJob
        # *   RayJob
        # 
        # Valid values and corresponding frameworks:
        # 
        # *   OneFlowJob: OneFlow.
        # *   PyTorchJob: PyTorch.
        # *   SlurmJob: Slurm.
        # *   XGBoostJob: XGBoost.
        # *   ElasticBatchJob: ElasticBatch.
        # *   MPIJob: MPIJob.
        # *   TFJob: Tensorflow.
        # *   RayJob: Ray.
        # 
        # This parameter is required.
        self.job_type = job_type
        # The additional configuration of the job. You can use this parameter to adjust the behavior of the attached data source. For example, if the attached data source of the job is of the OSS type, you can use this parameter to add the following configurations to override the default parameters of JindoFS: `fs.oss.download.thread.concurrency=4,fs.oss.download.queue.size=16`.
        self.options = options
        # The priority of the job. Default value: 1. Valid values: 1 to 9.
        # 
        # *   1 is the lowest priority.
        # *   9: the highest priority.
        self.priority = priority
        # The ID of the resource group. This parameter is optional.
        # 
        # *   If you leave this parameter empty, the job is submitted to a public resource group.
        # *   If a resource quota is bound to the current workspace, you can specify the resource quota ID. For more information about how to query the resource quota ID, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        # The additional parameter configurations of the job.
        self.settings = settings
        # The policy that is used to check whether a distributed multi-node job is successful. Only TensorFlow distributed multi-node jobs are supported.
        # 
        # *   ChiefWorker: If you use this policy, the job is considered successful when the pod on the chief node completes operations.
        # *   AllWorkers (default): If you use this policy, the job is considered successful when all worker nodes complete operations.
        self.success_policy = success_policy
        # The folder in which the third-party Python library file requirements.txt is stored. Before the startup command specified by the UserCommand parameter is run on each node, DLC fetches the requirements.txt file from the folder and runs `pip install -r` to install the required package and library.
        self.thirdparty_lib_dir = thirdparty_lib_dir
        # The third-party Python libraries to be installed.
        self.thirdparty_libs = thirdparty_libs
        # The startup command for all nodes of the job.
        # 
        # This parameter is required.
        self.user_command = user_command
        # The VPC settings.
        self.user_vpc = user_vpc
        # The workspace ID.
        self.workspace_id = workspace_id

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.elastic_spec:
            self.elastic_spec.validate()
        if self.job_specs:
            for v1 in self.job_specs:
                 if v1:
                    v1.validate()
        if self.settings:
            self.settings.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.code_source is not None:
            result['CodeSource'] = self.code_source.to_map()

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.elastic_spec is not None:
            result['ElasticSpec'] = self.elastic_spec.to_map()

        if self.envs is not None:
            result['Envs'] = self.envs

        if self.job_max_running_time_minutes is not None:
            result['JobMaxRunningTimeMinutes'] = self.job_max_running_time_minutes

        result['JobSpecs'] = []
        if self.job_specs is not None:
            for k1 in self.job_specs:
                result['JobSpecs'].append(k1.to_map() if k1 else None)

        if self.job_type is not None:
            result['JobType'] = self.job_type

        if self.options is not None:
            result['Options'] = self.options

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.success_policy is not None:
            result['SuccessPolicy'] = self.success_policy

        if self.thirdparty_lib_dir is not None:
            result['ThirdpartyLibDir'] = self.thirdparty_lib_dir

        if self.thirdparty_libs is not None:
            result['ThirdpartyLibs'] = self.thirdparty_libs

        if self.user_command is not None:
            result['UserCommand'] = self.user_command

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('CodeSource') is not None:
            temp_model = main_models.CreateJobRequestCodeSource()
            self.code_source = temp_model.from_map(m.get('CodeSource'))

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.CreateJobRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('ElasticSpec') is not None:
            temp_model = main_models.JobElasticSpec()
            self.elastic_spec = temp_model.from_map(m.get('ElasticSpec'))

        if m.get('Envs') is not None:
            self.envs = m.get('Envs')

        if m.get('JobMaxRunningTimeMinutes') is not None:
            self.job_max_running_time_minutes = m.get('JobMaxRunningTimeMinutes')

        self.job_specs = []
        if m.get('JobSpecs') is not None:
            for k1 in m.get('JobSpecs'):
                temp_model = main_models.JobSpec()
                self.job_specs.append(temp_model.from_map(k1))

        if m.get('JobType') is not None:
            self.job_type = m.get('JobType')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Settings') is not None:
            temp_model = main_models.JobSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('SuccessPolicy') is not None:
            self.success_policy = m.get('SuccessPolicy')

        if m.get('ThirdpartyLibDir') is not None:
            self.thirdparty_lib_dir = m.get('ThirdpartyLibDir')

        if m.get('ThirdpartyLibs') is not None:
            self.thirdparty_libs = m.get('ThirdpartyLibs')

        if m.get('UserCommand') is not None:
            self.user_command = m.get('UserCommand')

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateJobRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateJobRequestUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default route. Default value: false. Valid values:
        # 
        # *   eth0: The default network interface is used to access the Internet through the public gateway.
        # *   eth1: The user\\"s elastic network interface (ENI) is used to access the Internet through the private gateway. For more information about the configuration method, see [Enable Internet access for a DSW instance by using a private Internet NAT gateway](https://help.aliyun.com/document_detail/2525343.html).
        self.default_route = default_route
        # The extended CIDR block.
        # 
        # *   If you leave the SwitchId and ExtendedCIDRs parameters empty, the system automatically obtains all CIDR blocks in a VPC.
        # *   If you configure the SwitchId and ExtendedCIDRs parameters, we recommend that you specify all CIDR blocks in a VPC.
        self.extended_cidrs = extended_cidrs
        # The ID of the security group.
        self.security_group_id = security_group_id
        # The vSwitch ID. This parameter is optional.
        # 
        # *   If you leave this parameter empty, the system automatically selects a vSwitch based on the inventory status.
        # *   You can also specify a vSwitch ID.
        self.switch_id = switch_id
        # The VPC ID.
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_route is not None:
            result['DefaultRoute'] = self.default_route

        if self.extended_cidrs is not None:
            result['ExtendedCIDRs'] = self.extended_cidrs

        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.switch_id is not None:
            result['SwitchId'] = self.switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRoute') is not None:
            self.default_route = m.get('DefaultRoute')

        if m.get('ExtendedCIDRs') is not None:
            self.extended_cidrs = m.get('ExtendedCIDRs')

        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('SwitchId') is not None:
            self.switch_id = m.get('SwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateJobRequestDataSources(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_version: str = None,
        enable_cache: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        options: str = None,
        uri: str = None,
    ):
        # The data source ID.
        self.data_source_id = data_source_id
        self.data_source_version = data_source_version
        self.enable_cache = enable_cache
        self.mount_access = mount_access
        # The path to which the job is mounted. By default, the mount path in the data source configuration is used. This parameter is optional.
        self.mount_path = mount_path
        # The mount attribute of the custom dataset. Set the value to OSS.
        self.options = options
        # The data source path.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_version is not None:
            result['DataSourceVersion'] = self.data_source_version

        if self.enable_cache is not None:
            result['EnableCache'] = self.enable_cache

        if self.mount_access is not None:
            result['MountAccess'] = self.mount_access

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.options is not None:
            result['Options'] = self.options

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceVersion') is not None:
            self.data_source_version = m.get('DataSourceVersion')

        if m.get('EnableCache') is not None:
            self.enable_cache = m.get('EnableCache')

        if m.get('MountAccess') is not None:
            self.mount_access = m.get('MountAccess')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class CreateJobRequestCodeSource(DaraModel):
    def __init__(
        self,
        branch: str = None,
        code_source_id: str = None,
        commit: str = None,
        mount_path: str = None,
    ):
        # The branch of the referenced code repository. By default, the branch configured in the code source is used. This parameter is optional.
        self.branch = branch
        # The ID of the code source.
        self.code_source_id = code_source_id
        # The commit ID of the code to be downloaded. By default, the commit ID configured in the code source is used. This parameter is optional.
        self.commit = commit
        # The path to which the job is mounted. By default, the mount path configured in the data source is used. This parameter is optional.
        self.mount_path = mount_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.branch is not None:
            result['Branch'] = self.branch

        if self.code_source_id is not None:
            result['CodeSourceId'] = self.code_source_id

        if self.commit is not None:
            result['Commit'] = self.commit

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Branch') is not None:
            self.branch = m.get('Branch')

        if m.get('CodeSourceId') is not None:
            self.code_source_id = m.get('CodeSourceId')

        if m.get('Commit') is not None:
            self.commit = m.get('Commit')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

