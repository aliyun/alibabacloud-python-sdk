# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetLhSpaceByNameRequest(DaraModel):
    def __init__(
        self,
        space_name: str = None,
        tid: int = None,
    ):
        # The name of the workspace.
        # 
        # This parameter is required.
        self.space_name = space_name
        # The ID of the tenant. You can call the [GetUserActiveTenant](https://help.aliyun.com/document_detail/198073.html) or [ListUserTenants](https://help.aliyun.com/document_detail/198074.html) operation to obtain the tenant ID.
        self.tid = tid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.space_name is not None:
            result['SpaceName'] = self.space_name

        if self.tid is not None:
            result['Tid'] = self.tid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SpaceName') is not None:
            self.space_name = m.get('SpaceName')

        if m.get('Tid') is not None:
            self.tid = m.get('Tid')

        return self

