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
        # The users that you want to add.
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
        # The public key of the user.
        # 
        # You can add up to 20 users in a call.
        # 
        # Specify one of the Password and AuthKey parameters. The AuthKey parameter takes effect only when the cluster authentication method is set to Key. Key authentication is not recommended.
        self.auth_key = auth_key
        # The permission group to which the user belongs. Valid values:
        # 
        # users: ordinary permissions, which are suitable for ordinary users that need only to submit and debug jobs. wheel: sudo permissions, which are suitable for administrators who need to manage clusters. In addition to submitting and debugging jobs, you can also run sudo commands to install software and restart nodes. You can add up to 20 users in a call.
        self.group = group
        # The password of the user. The password must be 6 to 30 characters in length and must contain three of the following character types:
        # 
        # *   Uppercase letters
        # *   Lowercase letters
        # *   Digits
        # *   Special characters ()~!@#$%^&\\*-_+=|{}[]:;\\"/<>,.?/
        # 
        # You can add up to 20 users in a call.
        # 
        # Specify one of the Password and AuthKey parameters. The Password parameter takes effect only when the cluster authentication method is set to Password. Password authentication is recommended.
        self.password = password
        # The username. The username must be 1 to 30 characters in length. It must start with a letter and can contain digits, letters, and periods (.).
        # 
        # You can add up to 20 users in a call.
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

