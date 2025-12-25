# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DeleteRCInstancesRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force: bool = None,
        instance_id: List[str] = None,
        region_id: str = None,
        terminate_subscription: bool = None,
    ):
        # Specifies whether to perform only a dry run, without performing the actual request. Valid values:
        # 
        # *   **true**: performs only a dry run. The system checks the request for potential issues, including missing parameter values, incorrect request syntax, service limits, and insufficient inventory errors.
        # *   **false** (default): performs a dry run and performs the actual request. If the request passes the dry run, the instance is created.
        self.dry_run = dry_run
        # Specifies whether to forcefully release a running instance. Valid values:
        # 
        # *   **Yes**
        # *   **No** (default)
        self.force = force
        # The details of the instance.
        # 
        # This parameter is required.
        self.instance_id = instance_id
        # The region ID of the instance.
        self.region_id = region_id
        # Specifies whether to release an expired subscription instance. Valid values:
        # 
        # *   **true**
        # *   **false** (default)
        self.terminate_subscription = terminate_subscription

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.force is not None:
            result['Force'] = self.force

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.terminate_subscription is not None:
            result['TerminateSubscription'] = self.terminate_subscription

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TerminateSubscription') is not None:
            self.terminate_subscription = m.get('TerminateSubscription')

        return self

