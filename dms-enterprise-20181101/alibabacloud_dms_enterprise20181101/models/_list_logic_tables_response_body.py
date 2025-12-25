# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListLogicTablesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_table_list: main_models.ListLogicTablesResponseBodyLogicTableList = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The details of the logical tables.
        self.logic_table_list = logic_table_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request is successful.
        self.success = success
        # The total number of logical tables that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.logic_table_list:
            self.logic_table_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.logic_table_list is not None:
            result['LogicTableList'] = self.logic_table_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LogicTableList') is not None:
            temp_model = main_models.ListLogicTablesResponseBodyLogicTableList()
            self.logic_table_list = temp_model.from_map(m.get('LogicTableList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLogicTablesResponseBodyLogicTableList(DaraModel):
    def __init__(
        self,
        logic_table: List[main_models.ListLogicTablesResponseBodyLogicTableListLogicTable] = None,
    ):
        self.logic_table = logic_table

    def validate(self):
        if self.logic_table:
            for v1 in self.logic_table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogicTable'] = []
        if self.logic_table is not None:
            for k1 in self.logic_table:
                result['LogicTable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_table = []
        if m.get('LogicTable') is not None:
            for k1 in m.get('LogicTable'):
                temp_model = main_models.ListLogicTablesResponseBodyLogicTableListLogicTable()
                self.logic_table.append(temp_model.from_map(k1))

        return self

class ListLogicTablesResponseBodyLogicTableListLogicTable(DaraModel):
    def __init__(
        self,
        database_id: str = None,
        logic: bool = None,
        owner_id_list: main_models.ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList = None,
        owner_name_list: main_models.ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList = None,
        schema_name: str = None,
        table_count: str = None,
        table_expr: str = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
    ):
        # The ID of the logical database.
        self.database_id = database_id
        # Indicates whether the table is a logical table. The value is fixed to true.
        self.logic = logic
        # The IDs of the owners of the logical tables.
        self.owner_id_list = owner_id_list
        # The nicknames of the owners of the logical tables.
        self.owner_name_list = owner_name_list
        # The logical database to which the logical table belongs.
        self.schema_name = schema_name
        # The number of logical tables.
        self.table_count = table_count
        # The expression of the logical table.
        self.table_expr = table_expr
        # The GUID of the logical table.
        self.table_guid = table_guid
        # The ID of the logical table.
        self.table_id = table_id
        # The name of the logical table.
        self.table_name = table_name

    def validate(self):
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_count is not None:
            result['TableCount'] = self.table_count

        if self.table_expr is not None:
            result['TableExpr'] = self.table_expr

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableCount') is not None:
            self.table_count = m.get('TableCount')

        if m.get('TableExpr') is not None:
            self.table_expr = m.get('TableExpr')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class ListLogicTablesResponseBodyLogicTableListLogicTableOwnerNameList(DaraModel):
    def __init__(
        self,
        owner_names: List[str] = None,
    ):
        self.owner_names = owner_names

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_names is not None:
            result['OwnerNames'] = self.owner_names

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerNames') is not None:
            self.owner_names = m.get('OwnerNames')

        return self

class ListLogicTablesResponseBodyLogicTableListLogicTableOwnerIdList(DaraModel):
    def __init__(
        self,
        owner_ids: List[str] = None,
    ):
        self.owner_ids = owner_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        return self

