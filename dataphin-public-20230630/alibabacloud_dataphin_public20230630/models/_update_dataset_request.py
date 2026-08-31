# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class UpdateDatasetRequest(DaraModel):
    def __init__(
        self,
        op_tenant_id: int = None,
        op_user_id: str = None,
        project_id: str = None,
        update_command: main_models.UpdateDatasetRequestUpdateCommand = None,
    ):
        # The tenant ID.
        # 
        # This parameter is required.
        self.op_tenant_id = op_tenant_id
        self.op_user_id = op_user_id
        # The project ID.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The update request struct.
        # 
        # This parameter is required.
        self.update_command = update_command

    def validate(self):
        if self.update_command:
            self.update_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        if self.op_user_id is not None:
            result['OpUserId'] = self.op_user_id

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.update_command is not None:
            result['UpdateCommand'] = self.update_command.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        if m.get('OpUserId') is not None:
            self.op_user_id = m.get('OpUserId')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('UpdateCommand') is not None:
            temp_model = main_models.UpdateDatasetRequestUpdateCommand()
            self.update_command = temp_model.from_map(m.get('UpdateCommand'))

        return self

class UpdateDatasetRequestUpdateCommand(DaraModel):
    def __init__(
        self,
        api_info: main_models.UpdateDatasetRequestUpdateCommandApiInfo = None,
        content_type: str = None,
        data_cell_id: str = None,
        description: str = None,
        file_id: str = None,
        id: int = None,
        metadata_storage_type: str = None,
        name: str = None,
        owner: str = None,
        scenario: str = None,
        storage_type: str = None,
        type: str = None,
        version: str = None,
        version_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfig = None,
    ):
        self.api_info = api_info
        # **The content type.**
        self.content_type = content_type
        # The subject area ID.
        self.data_cell_id = data_cell_id
        # **The description.**
        self.description = description
        # The file ID (the file ID at creation time).
        # 
        # This parameter is required.
        self.file_id = file_id
        # The dataset ID (business primary key).
        # 
        # This parameter is required.
        self.id = id
        # **The metastore type.**
        self.metadata_storage_type = metadata_storage_type
        # The dataset name.
        self.name = name
        # The list of owner IDs, separated by commas.
        self.owner = owner
        # **Scenarios:** `OFFLINE` (offline, default) / `REALTIME` (real-time).
        self.scenario = scenario
        # **The storage type.**
        self.storage_type = storage_type
        # The dataset type.
        self.type = type
        # The version.
        self.version = version
        # The dataset version configuration.
        self.version_config = version_config

    def validate(self):
        if self.api_info:
            self.api_info.validate()
        if self.version_config:
            self.version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info is not None:
            result['ApiInfo'] = self.api_info.to_map()

        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.description is not None:
            result['Description'] = self.description

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.id is not None:
            result['Id'] = self.id

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
        if m.get('ApiInfo') is not None:
            temp_model = main_models.UpdateDatasetRequestUpdateCommandApiInfo()
            self.api_info = temp_model.from_map(m.get('ApiInfo'))

        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfig()
            self.version_config = temp_model.from_map(m.get('VersionConfig'))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfig(DaraModel):
    def __init__(
        self,
        file_storage_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfigFileStorageConfig = None,
        metadata_storage_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfig = None,
        realtime_meta_table_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfig = None,
        version_description: str = None,
    ):
        # The file storage configuration.
        self.file_storage_config = file_storage_config
        # The metastore configuration.
        self.metadata_storage_config = metadata_storage_config
        # The real-time meta table configuration. Takes effect when metadataStorageType is set to STREAM_TABLE.
        self.realtime_meta_table_config = realtime_meta_table_config
        # **Version description**
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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigFileStorageConfig()
            self.file_storage_config = temp_model.from_map(m.get('FileStorageConfig'))

        if m.get('MetadataStorageConfig') is not None:
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfig()
            self.metadata_storage_config = temp_model.from_map(m.get('MetadataStorageConfig'))

        if m.get('RealtimeMetaTableConfig') is not None:
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfig()
            self.realtime_meta_table_config = temp_model.from_map(m.get('RealtimeMetaTableConfig'))

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfig(DaraModel):
    def __init__(
        self,
        datasource_type: str = None,
        meta_table_name: str = None,
        project_id: int = None,
        table_schema: main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchema = None,
    ):
        # The meta table data source type (only KAFKA is supported in the current release).
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # The meta table name.
        # 
        # This parameter is required.
        self.meta_table_name = meta_table_name
        # The project ID to which the meta table belongs (cross-project access is supported).
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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns] = None,
    ):
        # **The field list.**
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
                temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The field description.
        self.comment = comment
        # **The array element subtype. Valid only when type is set to ARRAY.**
        self.element_type = element_type
        # **The maximum capacity of the array. This parameter is valid only when type is set to ARRAY. Default value: 4096.**
        self.max_capacity = max_capacity
        # **The field name.**
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the field is a primary key.
        self.pk = pk
        # **The field type.**
        # 
        # This parameter is required.
        self.type = type
        # Indicates whether the field is a URL.
        self.url = url
        # The vector index configuration. Configure this parameter when the field type is FLOAT_VECTOR, FLOAT16_VECTOR, or BFLOAT16_VECTOR. This parameter is used to specify the dimensions, index type, and similarity metric.
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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        embedding_model: str = None,
        index_params: Dict[str, Any] = None,
        index_type: str = None,
        similarity_type: str = None,
    ):
        # The embedding dimension.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The embedding model.
        # 
        # This parameter is required.
        self.embedding_model = embedding_model
        # The index build parameters. Different parameters are required based on the indexType. For example, HNSW requires {M:30, efConstruction:360}, and IVF_FLAT requires {nlist:128}.
        self.index_params = index_params
        # The index type. PostgreSQL supports IVFFlat and HNSW. Milvus supports all types.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type. Default value: COSINE. Valid values: COSINE, L2, and IP.
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

class UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_schema: str = None,
        metadata_storage_mode: str = None,
        metadata_storage_type: str = None,
        prod_schema: str = None,
        table_name: str = None,
        table_schema: main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchema = None,
    ):
        # **The data source ID.**
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # **The data source name.**
        self.data_source_name = data_source_name
        # **The development database/schema.**
        self.dev_schema = dev_schema
        # Specifies whether to store metadata in a new table or an existing table.
        # 
        # This parameter is required.
        self.metadata_storage_mode = metadata_storage_mode
        # **The metastore type.**
        self.metadata_storage_type = metadata_storage_type
        # **The production database/schema.**
        # 
        # This parameter is required.
        self.prod_schema = prod_schema
        # **The table name.**
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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumns] = None,
    ):
        # The field list.
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
                temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The field description.
        self.comment = comment
        # **The array element subtype. Valid only when type is set to ARRAY.**
        self.element_type = element_type
        # The maximum capacity of the array. Valid only when type is set to ARRAY. Default value: 4096.
        self.max_capacity = max_capacity
        # **The field name.**
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the field is a primary key.
        self.pk = pk
        # **The field type.**
        # 
        # This parameter is required.
        self.type = type
        # Indicates whether the field is a URL.
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
            temp_model = main_models.UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class UpdateDatasetRequestUpdateCommandVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
    def __init__(
        self,
        dimension: int = None,
        embedding_model: str = None,
        index_params: Dict[str, Any] = None,
        index_type: str = None,
        similarity_type: str = None,
    ):
        # The embedding dimension.
        # 
        # This parameter is required.
        self.dimension = dimension
        # The embedding model.
        # 
        # This parameter is required.
        self.embedding_model = embedding_model
        # The index build parameters. Different parameters are required based on the indexType. For example, HNSW requires {M:30, efConstruction:360}, and IVF_FLAT requires {nlist:128}.
        self.index_params = index_params
        # The index type. PostgreSQL supports IVFFlat and HNSW. Milvus supports all types.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type. Default value: COSINE. Valid values: COSINE, L2, and IP.
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

class UpdateDatasetRequestUpdateCommandVersionConfigFileStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_path: str = None,
        mount_path: str = None,
        prod_path: str = None,
    ):
        # **The data source ID.**
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

class UpdateDatasetRequestUpdateCommandApiInfo(DaraModel):
    def __init__(
        self,
        exec_timeout: int = None,
        execute_mode: int = None,
        os_api_group: int = None,
        os_project: int = None,
        protocol: int = None,
        request_method: int = None,
        request_param_list: List[main_models.UpdateDatasetRequestUpdateCommandApiInfoRequestParamList] = None,
        response_param_list: List[main_models.UpdateDatasetRequestUpdateCommandApiInfoResponseParamList] = None,
        timeout: int = None,
    ):
        self.exec_timeout = exec_timeout
        self.execute_mode = execute_mode
        self.os_api_group = os_api_group
        self.os_project = os_project
        self.protocol = protocol
        self.request_method = request_method
        self.request_param_list = request_param_list
        self.response_param_list = response_param_list
        self.timeout = timeout

    def validate(self):
        if self.request_param_list:
            for v1 in self.request_param_list:
                 if v1:
                    v1.validate()
        if self.response_param_list:
            for v1 in self.response_param_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exec_timeout is not None:
            result['ExecTimeout'] = self.exec_timeout

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.os_api_group is not None:
            result['OsApiGroup'] = self.os_api_group

        if self.os_project is not None:
            result['OsProject'] = self.os_project

        if self.protocol is not None:
            result['Protocol'] = self.protocol

        if self.request_method is not None:
            result['RequestMethod'] = self.request_method

        result['RequestParamList'] = []
        if self.request_param_list is not None:
            for k1 in self.request_param_list:
                result['RequestParamList'].append(k1.to_map() if k1 else None)

        result['ResponseParamList'] = []
        if self.response_param_list is not None:
            for k1 in self.response_param_list:
                result['ResponseParamList'].append(k1.to_map() if k1 else None)

        if self.timeout is not None:
            result['Timeout'] = self.timeout

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExecTimeout') is not None:
            self.exec_timeout = m.get('ExecTimeout')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('OsApiGroup') is not None:
            self.os_api_group = m.get('OsApiGroup')

        if m.get('OsProject') is not None:
            self.os_project = m.get('OsProject')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestMethod') is not None:
            self.request_method = m.get('RequestMethod')

        self.request_param_list = []
        if m.get('RequestParamList') is not None:
            for k1 in m.get('RequestParamList'):
                temp_model = main_models.UpdateDatasetRequestUpdateCommandApiInfoRequestParamList()
                self.request_param_list.append(temp_model.from_map(k1))

        self.response_param_list = []
        if m.get('ResponseParamList') is not None:
            for k1 in m.get('ResponseParamList'):
                temp_model = main_models.UpdateDatasetRequestUpdateCommandApiInfoResponseParamList()
                self.response_param_list.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class UpdateDatasetRequestUpdateCommandApiInfoResponseParamList(DaraModel):
    def __init__(
        self,
        descr: str = None,
        is_url: bool = None,
        param_name: str = None,
        param_type: str = None,
        sample: str = None,
    ):
        self.descr = descr
        self.is_url = is_url
        self.param_name = param_name
        self.param_type = param_type
        self.sample = sample

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.descr is not None:
            result['Descr'] = self.descr

        if self.is_url is not None:
            result['IsUrl'] = self.is_url

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.sample is not None:
            result['Sample'] = self.sample

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Descr') is not None:
            self.descr = m.get('Descr')

        if m.get('IsUrl') is not None:
            self.is_url = m.get('IsUrl')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        return self

class UpdateDatasetRequestUpdateCommandApiInfoRequestParamList(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        descr: str = None,
        is_url: bool = None,
        must: bool = None,
        param_name: str = None,
        param_type: str = None,
        sample: str = None,
    ):
        self.default_value = default_value
        self.descr = descr
        self.is_url = is_url
        self.must = must
        self.param_name = param_name
        self.param_type = param_type
        self.sample = sample

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.descr is not None:
            result['Descr'] = self.descr

        if self.is_url is not None:
            result['IsUrl'] = self.is_url

        if self.must is not None:
            result['Must'] = self.must

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.sample is not None:
            result['Sample'] = self.sample

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Descr') is not None:
            self.descr = m.get('Descr')

        if m.get('IsUrl') is not None:
            self.is_url = m.get('IsUrl')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        return self

