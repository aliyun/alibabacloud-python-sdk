# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteEgressProxyIpPoolRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: bool = None,
        egress_proxy_ip_pool_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can generate the value of this parameter on the client side. Make sure that the value is unique across different requests. The client token can contain only ASCII characters.
        # 
        # > Note: If you do not specify this parameter, the system automatically uses the RequestId of the API request as the client token. The RequestId of each API request is different.
        self.client_token = client_token
        # Specifies whether to only precheck the request. Valid values:
        # 
        # - **true**: The system sends a check request and does not delete the egress proxy IP address pool. The system checks whether the required parameters are specified, the request format is valid, and the service limits are met. If the check fails, the system returns the corresponding error. If the check succeeds, the system returns the error code DryRunOperation.
        # 
        # - **false** (default): The system sends a normal request. If the check succeeds, the system returns an HTTP 2xx status code and performs the operation.
        self.dry_run = dry_run
        # The ID of the egress proxy IP address pool.
        # 
        # This parameter is required.
        self.egress_proxy_ip_pool_id = egress_proxy_ip_pool_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.egress_proxy_ip_pool_id is not None:
            result['EgressProxyIpPoolId'] = self.egress_proxy_ip_pool_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EgressProxyIpPoolId') is not None:
            self.egress_proxy_ip_pool_id = m.get('EgressProxyIpPoolId')

        return self

