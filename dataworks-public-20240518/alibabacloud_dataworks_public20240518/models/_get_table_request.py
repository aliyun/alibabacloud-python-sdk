# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetTableRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
        include_business_metadata: bool = None,
    ):
        # The ID. You can refer to the response of the ListTables operation and the [concepts related to metadata entities.](https://help.aliyun.com/document_detail/2880092.html)
        # 
        # The format: `${EntityType}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}:${Table name}`. Use empty strings as placeholders for levels that do not exist.
        # 
        # >  For the MaxCompute and DLF types, use an empty string as the placeholder for the instance ID.
        # 
        # >  The catalog identifier of the StarRocks is the catalog name, and the catalog identifier of the DLF type is the catalog ID. Other types do not support the catalog level. Use an empty string as a placeholder.
        # 
        # >  For MaxCompute, the database name refers to the MaxCompute project name. If the project has schema enabled, you must specify the schema name. Otherwise, use an empty string as the placeholder for the schema name.
        # 
        # Examples of common ID formats
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
        # `instance_id`: The instance ID, required when the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, which is required when the data source is registered via a connection string.\\
        # `catalog_id`: The DLF catalog ID.\\
        # `project_name`: The MaxCompute project name.\\
        # `database_name`: The database name.\\
        # `schema_name`: The schema name. For the MaxCompute type, this is required only if the project has enabled schema. Otherwise, use an empty string as a placeholder.\\
        # `table_name`: The table name.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to include metadata. Default: false.
        self.include_business_metadata = include_business_metadata

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncludeBusinessMetadata') is not None:
            self.include_business_metadata = m.get('IncludeBusinessMetadata')

        return self

