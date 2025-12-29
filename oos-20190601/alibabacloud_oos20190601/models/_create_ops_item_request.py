# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from darabonba.model import DaraModel

class CreateOpsItemRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        client_token: str = None,
        dedup_string: str = None,
        description: str = None,
        priority: int = None,
        region_id: str = None,
        resource_group_id: str = None,
        resources: str = None,
        severity: str = None,
        solutions: str = None,
        source: str = None,
        tags: Dict[str, Any] = None,
        title: str = None,
    ):
        # The category.
        # 
        # Valid values:
        # 
        # *   Availability
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Performance
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Security
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Cost
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Recovery
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.category = category
        # The client token that is used to ensure the idempotence of the request.
        self.client_token = client_token
        # The string to be deduplicated.
        self.dedup_string = dedup_string
        # The description of the operation.
        self.description = description
        # The priority. Valid values: 1 to 5. 1 indicates the highest priority.
        self.priority = priority
        # The region ID.
        self.region_id = region_id
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The Alibaba Cloud Resource Names (ARNs) of the associated resources.
        self.resources = resources
        # The severity level.
        # 
        # Valid values:
        # 
        # *   High
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Low
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Medium
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   Critical
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.severity = severity
        # The solutions.
        self.solutions = solutions
        # The source business.
        # 
        # This parameter is required.
        self.source = source
        # The tags.
        self.tags = tags
        # The title of the O\\&M item.
        # 
        # This parameter is required.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dedup_string is not None:
            result['DedupString'] = self.dedup_string

        if self.description is not None:
            result['Description'] = self.description

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        if self.resources is not None:
            result['Resources'] = self.resources

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.solutions is not None:
            result['Solutions'] = self.solutions

        if self.source is not None:
            result['Source'] = self.source

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DedupString') is not None:
            self.dedup_string = m.get('DedupString')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        if m.get('Resources') is not None:
            self.resources = m.get('Resources')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('Solutions') is not None:
            self.solutions = m.get('Solutions')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self

