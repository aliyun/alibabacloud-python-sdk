# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSpareIpRequest(DaraModel):
    def __init__(
        self,
        accelerator_id: str = None,
        client_token: str = None,
        dry_run: bool = None,
        region_id: str = None,
        spare_ip: str = None,
    ):
        # The instance ID of the Alibaba Cloud Global Accelerator (GA) instance.
        # 
        # This parameter is required.
        self.accelerator_id = accelerator_id
        # The client token that is used to ensure the idempotence of a request.
        # 
        # Generate a unique value from your client to ensure that different requests have unique ClientToken values. ClientToken supports only ASCII characters.
        self.client_token = client_token
        # Specifies whether to perform a dry run. Valid values:
        # - **true**: performs a dry run without actually creating the resource. The system checks the required parameters, request syntax, and business limitations. If the check fails, the corresponding error is returned. If the check passes, the error code `DryRunOperation` is returned.
        # - **false** (default): performs a dry run and sends the request. If the check passes, an HTTP 2xx status code is returned and the operation is performed.
        self.dry_run = dry_run
        # The region ID of the Alibaba Cloud Global Accelerator (GA) instance. Set the value to **cn-hangzhou**.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The CNAME spare IP address. When an acceleration area is abnormal, traffic is switched to this IP address.
        # 
        # This parameter is required.
        self.spare_ip = spare_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accelerator_id is not None:
            result['AcceleratorId'] = self.accelerator_id

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.spare_ip is not None:
            result['SpareIp'] = self.spare_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AcceleratorId') is not None:
            self.accelerator_id = m.get('AcceleratorId')

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SpareIp') is not None:
            self.spare_ip = m.get('SpareIp')

        return self

