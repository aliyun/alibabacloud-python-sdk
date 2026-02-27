# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetMemberDeletionPermissionRequest(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # Specifies whether to enable the member deletion feature. Valid values:
        # 
        # *   Enabled: enables the member deletion feature
        # *   Disabled: disables the member deletion feature
        # 
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

