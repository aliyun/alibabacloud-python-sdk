# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AssociateEipAddressBatchRequest(DaraModel):
    def __init__(
        self,
        binded_instance_id: str = None,
        binded_instance_type: str = None,
        client_token: str = None,
        instance_ids: List[str] = None,
        mode: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the instance with which you want to associate the EIPs.
        # 
        # The instance can be a NAT gateway or a secondary ENI.
        # 
        # This parameter is required.
        self.binded_instance_id = binded_instance_id
        # The type of the instance with which you want to associate the EIPs. Valid values:
        # 
        # *   **Nat**: NAT gateway
        # *   **NetworkInterface**: secondary ENI
        # 
        # This parameter is required.
        self.binded_instance_type = binded_instance_type
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate a token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The EIPs to be associated with the instance.
        # 
        # You must enter at least one EIP. You can enter up to 50 EIPs.
        # 
        # This parameter is required.
        self.instance_ids = instance_ids
        # The association mode. Set the value to **MULTI_BINDED**, which specifies the Multi-EIP-to-ENI mode.
        # 
        # This parameter is required only when **BindedInstanceType** is set to **NetworkInterface**.
        self.mode = mode
        self.owner_id = owner_id
        # The ID of the region to which the EIPs belong. You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binded_instance_id is not None:
            result['BindedInstanceId'] = self.binded_instance_id

        if self.binded_instance_type is not None:
            result['BindedInstanceType'] = self.binded_instance_type

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.mode is not None:
            result['Mode'] = self.mode

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindedInstanceId') is not None:
            self.binded_instance_id = m.get('BindedInstanceId')

        if m.get('BindedInstanceType') is not None:
            self.binded_instance_type = m.get('BindedInstanceType')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('Mode') is not None:
            self.mode = m.get('Mode')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

