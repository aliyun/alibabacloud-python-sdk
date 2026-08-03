# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateGlobalEventsStorageRegionRequest(DaraModel):
    def __init__(
        self,
        storage_region: str = None,
    ):
        # The region where you want to store global events.
        # 
        # Valid values:
        # 
        # *   ap-southeast-1
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the Singapore region
        # 
        #     <!-- -->
        # 
        # *   cn-hangzhou
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     the China (Hangzhou) region
        # 
        #     <!-- -->
        # 
        # This parameter is required.
        self.storage_region = storage_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')

        return self

