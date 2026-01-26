# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeAddonReleaseRequest(DaraModel):
    def __init__(
        self,
        environment_id: str = None,
        region_id: str = None,
        release_name: str = None,
    ):
        # The environment ID.
        # 
        # This parameter is required.
        self.environment_id = environment_id
        # The region ID.
        self.region_id = region_id
        # The name of the add-on release.
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
        if self.environment_id is not None:
            result['EnvironmentId'] = self.environment_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.release_name is not None:
            result['ReleaseName'] = self.release_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnvironmentId') is not None:
            self.environment_id = m.get('EnvironmentId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ReleaseName') is not None:
            self.release_name = m.get('ReleaseName')

        return self

