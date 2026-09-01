# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteIpsecServerRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        dry_run: str = None,
        ipsec_server_id: str = None,
        region_id: str = None,
    ):
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the token, but you must make sure that the token is unique among different requests. The token can contain only ASCII characters.
        # 
        # > If you do not specify this parameter, the system automatically uses the **RequestId** of the API request as the **ClientToken**. The **RequestId** of each API request is different.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # 
        # - **true**: performs a dry run without deleting the IPsec server. The system checks the required parameters, request syntax, and business restrictions. If the check fails, the corresponding error message is returned. If the check succeeds, `DryRunOperation` is returned.
        # 
        # - **false** (default): performs a dry run and sends the request. After the check succeeds, the IPsec server is directly deleted.
        self.dry_run = dry_run
        # The ID of the IPsec server.
        # 
        # This parameter is required.
        self.ipsec_server_id = ipsec_server_id
        # The region ID of the IPsec server.
        # 
        # This parameter is required.
        self.region_id = region_id

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

        if self.ipsec_server_id is not None:
            result['IpsecServerId'] = self.ipsec_server_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('IpsecServerId') is not None:
            self.ipsec_server_id = m.get('IpsecServerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

