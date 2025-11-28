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
        # For more information about the value range, see Document [https://www.postgresql.org/docs/current/multibyte.html](url).
        # 
        # Default value: UTF-8.
        self.character_set_name = character_set_name
        # Database locale parameter (specifies string comparison/sorting rules).
        # 
        # > 
        # 
        # *   The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # 
        # *   Valid values for the Collate field: You can execute the SELECT DISTINCT collname FROM pg_collation; statement to obtain the field value. The default value is en_US.utf8.
        self.collate = collate
        # Database locale parameter (defines character classification/case conversion rules).
        # 
        # > 
        # 
        # *   The locale must be compatible with the character set specified by the CharacterSetName parameter.
        # 
        # *   You can execute the SELECT DISTINCT collctype FROM pg_collation; statement to obtain the field value. The default value is en_US.utf8.
        self.ctype = ctype
        # The cluster ID.
        # 
        # > You can call the [DescribeDBInstances](https://help.aliyun.com/document_detail/86911.html) operation to query the information about all AnalyticDB for PostgreSQL instances within a region, including instance IDs.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The name of the database.
        # 
        # *   Only contains letters, digits, and underscores (_).
        # *   Must start with a letter.
        # *   Up to 63 characters in length.
        # 
        # This parameter is required.
        self.database_name = database_name
        # The description of the database.
        # 
        # *   Must start with a letter.
        # *   Cannot start with http:// or https://.
        # *   Only contains letters, underscores (_), hyphens (-), and digits.
        # *   Must be 2 to 256 characters in length.
        self.description = description
        # The owner of the table.
        # 
        # *   Only contains lowercase letters, digits, and underscores (_).
        # *   Must start with a lowercase letter and end with a lowercase letter or a digit.
        # *   Cannot start with gp.
        # *   Must be 2 to 16 characters in length.
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

