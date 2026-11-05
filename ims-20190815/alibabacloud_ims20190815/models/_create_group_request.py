# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateGroupRequest(DaraModel):
    def __init__(
        self,
        comments: str = None,
        display_name: str = None,
        group_name: str = None,
    ):
        # The comments.
        # 
        # The maximum length is 128 characters.
        self.comments = comments
        # The display name of the user group.
        # 
        # The maximum length is 24 characters.
        self.display_name = display_name
        # The name of the user group. This parameter is required.
        # 
        # The maximum length is 64 characters. It can contain letters, digits, periods (.), underscores (_), and hyphens (-).
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

        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Comments') is not None:
            self.comments = m.get('Comments')

        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self

