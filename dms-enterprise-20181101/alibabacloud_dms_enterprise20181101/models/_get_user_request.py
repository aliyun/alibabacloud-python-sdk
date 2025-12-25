# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUserRequest(DaraModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
        user_id: str = None,
    ):
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to obtain the tenant ID.
        self.tid = tid
        # The UID of the Alibaba Cloud account. You can view your UID by moving the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console.
        self.uid = uid
        # The ID of the user. You can call the [ListUsers](https://help.aliyun.com/document_detail/141938.html) operation to query the ID of the user.
        self.user_id = user_id

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

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

