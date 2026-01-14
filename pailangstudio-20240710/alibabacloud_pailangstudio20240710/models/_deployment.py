# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class Deployment(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        auto_approval: bool = None,
        chat_history_config: main_models.DeploymentChatHistoryConfig = None,
        content_moderation_config: main_models.DeploymentContentModerationConfig = None,
        creator: str = None,
        credential_config: main_models.DeploymentCredentialConfig = None,
        data_sources: List[main_models.DeploymentDataSources] = None,
        deployment_config: str = None,
        deployment_id: str = None,
        deployment_stages: List[main_models.DeploymentDeploymentStages] = None,
        deployment_status: str = None,
        description: str = None,
        ecs_spec: main_models.DeploymentEcsSpec = None,
        enable_trace: bool = None,
        envs: List[main_models.DeploymentEnvs] = None,
        error_message: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        labels: List[main_models.DeploymentLabels] = None,
        operation_type: str = None,
        resource_id: str = None,
        resource_snapshot_id: str = None,
        resource_type: str = None,
        service_group: str = None,
        service_name: str = None,
        user_vpc: main_models.DeploymentUserVpc = None,
        work_dir: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.auto_approval = auto_approval
        self.chat_history_config = chat_history_config
        self.content_moderation_config = content_moderation_config
        self.creator = creator
        self.credential_config = credential_config
        self.data_sources = data_sources
        self.deployment_config = deployment_config
        self.deployment_id = deployment_id
        self.deployment_stages = deployment_stages
        self.deployment_status = deployment_status
        self.description = description
        self.ecs_spec = ecs_spec
        self.enable_trace = enable_trace
        self.envs = envs
        self.error_message = error_message
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.labels = labels
        self.operation_type = operation_type
        self.resource_id = resource_id
        self.resource_snapshot_id = resource_snapshot_id
        self.resource_type = resource_type
        self.service_group = service_group
        self.service_name = service_name
        self.user_vpc = user_vpc
        self.work_dir = work_dir
        self.workspace_id = workspace_id

    def validate(self):
        if self.chat_history_config:
            self.chat_history_config.validate()
        if self.content_moderation_config:
            self.content_moderation_config.validate()
        if self.credential_config:
            self.credential_config.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.deployment_stages:
            for v1 in self.deployment_stages:
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

        if self.auto_approval is not None:
            result['AutoApproval'] = self.auto_approval

        if self.chat_history_config is not None:
            result['ChatHistoryConfig'] = self.chat_history_config.to_map()

        if self.content_moderation_config is not None:
            result['ContentModerationConfig'] = self.content_moderation_config.to_map()

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.deployment_config is not None:
            result['DeploymentConfig'] = self.deployment_config

        if self.deployment_id is not None:
            result['DeploymentId'] = self.deployment_id

        result['DeploymentStages'] = []
        if self.deployment_stages is not None:
            for k1 in self.deployment_stages:
                result['DeploymentStages'].append(k1.to_map() if k1 else None)

        if self.deployment_status is not None:
            result['DeploymentStatus'] = self.deployment_status

        if self.description is not None:
            result['Description'] = self.description

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec.to_map()

        if self.enable_trace is not None:
            result['EnableTrace'] = self.enable_trace

        result['Envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['Envs'].append(k1.to_map() if k1 else None)

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_snapshot_id is not None:
            result['ResourceSnapshotId'] = self.resource_snapshot_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.service_group is not None:
            result['ServiceGroup'] = self.service_group

        if self.service_name is not None:
            result['ServiceName'] = self.service_name

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

        if m.get('AutoApproval') is not None:
            self.auto_approval = m.get('AutoApproval')

        if m.get('ChatHistoryConfig') is not None:
            temp_model = main_models.DeploymentChatHistoryConfig()
            self.chat_history_config = temp_model.from_map(m.get('ChatHistoryConfig'))

        if m.get('ContentModerationConfig') is not None:
            temp_model = main_models.DeploymentContentModerationConfig()
            self.content_moderation_config = temp_model.from_map(m.get('ContentModerationConfig'))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.DeploymentCredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.DeploymentDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('DeploymentConfig') is not None:
            self.deployment_config = m.get('DeploymentConfig')

        if m.get('DeploymentId') is not None:
            self.deployment_id = m.get('DeploymentId')

        self.deployment_stages = []
        if m.get('DeploymentStages') is not None:
            for k1 in m.get('DeploymentStages'):
                temp_model = main_models.DeploymentDeploymentStages()
                self.deployment_stages.append(temp_model.from_map(k1))

        if m.get('DeploymentStatus') is not None:
            self.deployment_status = m.get('DeploymentStatus')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EcsSpec') is not None:
            temp_model = main_models.DeploymentEcsSpec()
            self.ecs_spec = temp_model.from_map(m.get('EcsSpec'))

        if m.get('EnableTrace') is not None:
            self.enable_trace = m.get('EnableTrace')

        self.envs = []
        if m.get('Envs') is not None:
            for k1 in m.get('Envs'):
                temp_model = main_models.DeploymentEnvs()
                self.envs.append(temp_model.from_map(k1))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.DeploymentLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceSnapshotId') is not None:
            self.resource_snapshot_id = m.get('ResourceSnapshotId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('ServiceGroup') is not None:
            self.service_group = m.get('ServiceGroup')

        if m.get('ServiceName') is not None:
            self.service_name = m.get('ServiceName')

        if m.get('UserVpc') is not None:
            temp_model = main_models.DeploymentUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('WorkDir') is not None:
            self.work_dir = m.get('WorkDir')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class DeploymentUserVpc(DaraModel):
    def __init__(
        self,
        security_group_id: str = None,
        v_switch_id: str = None,
        vpc_id: str = None,
    ):
        # 安全组ID
        self.security_group_id = security_group_id
        # 交换机ID
        self.v_switch_id = v_switch_id
        # VPC ID
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.security_group_id is not None:
            result['SecurityGroupId'] = self.security_group_id

        if self.v_switch_id is not None:
            result['VSwitchId'] = self.v_switch_id

        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SecurityGroupId') is not None:
            self.security_group_id = m.get('SecurityGroupId')

        if m.get('VSwitchId') is not None:
            self.v_switch_id = m.get('VSwitchId')

        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')

        return self

class DeploymentLabels(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 标签键
        self.key = key
        # 标签值
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

class DeploymentEnvs(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 环境键
        self.key = key
        # 环境值
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

class DeploymentEcsSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        computing_instance_config: main_models.DeploymentEcsSpecComputingInstanceConfig = None,
        extra_ephemeral_storage: int = None,
        gpu: int = None,
        gpucore_percentage: int = None,
        gpumemory: int = None,
        gputype: str = None,
        instance_type: str = None,
        memory: int = None,
        pod_count: int = None,
        quota_id: str = None,
        quota_type: str = None,
        resource_burstable: bool = None,
        resource_id: str = None,
        shared_memory: int = None,
    ):
        # CPU信息
        self.cpu = cpu
        # 竞价资源配置
        self.computing_instance_config = computing_instance_config
        # 额外系统盘
        self.extra_ephemeral_storage = extra_ephemeral_storage
        # GPU信息
        self.gpu = gpu
        # GPU算力占比
        self.gpucore_percentage = gpucore_percentage
        # GPU显存
        self.gpumemory = gpumemory
        # GPU类型
        self.gputype = gputype
        # 实例类型
        self.instance_type = instance_type
        # 内存信息
        self.memory = memory
        # Pod数量
        self.pod_count = pod_count
        # 资源配额ID
        self.quota_id = quota_id
        # 资源配额类型
        self.quota_type = quota_type
        # 是否启用弹性资源池
        self.resource_burstable = resource_burstable
        # 资源组ID
        self.resource_id = resource_id
        # 共享内存
        self.shared_memory = shared_memory

    def validate(self):
        if self.computing_instance_config:
            self.computing_instance_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu is not None:
            result['CPU'] = self.cpu

        if self.computing_instance_config is not None:
            result['ComputingInstanceConfig'] = self.computing_instance_config.to_map()

        if self.extra_ephemeral_storage is not None:
            result['ExtraEphemeralStorage'] = self.extra_ephemeral_storage

        if self.gpu is not None:
            result['GPU'] = self.gpu

        if self.gpucore_percentage is not None:
            result['GPUCorePercentage'] = self.gpucore_percentage

        if self.gpumemory is not None:
            result['GPUMemory'] = self.gpumemory

        if self.gputype is not None:
            result['GPUType'] = self.gputype

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.memory is not None:
            result['Memory'] = self.memory

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.quota_id is not None:
            result['QuotaId'] = self.quota_id

        if self.quota_type is not None:
            result['QuotaType'] = self.quota_type

        if self.resource_burstable is not None:
            result['ResourceBurstable'] = self.resource_burstable

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

        if m.get('ComputingInstanceConfig') is not None:
            temp_model = main_models.DeploymentEcsSpecComputingInstanceConfig()
            self.computing_instance_config = temp_model.from_map(m.get('ComputingInstanceConfig'))

        if m.get('ExtraEphemeralStorage') is not None:
            self.extra_ephemeral_storage = m.get('ExtraEphemeralStorage')

        if m.get('GPU') is not None:
            self.gpu = m.get('GPU')

        if m.get('GPUCorePercentage') is not None:
            self.gpucore_percentage = m.get('GPUCorePercentage')

        if m.get('GPUMemory') is not None:
            self.gpumemory = m.get('GPUMemory')

        if m.get('GPUType') is not None:
            self.gputype = m.get('GPUType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('Memory') is not None:
            self.memory = m.get('Memory')

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('QuotaId') is not None:
            self.quota_id = m.get('QuotaId')

        if m.get('QuotaType') is not None:
            self.quota_type = m.get('QuotaType')

        if m.get('ResourceBurstable') is not None:
            self.resource_burstable = m.get('ResourceBurstable')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

class DeploymentEcsSpecComputingInstanceConfig(DaraModel):
    def __init__(
        self,
        computing_instances: List[main_models.DeploymentEcsSpecComputingInstanceConfigComputingInstances] = None,
        disable_spot_protection_period: bool = None,
    ):
        # 机器资源配置
        self.computing_instances = computing_instances
        # 是否启用竞价保留时长
        self.disable_spot_protection_period = disable_spot_protection_period

    def validate(self):
        if self.computing_instances:
            for v1 in self.computing_instances:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ComputingInstances'] = []
        if self.computing_instances is not None:
            for k1 in self.computing_instances:
                result['ComputingInstances'].append(k1.to_map() if k1 else None)

        if self.disable_spot_protection_period is not None:
            result['DisableSpotProtectionPeriod'] = self.disable_spot_protection_period

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.computing_instances = []
        if m.get('ComputingInstances') is not None:
            for k1 in m.get('ComputingInstances'):
                temp_model = main_models.DeploymentEcsSpecComputingInstanceConfigComputingInstances()
                self.computing_instances.append(temp_model.from_map(k1))

        if m.get('DisableSpotProtectionPeriod') is not None:
            self.disable_spot_protection_period = m.get('DisableSpotProtectionPeriod')

        return self

class DeploymentEcsSpecComputingInstanceConfigComputingInstances(DaraModel):
    def __init__(
        self,
        spot_price_limit: float = None,
        type: str = None,
    ):
        # 竞价出价
        self.spot_price_limit = spot_price_limit
        # 机型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.spot_price_limit is not None:
            result['SpotPriceLimit'] = self.spot_price_limit

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpotPriceLimit') is not None:
            self.spot_price_limit = m.get('SpotPriceLimit')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DeploymentDeploymentStages(DaraModel):
    def __init__(
        self,
        description: str = None,
        error_message: str = None,
        gmt_end_time: str = None,
        gmt_start_time: str = None,
        stage: int = None,
        stage_info: str = None,
        stage_name: str = None,
        stage_status: str = None,
    ):
        # 描述
        self.description = description
        # 错误信息
        self.error_message = error_message
        # 结束时间
        self.gmt_end_time = gmt_end_time
        # 开始时间
        self.gmt_start_time = gmt_start_time
        # 阶段
        self.stage = stage
        # 阶段信息
        self.stage_info = stage_info
        # 阶段名称
        self.stage_name = stage_name
        # 阶段状态
        self.stage_status = stage_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.gmt_end_time is not None:
            result['GmtEndTime'] = self.gmt_end_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.stage is not None:
            result['Stage'] = self.stage

        if self.stage_info is not None:
            result['StageInfo'] = self.stage_info

        if self.stage_name is not None:
            result['StageName'] = self.stage_name

        if self.stage_status is not None:
            result['StageStatus'] = self.stage_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('GmtEndTime') is not None:
            self.gmt_end_time = m.get('GmtEndTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('Stage') is not None:
            self.stage = m.get('Stage')

        if m.get('StageInfo') is not None:
            self.stage_info = m.get('StageInfo')

        if m.get('StageName') is not None:
            self.stage_name = m.get('StageName')

        if m.get('StageStatus') is not None:
            self.stage_status = m.get('StageStatus')

        return self

class DeploymentDataSources(DaraModel):
    def __init__(
        self,
        dataset_id: str = None,
        mount_path: str = None,
        uri: str = None,
    ):
        # 数据集ID
        self.dataset_id = dataset_id
        # 挂载路径
        self.mount_path = mount_path
        # 统一资源识别码
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

class DeploymentCredentialConfig(DaraModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        credential_config_items: List[main_models.DeploymentCredentialConfigCredentialConfigItems] = None,
        enable_credential_inject: bool = None,
    ):
        # AliyunEnvRoleKey
        self.aliyun_env_role_key = aliyun_env_role_key
        # Credential配置项列表
        self.credential_config_items = credential_config_items
        # 是否启用Credential注入
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
                temp_model = main_models.DeploymentCredentialConfigCredentialConfigItems()
                self.credential_config_items.append(temp_model.from_map(k1))

        if m.get('EnableCredentialInject') is not None:
            self.enable_credential_inject = m.get('EnableCredentialInject')

        return self

class DeploymentCredentialConfigCredentialConfigItems(DaraModel):
    def __init__(
        self,
        key: str = None,
        roles: List[main_models.DeploymentCredentialConfigCredentialConfigItemsRoles] = None,
        type: str = None,
    ):
        # Key
        self.key = key
        # 角色列表
        self.roles = roles
        # Type
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
                temp_model = main_models.DeploymentCredentialConfigCredentialConfigItemsRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class DeploymentCredentialConfigCredentialConfigItemsRoles(DaraModel):
    def __init__(
        self,
        assume_role_for: str = None,
        role_arn: str = None,
        role_type: str = None,
    ):
        # AssumeRoleFor
        self.assume_role_for = assume_role_for
        # 角色名称
        self.role_arn = role_arn
        # 角色类型
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

class DeploymentContentModerationConfig(DaraModel):
    def __init__(
        self,
        enable_input_moderation: bool = None,
        enable_output_moderation: bool = None,
        streaming_moderation_threshold: int = None,
    ):
        # 启用输入内容审查
        self.enable_input_moderation = enable_input_moderation
        # 启用输出内容审查
        self.enable_output_moderation = enable_output_moderation
        # 流式输出内容送审缓存大小
        self.streaming_moderation_threshold = streaming_moderation_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_input_moderation is not None:
            result['EnableInputModeration'] = self.enable_input_moderation

        if self.enable_output_moderation is not None:
            result['EnableOutputModeration'] = self.enable_output_moderation

        if self.streaming_moderation_threshold is not None:
            result['StreamingModerationThreshold'] = self.streaming_moderation_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableInputModeration') is not None:
            self.enable_input_moderation = m.get('EnableInputModeration')

        if m.get('EnableOutputModeration') is not None:
            self.enable_output_moderation = m.get('EnableOutputModeration')

        if m.get('StreamingModerationThreshold') is not None:
            self.streaming_moderation_threshold = m.get('StreamingModerationThreshold')

        return self

class DeploymentChatHistoryConfig(DaraModel):
    def __init__(
        self,
        connection_name: str = None,
        storage_type: str = None,
    ):
        # 连接名称
        self.connection_name = connection_name
        # 存储类型
        self.storage_type = storage_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        return self

