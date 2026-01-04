# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListUsersForGroupResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        total_count: int = None,
        users: List[main_models.ListUsersForGroupResponseBodyUsers] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned. The maximum number of entries that can be returned per page is specified by PageSize.
        self.total_count = total_count
        # The information about accounts.
        self.users = users

    def validate(self):
        if self.users:
            for v1 in self.users:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['Users'] = []
        if self.users is not None:
            for k1 in self.users:
                result['Users'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.users = []
        if m.get('Users') is not None:
            for k1 in m.get('Users'):
                temp_model = main_models.ListUsersForGroupResponseBodyUsers()
                self.users.append(temp_model.from_map(k1))

        return self

class ListUsersForGroupResponseBodyUsers(DaraModel):
    def __init__(
        self,
        group_member_relation_source_id: str = None,
        group_member_relation_source_type: str = None,
        user_id: str = None,
    ):
        # Account membership source id
        self.group_member_relation_source_id = group_member_relation_source_id
        # Account membership source type
        self.group_member_relation_source_type = group_member_relation_source_type
        # The account ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_member_relation_source_id is not None:
            result['GroupMemberRelationSourceId'] = self.group_member_relation_source_id

        if self.group_member_relation_source_type is not None:
            result['GroupMemberRelationSourceType'] = self.group_member_relation_source_type

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupMemberRelationSourceId') is not None:
            self.group_member_relation_source_id = m.get('GroupMemberRelationSourceId')

        if m.get('GroupMemberRelationSourceType') is not None:
            self.group_member_relation_source_type = m.get('GroupMemberRelationSourceType')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

