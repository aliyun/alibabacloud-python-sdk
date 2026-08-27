# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserShrinkRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        is_active: bool = None,
        role_codes_shrink: str = None,
        tenant_id: str = None,
        user_group_ids_shrink: str = None,
        wn_user_id: str = None,
    ):
        # The display name of the user.
        self.display_name = display_name
        # Specifies whether the account is activated. Valid values:
        #  - **true**: Activated.
        # - **false**: Not activated.
        self.is_active = is_active
        # The new list of system role codes (full replacement, must contain at least one role). Valid values: SUPER_ADMIN / SYSTEM_ADMIN / SEMANTIC_ADMIN / SKILL_ADMIN / KB_ADMIN / AGENT_ADMIN / APPLICATION_USER.
        self.role_codes_shrink = role_codes_shrink
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The new list of user group IDs (full replacement. If not specified, the value is not modified).
        self.user_group_ids_shrink = user_group_ids_shrink
        # The ID of the target user (WINNEXO platform user ID).
        # 
        # This parameter is required.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.role_codes_shrink is not None:
            result['roleCodes'] = self.role_codes_shrink

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids_shrink is not None:
            result['userGroupIds'] = self.user_group_ids_shrink

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('roleCodes') is not None:
            self.role_codes_shrink = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids_shrink = m.get('userGroupIds')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

