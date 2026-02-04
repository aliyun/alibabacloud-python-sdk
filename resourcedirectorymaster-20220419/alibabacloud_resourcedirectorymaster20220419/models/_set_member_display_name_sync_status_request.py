# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetMemberDisplayNameSyncStatusRequest(DaraModel):
    def __init__(
        self,
        status: str = None,
    ):
        # The status of the Member Display Name Synchronization feature. Valid values:
        # 
        # *   Enabled: The feature is enabled. This indicates that the display names specified by the management account for the members will be synchronized to the basic account information of the members. The display name information will be visible and perceptible to the members. If a notification is sent to a member, the display name of the member will be used as the appellation of the member.
        # *   Disabled: The feature is disabled. This indicates that the display names specified by the management account for the members are valid only in the resource directory and will not be updated to the basic account information of the members.
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

