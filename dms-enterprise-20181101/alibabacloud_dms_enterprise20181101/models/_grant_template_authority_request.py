# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GrantTemplateAuthorityRequest(DaraModel):
    def __init__(
        self,
        comment: str = None,
        expire_date: str = None,
        template_id: int = None,
        tid: int = None,
        user_ids: str = None,
    ):
        # The reason why you want to grant permissions on resources to the users by using the permission template.
        self.comment = comment
        # The time when the permission expires. Specify the time in the yyyy-MM-DD HH:mm:ss format.
        # 
        # This parameter is required.
        self.expire_date = expire_date
        # The ID of the permission template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid
        # The IDs of users to which you want to grant permissions on resources by using the permission template.
        # 
        # This parameter is required.
        self.user_ids = user_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['Comment'] = self.comment

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

