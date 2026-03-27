# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class Column(DaraModel):
    def __init__(
        self,
        business_metadata: main_models.ColumnBusinessMetadata = None,
        comment: str = None,
        foreign_key: bool = None,
        id: str = None,
        name: str = None,
        partition_key: bool = None,
        position: int = None,
        primary_key: bool = None,
        table_id: str = None,
        type: str = None,
    ):
        # Business metadata.
        self.business_metadata = business_metadata
        # The comment.
        self.comment = comment
        # Specifies whether the column is a foreign key (only supported by MaxCompute).
        self.foreign_key = foreign_key
        # The ID. For more information, see [Description of concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is: `${EntityType}:${Instance ID or encoded URL}:${Catalog Identifier}:${Database name}:${Schema name}:${Table Name}:${Column name}`. Use empty strings as placeholders for non-existent hierarchy levels.
        # 
        # >  For the MaxCompute and DLF types, use an empty string as the placeholder for the instance ID. For MaxCompute, the database name refers to the MaxCompute project name. If the project has schema enabled, you must specify the schema name. Otherwise, use an empty string as the placeholder for the schema name.
        # 
        # >  For StarRocks, the catalog identifier is the catalog name. For DLF, it is the catalog ID. Other types do not support the catalog level and you can use an empty string as a placeholder.
        # 
        # Examples of ID formats for common types are as follows:
        # 
        # `maxcompute-column:::project_name:[schema_name]:table_name:column_name`
        # 
        # `dlf-column::catalog_id:database_name::table_name:column_name`
        # 
        # `hms-column:instance_id::database_name::table_name:column_name`
        # 
        # `holo-column:instance_id::database_name:schema_name:table_name:column_name`
        # 
        # `mysql-column:(instance_id|encoded_jdbc_url)::database_name::table_name:column_name`
        # 
        # > \\
        # `instance_id`: The instance ID, required when the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, which is required when the data source is registered via a connection string.\\
        # `catalog_id`: The DLF catalog ID.\\
        # `project_name`: The MaxCompute project name.\\
        # `database_name`: The database name.\\
        # `schema_name`: The schema name. For the MaxCompute type, this is required only if the project has enabled schema; otherwise, use an empty string as a placeholder.\\
        # `table_name`: The table name.\\
        # `column_name`: The field name.
        self.id = id
        # The name.
        self.name = name
        # Specifies whether the column is a partition key.
        self.partition_key = partition_key
        # The position of the field.
        self.position = position
        # Specifies whether the column is a primary key (only supported by MaxCompute).
        self.primary_key = primary_key
        # The table ID. You can refer to the `Table` object.
        self.table_id = table_id
        # The type.
        self.type = type

    def validate(self):
        if self.business_metadata:
            self.business_metadata.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_metadata is not None:
            result['BusinessMetadata'] = self.business_metadata.to_map()

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.foreign_key is not None:
            result['ForeignKey'] = self.foreign_key

        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        if self.partition_key is not None:
            result['PartitionKey'] = self.partition_key

        if self.position is not None:
            result['Position'] = self.position

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessMetadata') is not None:
            temp_model = main_models.ColumnBusinessMetadata()
            self.business_metadata = temp_model.from_map(m.get('BusinessMetadata'))

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ForeignKey') is not None:
            self.foreign_key = m.get('ForeignKey')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PartitionKey') is not None:
            self.partition_key = m.get('PartitionKey')

        if m.get('Position') is not None:
            self.position = m.get('Position')

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self



class ColumnBusinessMetadata(DaraModel):
    def __init__(
        self,
        description: str = None,
    ):
        # A business-level description of the field (supported only by MaxCompute, HMS (EMR clusters) and DLF.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

