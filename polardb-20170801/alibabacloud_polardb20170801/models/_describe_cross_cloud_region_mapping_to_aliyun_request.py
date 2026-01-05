# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCrossCloudRegionMappingToAliyunRequest(DaraModel):
    def __init__(
        self,
        aliyun_region_id: str = None,
        cloud_provider: str = None,
        cross_cloud_region_id: str = None,
    ):
        self.aliyun_region_id = aliyun_region_id
        self.cloud_provider = cloud_provider
        self.cross_cloud_region_id = cross_cloud_region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.aliyun_region_id is not None:
            result['AliyunRegionId'] = self.aliyun_region_id

        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.cross_cloud_region_id is not None:
            result['CrossCloudRegionId'] = self.cross_cloud_region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliyunRegionId') is not None:
            self.aliyun_region_id = m.get('AliyunRegionId')

        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('CrossCloudRegionId') is not None:
            self.cross_cloud_region_id = m.get('CrossCloudRegionId')

        return self

