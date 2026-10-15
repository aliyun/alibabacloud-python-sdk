# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class CreateUserInvitationCodeRequest(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        end_user_ids: List[str] = None,
        terminal_group_id: str = None,
        validity_minutes: int = None,
    ):
        # The logon identifier (EndUserId) of a single user, used for compatibility with single-user creation. You must specify either this parameter or EndUserIds, but not both. If neither is specified, PARAMETER_MISSING is returned. If both are specified, PARAM_ERROR is returned.
        self.end_user_id = end_user_id
        # The array of user logon identifiers (EndUserIds). You must specify either this parameter or EndUserId. You can specify 1 to 100 unique, non-empty strings at a time, and a code is generated for each user. If any user does not exist, USER_NOT_FOUND is returned. If the array is empty, or contains duplicate items, empty items, or non-string items, PARAM_ERROR is returned.
        self.end_user_ids = end_user_ids
        # The ID of the terminal group. The group must belong to the current account and must not be deleted. After the corresponding terminal uses the management code to complete management, it is added to this group. If the group does not exist, is deleted, or does not belong to the current account, TERMINAL_GROUP_NOT_FOUND is returned.
        # 
        # This parameter is required.
        self.terminal_group_id = terminal_group_id
        # The validity period of the management code, in minutes. A value of -1 indicates that the code is permanently valid. For values between 60 and 1440, only integer multiples of 60 (1 to 24 hours) are allowed. For values greater than 1440, only integer multiples of 1440 are allowed, up to a maximum of 12960 (2 to 9 days). Other values return PARAM_ERROR. The server calculates the validity period based on this duration.
        # 
        # This parameter is required.
        self.validity_minutes = validity_minutes

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.end_user_ids is not None:
            result['EndUserIds'] = self.end_user_ids

        if self.terminal_group_id is not None:
            result['TerminalGroupId'] = self.terminal_group_id

        if self.validity_minutes is not None:
            result['ValidityMinutes'] = self.validity_minutes

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('EndUserIds') is not None:
            self.end_user_ids = m.get('EndUserIds')

        if m.get('TerminalGroupId') is not None:
            self.terminal_group_id = m.get('TerminalGroupId')

        if m.get('ValidityMinutes') is not None:
            self.validity_minutes = m.get('ValidityMinutes')

        return self

