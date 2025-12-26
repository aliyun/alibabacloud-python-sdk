# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class FlowRun(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        child_runs: List[main_models.FlowRunChildRuns] = None,
        creator: str = None,
        credential_config: main_models.FlowRunCredentialConfig = None,
        data_column_mapping: Dict[str, str] = None,
        data_sources: List[main_models.FlowRunDataSources] = None,
        duration: int = None,
        ecs_spec: main_models.FlowRunEcsSpec = None,
        envs: List[main_models.FlowRunEnvs] = None,
        evaluation_configs: List[main_models.FlowRunEvaluationConfigs] = None,
        evaluation_worker_count: int = None,
        exception: str = None,
        flow_id: str = None,
        flow_name: str = None,
        flow_run_id: str = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modified_time: str = None,
        gmt_start_time: str = None,
        labels: List[main_models.FlowRunLabels] = None,
        node_name: str = None,
        node_run_infos: List[main_models.FlowRunNodeRunInfos] = None,
        resource_id: str = None,
        run_mode: str = None,
        run_name: str = None,
        run_result: str = None,
        run_status: str = None,
        run_timeout: int = None,
        user_vpc: main_models.FlowRunUserVpc = None,
        variant: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.child_runs = child_runs
        self.creator = creator
        self.credential_config = credential_config
        self.data_column_mapping = data_column_mapping
        self.data_sources = data_sources
        self.duration = duration
        self.ecs_spec = ecs_spec
        self.envs = envs
        self.evaluation_configs = evaluation_configs
        self.evaluation_worker_count = evaluation_worker_count
        self.exception = exception
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.flow_run_id = flow_run_id
        self.gmt_create_time = gmt_create_time
        self.gmt_finish_time = gmt_finish_time
        self.gmt_modified_time = gmt_modified_time
        self.gmt_start_time = gmt_start_time
        self.labels = labels
        self.node_name = node_name
        self.node_run_infos = node_run_infos
        self.resource_id = resource_id
        self.run_mode = run_mode
        self.run_name = run_name
        self.run_result = run_result
        self.run_status = run_status
        self.run_timeout = run_timeout
        self.user_vpc = user_vpc
        self.variant = variant
        self.workspace_id = workspace_id

    def validate(self):
        if self.child_runs:
            for v1 in self.child_runs:
                 if v1:
                    v1.validate()
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
        if self.evaluation_configs:
            for v1 in self.evaluation_configs:
                 if v1:
                    v1.validate()
        if self.labels:
            for v1 in self.labels:
                 if v1:
                    v1.validate()
        if self.node_run_infos:
            for v1 in self.node_run_infos:
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

        result['ChildRuns'] = []
        if self.child_runs is not None:
            for k1 in self.child_runs:
                result['ChildRuns'].append(k1.to_map() if k1 else None)

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.credential_config is not None:
            result['CredentialConfig'] = self.credential_config.to_map()

        if self.data_column_mapping is not None:
            result['DataColumnMapping'] = self.data_column_mapping

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.ecs_spec is not None:
            result['EcsSpec'] = self.ecs_spec.to_map()

        result['Envs'] = []
        if self.envs is not None:
            for k1 in self.envs:
                result['Envs'].append(k1.to_map() if k1 else None)

        result['EvaluationConfigs'] = []
        if self.evaluation_configs is not None:
            for k1 in self.evaluation_configs:
                result['EvaluationConfigs'].append(k1.to_map() if k1 else None)

        if self.evaluation_worker_count is not None:
            result['EvaluationWorkerCount'] = self.evaluation_worker_count

        if self.exception is not None:
            result['Exception'] = self.exception

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.flow_run_id is not None:
            result['FlowRunId'] = self.flow_run_id

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        result['Labels'] = []
        if self.labels is not None:
            for k1 in self.labels:
                result['Labels'].append(k1.to_map() if k1 else None)

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        result['NodeRunInfos'] = []
        if self.node_run_infos is not None:
            for k1 in self.node_run_infos:
                result['NodeRunInfos'].append(k1.to_map() if k1 else None)

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.run_name is not None:
            result['RunName'] = self.run_name

        if self.run_result is not None:
            result['RunResult'] = self.run_result

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        if self.run_timeout is not None:
            result['RunTimeout'] = self.run_timeout

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        if self.variant is not None:
            result['Variant'] = self.variant

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        self.child_runs = []
        if m.get('ChildRuns') is not None:
            for k1 in m.get('ChildRuns'):
                temp_model = main_models.FlowRunChildRuns()
                self.child_runs.append(temp_model.from_map(k1))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CredentialConfig') is not None:
            temp_model = main_models.FlowRunCredentialConfig()
            self.credential_config = temp_model.from_map(m.get('CredentialConfig'))

        if m.get('DataColumnMapping') is not None:
            self.data_column_mapping = m.get('DataColumnMapping')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.FlowRunDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EcsSpec') is not None:
            temp_model = main_models.FlowRunEcsSpec()
            self.ecs_spec = temp_model.from_map(m.get('EcsSpec'))

        self.envs = []
        if m.get('Envs') is not None:
            for k1 in m.get('Envs'):
                temp_model = main_models.FlowRunEnvs()
                self.envs.append(temp_model.from_map(k1))

        self.evaluation_configs = []
        if m.get('EvaluationConfigs') is not None:
            for k1 in m.get('EvaluationConfigs'):
                temp_model = main_models.FlowRunEvaluationConfigs()
                self.evaluation_configs.append(temp_model.from_map(k1))

        if m.get('EvaluationWorkerCount') is not None:
            self.evaluation_worker_count = m.get('EvaluationWorkerCount')

        if m.get('Exception') is not None:
            self.exception = m.get('Exception')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('FlowRunId') is not None:
            self.flow_run_id = m.get('FlowRunId')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        self.labels = []
        if m.get('Labels') is not None:
            for k1 in m.get('Labels'):
                temp_model = main_models.FlowRunLabels()
                self.labels.append(temp_model.from_map(k1))

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        self.node_run_infos = []
        if m.get('NodeRunInfos') is not None:
            for k1 in m.get('NodeRunInfos'):
                temp_model = main_models.FlowRunNodeRunInfos()
                self.node_run_infos.append(temp_model.from_map(k1))

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')

        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        if m.get('RunTimeout') is not None:
            self.run_timeout = m.get('RunTimeout')

        if m.get('UserVpc') is not None:
            temp_model = main_models.FlowRunUserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        if m.get('Variant') is not None:
            self.variant = m.get('Variant')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class FlowRunUserVpc(DaraModel):
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

class FlowRunNodeRunInfos(DaraModel):
    def __init__(
        self,
        duration: str = None,
        error_message: str = None,
        inputs: str = None,
        node_name: str = None,
        output: str = None,
        status: str = None,
        stdout: str = None,
    ):
        # 耗时
        self.duration = duration
        # 错误信息
        self.error_message = error_message
        # 输入
        self.inputs = inputs
        # 节点名称
        self.node_name = node_name
        # 输出
        self.output = output
        # 节点状态
        self.status = status
        # 日志信息
        self.stdout = stdout

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.inputs is not None:
            result['Inputs'] = self.inputs

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.output is not None:
            result['Output'] = self.output

        if self.status is not None:
            result['Status'] = self.status

        if self.stdout is not None:
            result['Stdout'] = self.stdout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Inputs') is not None:
            self.inputs = m.get('Inputs')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Stdout') is not None:
            self.stdout = m.get('Stdout')

        return self

class FlowRunLabels(DaraModel):
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

class FlowRunEvaluationConfigs(DaraModel):
    def __init__(
        self,
        data_column_mapping: Dict[str, str] = None,
        flow_source: main_models.FlowRunEvaluationConfigsFlowSource = None,
        inputs_override_config: str = None,
    ):
        # 映射配置
        self.data_column_mapping = data_column_mapping
        # 应用流来源
        self.flow_source = flow_source
        # 输入配置
        self.inputs_override_config = inputs_override_config

    def validate(self):
        if self.flow_source:
            self.flow_source.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_column_mapping is not None:
            result['DataColumnMapping'] = self.data_column_mapping

        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source.to_map()

        if self.inputs_override_config is not None:
            result['InputsOverrideConfig'] = self.inputs_override_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataColumnMapping') is not None:
            self.data_column_mapping = m.get('DataColumnMapping')

        if m.get('FlowSource') is not None:
            temp_model = main_models.FlowRunEvaluationConfigsFlowSource()
            self.flow_source = temp_model.from_map(m.get('FlowSource'))

        if m.get('InputsOverrideConfig') is not None:
            self.inputs_override_config = m.get('InputsOverrideConfig')

        return self

class FlowRunEvaluationConfigsFlowSource(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        # ID
        self.id = id
        # 名称
        self.name = name
        # 类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class FlowRunEnvs(DaraModel):
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

class FlowRunEcsSpec(DaraModel):
    def __init__(
        self,
        cpu: int = None,
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
        shared_memory: int = None,
    ):
        # CPU信息
        self.cpu = cpu
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
        # 共享内存
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

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CPU') is not None:
            self.cpu = m.get('CPU')

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

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        return self

class FlowRunDataSources(DaraModel):
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

class FlowRunCredentialConfig(DaraModel):
    def __init__(
        self,
        aliyun_env_role_key: str = None,
        credential_config_items: List[main_models.FlowRunCredentialConfigCredentialConfigItems] = None,
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
                temp_model = main_models.FlowRunCredentialConfigCredentialConfigItems()
                self.credential_config_items.append(temp_model.from_map(k1))

        if m.get('EnableCredentialInject') is not None:
            self.enable_credential_inject = m.get('EnableCredentialInject')

        return self

class FlowRunCredentialConfigCredentialConfigItems(DaraModel):
    def __init__(
        self,
        key: str = None,
        roles: List[main_models.FlowRunCredentialConfigCredentialConfigItemsRoles] = None,
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
                temp_model = main_models.FlowRunCredentialConfigCredentialConfigItemsRoles()
                self.roles.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class FlowRunCredentialConfigCredentialConfigItemsRoles(DaraModel):
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

class FlowRunChildRuns(DaraModel):
    def __init__(
        self,
        duration: int = None,
        flow_run_id: str = None,
        flow_source: main_models.FlowRunChildRunsFlowSource = None,
        gmt_create_time: str = None,
        gmt_finish_time: str = None,
        gmt_modified_time: str = None,
        gmt_start_time: str = None,
        job_info: main_models.FlowRunChildRunsJobInfo = None,
        run_mode: str = None,
        run_name: str = None,
        run_result: str = None,
        run_status: str = None,
    ):
        # 运行时长
        self.duration = duration
        # 应用流运行ID
        self.flow_run_id = flow_run_id
        # 应用流来源
        self.flow_source = flow_source
        # 创建时间
        self.gmt_create_time = gmt_create_time
        # 结束时间
        self.gmt_finish_time = gmt_finish_time
        # 修改时间
        self.gmt_modified_time = gmt_modified_time
        # 开始时间
        self.gmt_start_time = gmt_start_time
        # 任务信息
        self.job_info = job_info
        # 运行模式
        self.run_mode = run_mode
        # 运行名称
        self.run_name = run_name
        # 运行结果
        self.run_result = run_result
        # 运行状态
        self.run_status = run_status

    def validate(self):
        if self.flow_source:
            self.flow_source.validate()
        if self.job_info:
            self.job_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.duration is not None:
            result['Duration'] = self.duration

        if self.flow_run_id is not None:
            result['FlowRunId'] = self.flow_run_id

        if self.flow_source is not None:
            result['FlowSource'] = self.flow_source.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_finish_time is not None:
            result['GmtFinishTime'] = self.gmt_finish_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.gmt_start_time is not None:
            result['GmtStartTime'] = self.gmt_start_time

        if self.job_info is not None:
            result['JobInfo'] = self.job_info.to_map()

        if self.run_mode is not None:
            result['RunMode'] = self.run_mode

        if self.run_name is not None:
            result['RunName'] = self.run_name

        if self.run_result is not None:
            result['RunResult'] = self.run_result

        if self.run_status is not None:
            result['RunStatus'] = self.run_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('FlowRunId') is not None:
            self.flow_run_id = m.get('FlowRunId')

        if m.get('FlowSource') is not None:
            temp_model = main_models.FlowRunChildRunsFlowSource()
            self.flow_source = temp_model.from_map(m.get('FlowSource'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtFinishTime') is not None:
            self.gmt_finish_time = m.get('GmtFinishTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('GmtStartTime') is not None:
            self.gmt_start_time = m.get('GmtStartTime')

        if m.get('JobInfo') is not None:
            temp_model = main_models.FlowRunChildRunsJobInfo()
            self.job_info = temp_model.from_map(m.get('JobInfo'))

        if m.get('RunMode') is not None:
            self.run_mode = m.get('RunMode')

        if m.get('RunName') is not None:
            self.run_name = m.get('RunName')

        if m.get('RunResult') is not None:
            self.run_result = m.get('RunResult')

        if m.get('RunStatus') is not None:
            self.run_status = m.get('RunStatus')

        return self

class FlowRunChildRunsJobInfo(DaraModel):
    def __init__(
        self,
        job_id: str = None,
    ):
        # 任务ID
        self.job_id = job_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.job_id is not None:
            result['JobId'] = self.job_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('JobId') is not None:
            self.job_id = m.get('JobId')

        return self

class FlowRunChildRunsFlowSource(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        type: str = None,
    ):
        # ID
        self.id = id
        # 名称
        self.name = name
        # 类型
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

