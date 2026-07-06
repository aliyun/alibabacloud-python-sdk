# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetColumnRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID. You can obtain this value from the response of the ListColumns operation. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${InstanceID or encoded URL}:${DataCatalogIdentifier}:${DatabaseName}:${SchemaName}:${TableName}:${ColumnName}`. Use an empty string as a placeholder for levels that do not exist.
        # 
        # > For MaxCompute and DLF types, use an empty string as a placeholder for the instance ID. For MaxCompute, the database name is the MaxCompute project name. Projects with the three-layer model enabled must include the schema name. For projects without the three-layer model, use an empty string as a placeholder for the schema name.
        # 
        # > For StarRocks, the data catalog identifier is the catalog name. For DLF, the data catalog identifier is the catalog ID. Other types do not support the catalog level. Use an empty string as a placeholder.
        # 
        # The following are ID format examples for common types:
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
        # > Other parameters:  
        # `instance_id`: The instance ID. This parameter is required when the data source is registered in instance mode.   
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string. This parameter is required when the data source is registered by using a connection string.   
        # `catalog_id`: The DLF catalog ID.   
        # `project_name`: The MaxCompute project name.   
        # `database_name`: The database name.   
        # `schema_name`: The schema name. For MaxCompute, this parameter is required only when the three-layer model is enabled for the project. If the three-layer model is not enabled, use an empty string as a placeholder.    
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

