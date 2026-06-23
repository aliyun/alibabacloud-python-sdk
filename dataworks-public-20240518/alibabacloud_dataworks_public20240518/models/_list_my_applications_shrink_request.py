# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListMyApplicationsShrinkRequest(DaraModel):
    def __init__(
        self,
        def_schema: str = None,
        end_time: int = None,
        next_token: str = None,
        page_size: int = None,
        resource_shrink: str = None,
        resource_type_shrink: str = None,
        start_time: int = None,
        statuses_shrink: str = None,
    ):
        # The resource type.
        # 
        # This parameter is required.
        self.def_schema = def_schema
        # The end time of the application, specified as a Unix timestamp in milliseconds.
        # 
        # This parameter is required.
        self.end_time = end_time
        # A token that you can use in a subsequent request to retrieve the next page of results.
        self.next_token = next_token
        # The number of entries to return on each page. Default value: 10. Maximum value: 200.
        self.page_size = page_size
        # The search criteria for the resource.
        self.resource_shrink = resource_shrink
        # The name of the leaf node that specifies the resource type. You can specify multiple resource types. Note that different leaf node names can map to the same business logic.
        # 
        # This parameter is required.
        self.resource_type_shrink = resource_type_shrink
        # The start time of the application, specified as a Unix timestamp in milliseconds.
        # 
        # This parameter is required.
        self.start_time = start_time
        # The approval statuses for filtering. Valid values:
        # 
        # - `WaitApproval`: Pending approval
        # 
        # - `Confirmed`: Pending authorization
        # 
        # - `RejectApproval`: Approval rejected
        # 
        # - `AuthorizeSucceed`: Authorization succeeded
        # 
        # - `AuthorizeFailed`: Authorization failed
        # 
        # - `Deleted`: The application was deleted.
        # 
        # - `Canceled`: The application was canceled.
        self.statuses_shrink = statuses_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.def_schema is not None:
            result['DefSchema'] = self.def_schema

        if self.end_time is not None:
            result['EndTime'] = self.end_time

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

        if self.statuses_shrink is not None:
            result['Statuses'] = self.statuses_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefSchema') is not None:
            self.def_schema = m.get('DefSchema')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

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

        if m.get('Statuses') is not None:
            self.statuses_shrink = m.get('Statuses')

        return self

