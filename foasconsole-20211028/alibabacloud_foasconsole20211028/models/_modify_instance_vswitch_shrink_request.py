# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyInstanceVswitchShrinkRequest(DaraModel):
    def __init__(
        self,
        ha_vswitch_ids_shrink: str = None,
        instance_id: str = None,
        v_switch_ids_shrink: str = None,
    ):
        self.ha_vswitch_ids_shrink = ha_vswitch_ids_shrink
        # This parameter is required.
        self.instance_id = instance_id
        self.v_switch_ids_shrink = v_switch_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ha_vswitch_ids_shrink is not None:
            result['HaVSwitchIds'] = self.ha_vswitch_ids_shrink

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.v_switch_ids_shrink is not None:
            result['VSwitchIds'] = self.v_switch_ids_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HaVSwitchIds') is not None:
            self.ha_vswitch_ids_shrink = m.get('HaVSwitchIds')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('VSwitchIds') is not None:
            self.v_switch_ids_shrink = m.get('VSwitchIds')

        return self

