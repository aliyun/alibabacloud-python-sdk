# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteUserRequest(DaraModel):
    def __init__(
        self,
        tid: int = None,
        uid: str = None,
    ):
        # The ID of the tenant. 
        # 
        # >  To view the ID of the tenant, move the pointer over the profile picture in the upper-right corner of the DMS console. For more information, see the "View information about the current tenant" section of the [Manage DMS tenants](https://www.alibabacloud.com/help/en/data-management-service/latest/manage-dms-tenants) topic.
        self.tid = tid
        # The unique ID (UID) of Alibaba Cloud account to delete.
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

