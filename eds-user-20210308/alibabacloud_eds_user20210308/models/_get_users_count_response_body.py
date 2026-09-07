# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetUsersCountResponseBody(DaraModel):
    def __init__(
        self,
        group_count: int = None,
        max_user_number: int = None,
        org_count: int = None,
        request_id: str = None,
        user_count: int = None,
    ):
        self.group_count = group_count
        self.max_user_number = max_user_number
        self.org_count = org_count
        self.request_id = request_id
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_count is not None:
            result['GroupCount'] = self.group_count

        if self.max_user_number is not None:
            result['MaxUserNumber'] = self.max_user_number

        if self.org_count is not None:
            result['OrgCount'] = self.org_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.user_count is not None:
            result['UserCount'] = self.user_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupCount') is not None:
            self.group_count = m.get('GroupCount')

        if m.get('MaxUserNumber') is not None:
            self.max_user_number = m.get('MaxUserNumber')

        if m.get('OrgCount') is not None:
            self.org_count = m.get('OrgCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UserCount') is not None:
            self.user_count = m.get('UserCount')

        return self

