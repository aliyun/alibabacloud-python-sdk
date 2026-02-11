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
        # The log code of the cloud service, such as the code of the process log for Security Center. This parameter is optional. If you leave this parameter empty, operations are performed on all logs of the cloud service.
        self.log_code = log_code
        # The code of the cloud service. Valid values:
        # 
        # *   qcloud_waf
        # *   qlcoud_cfw
        # *   hcloud_waf
        # *   hcloud_cfw
        # *   ddos
        # *   sas
        # *   cfw
        # *   config
        # *   csk
        # *   fc
        # *   rds
        # *   nas
        # *   apigateway
        # *   cdn
        # *   mongodb
        # *   eip
        # *   slb
        # *   vpc
        # *   actiontrail
        # *   waf
        # *   bastionhost
        # *   oss
        # *   polardb
        # 
        # This parameter is required.
        self.product_code = product_code
        # The region in which the data management center of the threat analysis feature resides. Specify this parameter based on the region where your assets reside. Valid values:
        # 
        # *   cn-hangzhou: Your assets reside in regions in China.
        # *   ap-southeast-1: Your assets reside in regions outside China.
        self.region_id = region_id
        # The ID of the account that you switch from the management account.
        self.role_for = role_for
        # The type of the view. Valid values:
        # - 0: the current Alibaba Cloud account
        # - 1: the global account
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

