# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

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
        # Indicates whether the field is a foreign key. Only MaxCompute supports this property.
        self.foreign_key = foreign_key
        # The ID. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${instance ID or URL-encoded connection string}:${data catalog identifier}:${database name}:${schema name}:${table name}:${field name}`. Use an empty string for any level that does not exist.
        # 
        # > For MaxCompute and DLF types, use an empty string for the instance ID. For MaxCompute, the database name is the MaxCompute project name. If the project uses the three-layer model, provide the schema name. Otherwise, use an empty string for the schema name.
        # 
        # > For StarRocks, the data catalog identifier is the catalog name. For DLF, it is the catalog ID. Other types do not support the catalog level, so use an empty string.
        # 
        # Examples of common ID formats:
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
        # > Where:<br>
        # > `instance_id`: The instance ID, required when the data source is registered in instance mode.<br>
        # > `encoded_jdbc_url`: The URL-encoded JDBC connection string, required when the data source is registered using a connection string.<br>
        # > `catalog_id`: The DLF catalog ID.<br>
        # > `project_name`: The MaxCompute project name.<br>
        # > `database_name`: The database name.<br>
        # > `schema_name`: The schema name. For MaxCompute, provide this only if the project uses the three-layer model. Otherwise, use an empty string.<br>
        # > `table_name`: The table name.<br>
        # > `column_name`: The field name.<br><br><br><br><br><br><br><br>
        self.id = id
        # The name.
        self.name = name
        # Indicates whether the field is a partition key.
        self.partition_key = partition_key
        # The position.
        self.position = position
        # Indicates whether the field is a primary key. Only MaxCompute supports this property.
        self.primary_key = primary_key
        # The table ID. For details, see the `Table` object.
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
        custom_attributes: Dict[str, List[str]] = None,
        description: str = None,
    ):
        # Custom attribute values. The key is the custom attribute identifier, and the value is a list of attribute values.
        self.custom_attributes = custom_attributes
        # The business description of the field. Supported only for MaxCompute, HMS (EMR cluster), and DLF types.
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.custom_attributes is not None:
            result['CustomAttributes'] = self.custom_attributes

        if self.description is not None:
            result['Description'] = self.description

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAttributes') is not None:
            self.custom_attributes = m.get('CustomAttributes')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        return self

