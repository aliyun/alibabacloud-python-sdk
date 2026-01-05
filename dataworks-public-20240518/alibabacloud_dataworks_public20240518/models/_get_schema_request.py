# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSchemaRequest(DaraModel):
    def __init__(
        self,
        id: str = None,
    ):
        # The ID. You can refer to the ListSchemas operation and [Concepts related to metadata entities](https://help.aliyun.com/document_detail/2880092.html).
        # 
        # The format is `${EntityType}:${Instance ID or escaped URL}:${Catalog ID}:${Database name}:${Schema name}</code>`. Use empty strings as placeholders for missing levels.
        # 
        # >  For the MaxCompute type, use an empty string as the placeholder for the instance ID level. The database name is the MaxCompute project name, and the project must have the three-level model enabled.
        # 
        # Examples:
        # 
        # `maxcompute-schema:::project_name:schema_name` (The three-level model is enabled for the MaxCompute project.)
        # 
        # `holo-schema:instance_id::database_name:schema_name`
        # 
        # > \\
        # `instance_id`: The Hologres instance ID\\
        # . `database_name`: The database name\\
        # . `database_name`: The MaxCompute project name\\
        # . `schema_name`: The schema name.
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

