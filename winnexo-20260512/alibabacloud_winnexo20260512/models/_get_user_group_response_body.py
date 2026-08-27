# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from darabonba.model import DaraModel

class GetUserGroupResponseBody(DaraModel):
    def __init__(
        self,
        child_groups: List[Any] = None,
        code: str = None,
        members: List[Any] = None,
        message: str = None,
        parent_group: Any = None,
        request_id: str = None,
        user_group: Any = None,
    ):
        # **The list of direct child user groups.**
        self.child_groups = child_groups
        # The status code.
        self.code = code
        # **The list of direct members in the current user group.**
        self.members = members
        # The description of the status code.
        self.message = message
        # **The parent user group information. This is empty for the root node.**
        self.parent_group = parent_group
        # The request ID.
        self.request_id = request_id
        # **The target user group information.**
        self.user_group = user_group

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.child_groups is not None:
            result['childGroups'] = self.child_groups

        if self.code is not None:
            result['code'] = self.code

        if self.members is not None:
            result['members'] = self.members

        if self.message is not None:
            result['message'] = self.message

        if self.parent_group is not None:
            result['parentGroup'] = self.parent_group

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.user_group is not None:
            result['userGroup'] = self.user_group

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('childGroups') is not None:
            self.child_groups = m.get('childGroups')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('members') is not None:
            self.members = m.get('members')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('parentGroup') is not None:
            self.parent_group = m.get('parentGroup')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('userGroup') is not None:
            self.user_group = m.get('userGroup')

        return self

