# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class EnableConversationShareRequest(DaraModel):
    def __init__(
        self,
        session_id: str = None,
        share_access_type: str = None,
        share_user_group_ids: List[str] = None,
        share_user_ids: List[int] = None,
        tenant_id: str = None,
    ):
        # The unique identifier of the function session.
        # 
        # This parameter is required.
        self.session_id = session_id
        # The sharing scope. Valid values:
        # - PUBLIC: accessible to all users
        # - SPECIFIED: accessible to specified users or user groups
        self.share_access_type = share_access_type
        # The list of user group IDs for the specified scope. When shareAccessType is set to SPECIFIED, at least one of this list or the user list must not be empty.
        self.share_user_group_ids = share_user_group_ids
        # The list of platform user IDs for the specified scope. When shareAccessType is set to SPECIFIED, at least one of this list or the user group list must not be empty.
        self.share_user_ids = share_user_ids
        # The tenant ID.
        self.tenant_id = tenant_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.session_id is not None:
            result['sessionId'] = self.session_id

        if self.share_access_type is not None:
            result['shareAccessType'] = self.share_access_type

        if self.share_user_group_ids is not None:
            result['shareUserGroupIds'] = self.share_user_group_ids

        if self.share_user_ids is not None:
            result['shareUserIds'] = self.share_user_ids

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')

        if m.get('shareAccessType') is not None:
            self.share_access_type = m.get('shareAccessType')

        if m.get('shareUserGroupIds') is not None:
            self.share_user_group_ids = m.get('shareUserGroupIds')

        if m.get('shareUserIds') is not None:
            self.share_user_ids = m.get('shareUserIds')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        return self

