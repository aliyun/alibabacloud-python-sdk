# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetDatasetResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_dto: main_models.GetDatasetResponseBodyDatasetDTO = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The dataset object.
        self.dataset_dto = dataset_dto
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The details of the backend exception.
        self.message = message
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.dataset_dto:
            self.dataset_dto.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_dto is not None:
            result['DatasetDTO'] = self.dataset_dto.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetDTO') is not None:
            temp_model = main_models.GetDatasetResponseBodyDatasetDTO()
            self.dataset_dto = temp_model.from_map(m.get('DatasetDTO'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetDatasetResponseBodyDatasetDTO(DaraModel):
    def __init__(
        self,
        content_type: str = None,
        creator: str = None,
        creator_name: str = None,
        data_cell_id: str = None,
        data_cell_name: str = None,
        description: str = None,
        directory: str = None,
        file_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        lock_owner: str = None,
        lock_owner_name: str = None,
        metadata_storage_type: str = None,
        name: str = None,
        owner_list: List[main_models.GetDatasetResponseBodyDatasetDTOOwnerList] = None,
        project_id: int = None,
        project_name: str = None,
        scenario: str = None,
        storage_type: str = None,
        tenant_id: int = None,
        type: str = None,
        version_list: List[main_models.GetDatasetResponseBodyDatasetDTOVersionList] = None,
    ):
        # The content type.
        self.content_type = content_type
        # The creator ID.
        self.creator = creator
        # The creator name.
        self.creator_name = creator_name
        # The subject area ID.
        self.data_cell_id = data_cell_id
        # The subject area name.
        self.data_cell_name = data_cell_name
        # The description.
        self.description = description
        # The directory (retrieved from the file service by using the fileId).
        self.directory = directory
        # The file ID.
        self.file_id = file_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The dataset ID (business primary key).
        self.id = id
        # The ID of the development owner.
        self.lock_owner = lock_owner
        # The display name of the development owner on the interface.
        self.lock_owner_name = lock_owner_name
        # The metastore type.
        self.metadata_storage_type = metadata_storage_type
        # The dataset name.
        self.name = name
        # The list of owners.
        self.owner_list = owner_list
        # The ID of the project to which the dataset belongs.
        self.project_id = project_id
        # The name of the project to which the dataset belongs.
        self.project_name = project_name
        # The dataset scenarios. Valid values:
        # - OFFLINE: offline (default).
        # - REALTIME: real-time.
        self.scenario = scenario
        # The storage type.
        self.storage_type = storage_type
        # The tenant ID.
        self.tenant_id = tenant_id
        # The dataset type.
        self.type = type
        # The list of versions.
        self.version_list = version_list

    def validate(self):
        if self.owner_list:
            for v1 in self.owner_list:
                 if v1:
                    v1.validate()
        if self.version_list:
            for v1 in self.version_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content_type is not None:
            result['ContentType'] = self.content_type

        if self.creator is not None:
            result['Creator'] = self.creator

        if self.creator_name is not None:
            result['CreatorName'] = self.creator_name

        if self.data_cell_id is not None:
            result['DataCellId'] = self.data_cell_id

        if self.data_cell_name is not None:
            result['DataCellName'] = self.data_cell_name

        if self.description is not None:
            result['Description'] = self.description

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.lock_owner is not None:
            result['LockOwner'] = self.lock_owner

        if self.lock_owner_name is not None:
            result['LockOwnerName'] = self.lock_owner_name

        if self.metadata_storage_type is not None:
            result['MetadataStorageType'] = self.metadata_storage_type

        if self.name is not None:
            result['Name'] = self.name

        result['OwnerList'] = []
        if self.owner_list is not None:
            for k1 in self.owner_list:
                result['OwnerList'].append(k1.to_map() if k1 else None)

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.scenario is not None:
            result['Scenario'] = self.scenario

        if self.storage_type is not None:
            result['StorageType'] = self.storage_type

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        if self.type is not None:
            result['Type'] = self.type

        result['VersionList'] = []
        if self.version_list is not None:
            for k1 in self.version_list:
                result['VersionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('CreatorName') is not None:
            self.creator_name = m.get('CreatorName')

        if m.get('DataCellId') is not None:
            self.data_cell_id = m.get('DataCellId')

        if m.get('DataCellName') is not None:
            self.data_cell_name = m.get('DataCellName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LockOwner') is not None:
            self.lock_owner = m.get('LockOwner')

        if m.get('LockOwnerName') is not None:
            self.lock_owner_name = m.get('LockOwnerName')

        if m.get('MetadataStorageType') is not None:
            self.metadata_storage_type = m.get('MetadataStorageType')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.owner_list = []
        if m.get('OwnerList') is not None:
            for k1 in m.get('OwnerList'):
                temp_model = main_models.GetDatasetResponseBodyDatasetDTOOwnerList()
                self.owner_list.append(temp_model.from_map(k1))

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('Scenario') is not None:
            self.scenario = m.get('Scenario')

        if m.get('StorageType') is not None:
            self.storage_type = m.get('StorageType')

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.version_list = []
        if m.get('VersionList') is not None:
            for k1 in m.get('VersionList'):
                temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionList()
                self.version_list.append(temp_model.from_map(k1))

        return self

class GetDatasetResponseBodyDatasetDTOVersionList(DaraModel):
    def __init__(
        self,
        creator: str = None,
        data_version_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfig = None,
        dataset_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        version: str = None,
    ):
        # The creator ID.
        self.creator = creator
        # The dataset version configuration.
        self.data_version_config = data_version_config
        # The dataset ID.
        self.dataset_id = dataset_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The version ID.
        self.id = id
        # The version number.
        self.version = version

    def validate(self):
        if self.data_version_config:
            self.data_version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.data_version_config is not None:
            result['DataVersionConfig'] = self.data_version_config.to_map()

        if self.dataset_id is not None:
            result['DatasetId'] = self.dataset_id

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataVersionConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfig()
            self.data_version_config = temp_model.from_map(m.get('DataVersionConfig'))

        if m.get('DatasetId') is not None:
            self.dataset_id = m.get('DatasetId')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfig(DaraModel):
    def __init__(
        self,
        file_storage_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigFileStorageConfig = None,
        metadata_storage_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfig = None,
        realtime_meta_table_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfig = None,
        version_description: str = None,
    ):
        # The file storage configuration.
        self.file_storage_config = file_storage_config
        # The metastore configuration.
        self.metadata_storage_config = metadata_storage_config
        # The real-time meta table configuration. This parameter takes effect only when metadataStorageType is set to REALTIME_META_TABLE.
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
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigFileStorageConfig()
            self.file_storage_config = temp_model.from_map(m.get('FileStorageConfig'))

        if m.get('MetadataStorageConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfig()
            self.metadata_storage_config = temp_model.from_map(m.get('MetadataStorageConfig'))

        if m.get('RealtimeMetaTableConfig') is not None:
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfig()
            self.realtime_meta_table_config = temp_model.from_map(m.get('RealtimeMetaTableConfig'))

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfig(DaraModel):
    def __init__(
        self,
        datasource_type: str = None,
        meta_table_name: str = None,
        project_id: int = None,
        table_schema: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema = None,
    ):
        # The data source type of the meta table. Only KAFKA is supported in the current release.
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # The meta table name.
        # 
        # This parameter is required.
        self.meta_table_name = meta_table_name
        # The project ID to which the meta table belongs. Cross-project references are supported.
        # 
        # This parameter is required.
        self.project_id = project_id
        # The table schema configuration (reuses MetadataStorageConfigDTO.TableSchemaDTO).
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
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns] = None,
    ):
        # The list of columns.
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
                temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The column comment.
        self.comment = comment
        # The array element subtype.
        self.element_type = element_type
        # The maximum array capacity.
        self.max_capacity = max_capacity
        # The column name.
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the column is a primary key.
        # 
        # This parameter is required.
        self.pk = pk
        # The column type.
        # 
        # This parameter is required.
        self.type = type
        # Indicates whether the column is a URL.
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
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
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
        # The index build parameters.
        self.index_params = index_params
        # The index type.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type.
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

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_schema: str = None,
        metadata_storage_mode: str = None,
        metadata_storage_type: str = None,
        prod_schema: str = None,
        table_name: str = None,
        table_schema: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchema = None,
    ):
        # The data source ID.
        # 
        # This parameter is required.
        self.data_source_id = data_source_id
        # The data source name.
        self.data_source_name = data_source_name
        # The development database/schema.
        self.dev_schema = dev_schema
        # The storage destination (new table or existing table).
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
        # The table schema configuration.
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
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns] = None,
    ):
        # The list of columns.
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
                temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The column comment.
        self.comment = comment
        # The array element subtype. This parameter is valid only when type is set to ARRAY.
        self.element_type = element_type
        # The maximum array capacity. This parameter is valid only when type is set to ARRAY. Default value: 4096.
        self.max_capacity = max_capacity
        # The column name.
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the column is a primary key.
        # 
        # This parameter is required.
        self.pk = pk
        # The column type.
        # 
        # This parameter is required.
        self.type = type
        # Indicates whether the column is a URL.
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
            temp_model = main_models.GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
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
        # The index build parameters. Different parameters are required depending on the index type. For example, HNSW requires {M:30, efConstruction:360}, and IVF_FLAT requires {nlist:128}.
        self.index_params = index_params
        # The index type. PG supports IVFFlat and HNSW. Milvus supports all types.
        # 
        # This parameter is required.
        self.index_type = index_type
        # The similarity type. Default value: COSINE. COSINE corresponds to vector_cosine_ops, L2 corresponds to vector_l2_ops, and IP corresponds to vector_ip_ops.
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

class GetDatasetResponseBodyDatasetDTOVersionListDataVersionConfigFileStorageConfig(DaraModel):
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

class GetDatasetResponseBodyDatasetDTOOwnerList(DaraModel):
    def __init__(
        self,
        user_id: str = None,
        user_name: str = None,
    ):
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

