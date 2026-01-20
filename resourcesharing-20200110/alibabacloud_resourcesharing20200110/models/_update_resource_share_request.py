# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateResourceShareRequest(DaraModel):
    def __init__(
        self,
        allow_external_targets: bool = None,
        resource_share_id: str = None,
        resource_share_name: str = None,
    ):
        # Specifies whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets
        # The ID of the resource share.
        # 
        # This parameter is required.
        self.resource_share_id = resource_share_id
        # The new name of the resource share.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # The name can contain letters, digits, periods (.), underscores (_), and hyphens (-).
        # 
        # This parameter is required.
        self.resource_share_name = resource_share_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets

        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id

        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')

        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')

        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')

        return self

