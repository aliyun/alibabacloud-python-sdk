# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        addon_name: str = None,
        environment_id: str = None,
        force: bool = None,
        region_id: str = None,
        release_name: str = None,
    ):
        # The name of the add-on. If you assign a value to AddonName, the ReleaseName parameter is ignored and all AddonReleases that belong to the same add-on are deleted.
        self.addon_name = addon_name
        # Environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # Whether to be forcibly deleted. The default value is false.
        self.force = force
        # The region ID.
        self.region_id = region_id
        # Name of Release.
        # 
        # This parameter is required.
        self.release_name = release_name

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

        if self.force is not None:
            result['Force'] = self.force

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonName') is not None:
            self.addon_name = m.get('AddonName')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('Force') is not None:
            self.force = m.get('Force')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        return self

