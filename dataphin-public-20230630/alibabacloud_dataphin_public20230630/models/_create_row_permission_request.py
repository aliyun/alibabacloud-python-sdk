# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class CreateRowPermissionRequest(DaraModel):
    def __init__(
        self,
        create_row_permission_command: main_models.CreateRowPermissionRequestCreateRowPermissionCommand = None,
        op_tenant_id: int = None,
    ):
        # This parameter is required.
        self.create_row_permission_command = create_row_permission_command
        # This parameter is required.
        self.op_tenant_id = op_tenant_id

    def validate(self):
        if self.create_row_permission_command:
            self.create_row_permission_command.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_row_permission_command is not None:
            result['CreateRowPermissionCommand'] = self.create_row_permission_command.to_map()

        if self.op_tenant_id is not None:
            result['OpTenantId'] = self.op_tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateRowPermissionCommand') is not None:
            temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommand()
            self.create_row_permission_command = temp_model.from_map(m.get('CreateRowPermissionCommand'))

        if m.get('OpTenantId') is not None:
            self.op_tenant_id = m.get('OpTenantId')

        return self

class CreateRowPermissionRequestCreateRowPermissionCommand(DaraModel):
    def __init__(
        self,
        mapping_columns: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandMappingColumns] = None,
        row_permission_desc: str = None,
        row_permission_name: str = None,
        rules: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandRules] = None,
        tables: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandTables] = None,
    ):
        # This parameter is required.
        self.mapping_columns = mapping_columns
        self.row_permission_desc = row_permission_desc
        # This parameter is required.
        self.row_permission_name = row_permission_name
        self.rules = rules
        self.tables = tables

    def validate(self):
        if self.mapping_columns:
            for v1 in self.mapping_columns:
                 if v1:
                    v1.validate()
        if self.rules:
            for v1 in self.rules:
                 if v1:
                    v1.validate()
        if self.tables:
            for v1 in self.tables:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['MappingColumns'] = []
        if self.mapping_columns is not None:
            for k1 in self.mapping_columns:
                result['MappingColumns'].append(k1.to_map() if k1 else None)

        if self.row_permission_desc is not None:
            result['RowPermissionDesc'] = self.row_permission_desc

        if self.row_permission_name is not None:
            result['RowPermissionName'] = self.row_permission_name

        result['Rules'] = []
        if self.rules is not None:
            for k1 in self.rules:
                result['Rules'].append(k1.to_map() if k1 else None)

        result['Tables'] = []
        if self.tables is not None:
            for k1 in self.tables:
                result['Tables'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.mapping_columns = []
        if m.get('MappingColumns') is not None:
            for k1 in m.get('MappingColumns'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandMappingColumns()
                self.mapping_columns.append(temp_model.from_map(k1))

        if m.get('RowPermissionDesc') is not None:
            self.row_permission_desc = m.get('RowPermissionDesc')

        if m.get('RowPermissionName') is not None:
            self.row_permission_name = m.get('RowPermissionName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandRules()
                self.rules.append(temp_model.from_map(k1))

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandTables()
                self.tables.append(temp_model.from_map(k1))

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandTables(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        mapping_column_name: str = None,
        resource_id: str = None,
    ):
        # This parameter is required.
        self.column_name = column_name
        # This parameter is required.
        self.mapping_column_name = mapping_column_name
        # This parameter is required.
        self.resource_id = resource_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.mapping_column_name is not None:
            result['MappingColumnName'] = self.mapping_column_name

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('MappingColumnName') is not None:
            self.mapping_column_name = m.get('MappingColumnName')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandRules(DaraModel):
    def __init__(
        self,
        expressions: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesExpressions] = None,
        is_delete: bool = None,
        rule_name: str = None,
        scope_type: str = None,
        status: int = None,
        user_mapping_list: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingList] = None,
    ):
        # This parameter is required.
        self.expressions = expressions
        self.is_delete = is_delete
        # This parameter is required.
        self.rule_name = rule_name
        # This parameter is required.
        self.scope_type = scope_type
        # This parameter is required.
        self.status = status
        self.user_mapping_list = user_mapping_list

    def validate(self):
        if self.expressions:
            for v1 in self.expressions:
                 if v1:
                    v1.validate()
        if self.user_mapping_list:
            for v1 in self.user_mapping_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Expressions'] = []
        if self.expressions is not None:
            for k1 in self.expressions:
                result['Expressions'].append(k1.to_map() if k1 else None)

        if self.is_delete is not None:
            result['IsDelete'] = self.is_delete

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.scope_type is not None:
            result['ScopeType'] = self.scope_type

        if self.status is not None:
            result['Status'] = self.status

        result['UserMappingList'] = []
        if self.user_mapping_list is not None:
            for k1 in self.user_mapping_list:
                result['UserMappingList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.expressions = []
        if m.get('Expressions') is not None:
            for k1 in m.get('Expressions'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesExpressions()
                self.expressions.append(temp_model.from_map(k1))

        if m.get('IsDelete') is not None:
            self.is_delete = m.get('IsDelete')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('ScopeType') is not None:
            self.scope_type = m.get('ScopeType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        self.user_mapping_list = []
        if m.get('UserMappingList') is not None:
            for k1 in m.get('UserMappingList'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingList()
                self.user_mapping_list.append(temp_model.from_map(k1))

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingList(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        accounts: List[main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingListAccounts] = None,
    ):
        # This parameter is required.
        self.account_type = account_type
        # This parameter is required.
        self.accounts = accounts

    def validate(self):
        if self.accounts:
            for v1 in self.accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_type is not None:
            result['AccountType'] = self.account_type

        result['Accounts'] = []
        if self.accounts is not None:
            for k1 in self.accounts:
                result['Accounts'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountType') is not None:
            self.account_type = m.get('AccountType')

        self.accounts = []
        if m.get('Accounts') is not None:
            for k1 in m.get('Accounts'):
                temp_model = main_models.CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingListAccounts()
                self.accounts.append(temp_model.from_map(k1))

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandRulesUserMappingListAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # This parameter is required.
        self.account_id = account_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandRulesExpressions(DaraModel):
    def __init__(
        self,
        mapping_column_name: str = None,
        operator: str = None,
        sub_conditions: List[Any] = None,
        type: str = None,
        values: List[str] = None,
    ):
        # This parameter is required.
        self.mapping_column_name = mapping_column_name
        # This parameter is required.
        self.operator = operator
        # This parameter is required.
        self.sub_conditions = sub_conditions
        # This parameter is required.
        self.type = type
        # This parameter is required.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mapping_column_name is not None:
            result['MappingColumnName'] = self.mapping_column_name

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.sub_conditions is not None:
            result['SubConditions'] = self.sub_conditions

        if self.type is not None:
            result['Type'] = self.type

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MappingColumnName') is not None:
            self.mapping_column_name = m.get('MappingColumnName')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('SubConditions') is not None:
            self.sub_conditions = m.get('SubConditions')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

class CreateRowPermissionRequestCreateRowPermissionCommandMappingColumns(DaraModel):
    def __init__(
        self,
        column_desc: str = None,
        column_name: str = None,
        column_type: str = None,
    ):
        self.column_desc = column_desc
        # This parameter is required.
        self.column_name = column_name
        # This parameter is required.
        self.column_type = column_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_desc is not None:
            result['ColumnDesc'] = self.column_desc

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.column_type is not None:
            result['ColumnType'] = self.column_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnDesc') is not None:
            self.column_desc = m.get('ColumnDesc')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('ColumnType') is not None:
            self.column_type = m.get('ColumnType')

        return self

