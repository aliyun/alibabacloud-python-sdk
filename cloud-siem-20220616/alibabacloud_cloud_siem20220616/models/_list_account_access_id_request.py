# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAccountAccessIdRequest(DaraModel):
    def __init__(
        self,
        cloud_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The code of the multi-cloud provider.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The location of the data management center for threat detection and response. Select the management center location based on the region of your assets. Valid values:
        # - cn-hangzhou: Your assets belong to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: Your assets belong to regions outside China.
        self.region_id = region_id
        # The ID of the member to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
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

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

