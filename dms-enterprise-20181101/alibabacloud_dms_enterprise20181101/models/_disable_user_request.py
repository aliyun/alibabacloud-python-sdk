# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DisableUserRequest(DaraModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid
        # The UID of the Alibaba Cloud account.
        # 
        # This parameter is required.
        self.uid = uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tid is not None:
            result['Tid'] = self.tid

        if self.uid is not None:
            result['Uid'] = self.uid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        return self

