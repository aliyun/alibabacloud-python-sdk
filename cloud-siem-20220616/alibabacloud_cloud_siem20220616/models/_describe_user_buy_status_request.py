# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserBuyStatusRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sub_user_id: int = None,
    ):
        # The region of the Data Management center for threat analysis. Select a region for the management center based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are in a region outside China.
        self.region_id = region_id
        # The ID of the Alibaba Cloud account.
        self.sub_user_id = sub_user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

