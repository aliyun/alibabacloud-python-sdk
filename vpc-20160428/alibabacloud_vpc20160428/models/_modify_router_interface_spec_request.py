# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRouterInterfaceSpecRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        owner_account: str = None,
        owner_id: int = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
        router_interface_id: str = None,
        spec: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The ClientToken value can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** may differ for each API request.
        self.client_token = client_token
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The region where the router interface is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the region ID.
        # 
        # This parameter is required.
        self.region_id = region_id
        self.resource_owner_account = resource_owner_account
        self.resource_owner_id = resource_owner_id
        # The ID of the router interface.
        # 
        # This parameter is required.
        self.router_interface_id = router_interface_id
        # The specification of the router interface. The following table describes the available specifications and the corresponding bandwidths:
        # 
        # * **Mini.2**: 2 Mbps
        # 
        # * **Mini.5**: 5 Mbps
        # 
        # * **Small.1**: 10 Mbps
        # 
        # * **Small.2**: 20 Mbps
        # 
        # * **Small.5**: 50 Mbps
        # 
        # * **Middle.1**: 100 Mbps
        # 
        # * **Middle.2**: 200 Mbps
        # 
        # * **Middle.5**: 500 Mbps
        # 
        # * **Large.1**: 1000 Mbps
        # 
        # * **Large.2**: 2000 Mbps
        # 
        # * **Large.5**: 5000 Mbps
        # 
        # * **Xlarge.1**: 10000 Mbps
        # 
        # > If **Role** is set to **AcceptingSide** (accepter), set **Spec** to **Negative**.
        # 
        # This parameter is required.
        self.spec = spec

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

        if self.router_interface_id is not None:
            result['RouterInterfaceId'] = self.router_interface_id

        if self.spec is not None:
            result['Spec'] = self.spec

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('RouterInterfaceId') is not None:
            self.router_interface_id = m.get('RouterInterfaceId')

        if m.get('Spec') is not None:
            self.spec = m.get('Spec')

        return self

