# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class EnableUserRequest(DaraModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        # The ID of the tenant.
        # 
        # >  To obtain the tenant ID, move the pointer over the profile picture in the upper-right corner of the Data Management (DMS) console. For more information, see [Tenant information](https://help.aliyun.com/document_detail/181330.html).
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

