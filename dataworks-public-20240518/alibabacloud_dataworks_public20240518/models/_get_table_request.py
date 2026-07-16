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
        # The ID. You can obtain this value from the response of the ListTables operation. For more information, see [Metadata entity concepts](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # 
        # The format is `${EntityType}:${InstanceID or encoded URL}:${DataCatalogIdentifier}:${DatabaseName}:${SchemaName}:${TableName}`. Use an empty string as a placeholder for levels that do not exist.
        # 
        # > For MaxCompute and DLF types, use an empty string as a placeholder for the instance ID.
        # 
        # > For StarRocks, the data catalog identifier is the catalog name. For DLF, the data catalog identifier is the catalog ID. Other types do not support the catalog level. Use an empty string as a placeholder.
        # 
        # > For MaxCompute, the database name is the MaxCompute project name. Projects with the three-layer model enabled require a schema name. For projects without the three-layer model enabled, use an empty string as a placeholder for the schema name.
        # 
        # The following examples show the ID formats for common types:
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
        # > Where  
        # `instance_id`: The instance ID. This is required when the data source is registered in instance mode.  
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string. This is required when the data source is registered using a connection string.   
        # `catalog_id`: The DLF catalog ID.   
        # `project_name`: The MaxCompute project name.   
        # `database_name`: The database name.   
        # `schema_name`: The schema name. For MaxCompute, this is required only when the three-layer model is enabled for the project. Use an empty string as a placeholder if the three-layer model is not enabled.   
        # `table_name`: The table name.
        # 
        # This parameter is required.
        self.id = id
        # Specifies whether to include business metadata. Default value: false.
        self.include_business_metadata = include_business_metadata
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

