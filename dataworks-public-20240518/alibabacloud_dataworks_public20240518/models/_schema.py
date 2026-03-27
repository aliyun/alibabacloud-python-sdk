# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Schema(DaraModel):
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
        # The schema ID. For more information, see [Concepts related to metadata entities.](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${Instance ID or escaped URL}:${Catalog name}:${Database name}`. Use empty strings as placeholders for levels that do not exist.
        # 
        # >  For the MaxCompute type, the instance ID level is represented by an empty string. The database name is the name of the MaxCompute project, which has enabled the schema feature.
        # 
        # Examples of common ID formats
        # 
        # `maxcompute-project:::project_name` (For MaxCompute projects schema enabled)
        # 
        # `holo-schema:instance_id::database_name:schema_name`
        # 
        # > \\
        # `instance_id`: The Hologres instance ID\\
        # . `database_name`: The database name\\
        # . `project_name`: The MaxCompute project name\\
        # . `schema_name`: The schema name.
        self.id = id
        # The modification time. The value is a UNIX timestamp. Unit: milliseconds.
        self.modify_time = modify_time
        # The name.
        self.name = name
        # The parent entity ID. For more information, see [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format: `${EntityType}:${Instance ID or escaped URL}:${Catalog name}:${Database name}`. Use empty strings as placeholders for levels that do not exist.
        # 
        # >  For the MaxCompute type, the instance ID level is represented by an empty string. The database name is the name of the MaxCompute project with schema enabled.
        # 
        # Examples of common ParentMetaEntityId formats
        # 
        # `maxcompute-project:::project_name` (For MaxCompute projects with schema enabled)
        # 
        # `holo-database:instance_id::database_name`
        # 
        # > \\
        # `instance_id`: The Hologres instance ID\\
        # . `database_name`: The database name\\
        # . `project_name`: The MaxCompute project name.
        self.parent_meta_entity_id = parent_meta_entity_id
        # The type.
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

