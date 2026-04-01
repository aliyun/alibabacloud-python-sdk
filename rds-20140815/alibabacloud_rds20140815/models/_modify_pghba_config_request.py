# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class ModifyPGHbaConfigRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dbinstance_id: str = None,
        hba_item: List[main_models.ModifyPGHbaConfigRequestHbaItem] = None,
        ops_type: str = None,
        owner_account: str = None,
        owner_id: int = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # A reserved parameter. You do not need to specify this parameter.
        self.client_token = client_token
        # The instance ID. You can call the DescribeDBInstances operation to query the instance ID.
        # 
        # This parameter is required.
        self.dbinstance_id = dbinstance_id
        # An array that consists of the details of the AD domain services.
        # 
        # This parameter is required.
        self.hba_item = hba_item
        # The method that you use to modify the pg_hba.conf file. Valid values:
        # 
        # *   **add**: adds one or more records. If you use this method, make sure that the value of the PriorityId parameter for each new record is different from the value of the PriorityId parameter for any existing record.
        # *   **delete**: deletes one or more records. If you use this method, the record that corresponds to the specified value of the **PriorityId** parameter is deleted from the pg_hba.conf file.
        # *   **modify**: modifies one or more records. If you use this method, the record that corresponds to the specified value of the **PriorityId** parameter is modified.
        # *   **update**: overwrites the existing configuration in the pg_hba.conf file by using the new configuration.
        # 
        # This parameter is required.
        self.ops_type = ops_type
        self.owner_account = owner_account
        self.owner_id = owner_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        if self.hba_item:
            for v1 in self.hba_item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dbinstance_id is not None:
            result['DBInstanceId'] = self.dbinstance_id

        result['HbaItem'] = []
        if self.hba_item is not None:
            for k1 in self.hba_item:
                result['HbaItem'].append(k1.to_map() if k1 else None)

        if self.ops_type is not None:
            result['OpsType'] = self.ops_type

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DBInstanceId') is not None:
            self.dbinstance_id = m.get('DBInstanceId')

        self.hba_item = []
        if m.get('HbaItem') is not None:
            for k1 in m.get('HbaItem'):
                temp_model = main_models.ModifyPGHbaConfigRequestHbaItem()
                self.hba_item.append(temp_model.from_map(k1))

        if m.get('OpsType') is not None:
            self.ops_type = m.get('OpsType')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

class ModifyPGHbaConfigRequestHbaItem(DaraModel):
    def __init__(
        self,
        address: str = None,
        database: str = None,
        mask: str = None,
        method: str = None,
        option: str = None,
        priority_id: int = None,
        type: str = None,
        user: str = None,
    ):
        # The IP addresses from which the specified users can access the specified databases. If you set this parameter to 0.0.0.0/0, the specified users are allowed to access the specified databases from all IP addresses.
        # 
        # This parameter is required.
        self.address = address
        # The name of the database. If you set this parameter to all, the specified users are allowed to access all databases on the instance.
        # 
        # If you specify multiple entries, separate the entries with commas (,).
        # 
        # This parameter is required.
        self.database = database
        # The mask of the IP address. If the value of the **Address** parameter is an IP address, you can use this parameter to specify the mask of the IP address.
        self.mask = mask
        # The authentication method. Valid values:
        # 
        # *   **trust**
        # *   **reject**
        # *   **scram-sha-256**
        # *   **md5**
        # *   **password**
        # *   **gss**
        # *   **sspi**
        # *   **ldap**
        # *   **radius**
        # *   **cert**
        # *   **pam**
        # 
        # This parameter is required.
        self.method = method
        # The options of the authentication method. In this topic, LDAP is used as an example. You must configure this parameter. For more information, see [Authentication Methods](https://www.postgresql.org/docs/11/auth-methods.html).
        self.option = option
        # The priority of the record. If you set this parameter to 0, the record has the highest priority. Valid values: 0 to 10000.
        # 
        # This parameter is used to identify each record. When you add a record, the value of the PriorityId parameter for the new record must be different from the value of the PriorityId parameter of any existing record. When you modify or delete a record, you must also modify or delete the value of the PriorityId parameter for this record.
        # 
        # This parameter is required.
        self.priority_id = priority_id
        # The connection type.
        # 
        # Valid values:
        # 
        # *   **host**: The record matches TCP/IP connections, including SSL connections and non-SSL connections.
        # *   **hostssl**: The record matches only TCP/IP connections that are established over SSL.
        # *   **hostnossl**: The record matches only TCP/IP connections that are not established over SSL connections.
        # 
        # >  You can set this parameter to hostssl only when SSL encryption is enabled for the instance. For more information, see Configure SSL encryption for an ApsaraDB RDS for PostgreSQL instance.[](~~229518~~)
        # 
        # This parameter is required.
        self.type = type
        # The user who is allowed to access the specified databases. You must specify the user that is used to log on to the RDS instance. If you specify multiple entries, separate the entries with commas (,).
        # 
        # This parameter is required.
        self.user = user

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.address is not None:
            result['Address'] = self.address

        if self.database is not None:
            result['Database'] = self.database

        if self.mask is not None:
            result['Mask'] = self.mask

        if self.method is not None:
            result['Method'] = self.method

        if self.option is not None:
            result['Option'] = self.option

        if self.priority_id is not None:
            result['PriorityId'] = self.priority_id

        if self.type is not None:
            result['Type'] = self.type

        if self.user is not None:
            result['User'] = self.user

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Address') is not None:
            self.address = m.get('Address')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Mask') is not None:
            self.mask = m.get('Mask')

        if m.get('Method') is not None:
            self.method = m.get('Method')

        if m.get('Option') is not None:
            self.option = m.get('Option')

        if m.get('PriorityId') is not None:
            self.priority_id = m.get('PriorityId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('User') is not None:
            self.user = m.get('User')

        return self

