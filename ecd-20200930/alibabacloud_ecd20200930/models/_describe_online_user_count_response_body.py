# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeOnlineUserCountResponseBody(DaraModel):
    def __init__(
        self,
        ad_assigned_user_count: int = None,
        assigned_user_count: int = None,
        online_user_count: int = None,
        request_id: str = None,
        simple_assigned_user_count: int = None,
    ):
        self.ad_assigned_user_count = ad_assigned_user_count
        self.assigned_user_count = assigned_user_count
        self.online_user_count = online_user_count
        self.request_id = request_id
        self.simple_assigned_user_count = simple_assigned_user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ad_assigned_user_count is not None:
            result['AdAssignedUserCount'] = self.ad_assigned_user_count

        if self.assigned_user_count is not None:
            result['AssignedUserCount'] = self.assigned_user_count

        if self.online_user_count is not None:
            result['OnlineUserCount'] = self.online_user_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.simple_assigned_user_count is not None:
            result['SimpleAssignedUserCount'] = self.simple_assigned_user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AdAssignedUserCount') is not None:
            self.ad_assigned_user_count = m.get('AdAssignedUserCount')

        if m.get('AssignedUserCount') is not None:
            self.assigned_user_count = m.get('AssignedUserCount')

        if m.get('OnlineUserCount') is not None:
            self.online_user_count = m.get('OnlineUserCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SimpleAssignedUserCount') is not None:
            self.simple_assigned_user_count = m.get('SimpleAssignedUserCount')

        return self

