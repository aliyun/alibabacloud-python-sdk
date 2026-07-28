# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class LockEmbodiedAIPlatformRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        platform_name: str = None,
        region_id: str = None,
    ):
        # The instance cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The name of the embodied intelligence multimodal data platform.
        # > The name can contain lowercase letters, digits, and underscores. It must start with a letter and end with a letter or digit. The name can be up to 16 characters in length.
        # 
        # This parameter is required.
        self.platform_name = platform_name
        # The region ID.
        # 
        # > You can call the DescribeRegions operation to query the region ID of a specified Data Lakehouse Edition cluster.
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
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

