# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeRegionsRequest(DaraModel):
    def __init__(
        self,
        accept_language: str = None,
        region_id: str = None,
        resource_type: str = None,
    ):
        # The language type for region and zone names. This parameter determines the value of `LocalName` in the response. Valid values:
        # 
        # - zh-CN: Chinese.
        # - en-US: English.
        # - ja: Japanese.
        # 
        # Default value: zh-CN.
        self.accept_language = accept_language
        # The region ID of the user access endpoint.
        self.region_id = region_id
        # The resource type. Valid values:
        # 
        # - ear: asynchronous replication.
        # 
        # - lens: EBS Lens.
        # 
        # - dbsc: dedicated block storage cluster.
        # 
        # If you do not specify a resource type, region information for all resource types is returned.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')

        return self

