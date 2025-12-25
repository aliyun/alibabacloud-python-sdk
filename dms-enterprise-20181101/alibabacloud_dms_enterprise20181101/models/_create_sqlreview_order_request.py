# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class CreateSQLReviewOrderRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        param: main_models.CreateSQLReviewOrderRequestParam = None,
        related_user_list: List[int] = None,
        tid: int = None,
    ):
        # The purpose or objective of the SQL review. This reduces unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param = param
        # The stakeholders involved in this operation. All the specified stakeholders can view the ticket details and take part in the approval process. Irrelevant users other than DMS administrators and database administrators (DBAs) are not allowed to view the ticket details.
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
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            temp_model = main_models.CreateSQLReviewOrderRequestParam()
            self.param = temp_model.from_map(m.get('Param'))

        if m.get('RelatedUserList') is not None:
            self.related_user_list = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

class CreateSQLReviewOrderRequestParam(DaraModel):
    def __init__(
        self,
        attachment_key_list: List[str] = None,
        db_id: int = None,
        project_name: str = None,
    ):
        # The files to be reviewed. Multiple files can be reviewed at a time.
        # 
        # This parameter is required.
        self.attachment_key_list = attachment_key_list
        # The ID of the database. You can call the [SearchDatabases](https://help.aliyun.com/document_detail/141876.html) operation to query the ID of the database.
        # 
        # >  You can call this operation to query only physical databases. This operation is unavailable to query logical databases.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The name of the project.
        # 
        # This parameter is required.
        self.project_name = project_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attachment_key_list is not None:
            result['AttachmentKeyList'] = self.attachment_key_list

        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AttachmentKeyList') is not None:
            self.attachment_key_list = m.get('AttachmentKeyList')

        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        return self

