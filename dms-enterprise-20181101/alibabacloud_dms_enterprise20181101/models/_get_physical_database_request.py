# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPhysicalDatabaseRequest(DaraModel):
    def __init__(
        self,
        db_id: int = None,
        tid: int = None,
    ):
        # The ID of the physical database. You can call the [SearchDatabase](https://help.aliyun.com/document_detail/141876.html) operation to obtain the ID.
        # 
        # This parameter is required.
        self.db_id = db_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) operation to query the ID of the tenant.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.db_id is not None:
            result['DbId'] = self.db_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DbId') is not None:
            self.db_id = m.get('DbId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

