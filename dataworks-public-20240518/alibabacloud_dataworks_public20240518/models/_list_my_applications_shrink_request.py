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
        # Filters by resource type.
        # 
        # Note: The resource types supported by the system for applications are constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).name.
        # 
        # See also: [ResourceSchema documentation for International site](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        # 
        # This parameter is required.
        self.def_schema = def_schema
        # The end time of the application period (millisecond timestamp).
        # 
        # This parameter is required.
        self.end_time = end_time
        # The pagination cursor.
        self.next_token = next_token
        # The number of entries per page. Default value: 10. Maximum value: 200.
        self.page_size = page_size
        # Filters by resource with exact or wildcard matching. The resource description is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).
        # 
        # See also: [ResourceSchema documentation for International site](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        self.resource_shrink = resource_shrink
        # Filters by minimum permission resource type.
        # 
        # Note: The minimum permission resource type is constrained by [ResourceSchema](https://help.aliyun.com/zh/dataworks/developer-reference/resourceschema-template-instructions).resources[*].isValidLeaf being true.
        # 
        # See also: [ResourceSchema documentation for International site](https://www.alibabacloud.com/help/zh/dataworks/developer-reference/resourceschema-template-instructions)
        # 
        # This parameter is required.
        self.resource_type_shrink = resource_type_shrink
        # The start time of the application period (millisecond timestamp).
        # 
        # This parameter is required.
        self.start_time = start_time
        # Filters by approval status. Valid values:
        # 
        # - WaitApproval: pending approval.
        # - Confirmed: pending authorization.
        # - RejectApproval: approval rejected.
        # - AuthorizeSucceed: authorization succeeded.
        # - AuthorizeFailed: authorization failed.
        # - Deleted: deleted.
        # - Canceled: withdrawn.
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

