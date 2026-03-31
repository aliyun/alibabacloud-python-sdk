# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class TagResourcesShrinkRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_shrink: str = None,
    ):
        # The region ID of the tags.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The resource IDs. You can add tags to up to 50 resources.
        # 
        # This parameter is required.
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
        # The tag value of the resource.
        # 
        # You can specify up to 20 tag values.
        # 
        # This parameter is required.
        self.tag_shrink = tag_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('Tag') is not None:
            self.tag_shrink = m.get('Tag')

        return self

