# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class RemoveUsersRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        unbind_desktops: bool = None,
        users: List[str] = None,
    ):
        # The business channel.
        self.business_channel = business_channel
        # Specifies whether to automatically revoke cloud desktop authorization before deleting convenience users. Valid values:
        # 
        # - true: Asynchronously revokes cloud desktop authorization and deletes convenience users. The API returns the task acceptance result.
        # - false (default): Synchronously deletes convenience users without automatically revoking cloud desktop authorization. If associated resources prevent deletion, a deletion failure is returned.
        # 
        # When this parameter is set to true, the caller must also have the ecd:ModifyUserEntitlement permission. Task acceptance does not mean that the convenience users have been deleted.
        self.unbind_desktops = unbind_desktops
        # The list of usernames of the convenience users to be deleted.
        # 
        # This parameter is required.
        self.users = users

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

        if self.unbind_desktops is not None:
            result['UnbindDesktops'] = self.unbind_desktops

        if self.users is not None:
            result['Users'] = self.users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

        if m.get('UnbindDesktops') is not None:
            self.unbind_desktops = m.get('UnbindDesktops')

        if m.get('Users') is not None:
            self.users = m.get('Users')

        return self

