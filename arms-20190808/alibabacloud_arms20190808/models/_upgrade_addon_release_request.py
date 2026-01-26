# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpgradeAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        addon_version: str = None,
        dry_run: bool = None,
        environment_id: str = None,
        region_id: str = None,
        release_name: str = None,
        values: str = None,
    ):
        # The version of the add-on.
        # 
        # This parameter is required.
        self.addon_version = addon_version
        # Specifies whether to perform only a dry run, without performing the actual request.
        self.dry_run = dry_run
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        self.region_id = region_id
        # The name of the release.
        # 
        # This parameter is required.
        self.release_name = release_name
        # The metadata information.
        # 
        # This parameter is required.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.addon_version is not None:
            result['AddonVersion'] = self.addon_version

        if self.dry_run is not None:
            result['DryRun'] = self.dry_run

        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddonVersion') is not None:
            self.addon_version = m.get('AddonVersion')

        if m.get('DryRun') is not None:
            self.dry_run = m.get('DryRun')

        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self

