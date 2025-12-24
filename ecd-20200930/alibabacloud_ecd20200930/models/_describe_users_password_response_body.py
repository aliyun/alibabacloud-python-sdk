# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeUsersPasswordResponseBody(DaraModel):
    def __init__(
        self,
        desktop_users: List[main_models.DescribeUsersPasswordResponseBodyDesktopUsers] = None,
        request_id: str = None,
    ):
        # The authorized users of the cloud computer.
        self.desktop_users = desktop_users
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.desktop_users:
            for v1 in self.desktop_users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['DesktopUsers'] = []
        if self.desktop_users is not None:
            for k1 in self.desktop_users:
                result['DesktopUsers'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.desktop_users = []
        if m.get('DesktopUsers') is not None:
            for k1 in m.get('DesktopUsers'):
                temp_model = main_models.DescribeUsersPasswordResponseBodyDesktopUsers()
                self.desktop_users.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUsersPasswordResponseBodyDesktopUsers(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        end_user_id: str = None,
        password: str = None,
    ):
        # The display name of the end user.
        self.display_name = display_name
        # The ID of the end user.
        self.end_user_id = end_user_id
        # The password of the end user.
        self.password = password

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.end_user_id is not None:
            result['EndUserId'] = self.end_user_id

        if self.password is not None:
            result['Password'] = self.password

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('EndUserId') is not None:
            self.end_user_id = m.get('EndUserId')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        return self

