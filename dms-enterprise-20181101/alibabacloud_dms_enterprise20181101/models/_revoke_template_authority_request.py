# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RevokeTemplateAuthorityRequest(DaraModel):
    def __init__(
        self,
        template_id: int = None,
        tid: int = None,
        user_ids: str = None,
    ):
        # The ID of the permission template.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to query the tenant ID.
        self.tid = tid
        # The IDs of users from whom you want to revoke permissions by using a permission template.
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
        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.tid is not None:
            result['Tid'] = self.tid

        if self.user_ids is not None:
            result['UserIds'] = self.user_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')

        return self

