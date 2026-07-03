# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListProjectLogStoresRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        source_log_code: str = None,
        source_prod_code: str = None,
        sub_user_id: int = None,
    ):
        # The region of the Data Management center for threat analysis. Specify the region based on where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Assets are in regions outside China.
        self.region_id = region_id
        # The code of the log to query.
        # 
        # This parameter is required.
        self.source_log_code = source_log_code
        # The code of the product to query.
        # 
        # This parameter is required.
        self.source_prod_code = source_prod_code
        # The ID of the Alibaba Cloud account to query.
        # 
        # This parameter is required.
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

        if self.source_log_code is not None:
            result['SourceLogCode'] = self.source_log_code

        if self.source_prod_code is not None:
            result['SourceProdCode'] = self.source_prod_code

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SourceLogCode') is not None:
            self.source_log_code = m.get('SourceLogCode')

        if m.get('SourceProdCode') is not None:
            self.source_prod_code = m.get('SourceProdCode')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        return self

