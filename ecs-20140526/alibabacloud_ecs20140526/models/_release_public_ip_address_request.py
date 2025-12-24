# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ReleasePublicIpAddressRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        instance_id: str = None,
        public_ip_address: str = None,
        region_id: str = None,
    ):
        # > This parameter is unavailable.
        self.dry_run = dry_run
        # The ID of the instance.
        self.instance_id = instance_id
        # The public IP address of the instance.
        # 
        # This parameter is required.
        self.public_ip_address = public_ip_address
        # The region ID of the instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.public_ip_address is not None:
            result['PublicIpAddress'] = self.public_ip_address

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('PublicIpAddress') is not None:
            self.public_ip_address = m.get('PublicIpAddress')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

