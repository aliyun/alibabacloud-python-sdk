# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class GetStructSyncOrderDetailResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        struct_sync_order_detail: main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail = None,
        success: bool = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # The details of the schema synchronization ticket.
        self.struct_sync_order_detail = struct_sync_order_detail
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        if self.struct_sync_order_detail:
            self.struct_sync_order_detail.validate()

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

        if self.struct_sync_order_detail is not None:
            result['StructSyncOrderDetail'] = self.struct_sync_order_detail.to_map()

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StructSyncOrderDetail') is not None:
            temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail()
            self.struct_sync_order_detail = temp_model.from_map(m.get('StructSyncOrderDetail'))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetail(DaraModel):
    def __init__(
        self,
        ignore_error: bool = None,
        source_database_info: main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo = None,
        source_type: str = None,
        source_version_info: main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo = None,
        table_info_list: List[main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList] = None,
        target_database_info: main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo = None,
        target_type: str = None,
        target_version_info: main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo = None,
    ):
        # Indicates whether to skip errors. Valid values:
        # 
        # *   **true**: skips the error and continues to execute SQL statements.
        # *   **false**: stops executing SQL statements.
        self.ignore_error = ignore_error
        # The information about the source database.
        self.source_database_info = source_database_info
        # The schema version of the source database. Valid values:
        # 
        # *   **DATASOURCE**: the default latest version of the system
        # *   **VERSION**: a previous schema version that you manually specify
        self.source_type = source_type
        # The version information about the source instance.
        # 
        # > This parameter is displayed only when the value of the **SourceType** parameter is **VERSION**.
        self.source_version_info = source_version_info
        # The information about the table whose schema you want to synchronize.
        self.table_info_list = table_info_list
        # The information about the destination database.
        self.target_database_info = target_database_info
        # The schema version of the destination database. Valid values:
        # 
        # *   **DATASOURCE**: the default latest version of the system
        # *   **VERSION**: a previous schema version that you manually specify
        self.target_type = target_type
        # The version information about the destination instance.
        # 
        # > This parameter is displayed only when the value of the **SourceType** parameter is **VERSION**.
        self.target_version_info = target_version_info

    def validate(self):
        if self.source_database_info:
            self.source_database_info.validate()
        if self.source_version_info:
            self.source_version_info.validate()
        if self.table_info_list:
            for v1 in self.table_info_list:
                 if v1:
                    v1.validate()
        if self.target_database_info:
            self.target_database_info.validate()
        if self.target_version_info:
            self.target_version_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error

        if self.source_database_info is not None:
            result['SourceDatabaseInfo'] = self.source_database_info.to_map()

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.source_version_info is not None:
            result['SourceVersionInfo'] = self.source_version_info.to_map()

        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k1 in self.table_info_list:
                result['TableInfoList'].append(k1.to_map() if k1 else None)

        if self.target_database_info is not None:
            result['TargetDatabaseInfo'] = self.target_database_info.to_map()

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        if self.target_version_info is not None:
            result['TargetVersionInfo'] = self.target_version_info.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')

        if m.get('SourceDatabaseInfo') is not None:
            temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo()
            self.source_database_info = temp_model.from_map(m.get('SourceDatabaseInfo'))

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SourceVersionInfo') is not None:
            temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo()
            self.source_version_info = temp_model.from_map(m.get('SourceVersionInfo'))

        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k1 in m.get('TableInfoList'):
                temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList()
                self.table_info_list.append(temp_model.from_map(k1))

        if m.get('TargetDatabaseInfo') is not None:
            temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo()
            self.target_database_info = temp_model.from_map(m.get('TargetDatabaseInfo'))

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        if m.get('TargetVersionInfo') is not None:
            temp_model = main_models.GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo()
            self.target_version_info = temp_model.from_map(m.get('TargetVersionInfo'))

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetVersionInfo(DaraModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        # The version number.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTargetDatabaseInfo(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        # The ID of the destination database.
        self.db_id = db_id
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment to which the database instance belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database
        self.logic = logic
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

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailTableInfoList(DaraModel):
    def __init__(
        self,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        # The name of the table whose schema you want to synchronize.
        self.source_table_name = source_table_name
        # The name of the table to which you want to synchronize the schema of a table.
        self.target_table_name = target_table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.source_table_name is not None:
            result['SourceTableName'] = self.source_table_name

        if self.target_table_name is not None:
            result['TargetTableName'] = self.target_table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SourceTableName') is not None:
            self.source_table_name = m.get('SourceTableName')

        if m.get('TargetTableName') is not None:
            self.target_table_name = m.get('TargetTableName')

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceVersionInfo(DaraModel):
    def __init__(
        self,
        version_id: str = None,
    ):
        # The version number.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class GetStructSyncOrderDetailResponseBodyStructSyncOrderDetailSourceDatabaseInfo(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_type: str = None,
        env_type: str = None,
        logic: bool = None,
        search_name: str = None,
    ):
        # The ID of the source database.
        self.db_id = db_id
        # The type of the database engine.
        self.db_type = db_type
        # The type of the environment to which the database instance belongs. For more information, see [Change the environment type of an instance](https://help.aliyun.com/document_detail/163309.html).
        self.env_type = env_type
        # Indicates whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database
        self.logic = logic
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

        if m.get('SearchName') is not None:
            self.search_name = m.get('SearchName')

        return self

