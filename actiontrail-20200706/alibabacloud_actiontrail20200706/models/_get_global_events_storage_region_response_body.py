# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGlobalEventsStorageRegionResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        storage_region: str = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The region where global events are stored.
        # 
        # Valid values:
        # 
        # - ap-southeast-1
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   the Singapore region
        # 
        #   <!-- -->
        # 
        # - cn-hangzhou
        # 
        #   <!-- -->
        # 
        #   :
        # 
        #   <!-- -->
        # 
        #   the China (Hangzhou) region
        # 
        #   <!-- -->
        self.storage_region = storage_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.storage_region is not None:
            result['StorageRegion'] = self.storage_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StorageRegion') is not None:
            self.storage_region = m.get('StorageRegion')

        return self

