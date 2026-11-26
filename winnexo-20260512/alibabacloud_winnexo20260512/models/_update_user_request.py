# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        app_token: str = None,
        display_name: str = None,
        is_active: bool = None,
        ops_user_code: str = None,
        ops_user_id: str = None,
        role_codes: List[str] = None,
        tenant_id: str = None,
        user_group_ids: List[str] = None,
        wn_user_id: str = None,
    ):
        # The platform application token issued by the console. If specified, the operation is executed as the user identified by opsUserId or opsUserCode.
        self.app_token = app_token
        # The display name of the user.
        self.display_name = display_name
        # Specifies whether the account is activated. Valid values:
        # - **true**: Activated.
        # - **false**: Not activated.
        self.is_active = is_active
        # The proxy user code, which is unique within the tenant. This parameter is used only when the application credential is configured as source_uid.
        self.ops_user_code = ops_user_code
        # The proxy user ID, which is the WINNEXO platform user ID. This parameter is used only when the application credential is configured as winnexo_uid.
        self.ops_user_id = ops_user_id
        # The new list of system role codes. This list fully replaces the existing roles and must contain at least one role. Valid values: SUPER_ADMIN, SYSTEM_ADMIN, SEMANTIC_ADMIN, SKILL_ADMIN, KB_ADMIN, AGENT_ADMIN, and APPLICATION_USER.
        self.role_codes = role_codes
        # The ID of the effective tenant.
        self.tenant_id = tenant_id
        # The new list of user group IDs. This list fully replaces the existing user groups. If this parameter is not specified, the user groups are not modified.
        self.user_group_ids = user_group_ids
        # The ID of the target user, which is the WINNEXO platform user ID.
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
        if self.app_token is not None:
            result['appToken'] = self.app_token

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.ops_user_code is not None:
            result['opsUserCode'] = self.ops_user_code

        if self.ops_user_id is not None:
            result['opsUserId'] = self.ops_user_id

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.tenant_id is not None:
            result['tenantId'] = self.tenant_id

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appToken') is not None:
            self.app_token = m.get('appToken')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('opsUserCode') is not None:
            self.ops_user_code = m.get('opsUserCode')

        if m.get('opsUserId') is not None:
            self.ops_user_id = m.get('opsUserId')

        if m.get('roleCodes') is not None:
            self.role_codes = m.get('roleCodes')

        if m.get('tenantId') is not None:
            self.tenant_id = m.get('tenantId')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

