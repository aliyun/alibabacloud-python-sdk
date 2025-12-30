# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class ListRowPermissionByUserIdResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        page_result: main_models.ListRowPermissionByUserIdResponseBodyPageResult = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.page_result = page_result
        self.request_id = request_id
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
            temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResult()
            self.page_result = temp_model.from_map(m.get('PageResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListRowPermissionByUserIdResponseBodyPageResult(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultData] = None,
        total_count: int = None,
    ):
        self.data = data
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
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultData()
                self.data.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListRowPermissionByUserIdResponseBodyPageResultData(DaraModel):
    def __init__(
        self,
        creator: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        modifier: str = None,
        rules: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRules] = None,
        tables: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultDataTables] = None,
        tenant_id: int = None,
    ):
        self.creator = creator
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.modifier = modifier
        self.rules = rules
        self.tables = tables
        self.tenant_id = tenant_id

    def validate(self):
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

        if self.modifier is not None:
            result['Modifier'] = self.modifier

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

        if m.get('Modifier') is not None:
            self.modifier = m.get('Modifier')

        self.rules = []
        if m.get('Rules') is not None:
            for k1 in m.get('Rules'):
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRules()
                self.rules.append(temp_model.from_map(k1))

        self.tables = []
        if m.get('Tables') is not None:
            for k1 in m.get('Tables'):
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultDataTables()
                self.tables.append(temp_model.from_map(k1))

        if m.get('TenantId') is not None:
            self.tenant_id = m.get('TenantId')

        return self

class ListRowPermissionByUserIdResponseBodyPageResultDataTables(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        mapping_column_name: str = None,
        resource_id: str = None,
    ):
        self.column_name = column_name
        self.mapping_column_name = mapping_column_name
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

class ListRowPermissionByUserIdResponseBodyPageResultDataRules(DaraModel):
    def __init__(
        self,
        expressions: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesExpressions] = None,
        is_delete: bool = None,
        rule_name: str = None,
        scope_type: str = None,
        status: int = None,
        user_mapping_list: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingList] = None,
    ):
        self.expressions = expressions
        self.is_delete = is_delete
        self.rule_name = rule_name
        self.scope_type = scope_type
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
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesExpressions()
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
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingList()
                self.user_mapping_list.append(temp_model.from_map(k1))

        return self

class ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingList(DaraModel):
    def __init__(
        self,
        account_type: str = None,
        accounts: List[main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingListAccounts] = None,
    ):
        self.account_type = account_type
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
                temp_model = main_models.ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingListAccounts()
                self.accounts.append(temp_model.from_map(k1))

        return self

class ListRowPermissionByUserIdResponseBodyPageResultDataRulesUserMappingListAccounts(DaraModel):
    def __init__(
        self,
        account_id: str = None,
    ):
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

class ListRowPermissionByUserIdResponseBodyPageResultDataRulesExpressions(DaraModel):
    def __init__(
        self,
        mapping_column_name: str = None,
        operator: str = None,
        sub_conditions: List[Any] = None,
        type: str = None,
        values: List[str] = None,
    ):
        self.mapping_column_name = mapping_column_name
        self.operator = operator
        self.sub_conditions = sub_conditions
        self.type = type
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

