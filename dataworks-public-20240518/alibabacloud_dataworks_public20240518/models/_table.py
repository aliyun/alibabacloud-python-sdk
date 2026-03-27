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
        # The information about the business metadata that is related to DataWorks, including the usage notes, tags, categories, ancestor tasks, and extended information.
        self.business_metadata = business_metadata
        # The comments.
        self.comment = comment
        # The creation time. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The table ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The common format of this parameter is `${Entity type}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}:${Schema name}:${Table name}`. If a level does not exist, specify an empty string as a placeholder.
        # 
        # >  For MaxCompute and DLF tables, specify an empty string at the Instance ID level as a placeholder. For MaxCompute tables, specify a MaxCompute project name at the Database name level. If the three-layer model is enabled for your MaxCompute project, you must specify a schema name at the Schema name level. Otherwise, you can specify an empty string at the Schema name level as a placeholder.
        # 
        # >  For StarRocks tables, specify a catalog name at the Catalog identifier level. For DLF tables, specify a catalog ID at the Catalog identifier level. Other types of tables do not support the Catalog identifier level, and you can specify an empty string as a placeholder.
        # 
        # You can configure this parameter in one of the following formats based on your table type:
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
        # > \\
        # `instance_id`: the ID of an instance. If the related data source is added to DataWorks in Alibaba Cloud instance mode, you must configure this parameter.\\
        # `encoded_jdbc_url`: the JDBC connection string that is URL-encoded. If the related data source is added to DataWorks in connection string mode, you must configure this parameter.\\
        # `catalog_id`: the ID of a DLF catalog.\\
        # `project_name`: the name of a MaxCompute project.\\
        # `database_name`: the name of a database.\\
        # `schema_name`: the name of a schema. For a MaxCompute table, this parameter is required only if the three-layer model is enabled for the MaxCompute project to which the table belongs. If the schema feature is not enabled for the MaxCompute project, specify an empty string for this parameter as a placeholder.\\
        # `table_name`: the name of a table.
        self.id = id
        # The modification time. This value is a UNIX timestamp. Unit: milliseconds.
        self.modify_time = modify_time
        # The table name.
        self.name = name
        # The ID of a parent metadata entity. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # *   For data source types that support schemas, such as `MaxCompute, Hologres, PostgreSQL, SQL Server, HybridDB for PostgreSQL, and Oracle`, the `ParentMetaEntityId` parameter specifies the schema of the database to which the table belongs. In this case, the common format of this parameter is `${Entity type}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}:${Schema name}`. If a level does not exist, leave the level empty. For a MaxCompute data table, you must make sure that the three-layer model is enabled for the MaxCompute project to which the table belongs.
        # *   For other data source types that do not support schemas, the `ParentMetaEntityId` parameter specifies the database to which the table belongs. In this case, the common format of this parameter is `${Entity type}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}`. If a level does not exist, leave the level empty.
        # 
        # >  For MaxCompute and DLF tables, specify an empty string at the Instance ID level as a placeholder. For MaxCompute tables, specify a MaxCompute project name at the Database name level.
        # 
        # >  For StarRocks tables, specify a catalog name at the Catalog identifier level. For DLF tables, specify a catalog ID at the Catalog identifier level. Other types of tables do not support the Catalog identifier level, and you can specify an empty string as a placeholder.
        # 
        # You can configure this parameter in one of the following formats based on your table type:
        # 
        # `maxcompute-project:::project_name`
        # 
        # `maxcompute-schema:::project_name:schema_name` (Three-layer model enabled for the MaxCompute project)
        # 
        # `dlf-database::catalog_id:database_name`
        # 
        # `hms-database:instance_id::database_name`
        # 
        # `holo-schema:instance_id::database_name:schema_name`
        # 
        # `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > \\
        # `instance_id`: the ID of an instance. If the related data source is added to DataWorks in Alibaba Cloud instance mode, you must configure this parameter.\\
        # `encoded_jdbc_url`: the JDBC connection string that is URL-encoded. If the related data source is added to DataWorks in connection string mode, you must configure this parameter.\\
        # `catalog_id`: the ID of a DLF catalog.\\
        # `project_name`: the name of a MaxCompute project.\\
        # `database_name`: the name of a database.\\
        # `schema_name`: the name of a schema.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The partition keys. If the table is a non-partitioned table, leave this parameter empty.
        self.partition_keys = partition_keys
        # The table type. The value of this parameter is related to the type of metadata crawler.
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
        # Specifies whether the table is a compressed table. Valid values: true and false.
        self.compressed = compressed
        # The input format.
        self.input_format = input_format
        # The storage location of the table.
        self.location = location
        # The output format.
        self.output_format = output_format
        # The table owner.
        self.owner = owner
        # The information about parameters.
        self.parameters = parameters
        # The implementation class of SerDe.
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
        extension: main_models.TableBusinessMetadataExtension = None,
        readme: str = None,
        tags: List[main_models.TableBusinessMetadataTags] = None,
        upstream_tasks: List[main_models.TableBusinessMetadataUpstreamTasks] = None,
    ):
        # The categories.
        self.categories = categories
        # The extended information. Only MaxCompute tables supports this parameter.
        self.extension = extension
        # The usage notes.
        self.readme = readme
        # The tags.
        self.tags = tags
        # The ancestor tasks.
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
        # The ancestor task ID.
        self.id = id
        # The ancestor task name.
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
        # The tag key. You cannot leave this parameter empty.
        self.key = key
        # The tag value. You can leave this parameter empty.
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
        # The type of the environment. Valid values:
        # 
        # *   Prod
        # *   Dev
        self.env_type = env_type
        # The number of times the table is added to favorites.
        self.favor_count = favor_count
        # The DataWorks workspace ID.
        self.project_id = project_id
        # The number of times the table is read.
        self.read_count = read_count
        # The number of times the table is viewed.
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
        # The parent category ID. You can leave this parameter empty.
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

