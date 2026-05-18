# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BindVscMountPointAliasResponseBody(DaraModel):
    def __init__(
        self,
        mount_point_alias: str = None,
        request_id: str = None,
    ):
        self.mount_point_alias = mount_point_alias
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mount_point_alias is not None:
            result['MountPointAlias'] = self.mount_point_alias

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MountPointAlias') is not None:
            self.mount_point_alias = m.get('MountPointAlias')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

