# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetVpnGatewayDiagnoseResultRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        diagnose_id: str = None,
        region_id: str = None,
        vpn_gateway_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The client token can contain only ASCII characters.
        # 
        # **
        # 
        # **Description** If you do not specify this parameter, the system automatically uses the request ID as the client token. The request ID may be different for each request.
        self.client_token = client_token
        # The ID of the diagnostic operation.
        # 
        # When you call the [DiagnoseVpnGateway](https://help.aliyun.com/document_detail/469751.html) operation, the system returns a corresponding ID.
        self.diagnose_id = diagnose_id
        # The region ID of the VPN gateway.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the VPN gateway.
        self.vpn_gateway_id = vpn_gateway_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.diagnose_id is not None:
            result['DiagnoseId'] = self.diagnose_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.vpn_gateway_id is not None:
            result['VpnGatewayId'] = self.vpn_gateway_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DiagnoseId') is not None:
            self.diagnose_id = m.get('DiagnoseId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('VpnGatewayId') is not None:
            self.vpn_gateway_id = m.get('VpnGatewayId')

        return self

