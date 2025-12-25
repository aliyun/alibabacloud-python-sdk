# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetPermApplyOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        perm_apply_order_detail: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The details of the permission application ticket.
        self.perm_apply_order_detail = perm_apply_order_detail
        # The request ID. You can use the ID to query logs and troubleshoot issues.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
        self.success = success

    def validate(self):
        if self.perm_apply_order_detail:
            self.perm_apply_order_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.perm_apply_order_detail is not None:
            result['PermApplyOrderDetail'] = self.perm_apply_order_detail.to_map()

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

        if m.get('PermApplyOrderDetail') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail()
            self.perm_apply_order_detail = temp_model.from_map(m.get('PermApplyOrderDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetail(DaraModel):
    def __init__(
        self,
        apply_type: str = None,
        perm_type: int = None,
        resources: List[main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources] = None,
        seconds: int = None,
    ):
        # The type of objects on which you apply for permissions. Valid values:
        # 
        # *   **DB**: database
        # *   **TAB**: table
        # *   **COL**: column
        # *   **INSTANT**: instance
        self.apply_type = apply_type
        # The type of the permissions that you apply for. Valid values:
        # 
        # *   **1**: the permissions to query information.
        # *   **2**: the permissions to export information.
        # *   **3**: the permissions to query and export information.
        # *   **4**: the permissions to modify information.
        # *   **5**: the permissions to query and modify information.
        # *   **6**: the permissions to export and modify information.
        # *   **7**: the permissions to query, export, and modify information.
        # *   **8**: the permissions to log on to the database.
        self.perm_type = perm_type
        # The list of resources.
        self.resources = resources
        # The validity duration of the permissions. Unit: seconds.
        self.seconds = seconds

    def validate(self):
        if self.resources:
            for v1 in self.resources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apply_type is not None:
            result['ApplyType'] = self.apply_type

        if self.perm_type is not None:
            result['PermType'] = self.perm_type

        result['Resources'] = []
        if self.resources is not None:
            for k1 in self.resources:
                result['Resources'].append(k1.to_map() if k1 else None)

        if self.seconds is not None:
            result['Seconds'] = self.seconds

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyType') is not None:
            self.apply_type = m.get('ApplyType')

        if m.get('PermType') is not None:
            self.perm_type = m.get('PermType')

        self.resources = []
        if m.get('Resources') is not None:
            for k1 in m.get('Resources'):
                temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources()
                self.resources.append(temp_model.from_map(k1))

        if m.get('Seconds') is not None:
            self.seconds = m.get('Seconds')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResources(DaraModel):
    def __init__(
        self,
        column_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo = None,
        database_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo = None,
        instance_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo = None,
        row_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowInfo = None,
        row_value_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowValueInfo = None,
        table_info: main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo = None,
    ):
        # The information about the column.
        self.column_info = column_info
        # The information about the database.
        self.database_info = database_info
        # The information about the instance.
        self.instance_info = instance_info
        self.row_info = row_info
        self.row_value_info = row_value_info
        # The information about the table.
        self.table_info = table_info

    def validate(self):
        if self.column_info:
            self.column_info.validate()
        if self.database_info:
            self.database_info.validate()
        if self.instance_info:
            self.instance_info.validate()
        if self.row_info:
            self.row_info.validate()
        if self.row_value_info:
            self.row_value_info.validate()
        if self.table_info:
            self.table_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_info is not None:
            result['ColumnInfo'] = self.column_info.to_map()

        if self.database_info is not None:
            result['DatabaseInfo'] = self.database_info.to_map()

        if self.instance_info is not None:
            result['InstanceInfo'] = self.instance_info.to_map()

        if self.row_info is not None:
            result['RowInfo'] = self.row_info.to_map()

        if self.row_value_info is not None:
            result['RowValueInfo'] = self.row_value_info.to_map()

        if self.table_info is not None:
            result['TableInfo'] = self.table_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo()
            self.column_info = temp_model.from_map(m.get('ColumnInfo'))

        if m.get('DatabaseInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo()
            self.database_info = temp_model.from_map(m.get('DatabaseInfo'))

        if m.get('InstanceInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo()
            self.instance_info = temp_model.from_map(m.get('InstanceInfo'))

        if m.get('RowInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowInfo()
            self.row_info = temp_model.from_map(m.get('RowInfo'))

        if m.get('RowValueInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowValueInfo()
            self.row_value_info = temp_model.from_map(m.get('RowValueInfo'))

        if m.get('TableInfo') is not None:
            temp_model = main_models.GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo()
            self.table_info = temp_model.from_map(m.get('TableInfo'))

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesTableInfo(DaraModel):
    def __init__(
        self,
        table_name: str = None,
    ):
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowValueInfo(DaraModel):
    def __init__(
        self,
        row_value: str = None,
    ):
        self.row_value = row_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.row_value is not None:
            result['RowValue'] = self.row_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RowValue') is not None:
            self.row_value = m.get('RowValue')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesRowInfo(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        db_id: int = None,
        logic: bool = None,
        match_mode: str = None,
        row_group_id: int = None,
        schema_name: str = None,
        table_name: str = None,
    ):
        self.column_name = column_name
        self.db_id = db_id
        self.logic = logic
        self.match_mode = match_mode
        self.row_group_id = row_group_id
        self.schema_name = schema_name
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.match_mode is not None:
            result['MatchMode'] = self.match_mode

        if self.row_group_id is not None:
            result['RowGroupId'] = self.row_group_id

        if self.schema_name is not None:
            result['SchemaName'] = self.schema_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('MatchMode') is not None:
            self.match_mode = m.get('MatchMode')

        if m.get('RowGroupId') is not None:
            self.row_group_id = m.get('RowGroupId')

        if m.get('SchemaName') is not None:
            self.schema_name = m.get('SchemaName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesInstanceInfo(DaraModel):
    def __init__(
        self,
        db_type: str = None,
        dba_id: int = None,
        dba_nick_name: str = None,
        env_type: str = None,
        host: str = None,
        instance_id: str = None,
        owner_ids: List[int] = None,
        owner_nick_name: List[str] = None,
        port: int = None,
        search_name: str = None,
    ):
        # The type of the database engine.
        self.db_type = db_type
        # The ID of the database administrator (DBA) of the instance.
        self.dba_id = dba_id
        # The nickname of the DBA of the instance.
        self.dba_nick_name = dba_nick_name
        # The type of the environment to which the instance belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # The endpoint of the instance.
        self.host = host
        # The ID of the instance.
        self.instance_id = instance_id
        # The IDs of the owners of the instance.
        self.owner_ids = owner_ids
        # The nicknames of the owners of the instance.
        self.owner_nick_name = owner_nick_name
        # The port that is used to connect to the instance.
        self.port = port
        # The name that is used to search for the instance.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.dba_id is not None:
            result['DbaId'] = self.dba_id

        if self.dba_nick_name is not None:
            result['DbaNickName'] = self.dba_nick_name

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.host is not None:
            result['Host'] = self.host

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_nick_name is not None:
            result['OwnerNickName'] = self.owner_nick_name

        if self.port is not None:
            result['Port'] = self.port

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('DbaId') is not None:
            self.dba_id = m.get('DbaId')

        if m.get('DbaNickName') is not None:
            self.dba_nick_name = m.get('DbaNickName')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Host') is not None:
            self.host = m.get('Host')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerNickName') is not None:
            self.owner_nick_name = m.get('OwnerNickName')

        if m.get('Port') is not None:
            self.port = m.get('Port')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesDatabaseInfo(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        owner_ids: List[int] = None,
        owner_nick_names: List[str] = None,
        search_name: str = None,
    ):
        # The database ID.
        self.db_id = db_id
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment to which the instance belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.logic = logic
        # The IDs of the owners of the database.
        self.owner_ids = owner_ids
        # The nicknames of the owners of the database.
        self.owner_nick_names = owner_nick_names
        # The name that is used to search for the database.
        self.search_name = search_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_type is not None:
            result['DbType'] = self.db_type

        if self.env_type is not None:
            result['EnvType'] = self.env_type

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.owner_ids is not None:
            result['OwnerIds'] = self.owner_ids

        if self.owner_nick_names is not None:
            result['OwnerNickNames'] = self.owner_nick_names

        if self.search_name is not None:
            result['SearchName'] = self.search_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbType') is not None:
            self.db_type = m.get('DbType')

        if m.get('EnvType') is not None:
            self.env_type = m.get('EnvType')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('OwnerIds') is not None:
            self.owner_ids = m.get('OwnerIds')

        if m.get('OwnerNickNames') is not None:
            self.owner_nick_names = m.get('OwnerNickNames')

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetPermApplyOrderDetailResponseBodyPermApplyOrderDetailResourcesColumnInfo(DaraModel):
    def __init__(
        self,
        column_name: str = None,
        table_name: str = None,
    ):
        # The name of the column.
        self.column_name = column_name
        # The name of the table.
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

