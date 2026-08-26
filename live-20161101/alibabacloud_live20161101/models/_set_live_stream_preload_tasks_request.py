# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetLiveStreamPreloadTasksRequest(DaraModel):
    def __init__(
        self,
        area: str = None,
        domain_name: str = None,
        owner_id: int = None,
        play_url: str = None,
        preloaded_end_time: str = None,
        preloaded_start_time: str = None,
        region_id: str = None,
    ):
        # The prefetch area. Valid values:
        # - domestic: the Chinese mainland.
        # - overseas: outside the Chinese mainland, including Hong Kong (China), Macao (China), and Taiwan (China).
        # - global: global acceleration.
        #  
        # If you do not specify this parameter, the default prefetch area is the acceleration region configured for your domain name.
        self.area = area
        # The streaming domain.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        self.owner_id = owner_id
        # The live stream URLs. You can specify multiple URLs separated by commas (,). A maximum of 100 URLs can be specified.
        # 
        # This parameter is required.
        self.play_url = play_url
        # The end time of the prefetch task in UTC. Example: 2016-06-30T19:00:00Z. The interval between EndTime and StartTime cannot exceed 6 hours.
        self.preloaded_end_time = preloaded_end_time
        # The start time of the prefetch task in UTC. Example: 2016-06-29T19:00:00Z. If you do not specify this parameter, the default prefetch duration is 1 hour.
        self.preloaded_start_time = preloaded_start_time
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.area is not None:
            result['Area'] = self.area

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.play_url is not None:
            result['PlayUrl'] = self.play_url

        if self.preloaded_end_time is not None:
            result['PreloadedEndTime'] = self.preloaded_end_time

        if self.preloaded_start_time is not None:
            result['PreloadedStartTime'] = self.preloaded_start_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Area') is not None:
            self.area = m.get('Area')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('PlayUrl') is not None:
            self.play_url = m.get('PlayUrl')

        if m.get('PreloadedEndTime') is not None:
            self.preloaded_end_time = m.get('PreloadedEndTime')

        if m.get('PreloadedStartTime') is not None:
            self.preloaded_start_time = m.get('PreloadedStartTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        return self

