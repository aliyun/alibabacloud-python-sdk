# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class DescribeLivePrivateLineAvailGAResponseBody(DaraModel):
    def __init__(
        self,
        live_private_line_avail_gas: main_models.DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAs = None,
        request_id: str = None,
    ):
        # The GA instance configuration details.
        self.live_private_line_avail_gas = live_private_line_avail_gas
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.live_private_line_avail_gas:
            self.live_private_line_avail_gas.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.live_private_line_avail_gas is not None:
            result['LivePrivateLineAvailGAs'] = self.live_private_line_avail_gas.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LivePrivateLineAvailGAs') is not None:
            temp_model = main_models.DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAs()
            self.live_private_line_avail_gas = temp_model.from_map(m.get('LivePrivateLineAvailGAs'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAs(DaraModel):
    def __init__(
        self,
        live_private_line_avail_ga: List[main_models.DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAsLivePrivateLineAvailGA] = None,
    ):
        self.live_private_line_avail_ga = live_private_line_avail_ga

    def validate(self):
        if self.live_private_line_avail_ga:
            for v1 in self.live_private_line_avail_ga:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LivePrivateLineAvailGA'] = []
        if self.live_private_line_avail_ga is not None:
            for k1 in self.live_private_line_avail_ga:
                result['LivePrivateLineAvailGA'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_private_line_avail_ga = []
        if m.get('LivePrivateLineAvailGA') is not None:
            for k1 in m.get('LivePrivateLineAvailGA'):
                temp_model = main_models.DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAsLivePrivateLineAvailGA()
                self.live_private_line_avail_ga.append(temp_model.from_map(k1))

        return self

class DescribeLivePrivateLineAvailGAResponseBodyLivePrivateLineAvailGAsLivePrivateLineAvailGA(DaraModel):
    def __init__(
        self,
        acceleration_area: str = None,
        acceleration_type: str = None,
        app_name: str = None,
        binding_status: str = None,
        domain_name: str = None,
        ip: str = None,
        instance_id: str = None,
        status: str = None,
        stream_name: str = None,
        uid: str = None,
        video_center: str = None,
    ):
        # The acceleration channel.
        self.acceleration_area = acceleration_area
        # The acceleration type. Valid values:
        # 
        # *   play: streaming acceleration
        # *   publish: stream ingest acceleration
        self.acceleration_type = acceleration_type
        # The name of the application.
        self.app_name = app_name
        # Indicates whether the GA instance is bound to an acceleration circuit. Valid values:
        # 
        # *   yes
        # *   no
        self.binding_status = binding_status
        # The main streaming domain.
        self.domain_name = domain_name
        # The accelerated IP address.
        self.ip = ip
        # The ID of the GA instance.
        self.instance_id = instance_id
        # The status of the GA instance. Valid values:
        # 
        # *   active: The GA instance is available.
        # *   inactive: The GA instance is unavailable.
        self.status = status
        # The name of the live stream.
        self.stream_name = stream_name
        # The user ID (UID).
        self.uid = uid
        # The live center.
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

        if self.binding_status is not None:
            result['BindingStatus'] = self.binding_status

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.ip is not None:
            result['IP'] = self.ip

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.status is not None:
            result['Status'] = self.status

        if self.stream_name is not None:
            result['StreamName'] = self.stream_name

        if self.uid is not None:
            result['Uid'] = self.uid

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

        if m.get('BindingStatus') is not None:
            self.binding_status = m.get('BindingStatus')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('IP') is not None:
            self.ip = m.get('IP')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StreamName') is not None:
            self.stream_name = m.get('StreamName')

        if m.get('Uid') is not None:
            self.uid = m.get('Uid')

        if m.get('VideoCenter') is not None:
            self.video_center = m.get('VideoCenter')

        return self

