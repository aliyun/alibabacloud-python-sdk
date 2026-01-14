# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateUserGroupRequest(DaraModel):
    def __init__(
        self,
        user_group_description: str = None,
        user_group_id: str = None,
        user_group_name: str = None,
    ):
        # The description of the user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.user_group_description = user_group_description
        # The ID of the user group.
        # 
        # This parameter is required.
        self.user_group_id = user_group_id
        # The name of the user group.
        # 
        # *   Format verification: Maximum length 255
        # *   Special format verification: Chinese and English digits_ \\ / | () ] [
        self.user_group_name = user_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.user_group_description is not None:
            result['UserGroupDescription'] = self.user_group_description

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserGroupDescription') is not None:
            self.user_group_description = m.get('UserGroupDescription')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')

        return self

