# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListGroupMemberRequest(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        limit: int = None,
        marker: str = None,
        member_type: str = None,
    ):
        # The ID of the group of which you want to query members.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The member type. If you do not specify this parameter, both types of members are returned. Valid values:
        # 
        # *   user
        # *   group
        # 
        # Note: A group can be a member of only one group. It cannot be a member of multiple groups. A user can be a member of multiple groups.
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['group_id'] = self.group_id

        if self.limit is not None:
            result['limit'] = self.limit

        if self.marker is not None:
            result['marker'] = self.marker

        if self.member_type is not None:
            result['member_type'] = self.member_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')

        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')

        return self

