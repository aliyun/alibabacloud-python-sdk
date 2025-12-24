# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyDesktopOversoldUserGroupRequest(DaraModel):
    def __init__(
        self,
        image_id: str = None,
        name: str = None,
        oversold_group_id: str = None,
        policy_group_id: str = None,
        user_group_id: str = None,
    ):
        self.image_id = image_id
        self.name = name
        self.oversold_group_id = oversold_group_id
        self.policy_group_id = policy_group_id
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.name is not None:
            result['Name'] = self.name

        if self.oversold_group_id is not None:
            result['OversoldGroupId'] = self.oversold_group_id

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OversoldGroupId') is not None:
            self.oversold_group_id = m.get('OversoldGroupId')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')

        return self

