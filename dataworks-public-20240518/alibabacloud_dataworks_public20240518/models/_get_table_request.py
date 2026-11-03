# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        include_business_metadata: bool = None,
        include_extended_properties: bool = None,
    ):
        # The ID. You can refer to the response of the ListTables operation and [Concepts of metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # 
        # The format is `${EntityType}:${Instance ID or URL-encoded JDBC URL}:${Catalog ID}:${Database name}:${Schema name}:${Table name}`. Use an empty string as a placeholder for non-existent levels.
        # 
        # > For MaxCompute and DLF, use an empty string as a placeholder for the instance ID.
        # 
        # > For StarRocks, the catalog identifier is the catalog name. For DLF, the catalog identifier is the catalog ID. Other types do not support the catalog level, so you can use an empty string as a placeholder.
        # 
        # > For MaxCompute, the database name is the MaxCompute project name. For projects with the three-level model enabled, you must provide the schema name. For projects with the three-level model disabled, use an empty string as a placeholder for the schema name.
        # 
        # The following are the ID formats for several common types:
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
        # > Where:  
        # `instance_id`: the instance ID, which is required when the data source is registered in instance mode.  
        # `encoded_jdbc_url`: the URL-encoded JDBC connection string, which is required when the data source is registered in connection string mode.   
        # `catalog_id`: the DLF catalog ID.   
        # `project_name`: the MaxCompute project name.   
        # `database_name`: the database name.   
        # `schema_name`: the schema name. For MaxCompute, this is required only when the three-level model is enabled for the project. If it is disabled, use an empty string as a placeholder.   
        # `table_name`: the table name.
        # 
        # Recommended process to obtain this parameter: First, call ListCrawlers to obtain the MetaEntityId of the metadata crawler. For types that include the catalog level, such as DLF and StarRocks, call ListCatalogs to obtain the catalog ID. Then, call ListDatabases to obtain the database ID. If necessary, call ListSchemas to obtain the schema ID. Finally, call ListTables to obtain the target table ID, and use the returned table ID as the Id parameter for this API.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to include business metadata. Default value: false.
        self.include_business_metadata = include_business_metadata
        # Specifies whether to return extended properties. If you set this parameter to `true`, extended properties are returned. If you set this parameter to `false`, extended properties are not returned.
        self.include_extended_properties = include_extended_properties

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.include_business_metadata is not None:
            result['IncludeBusinessMetadata'] = self.include_business_metadata

        if self.include_extended_properties is not None:
            result['IncludeExtendedProperties'] = self.include_extended_properties

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncludeBusinessMetadata') is not None:
            self.include_business_metadata = m.get('IncludeBusinessMetadata')

        if m.get('IncludeExtendedProperties') is not None:
            self.include_extended_properties = m.get('IncludeExtendedProperties')

        return self

