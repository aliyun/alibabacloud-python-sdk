# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RebootRCInstanceRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        force_stop: bool = None,
        instance_id: str = None,
        reboot_time: str = None,
        region_id: str = None,
    ):
        self.dry_run = dry_run
        self.force_stop = force_stop
        # This parameter is required.
        self.instance_id = instance_id
        self.reboot_time = reboot_time
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

        if self.force_stop is not None:
            result['ForceStop'] = self.force_stop

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.reboot_time is not None:
            result['RebootTime'] = self.reboot_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('ForceStop') is not None:
            self.force_stop = m.get('ForceStop')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('RebootTime') is not None:
            self.reboot_time = m.get('RebootTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

