# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateStructSyncOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: main_models.CreateStructSyncOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The key of an attachment that is returned after the attachment is uploaded. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to query the key of the attachment.
        self.attachment_key = attachment_key
        # The remarks of the ticket.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        # The IDs of the stakeholders.
        self.related_user_list = related_user_list
        # The ID of the tenant.
        # 
        # >  To view the tenant ID, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see [Manage DMS tenants](https://help.aliyun.com/document_detail/181330.html).
        self.tid = tid

    def validate(self):
        if self.param:
            self.param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key is not None:
            result['AttachmentKey'] = self.attachment_key

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param is not None:
            result['Param'] = self.param.to_map()

        if self.related_user_list is not None:
            result['RelatedUserList'] = self.related_user_list

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKey') is not None:
            self.attachment_key = m.get('AttachmentKey')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            temp_model = main_models.CreateStructSyncOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateStructSyncOrderRequestParam(DaraModel):
    def __init__(
        self,
        ignore_error: bool = None,
        source: main_models.CreateStructSyncOrderRequestParamSource = None,
        table_info_list: List[main_models.CreateStructSyncOrderRequestParamTableInfoList] = None,
        target: main_models.CreateStructSyncOrderRequestParamTarget = None,
    ):
        # Specifies whether to skip an error that occurs in executing an SQL statement. Valid values:
        # 
        # *   **true**: continues to execute subsequent SQL statements if an error occurs in executing an SQL statement.
        # *   **false**: stops executing subsequent SQL statements if an error occurs in executing an SQL statement.
        self.ignore_error = ignore_error
        # The information about the base database.
        # 
        # This parameter is required.
        self.source = source
        # The information about the table of which you want to synchronize the schema.
        self.table_info_list = table_info_list
        # The information about the database to which you want to synchronize the schema of a table.
        # 
        # This parameter is required.
        self.target = target

    def validate(self):
        if self.source:
            self.source.validate()
        if self.table_info_list:
            for v1 in self.table_info_list:
                 if v1:
                    v1.validate()
        if self.target:
            self.target.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error

        if self.source is not None:
            result['Source'] = self.source.to_map()

        result['TableInfoList'] = []
        if self.table_info_list is not None:
            for k1 in self.table_info_list:
                result['TableInfoList'].append(k1.to_map() if k1 else None)

        if self.target is not None:
            result['Target'] = self.target.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')

        if m.get('Source') is not None:
            temp_model = main_models.CreateStructSyncOrderRequestParamSource()
            self.source = temp_model.from_map(m.get('Source'))

        self.table_info_list = []
        if m.get('TableInfoList') is not None:
            for k1 in m.get('TableInfoList'):
                temp_model = main_models.CreateStructSyncOrderRequestParamTableInfoList()
                self.table_info_list.append(temp_model.from_map(k1))

        if m.get('Target') is not None:
            temp_model = main_models.CreateStructSyncOrderRequestParamTarget()
            self.target = temp_model.from_map(m.get('Target'))

        return self

class CreateStructSyncOrderRequestParamTarget(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_search_name: str = None,
        logic: bool = None,
        version_id: str = None,
    ):
        # The ID of the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The name that is used to search for the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the name of the database.
        # 
        # This parameter is required.
        self.db_search_name = db_search_name
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database.
        self.logic = logic
        # The version number. By default, this parameter is left empty.
        # 
        # >  If you specify the schema version number of the destination database, Data Management (DMS) only compares the schemas of the two databases.
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

class CreateStructSyncOrderRequestParamTableInfoList(DaraModel):
    def __init__(
        self,
        source_table_name: str = None,
        target_table_name: str = None,
    ):
        # The name of the source table.
        self.source_table_name = source_table_name
        # The name of the destination table.
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

class CreateStructSyncOrderRequestParamSource(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        db_search_name: str = None,
        logic: bool = None,
        version_id: str = None,
    ):
        # The ID of the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The name that is used to search for the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the name of the database.
        # 
        # This parameter is required.
        self.db_search_name = db_search_name
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is not a logical database.
        self.logic = logic
        # The version number of the schema. The default value is the latest schema version number. For more information, see [Manage schema versions](https://help.aliyun.com/document_detail/202275.html).
        self.version_id = version_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.db_search_name is not None:
            result['DbSearchName'] = self.db_search_name

        if self.logic is not None:
            result['Logic'] = self.logic

        if self.version_id is not None:
            result['VersionId'] = self.version_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('DbSearchName') is not None:
            self.db_search_name = m.get('DbSearchName')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        if m.get('VersionId') is not None:
            self.version_id = m.get('VersionId')

        return self

