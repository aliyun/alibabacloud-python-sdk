# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBindAccountRequest(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The AccessKey ID of the cloud account.
        # 
        # This parameter is required.
        self.access_id = access_id
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The binding ID. You can call the [ListBindAccount](https://api.aliyun-inc.com/#/publishment/document/cloud-siem/863fdf54478f4cc5877e27c2a5fe9e44?tenantUuid=f382fccd88b94c5c8c864def6815b854&activeTabKey=api|ListBindAccount) operation to obtain the binding ID.
        self.bind_id = bind_id
        # The code of the multi-cloud provider. Valid values:
        # - qcloud: Tencent Cloud.
        # - aliyun: Alibaba Cloud.
        # - hcloud: Huawei Cloud.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The region where the data management center for threat analysis is located. You must select the region of the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: Assets are located in the Chinese mainland and Hong Kong (China).
        # - ap-southeast-1: Assets are located outside China.
        self.region_id = region_id
        # The ID of the user whose view the administrator switches to.
        self.role_for = role_for
        # The view type. Valid values:
        # - 0: The view of the current Alibaba Cloud account.
        # - 1: The view of all accounts in the enterprise.
        self.role_type = role_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_id is not None:
            result['AccessId'] = self.access_id

        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.bind_id is not None:
            result['BindId'] = self.bind_id

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
        if m.get('AccessId') is not None:
            self.access_id = m.get('AccessId')

        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('BindId') is not None:
            self.bind_id = m.get('BindId')

        if m.get('CloudCode') is not None:
            self.cloud_code = m.get('CloudCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('RoleType') is not None:
            self.role_type = m.get('RoleType')

        return self

