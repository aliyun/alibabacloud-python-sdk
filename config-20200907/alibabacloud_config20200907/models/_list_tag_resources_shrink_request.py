# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        # The pagination token that is used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The region ID of the tag.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource ID.
        # 
        # You can add tags to up to 50 resources.
        self.resource_id = resource_id
        # The resource type. Valid values:
        # 
        # *   `ACS::Config::Rule`
        # *   `ACS::Config::AggregateConfigRule`
        # *   `ACS::Config::Aggregator`
        # *   `ACS::Config::CompliancePack`
        # *   `ACS::Config::AggregateCompliancePack`
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tags of the resource.
        # 
        # You can add up to 20 tags to a resource.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_shrink is not None:
            result['Tag'] = self.tag_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

