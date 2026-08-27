# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class GetUserResponseBody(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        code: str = None,
        display_name: str = None,
        gmt_create: str = None,
        is_active: bool = None,
        last_login_time: str = None,
        message: str = None,
        request_id: str = None,
        role_codes: List[str] = None,
        user_group_ids: List[str] = None,
        wn_user_id: str = None,
    ):
        # The account ID.
        self.account_id = account_id
        # The error code.
        self.code = code
        # The display name of the account.
        self.display_name = display_name
        # The creation time.
        self.gmt_create = gmt_create
        # Indicates whether the account is activated. Valid values:
        #  - **true**: Activated.
        # - **false**: Not activated.
        self.is_active = is_active
        # The last logon time.
        self.last_login_time = last_login_time
        # The status code description.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The list of system role codes (full replacement, must contain at least one role). Valid values: SUPER_ADMIN, SYSTEM_ADMIN, SEMANTIC_ADMIN, SKILL_ADMIN, KB_ADMIN, AGENT_ADMIN, and APPLICATION_USER.
        self.role_codes = role_codes
        # The list of user group IDs to which the user belongs.
        self.user_group_ids = user_group_ids
        # The WINNEXO platform user ID.
        self.wn_user_id = wn_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['accountId'] = self.account_id

        if self.code is not None:
            result['code'] = self.code

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.is_active is not None:
            result['isActive'] = self.is_active

        if self.last_login_time is not None:
            result['lastLoginTime'] = self.last_login_time

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.role_codes is not None:
            result['roleCodes'] = self.role_codes

        if self.user_group_ids is not None:
            result['userGroupIds'] = self.user_group_ids

        if self.wn_user_id is not None:
            result['wnUserId'] = self.wn_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accountId') is not None:
            self.account_id = m.get('accountId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        if m.get('lastLoginTime') is not None:
            self.last_login_time = m.get('lastLoginTime')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('roleCodes') is not None:
            self.role_codes = m.get('roleCodes')

        if m.get('userGroupIds') is not None:
            self.user_group_ids = m.get('userGroupIds')

        if m.get('wnUserId') is not None:
            self.wn_user_id = m.get('wnUserId')

        return self

