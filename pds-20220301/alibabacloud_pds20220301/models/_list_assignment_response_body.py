# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_pds20220301 import models as main_models
from darabonba.model import DaraModel

class ListAssignmentResponseBody(DaraModel):
    def __init__(
        self,
        assignment_list: List[main_models.ListAssignmentResponseBodyAssignmentList] = None,
        next_marker: str = None,
    ):
        # The assigned roles.
        self.assignment_list = assignment_list
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.assignment_list:
            for v1 in self.assignment_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['assignment_list'] = []
        if self.assignment_list is not None:
            for k1 in self.assignment_list:
                result['assignment_list'].append(k1.to_map() if k1 else None)

        if self.next_marker is not None:
            result['next_marker'] = self.next_marker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignment_list = []
        if m.get('assignment_list') is not None:
            for k1 in m.get('assignment_list'):
                temp_model = main_models.ListAssignmentResponseBodyAssignmentList()
                self.assignment_list.append(temp_model.from_map(k1))

        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')

        return self

class ListAssignmentResponseBodyAssignmentList(DaraModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        domain_id: str = None,
        identity: main_models.Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
    ):
        # The time when the role was assigned. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The ID of the user who assigned the role.
        self.creator = creator
        # The domain ID.
        self.domain_id = domain_id
        # The identity to whom the role is assigned, which is a user or a group.
        self.identity = identity
        # The ID of the managed resource, such as a group ID.
        self.manage_resource_id = manage_resource_id
        # The type of the managed resource. For example, a value of RT_Group indicates group.
        self.manage_resource_type = manage_resource_type
        # The ID of the role assigned to the identity.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['created_at'] = self.created_at

        if self.creator is not None:
            result['creator'] = self.creator

        if self.domain_id is not None:
            result['domain_id'] = self.domain_id

        if self.identity is not None:
            result['identity'] = self.identity.to_map()

        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id

        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type

        if self.role_id is not None:
            result['role_id'] = self.role_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')

        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')

        if m.get('identity') is not None:
            temp_model = main_models.Identity()
            self.identity = temp_model.from_map(m.get('identity'))

        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')

        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')

        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')

        return self

