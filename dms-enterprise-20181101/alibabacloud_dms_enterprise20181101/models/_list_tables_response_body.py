# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListTablesResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
        table_list: main_models.ListTablesResponseBodyTableList = None,
        total_count: int = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success
        # The details of the tables.
        self.table_list = table_list
        # The total number of tables that meet the query conditions.
        self.total_count = total_count

    def validate(self):
        if self.table_list:
            self.table_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.table_list is not None:
            result['TableList'] = self.table_list.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TableList') is not None:
            temp_model = main_models.ListTablesResponseBodyTableList()
            self.table_list = temp_model.from_map(m.get('TableList'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListTablesResponseBodyTableList(DaraModel):
    def __init__(
        self,
        table: List[main_models.ListTablesResponseBodyTableListTable] = None,
    ):
        self.table = table

    def validate(self):
        if self.table:
            for v1 in self.table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Table'] = []
        if self.table is not None:
            for k1 in self.table:
                result['Table'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.table = []
        if m.get('Table') is not None:
            for k1 in m.get('Table'):
                temp_model = main_models.ListTablesResponseBodyTableListTable()
                self.table.append(temp_model.from_map(k1))

        return self

class ListTablesResponseBodyTableListTable(DaraModel):
    def __init__(
        self,
        database_id: str = None,
        description: str = None,
        encoding: str = None,
        engine: str = None,
        num_rows: int = None,
        owner_id_list: main_models.ListTablesResponseBodyTableListTableOwnerIdList = None,
        owner_name_list: main_models.ListTablesResponseBodyTableListTableOwnerNameList = None,
        store_capacity: int = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
        table_schema_name: str = None,
        table_type: str = None,
    ):
        # The ID of the physical database.
        self.database_id = database_id
        # The description of the table.
        self.description = description
        # The encoding format of the table.
        self.encoding = encoding
        # The engine of the table.
        self.engine = engine
        # The number of rows in the table. This is a statistical value and does not indicate the actual number of rows.
        self.num_rows = num_rows
        # The ID list of the table owners.
        self.owner_id_list = owner_id_list
        # The nickname list of the table owners.
        self.owner_name_list = owner_name_list
        # The storage space that is occupied by the table. This is a statistical value and does not indicate the accurate storage space. Unit: MB.
        self.store_capacity = store_capacity
        # The GUID of the table in DMS.
        self.table_guid = table_guid
        # The ID of the table.
        self.table_id = table_id
        # The table name.
        self.table_name = table_name
        # The database in which the table resides.
        self.table_schema_name = table_schema_name
        # The type of the table. Default value: NORMAL.
        self.table_type = table_type

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

        if self.description is not None:
            result['Description'] = self.description

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.num_rows is not None:
            result['NumRows'] = self.num_rows

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.store_capacity is not None:
            result['StoreCapacity'] = self.store_capacity

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        if self.table_type is not None:
            result['TableType'] = self.table_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('NumRows') is not None:
            self.num_rows = m.get('NumRows')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.ListTablesResponseBodyTableListTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.ListTablesResponseBodyTableListTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('StoreCapacity') is not None:
            self.store_capacity = m.get('StoreCapacity')

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        if m.get('TableType') is not None:
            self.table_type = m.get('TableType')

        return self

class ListTablesResponseBodyTableListTableOwnerNameList(DaraModel):
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

class ListTablesResponseBodyTableListTableOwnerIdList(DaraModel):
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

