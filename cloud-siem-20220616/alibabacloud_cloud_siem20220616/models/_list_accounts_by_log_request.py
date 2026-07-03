# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListAccountsByLogRequest(DaraModel):
    def __init__(
        self,
        cloud_code: str = None,
        log_codes: List[str] = None,
        prod_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The code of the multicloud environment.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The list of log codes. The value must be a JSON array.
        # 
        # This parameter is required.
        self.log_codes = log_codes
        # The code of the product.
        # 
        # This parameter is required.
        self.prod_code = prod_code
        # The region where the Data Management center of Threat Analysis is located. Select the region based on the region where your assets are located. Valid values:
        # 
        # - cn-hangzhou: Your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Your assets are outside China.
        self.region_id = region_id
        # The user ID of the member. This parameter allows an administrator to switch to the perspective of a member account.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts that belong to the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_code is not None:
            result['CloudCode'] = self.cloud_code

        if self.log_codes is not None:
            result['LogCodes'] = self.log_codes

        if self.prod_code is not None:
            result['ProdCode'] = self.prod_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('LogCodes') is not None:
            self.log_codes = m.get('LogCodes')

        if m.get('ProdCode') is not None:
            self.prod_code = m.get('ProdCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

