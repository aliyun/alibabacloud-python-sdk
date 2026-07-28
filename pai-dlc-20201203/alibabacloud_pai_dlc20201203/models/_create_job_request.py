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
        custom_envs: List[main_models.CreateJobRequestCustomEnvs] = None,
        data_sources: List[main_models.CreateJobRequestDataSources] = None,
        debugger_config_content: str = None,
        description: str = None,
        display_name: str = None,
        elastic_spec: main_models.JobElasticSpec = None,
        envs: Dict[str, str] = None,
        job_max_running_time_minutes: int = None,
        job_specs: List[main_models.JobSpec] = None,
        job_type: str = None,
        options: str = None,
        priority: int = None,
        resource_id: str = None,
        scheduling_strategy: str = None,
        settings: main_models.JobSettings = None,
        success_policy: str = None,
        template_id: str = None,
        template_version: int = None,
        thirdparty_lib_dir: str = None,
        thirdparty_libs: List[str] = None,
        user_command: str = None,
        user_vpc: main_models.CreateJobRequestUserVpc = None,
        workspace_id: str = None,
    ):
        # The visibility of the job. Valid values:
        # - PUBLIC: visible to all members in this workspace.
        # - PRIVATE: visible only to you and administrators in this workspace.
        self.accessibility = accessibility
        # The code source used by this job. Before the job nodes start, DLC automatically downloads the code configured in the code source and mounts it to a local directory in the container.
        self.code_source = code_source
        # The access credential configuration.
        self.credential_config = credential_config
        self.custom_envs = custom_envs
        # The list of data sources used by the job.
        self.data_sources = data_sources
        # This parameter is not supported. Ignore this parameter.
        self.debugger_config_content = debugger_config_content
        self.description = description
        # The name of the job. The naming conventions are as follows:
        # - The name cannot exceed 256 characters in length.
        # - The name can contain digits, letters, underscores (_), periods (.), and hyphens (-).
        # 
        # This parameter is required.
        self.display_name = display_name
        # This parameter is not supported. Ignore this parameter.
        self.elastic_spec = elastic_spec
        # The environment variable configuration.
        self.envs = envs
        # The maximum running time of the job. Unit: minutes.
        self.job_max_running_time_minutes = job_max_running_time_minutes
        # **JobSpecs** describes various configurations for job runtime, such as image address, startup command, node resource declarations, and replica count.
        # 
        # A DLC job consists of different types of nodes. Nodes of the same type share identical configurations, which is called a JobSpec. **JobSpecs** describes the configurations of all node types and is an array of JobSpec objects.
        # 
        # This parameter is required.
        self.job_specs = job_specs
        # The job type. This parameter is case-sensitive. Valid values:
        # - TFJob
        # - PyTorchJob
        # - MPIJob
        # - XGBoostJob
        # - OneFlowJob
        # - ElasticBatchJob
        # - SlurmJob
        # - RayJob
        # - DataJuicerJob
        # 
        # This parameter is required.
        self.job_type = job_type
        # The additional configuration for this node. You can use this parameter to adjust the behavior of mounted data sources. For example, if the node has an OSS-type data source mounted, you can set this parameter to `fs.oss.download.thread.concurrency=4,fs.oss.download.queue.size=16` to overwrite the default JindoFS parameter settings.
        self.options = options
        # The priority of the job. This is an optional parameter. Default value: 1. Valid values: 1 to 9.
        # 
        # - 1: the lowest priority.
        # - 9: the highest priority.
        self.priority = priority
        # The resource group ID. This is an optional parameter.
        # - If the value is empty, the job is submitted to the public resource group.
        # - If the current workspace has a resource quota attached, you can specify the corresponding resource quota ID. For details about how to query the resource quota ID, see [Manage resource quotas](https://help.aliyun.com/document_detail/2651299.html).
        self.resource_id = resource_id
        self.scheduling_strategy = scheduling_strategy
        # The additional parameter settings for the job.
        self.settings = settings
        # The success policy for distributed multi-node jobs. Currently, only TensorFlow multi-node jobs support this parameter.
        # - ChiefWorker: the entire job is considered successful as long as the Chief pod finishes successfully.
        # - AllWorkers (default): the entire job is considered successful only when all Workers finish successfully.
        self.success_policy = success_policy
        # The job template ID.
        self.template_id = template_id
        # The job template version.
        self.template_version = template_version
        # The folder name where the third-party Python library (requirements.txt) file is located. Before running the specified UserCommand on each node, PAI-DLC retrieves the requirements.txt file from the specified folder and runs `pip install -r` to install the libraries.
        self.thirdparty_lib_dir = thirdparty_lib_dir
        # The list of third-party Python libraries to install.
        self.thirdparty_libs = thirdparty_libs
        # The startup command for all nodes of the job.
        # 
        # This parameter is required.
        self.user_command = user_command
        # The user VPC configuration.
        self.user_vpc = user_vpc
        # The workspace ID. <props="china">For information about how to obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        if self.code_source:
            self.code_source.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.custom_envs:
            for v1 in self.custom_envs:
                 if v1:
                    v1.validate()
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

        result['CustomEnvs'] = []
        if self.custom_envs is not None:
            for k1 in self.custom_envs:
                result['CustomEnvs'].append(k1.to_map() if k1 else None)

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.debugger_config_content is not None:
            result['DebuggerConfigContent'] = self.debugger_config_content

        if self.description is not None:
            result['Description'] = self.description

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

        if self.scheduling_strategy is not None:
            result['SchedulingStrategy'] = self.scheduling_strategy

        if self.settings is not None:
            result['Settings'] = self.settings.to_map()

        if self.success_policy is not None:
            result['SuccessPolicy'] = self.success_policy

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_version is not None:
            result['TemplateVersion'] = self.template_version

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

        self.custom_envs = []
        if m.get('CustomEnvs') is not None:
            for k1 in m.get('CustomEnvs'):
                temp_model = main_models.CreateJobRequestCustomEnvs()
                self.custom_envs.append(temp_model.from_map(k1))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.CreateJobRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('DebuggerConfigContent') is not None:
            self.debugger_config_content = m.get('DebuggerConfigContent')

        if m.get('Description') is not None:
            self.description = m.get('Description')

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

        if m.get('SchedulingStrategy') is not None:
            self.scheduling_strategy = m.get('SchedulingStrategy')

        if m.get('Settings') is not None:
            temp_model = main_models.JobSettings()
            self.settings = temp_model.from_map(m.get('Settings'))

        if m.get('SuccessPolicy') is not None:
            self.success_policy = m.get('SuccessPolicy')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateVersion') is not None:
            self.template_version = m.get('TemplateVersion')

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
        # The default routing. Valid values:
        # - eth0: uses the default network interface controller (NIC) to access external networks through the public gateway.
        # - eth1: uses the user elastic network interfaces (ENIs) to access external networks through the private gateway. For the configuration method, see [Configure a DSW instance to access the Internet through a dedicated public gateway](https://help.aliyun.com/document_detail/2525343.html).
        self.default_route = default_route
        # The extended CIDR blocks.
        # - If the vSwitch ID is empty, this parameter is optional. The system automatically retrieves all CIDR blocks under the VPC.
        # - If the vSwitch ID is specified, this parameter is required. Specify all CIDR blocks under the VPC.
        self.extended_cidrs = extended_cidrs
        # The ID of the user security group.
        self.security_group_id = security_group_id
        # The ID of the user vSwitch. This is an optional parameter.
        # - If the value is empty, the system automatically selects an appropriate vSwitch based on inventory availability.
        # - You can also specify a vSwitch ID.
        self.switch_id = switch_id
        # The ID of the user VPC.
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
        access_point_id: str = None,
        data_source_id: str = None,
        data_source_version: str = None,
        enable_cache: bool = None,
        mount_access: str = None,
        mount_path: str = None,
        options: str = None,
        role_chain: str = None,
        uri: str = None,
    ):
        self.access_point_id = access_point_id
        # The ID of the data source. <props="china">For information about how to obtain the data source ID, see [ListDatasets](https://help.aliyun.com/document_detail/457222.html).
        self.data_source_id = data_source_id
        self.data_source_version = data_source_version
        self.enable_cache = enable_cache
        self.mount_access = mount_access
        # The mount path for this job. This is an optional parameter. By default, the mount path configured in the data source is used.
        self.mount_path = mount_path
        # Custom dataset mount properties. Currently, only OSS is supported.
        self.options = options
        self.role_chain = role_chain
        # The data source path.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

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

        if self.role_chain is not None:
            result['RoleChain'] = self.role_chain

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

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

        if m.get('RoleChain') is not None:
            self.role_chain = m.get('RoleChain')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class CreateJobRequestCustomEnvs(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        visible: str = None,
    ):
        self.key = key
        self.value = value
        self.visible = visible

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

        if self.visible is not None:
            result['Visible'] = self.visible

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        if m.get('Visible') is not None:
            self.visible = m.get('Visible')

        return self

class CreateJobRequestCodeSource(DaraModel):
    def __init__(
        self,
        branch: str = None,
        code_source_id: str = None,
        commit: str = None,
        is_shared_mount_path: bool = None,
        mount_path: str = None,
    ):
        # The branch of the code repository referenced when this job runs. This is an optional parameter. By default, the branch configured in the code source is used.
        self.branch = branch
        # The code source ID. <props="china">For information about how to obtain the code source ID, see [ListCodeSources](https://help.aliyun.com/document_detail/459922.html).
        self.code_source_id = code_source_id
        # The commit ID of the code to download for this job. This is an optional parameter. By default, the CommitID configured in the code source is used.
        self.commit = commit
        self.is_shared_mount_path = is_shared_mount_path
        # The mount path for this job. This is an optional parameter. By default, the mount path configured in the code source is used.
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

        if self.is_shared_mount_path is not None:
            result['IsSharedMountPath'] = self.is_shared_mount_path

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

        if m.get('IsSharedMountPath') is not None:
            self.is_shared_mount_path = m.get('IsSharedMountPath')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        return self

