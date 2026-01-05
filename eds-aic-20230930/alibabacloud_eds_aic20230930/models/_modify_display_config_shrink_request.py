# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ModifyDisplayConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        android_instance_ids: List[str] = None,
        display_config_shrink: str = None,
    ):
        self.android_instance_ids = android_instance_ids
        self.display_config_shrink = display_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_instance_ids is not None:
            result['AndroidInstanceIds'] = self.android_instance_ids

        if self.display_config_shrink is not None:
            result['DisplayConfig'] = self.display_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AndroidInstanceIds') is not None:
            self.android_instance_ids = m.get('AndroidInstanceIds')

        if m.get('DisplayConfig') is not None:
            self.display_config_shrink = m.get('DisplayConfig')

        return self

