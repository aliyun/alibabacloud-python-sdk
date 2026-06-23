# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListPendingApprovalsShrinkRequest(DaraModel):
    def __init__(
        self,
        access_types_shrink: str = None,
        def_schema: str = None,
        end_time: int = None,
        grantee_shrink: str = None,
        next_token: str = None,
        page_size: int = None,
        resource_shrink: str = None,
        resource_type_shrink: str = None,
        start_time: int = None,
    ):
        # The access types.
        self.access_types_shrink = access_types_shrink
        # The resource schema type.
        # 
        # This parameter is required.
        self.def_schema = def_schema
        # The end time of the query range, specified as a Unix timestamp in milliseconds.
        self.end_time = end_time
        # The grantee object used to filter results.
        self.grantee_shrink = grantee_shrink
        # The token used to retrieve the next page of results.
        self.next_token = next_token
        # The number of entries to return per page. Default: 10. Maximum: 200.
        self.page_size = page_size
        # The criteria to filter resources.
        self.resource_shrink = resource_shrink
        # The resource type, which corresponds to a leaf node name. You can specify multiple values. A business context can map to multiple leaf node names.
        # 
        # This parameter is required.
        self.resource_type_shrink = resource_type_shrink
        # The start time of the query range, specified as a Unix timestamp in milliseconds.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_types_shrink is not None:
            result['AccessTypes'] = self.access_types_shrink

        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.grantee_shrink is not None:
            result['Grantee'] = self.grantee_shrink

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.resource_shrink is not None:
            result['Resource'] = self.resource_shrink

        if self.resource_type_shrink is not None:
            result['ResourceType'] = self.resource_type_shrink

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessTypes') is not None:
            self.access_types_shrink = m.get('AccessTypes')

        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Grantee') is not None:
            self.grantee_shrink = m.get('Grantee')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('Resource') is not None:
            self.resource_shrink = m.get('Resource')

        if m.get('ResourceType') is not None:
            self.resource_type_shrink = m.get('ResourceType')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

