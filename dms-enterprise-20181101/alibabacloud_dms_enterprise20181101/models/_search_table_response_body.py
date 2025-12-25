# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class SearchTableResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        search_table_list: main_models.SearchTableResponseBodySearchTableList = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The details of the tables.
        self.search_table_list = search_table_list
        # Indicates whether the request was successful.
        self.success = success
        # The total number of entries that are returned.
        self.total_count = total_count

    def validate(self):
        if self.search_table_list:
            self.search_table_list.validate()

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

        if self.search_table_list is not None:
            result['SearchTableList'] = self.search_table_list.to_map()

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

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SearchTableList') is not None:
            temp_model = main_models.SearchTableResponseBodySearchTableList()
            self.search_table_list = temp_model.from_map(m.get('SearchTableList'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class SearchTableResponseBodySearchTableList(DaraModel):
    def __init__(
        self,
        search_table: List[main_models.SearchTableResponseBodySearchTableListSearchTable] = None,
    ):
        self.search_table = search_table

    def validate(self):
        if self.search_table:
            for v1 in self.search_table:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SearchTable'] = []
        if self.search_table is not None:
            for k1 in self.search_table:
                result['SearchTable'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_table = []
        if m.get('SearchTable') is not None:
            for k1 in m.get('SearchTable'):
                temp_model = main_models.SearchTableResponseBodySearchTableListSearchTable()
                self.search_table.append(temp_model.from_map(k1))

        return self

class SearchTableResponseBodySearchTableListSearchTable(DaraModel):
    def __init__(
        self,
        dbsearch_name: str = None,
        database_id: str = None,
        db_name: str = None,
        db_type: str = None,
        description: str = None,
        encoding: str = None,
        engine: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: main_models.SearchTableResponseBodySearchTableListSearchTableOwnerIdList = None,
        owner_name_list: main_models.SearchTableResponseBodySearchTableListSearchTableOwnerNameList = None,
        table_guid: str = None,
        table_id: str = None,
        table_name: str = None,
        table_schema_name: str = None,
    ):
        # The name that is used to search for the database to which the table belongs.
        self.dbsearch_name = dbsearch_name
        # The ID of the database to which the table belongs.
        self.database_id = database_id
        # The name of the database.
        self.db_name = db_name
        # The type of the database. Valid values:
        # 
        # *   **MySQL**
        # *   **SQLServer**
        # *   **PostgreSQL**
        # *   **Oracle**
        # *   **DRDS**
        # *   **OceanBase**
        # *   **Mongo**
        # *   **Redis**
        self.db_type = db_type
        # The description of the table.
        self.description = description
        # The encoding format of the table.
        self.encoding = encoding
        # The engine of the table.
        self.engine = engine
        # The type of the environment to which the database belongs.
        self.env_type = env_type
        # Indicates whether the table is a logical table. Valid values:
        # 
        # *   **true**: The table is a logical table.
        # *   **false**: The table is not a logical table.
        self.logic = logic
        # The IDs of the table owners.
        self.owner_id_list = owner_id_list
        # The nicknames of the table owners.
        self.owner_name_list = owner_name_list
        # The GUID of the table.
        self.table_guid = table_guid
        # The ID of the table.
        self.table_id = table_id
        # The name of the table.
        self.table_name = table_name
        # The name of the database to which the table belongs.
        self.table_schema_name = table_schema_name

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
        if self.dbsearch_name is not None:
            result['DBSearchName'] = self.dbsearch_name

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.description is not None:
            result['Description'] = self.description

        if self.encoding is not None:
            result['Encoding'] = self.encoding

        if self.engine is not None:
            result['Engine'] = self.engine

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.table_guid is not None:
            result['TableGuid'] = self.table_guid

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.table_schema_name is not None:
            result['TableSchemaName'] = self.table_schema_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBSearchName') is not None:
            self.dbsearch_name = m.get('DBSearchName')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Encoding') is not None:
            self.encoding = m.get('Encoding')

        if m.get('Engine') is not None:
            self.engine = m.get('Engine')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.SearchTableResponseBodySearchTableListSearchTableOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.SearchTableResponseBodySearchTableListSearchTableOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('TableGuid') is not None:
            self.table_guid = m.get('TableGuid')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TableSchemaName') is not None:
            self.table_schema_name = m.get('TableSchemaName')

        return self

class SearchTableResponseBodySearchTableListSearchTableOwnerNameList(DaraModel):
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

class SearchTableResponseBodySearchTableListSearchTableOwnerIdList(DaraModel):
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

