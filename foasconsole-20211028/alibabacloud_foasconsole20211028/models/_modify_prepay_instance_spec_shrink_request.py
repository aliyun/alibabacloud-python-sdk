# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyPrepayInstanceSpecShrinkRequest(DaraModel):
    def __init__(
        self,
        ha: bool = None,
        ha_resource_spec_shrink: str = None,
        ha_vswitch_ids_shrink: str = None,
        ha_zone_id: str = None,
        instance_id: str = None,
        region: str = None,
        resource_spec_shrink: str = None,
    ):
        self.ha = ha
        self.ha_resource_spec_shrink = ha_resource_spec_shrink
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        self.ha_zone_id = ha_zone_id
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.resource_spec_shrink = resource_spec_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha is not None:
            result['Ha'] = self.ha

        if self.ha_resource_spec_shrink is not None:
            result['HaResourceSpec'] = self.ha_resource_spec_shrink

        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink

        if self.ha_zone_id is not None:
            result['HaZoneId'] = self.ha_zone_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.region is not None:
            result['Region'] = self.region

        if self.resource_spec_shrink is not None:
            result['ResourceSpec'] = self.resource_spec_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Ha') is not None:
            self.ha = m.get('Ha')

        if m.get('HaResourceSpec') is not None:
            self.ha_resource_spec_shrink = m.get('HaResourceSpec')

        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')

        if m.get('HaZoneId') is not None:
            self.ha_zone_id = m.get('HaZoneId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('ResourceSpec') is not None:
            self.resource_spec_shrink = m.get('ResourceSpec')

        return self

