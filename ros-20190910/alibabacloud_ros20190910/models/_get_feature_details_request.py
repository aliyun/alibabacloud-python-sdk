# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFeatureDetailsRequest(DaraModel):
    def __init__(
        self,
        feature: str = None,
        region_id: str = None,
    ):
        # The one or more features that you want to query. Valid values:
        # 
        # *   Terraform: the Terraform hosting feature.
        # *   ResourceCleaner: the resource cleaner feature. You can use ALIYUN::ROS::ResourceCleaner to create a resource cleaner.
        # *   TemplateScratch: the scenario feature.
        # *   All: all features that are supported by ROS.
        # 
        # This parameter is required.
        self.feature = feature
        # The region ID of the stack. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/131035.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.feature is not None:
            result['Feature'] = self.feature

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Feature') is not None:
            self.feature = m.get('Feature')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

