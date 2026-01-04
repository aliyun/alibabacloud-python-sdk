# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreatePhysicalConnectionSetupOrderRequest(DaraModel):
    def __init__(
        self,
        access_point_id: str = None,
        auto_pay: bool = None,
        client_token: str = None,
        line_operator: str = None,
        owner_account: str = None,
        owner_id: int = None,
        port_type: str = None,
        redundant_physical_connection_id: str = None,
        region_id: str = None,
        resource_owner_account: str = None,
        resource_owner_id: int = None,
    ):
        # The ID of the access point.
        # 
        # This parameter is required.
        self.access_point_id = access_point_id
        # Specifies whether to enable automatic payments. Valid values:
        # 
        # *   **false** (default): disables automatic payment.
        # *   **true**
        self.auto_pay = auto_pay
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # >  If you do not specify this parameter, the system automatically uses the **request ID** as the **client token**. The **request ID** may be different for each request.
        self.client_token = client_token
        # The connectivity provider of the Express Connect circuit. Valid values:
        # 
        # *   **CT**: China Telecom
        # *   **CU**: China Unicom
        # *   **CM**: China Mobile
        # *   **CO**: other connectivity providers in the Chinese mainland
        # *   **Equinix**: Equinix
        # *   **Other**: other connectivity providers outside the Chinese mainland
        # 
        # This parameter is required.
        self.line_operator = line_operator
        self.owner_account = owner_account
        self.owner_id = owner_id
        # The port type of the Express Connect circuit. Valid values:
        # 
        # *   **100Base-T**: 100 Mbit/s copper Ethernet port
        # *   **1000Base-T** (default): 1,000 Mbit/s copper Ethernet port
        # *   **1000Base-LX**: 1,000 Mbit/s single-mode optical port (10 km)
        # *   **10GBase-T**: 10,000 Mbit/s copper Ethernet port
        # *   **10GBase-LR**: 10,000 Mbit/s single-mode optical port (10 km)
        # *   **40GBase-LR**: 40,000 Mbit/s single-mode optical port
        # *   **100GBase-LR**: 100,000 Mbit/s single-mode optical port
        # 
        # >  Whether 40GBase-LR and 100GBase-LR ports can be created depends on resource supplies. For more information, contact your account manager.
        self.port_type = port_type
        # The ID of the redundant physical connection. The redundant physical connection must be in the **Allocated**, **Confirmed**, or **Enabled** state.
        self.redundant_physical_connection_id = redundant_physical_connection_id
        # The region ID of the Express Connect circuit.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
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
        if self.access_point_id is not None:
            result['AccessPointId'] = self.access_point_id

        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.line_operator is not None:
            result['LineOperator'] = self.line_operator

        if self.owner_account is not None:
            result['OwnerAccount'] = self.owner_account

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.port_type is not None:
            result['PortType'] = self.port_type

        if self.redundant_physical_connection_id is not None:
            result['RedundantPhysicalConnectionId'] = self.redundant_physical_connection_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_owner_account is not None:
            result['ResourceOwnerAccount'] = self.resource_owner_account

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessPointId') is not None:
            self.access_point_id = m.get('AccessPointId')

        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('LineOperator') is not None:
            self.line_operator = m.get('LineOperator')

        if m.get('OwnerAccount') is not None:
            self.owner_account = m.get('OwnerAccount')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PortType') is not None:
            self.port_type = m.get('PortType')

        if m.get('RedundantPhysicalConnectionId') is not None:
            self.redundant_physical_connection_id = m.get('RedundantPhysicalConnectionId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceOwnerAccount') is not None:
            self.resource_owner_account = m.get('ResourceOwnerAccount')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        return self

