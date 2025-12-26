# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pailangstudio20240710 import models as main_models
from darabonba.model import DaraModel

class CreateKnowledgeBaseRequest(DaraModel):
    def __init__(
        self,
        accessibility: str = None,
        chunk_config: main_models.CreateKnowledgeBaseRequestChunkConfig = None,
        data_sources: List[main_models.CreateKnowledgeBaseRequestDataSources] = None,
        description: str = None,
        embedding_config: main_models.CreateKnowledgeBaseRequestEmbeddingConfig = None,
        index_column_config: main_models.CreateKnowledgeBaseRequestIndexColumnConfig = None,
        knowledge_base_type: str = None,
        meta_data_config: main_models.CreateKnowledgeBaseRequestMetaDataConfig = None,
        name: str = None,
        output_dir: str = None,
        runtime_id: str = None,
        vector_dbconfig: main_models.CreateKnowledgeBaseRequestVectorDBConfig = None,
        workspace_id: str = None,
    ):
        self.accessibility = accessibility
        # This parameter is required.
        self.chunk_config = chunk_config
        # This parameter is required.
        self.data_sources = data_sources
        self.description = description
        # This parameter is required.
        self.embedding_config = embedding_config
        self.index_column_config = index_column_config
        # This parameter is required.
        self.knowledge_base_type = knowledge_base_type
        self.meta_data_config = meta_data_config
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.output_dir = output_dir
        self.runtime_id = runtime_id
        # This parameter is required.
        self.vector_dbconfig = vector_dbconfig
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
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

        if self.chunk_config is not None:
            result['ChunkConfig'] = self.chunk_config.to_map()

        result['DataSources'] = []
        if self.data_sources is not None:
            for k1 in self.data_sources:
                result['DataSources'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.embedding_config is not None:
            result['EmbeddingConfig'] = self.embedding_config.to_map()

        if self.index_column_config is not None:
            result['IndexColumnConfig'] = self.index_column_config.to_map()

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

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Accessibility') is not None:
            self.accessibility = m.get('Accessibility')

        if m.get('ChunkConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestChunkConfig()
            self.chunk_config = temp_model.from_map(m.get('ChunkConfig'))

        self.data_sources = []
        if m.get('DataSources') is not None:
            for k1 in m.get('DataSources'):
                temp_model = main_models.CreateKnowledgeBaseRequestDataSources()
                self.data_sources.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EmbeddingConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestEmbeddingConfig()
            self.embedding_config = temp_model.from_map(m.get('EmbeddingConfig'))

        if m.get('IndexColumnConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestIndexColumnConfig()
            self.index_column_config = temp_model.from_map(m.get('IndexColumnConfig'))

        if m.get('KnowledgeBaseType') is not None:
            self.knowledge_base_type = m.get('KnowledgeBaseType')

        if m.get('MetaDataConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestMetaDataConfig()
            self.meta_data_config = temp_model.from_map(m.get('MetaDataConfig'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OutputDir') is not None:
            self.output_dir = m.get('OutputDir')

        if m.get('RuntimeId') is not None:
            self.runtime_id = m.get('RuntimeId')

        if m.get('VectorDBConfig') is not None:
            temp_model = main_models.CreateKnowledgeBaseRequestVectorDBConfig()
            self.vector_dbconfig = temp_model.from_map(m.get('VectorDBConfig'))

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class CreateKnowledgeBaseRequestVectorDBConfig(DaraModel):
    def __init__(
        self,
        collection_name: str = None,
        connection_id: str = None,
        vector_dbtype: str = None,
    ):
        # Collectioin名称
        self.collection_name = collection_name
        # Embedding连接ID
        self.connection_id = connection_id
        # VectorDB类型
        # 
        # This parameter is required.
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

        if self.vector_dbtype is not None:
            result['VectorDBType'] = self.vector_dbtype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CollectionName') is not None:
            self.collection_name = m.get('CollectionName')

        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('VectorDBType') is not None:
            self.vector_dbtype = m.get('VectorDBType')

        return self

class CreateKnowledgeBaseRequestMetaDataConfig(DaraModel):
    def __init__(
        self,
        custom_meta_data: List[main_models.CreateKnowledgeBaseRequestMetaDataConfigCustomMetaData] = None,
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
                temp_model = main_models.CreateKnowledgeBaseRequestMetaDataConfigCustomMetaData()
                self.custom_meta_data.append(temp_model.from_map(k1))

        return self

class CreateKnowledgeBaseRequestMetaDataConfigCustomMetaData(DaraModel):
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

class CreateKnowledgeBaseRequestIndexColumnConfig(DaraModel):
    def __init__(
        self,
        column_definitions: List[main_models.CreateKnowledgeBaseRequestIndexColumnConfigColumnDefinitions] = None,
        content_columns: List[main_models.CreateKnowledgeBaseRequestIndexColumnConfigContentColumns] = None,
        embedding_columns: List[main_models.CreateKnowledgeBaseRequestIndexColumnConfigEmbeddingColumns] = None,
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
                temp_model = main_models.CreateKnowledgeBaseRequestIndexColumnConfigColumnDefinitions()
                self.column_definitions.append(temp_model.from_map(k1))

        self.content_columns = []
        if m.get('ContentColumns') is not None:
            for k1 in m.get('ContentColumns'):
                temp_model = main_models.CreateKnowledgeBaseRequestIndexColumnConfigContentColumns()
                self.content_columns.append(temp_model.from_map(k1))

        self.embedding_columns = []
        if m.get('EmbeddingColumns') is not None:
            for k1 in m.get('EmbeddingColumns'):
                temp_model = main_models.CreateKnowledgeBaseRequestIndexColumnConfigEmbeddingColumns()
                self.embedding_columns.append(temp_model.from_map(k1))

        return self

class CreateKnowledgeBaseRequestIndexColumnConfigEmbeddingColumns(DaraModel):
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

class CreateKnowledgeBaseRequestIndexColumnConfigContentColumns(DaraModel):
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

class CreateKnowledgeBaseRequestIndexColumnConfigColumnDefinitions(DaraModel):
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

class CreateKnowledgeBaseRequestEmbeddingConfig(DaraModel):
    def __init__(
        self,
        connection_id: str = None,
        model: str = None,
    ):
        # Embedding连接ID
        # 
        # This parameter is required.
        self.connection_id = connection_id
        # 模型
        # 
        # This parameter is required.
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

        if self.model is not None:
            result['Model'] = self.model

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnectionId') is not None:
            self.connection_id = m.get('ConnectionId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        return self

class CreateKnowledgeBaseRequestDataSources(DaraModel):
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

class CreateKnowledgeBaseRequestChunkConfig(DaraModel):
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

