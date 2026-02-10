# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModifyImageFixCycleConfigRequest(DaraModel):
    def __init__(
        self,
        image_fix_cycle: int = None,
        image_fix_switch: str = None,
        image_fix_target: str = None,
        image_time_range: int = None,
    ):
        # The cycle of the scheduled fix. Unit: day.
        self.image_fix_cycle = image_fix_cycle
        # Specifies whether to enable the schedule image fix.
        # 
        # *   **on**: enable
        # *   **off**: disable
        self.image_fix_switch = image_fix_switch
        # The range of the scheduled fix. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **type**: The type of the image. The value is fixed to repo.
        # *   **target**: The content of the image. The value is in the format of Namespace/Image repository.
        self.image_fix_target = image_fix_target
        # The time range during which the image was modified. Unit: day.
        self.image_time_range = image_time_range

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.image_fix_cycle is not None:
            result['ImageFixCycle'] = self.image_fix_cycle

        if self.image_fix_switch is not None:
            result['ImageFixSwitch'] = self.image_fix_switch

        if self.image_fix_target is not None:
            result['ImageFixTarget'] = self.image_fix_target

        if self.image_time_range is not None:
            result['ImageTimeRange'] = self.image_time_range

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageFixCycle') is not None:
            self.image_fix_cycle = m.get('ImageFixCycle')

        if m.get('ImageFixSwitch') is not None:
            self.image_fix_switch = m.get('ImageFixSwitch')

        if m.get('ImageFixTarget') is not None:
            self.image_fix_target = m.get('ImageFixTarget')

        if m.get('ImageTimeRange') is not None:
            self.image_time_range = m.get('ImageTimeRange')

        return self

