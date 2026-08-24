# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class CreateUsersRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        user: List[main_models.CreateUsersRequestUser] = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The list of users.
        self.user = user

    def validate(self):
        if self.user:
            for v1 in self.user:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        result['User'] = []
        if self.user is not None:
            for k1 in self.user:
                result['User'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        self.user = []
        if m.get('User') is not None:
            for k1 in m.get('User'):
                temp_model = main_models.CreateUsersRequestUser()
                self.user.append(temp_model.from_map(k1))

        return self

class CreateUsersRequestUser(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        group: str = None,
        password: str = None,
        user_name: str = None,
    ):
        # The public key of the Nth user to add.
        # 
        # Valid values of N: 1 to 20.
        # 
        # This parameter is mutually exclusive with the Password parameter. This parameter takes effect when the cluster authentication method is set to key (not recommended).
        self.auth_key = auth_key
        # The user group of the Nth user to add. Valid values:
        # 
        # - users: ordinary permission group. This group is suitable for regular users who only need to commit and debug jobs.
        # - wheel: sudo permission group. This group is suitable for administrators who need to perform cluster management. In addition to committing and debugging jobs, users in this group can execute sudo commands to install software, restart nodes, and perform other operations.
        # 
        # Valid values of N: 1 to 20.
        self.group = group
        # The password of the Nth user to add. The password must be 8 to 30 characters in length and contain at least three of the following four character types:
        # - Uppercase letters
        # - Lowercase letters
        # - Digits
        # - Special characters: ()~!@#$%^&*-_+=|{}[]:;\\"/<>,.?/
        # 
        # Valid values of N: 1 to 20.
        # 
        # This parameter is mutually exclusive with the AuthKey parameter. This parameter takes effect when the cluster authentication method is set to password (recommended).
        self.password = password
        # The username of the Nth user to add. The username must be 1 to 30 characters in length, start with a letter, and can contain digits and special characters (.).
        # 
        # Valid values of N: 1 to 20.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.group is not None:
            result['Group'] = self.group

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

