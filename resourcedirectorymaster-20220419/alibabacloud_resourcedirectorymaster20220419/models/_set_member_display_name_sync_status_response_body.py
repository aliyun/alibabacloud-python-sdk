# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetMemberDisplayNameSyncStatusResponseBody(DaraModel):
    def __init__(
        self,
        member_account_display_name_sync_status: str = None,
        request_id: str = None,
    ):
        # The status of the Member Display Name Synchronization feature. Valid values:
        # 
        # *   Enabled
        # *   Disabled
        self.member_account_display_name_sync_status = member_account_display_name_sync_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.member_account_display_name_sync_status is not None:
            result['MemberAccountDisplayNameSyncStatus'] = self.member_account_display_name_sync_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MemberAccountDisplayNameSyncStatus') is not None:
            self.member_account_display_name_sync_status = m.get('MemberAccountDisplayNameSyncStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

