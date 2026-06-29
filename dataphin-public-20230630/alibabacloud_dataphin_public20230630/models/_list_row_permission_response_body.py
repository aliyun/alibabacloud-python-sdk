# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListRowPermissionResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListRowPermissionResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code. A value of OK indicates that the request was successful.
        self.code = code
        # The HTTP status code returned by the backend.
        self.http_status_code = http_status_code
        # The error message.
        self.message = message
        # The paged query result.
        self.page_result = page_result
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.page_result:
            self.page_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_result is not None:
            result['PageResult'] = self.page_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageResult') is not None:
            temp_model = main_models.ListRowPermissionResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRowPermissionResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRowPermissionResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        # The query result.
        self.data = data
        # The total number of records.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListRowPermissionResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRowPermissionResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        mapping_columns: List[main_models.ListRowPermissionResponseBodyPageResultDataMappingColumns] = None,
        modifier: str = None,
        row_permission_desc: str = None,
        row_permission_id: int = None,
        row_permission_name: str = None,
        rules: List[main_models.ListRowPermissionResponseBodyPageResultDataRules] = None,
        tables: List[main_models.ListRowPermissionResponseBodyPageResultDataTables] = None,
        tenant_id: int = None,
    ):
        # The creator.
        self.creator = creator
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The mapping fields.
        self.mapping_columns = mapping_columns
        # The modifier.
        self.modifier = modifier
        # The description of the row-level permission.
        self.row_permission_desc = row_permission_desc
        # The row-level permission ID.
        self.row_permission_id = row_permission_id
        # The name of the row-level permission.
        self.row_permission_name = row_permission_name
        # The rules.
        self.rules = rules
        # The related tables.
        self.tables = tables
        # The tenant ID.
        self.tenant_id = tenant_id

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
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        result['MappingColumns'] = []
        if self.mapping_columns is not None:
            for k1 in self.mapping_columns:
                result['MappingColumns'].append(k1.to_map() if k1 else None)

        if self.modifier is not None:
            result['Modifier'] = self.modifier

        if self.row_permission_desc is not None:
            result['RowPermissionDesc'] = self.row_permission_desc

        if self.row_permission_id is not None:
            result['RowPermissionId'] = self.row_permission_id

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

        if self.tenant_id is not None:
            result['TenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        self.mapping_columns = []
        if m.get('MappingColumns') is not None:
            for k1 in m.get('MappingColumns'):
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataMappingColumns()
                self.mapping_columns.append(temp_model.from_map(k1))

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        if m.get('RowPermissionDesc') is not None:
            self.row_permission_desc = m.get('RowPermissionDesc')

        if m.get('RowPermissionId') is not None:
            self.row_permission_id = m.get('RowPermissionId')

        if m.get('RowPermissionName') is not None:
            self.row_permission_name = m.get('RowPermissionName')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataRules()
                self.rules.append(temp_model.from_map(k1))

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class ListRowPermissionResponseBodyPageResultDataTables(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        mapping_column_name: str = None,
        resource_id: str = None,
    ):
        # The table field.
        self.column_name = column_name
        # The name of the mapping field.
        self.mapping_column_name = mapping_column_name
        # The GUID of the table.
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

class ListRowPermissionResponseBodyPageResultDataRules(DaraModel):
    def __init__(
        self,
        expressions: List[main_models.ListRowPermissionResponseBodyPageResultDataRulesExpressions] = None,
        id: int = None,
        is_delete: bool = None,
        rule_name: str = None,
        scope_type: str = None,
        status: int = None,
        user_mapping_list: List[main_models.ListRowPermissionResponseBodyPageResultDataRulesUserMappingList] = None,
    ):
        # The rule expressions.
        self.expressions = expressions
        # The rule ID.
        self.id = id
        # Indicates whether the rule is deleted.
        self.is_delete = is_delete
        # The rule name.
        self.rule_name = rule_name
        # The scope type of the rule.
        self.scope_type = scope_type
        # The rule status.
        self.status = status
        # The accounts bound to the rule.
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

        if self.id is not None:
            result['Id'] = self.id

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
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataRulesExpressions()
                self.expressions.append(temp_model.from_map(k1))

        if m.get('Id') is not None:
            self.id = m.get('Id')

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
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataRulesUserMappingList()
                self.user_mapping_list.append(temp_model.from_map(k1))

        return self

class ListRowPermissionResponseBodyPageResultDataRulesUserMappingList(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        accounts: List[main_models.ListRowPermissionResponseBodyPageResultDataRulesUserMappingListAccounts] = None,
    ):
        # The type of the account bound to the rule.
        self.account_type = account_type
        # The accounts bound to the rule.
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
                temp_model = main_models.ListRowPermissionResponseBodyPageResultDataRulesUserMappingListAccounts()
                self.accounts.append(temp_model.from_map(k1))

        return self

class ListRowPermissionResponseBodyPageResultDataRulesUserMappingListAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
    ):
        # The ID of the account bound to the rule.
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

class ListRowPermissionResponseBodyPageResultDataRulesExpressions(DaraModel):
    def __init__(
        self,
        mapping_column_name: str = None,
        operator: str = None,
        sub_conditions: List[Any] = None,
        type: str = None,
        values: List[str] = None,
    ):
        # The name of the mapping field.
        self.mapping_column_name = mapping_column_name
        # The expression operator.
        self.operator = operator
        # The sub-expressions.
        self.sub_conditions = sub_conditions
        # The expression type.
        self.type = type
        # The operation values of the expression.
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

class ListRowPermissionResponseBodyPageResultDataMappingColumns(DaraModel):
    def __init__(
        self,
        column_desc: str = None,
        column_name: str = None,
        column_type: str = None,
    ):
        # The description of the mapping field.
        self.column_desc = column_desc
        # The name of the mapping field.
        self.column_name = column_name
        # The type of the mapping field.
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

