# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateDatasetRequest(DaraModel):
    def __init__(
        self,
        create_command: main_models.CreateDatasetRequestCreateCommand = None,
        op_tenant_id: int = None,
        project_id: str = None,
    ):
        # The creation request.
        # 
        # This parameter is required.
        self.create_command = create_command
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id

    def validate(self):
        if self.create_command:
            self.create_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_command is not None:
            result['CreateCommand'] = self.create_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateCommand') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommand()
            self.create_command = temp_model.from_map(m.get('CreateCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        return self

class CreateDatasetRequestCreateCommand(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        data_cell_id: str = None,
        description: str = None,
        dir_name: str = None,
        file_id: str = None,
        metadata_storage_type: str = None,
        name: str = None,
        owner: str = None,
        scenario: str = None,
        storage_type: str = None,
        type: str = None,
        version: str = None,
        version_config: main_models.CreateDatasetRequestCreateCommandVersionConfig = None,
    ):
        # The dataset content type. Valid values: GENERAL, TEXT, AUDIO, VIDEO, IMAGE, TABLE, INDEX.
        # 
        # This parameter is required.
        self.content_type = content_type
        # The data domain ID.
        self.data_cell_id = data_cell_id
        # The description.
        self.description = description
        # The directory (obtained from the file service by using the fileId).
        # 
        # This parameter is required.
        self.dir_name = dir_name
        # The file ID.
        self.file_id = file_id
        # The metastore type.
        self.metadata_storage_type = metadata_storage_type
        # The dataset name.
        # 
        # This parameter is required.
        self.name = name
        # The list of owner IDs, separated by commas.
        self.owner = owner
        # The dataset scenarios. Valid values:
        # - OFFLINE: offline. This is the default value.
        # - REALTIME: real-time.
        # 
        # This parameter is required.
        self.scenario = scenario
        # The storage type.
        self.storage_type = storage_type
        # The dataset type. Valid values: FILE, TABLE, HYBRID.
        # 
        # This parameter is required.
        self.type = type
        # The version number. If not specified, the default version V1 is used.
        self.version = version
        # The version configuration.
        self.version_config = version_config

    def validate(self):
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.description is not None:
            result['Description'] = self.description

        if self.dir_name is not None:
            result['DirName'] = self.dir_name

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.metadata_storage_type is not None:
            result['MetadataStorageType'] = self.metadata_storage_type

        if self.name is not None:
            result['Name'] = self.name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.type is not None:
            result['Type'] = self.type

        if self.version is not None:
            result['Version'] = self.version

        if self.version_config is not None:
            result['VersionConfig'] = self.version_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DirName') is not None:
            self.dir_name = m.get('DirName')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('MetadataStorageType') is not None:
            self.metadata_storage_type = m.get('MetadataStorageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        if m.get('VersionConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfig()
            self.version_config = temp_model.from_map(m.get('VersionConfig'))

        return self

class CreateDatasetRequestCreateCommandVersionConfig(DaraModel):
    def __init__(
        self,
        file_storage_config: main_models.CreateDatasetRequestCreateCommandVersionConfigFileStorageConfig = None,
        metadata_storage_config: main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfig = None,
        realtime_meta_table_config: main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfig = None,
        version_description: str = None,
    ):
        # The file storage configuration.
        self.file_storage_config = file_storage_config
        # The metastore configuration.
        self.metadata_storage_config = metadata_storage_config
        # The real-time meta table configuration. Takes effect when metadataStorageType is set to STREAM_TABLE.
        self.realtime_meta_table_config = realtime_meta_table_config
        # The version description.
        self.version_description = version_description

    def validate(self):
        if self.file_storage_config:
            self.file_storage_config.validate()
        if self.metadata_storage_config:
            self.metadata_storage_config.validate()
        if self.realtime_meta_table_config:
            self.realtime_meta_table_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_storage_config is not None:
            result['FileStorageConfig'] = self.file_storage_config.to_map()

        if self.metadata_storage_config is not None:
            result['MetadataStorageConfig'] = self.metadata_storage_config.to_map()

        if self.realtime_meta_table_config is not None:
            result['RealtimeMetaTableConfig'] = self.realtime_meta_table_config.to_map()

        if self.version_description is not None:
            result['VersionDescription'] = self.version_description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileStorageConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigFileStorageConfig()
            self.file_storage_config = temp_model.from_map(m.get('FileStorageConfig'))

        if m.get('MetadataStorageConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfig()
            self.metadata_storage_config = temp_model.from_map(m.get('MetadataStorageConfig'))

        if m.get('RealtimeMetaTableConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfig()
            self.realtime_meta_table_config = temp_model.from_map(m.get('RealtimeMetaTableConfig'))

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

class CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfig(DaraModel):
    def __init__(
        self,
        datasource_type: str = None,
        meta_table_name: str = None,
        project_id: int = None,
        table_schema: main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchema = None,
    ):
        # The meta table data source type (only KAFKA is supported in this version).
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # The meta table name.
        # 
        # This parameter is required.
        self.meta_table_name = meta_table_name
        # The project ID of the meta table (cross-project supported).
        # 
        # This parameter is required.
        self.project_id = project_id
        # The table schema.
        self.table_schema = table_schema

    def validate(self):
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.datasource_type is not None:
            result['DatasourceType'] = self.datasource_type

        if self.meta_table_name is not None:
            result['MetaTableName'] = self.meta_table_name

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatasourceType') is not None:
            self.datasource_type = m.get('DatasourceType')

        if m.get('MetaTableName') is not None:
            self.meta_table_name = m.get('MetaTableName')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('TableSchema') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns] = None,
    ):
        # The column list.
        self.columns = columns

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The field comment.
        self.comment = comment
        # The array element subtype. Valid only when type is set to ARRAY.
        self.element_type = element_type
        # The maximum capacity of the array. Valid only when type is set to ARRAY. Default value: 4096.
        self.max_capacity = max_capacity
        # The field name.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether the field is a primary key.
        self.pk = pk
        # The field type.
        # 
        # This parameter is required.
        self.type = type
        # Specifies whether the field is a URL.
        self.url = url
        # The vector index configuration. Configure this when the field type is FLOAT_VECTOR/FLOAT16_VECTOR/BFLOAT16_VECTOR to set the dimension, index type, and similarity.
        self.vector_index_config = vector_index_config

    def validate(self):
        if self.vector_index_config:
            self.vector_index_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.element_type is not None:
            result['ElementType'] = self.element_type

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.name is not None:
            result['Name'] = self.name

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.vector_index_config is not None:
            result['VectorIndexConfig'] = self.vector_index_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ElementType') is not None:
            self.element_type = m.get('ElementType')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VectorIndexConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class CreateDatasetRequestCreateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        embedding_model: str = None,
        index_params: Dict[str, Any] = None,
        index_type: str = None,
        similarity_type: str = None,
    ):
        # The vector dimensions.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The embedding model.
        # 
        # This parameter is required.
        self.embedding_model = embedding_model
        # The index build parameters. Different parameters are required based on the indexType. For example, HNSW requires {M:30, efConstruction:360} and IVF_FLAT requires {nlist:128}.
        self.index_params = index_params
        # The index type. PostgreSQL supports IVFFlat and HNSW. Milvus supports all types.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type. Default value: COSINE. Valid values: COSINE, L2, IP.
        # 
        # This parameter is required.
        self.similarity_type = similarity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.index_params is not None:
            result['IndexParams'] = self.index_params

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.similarity_type is not None:
            result['SimilarityType'] = self.similarity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('IndexParams') is not None:
            self.index_params = m.get('IndexParams')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('SimilarityType') is not None:
            self.similarity_type = m.get('SimilarityType')

        return self

class CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_schema: str = None,
        metadata_storage_mode: str = None,
        metadata_storage_type: str = None,
        prod_schema: str = None,
        table_name: str = None,
        table_schema: main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchema = None,
    ):
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The data source name.
        self.data_source_name = data_source_name
        # The development database/schema.
        self.dev_schema = dev_schema
        # The metadata storage mode. Valid values:
        # - CREATE: create a new table.
        # - EXISTING: use an existing table.
        # 
        # This parameter is required.
        self.metadata_storage_mode = metadata_storage_mode
        # The metastore type.
        self.metadata_storage_type = metadata_storage_type
        # The production database/schema.
        # 
        # This parameter is required.
        self.prod_schema = prod_schema
        # The table name.
        # 
        # This parameter is required.
        self.table_name = table_name
        # The table schema.
        self.table_schema = table_schema

    def validate(self):
        if self.table_schema:
            self.table_schema.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.dev_schema is not None:
            result['DevSchema'] = self.dev_schema

        if self.metadata_storage_mode is not None:
            result['MetadataStorageMode'] = self.metadata_storage_mode

        if self.metadata_storage_type is not None:
            result['MetadataStorageType'] = self.metadata_storage_type

        if self.prod_schema is not None:
            result['ProdSchema'] = self.prod_schema

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema is not None:
            result['TableSchema'] = self.table_schema.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DevSchema') is not None:
            self.dev_schema = m.get('DevSchema')

        if m.get('MetadataStorageMode') is not None:
            self.metadata_storage_mode = m.get('MetadataStorageMode')

        if m.get('MetadataStorageType') is not None:
            self.metadata_storage_type = m.get('MetadataStorageType')

        if m.get('ProdSchema') is not None:
            self.prod_schema = m.get('ProdSchema')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchema') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumns] = None,
    ):
        # The column list.
        self.columns = columns

    def validate(self):
        if self.columns:
            for v1 in self.columns:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Columns'] = []
        if self.columns is not None:
            for k1 in self.columns:
                result['Columns'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.columns = []
        if m.get('Columns') is not None:
            for k1 in m.get('Columns'):
                temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The field comment.
        self.comment = comment
        # The array element subtype. Valid only when type is set to ARRAY.
        self.element_type = element_type
        # The maximum capacity of the array. Valid only when type is set to ARRAY. Default value: 4096.
        self.max_capacity = max_capacity
        # The field name.
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether the field is a primary key.
        self.pk = pk
        # The field type.
        # 
        # This parameter is required.
        self.type = type
        # Specifies whether the field is a URL.
        self.url = url
        # The vector index configuration.
        self.vector_index_config = vector_index_config

    def validate(self):
        if self.vector_index_config:
            self.vector_index_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.element_type is not None:
            result['ElementType'] = self.element_type

        if self.max_capacity is not None:
            result['MaxCapacity'] = self.max_capacity

        if self.name is not None:
            result['Name'] = self.name

        if self.pk is not None:
            result['Pk'] = self.pk

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.vector_index_config is not None:
            result['VectorIndexConfig'] = self.vector_index_config.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ElementType') is not None:
            self.element_type = m.get('ElementType')

        if m.get('MaxCapacity') is not None:
            self.max_capacity = m.get('MaxCapacity')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Pk') is not None:
            self.pk = m.get('Pk')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('VectorIndexConfig') is not None:
            temp_model = main_models.CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class CreateDatasetRequestCreateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        embedding_model: str = None,
        index_params: Dict[str, Any] = None,
        index_type: str = None,
        similarity_type: str = None,
    ):
        # The vector dimensions.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The embedding model.
        # 
        # This parameter is required.
        self.embedding_model = embedding_model
        # The index build parameters. Different parameters are required based on the indexType. For example, HNSW requires {M:30, efConstruction:360} and IVF_FLAT requires {nlist:128}.
        self.index_params = index_params
        # The index type. PostgreSQL supports IVFFlat and HNSW. Milvus supports all types.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type. Default value: COSINE. Valid values: COSINE, L2, IP.
        # 
        # This parameter is required.
        self.similarity_type = similarity_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension is not None:
            result['Dimension'] = self.dimension

        if self.embedding_model is not None:
            result['EmbeddingModel'] = self.embedding_model

        if self.index_params is not None:
            result['IndexParams'] = self.index_params

        if self.index_type is not None:
            result['IndexType'] = self.index_type

        if self.similarity_type is not None:
            result['SimilarityType'] = self.similarity_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Dimension') is not None:
            self.dimension = m.get('Dimension')

        if m.get('EmbeddingModel') is not None:
            self.embedding_model = m.get('EmbeddingModel')

        if m.get('IndexParams') is not None:
            self.index_params = m.get('IndexParams')

        if m.get('IndexType') is not None:
            self.index_type = m.get('IndexType')

        if m.get('SimilarityType') is not None:
            self.similarity_type = m.get('SimilarityType')

        return self

class CreateDatasetRequestCreateCommandVersionConfigFileStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_path: str = None,
        mount_path: str = None,
        prod_path: str = None,
    ):
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The data source name.
        self.data_source_name = data_source_name
        # The development path (not required for basic projects).
        self.dev_path = dev_path
        # The mount path.
        # 
        # This parameter is required.
        self.mount_path = mount_path
        # The production path.
        # 
        # This parameter is required.
        self.prod_path = prod_path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.data_source_name is not None:
            result['DataSourceName'] = self.data_source_name

        if self.dev_path is not None:
            result['DevPath'] = self.dev_path

        if self.mount_path is not None:
            result['MountPath'] = self.mount_path

        if self.prod_path is not None:
            result['ProdPath'] = self.prod_path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DataSourceName') is not None:
            self.data_source_name = m.get('DataSourceName')

        if m.get('DevPath') is not None:
            self.dev_path = m.get('DevPath')

        if m.get('MountPath') is not None:
            self.mount_path = m.get('MountPath')

        if m.get('ProdPath') is not None:
            self.prod_path = m.get('ProdPath')

        return self

