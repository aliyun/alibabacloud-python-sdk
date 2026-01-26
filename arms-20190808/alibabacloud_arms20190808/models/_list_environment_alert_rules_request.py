# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListEnvironmentAlertRulesRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        environment_id: str = None,
        region_id: str = None,
        scene: str = None,
    ):
        # The name of the add-on. You must specify AddonName or Scene.
        self.addon_name = addon_name
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        self.region_id = region_id
        # The scenario of the add-on. You must specify AddonName or Scene.
        self.scene = scene

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_name is not None:
            result['AddonName'] = self.addon_name

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scene is not None:
            result['Scene'] = self.scene

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scene') is not None:
            self.scene = m.get('Scene')

        return self

