# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Database(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        id: str = None,
        location_uri: str = None,
        modify_time: int = None,
        name: str = None,
        parent_meta_entity_id: str = None,
    ):
        # The comments.
        self.comment = comment
        # The creation time. This value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The database ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The common format of this parameter is `${Entity type}:${Instance ID or escaped URL}:${Catalog identifier}:${Database name}`. If a level does not exist, specify an empty string as a placeholder.
        # 
        # >  For StarRocks data sources, specify a catalog name at the Catalog identifier level. For DLF data sources, specify a catalog ID at the Catalog identifier level. Other types of data sources do not support the Catalog identifier level. You can specify an empty string as a placeholder.
        # 
        # You can configure this parameter in one of the following formats based on your data source type:
        # 
        # `dlf-database::catalog_id:database_name`
        # 
        # `holo-database:instance_id::database_name`
        # 
        # `mysql-database:(instance_id|encoded_jdbc_url)::database_name`
        # 
        # > \\
        # `catalog_id`: the ID of a DLF catalog.\\
        # `instance_id`: the ID of an instance. If the related data source is added to DataWorks in Alibaba Cloud instance mode, you must configure this parameter.\\
        # `encoded_jdbc_url`: the JDBC connection string that is URL-encoded. If the related data source is added to DataWorks in connection string mode, you must configure this parameter.\\
        # `database_name`: the name of a database.
        self.id = id
        # The uniform resource identifier (URI) of the storage location.
        self.location_uri = location_uri
        # The update time. This value is a UNIX timestamp. Unit: milliseconds.
        self.modify_time = modify_time
        # The database name.
        self.name = name
        # The parent entity ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # You can call the ListCrawlerTypes operation to query the parent entity types.
        # 
        # *   If the parent entity is a catalog, you can configure the `ParentMetaEntityId` parameter by referring to the `Catalog` topic.
        # *   If the parent entity is a metadata crawler, you can configure the `ParentMetaEntityId` parameter in the `${Crawler type}:${Instance ID or escaped URL}` format.
        # 
        # You can configure the ParentMetaEntityId parameter in one of the following formats based on your data source type:
        # 
        # `dlf-catalog::catalog_id`
        # 
        # `holo:instance_id`
        # 
        # `mysql:(instance_id|encoded_jdbc_url)`
        # 
        # > \\
        # `catalog_id`: the ID of a DLF catalog.\\
        # `instance_id`: the ID of an instance. If the related data source is added to DataWorks in Alibaba Cloud instance mode, you must configure this parameter.\\
        # `encoded_jdbc_url`: the JDBC connection string that is URL-encoded. If the related data source is added to DataWorks in connection string mode, you must configure this parameter.
        self.parent_meta_entity_id = parent_meta_entity_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.id is not None:
            result['Id'] = self.id

        if self.location_uri is not None:
            result['LocationUri'] = self.location_uri

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LocationUri') is not None:
            self.location_uri = m.get('LocationUri')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        return self

