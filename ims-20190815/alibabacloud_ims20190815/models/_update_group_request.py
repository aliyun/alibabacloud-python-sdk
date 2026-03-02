# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGroupRequest(DaraModel):
    def __init__(
        self,
        group_name: str = None,
        new_comments: str = None,
        new_display_name: str = None,
        new_group_name: str = None,
    ):
        self.group_name = group_name
        self.new_comments = new_comments
        self.new_display_name = new_display_name
        self.new_group_name = new_group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_name is not None:
            result['GroupName'] = self.group_name

        if self.new_comments is not None:
            result['NewComments'] = self.new_comments

        if self.new_display_name is not None:
            result['NewDisplayName'] = self.new_display_name

        if self.new_group_name is not None:
            result['NewGroupName'] = self.new_group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        if m.get('NewComments') is not None:
            self.new_comments = m.get('NewComments')

        if m.get('NewDisplayName') is not None:
            self.new_display_name = m.get('NewDisplayName')

        if m.get('NewGroupName') is not None:
            self.new_group_name = m.get('NewGroupName')

        return self

