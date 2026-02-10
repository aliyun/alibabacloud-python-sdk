# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class SetSyncRefreshRegionRequest(DaraModel):
    def __init__(
        self,
        default_region: int = None,
        region_ids: List[str] = None,
        vendor: str = None,
    ):
        # The access type of the multi-cloud site. Valid values:
        # 
        # *   **0**: The current site is not the default site of multi-cloud site. You can specify the current site as the default site of the multi-cloud site.
        # *   **1**: The current site is the default site of multi-cloud site.
        self.default_region = default_region
        # The regions from which you want to synchronize assets at the current site.
        self.region_ids = region_ids
        # The cloud service provider. Valid values:
        # 
        # *   **Tencent**: Tencent Cloud
        # *   **HUAWEICLOUD**: Huawei Cloud
        # *   **Azure**: Microsoft Azure
        # *   **AWS**: Amazon Web Services (AWS)
        self.vendor = vendor

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_region is not None:
            result['DefaultRegion'] = self.default_region

        if self.region_ids is not None:
            result['RegionIds'] = self.region_ids

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultRegion') is not None:
            self.default_region = m.get('DefaultRegion')

        if m.get('RegionIds') is not None:
            self.region_ids = m.get('RegionIds')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

