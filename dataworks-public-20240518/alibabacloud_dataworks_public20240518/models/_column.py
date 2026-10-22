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
        statistics_infos: Dict[str, str] = None,
        table_id: str = None,
        technical_metadata: main_models.ColumnTechnicalMetadata = None,
        type: str = None,
    ):
        # The business metadata.
        self.business_metadata = business_metadata
        # The comment.
        self.comment = comment
        # Specifies whether the column is a foreign key. Currently, only the MaxCompute type is supported.
        self.foreign_key = foreign_key
        # The ID. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${Instance ID or URL-encoded URL}:${Catalog ID}:${Database name}:${Schema name}:${Table name}:${Column name}`. Use an empty string as a placeholder for non-existent levels.
        # 
        # > For MaxCompute and DLF types, use an empty string as a placeholder for the instance ID. For the MaxCompute type, the database name is the MaxCompute project name. Projects with the three-tier model enabled require the schema name. For projects without the three-tier model enabled, use an empty string as a placeholder for the schema name.
        # 
        # > For the StarRocks type, the catalog ID is the catalog name. For the DLF type, the catalog ID is the catalog ID. Other types do not support the catalog level, and an empty string can be used as a placeholder.
        # 
        # The following are the ID formats for several common types:
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
        # > Where:   
        # `instance_id`: The instance ID, which is required when the data source is registered in instance mode.   
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, which is required when the data source is registered in connection string mode.   
        # `catalog_id`: The DLF catalog ID.   
        # `project_name`: The MaxCompute project name.   
        # `database_name`: The database name.   
        # `schema_name`: The schema name. For the MaxCompute type, this is required only if the three-tier model is enabled for the project. If it is not enabled, use an empty string as a placeholder.    
        # `table_name`: The table name.   
        # `column_name`: The column name.
        self.id = id
        # The name.
        self.name = name
        # Specifies whether the column is a partition key.
        self.partition_key = partition_key
        # The position.
        self.position = position
        # Specifies whether the column is a primary key. Currently, only the MaxCompute type is supported.
        self.primary_key = primary_key
        self.statistics_infos = statistics_infos
        # The ID of the table. Refer to the Table object.
        self.table_id = table_id
        # The technical metadata.
        self.technical_metadata = technical_metadata
        # The type.
        self.type = type

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

        if self.statistics_infos is not None:
            result['StatisticsInfos'] = self.statistics_infos

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.technical_metadata is not None:
            result['TechnicalMetadata'] = self.technical_metadata.to_map()

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

        if m.get('StatisticsInfos') is not None:
            self.statistics_infos = m.get('StatisticsInfos')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TechnicalMetadata') is not None:
            temp_model = main_models.ColumnTechnicalMetadata()
            self.technical_metadata = temp_model.from_map(m.get('TechnicalMetadata'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ColumnTechnicalMetadata(DaraModel):
    def __init__(
        self,
        parameters: Dict[str, str] = None,
    ):
        # The technical parameters of the column, where the key is the parameter name and the value is a string. Objects or arrays are represented as JSON strings.
        self.parameters = parameters

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self



class ColumnBusinessMetadata(DaraModel):
    def __init__(
        self,
        custom_attributes: Dict[str, List[str]] = None,
        description: str = None,
    ):
        # The custom attribute values, where the key is the custom attribute identifier and the value is a list of attribute values.
        self.custom_attributes = custom_attributes
        # The business description of the column. Currently, only MaxCompute, HMS (EMR cluster), and DLF types are supported.
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

