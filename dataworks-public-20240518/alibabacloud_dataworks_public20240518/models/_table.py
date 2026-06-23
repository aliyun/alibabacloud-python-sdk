# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class Table(DaraModel):
    def __init__(
        self,
        business_metadata: main_models.TableBusinessMetadata = None,
        comment: str = None,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        parent_meta_entity_id: str = None,
        partition_keys: List[str] = None,
        table_type: str = None,
        technical_metadata: main_models.TableTechnicalMetadata = None,
    ):
        # The business metadata. This parameter is specific to DataWorks and includes instructions, tags, categories, upstream tasks, and extended information.
        self.business_metadata = business_metadata
        # The comment on the table.
        self.comment = comment
        # The table creation time, provided as a Unix timestamp in milliseconds.
        self.create_time = create_time
        # The ID of the entity. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${instance ID or escaped URL}:${data catalog identifier}:${database name}:${schema name}:${table name}`. Use an empty string as a placeholder for any non-existent level.
        # 
        # > For MaxCompute and DLF data types, use an empty string as a placeholder for the instance ID. For MaxCompute, the database name is the MaxCompute project name. You must provide a schema name for projects where the three-layer model is enabled. If the model is not enabled, use an empty string as a placeholder for the schema name.
        # 
        # > For StarRocks data types, the data catalog identifier is the catalog name. For DLF data types, the data catalog identifier is the catalog ID. Other data types do not support the catalog level. For these types, use an empty string as a placeholder.
        # 
        # The following are the ID formats for several common data types:
        # 
        # `maxcompute-table:::project_name:[schema_name]:table_name`
        # 
        # `dlf-table::catalog_id:database_name::table_name`
        # 
        # `hms-table:instance_id::database_name::table_name`
        # 
        # `holo-table:instance_id::database_name:schema_name:table_name`
        # 
        # `mysql-table:(instance_id|encoded_jdbc_url)::database_name::table_name`
        # 
        # > Placeholder descriptions:<br>
        # > `instance_id`: The instance ID. This is required when the data source is registered in instance mode.<br>
        # > `encoded_jdbc_url`: The URL-encoded JDBC connection string. This is required when the data source is registered by using a connection string.<br>
        # > `catalog_id`: The DLF catalog ID.<br>
        # > `project_name`: The MaxCompute project name.<br>
        # > `database_name`: The database name.<br>
        # > `schema_name`: The schema name. For the MaxCompute data type, this is required only if the project has the three-layer model enabled. Otherwise, use an empty string as a placeholder.<br>
        # > `table_name`: The table name.<br><br><br><br><br><br><br>
        self.id = id
        # The time the table was last modified, provided as a Unix timestamp in milliseconds.
        self.modify_time = modify_time
        # The name of the table.
        self.name = name
        # The ID of the parent metadata entity. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # - For data types that support schemas, such as `maxcompute/holo/postgresql/sqlserver/hybriddb_for_postgresql/oracle`, `ParentMetaEntityId` specifies the table\\"s database schema. For the MaxCompute data type, this applies only to MaxCompute projects with the three-layer model enabled. The format is `${EntityType}:${instance ID or escaped URL}:${data catalog identifier}:${database name}:${schema name}`. Use an empty string as a placeholder for any non-existent level.
        # 
        # - For other data types, `ParentMetaEntityId` specifies the table\\"s database. The format is `${EntityType}:${instance ID or escaped URL}:${data catalog identifier}:${database name}`. Use an empty string as a placeholder for any non-existent level.
        # 
        # > For MaxCompute and DLF data types, use an empty string as a placeholder for the instance ID. For the MaxCompute data type, the database name is the MaxCompute project name.
        # 
        # > For StarRocks data types, the data catalog identifier is the catalog name. For DLF data types, the data catalog identifier is the catalog ID. Other data types do not support the catalog level. For these types, use an empty string as a placeholder.
        # 
        # The following are the formats of `ParentMetaEntityId` for several common data types:
        # 
        # `maxcompute-project:::project_name`
        # 
        # `maxcompute-schema:::project_name:schema_name` (Only for projects with the three-layer model enabled)
        # 
        # `dlf-database::catalog_id:database_name`
        # 
        # `hms-database:instance_id::database_name`
        # 
        # `holo-schema:instance_id::database_name:schema_name`
        # 
        # `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > Placeholder descriptions:<br>
        # > `instance_id`: The instance ID. This is required when the data source is registered in instance mode.<br>
        # > `encoded_jdbc_url`: The URL-encoded JDBC connection string. This is required when the data source is registered by using a connection string.<br>
        # > `catalog_id`: The DLF catalog ID.<br>
        # > `project_name`: The MaxCompute project name.<br>
        # > `database_name`: The database name.<br>
        # > `schema_name`: The schema name.<br><br><br><br><br><br>
        self.parent_meta_entity_id = parent_meta_entity_id
        # The list of partition keys. This parameter is empty for non-partitioned tables.
        self.partition_keys = partition_keys
        # The table type. The value depends on the type of metadata collector.
        self.table_type = table_type
        # The technical metadata.
        self.technical_metadata = technical_metadata

    def validate(self):
        if self.business_metadata:
            self.business_metadata.validate()
        if self.technical_metadata:
            self.technical_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_metadata is not None:
            result['BusinessMetadata'] = self.business_metadata.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        if self.partition_keys is not None:
            result['PartitionKeys'] = self.partition_keys

        if self.table_type is not None:
            result['TableType'] = self.table_type

        if self.technical_metadata is not None:
            result['TechnicalMetadata'] = self.technical_metadata.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMetadata') is not None:
            temp_model = main_models.TableBusinessMetadata()
            self.business_metadata = temp_model.from_map(m.get('BusinessMetadata'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        if m.get('PartitionKeys') is not None:
            self.partition_keys = m.get('PartitionKeys')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        if m.get('TechnicalMetadata') is not None:
            temp_model = main_models.TableTechnicalMetadata()
            self.technical_metadata = temp_model.from_map(m.get('TechnicalMetadata'))

        return self

class TableTechnicalMetadata(DaraModel):
    def __init__(
        self,
        compressed: bool = None,
        input_format: str = None,
        location: str = None,
        output_format: str = None,
        owner: str = None,
        parameters: Dict[str, str] = None,
        serialization_library: str = None,
    ):
        # Indicates whether the table is compressed.
        self.compressed = compressed
        # The input format.
        self.input_format = input_format
        # The storage location.
        self.location = location
        # The output format.
        self.output_format = output_format
        # The table owner.
        self.owner = owner
        # The parameter information.
        self.parameters = parameters
        # The class used by the serializer/deserializer (SerDe).
        self.serialization_library = serialization_library

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.compressed is not None:
            result['Compressed'] = self.compressed

        if self.input_format is not None:
            result['InputFormat'] = self.input_format

        if self.location is not None:
            result['Location'] = self.location

        if self.output_format is not None:
            result['OutputFormat'] = self.output_format

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        if self.serialization_library is not None:
            result['SerializationLibrary'] = self.serialization_library

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Compressed') is not None:
            self.compressed = m.get('Compressed')

        if m.get('InputFormat') is not None:
            self.input_format = m.get('InputFormat')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('OutputFormat') is not None:
            self.output_format = m.get('OutputFormat')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        if m.get('SerializationLibrary') is not None:
            self.serialization_library = m.get('SerializationLibrary')

        return self

class TableBusinessMetadata(DaraModel):
    def __init__(
        self,
        categories: List[List[main_models.TableBusinessMetadataCategories]] = None,
        custom_attributes: Dict[str, List[str]] = None,
        extension: main_models.TableBusinessMetadataExtension = None,
        readme: str = None,
        tags: List[main_models.TableBusinessMetadataTags] = None,
        upstream_tasks: List[main_models.TableBusinessMetadataUpstreamTasks] = None,
    ):
        # The list of categories to which the table belongs.
        self.categories = categories
        # A map of custom attribute identifiers to lists of their corresponding values.
        self.custom_attributes = custom_attributes
        # Extended information. This parameter is supported only for the MaxCompute data type.
        self.extension = extension
        # The instructions for use.
        self.readme = readme
        # The list of tags.
        self.tags = tags
        # The list of upstream tasks.
        self.upstream_tasks = upstream_tasks

    def validate(self):
        if self.categories:
            for v1 in self.categories:
                for v2 in v1:
                     if v2:
                        v2.validate()
        if self.extension:
            self.extension.validate()
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()
        if self.upstream_tasks:
            for v1 in self.upstream_tasks:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Categories'] = []
        if self.categories is not None:
            for k1 in self.categories:
                l1 = []
                for k2 in k1:
                    l1.append(k2.to_map() if k2 else None)
                result['Categories'].append(l1)

        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.extension is not None:
            result['Extension'] = self.extension.to_map()

        if self.readme is not None:
            result['Readme'] = self.readme

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        result['UpstreamTasks'] = []
        if self.upstream_tasks is not None:
            for k1 in self.upstream_tasks:
                result['UpstreamTasks'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.categories = []
        if m.get('Categories') is not None:
            for k1 in m.get('Categories'):
                l1 = []
                for k2 in k1:
                    temp_model = main_models.TableBusinessMetadataCategories()
                    l1.append(temp_model.from_map(k2))
                self.categories.append(l1)

        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('Extension') is not None:
            temp_model = main_models.TableBusinessMetadataExtension()
            self.extension = temp_model.from_map(m.get('Extension'))

        if m.get('Readme') is not None:
            self.readme = m.get('Readme')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.TableBusinessMetadataTags()
                self.tags.append(temp_model.from_map(k1))

        self.upstream_tasks = []
        if m.get('UpstreamTasks') is not None:
            for k1 in m.get('UpstreamTasks'):
                temp_model = main_models.TableBusinessMetadataUpstreamTasks()
                self.upstream_tasks.append(temp_model.from_map(k1))

        return self

class TableBusinessMetadataUpstreamTasks(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The task ID.
        self.id = id
        # The task name.
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class TableBusinessMetadataTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key. This value cannot be empty.
        self.key = key
        # The tag value. This can be an empty string.
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

class TableBusinessMetadataExtension(DaraModel):
    def __init__(
        self,
        env_type: str = None,
        favor_count: int = None,
        project_id: int = None,
        read_count: int = None,
        view_count: int = None,
    ):
        # The environment type. Valid values:
        # 
        # - Prod: The production environment.
        # 
        # - Dev: The development environment.
        self.env_type = env_type
        # The number of times the table was favorited.
        self.favor_count = favor_count
        # The workspace ID.
        self.project_id = project_id
        # The number of reads.
        self.read_count = read_count
        # The number of views.
        self.view_count = view_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.favor_count is not None:
            result['FavorCount'] = self.favor_count

        if self.project_id is not None:
            result['ProjectId'] = self.project_id

        if self.read_count is not None:
            result['ReadCount'] = self.read_count

        if self.view_count is not None:
            result['ViewCount'] = self.view_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('FavorCount') is not None:
            self.favor_count = m.get('FavorCount')

        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')

        if m.get('ReadCount') is not None:
            self.read_count = m.get('ReadCount')

        if m.get('ViewCount') is not None:
            self.view_count = m.get('ViewCount')

        return self

class TableBusinessMetadataCategories(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        parent_id: str = None,
    ):
        # The category ID.
        self.id = id
        # The category name.
        self.name = name
        # The parent category\\"s ID. This can be an empty string.
        self.parent_id = parent_id

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

        if self.parent_id is not None:
            result['ParentId'] = self.parent_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentId') is not None:
            self.parent_id = m.get('ParentId')

        return self

