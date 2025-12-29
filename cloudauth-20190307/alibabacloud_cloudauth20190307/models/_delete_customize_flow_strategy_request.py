# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCustomizeFlowStrategyRequest(DaraModel):
    def __init__(
        self,
        api_name: str = None,
        id: int = None,
        product_type: str = None,
        region_id: str = None,
        user_id: int = None,
    ):
        # API name, same as **ProductCode**.
        self.api_name = api_name
        # Policy ID.
        # 
        # This parameter is required.
        self.id = id
        # Product type, currently only supports **ANT_CLOUD_AUTH** (Financial-grade Real Person), all others have been phased out.
        self.product_type = product_type
        # regionId
        self.region_id = region_id
        # User ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_name is not None:
            result['ApiName'] = self.api_name

        if self.id is not None:
            result['Id'] = self.id

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.user_id is not None:
            result['UserId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiName') is not None:
            self.api_name = m.get('ApiName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        return self

