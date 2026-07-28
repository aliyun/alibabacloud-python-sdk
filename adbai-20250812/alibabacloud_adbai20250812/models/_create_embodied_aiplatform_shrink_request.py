# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateEmbodiedAIPlatformShrinkRequest(DaraModel):
    def __init__(
        self,
        dbcluster_id: str = None,
        device_count: int = None,
        platform_name: str = None,
        ray_config_shrink: str = None,
        ray_train_config_shrink: str = None,
        region_id: str = None,
        webserver_spec_name: str = None,
    ):
        # The instance cluster ID.
        # 
        # This parameter is required.
        self.dbcluster_id = dbcluster_id
        # The ontology count.
        self.device_count = device_count
        # The name of the embodied intelligence multimodal data platform.
        # > The name can contain lowercase letters, digits, and underscores. It must start with a letter and end with a letter or digit. The name can be up to 16 characters in length.
        # 
        # This parameter is required.
        self.platform_name = platform_name
        # The Ray specification information of the platform.
        self.ray_config_shrink = ray_config_shrink
        # The development and training resource configuration.
        self.ray_train_config_shrink = ray_train_config_shrink
        # The region ID.
        # 
        # > You can call the DescribeRegions operation to query the region ID of a specified Data Lakehouse Edition cluster.
        # 
        # This parameter is required.
        self.region_id = region_id
        # The webserver specification of the platform.
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

        if self.device_count is not None:
            result['DeviceCount'] = self.device_count

        if self.platform_name is not None:
            result['PlatformName'] = self.platform_name

        if self.ray_config_shrink is not None:
            result['RayConfig'] = self.ray_config_shrink

        if self.ray_train_config_shrink is not None:
            result['RayTrainConfig'] = self.ray_train_config_shrink

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.webserver_spec_name is not None:
            result['WebserverSpecName'] = self.webserver_spec_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DBClusterId') is not None:
            self.dbcluster_id = m.get('DBClusterId')

        if m.get('DeviceCount') is not None:
            self.device_count = m.get('DeviceCount')

        if m.get('PlatformName') is not None:
            self.platform_name = m.get('PlatformName')

        if m.get('RayConfig') is not None:
            self.ray_config_shrink = m.get('RayConfig')

        if m.get('RayTrainConfig') is not None:
            self.ray_train_config_shrink = m.get('RayTrainConfig')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('WebserverSpecName') is not None:
            self.webserver_spec_name = m.get('WebserverSpecName')

        return self

