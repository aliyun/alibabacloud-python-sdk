# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListDatasetsResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListDatasetsResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The backend response code.
        self.code = code
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The backend exception details.
        self.message = message
        # The paged result.
        self.page_result = page_result
        # Id of the request
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListDatasetsResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDatasetsResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        count: int = None,
        result_data: List[main_models.ListDatasetsResponseBodyPageResultResultData] = None,
    ):
        # The total count.
        self.count = count
        # The object.
        self.result_data = result_data

    def validate(self):
        if self.result_data:
            for v1 in self.result_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['ResultData'] = []
        if self.result_data is not None:
            for k1 in self.result_data:
                result['ResultData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.result_data = []
        if m.get('ResultData') is not None:
            for k1 in m.get('ResultData'):
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultData()
                self.result_data.append(temp_model.from_map(k1))

        return self

class ListDatasetsResponseBodyPageResultResultData(DaraModel):
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
        owner_list: List[main_models.ListDatasetsResponseBodyPageResultResultDataOwnerList] = None,
        project_id: int = None,
        project_name: str = None,
        scenario: str = None,
        storage_type: str = None,
        tenant_id: int = None,
        type: str = None,
        version_list: List[main_models.ListDatasetsResponseBodyPageResultResultDataVersionList] = None,
    ):
        # The content type.
        self.content_type = content_type
        # The creator ID.
        self.creator = creator
        # The creator name.
        self.creator_name = creator_name
        # The data domain ID.
        self.data_cell_id = data_cell_id
        # **The data domain name.**
        self.data_cell_name = data_cell_name
        # The description.
        self.description = description
        # The directory (retrieved from the file service by fileId).
        self.directory = directory
        # The file ID.
        self.file_id = file_id
        # The creation time.
        self.gmt_create = gmt_create
        # The modification time.
        self.gmt_modified = gmt_modified
        # The dataset ID (business primary key).
        self.id = id
        # The development owner ID.
        self.lock_owner = lock_owner
        # The name of the development owner (interface Displayed Fields).
        self.lock_owner_name = lock_owner_name
        # **The metastore type.**
        self.metadata_storage_type = metadata_storage_type
        # The dataset name.
        self.name = name
        # The owner list.
        self.owner_list = owner_list
        # The project ID.
        self.project_id = project_id
        # The project name.
        self.project_name = project_name
        # The dataset scenarios. Valid values:
        # - OFFLINE: offline (default).
        # - REALTIME: real-time.
        self.scenario = scenario
        # **The storage type.**
        self.storage_type = storage_type
        # The tenant ID.
        self.tenant_id = tenant_id
        # **The dataset type.**
        self.type = type
        # The version list.
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
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataOwnerList()
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
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionList()
                self.version_list.append(temp_model.from_map(k1))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionList(DaraModel):
    def __init__(
        self,
        api_info: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfo = None,
        creator: str = None,
        data_version_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfig = None,
        dataset_id: int = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        version: str = None,
    ):
        self.api_info = api_info
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
        if self.api_info:
            self.api_info.validate()
        if self.data_version_config:
            self.data_version_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_info is not None:
            result['ApiInfo'] = self.api_info.to_map()

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
        if m.get('ApiInfo') is not None:
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfo()
            self.api_info = temp_model.from_map(m.get('ApiInfo'))

        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('DataVersionConfig') is not None:
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfig()
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

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfig(DaraModel):
    def __init__(
        self,
        file_storage_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigFileStorageConfig = None,
        metadata_storage_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfig = None,
        realtime_meta_table_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfig = None,
        version_description: str = None,
    ):
        # The file storage configuration.
        self.file_storage_config = file_storage_config
        # The metastore configuration.
        self.metadata_storage_config = metadata_storage_config
        # The real-time meta table configuration (takes effect only when `metadataStorageType=REALTIME_META_TABLE`).
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
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigFileStorageConfig()
            self.file_storage_config = temp_model.from_map(m.get('FileStorageConfig'))

        if m.get('MetadataStorageConfig') is not None:
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfig()
            self.metadata_storage_config = temp_model.from_map(m.get('MetadataStorageConfig'))

        if m.get('RealtimeMetaTableConfig') is not None:
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfig()
            self.realtime_meta_table_config = temp_model.from_map(m.get('RealtimeMetaTableConfig'))

        if m.get('VersionDescription') is not None:
            self.version_description = m.get('VersionDescription')

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfig(DaraModel):
    def __init__(
        self,
        datasource_type: str = None,
        meta_table_name: str = None,
        project_id: int = None,
        table_schema: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema = None,
    ):
        # The meta table data source type (only KAFKA is available in this release).
        # 
        # This parameter is required.
        self.datasource_type = datasource_type
        # The meta table name.
        # 
        # This parameter is required.
        self.meta_table_name = meta_table_name
        # The project ID of the meta table (cross-project access is supported).
        # 
        # This parameter is required.
        self.project_id = project_id
        # The table schema configuration (reuses `MetadataStorageConfigDTO.TableSchemaDTO`).
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
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns] = None,
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
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # **The field description.**
        self.comment = comment
        # **The array element subtype. This parameter takes effect only when type is set to ARRAY.**
        self.element_type = element_type
        # **The maximum array capacity. This parameter takes effect only when type is set to ARRAY. Default value: 4096.**
        self.max_capacity = max_capacity
        # **The field name.**
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the field is a primary key.
        # 
        # This parameter is required.
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
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigRealtimeMetaTableConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
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
        # The index type. PG supports IVFFlat and HNSW. Milvus supports all index types.
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

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfig(DaraModel):
    def __init__(
        self,
        data_source_id: str = None,
        data_source_name: str = None,
        dev_schema: str = None,
        metadata_storage_mode: str = None,
        metadata_storage_type: str = None,
        prod_schema: str = None,
        table_name: str = None,
        table_schema: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchema = None,
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
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchema()
            self.table_schema = temp_model.from_map(m.get('TableSchema'))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchema(DaraModel):
    def __init__(
        self,
        columns: List[main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns] = None,
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
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns()
                self.columns.append(temp_model.from_map(k1))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumns(DaraModel):
    def __init__(
        self,
        comment: str = None,
        element_type: str = None,
        max_capacity: int = None,
        name: str = None,
        pk: bool = None,
        type: str = None,
        url: bool = None,
        vector_index_config: main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig = None,
    ):
        # The field description.
        self.comment = comment
        # The array element subtype. This parameter takes effect only when type is set to ARRAY.
        self.element_type = element_type
        # The maximum array capacity. This parameter takes effect only when type is set to ARRAY. Default value: 4096.
        self.max_capacity = max_capacity
        # The field name.
        # 
        # This parameter is required.
        self.name = name
        # Indicates whether the field is a primary key.
        # 
        # This parameter is required.
        self.pk = pk
        # The field type.
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
            temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig()
            self.vector_index_config = temp_model.from_map(m.get('VectorIndexConfig'))

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigMetadataStorageConfigTableSchemaColumnsVectorIndexConfig(DaraModel):
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
        # The index type. PG supports IVFFlat and HNSW. Milvus supports all index types.
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

class ListDatasetsResponseBodyPageResultResultDataVersionListDataVersionConfigFileStorageConfig(DaraModel):
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

class ListDatasetsResponseBodyPageResultResultDataVersionListApiInfo(DaraModel):
    def __init__(
        self,
        api_no: int = None,
        exec_timeout: int = None,
        execute_mode: int = None,
        os_api_group: int = None,
        os_api_group_name: str = None,
        os_project: int = None,
        os_project_name: str = None,
        protocol: int = None,
        request_method: int = None,
        request_param_list: List[main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoRequestParamList] = None,
        response_param_list: List[main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoResponseParamList] = None,
        timeout: int = None,
    ):
        self.api_no = api_no
        # This parameter is required.
        self.exec_timeout = exec_timeout
        # This parameter is required.
        self.execute_mode = execute_mode
        # This parameter is required.
        self.os_api_group = os_api_group
        self.os_api_group_name = os_api_group_name
        # This parameter is required.
        self.os_project = os_project
        self.os_project_name = os_project_name
        # This parameter is required.
        self.protocol = protocol
        # This parameter is required.
        self.request_method = request_method
        # This parameter is required.
        self.request_param_list = request_param_list
        self.response_param_list = response_param_list
        # This parameter is required.
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
        if self.api_no is not None:
            result['ApiNo'] = self.api_no

        if self.exec_timeout is not None:
            result['ExecTimeout'] = self.exec_timeout

        if self.execute_mode is not None:
            result['ExecuteMode'] = self.execute_mode

        if self.os_api_group is not None:
            result['OsApiGroup'] = self.os_api_group

        if self.os_api_group_name is not None:
            result['OsApiGroupName'] = self.os_api_group_name

        if self.os_project is not None:
            result['OsProject'] = self.os_project

        if self.os_project_name is not None:
            result['OsProjectName'] = self.os_project_name

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
        if m.get('ApiNo') is not None:
            self.api_no = m.get('ApiNo')

        if m.get('ExecTimeout') is not None:
            self.exec_timeout = m.get('ExecTimeout')

        if m.get('ExecuteMode') is not None:
            self.execute_mode = m.get('ExecuteMode')

        if m.get('OsApiGroup') is not None:
            self.os_api_group = m.get('OsApiGroup')

        if m.get('OsApiGroupName') is not None:
            self.os_api_group_name = m.get('OsApiGroupName')

        if m.get('OsProject') is not None:
            self.os_project = m.get('OsProject')

        if m.get('OsProjectName') is not None:
            self.os_project_name = m.get('OsProjectName')

        if m.get('Protocol') is not None:
            self.protocol = m.get('Protocol')

        if m.get('RequestMethod') is not None:
            self.request_method = m.get('RequestMethod')

        self.request_param_list = []
        if m.get('RequestParamList') is not None:
            for k1 in m.get('RequestParamList'):
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoRequestParamList()
                self.request_param_list.append(temp_model.from_map(k1))

        self.response_param_list = []
        if m.get('ResponseParamList') is not None:
            for k1 in m.get('ResponseParamList'):
                temp_model = main_models.ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoResponseParamList()
                self.response_param_list.append(temp_model.from_map(k1))

        if m.get('Timeout') is not None:
            self.timeout = m.get('Timeout')

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoResponseParamList(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        descr: str = None,
        is_url: bool = None,
        mapping_column: str = None,
        original_column: str = None,
        param_name: str = None,
        param_type: str = None,
        sample: str = None,
        seq_num: str = None,
    ):
        self.date_format = date_format
        self.descr = descr
        self.is_url = is_url
        self.mapping_column = mapping_column
        self.original_column = original_column
        self.param_name = param_name
        self.param_type = param_type
        self.sample = sample
        self.seq_num = seq_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.descr is not None:
            result['Descr'] = self.descr

        if self.is_url is not None:
            result['IsUrl'] = self.is_url

        if self.mapping_column is not None:
            result['MappingColumn'] = self.mapping_column

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.seq_num is not None:
            result['SeqNum'] = self.seq_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('Descr') is not None:
            self.descr = m.get('Descr')

        if m.get('IsUrl') is not None:
            self.is_url = m.get('IsUrl')

        if m.get('MappingColumn') is not None:
            self.mapping_column = m.get('MappingColumn')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('SeqNum') is not None:
            self.seq_num = m.get('SeqNum')

        return self

class ListDatasetsResponseBodyPageResultResultDataVersionListApiInfoRequestParamList(DaraModel):
    def __init__(
        self,
        date_format: str = None,
        default_value: str = None,
        descr: str = None,
        is_url: bool = None,
        mapping_column: str = None,
        must: bool = None,
        operator: str = None,
        optional: bool = None,
        original_column: str = None,
        param_name: str = None,
        param_type: str = None,
        sample: str = None,
        seq_num: int = None,
    ):
        self.date_format = date_format
        self.default_value = default_value
        self.descr = descr
        self.is_url = is_url
        self.mapping_column = mapping_column
        self.must = must
        self.operator = operator
        self.optional = optional
        self.original_column = original_column
        self.param_name = param_name
        self.param_type = param_type
        self.sample = sample
        self.seq_num = seq_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.date_format is not None:
            result['DateFormat'] = self.date_format

        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.descr is not None:
            result['Descr'] = self.descr

        if self.is_url is not None:
            result['IsUrl'] = self.is_url

        if self.mapping_column is not None:
            result['MappingColumn'] = self.mapping_column

        if self.must is not None:
            result['Must'] = self.must

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.optional is not None:
            result['Optional'] = self.optional

        if self.original_column is not None:
            result['OriginalColumn'] = self.original_column

        if self.param_name is not None:
            result['ParamName'] = self.param_name

        if self.param_type is not None:
            result['ParamType'] = self.param_type

        if self.sample is not None:
            result['Sample'] = self.sample

        if self.seq_num is not None:
            result['SeqNum'] = self.seq_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DateFormat') is not None:
            self.date_format = m.get('DateFormat')

        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Descr') is not None:
            self.descr = m.get('Descr')

        if m.get('IsUrl') is not None:
            self.is_url = m.get('IsUrl')

        if m.get('MappingColumn') is not None:
            self.mapping_column = m.get('MappingColumn')

        if m.get('Must') is not None:
            self.must = m.get('Must')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('OriginalColumn') is not None:
            self.original_column = m.get('OriginalColumn')

        if m.get('ParamName') is not None:
            self.param_name = m.get('ParamName')

        if m.get('ParamType') is not None:
            self.param_type = m.get('ParamType')

        if m.get('Sample') is not None:
            self.sample = m.get('Sample')

        if m.get('SeqNum') is not None:
            self.seq_num = m.get('SeqNum')

        return self

class ListDatasetsResponseBodyPageResultResultDataOwnerList(DaraModel):
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

