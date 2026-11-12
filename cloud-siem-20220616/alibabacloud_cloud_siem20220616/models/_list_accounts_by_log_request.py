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
        # The code of the cloud provider.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The list of log codes. This parameter is a repeatList array parameter that must be passed in dot-separated expanded form, for example, LogCodes.1=cloud_siem_hcloud_waf_alert_log. Passing a JSON array string directly is not supported.
        # 
        # This parameter is required.
        self.log_codes = log_codes
        # The code of the product.
        # 
        # This parameter is required.
        self.prod_code = prod_code
        # The region where the CTDR data management center is located. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: the assets belong to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: the assets belong to regions outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type.
        # 
        # - 0: the view of the current Alibaba Cloud account.
        # - 1: the view of all accounts in the enterprise.
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

