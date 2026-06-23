# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteBgpPeerRequest(DaraModel):
    def __init__(
        self,
        bgp_peer_id: str = None,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the BGP peer.
        # 
        # This parameter is required.
        self.bgp_peer_id = bgp_peer_id
        # The client token that is used to ensure the idempotence of the request.
        # 
        # Generate a parameter value from your client to ensure uniqueness across different requests. ClientToken only supports ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may vary for each API request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region where the BGP group is located.
        # 
        # You can obtain the region ID by calling the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) API.
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
        if self.bgp_peer_id is not None:
            result['BgpPeerId'] = self.bgp_peer_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

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
        if m.get('BgpPeerId') is not None:
            self.bgp_peer_id = m.get('BgpPeerId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

