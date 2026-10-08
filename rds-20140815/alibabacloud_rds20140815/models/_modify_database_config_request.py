# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDatabaseConfigRequest(DaraModel):
    def __init__(
        self,
        dbinstance_id: str = None,
        dbname: str = None,
        database_property_name: str = None,
        database_property_value: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # The database name.
        # 
        # > Specifying multiple database names is not supported.
        # 
        # This parameter is required.
        self.dbname = dbname
        # The database attribute that you want to modify.
        # 
        # - **Modify database attributes feature**: Enter the attribute name of the target database.
        # - **Data archiving to OSS feature**: Enter the status of the target database. Set this parameter to `covert_online_db_to_cold_storage` to convert an online database to a cold storage database, or set this parameter to `convert_cold_storage_db_to_online` to convert a cold storage database to an online database.
        # 
        # This parameter is required.
        self.database_property_name = database_property_name
        # The value of the database attribute that you want to modify.
        # - **Modify database attributes feature**: Enter the attribute value of the target database.
        # - **Data archiving to OSS feature**: Set this parameter to **1** to convert the target database to cold storage or online status.
        # 
        # This parameter is required.
        self.database_property_value = database_property_value
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
        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        if self.dbname is not None:
            result['DBName'] = self.dbname

        if self.database_property_name is not None:
            result['DatabasePropertyName'] = self.database_property_name

        if self.database_property_value is not None:
            result['DatabasePropertyValue'] = self.database_property_value

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
        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        if m.get('DBName') is not None:
            self.dbname = m.get('DBName')

        if m.get('DatabasePropertyName') is not None:
            self.database_property_name = m.get('DatabasePropertyName')

        if m.get('DatabasePropertyValue') is not None:
            self.database_property_value = m.get('DatabasePropertyValue')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

