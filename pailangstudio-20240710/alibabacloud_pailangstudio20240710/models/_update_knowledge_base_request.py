# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class UpdateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        auto_update_config: main_models.UpdateKnowledgeBaseRequestAutoUpdateConfig = None,
        bind_runtime: bool = None,
        description: str = None,
        meta_data_config: main_models.UpdateKnowledgeBaseRequestMetaDataConfig = None,
        runtime_id: str = None,
        workspace_id: str = None,
    ):
        self.auto_update_config = auto_update_config
        self.bind_runtime = bind_runtime
        self.description = description
        self.meta_data_config = meta_data_config
        self.runtime_id = runtime_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.auto_update_config:
            self.auto_update_config.validate()
        if self.meta_data_config:
            self.meta_data_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_update_config is not None:
            result['AutoUpdateConfig'] = self.auto_update_config.to_map()

        if self.bind_runtime is not None:
            result['BindRuntime'] = self.bind_runtime

        if self.description is not None:
            result['Description'] = self.description

        if self.meta_data_config is not None:
            result['MetaDataConfig'] = self.meta_data_config.to_map()

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoUpdateConfig') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestAutoUpdateConfig()
            self.auto_update_config = temp_model.from_map(m.get('AutoUpdateConfig'))

        if m.get('BindRuntime') is not None:
            self.bind_runtime = m.get('BindRuntime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('MetaDataConfig') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestMetaDataConfig()
            self.meta_data_config = temp_model.from_map(m.get('MetaDataConfig'))

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class UpdateKnowledgeBaseRequestMetaDataConfig(DaraModel):
    def __init__(
        self,
        custom_meta_data: List[main_models.UpdateKnowledgeBaseRequestMetaDataConfigCustomMetaData] = None,
    ):
        # 自定义元数据
        self.custom_meta_data = custom_meta_data

    def validate(self):
        if self.custom_meta_data:
            for v1 in self.custom_meta_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomMetaData'] = []
        if self.custom_meta_data is not None:
            for k1 in self.custom_meta_data:
                result['CustomMetaData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.custom_meta_data = []
        if m.get('CustomMetaData') is not None:
            for k1 in m.get('CustomMetaData'):
                temp_model = main_models.UpdateKnowledgeBaseRequestMetaDataConfigCustomMetaData()
                self.custom_meta_data.append(temp_model.from_map(k1))

        return self

class UpdateKnowledgeBaseRequestMetaDataConfigCustomMetaData(DaraModel):
    def __init__(
        self,
        key: str = None,
        value_type: str = None,
    ):
        # 元数据Key
        self.key = key
        # 元数据Value类型
        self.value_type = value_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class UpdateKnowledgeBaseRequestAutoUpdateConfig(DaraModel):
    def __init__(
        self,
        ecs_specs: List[main_models.UpdateKnowledgeBaseRequestAutoUpdateConfigEcsSpecs] = None,
        embedding_config: main_models.UpdateKnowledgeBaseRequestAutoUpdateConfigEmbeddingConfig = None,
        max_running_time_in_seconds: int = None,
        resource_id: str = None,
        status: str = None,
        user_vpc: main_models.UserVpc = None,
    ):
        # 运行资源配置
        self.ecs_specs = ecs_specs
        # Embedding配置
        self.embedding_config = embedding_config
        # 任务最大运行时间
        self.max_running_time_in_seconds = max_running_time_in_seconds
        # 资源组ID
        self.resource_id = resource_id
        # 知识库自动更新状态
        self.status = status
        # 用户VPC配置
        self.user_vpc = user_vpc

    def validate(self):
        if self.ecs_specs:
            for v1 in self.ecs_specs:
                 if v1:
                    v1.validate()
        if self.embedding_config:
            self.embedding_config.validate()
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['EcsSpecs'] = []
        if self.ecs_specs is not None:
            for k1 in self.ecs_specs:
                result['EcsSpecs'].append(k1.to_map() if k1 else None)

        if self.embedding_config is not None:
            result['EmbeddingConfig'] = self.embedding_config.to_map()

        if self.max_running_time_in_seconds is not None:
            result['MaxRunningTimeInSeconds'] = self.max_running_time_in_seconds

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.status is not None:
            result['Status'] = self.status

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.ecs_specs = []
        if m.get('EcsSpecs') is not None:
            for k1 in m.get('EcsSpecs'):
                temp_model = main_models.UpdateKnowledgeBaseRequestAutoUpdateConfigEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.UpdateKnowledgeBaseRequestAutoUpdateConfigEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('EmbeddingConfig'))

        if m.get('MaxRunningTimeInSeconds') is not None:
            self.max_running_time_in_seconds = m.get('MaxRunningTimeInSeconds')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self

class UpdateKnowledgeBaseRequestAutoUpdateConfigEmbeddingConfig(DaraModel):
    def __init__(
        self,
        batch_size: int = None,
        concurrency: int = None,
    ):
        # Embedding分批大小
        self.batch_size = batch_size
        # Embedding并发数
        self.concurrency = concurrency

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_size is not None:
            result['BatchSize'] = self.batch_size

        if self.concurrency is not None:
            result['Concurrency'] = self.concurrency

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchSize') is not None:
            self.batch_size = m.get('BatchSize')

        if m.get('Concurrency') is not None:
            self.concurrency = m.get('Concurrency')

        return self

class UpdateKnowledgeBaseRequestAutoUpdateConfigEcsSpecs(DaraModel):
    def __init__(
        self,
        cpu: int = None,
        driver: str = None,
        gpu: int = None,
        gputype: str = None,
        instance_type: str = None,
        memory: int = None,
        pod_count: int = None,
        shared_memory: int = None,
        type: str = None,
    ):
        # CPU核数
        self.cpu = cpu
        # 驱动版本
        self.driver = driver
        # GPU卡数
        self.gpu = gpu
        # GPU类型
        self.gputype = gputype
        # 机型名称
        self.instance_type = instance_type
        # 内存大小
        self.memory = memory
        # 副本数量
        self.pod_count = pod_count
        # 共享内存容量
        self.shared_memory = shared_memory
        # 节点类型
        self.type = type

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

        if self.pod_count is not None:
            result['PodCount'] = self.pod_count

        if self.shared_memory is not None:
            result['SharedMemory'] = self.shared_memory

        if self.type is not None:
            result['Type'] = self.type

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

        if m.get('PodCount') is not None:
            self.pod_count = m.get('PodCount')

        if m.get('SharedMemory') is not None:
            self.shared_memory = m.get('SharedMemory')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

