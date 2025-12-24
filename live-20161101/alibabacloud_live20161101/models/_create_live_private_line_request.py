# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateLivePrivateLineRequest(DaraModel):
    def __init__(
        self,
        acceleration_area: str = None,
        acceleration_type: str = None,
        app_name: str = None,
        domain_name: str = None,
        instance_id: str = None,
        max_bandwidth: str = None,
        owner_id: int = None,
        region_id: str = None,
        reuse: str = None,
        stream_name: str = None,
        video_center: str = None,
    ):
        # The acceleration channel.
        # 
        # This parameter is required.
        self.acceleration_area = acceleration_area
        # The acceleration type. Valid values:
        # 
        # *   play: streaming acceleration
        # *   publish: stream ingest acceleration
        # 
        # This parameter is required.
        self.acceleration_type = acceleration_type
        # The name of the application.
        # 
        # This parameter is required.
        self.app_name = app_name
        # The main streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # The acceleration channel that you want to reuse. This parameter is required if Reuse is set to yes.
        self.instance_id = instance_id
        # The accelerated bandwidth. Unit: Mbit/s. This parameter is required if Reuse is set to no.
        self.max_bandwidth = max_bandwidth
        self.owner_id = owner_id
        self.region_id = region_id
        # Specifies whether to reuse an existing acceleration channel. Valid values:
        # 
        # *   yes: reuses an existing acceleration channel.
        # *   no: creates a new acceleration channel.
        # 
        # This parameter is required.
        self.reuse = reuse
        # The name of the live stream.
        # 
        # This parameter is required.
        self.stream_name = stream_name
        # The live center. Valid values: cn-beijing, cn-shanghai, cn-shenzhen, cn-qingdao, ap-northeast-1, ap-southeast-5, eu-central-1, and ap-southeast-1, which indicate China (Beijing), China (Shanghai), China (Shenzhen), China (Qingdao), Japan (Tokyo), Indonesia (Jakarta), Germany (Frankfurt), and Singapore, respectively.
        # 
        # This parameter is required.
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

        if self.acceleration_type is not None:
            result['AccelerationType'] = self.acceleration_type

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.max_bandwidth is not None:
            result['MaxBandwidth'] = self.max_bandwidth

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.reuse is not None:
            result['Reuse'] = self.reuse

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.video_center is not None:
            result['VideoCenter'] = self.video_center

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccelerationArea') is not None:
            self.acceleration_area = m.get('AccelerationArea')

        if m.get('AccelerationType') is not None:
            self.acceleration_type = m.get('AccelerationType')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('MaxBandwidth') is not None:
            self.max_bandwidth = m.get('MaxBandwidth')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Reuse') is not None:
            self.reuse = m.get('Reuse')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('VideoCenter') is not None:
            self.video_center = m.get('VideoCenter')

        return self

