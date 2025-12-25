# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateDataImportOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: main_models.CreateDataImportOrderRequestParam = None,
        real_login_user_uid: str = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The key of the attachment that provides more instructions for the ticket. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to obtain the attachment key from the value of the AttachmentKey parameter.
        self.attachment_key = attachment_key
        # The purpose or objective of the data import. This parameter is used to help reduce unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        self.real_login_user_uid = real_login_user_uid
        # The stakeholders of the data import. All stakeholders can view the ticket details and assist in the approval process. Irrelevant users other than DMS administrators and database administrators (DBAs) are not allowed to view the ticket details.
        self.related_user_list = related_user_list
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
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

        if self.real_login_user_uid is not None:
            result['RealLoginUserUid'] = self.real_login_user_uid

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
            temp_model = main_models.CreateDataImportOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateDataImportOrderRequestParam(DaraModel):
    def __init__(
        self,
        attachment_name: str = None,
        classify: str = None,
        csv_first_row_is_column_def: bool = None,
        db_item_list: List[main_models.CreateDataImportOrderRequestParamDbItemList] = None,
        exec_mode: str = None,
        file_encoding: str = None,
        file_type: str = None,
        ignore_error: bool = None,
        import_mode: str = None,
        insert_type: str = None,
        rollback_attachment_name: str = None,
        rollback_sql: str = None,
        rollback_sql_type: str = None,
        table_name: str = None,
    ):
        # The key of the attachment that contains the SQL statements used to import data. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to the attachment key from the value of the AttachmentKey parameter.
        # 
        # This parameter is required.
        self.attachment_name = attachment_name
        # The reason for the data import.
        self.classify = classify
        # The type of the CSV file. Valid values:
        # 
        # *   **true**: The first row in the CSV file contains field names.
        # *   **false**: The first row in the CSV file contains data.
        # 
        # >  This parameter is required if you set the **FileType** parameter to **CSV**.
        self.csv_first_row_is_column_def = csv_first_row_is_column_def
        # The database to which you want to import data. You can specify only one database.
        # 
        # This parameter is required.
        self.db_item_list = db_item_list
        self.exec_mode = exec_mode
        # The encoding algorithm to be used by the destination database. Valid values:
        # 
        # *   **AUTO**: automatic identification
        # *   **UTF-8**: UTF-8 encoding
        # *   **GBK**: GBK encoding
        # *   **ISO-8859-1**: ISO-8859-1 encoding
        self.file_encoding = file_encoding
        # The format of the file for the data import. Valid values:
        # 
        # *   **SQL**: an SQL file
        # *   **CSV**: a CSV file
        # 
        # This parameter is required.
        self.file_type = file_type
        # Specifies whether to skip an error that occurs. Valid values:
        # 
        # *   **true**: skips the error and continues to execute SQL statements.
        # *   **false**: stops executing SQL statements.
        self.ignore_error = ignore_error
        # The import mode. Valid values:
        # 
        # *   **FAST_MODE**: In the Execute step, the uploaded file is read and SQL statements are executed to import data to the specified destination database. Compared with the security mode, this mode can be used to import data in a less secure but more efficient manner.
        # *   **SAFE_MODE**: In the Precheck step, the uploaded file is parsed, and SQL statements or CSV file data is cached. In the Execute step, the cached SQL statements are read and executed to import data, or the cached CSV file data is read and imported to the specified destination database. This mode can be used to import data in a more secure but less efficient manner.
        self.import_mode = import_mode
        # The mode in which the data in the CSV format is to be written to the destination table. Valid values:
        # 
        # *   **INSERT**: The database checks the primary key when data is written. If a duplicate primary key value exists, an error message is returned.
        # *   **INSERT_IGNORE**: If the imported data contains data records that are the same as those in the destination table, the new data records are ignored.
        # *   **REPLACE_INTO**: If the imported data contains a row that has the same value for the primary key or unique index as one row in the destination table, the database deletes the existing row and inserts the new row into the destination table.
        # 
        # >  This parameter is required if you set the **FileType** parameter to **CSV**.
        self.insert_type = insert_type
        # The key of the attachment that contains the SQL statements used to roll back the data import. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to obtain the attachment key from the value of the AttachmentKey parameter.
        # 
        # >  This parameter is required if you set the **RollbackSqlType** parameter to **ATTACHMENT**.
        self.rollback_attachment_name = rollback_attachment_name
        # The SQL statements used to roll back the data import.
        # 
        # >  This parameter is required if you set the **RollbackSqlType** parameter to **TEXT**.
        self.rollback_sql = rollback_sql
        # The format of the SQL statements used to roll back the data import. Valid values:
        # 
        # *   **TEXT**: text
        # *   **ATTACHMENT**: attachment
        self.rollback_sql_type = rollback_sql_type
        # The destination table to which you want to import the data in the CSV format.
        # 
        # >  This parameter is required if you set the **FileType** parameter to **CSV**.
        self.table_name = table_name

    def validate(self):
        if self.db_item_list:
            for v1 in self.db_item_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_name is not None:
            result['AttachmentName'] = self.attachment_name

        if self.classify is not None:
            result['Classify'] = self.classify

        if self.csv_first_row_is_column_def is not None:
            result['CsvFirstRowIsColumnDef'] = self.csv_first_row_is_column_def

        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k1 in self.db_item_list:
                result['DbItemList'].append(k1.to_map() if k1 else None)

        if self.exec_mode is not None:
            result['ExecMode'] = self.exec_mode

        if self.file_encoding is not None:
            result['FileEncoding'] = self.file_encoding

        if self.file_type is not None:
            result['FileType'] = self.file_type

        if self.ignore_error is not None:
            result['IgnoreError'] = self.ignore_error

        if self.import_mode is not None:
            result['ImportMode'] = self.import_mode

        if self.insert_type is not None:
            result['InsertType'] = self.insert_type

        if self.rollback_attachment_name is not None:
            result['RollbackAttachmentName'] = self.rollback_attachment_name

        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql

        if self.rollback_sql_type is not None:
            result['RollbackSqlType'] = self.rollback_sql_type

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        if m.get('CsvFirstRowIsColumnDef') is not None:
            self.csv_first_row_is_column_def = m.get('CsvFirstRowIsColumnDef')

        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k1 in m.get('DbItemList'):
                temp_model = main_models.CreateDataImportOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k1))

        if m.get('ExecMode') is not None:
            self.exec_mode = m.get('ExecMode')

        if m.get('FileEncoding') is not None:
            self.file_encoding = m.get('FileEncoding')

        if m.get('FileType') is not None:
            self.file_type = m.get('FileType')

        if m.get('IgnoreError') is not None:
            self.ignore_error = m.get('IgnoreError')

        if m.get('ImportMode') is not None:
            self.import_mode = m.get('ImportMode')

        if m.get('InsertType') is not None:
            self.insert_type = m.get('InsertType')

        if m.get('RollbackAttachmentName') is not None:
            self.rollback_attachment_name = m.get('RollbackAttachmentName')

        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')

        if m.get('RollbackSqlType') is not None:
            self.rollback_sql_type = m.get('RollbackSqlType')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class CreateDataImportOrderRequestParamDbItemList(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        logic: bool = None,
    ):
        # The ID of the database. The database can be a physical database or a logical database.
        # 
        # *   To obtain the ID of a physical database, call the [ListDatabases](https://help.aliyun.com/document_detail/141873.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # *   To obtain the ID of a logical database, call the [ListLogicDatabases](https://help.aliyun.com/document_detail/141874.html) or [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation.
        # 
        # This parameter is required.
        self.db_id = db_id
        # Specifies whether the database is a logical database. Valid values:
        # 
        # *   **true**: The database is a logical database.
        # *   **false**: The database is a physical database.
        # 
        # >  If you set this parameter to **true**, the database that you specify must be a logical database.
        # 
        # This parameter is required.
        self.logic = logic

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.logic is not None:
            result['Logic'] = self.logic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Logic') is not None:
            self.logic = m.get('Logic')

        return self

