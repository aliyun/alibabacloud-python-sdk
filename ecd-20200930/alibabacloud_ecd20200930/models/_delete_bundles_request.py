# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteBundlesRequest(DaraModel):
    def __init__(
        self,
        bundle_id: List[str] = None,
        region_id: str = None,
    ):
        # The IDs of the cloud computer templates. You can specify 1 to 100 IDs.
        # 
        # This parameter is required.
        self.bundle_id = bundle_id
        # The region ID. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/196646.html) operation to query the most recent region list.
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
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

