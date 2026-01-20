# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AssociateResourceSharePermissionRequest(DaraModel):
    def __init__(
        self,
        permission_name: str = None,
        replace: bool = None,
        resource_share_id: str = None,
    ):
        # The name of the permission.
        # 
        # This parameter is required.
        self.permission_name = permission_name
        # Specifies whether to use the specified permission to replace an existing permission. Valid values:
        # 
        # *   false: does not use the specified permission to replace an existing permission. This is the default value. If you set the value to false for a resource share that does not have associated permissions, the system associates the specified permission with the resource share. In a resource share, one resource type can have only one permission. If you set the value to false for a resource share that already has a permission for the resource type indicated by the specified permission, the system reports an error. This prevents you from replacing the existing permission by mistake.
        # *   true: uses the specified permission to replace an existing permission of the same resource type.
        self.replace = replace
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name

        if self.replace is not None:
            result['Replace'] = self.replace

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')

        if m.get('Replace') is not None:
            self.replace = m.get('Replace')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        return self

