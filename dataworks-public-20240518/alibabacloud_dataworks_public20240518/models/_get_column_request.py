# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetColumnRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID. You can refer to the response of the ListColumns operation and the [description of concepts related to metadata entities.](https://help.aliyun.com/document_detail/2880092.html)
        # 
        # The format: `${EntityType}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}:${Schema name}:${Table name}:${Column name}`. Use empty strings as placeholders for levels that do not exist.
        # 
        # >  For the MaxCompute and DLF types, use an empty string as the placeholder for the instance ID. For MaxCompute, the database name refers to the MaxCompute project name. If the project has schema enabled, you must specify the schema name. Otherwise, use an empty string as the placeholder for the schema name.
        # 
        # >  The catalog identifier of the StarRocks is the catalog name, and the catalog identifier of the DLF type is the catalog ID. Other types do not support catalog levels. Use empty strings as placeholders.
        # 
        # Examples of common ID formats
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
        # `instance_id`: the ID of the instance, which is required when the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, which is required when the data source is registered via a connection string.\\
        # `catalog_id`: The DLF catalog ID.\\
        # `project_name`: The MaxCompute project name.\\
        # `database_name`: The database name.\\
        # `schema_name`: The schema name. For the MaxCompute type, this is required only if the project has enabled schema; otherwise, use an empty string as a placeholder.\\
        # `table_name`: The table name.\\
        # `column_name`: The field name.
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

