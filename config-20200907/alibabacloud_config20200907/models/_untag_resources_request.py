# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UntagResourcesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        region_id: str = None,
        resource_id: List[str] = None,
        resource_type: str = None,
        tag_key: List[str] = None,
    ):
        # Specifies whether to detach all tags from the resources. Valid values:
        # 
        # - true: Detach all tags from the resources.
        # 
        # - false (default): Detach the specified tags.
        self.all = all
        # The ID of the region.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The IDs of the resources. You can specify a maximum of 50 resource IDs.
        # 
        # You can detach tags from up to 50 resources at a time.
        # 
        # This parameter is required.
        self.resource_id = resource_id
        # The type of the CloudConfig resource. Valid values:
        # 
        # - `ACS::Config::Rule`: a rule for a single account.
        # 
        # - `ACS::Config::AggregateConfigRule`: a rule for multiple accounts.
        # 
        # - `ACS::Config::Aggregator`: an account group.
        # 
        # - `ACS::Config::CompliancePack`: a compliance package for a single account.
        # 
        # - `ACS::Config::AggregateCompliancePack`: a compliance package for multiple accounts.
        # 
        # This parameter is required.
        self.resource_type = resource_type
        # The tag keys of the tags to detach.
        self.tag_key = tag_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['All'] = self.all

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        return self

