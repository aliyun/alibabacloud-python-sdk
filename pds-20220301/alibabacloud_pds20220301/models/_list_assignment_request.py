# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAssignmentRequest(DaraModel):
    def __init__(
        self,
        limit: int = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The ID of the managed resource, such as a group ID.
        # 
        # This parameter is required.
        self.manage_resource_id = manage_resource_id
        # The type of the managed resource. Set the value to RT_Group, which specifies that the administrators of a group are queried.
        # 
        # This parameter is required.
        self.manage_resource_type = manage_resource_type
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.limit is not None:
            result['limit'] = self.limit

        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id

        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type

        if self.marker is not None:
            result['marker'] = self.marker

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')

        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')

        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        return self

