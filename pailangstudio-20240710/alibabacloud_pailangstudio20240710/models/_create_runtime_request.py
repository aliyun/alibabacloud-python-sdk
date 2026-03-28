# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class CreateRuntimeRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        auto_update_image: bool = None,
        credential_config: main_models.CreateRuntimeRequestCredentialConfig = None,
        data_sources: List[main_models.CreateRuntimeRequestDataSources] = None,
        ecs_spec: main_models.CreateRuntimeRequestEcsSpec = None,
        envs: List[main_models.CreateRuntimeRequestEnvs] = None,
        labels: List[main_models.CreateRuntimeRequestLabels] = None,
        resource_id: str = None,
        run_timeout: int = None,
        runtime_name: str = None,
        runtime_type: str = None,
        user_vpc: main_models.CreateRuntimeRequestUserVpc = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        # Workspace visibility. Possible values are:
        # 
        # *   PRIVATE: In this workspace, visible only to you and administrators.
        # *   PUBLIC: In this workspace, visible to everyone.
        self.accessibility = accessibility
        self.auto_update_image = auto_update_image
        # The credential configuration.
        self.credential_config = credential_config
        # Mount data source.
        self.data_sources = data_sources
        # The configurations of ECS resources.
        self.ecs_spec = ecs_spec
        # The environment variables. Separate the environment variables with commas (,).
        self.envs = envs
        # The list of tags.
        self.labels = labels
        # The resource quota ID.
        self.resource_id = resource_id
        # Timeout in seconds for a single test executed on the runtime.
        self.run_timeout = run_timeout
        # The name of the container runtime. Format requirements:
        # 
        # *   Can only contain English letters, digits, and underscores (_).
        # *   Starts with a letter.
        # *   The length must be 1 to 256 characters.
        self.runtime_name = runtime_name
        # The runtime type used by the nodes. Valid values:
        # 
        # *   DSW: PAI-DSW instance
        self.runtime_type = runtime_type
        # User VPC Configuration.
        self.user_vpc = user_vpc
        # The OSS path of the working directory.
        self.work_dir = work_dir
        # The ID of the workspace. To obtain the workspace ID, see [ListWorkspaces](https://help.aliyun.com/document_detail/449124.html).
        self.workspace_id = workspace_id

    def validate(self):
        if self.credential_config:
            self.credential_config.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.ecs_spec:
            self.ecs_spec.validate()
        if self.envs:
            for v1 in self.envs:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.auto_update_image is not None:
            result['AutoUpdateImage'] = self.auto_update_image

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec.to_map()

        result['Envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['Envs'].append(k1.to_map() if k1 else None)

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.run_timeout is not None:
            result['RunTimeout'] = self.run_timeout

        if self.runtime_name is not None:
            result['RuntimeName'] = self.runtime_name

        if self.runtime_type is not None:
            result['RuntimeType'] = self.runtime_type

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.work_dir is not None:
            result['WorkDir'] = self.work_dir

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AutoUpdateImage') is not None:
            self.auto_update_image = m.get('AutoUpdateImage')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.CreateRuntimeRequestCredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.CreateRuntimeRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('EcsSpec') is not None:
            temp_model = main_models.CreateRuntimeRequestEcsSpec()
            self.ecs_spec = temp_model.from_map(m.get('EcsSpec'))

        self.envs = []
        if m.get('Envs') is not None:
            for k1 in m.get('Envs'):
                temp_model = main_models.CreateRuntimeRequestEnvs()
                self.envs.append(temp_model.from_map(k1))

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.CreateRuntimeRequestLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RunTimeout') is not None:
            self.run_timeout = m.get('RunTimeout')

        if m.get('RuntimeName') is not None:
            self.runtime_name = m.get('RuntimeName')

        if m.get('RuntimeType') is not None:
            self.runtime_type = m.get('RuntimeType')

        if m.get('UserVpc') is not None:
            temp_model = main_models.CreateRuntimeRequestUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateRuntimeRequestUserVpc(DaraModel):
    def __init__(
        self,
        default_route: str = None,
        extended_cidrs: List[str] = None,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # The default Ingress.
        self.default_route = default_route
        # The extended CIDR blocks.
        self.extended_cidrs = extended_cidrs
        # The ID of a security group.
        self.security_group_id = security_group_id
        # The vSwitch IDs.
        self.v_switch_id = v_switch_id
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

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

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

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class CreateRuntimeRequestLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
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

class CreateRuntimeRequestEnvs(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The environment key.
        self.key = key
        # The value of the environment.
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

class CreateRuntimeRequestEcsSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        driver: str = None,
        gpu: int = None,
        gputype: str = None,
        instance_type: str = None,
        memory: int = None,
        shared_memory: int = None,
    ):
        # The number of CPU cores.
        self.cpu = cpu
        # The version of the GPU driver.
        self.driver = driver
        # The number of the GPUs.
        self.gpu = gpu
        # The GPU Class. Valid values are as follows:
        # 
        # *   V100
        # *   A100
        # *   T4
        # *   A10
        # *   P100
        self.gputype = gputype
        # Instance Type
        self.instance_type = instance_type
        # The memory size, in GB.
        self.memory = memory
        # The shared memory size. Unit: GB.
        self.shared_memory = shared_memory

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.driver is not None:
            result['Driver'] = self.driver

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('Driver') is not None:
            self.driver = m.get('Driver')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

class CreateRuntimeRequestDataSources(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
        uri: str = None,
    ):
        # The ID of the dataset. Choose either Uri or another option.
        self.dataset_id = dataset_id
        # The path to which the data disk is mounted.
        self.mount_path = mount_path
        # The OSS path of the data source. You must choose either DatasetId or another option.
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class CreateRuntimeRequestCredentialConfig(DaraModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        credential_config_items: List[main_models.CreateRuntimeRequestCredentialConfigCredentialConfigItems] = None,
        enable_credential_inject: bool = None,
    ):
        # The key of the environment variable role.
        self.aliyun_env_role_key = aliyun_env_role_key
        # The list of credential configurations.
        self.credential_config_items = credential_config_items
        # Whether to enable credential injection.
        self.enable_credential_inject = enable_credential_inject

    def validate(self):
        if self.credential_config_items:
            for v1 in self.credential_config_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_env_role_key is not None:
            result['AliyunEnvRoleKey'] = self.aliyun_env_role_key

        result['CredentialConfigItems'] = []
        if self.credential_config_items is not None:
            for k1 in self.credential_config_items:
                result['CredentialConfigItems'].append(k1.to_map() if k1 else None)

        if self.enable_credential_inject is not None:
            result['EnableCredentialInject'] = self.enable_credential_inject

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunEnvRoleKey') is not None:
            self.aliyun_env_role_key = m.get('AliyunEnvRoleKey')

        self.credential_config_items = []
        if m.get('CredentialConfigItems') is not None:
            for k1 in m.get('CredentialConfigItems'):
                temp_model = main_models.CreateRuntimeRequestCredentialConfigCredentialConfigItems()
                self.credential_config_items.append(temp_model.from_map(k1))

        if m.get('EnableCredentialInject') is not None:
            self.enable_credential_inject = m.get('EnableCredentialInject')

        return self

class CreateRuntimeRequestCredentialConfigCredentialConfigItems(DaraModel):
    def __init__(
        self,
        key: str = None,
        roles: List[main_models.CreateRuntimeRequestCredentialConfigCredentialConfigItemsRoles] = None,
        type: str = None,
    ):
        # The key that identifies the configuration.
        self.key = key
        # The list of configured roles.
        self.roles = roles
        # The configuration type. Valid values:
        # 
        # *   Role: role assumption
        # *   RoleChain: role chain assumption
        self.type = type

    def validate(self):
        if self.roles:
            for v1 in self.roles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        result['Roles'] = []
        if self.roles is not None:
            for k1 in self.roles:
                result['Roles'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        self.roles = []
        if m.get('Roles') is not None:
            for k1 in m.get('Roles'):
                temp_model = main_models.CreateRuntimeRequestCredentialConfigCredentialConfigItemsRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CreateRuntimeRequestCredentialConfigCredentialConfigItemsRoles(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        # The entity to which the role is assigned.
        self.assume_role_for = assume_role_for
        # The Alibaba Cloud Resource Name (ARN) of the RAM role.
        self.role_arn = role_arn
        # The class of the role. Valid values:
        # 
        # *   service: assumed by the service;
        # *   user: assumed by the regular user account
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assume_role_for is not None:
            result['AssumeRoleFor'] = self.assume_role_for

        if self.role_arn is not None:
            result['RoleArn'] = self.role_arn

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssumeRoleFor') is not None:
            self.assume_role_for = m.get('AssumeRoleFor')

        if m.get('RoleArn') is not None:
            self.role_arn = m.get('RoleArn')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

