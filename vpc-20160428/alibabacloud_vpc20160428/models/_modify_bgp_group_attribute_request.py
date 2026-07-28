# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyBgpGroupAttributeRequest(DaraModel):
    def __init__(
        self,
        auth_key: str = None,
        bgp_group_id: str = None,
        clear_auth_key: bool = None,
        client_token: str = None,
        description: str = None,
        is_fake_asn: bool = None,
        local_asn: int = None,
        name: str = None,
        owner_account: str = None,
        owner_id: int = None,
        peer_asn: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        route_quota: int = None,
    ):
        # The authentication key of the BGP group.
        self.auth_key = auth_key
        # The ID of the BGP group.
        # 
        # This parameter is required.
        self.bgp_group_id = bgp_group_id
        # Specifies whether to clear the authentication key. Valid values:
        # 
        # - **true**: Yes.
        # - **false** (default): No.
        self.clear_auth_key = clear_auth_key
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may be different for each API request.
        self.client_token = client_token
        # The description of the BGP group.
        # 
        # The description must be 0 to 256 characters in length and cannot start with `http://` or `https://`.
        self.description = description
        # Specifies whether to use a fake ASN. Valid values:
        # 
        # - **false** (default): No.
        # - **true**: Yes.
        # 
        # > A router that runs BGP can belong to only one AS. When you need to replace an existing AS with a new one (for example, during AS migration or merger with another AS) and cannot immediately modify the BGP configuration due to business constraints, you can specify a fake ASN to establish a connection with the local end to ensure service continuity.
        self.is_fake_asn = is_fake_asn
        # The custom Alibaba Cloud-side BGP autonomous system number (ASN). Valid values:
        # 
        # - **45104**
        # - **64512 to 65534**
        # - **4200000000 to 4294967294**
        # 
        # > **65025** is reserved by Alibaba Cloud. The Alibaba Cloud side uses **45104** as the default **LocalAsn** value. Using a custom **LocalAsn** value in multi-ISP access scenarios may cause BGP routing loops. Evaluate the risks before you use this feature.
        self.local_asn = local_asn
        # The name of the BGP group. 
        # 
        # The name must be 0 to 128 characters in length and cannot start with `http://` or `https://`.
        self.name = name
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The ASN of the on-premises device.
        self.peer_asn = peer_asn
        # The region ID of the BGP group. 
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The maximum number of routes for a BGP peer. Unit: entries. Default value: **110**.
        self.route_quota = route_quota

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_key is not None:
            result['AuthKey'] = self.auth_key

        if self.bgp_group_id is not None:
            result['BgpGroupId'] = self.bgp_group_id

        if self.clear_auth_key is not None:
            result['ClearAuthKey'] = self.clear_auth_key

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.description is not None:
            result['Description'] = self.description

        if self.is_fake_asn is not None:
            result['IsFakeAsn'] = self.is_fake_asn

        if self.local_asn is not None:
            result['LocalAsn'] = self.local_asn

        if self.name is not None:
            result['Name'] = self.name

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.peer_asn is not None:
            result['PeerAsn'] = self.peer_asn

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.route_quota is not None:
            result['RouteQuota'] = self.route_quota

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthKey') is not None:
            self.auth_key = m.get('AuthKey')

        if m.get('BgpGroupId') is not None:
            self.bgp_group_id = m.get('BgpGroupId')

        if m.get('ClearAuthKey') is not None:
            self.clear_auth_key = m.get('ClearAuthKey')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsFakeAsn') is not None:
            self.is_fake_asn = m.get('IsFakeAsn')

        if m.get('LocalAsn') is not None:
            self.local_asn = m.get('LocalAsn')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PeerAsn') is not None:
            self.peer_asn = m.get('PeerAsn')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('RouteQuota') is not None:
            self.route_quota = m.get('RouteQuota')

        return self

