# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetLogicDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_database: main_models.GetLogicDatabaseResponseBodyLogicDatabase = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The status code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The details of the logical database.
        self.logic_database = logic_database
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true: The request was successful.
        # *   false: The request failed.
        self.success = success

    def validate(self):
        if self.logic_database:
            self.logic_database.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.logic_database is not None:
            result['LogicDatabase'] = self.logic_database.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LogicDatabase') is not None:
            temp_model = main_models.GetLogicDatabaseResponseBodyLogicDatabase()
            self.logic_database = temp_model.from_map(m.get('LogicDatabase'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetLogicDatabaseResponseBodyLogicDatabase(DaraModel):
    def __init__(
        self,
        alias: str = None,
        database_id: str = None,
        database_ids: main_models.GetLogicDatabaseResponseBodyLogicDatabaseDatabaseIds = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_id_list: main_models.GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList = None,
        owner_name_list: main_models.GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList = None,
        schema_name: str = None,
        search_name: str = None,
    ):
        # The alias of the logical database.
        self.alias = alias
        # The ID of the logical database.
        self.database_id = database_id
        # The IDs of database shards of the logical database.
        self.database_ids = database_ids
        # The database engine. For more information about the valid values of the DbType parameter, see [DbType parameter](https://help.aliyun.com/document_detail/198106.html).
        self.db_type = db_type
        # The type of the environment to which the database belongs. Valid values:
        # 
        # *   product: production environment
        # *   dev: development environment
        # *   pre: pre-release environment
        # *   test: test environment
        # *   sit: system integration testing (SIT) environment
        # *   uat: user acceptance testing (UAT) environment
        # *   pet: stress testing environment
        # *   stag: staging environment
        self.env_type = env_type
        # Indicates whether the database is a logical database. The return value is true.
        self.logic = logic
        # The IDs of the owners of the logical database.
        self.owner_id_list = owner_id_list
        # The names of the owners of the logical database.
        self.owner_name_list = owner_name_list
        # The name of the logical database.
        self.schema_name = schema_name
        # The name that is used to search for the logical database.
        self.search_name = search_name

    def validate(self):
        if self.database_ids:
            self.database_ids.validate()
        if self.owner_id_list:
            self.owner_id_list.validate()
        if self.owner_name_list:
            self.owner_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alias is not None:
            result['Alias'] = self.alias

        if self.database_id is not None:
            result['DatabaseId'] = self.database_id

        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids.to_map()

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_id_list is not None:
            result['OwnerIdList'] = self.owner_id_list.to_map()

        if self.owner_name_list is not None:
            result['OwnerNameList'] = self.owner_name_list.to_map()

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')

        if m.get('DatabaseId') is not None:
            self.database_id = m.get('DatabaseId')

        if m.get('DatabaseIds') is not None:
            temp_model = main_models.GetLogicDatabaseResponseBodyLogicDatabaseDatabaseIds()
            self.database_ids = temp_model.from_map(m.get('DatabaseIds'))

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIdList') is not None:
            temp_model = main_models.GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList()
            self.owner_id_list = temp_model.from_map(m.get('OwnerIdList'))

        if m.get('OwnerNameList') is not None:
            temp_model = main_models.GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList()
            self.owner_name_list = temp_model.from_map(m.get('OwnerNameList'))

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetLogicDatabaseResponseBodyLogicDatabaseOwnerNameList(DaraModel):
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

class GetLogicDatabaseResponseBodyLogicDatabaseOwnerIdList(DaraModel):
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

class GetLogicDatabaseResponseBodyLogicDatabaseDatabaseIds(DaraModel):
    def __init__(
        self,
        database_ids: List[int] = None,
    ):
        self.database_ids = database_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.database_ids is not None:
            result['DatabaseIds'] = self.database_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DatabaseIds') is not None:
            self.database_ids = m.get('DatabaseIds')

        return self

