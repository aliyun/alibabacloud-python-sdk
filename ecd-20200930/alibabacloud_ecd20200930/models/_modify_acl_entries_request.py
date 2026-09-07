# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyAclEntriesRequest(DaraModel):
    def __init__(
        self,
        policy: str = None,
        region_id: str = None,
        source_id: List[str] = None,
        source_type: str = None,
    ):
        # The public network access control policy.
        # 
        # This parameter is required.
        self.policy = policy
        # The region ID. Call [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) to query the regions supported by Elastic Desktop Service.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The list of instance IDs for public network access control, which are office network IDs or cloud computer IDs.
        # 
        # This parameter is required.
        self.source_id = source_id
        # The granularity of the public network access control policy.
        # 
        # This parameter is required.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.policy is not None:
            result['Policy'] = self.policy

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.source_id is not None:
            result['SourceId'] = self.source_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceId') is not None:
            self.source_id = m.get('SourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

