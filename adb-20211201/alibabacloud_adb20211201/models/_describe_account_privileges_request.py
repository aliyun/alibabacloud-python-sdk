# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAccountPrivilegesRequest(DaraModel):
    def __init__(
        self,
        account_name: str = None,
        column_privilege_object: str = None,
        dbcluster_id: str = None,
        database_privilege_object: str = None,
        page_number: str = None,
        page_size: str = None,
        privilege_type: str = None,
        region_id: str = None,
        table_privilege_object: str = None,
    ):
        # The name of the database account whose privileges you want to query.
        # 
        # This parameter is required.
        self.account_name = account_name
        # Filters the results by column name. This parameter is used only when `PrivilegeType` is set to `Column`.
        self.column_privilege_object = column_privilege_object
        # <props="china">The ID of the Enterprise Edition, Basic Edition, or Lakehouse Edition cluster.
        # <props="intl">The ID of the Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # Filters the results by database name. This parameter is used only when `PrivilegeType` is set to `Database`, `Table`, or `Column`.
        self.database_privilege_object = database_privilege_object
        # The page number. Pages start at 1. Default value: 1.
        self.page_number = page_number
        # The number of entries per page. Default value: 20.
        self.page_size = page_size
        # The privilege level to query. To obtain the valid values for this parameter, call the `DescribeEnabledPrivileges` operation.
        self.privilege_type = privilege_type
        # The region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        # Filters the results by table name. You can use this parameter with `DatabasePrivilegeObject` to refine the search. This parameter is used only when `PrivilegeType` is set to `Table` or `Column`.
        self.table_privilege_object = table_privilege_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.column_privilege_object is not None:
            result['ColumnPrivilegeObject'] = self.column_privilege_object

        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.database_privilege_object is not None:
            result['DatabasePrivilegeObject'] = self.database_privilege_object

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.privilege_type is not None:
            result['PrivilegeType'] = self.privilege_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.table_privilege_object is not None:
            result['TablePrivilegeObject'] = self.table_privilege_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('ColumnPrivilegeObject') is not None:
            self.column_privilege_object = m.get('ColumnPrivilegeObject')

        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DatabasePrivilegeObject') is not None:
            self.database_privilege_object = m.get('DatabasePrivilegeObject')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PrivilegeType') is not None:
            self.privilege_type = m.get('PrivilegeType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TablePrivilegeObject') is not None:
            self.table_privilege_object = m.get('TablePrivilegeObject')

        return self

