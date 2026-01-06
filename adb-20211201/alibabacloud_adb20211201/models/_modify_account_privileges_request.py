# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class ModifyAccountPrivilegesRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        account_privileges: List[main_models.ModifyAccountPrivilegesRequestAccountPrivileges] = None,
        dbcluster_id: str = None,
        region_id: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The permissions that you want to grant to the database account.
        # 
        # This parameter is required.
        self.account_privileges = account_privileges
        # The ID of the AnalyticDB for MySQL Data Lakehouse Edition (V3.0) cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        if self.account_privileges:
            for v1 in self.account_privileges:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        result['AccountPrivileges'] = []
        if self.account_privileges is not None:
            for k1 in self.account_privileges:
                result['AccountPrivileges'].append(k1.to_map() if k1 else None)

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        self.account_privileges = []
        if m.get('AccountPrivileges') is not None:
            for k1 in m.get('AccountPrivileges'):
                temp_model = main_models.ModifyAccountPrivilegesRequestAccountPrivileges()
                self.account_privileges.append(temp_model.from_map(k1))

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

class ModifyAccountPrivilegesRequestAccountPrivileges(DaraModel):
    def __init__(
        self,
        privilege_object: main_models.ModifyAccountPrivilegesRequestAccountPrivilegesPrivilegeObject = None,
        privilege_type: str = None,
        privileges: List[str] = None,
    ):
        # The objects on which you want to grant permissions, including databases, tables, and columns.
        self.privilege_object = privilege_object
        # The permission level that you want to assign to the database account. You can call the `DescribeEnabledPrivileges` operation to query the permission level that can be assigned to the database account.
        self.privilege_type = privilege_type
        # The permissions that you want to grant to the database account.
        self.privileges = privileges

    def validate(self):
        if self.privilege_object:
            self.privilege_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.privilege_object is not None:
            result['PrivilegeObject'] = self.privilege_object.to_map()

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.privileges is not None:
            result['Privileges'] = self.privileges

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PrivilegeObject') is not None:
            temp_model = main_models.ModifyAccountPrivilegesRequestAccountPrivilegesPrivilegeObject()
            self.privilege_object = temp_model.from_map(m.get('PrivilegeObject'))

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('Privileges') is not None:
            self.privileges = m.get('Privileges')

        return self

class ModifyAccountPrivilegesRequestAccountPrivilegesPrivilegeObject(DaraModel):
    def __init__(
        self,
        column: str = None,
        database: str = None,
        table: str = None,
    ):
        # The columns on which you want to grant permissions. This parameter must be specified when the PrivilegeType parameter is set to Column.
        self.column = column
        # The databases on which you want to grant permissions. This parameter must be specified when the PrivilegeType parameter is set to Database, Table, or Column.
        self.database = database
        # The tables on which you want to grant permissions. This parameter must be specified when the PrivilegeType parameter is set to Table or Column.
        self.table = table

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column is not None:
            result['Column'] = self.column

        if self.database is not None:
            result['Database'] = self.database

        if self.table is not None:
            result['Table'] = self.table

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Column') is not None:
            self.column = m.get('Column')

        if m.get('Database') is not None:
            self.database = m.get('Database')

        if m.get('Table') is not None:
            self.table = m.get('Table')

        return self

