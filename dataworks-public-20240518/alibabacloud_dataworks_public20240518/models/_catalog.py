# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Catalog(DaraModel):
    def __init__(
        self,
        comment: str = None,
        create_time: int = None,
        id: str = None,
        modify_time: int = None,
        name: str = None,
        parent_meta_entity_id: str = None,
        type: str = None,
    ):
        # The comment.
        self.comment = comment
        # The creation time. The value is a UNIX timestamp. Unit: milliseconds.
        self.create_time = create_time
        # The catalog ID. Currently, only the DLF and StarRocks types are supported. For details, see [description of concepts related to metadata entities.](https://help.aliyun.com/document_detail/2880092.html)
        # 
        # *   For the DLF type, the format is `dlf-catalog::catalog_id`.
        # *   For the starrocks type, the format is `starrocks-catalog:(instance_id|encoded_jdbc_url):catalog_name`.
        # 
        # > \\
        # `catalog_id`: The the DLF catalog ID.\\
        # `instance_id`: The instance ID, required if the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, required if the data source is registered using a connection string.\\
        # `catalog_name`: The StarRocks catalog name.
        self.id = id
        # The modification time. The value is a UNIX timestamp. Unit: milliseconds.
        self.modify_time = modify_time
        # The catalog name.
        self.name = name
        # The parent entity ID.
        # 
        # *   For the DLF type, the format of `ParentMetaEntityId` is `dlf`.
        # *   For the StarRocks type, the format of `ParentMetaEntityId` is `starrocks:(instance_id|encoded_jdbc_url)`.
        # 
        # > \\
        # `instance_id`: The instance ID, required when the data source is registered in instance mode.\\
        # `encoded_jdbc_url`: The URL-encoded JDBC connection string, required if the data source is registered via a connection string.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The catalog type. The value of this parameter varies based on the type of the metadata crawler.
        self.type = type

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

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.parent_meta_entity_id is not None:
            result['ParentMetaEntityId'] = self.parent_meta_entity_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ParentMetaEntityId') is not None:
            self.parent_meta_entity_id = m.get('ParentMetaEntityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

