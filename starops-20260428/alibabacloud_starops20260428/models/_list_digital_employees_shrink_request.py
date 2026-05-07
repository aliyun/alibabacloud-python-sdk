# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListDigitalEmployeesShrinkRequest(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        employee_type: str = None,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        resource_group_id: str = None,
        tags_shrink: str = None,
    ):
        self.display_name = display_name
        self.employee_type = employee_type
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        self.resource_group_id = resource_group_id
        self.tags_shrink = tags_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.employee_type is not None:
            result['employeeType'] = self.employee_type

        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.name is not None:
            result['name'] = self.name

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.resource_group_id is not None:
            result['resourceGroupId'] = self.resource_group_id

        if self.tags_shrink is not None:
            result['tags'] = self.tags_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('employeeType') is not None:
            self.employee_type = m.get('employeeType')

        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('resourceGroupId') is not None:
            self.resource_group_id = m.get('resourceGroupId')

        if m.get('tags') is not None:
            self.tags_shrink = m.get('tags')

        return self

