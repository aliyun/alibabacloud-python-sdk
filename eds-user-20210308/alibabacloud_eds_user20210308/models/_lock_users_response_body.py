# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_user20210308 import models as main_models
from darabonba.model import DaraModel

class LockUsersResponseBody(DaraModel):
    def __init__(
        self,
        lock_users_result: main_models.LockUsersResponseBodyLockUsersResult = None,
        request_id: str = None,
    ):
        # The result of the locking the convenience user.
        self.lock_users_result = lock_users_result
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.lock_users_result:
            self.lock_users_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lock_users_result is not None:
            result['LockUsersResult'] = self.lock_users_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LockUsersResult') is not None:
            temp_model = main_models.LockUsersResponseBodyLockUsersResult()
            self.lock_users_result = temp_model.from_map(m.get('LockUsersResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class LockUsersResponseBodyLockUsersResult(DaraModel):
    def __init__(
        self,
        failed_users: List[main_models.LockUsersResponseBodyLockUsersResultFailedUsers] = None,
        locked_users: List[str] = None,
    ):
        # The convenience users that failed to be locked.
        self.failed_users = failed_users
        # The convenience users that were locked.
        self.locked_users = locked_users

    def validate(self):
        if self.failed_users:
            for v1 in self.failed_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedUsers'] = []
        if self.failed_users is not None:
            for k1 in self.failed_users:
                result['FailedUsers'].append(k1.to_map() if k1 else None)

        if self.locked_users is not None:
            result['LockedUsers'] = self.locked_users

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_users = []
        if m.get('FailedUsers') is not None:
            for k1 in m.get('FailedUsers'):
                temp_model = main_models.LockUsersResponseBodyLockUsersResultFailedUsers()
                self.failed_users.append(temp_model.from_map(k1))

        if m.get('LockedUsers') is not None:
            self.locked_users = m.get('LockedUsers')

        return self

class LockUsersResponseBodyLockUsersResultFailedUsers(DaraModel):
    def __init__(
        self,
        end_user_id: str = None,
        error_code: str = None,
        error_message: str = None,
    ):
        # The ID of the convenience user that failed to be locked.
        self.end_user_id = end_user_id
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self

