# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserRequest(DaraModel):
    def __init__(
        self,
        cluster_id: str = None,
        group: str = None,
        password: str = None,
        user_name: str = None,
    ):
        # The cluster ID.
        # 
        # This parameter is required.
        self.cluster_id = cluster_id
        # The user group property to update. Valid values:
        # 
        # - users: ordinary permission group. This group is suitable for regular users who only need to submit and debug jobs.
        # 
        # - wheel: sudo permission group. This group is suitable for administrators who need cluster management. In addition to submitting and debugging jobs, users in this group can execute sudo commands to install software, restart nodes, and perform other operations.
        self.group = group
        # The user password property to update. The password must be 8 to 30 characters in length and must contain at least three of the following four character types:
        # 
        # - Uppercase letters
        # - Lowercase letters
        # - Digits
        # - Special characters: ()~!@#$%^&*-_+=|{}[]:;\\"/<>,.?/
        self.password = password
        # The username.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.group is not None:
            result['Group'] = self.group

        if self.password is not None:
            result['Password'] = self.password

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('Password') is not None:
            self.password = m.get('Password')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

