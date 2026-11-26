# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class MarkTodosReadRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        mark_all_read: bool = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        tenant_id: str = None,
        todo_ids: List[str] = None,
    ):
        # The platform application token issued by the console. If you specify this parameter, the operation is performed as the user specified by opsUserId or opsUserCode.
        self.app_token = app_token
        # Specifies whether to mark all to-do items as read. This parameter takes precedence over todoIds.
        self.mark_all_read = mark_all_read
        # The code of the proxy user, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The ID of the proxy user, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The list of to-do IDs. You can specify up to 100 IDs. This parameter is ignored when markAllRead is set to true.
        self.tenant_id = tenant_id
        # The list of to-do IDs. You can specify up to 100 IDs. This parameter is ignored when markAllRead is set to true.
        self.todo_ids = todo_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.mark_all_read is not None:
            result['markAllRead'] = self.mark_all_read

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.todo_ids is not None:
            result['todoIds'] = self.todo_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('markAllRead') is not None:
            self.mark_all_read = m.get('markAllRead')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('todoIds') is not None:
            self.todo_ids = m.get('todoIds')

        return self

