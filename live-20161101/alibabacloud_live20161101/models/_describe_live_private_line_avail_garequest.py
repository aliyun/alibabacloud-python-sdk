# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLivePrivateLineAvailGARequest(DaraModel):
    def __init__(
        self,
        acceleration_area: str = None,
        app_name: str = None,
        domain_name: str = None,
        is_ga_instance: str = None,
        owner_id: int = None,
        region_id: str = None,
        stream_name: str = None,
        video_center: str = None,
    ):
        # The acceleration channel.
        self.acceleration_area = acceleration_area
        # The name of the application.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # Specifies whether to query Global Accelerator (GA) instances. Valid values:
        # 
        # *   yes: queries the status of GA instances.
        # *   no: queries the binding information between GA instances and acceleration circuits.
        # 
        # This parameter is required.
        self.is_ga_instance = is_ga_instance
        self.owner_id = owner_id
        self.region_id = region_id
        # The name of the live stream.
        self.stream_name = stream_name
        # The live center. Valid values: cn-beijing, cn-shanghai, cn-shenzhen, cn-qingdao, ap-northeast-1, ap-southeast-5, eu-central-1, ap-southeast-1, and ap-south-1. cn-beijing indicates China (Beijing). cn-shanghai indicates China (Shanghai). cn-shenzhen indicates China (Shenzhen). cn-qingdao indicates China (Qingdao). ap-northeast-1 indicates Japan (Tokyo). ap-southeast-5 indicates Indonesia (Jakarta). eu-central-1 indicates Germany (Frankfurt). ap-southeast-1 indicates Singapore.
        self.video_center = video_center

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acceleration_area is not None:
            result['AccelerationArea'] = self.acceleration_area

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.is_ga_instance is not None:
            result['IsGaInstance'] = self.is_ga_instance

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.video_center is not None:
            result['VideoCenter'] = self.video_center

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationArea') is not None:
            self.acceleration_area = m.get('AccelerationArea')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IsGaInstance') is not None:
            self.is_ga_instance = m.get('IsGaInstance')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('VideoCenter') is not None:
            self.video_center = m.get('VideoCenter')

        return self

