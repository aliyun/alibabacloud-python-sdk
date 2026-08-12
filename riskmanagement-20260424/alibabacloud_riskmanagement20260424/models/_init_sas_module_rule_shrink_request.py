# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class InitSasModuleRuleShrinkRequest(DaraModel):
    def __init__(
        self,
        auto_bind: int = None,
        instances_shrink: str = None,
        is_trial: bool = None,
        region_id: str = None,
    ):
        # Specifies whether to enable automatic binding. Valid values:
        # 
        # - **0**: Disabled.
        # - **1**: Enabled.
        self.auto_bind = auto_bind
        # The list of instances.
        self.instances_shrink = instances_shrink
        # Specifies whether to use the trial version.
        self.is_trial = is_trial
        # The region ID of the access control instance.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_bind is not None:
            result['AutoBind'] = self.auto_bind

        if self.instances_shrink is not None:
            result['Instances'] = self.instances_shrink

        if self.is_trial is not None:
            result['IsTrial'] = self.is_trial

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoBind') is not None:
            self.auto_bind = m.get('AutoBind')

        if m.get('Instances') is not None:
            self.instances_shrink = m.get('Instances')

        if m.get('IsTrial') is not None:
            self.is_trial = m.get('IsTrial')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

