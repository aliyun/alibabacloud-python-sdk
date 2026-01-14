# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class BatchAddFeishuUsersRequest(DaraModel):
    def __init__(
        self,
        feishu_users: str = None,
        is_admin: bool = None,
        is_auth_admin: bool = None,
        user_group_ids: str = None,
        user_type: int = None,
    ):
        # Information of the users to be added
        self.feishu_users = feishu_users
        # Whether the user is an admin user:
        # - true
        # - false
        # 
        # Default is false if not provided
        self.is_admin = is_admin
        # Whether the user is an authorization administrator
        # 
        # - true
        # - false
        # 
        # Default is false if not provided
        self.is_auth_admin = is_auth_admin
        # User group ID(s)
        self.user_group_ids = user_group_ids
        # User type
        # - Developer: 1
        # - Visitor: 2
        # - Analyst: 3
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feishu_users is not None:
            result['FeishuUsers'] = self.feishu_users

        if self.is_admin is not None:
            result['IsAdmin'] = self.is_admin

        if self.is_auth_admin is not None:
            result['IsAuthAdmin'] = self.is_auth_admin

        if self.user_group_ids is not None:
            result['UserGroupIds'] = self.user_group_ids

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FeishuUsers') is not None:
            self.feishu_users = m.get('FeishuUsers')

        if m.get('IsAdmin') is not None:
            self.is_admin = m.get('IsAdmin')

        if m.get('IsAuthAdmin') is not None:
            self.is_auth_admin = m.get('IsAuthAdmin')

        if m.get('UserGroupIds') is not None:
            self.user_group_ids = m.get('UserGroupIds')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self

