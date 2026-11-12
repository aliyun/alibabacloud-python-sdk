# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBindAccountRequest(DaraModel):
    def __init__(
        self,
        access_id: str = None,
        account_id: str = None,
        account_name: str = None,
        bind_id: int = None,
        cloud_code: str = None,
        region_id: str = None,
        role_for: int = None,
        role_type: int = None,
    ):
        # The AccessKey ID of the cloud account.
        self.access_id = access_id
        # The ID of the cloud account.
        # 
        # This parameter is required.
        self.account_id = account_id
        # The name of the multi-cloud account.
        self.account_name = account_name
        # The ID of the binding record. This is the BindId returned by the ListBindAccount operation.
        # 
        # This parameter is required.
        self.bind_id = bind_id
        # The code of the multi-cloud provider. Valid values:
        # 
        # - **hcloud**: Huawei Cloud.
        # - **qcloud**: Tencent Cloud.
        # 
        # This parameter is required.
        self.cloud_code = cloud_code
        # The region where the threat detection and response (CTDR) data management center resides. Select the management center based on the region of your assets. Valid values:
        # - cn-hangzhou: The assets belong to the Chinese mainland or Hong Kong (China).
        # - ap-southeast-1: The assets belong to regions outside China.
        self.region_id = region_id
        # The ID of the member account to which the administrator switches the view.
        self.role_for = role_for
        # The view type. Valid values:
        # 
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

        if self.account_name is not None:
            result['AccountName'] = self.account_name

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

        if m.get('AccountName') is not None:
            self.account_name = m.get('AccountName')

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

