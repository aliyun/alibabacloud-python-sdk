# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeletionProtectionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        instance_id: str = None,
        owner_id: int = None,
        protection_enable: bool = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        type: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        # The ID of the instance for which you want to set deletion protection in Settings.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        self.owner_id = owner_id
        # Specifies whether to enable deletion protection. Valid values:
        # 
        # - **true**: enables deletion protection.
        # 
        # - **false**: disables deletion protection.
        # 
        # This parameter is required.
        self.protection_enable = protection_enable
        # The region ID of the instance for which you want to enable or disable deletion protection. You can call [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The type of the instance for which you want to enable or disable deletion protection. Valid values:
        # 
        # - **EIP**: elastic IP address (EIP).
        # 
        # - **CBWP**: Internet Shared Bandwidth.
        # 
        # - **NATGW**: NAT gateway.
        # 
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.protection_enable is not None:
            result['ProtectionEnable'] = self.protection_enable

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('ProtectionEnable') is not None:
            self.protection_enable = m.get('ProtectionEnable')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

