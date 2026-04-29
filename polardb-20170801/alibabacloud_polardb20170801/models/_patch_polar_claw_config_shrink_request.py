# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PatchPolarClawConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        config_patch_shrink: str = None,
        restart: bool = None,
    ):
        # This parameter is required.
        self.application_id = application_id
        self.config_patch_shrink = config_patch_shrink
        self.restart = restart

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.config_patch_shrink is not None:
            result['ConfigPatch'] = self.config_patch_shrink

        if self.restart is not None:
            result['Restart'] = self.restart

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ConfigPatch') is not None:
            self.config_patch_shrink = m.get('ConfigPatch')

        if m.get('Restart') is not None:
            self.restart = m.get('Restart')

        return self

