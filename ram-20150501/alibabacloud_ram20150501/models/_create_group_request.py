# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        comments: str = None,
        group_name: str = None,
    ):
        # The description.
        # 
        # The value can be up to 128 characters in length.
        self.comments = comments
        # The name of the user group.
        # 
        # The name must be 1 to 64 characters in length and can contain letters, digits, periods (.), hyphens (-), and underscores (_).
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comments is not None:
            result['Comments'] = self.comments

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

