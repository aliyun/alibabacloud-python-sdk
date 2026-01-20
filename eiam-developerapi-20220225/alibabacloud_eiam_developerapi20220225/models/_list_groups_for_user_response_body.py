# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam_developerapi20220225 import models as main_models
from darabonba.model import DaraModel

class ListGroupsForUserResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListGroupsForUserResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        total_count: int = None,
    ):
        self.data = data
        self.max_results = max_results
        self.next_token = next_token
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListGroupsForUserResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListGroupsForUserResponseBodyData(DaraModel):
    def __init__(
        self,
        group_id: str = None,
        group_member_relation_source_id: str = None,
        group_member_relation_source_type: str = None,
        instance_id: str = None,
    ):
        self.group_id = group_id
        self.group_member_relation_source_id = group_member_relation_source_id
        self.group_member_relation_source_type = group_member_relation_source_type
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['groupId'] = self.group_id

        if self.group_member_relation_source_id is not None:
            result['groupMemberRelationSourceId'] = self.group_member_relation_source_id

        if self.group_member_relation_source_type is not None:
            result['groupMemberRelationSourceType'] = self.group_member_relation_source_type

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('groupId') is not None:
            self.group_id = m.get('groupId')

        if m.get('groupMemberRelationSourceId') is not None:
            self.group_member_relation_source_id = m.get('groupMemberRelationSourceId')

        if m.get('groupMemberRelationSourceType') is not None:
            self.group_member_relation_source_type = m.get('groupMemberRelationSourceType')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        return self

