# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateSmartAGUserAccelerateConfigRequest(DaraModel):
    def __init__(
        self,
        bandwidth: int = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        smart_agid: str = None,
        user_name: str = None,
    ):
        # The maximum bandwidth value for the client. Unit: Kbit/s.
        # 
        # This parameter is required.
        self.bandwidth = bandwidth
        # The client token that is used to ensure the idempotence of the request.
        # 
        # You can use the client to generate the value, but you must make sure that it is unique among different requests. The token can contain only ASCII characters.
        # 
        # >  If you do not set this parameter, ClientToken is set to the value of RequestId. The value of RequestId for each API request may be different.
        self.client_token = client_token
        # Specifies whether to perform a precheck to check information such as the permissions and instance status. Valid values:
        # 
        # *   **false** (default): sends the request. After the request passes the check, the maximum bandwidth value of the client is modified.
        # *   **true**: prechecks the request but does not modify the maximum bandwidth value of the client. If you use this value, the system checks the required parameters and the request syntax. If the request fails the precheck, an error message is returned. If the request passes the precheck, the `DryRunOperation` error code is returned.
        self.dry_run = dry_run
        # The ID of the region where the SAG app instance is deployed.
        # 
        # You can call the [DescribeRegions](https://help.aliyun.com/document_detail/36063.html) operation to query the most recent region list.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The ID of the SAG app instance.
        # 
        # This parameter is required.
        self.smart_agid = smart_agid
        # The username of the client account.
        # 
        # This parameter is required.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.user_name is not None:
            result['UserName'] = self.user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        return self

