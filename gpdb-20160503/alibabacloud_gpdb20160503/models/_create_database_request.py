# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseRequest(DaraModel):
    def __init__(
        self,
        character_set_name: str = None,
        collate: str = None,
        ctype: str = None,
        dbinstance_id: str = None,
        database_name: str = None,
        description: str = None,
        owner: str = None,
    ):
        # The character set.
        # 
        # For valid values, see References [https://www.postgresql.org/docs/current/multibyte.html](url).
        # 
        # Default value: UTF8.
        self.character_set_name = character_set_name
        # The collation parameter of the database, which specifies the string comparison and sorting rules.
        # >
        # > - The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # > - Valid values for Collate: You can run the `SELECT DISTINCT collname FROM pg_collation;` command to query the valid values. If this parameter is not specified, the default value is en_US.utf8.
        self.collate = collate
        # The character type parameter of the database, which specifies the character classification and case conversion rules.
        # > 
        # > - The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # > - You can run the `SELECT DISTINCT collctype FROM pg_collation;` command to query the valid values. If this parameter is not specified, the default value is en_US.utf8.
        self.ctype = ctype
        # The instance ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the details of all AnalyticDB for PostgreSQL instances in a specific region, including the instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database. The name must meet the following requirements:
        # - It can contain only letters, digits, and underscores (_).
        # - It must start with a letter.
        # - It can be up to 63 characters in length.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The description of the database.
        # 
        # - It must start with a Chinese character or a letter.
        # 
        # - It cannot start with http:// or https://.
        # 
        # - It can contain Chinese characters, letters, underscores (_), hyphens (-), and digits.
        # 
        # - It must be 2 to 256 characters in length.
        self.description = description
        # The owner of the table.
        # 
        # - It can contain only lowercase letters, digits, and underscores (_).
        # 
        # - It must start with a lowercase letter and end with a lowercase letter or a digit.
        # 
        # - It cannot start with gp.
        # 
        # - It must be 2 to 16 characters in length.
        # 
        # This parameter is required.
        self.owner = owner

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.collate is not None:
            result['Collate'] = self.collate

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('Collate') is not None:
            self.collate = m.get('Collate')

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

        return self

