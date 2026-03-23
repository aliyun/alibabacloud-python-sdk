# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteRCInstancesShrinkRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force: bool = None,
        instance_id_shrink: str = None,
        region_id: str = None,
        terminate_subscription: bool = None,
    ):
        self.dry_run = dry_run
        self.force = force
        # This parameter is required.
        self.instance_id_shrink = instance_id_shrink
        self.region_id = region_id
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

        if self.instance_id_shrink is not None:
            result['InstanceId'] = self.instance_id_shrink

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
            self.instance_id_shrink = m.get('InstanceId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('TerminateSubscription') is not None:
            self.terminate_subscription = m.get('TerminateSubscription')

        return self

