# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyRCElasticScalingRequest(DaraModel):
    def __init__(
        self,
        dry_run: bool = None,
        instance_id: str = None,
        instance_type: str = None,
        region_id: str = None,
        scaling_enabled: bool = None,
        scheduled_rule: str = None,
    ):
        self.dry_run = dry_run
        self.instance_id = instance_id
        self.instance_type = instance_type
        self.region_id = region_id
        self.scaling_enabled = scaling_enabled
        self.scheduled_rule = scheduled_rule

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

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scaling_enabled is not None:
            result['ScalingEnabled'] = self.scaling_enabled

        if self.scheduled_rule is not None:
            result['ScheduledRule'] = self.scheduled_rule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ScalingEnabled') is not None:
            self.scaling_enabled = m.get('ScalingEnabled')

        if m.get('ScheduledRule') is not None:
            self.scheduled_rule = m.get('ScheduledRule')

        return self

