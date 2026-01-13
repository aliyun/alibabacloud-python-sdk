# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        access_privilege: str = None,
        character_set_name: str = None,
        collate: str = None,
        conn_limit: str = None,
        ctype: str = None,
        dbinstance_id: str = None,
        database_name: str = None,
        description: str = None,
        owner: str = None,
        request_id: str = None,
        size: str = None,
        table_space: str = None,
    ):
        # The permission control information.
        self.access_privilege = access_privilege
        # The character set.
        # 
        # For more information about the value range, see Document https://www.postgresql.org/docs/current/multibyte.html.
        self.character_set_name = character_set_name
        # Database locale parameter that specifies string comparison and sorting rules.
        # 
        # > 
        # 
        # *   The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # 
        # *   Collate: You can query available collations using the command SELECT DISTINCT collname FROM pg_collation;. If not specified, the default value is en_US.utf8.
        self.collate = collate
        # Limits the number of concurrent connections. -1 indicates unlimited.
        self.conn_limit = conn_limit
        # Database locale parameter that specifies character classification and case conversion rules.
        # 
        # > 
        # 
        # *   The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # 
        # *   You can execute the SELECT DISTINCT collctype FROM pg_collation; statement to obtain the field value. The default value is en_US.utf8.
        self.ctype = ctype
        # The cluster ID.
        self.dbinstance_id = dbinstance_id
        # The database name.
        # 
        # *   Only contain letters, digits, and underscores (_).
        # *   Must start with a letter.
        # *   Up to 63 characters in length.
        self.database_name = database_name
        # The database comment.
        self.description = description
        # The owner of the table.
        # 
        # *   Contain lowercase letters, digits, and underscores (_).
        # *   Must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   Cannot start with gp.
        # *   Must be 2 to 16 characters in length.
        self.owner = owner
        # The unique ID of the request.
        self.request_id = request_id
        # The database size.
        self.size = size
        # The database tablespace.
        self.table_space = table_space

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_privilege is not None:
            result['AccessPrivilege'] = self.access_privilege

        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.collate is not None:
            result['Collate'] = self.collate

        if self.conn_limit is not None:
            result['ConnLimit'] = self.conn_limit

        if self.ctype is not None:
            result['Ctype'] = self.ctype

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.database_name is not None:
            result['DatabaseName'] = self.database_name

        if self.description is not None:
            result['Description'] = self.description

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.size is not None:
            result['Size'] = self.size

        if self.table_space is not None:
            result['TableSpace'] = self.table_space

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPrivilege') is not None:
            self.access_privilege = m.get('AccessPrivilege')

        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('Collate') is not None:
            self.collate = m.get('Collate')

        if m.get('ConnLimit') is not None:
            self.conn_limit = m.get('ConnLimit')

        if m.get('Ctype') is not None:
            self.ctype = m.get('Ctype')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DatabaseName') is not None:
            self.database_name = m.get('DatabaseName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TableSpace') is not None:
            self.table_space = m.get('TableSpace')

        return self

