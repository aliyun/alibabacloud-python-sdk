# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateFreeLockCorrectOrderRequest(DaraModel):
    def __init__(
        self,
        attachment_key: str = None,
        comment: str = None,
        param: main_models.CreateFreeLockCorrectOrderRequestParam = None,
        real_login_user_uid: str = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The key of the attachment that provides more instructions for the ticket. You can call the [GetUserUploadFileJob](https://help.aliyun.com/document_detail/206069.html) operation to obtain the attachment key from the value of the AttachmentKey parameter.
        self.attachment_key = attachment_key
        # The purpose or objective of the data change. This parameter is used to help reduce unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        self.real_login_user_uid = real_login_user_uid
        # The stakeholders of the data change. All stakeholders can view the ticket details and assist in the approval process. Irrelevant users other than DMS administrators and database administrators (DBAs) are not allowed to view the ticket details.
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
            temp_model = main_models.CreateFreeLockCorrectOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RealLoginUserUid') is not None:
            self.real_login_user_uid = m.get('RealLoginUserUid')

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateFreeLockCorrectOrderRequestParam(DaraModel):
    def __init__(
        self,
        attachment_name: str = None,
        classify: str = None,
        db_item_list: List[main_models.CreateFreeLockCorrectOrderRequestParamDbItemList] = None,
        exec_mode: str = None,
        exec_sql: str = None,
        rollback_attachment_name: str = None,
        rollback_sql: str = None,
        rollback_sql_type: str = None,
        sql_type: str = None,
    ):
        # The key of the attachment that contains the SQL statements used to change data. This parameter is not supported.
        self.attachment_name = attachment_name
        # The reason for the data change.
        self.classify = classify
        # The databases in which you want to change data.
        # 
        # This parameter is required.
        self.db_item_list = db_item_list
        # The execution mode of the ticket after the ticket is approved. Valid values:
        # 
        # *   **COMMITOR**: The data change is performed by the user who submits the ticket.
        # *   **AUTO**: The data change is automatically performed after the ticket is approved.
        # *   **LAST_AUDITOR**: The data change is performed by the last approver of the ticket.
        self.exec_mode = exec_mode
        # The SQL statements that you want to execute to change data.
        # 
        # This parameter is required.
        self.exec_sql = exec_sql
        # The key of the attachment that contains the SQL statements used to roll back the data change.
        self.rollback_attachment_name = rollback_attachment_name
        # The SQL statements used to roll back the data change.
        self.rollback_sql = rollback_sql
        # The format of the SQL statements used to roll back the data change. Valid values:
        # 
        # *   **TEXT**: text
        # *   **ATTACHMENT**: attachment. This value is not supported.
        self.rollback_sql_type = rollback_sql_type
        # The format of the SQL statements used to change data. Valid values:
        # 
        # *   **TEXT**: text
        # *   **ATTACHMENT**: attachment. This value is not supported.
        # 
        # This parameter is required.
        self.sql_type = sql_type

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

        result['DbItemList'] = []
        if self.db_item_list is not None:
            for k1 in self.db_item_list:
                result['DbItemList'].append(k1.to_map() if k1 else None)

        if self.exec_mode is not None:
            result['ExecMode'] = self.exec_mode

        if self.exec_sql is not None:
            result['ExecSQL'] = self.exec_sql

        if self.rollback_attachment_name is not None:
            result['RollbackAttachmentName'] = self.rollback_attachment_name

        if self.rollback_sql is not None:
            result['RollbackSQL'] = self.rollback_sql

        if self.rollback_sql_type is not None:
            result['RollbackSqlType'] = self.rollback_sql_type

        if self.sql_type is not None:
            result['SqlType'] = self.sql_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentName') is not None:
            self.attachment_name = m.get('AttachmentName')

        if m.get('Classify') is not None:
            self.classify = m.get('Classify')

        self.db_item_list = []
        if m.get('DbItemList') is not None:
            for k1 in m.get('DbItemList'):
                temp_model = main_models.CreateFreeLockCorrectOrderRequestParamDbItemList()
                self.db_item_list.append(temp_model.from_map(k1))

        if m.get('ExecMode') is not None:
            self.exec_mode = m.get('ExecMode')

        if m.get('ExecSQL') is not None:
            self.exec_sql = m.get('ExecSQL')

        if m.get('RollbackAttachmentName') is not None:
            self.rollback_attachment_name = m.get('RollbackAttachmentName')

        if m.get('RollbackSQL') is not None:
            self.rollback_sql = m.get('RollbackSQL')

        if m.get('RollbackSqlType') is not None:
            self.rollback_sql_type = m.get('RollbackSqlType')

        if m.get('SqlType') is not None:
            self.sql_type = m.get('SqlType')

        return self

class CreateFreeLockCorrectOrderRequestParamDbItemList(DaraModel):
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

