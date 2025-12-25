# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListAuthorizedUsersForDatabaseResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        users: List[main_models.ListAuthorizedUsersForDatabaseResponseBodyUsers] = None,
    ):
        # The request ID. You can use the ID to locate logs and troubleshoot issues.
        self.request_id = request_id
        # The list of users that have permissions on the specified instance.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListAuthorizedUsersForDatabaseResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListAuthorizedUsersForDatabaseResponseBodyUsers(DaraModel):
    def __init__(
        self,
        uid: str = None,
        user_id: str = None,
        user_nick_name: str = None,
    ):
        # The UID of the user\\"s Alibaba Cloud account.
        self.uid = uid
        # The user IDs.
        self.user_id = user_id
        # The nickname of the user.
        self.user_nick_name = user_nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.uid is not None:
            result['Uid'] = self.uid

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.user_nick_name is not None:
            result['UserNickName'] = self.user_nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('UserNickName') is not None:
            self.user_nick_name = m.get('UserNickName')

        return self

