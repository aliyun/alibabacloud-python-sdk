# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserStatusRequest(DaraModel):
    def __init__(
        self,
        directory_id: str = None,
        new_status: str = None,
        user_id: str = None,
    ):
        # The ID of the directory.
        self.directory_id = directory_id
        # The new status of the user. Valid values:
        # 
        # - Enabled: The logon of the user is enabled.
        # 
        # - Disabled: The logon of the user is disabled.
        self.new_status = new_status
        # The ID of the user.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.directory_id is not None:
            result['DirectoryId'] = self.directory_id

        if self.new_status is not None:
            result['NewStatus'] = self.new_status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DirectoryId') is not None:
            self.directory_id = m.get('DirectoryId')

        if m.get('NewStatus') is not None:
            self.new_status = m.get('NewStatus')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

