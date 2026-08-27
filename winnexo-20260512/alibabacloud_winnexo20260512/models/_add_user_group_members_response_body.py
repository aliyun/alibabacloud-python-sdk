# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddUserGroupMembersResponseBody(DaraModel):
    def __init__(
        self,
        affected_count: int = None,
        code: str = None,
        message: str = None,
        request_id: str = None,
        requested_count: int = None,
        user_group_id: str = None,
    ):
        # The number of user group member relationships that were actually added.
        self.affected_count = affected_count
        # The status code.
        self.code = code
        # The description of the status code.
        self.message = message
        # The request trace ID.
        self.request_id = request_id
        # The number of requested members before deduplication.
        self.requested_count = requested_count
        # The ID of the target user group.
        self.user_group_id = user_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affected_count is not None:
            result['affectedCount'] = self.affected_count

        if self.code is not None:
            result['code'] = self.code

        if self.message is not None:
            result['message'] = self.message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.requested_count is not None:
            result['requestedCount'] = self.requested_count

        if self.user_group_id is not None:
            result['userGroupId'] = self.user_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('affectedCount') is not None:
            self.affected_count = m.get('affectedCount')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('message') is not None:
            self.message = m.get('message')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('requestedCount') is not None:
            self.requested_count = m.get('requestedCount')

        if m.get('userGroupId') is not None:
            self.user_group_id = m.get('userGroupId')

        return self

