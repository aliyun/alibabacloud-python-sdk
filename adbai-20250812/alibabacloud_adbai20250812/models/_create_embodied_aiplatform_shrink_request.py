# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEmbodiedAIPlatformShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        platform_name: str = None,
        ray_config_shrink: str = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # This parameter is required.
        self.platform_name = platform_name
        self.ray_config_shrink = ray_config_shrink
        # This parameter is required.
        self.region_id = region_id
        self.webserver_spec_name = webserver_spec_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dbcluster_id is not None:
            result['DBClusterId'] = self.dbcluster_id

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.ray_config_shrink is not None:
            result['RayConfig'] = self.ray_config_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RayConfig') is not None:
            self.ray_config_shrink = m.get('RayConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')

        return self

