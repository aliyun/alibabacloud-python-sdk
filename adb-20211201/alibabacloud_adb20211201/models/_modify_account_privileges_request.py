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
        promql_insert_privileges: List[str] = None,
        promql_select_node_percentage: float = None,
        promql_select_privileges: List[str] = None,
        region_id: str = None,
        resource_group_name: str = None,
    ):
        # The name of the database account.
        # 
        # This parameter is required.
        self.account_name = account_name
        # The list of granted permissions.
        self.account_privileges = account_privileges
        # <props="china">The cluster ID of the Enterprise Edition, Basic Edition, or Data Lakehouse Edition cluster.
        # <props="intl">The cluster ID of the Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        self.promql_insert_privileges = promql_insert_privileges
        self.promql_select_node_percentage = promql_select_node_percentage
        self.promql_select_privileges = promql_select_privileges
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_group_name = resource_group_name

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

        if self.promql_insert_privileges is not None:
            result['PromqlInsertPrivileges'] = self.promql_insert_privileges

        if self.promql_select_node_percentage is not None:
            result['PromqlSelectNodePercentage'] = self.promql_select_node_percentage

        if self.promql_select_privileges is not None:
            result['PromqlSelectPrivileges'] = self.promql_select_privileges

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_name is not None:
            result['ResourceGroupName'] = self.resource_group_name

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

        if m.get('PromqlInsertPrivileges') is not None:
            self.promql_insert_privileges = m.get('PromqlInsertPrivileges')

        if m.get('PromqlSelectNodePercentage') is not None:
            self.promql_select_node_percentage = m.get('PromqlSelectNodePercentage')

        if m.get('PromqlSelectPrivileges') is not None:
            self.promql_select_privileges = m.get('PromqlSelectPrivileges')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupName') is not None:
            self.resource_group_name = m.get('ResourceGroupName')

        return self

class ModifyAccountPrivilegesRequestAccountPrivileges(DaraModel):
    def __init__(
        self,
        privilege_object: main_models.ModifyAccountPrivilegesRequestAccountPrivilegesPrivilegeObject = None,
        privilege_type: str = None,
        privileges: List[str] = None,
    ):
        # The privilege object, which is a tuple of database, table, and column.
        self.privilege_object = privilege_object
        # The privilege level, obtained from the `DescribeEnabledPrivileges` operation.
        self.privilege_type = privilege_type
        # The list of granted permissions.
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
        # The column to which permissions are granted. This parameter is required when the privilege level is column.
        self.column = column
        # The database to which permissions are granted. This parameter is required when the privilege level is database, table, or column.
        self.database = database
        # The table to which permissions are granted. This parameter is required when the privilege level is table or column.
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

