# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateLoadBalancerProtectionRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        deletion_protection_enabled: bool = None,
        deletion_protection_reason: str = None,
        dry_run: bool = None,
        load_balancer_id: str = None,
        modification_protection_reason: str = None,
        modification_protection_status: str = None,
        region_id: str = None,
    ):
        self.client_token = client_token
        self.deletion_protection_enabled = deletion_protection_enabled
        self.deletion_protection_reason = deletion_protection_reason
        self.dry_run = dry_run
        # This parameter is required.
        self.load_balancer_id = load_balancer_id
        self.modification_protection_reason = modification_protection_reason
        self.modification_protection_status = modification_protection_status
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

        if self.deletion_protection_enabled is not None:
            result['DeletionProtectionEnabled'] = self.deletion_protection_enabled

        if self.deletion_protection_reason is not None:
            result['DeletionProtectionReason'] = self.deletion_protection_reason

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.load_balancer_id is not None:
            result['LoadBalancerId'] = self.load_balancer_id

        if self.modification_protection_reason is not None:
            result['ModificationProtectionReason'] = self.modification_protection_reason

        if self.modification_protection_status is not None:
            result['ModificationProtectionStatus'] = self.modification_protection_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('DeletionProtectionEnabled') is not None:
            self.deletion_protection_enabled = m.get('DeletionProtectionEnabled')

        if m.get('DeletionProtectionReason') is not None:
            self.deletion_protection_reason = m.get('DeletionProtectionReason')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('LoadBalancerId') is not None:
            self.load_balancer_id = m.get('LoadBalancerId')

        if m.get('ModificationProtectionReason') is not None:
            self.modification_protection_reason = m.get('ModificationProtectionReason')

        if m.get('ModificationProtectionStatus') is not None:
            self.modification_protection_status = m.get('ModificationProtectionStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

