# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetPermissionRequest(DaraModel):
    def __init__(
        self,
        permission_name: str = None,
        permission_version: str = None,
    ):
        # The name of the permission.
        # 
        # This parameter is required.
        self.permission_name = permission_name
        # The version of the permission.
        self.permission_version = permission_version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name

        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')

        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')

        return self

