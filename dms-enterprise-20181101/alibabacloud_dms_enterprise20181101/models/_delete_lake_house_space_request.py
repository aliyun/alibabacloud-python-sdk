# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteLakeHouseSpaceRequest(DaraModel):
    def __init__(
        self,
        space_id: int = None,
        tid: int = None,
    ):
        # The ID of the workspace. You can call the [GetLhSpaceByName](https://help.aliyun.com/document_detail/424379.html) operation to obtain the workspace ID.
        # 
        # This parameter is required.
        self.space_id = space_id
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.space_id is not None:
            result['SpaceId'] = self.space_id

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceId') is not None:
            self.space_id = m.get('SpaceId')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

