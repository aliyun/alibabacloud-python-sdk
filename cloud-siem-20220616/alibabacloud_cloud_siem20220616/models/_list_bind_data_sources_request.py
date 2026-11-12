# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListBindDataSourcesRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        cloud_code: str = None,
        region_id: str = None,
    ):
        # The cloud account ID.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The code of the multi-cloud provider.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The region where the threat analysis data management center resides. Select the management center region based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets reside in the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

