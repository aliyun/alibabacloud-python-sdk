# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetColumnRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID. You can refer to the response of the ListColumns operation and [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${Instance ID or URL-encoded JDBC URL}:${Data catalog identifier}:${Database name}:${Schema name}:${Table name}:${Column name}`. Use an empty string as a placeholder for non-existent levels.
        # 
        # > For MaxCompute and DLF types, use an empty string as a placeholder for the instance ID. For MaxCompute, the database name is the MaxCompute project name. If the three-level model is enabled for the project, you must provide the schema name. Otherwise, use an empty string as a placeholder for the schema name.
        # 
        # > For StarRocks, the data catalog identifier is the catalog name. For DLF, the data catalog identifier is the catalog ID. Other types do not support the catalog level, so you can use an empty string as a placeholder.
        # 
        # The following are the ID formats for common types:
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
        # > Others  
        # `instance_id`: The instance ID. This is required when the data source is registered in instance mode.   
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string. This is required when the data source is registered by using a connection string.   
        # `catalog_id`: The DLF catalog ID.   
        # `project_name`: The MaxCompute project name.   
        # `database_name`: The database name.   
        # `schema_name`: The schema name. For MaxCompute, this is required only if the three-level model is enabled for the project. Otherwise, use an empty string as a placeholder.    
        # `table_name`: The table name.    
        # `column_name`: The column name.
        # 
        # This parameter is required.
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        return self

