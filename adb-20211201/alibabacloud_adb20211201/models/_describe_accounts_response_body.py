# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_adb20211201 import models as main_models
from darabonba.model import DaraModel

class DescribeAccountsResponseBody(DaraModel):
    def __init__(
        self,
        account_list: main_models.DescribeAccountsResponseBodyAccountList = None,
        request_id: str = None,
    ):
        self.account_list = account_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.account_list:
            self.account_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_list is not None:
            result['AccountList'] = self.account_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountList') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountList()
            self.account_list = temp_model.from_map(m.get('AccountList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAccountsResponseBodyAccountList(DaraModel):
    def __init__(
        self,
        dbaccount: List[main_models.DescribeAccountsResponseBodyAccountListDBAccount] = None,
    ):
        self.dbaccount = dbaccount

    def validate(self):
        if self.dbaccount:
            for v1 in self.dbaccount:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DBAccount'] = []
        if self.dbaccount is not None:
            for k1 in self.dbaccount:
                result['DBAccount'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dbaccount = []
        if m.get('DBAccount') is not None:
            for k1 in m.get('DBAccount'):
                temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccount()
                self.dbaccount.append(temp_model.from_map(k1))

        return self

class DescribeAccountsResponseBodyAccountListDBAccount(DaraModel):
    def __init__(
        self,
        account_description: str = None,
        account_name: str = None,
        account_status: str = None,
        account_type: str = None,
        engine: str = None,
        promql_insert_privileges: main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlInsertPrivileges = None,
        promql_select_nodes: main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectNodes = None,
        promql_select_privileges: main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectPrivileges = None,
        ram_user_list: main_models.DescribeAccountsResponseBodyAccountListDBAccountRamUserList = None,
        ram_users: str = None,
        promql_select_node_percentage: float = None,
    ):
        self.account_description = account_description
        self.account_name = account_name
        self.account_status = account_status
        self.account_type = account_type
        self.engine = engine
        self.promql_insert_privileges = promql_insert_privileges
        self.promql_select_nodes = promql_select_nodes
        self.promql_select_privileges = promql_select_privileges
        self.ram_user_list = ram_user_list
        self.ram_users = ram_users
        self.promql_select_node_percentage = promql_select_node_percentage

    def validate(self):
        if self.promql_insert_privileges:
            self.promql_insert_privileges.validate()
        if self.promql_select_nodes:
            self.promql_select_nodes.validate()
        if self.promql_select_privileges:
            self.promql_select_privileges.validate()
        if self.ram_user_list:
            self.ram_user_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_description is not None:
            result['AccountDescription'] = self.account_description

        if self.account_name is not None:
            result['AccountName'] = self.account_name

        if self.account_status is not None:
            result['AccountStatus'] = self.account_status

        if self.account_type is not None:
            result['AccountType'] = self.account_type

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.promql_insert_privileges is not None:
            result['PromqlInsertPrivileges'] = self.promql_insert_privileges.to_map()

        if self.promql_select_nodes is not None:
            result['PromqlSelectNodes'] = self.promql_select_nodes.to_map()

        if self.promql_select_privileges is not None:
            result['PromqlSelectPrivileges'] = self.promql_select_privileges.to_map()

        if self.ram_user_list is not None:
            result['RamUserList'] = self.ram_user_list.to_map()

        if self.ram_users is not None:
            result['RamUsers'] = self.ram_users

        if self.promql_select_node_percentage is not None:
            result['promqlSelectNodePercentage'] = self.promql_select_node_percentage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountDescription') is not None:
            self.account_description = m.get('AccountDescription')

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

        if m.get('AccountStatus') is not None:
            self.account_status = m.get('AccountStatus')

        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('PromqlInsertPrivileges') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlInsertPrivileges()
            self.promql_insert_privileges = temp_model.from_map(m.get('PromqlInsertPrivileges'))

        if m.get('PromqlSelectNodes') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectNodes()
            self.promql_select_nodes = temp_model.from_map(m.get('PromqlSelectNodes'))

        if m.get('PromqlSelectPrivileges') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectPrivileges()
            self.promql_select_privileges = temp_model.from_map(m.get('PromqlSelectPrivileges'))

        if m.get('RamUserList') is not None:
            temp_model = main_models.DescribeAccountsResponseBodyAccountListDBAccountRamUserList()
            self.ram_user_list = temp_model.from_map(m.get('RamUserList'))

        if m.get('RamUsers') is not None:
            self.ram_users = m.get('RamUsers')

        if m.get('promqlSelectNodePercentage') is not None:
            self.promql_select_node_percentage = m.get('promqlSelectNodePercentage')

        return self

class DescribeAccountsResponseBodyAccountListDBAccountRamUserList(DaraModel):
    def __init__(
        self,
        ram_user_list: List[str] = None,
    ):
        self.ram_user_list = ram_user_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ram_user_list is not None:
            result['RamUserList'] = self.ram_user_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RamUserList') is not None:
            self.ram_user_list = m.get('RamUserList')

        return self

class DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectPrivileges(DaraModel):
    def __init__(
        self,
        promql_select_privileges: List[str] = None,
    ):
        self.promql_select_privileges = promql_select_privileges

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promql_select_privileges is not None:
            result['PromqlSelectPrivileges'] = self.promql_select_privileges

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromqlSelectPrivileges') is not None:
            self.promql_select_privileges = m.get('PromqlSelectPrivileges')

        return self

class DescribeAccountsResponseBodyAccountListDBAccountPromqlSelectNodes(DaraModel):
    def __init__(
        self,
        promql_select_nodes: List[str] = None,
    ):
        self.promql_select_nodes = promql_select_nodes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promql_select_nodes is not None:
            result['PromqlSelectNodes'] = self.promql_select_nodes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromqlSelectNodes') is not None:
            self.promql_select_nodes = m.get('PromqlSelectNodes')

        return self

class DescribeAccountsResponseBodyAccountListDBAccountPromqlInsertPrivileges(DaraModel):
    def __init__(
        self,
        promql_insert_privileges: List[str] = None,
    ):
        self.promql_insert_privileges = promql_insert_privileges

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.promql_insert_privileges is not None:
            result['PromqlInsertPrivileges'] = self.promql_insert_privileges

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PromqlInsertPrivileges') is not None:
            self.promql_insert_privileges = m.get('PromqlInsertPrivileges')

        return self

