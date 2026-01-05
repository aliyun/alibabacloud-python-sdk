# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeCrossCloudRegionRequest(DaraModel):
    def __init__(
        self,
        cloud_provider: str = None,
        cross_cloud_region_id: str = None,
        dbtype: str = None,
    ):
        self.cloud_provider = cloud_provider
        self.cross_cloud_region_id = cross_cloud_region_id
        self.dbtype = dbtype

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_provider is not None:
            result['CloudProvider'] = self.cloud_provider

        if self.cross_cloud_region_id is not None:
            result['CrossCloudRegionId'] = self.cross_cloud_region_id

        if self.dbtype is not None:
            result['DBType'] = self.dbtype

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudProvider') is not None:
            self.cloud_provider = m.get('CloudProvider')

        if m.get('CrossCloudRegionId') is not None:
            self.cross_cloud_region_id = m.get('CrossCloudRegionId')

        if m.get('DBType') is not None:
            self.dbtype = m.get('DBType')

        return self

