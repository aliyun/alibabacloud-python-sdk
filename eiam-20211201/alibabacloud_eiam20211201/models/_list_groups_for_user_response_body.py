# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListGroupsForUserResponseBody(DaraModel):
    def __init__(
        self,
        groups: List[main_models.ListGroupsForUserResponseBodyGroups] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The queried account groups.
        self.groups = groups
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned. The maximum number of entries returned at a time depends on the value of PageSize.
        self.total_count = total_count

    def validate(self):
        if self.groups:
            for v1 in self.groups:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Groups'] = []
        if self.groups is not None:
            for k1 in self.groups:
                result['Groups'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.groups = []
        if m.get('Groups') is not None:
            for k1 in m.get('Groups'):
                temp_model = main_models.ListGroupsForUserResponseBodyGroups()
                self.groups.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListGroupsForUserResponseBodyGroups(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_member_relation_source_id: str = None,
        group_member_relation_source_type: str = None,
    ):
        # The group ID.
        self.group_id = group_id
        # Account membership source ID
        self.group_member_relation_source_id = group_member_relation_source_id
        # Account membership source type
        self.group_member_relation_source_type = group_member_relation_source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_member_relation_source_id is not None:
            result['GroupMemberRelationSourceId'] = self.group_member_relation_source_id

        if self.group_member_relation_source_type is not None:
            result['GroupMemberRelationSourceType'] = self.group_member_relation_source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupMemberRelationSourceId') is not None:
            self.group_member_relation_source_id = m.get('GroupMemberRelationSourceId')

        if m.get('GroupMemberRelationSourceType') is not None:
            self.group_member_relation_source_type = m.get('GroupMemberRelationSourceType')

        return self

