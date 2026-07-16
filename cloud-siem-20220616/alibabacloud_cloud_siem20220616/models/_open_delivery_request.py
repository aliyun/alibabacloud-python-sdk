# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class OpenDeliveryRequest(DaraModel):
    def __init__(
        self,
        log_code: str = None,
        product_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The code for a specific log of the cloud service, such as the process log of Security Center. This parameter is optional. If you do not specify this parameter, the operation applies to all logs of the service.
        self.log_code = log_code
        # The code of the cloud service. Valid values:
        # 
        # - qcloud_waf
        # 
        # - qcloud_cfw
        # 
        # - hcloud_waf
        # 
        # - hcloud_cfw
        # 
        # - ddos
        # 
        # - sas
        # 
        # - cfw
        # 
        # - config
        # 
        # - csk
        # 
        # - fc
        # 
        # - rds
        # 
        # - nas
        # 
        # - apigateway
        # 
        # - cdn
        # 
        # - mongodb
        # 
        # - eip
        # 
        # - slb
        # 
        # - vpc
        # 
        # - actiontrail
        # 
        # - waf
        # 
        # - bastionhost
        # 
        # - oss
        # 
        # - polardb
        # 
        # This parameter is required.
        self.product_code = product_code
        # The region where the Data Management center of threat analysis is located. Select a region based on the location of your assets. Valid values:
        # 
        # - cn-hangzhou: Select this value if your assets are in the Chinese mainland or China (Hong Kong).
        # 
        # - ap-southeast-1: Select this value if your assets are in a region outside China.
        self.region_id = region_id
        # The ID of the member account that the administrator wants to access.
        self.role_for = role_for
        # The type of the view. Valid values:
        # 
        # - 0: The view of the current Alibaba Cloud account.
        # 
        # - 1: The view of all accounts within the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.role_type is not None:
            result['RoleType'] = self.role_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

