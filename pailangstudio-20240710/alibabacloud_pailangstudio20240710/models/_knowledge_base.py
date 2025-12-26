# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class KnowledgeBase(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        auto_update_config: main_models.KnowledgeBaseAutoUpdateConfig = None,
        chunk_config: main_models.KnowledgeBaseChunkConfig = None,
        creator: str = None,
        data_sources: List[main_models.KnowledgeBaseDataSources] = None,
        dataset_id: str = None,
        description: str = None,
        embedding_config: main_models.KnowledgeBaseEmbeddingConfig = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        index_column_config: main_models.KnowledgeBaseIndexColumnConfig = None,
        knowledge_base_id: str = None,
        knowledge_base_type: str = None,
        meta_data_config: main_models.KnowledgeBaseMetaDataConfig = None,
        name: str = None,
        output_dir: str = None,
        runtime_id: str = None,
        vector_dbconfig: main_models.KnowledgeBaseVectorDBConfig = None,
        version_name: str = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        self.auto_update_config = auto_update_config
        self.chunk_config = chunk_config
        self.creator = creator
        self.data_sources = data_sources
        self.dataset_id = dataset_id
        self.description = description
        self.embedding_config = embedding_config
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.index_column_config = index_column_config
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_base_type = knowledge_base_type
        self.meta_data_config = meta_data_config
        self.name = name
        self.output_dir = output_dir
        self.runtime_id = runtime_id
        self.vector_dbconfig = vector_dbconfig
        self.version_name = version_name
        self.workspace_id = workspace_id

    def validate(self):
        if self.auto_update_config:
            self.auto_update_config.validate()
        if self.chunk_config:
            self.chunk_config.validate()
        if self.data_sources:
            for v1 in self.data_sources:
                 if v1:
                    v1.validate()
        if self.embedding_config:
            self.embedding_config.validate()
        if self.index_column_config:
            self.index_column_config.validate()
        if self.meta_data_config:
            self.meta_data_config.validate()
        if self.vector_dbconfig:
            self.vector_dbconfig.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accessibility is not None:
            result['Accessibility'] = self.accessibility

        if self.auto_update_config is not None:
            result['AutoUpdateConfig'] = self.auto_update_config.to_map()

        if self.chunk_config is not None:
            result['ChunkConfig'] = self.chunk_config.to_map()

        if self.creator is not None:
            result['Creator'] = self.creator

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_config is not None:
            result['EmbeddingConfig'] = self.embedding_config.to_map()

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.index_column_config is not None:
            result['IndexColumnConfig'] = self.index_column_config.to_map()

        if self.knowledge_base_id is not None:
            result['KnowledgeBaseId'] = self.knowledge_base_id

        if self.knowledge_base_type is not None:
            result['KnowledgeBaseType'] = self.knowledge_base_type

        if self.meta_data_config is not None:
            result['MetaDataConfig'] = self.meta_data_config.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.output_dir is not None:
            result['OutputDir'] = self.output_dir

        if self.runtime_id is not None:
            result['RuntimeId'] = self.runtime_id

        if self.vector_dbconfig is not None:
            result['VectorDBConfig'] = self.vector_dbconfig.to_map()

        if self.version_name is not None:
            result['VersionName'] = self.version_name

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('AutoUpdateConfig') is not None:
            temp_model = main_models.KnowledgeBaseAutoUpdateConfig()
            self.auto_update_config = temp_model.from_map(m.get('AutoUpdateConfig'))

        if m.get('ChunkConfig') is not None:
            temp_model = main_models.KnowledgeBaseChunkConfig()
            self.chunk_config = temp_model.from_map(m.get('ChunkConfig'))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.KnowledgeBaseDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.KnowledgeBaseEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('EmbeddingConfig'))

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('IndexColumnConfig') is not None:
            temp_model = main_models.KnowledgeBaseIndexColumnConfig()
            self.index_column_config = temp_model.from_map(m.get('IndexColumnConfig'))

        if m.get('KnowledgeBaseId') is not None:
            self.knowledge_base_id = m.get('KnowledgeBaseId')

        if m.get('KnowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('KnowledgeBaseType')

        if m.get('MetaDataConfig') is not None:
            temp_model = main_models.KnowledgeBaseMetaDataConfig()
            self.meta_data_config = temp_model.from_map(m.get('MetaDataConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputDir') is not None:
            self.output_dir = m.get('OutputDir')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('VectorDBConfig') is not None:
            temp_model = main_models.KnowledgeBaseVectorDBConfig()
            self.vector_dbconfig = temp_model.from_map(m.get('VectorDBConfig'))

        if m.get('VersionName') is not None:
            self.version_name = m.get('VersionName')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class KnowledgeBaseVectorDBConfig(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        connection_id: str = None,
        connection_name: str = None,
        vector_dbtype: str = None,
    ):
        # Collectioin名称
        self.collection_name = collection_name
        # Embedding连接ID
        self.connection_id = connection_id
        # VectorDB连接名称
        self.connection_name = connection_name
        # VectorDB类型
        self.vector_dbtype = vector_dbtype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.collection_name is not None:
            result['CollectionName'] = self.collection_name

        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.vector_dbtype is not None:
            result['VectorDBType'] = self.vector_dbtype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('VectorDBType') is not None:
            self.vector_dbtype = m.get('VectorDBType')

        return self

class KnowledgeBaseMetaDataConfig(DaraModel):
    def __init__(
        self,
        custom_meta_data: List[main_models.KnowledgeBaseMetaDataConfigCustomMetaData] = None,
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
                temp_model = main_models.KnowledgeBaseMetaDataConfigCustomMetaData()
                self.custom_meta_data.append(temp_model.from_map(k1))

        return self

class KnowledgeBaseMetaDataConfigCustomMetaData(DaraModel):
    def __init__(
        self,
        key: str = None,
        reference_count: int = None,
        value_count: int = None,
        value_type: str = None,
    ):
        # 元数据Key
        self.key = key
        # 引用次数
        self.reference_count = reference_count
        # 值的个数
        self.value_count = value_count
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

        if self.reference_count is not None:
            result['ReferenceCount'] = self.reference_count

        if self.value_count is not None:
            result['ValueCount'] = self.value_count

        if self.value_type is not None:
            result['ValueType'] = self.value_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('ReferenceCount') is not None:
            self.reference_count = m.get('ReferenceCount')

        if m.get('ValueCount') is not None:
            self.value_count = m.get('ValueCount')

        if m.get('ValueType') is not None:
            self.value_type = m.get('ValueType')

        return self

class KnowledgeBaseIndexColumnConfig(DaraModel):
    def __init__(
        self,
        column_definitions: List[main_models.KnowledgeBaseIndexColumnConfigColumnDefinitions] = None,
        content_columns: List[main_models.KnowledgeBaseIndexColumnConfigContentColumns] = None,
        embedding_columns: List[main_models.KnowledgeBaseIndexColumnConfigEmbeddingColumns] = None,
    ):
        # 所有列名
        self.column_definitions = column_definitions
        # 内容检索列
        self.content_columns = content_columns
        # Embedding列
        self.embedding_columns = embedding_columns

    def validate(self):
        if self.column_definitions:
            for v1 in self.column_definitions:
                 if v1:
                    v1.validate()
        if self.content_columns:
            for v1 in self.content_columns:
                 if v1:
                    v1.validate()
        if self.embedding_columns:
            for v1 in self.embedding_columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ColumnDefinitions'] = []
        if self.column_definitions is not None:
            for k1 in self.column_definitions:
                result['ColumnDefinitions'].append(k1.to_map() if k1 else None)

        result['ContentColumns'] = []
        if self.content_columns is not None:
            for k1 in self.content_columns:
                result['ContentColumns'].append(k1.to_map() if k1 else None)

        result['EmbeddingColumns'] = []
        if self.embedding_columns is not None:
            for k1 in self.embedding_columns:
                result['EmbeddingColumns'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.column_definitions = []
        if m.get('ColumnDefinitions') is not None:
            for k1 in m.get('ColumnDefinitions'):
                temp_model = main_models.KnowledgeBaseIndexColumnConfigColumnDefinitions()
                self.column_definitions.append(temp_model.from_map(k1))

        self.content_columns = []
        if m.get('ContentColumns') is not None:
            for k1 in m.get('ContentColumns'):
                temp_model = main_models.KnowledgeBaseIndexColumnConfigContentColumns()
                self.content_columns.append(temp_model.from_map(k1))

        self.embedding_columns = []
        if m.get('EmbeddingColumns') is not None:
            for k1 in m.get('EmbeddingColumns'):
                temp_model = main_models.KnowledgeBaseIndexColumnConfigEmbeddingColumns()
                self.embedding_columns.append(temp_model.from_map(k1))

        return self

class KnowledgeBaseIndexColumnConfigEmbeddingColumns(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # 列Key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class KnowledgeBaseIndexColumnConfigContentColumns(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # 列Key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class KnowledgeBaseIndexColumnConfigColumnDefinitions(DaraModel):
    def __init__(
        self,
        key: str = None,
    ):
        # 列Key
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class KnowledgeBaseEmbeddingConfig(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        connection_name: str = None,
        model: str = None,
    ):
        # Embedding连接ID
        self.connection_id = connection_id
        # Embedding连接名称
        self.connection_name = connection_name
        # 模型
        self.model = model

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.connection_id is not None:
            result['ConnectionId'] = self.connection_id

        if self.connection_name is not None:
            result['ConnectionName'] = self.connection_name

        if self.model is not None:
            result['Model'] = self.model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('ConnectionName') is not None:
            self.connection_name = m.get('ConnectionName')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        return self

class KnowledgeBaseDataSources(DaraModel):
    def __init__(
        self,
        uri: str = None,
    ):
        # 统一资源识别码
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self

class KnowledgeBaseChunkConfig(DaraModel):
    def __init__(
        self,
        chunk_duration: int = None,
        chunk_overlap: int = None,
        chunk_size: int = None,
        chunk_strategy: str = None,
    ):
        # 分块时长
        self.chunk_duration = chunk_duration
        # 分块重叠大小
        self.chunk_overlap = chunk_overlap
        # 分块大小
        self.chunk_size = chunk_size
        # 分块策略
        self.chunk_strategy = chunk_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunk_duration is not None:
            result['ChunkDuration'] = self.chunk_duration

        if self.chunk_overlap is not None:
            result['ChunkOverlap'] = self.chunk_overlap

        if self.chunk_size is not None:
            result['ChunkSize'] = self.chunk_size

        if self.chunk_strategy is not None:
            result['ChunkStrategy'] = self.chunk_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChunkDuration') is not None:
            self.chunk_duration = m.get('ChunkDuration')

        if m.get('ChunkOverlap') is not None:
            self.chunk_overlap = m.get('ChunkOverlap')

        if m.get('ChunkSize') is not None:
            self.chunk_size = m.get('ChunkSize')

        if m.get('ChunkStrategy') is not None:
            self.chunk_strategy = m.get('ChunkStrategy')

        return self

class KnowledgeBaseAutoUpdateConfig(DaraModel):
    def __init__(
        self,
        ecs_specs: List[main_models.KnowledgeBaseAutoUpdateConfigEcsSpecs] = None,
        embedding_config: main_models.KnowledgeBaseAutoUpdateConfigEmbeddingConfig = None,
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
                temp_model = main_models.KnowledgeBaseAutoUpdateConfigEcsSpecs()
                self.ecs_specs.append(temp_model.from_map(k1))

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.KnowledgeBaseAutoUpdateConfigEmbeddingConfig()
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

class KnowledgeBaseAutoUpdateConfigEmbeddingConfig(DaraModel):
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

class KnowledgeBaseAutoUpdateConfigEcsSpecs(DaraModel):
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

