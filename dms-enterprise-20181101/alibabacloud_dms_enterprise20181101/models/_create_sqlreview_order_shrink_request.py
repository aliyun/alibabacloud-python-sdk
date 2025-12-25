# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSQLReviewOrderShrinkRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        param_shrink: str = None,
        related_user_list_shrink: str = None,
        tid: int = None,
    ):
        # The purpose or objective of the SQL review. This reduces unnecessary communication.
        # 
        # This parameter is required.
        self.comment = comment
        # The parameters of the ticket.
        # 
        # This parameter is required.
        self.param_shrink = param_shrink
        # The stakeholders involved in this operation. All the specified stakeholders can view the ticket details and take part in the approval process. Irrelevant users other than DMS administrators and database administrators (DBAs) are not allowed to view the ticket details.
        self.related_user_list_shrink = related_user_list_shrink
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.param_shrink is not None:
            result['Param'] = self.param_shrink

        if self.related_user_list_shrink is not None:
            result['RelatedUserList'] = self.related_user_list_shrink

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('Param') is not None:
            self.param_shrink = m.get('Param')

        if m.get('RelatedUserList') is not None:
            self.related_user_list_shrink = m.get('RelatedUserList')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

