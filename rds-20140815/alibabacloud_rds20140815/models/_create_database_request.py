# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateDatabaseRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privilege: str = None,
        character_set_name: str = None,
        collation_name: str = None,
        dbdescription: str = None,
        dbinstance_id: str = None,
        dbname: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        self.account_name = account_name
        self.account_privilege = account_privilege
        # The character set. Valid values:
        # * MySQL/MariaDB: **utf8, gbk, latin1, utf8mb4**
        # * SQL Server: **Chinese_PRC_CI_AS, Chinese_PRC_CS_AS, SQL_Latin1_General_CP1_CI_AS, SQL_Latin1_General_CP1_CS_AS, Chinese_PRC_BIN**
        # * PostgreSQL: You must specify the character set, Collate, and Ctype in the format of `Character set,<Collate>,<Ctype>`. Example: `UTF8,C,en_US.utf8`.
        #     - Valid values for the character set: **KOI8U, UTF8, WIN866, WIN874, WIN1250, WIN1251, WIN1252, WIN1253, WIN1254, WIN1255, WIN1256, WIN1257, WIN1258, EUC_CN, EUC_KR, EUC_TW, EUC_JP, EUC_JIS_2004, KOI8R, MULE_INTERNAL, LATIN1, LATIN2, LATIN3, LATIN4, LATIN5, LATIN6, LATIN7, LATIN8, LATIN9, LATIN10, ISO_8859_5, ISO_8859_6, ISO_8859_7, ISO_8859_8, SQL_ASCII**.
        #     - Valid values for **Collate**: You can run the `SELECT DISTINCT collname FROM pg_collation;` command to query the valid values. If this parameter is not specified, the default value **C** is used.
        #     - Valid values for **Ctype**: You can run the `SELECT DISTINCT collctype FROM pg_collation;` command to query the valid values. If this parameter is not specified, the default value **en_US.utf8** is used.
        # 
        # This parameter is required.
        self.character_set_name = character_set_name
        # The collation. This parameter is supported only for ApsaraDB RDS for MySQL instances. Specify a collation that matches the character set. For example, if the character set is utf8mb4, the collation must be utf8mb4_bin or utf8mb4_general_ci.
        self.collation_name = collation_name
        # The database description. The description must be 2 to 256 characters in length and can contain letters, digits, Chinese characters, underscores (_), and hyphens (-). The description must start with a Chinese character or a letter.
        # >The description cannot start with `http://` or `https://`.
        self.dbdescription = dbdescription
        # The instance ID. You can call DescribeDBInstances to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        # 
        # > * The name must be 2 to 64 characters in length.
        # > * The name must start with a letter and end with a letter or digit.
        # > * The name can contain lowercase letters, digits, underscores (_), and hyphens (-).
        # > * The database name must be unique within the instance.
        # > * For more information about invalid characters, see [Reserved words](https://help.aliyun.com/document_detail/26317.html).
        # 
        # This parameter is required.
        self.dbname = dbname
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_privilege is not None:
            result['AccountPrivilege'] = self.account_privilege

        if self.character_set_name is not None:
            result['CharacterSetName'] = self.character_set_name

        if self.collation_name is not None:
            result['CollationName'] = self.collation_name

        if self.dbdescription is not None:
            result['DBDescription'] = self.dbdescription

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountPrivilege') is not None:
            self.account_privilege = m.get('AccountPrivilege')

        if m.get('CharacterSetName') is not None:
            self.character_set_name = m.get('CharacterSetName')

        if m.get('CollationName') is not None:
            self.collation_name = m.get('CollationName')

        if m.get('DBDescription') is not None:
            self.dbdescription = m.get('DBDescription')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

